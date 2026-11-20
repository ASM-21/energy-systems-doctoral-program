"""Single-period economic dispatch teaching model.

Synthetic single-node linear program; not a production-cost model or a real
RTO/ISO market representation.
"""
from __future__ import annotations

import argparse
import csv
from pathlib import Path
from typing import Iterable

import numpy as np
from scipy.optimize import linprog


def load_generators(path: str | Path) -> list[dict]:
    with open(path, newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    units = [
        {
            "name": row["name"],
            "marginal_cost": float(row["marginal_cost_usd_per_mwh"]),
            "capacity": float(row["capacity_mw"]),
            "emissions_rate": float(row["emissions_tco2_per_mwh"]),
        }
        for row in rows
    ]
    if not units:
        raise ValueError("Generator input must contain at least one unit.")
    if any(u["capacity"] < 0 or u["marginal_cost"] < 0 for u in units):
        raise ValueError("Capacity and marginal cost must be nonnegative.")
    if any(u["emissions_rate"] < 0 for u in units):
        raise ValueError("Emissions rates must be nonnegative.")
    return units


def solve_dispatch(units: Iterable[dict], demand_mw: float) -> dict:
    units = list(units)
    if not units:
        raise ValueError("At least one generator is required.")
    if demand_mw < 0:
        raise ValueError("Demand must be nonnegative.")
    total_capacity = sum(float(u["capacity"]) for u in units)
    if demand_mw > total_capacity:
        raise ValueError(
            f"Infeasible demand: {demand_mw:g} MW exceeds "
            f"total capacity {total_capacity:g} MW."
        )

    costs = np.array([float(u["marginal_cost"]) for u in units])
    capacities = [(0.0, float(u["capacity"])) for u in units]
    result = linprog(
        c=costs,
        A_eq=np.ones((1, len(units))),
        b_eq=[float(demand_mw)],
        bounds=capacities,
        method="highs",
    )
    if not result.success:
        raise RuntimeError(f"Optimization failed: {result.message}")

    dispatch = [
        {
            "name": unit["name"],
            "generation_mw": float(p),
            "capacity_mw": float(unit["capacity"]),
            "marginal_cost_usd_per_mwh": float(unit["marginal_cost"]),
            "emissions_tco2": float(p) * float(unit["emissions_rate"]),
        }
        for unit, p in zip(units, result.x)
    ]
    return {
        "demand_mw": float(demand_mw),
        "total_cost_usd_per_hour": float(result.fun),
        "marginal_price_usd_per_mwh": float(result.eqlin.marginals[0]),
        "total_emissions_tco2_per_hour": sum(
            row["emissions_tco2"] for row in dispatch
        ),
        "dispatch": dispatch,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--demand", type=float, default=1000.0, help="Demand in MW")
    parser.add_argument(
        "--generators",
        type=Path,
        default=Path(__file__).parent / "data" / "generators.csv",
        help="Generator CSV path",
    )
    args = parser.parse_args()

    result = solve_dispatch(load_generators(args.generators), args.demand)
    print(f"Demand: {result['demand_mw']:.1f} MW")
    print(f"Variable cost: ${result['total_cost_usd_per_hour']:,.2f}/hour")
    print(f"Energy-balance dual: ${result['marginal_price_usd_per_mwh']:.2f}/MWh")
    print(f"Emissions: {result['total_emissions_tco2_per_hour']:.2f} tCO2/hour")
    print("\nDispatch:")
    for row in result["dispatch"]:
        print(
            f"  {row['name']}: {row['generation_mw']:.1f} / "
            f"{row['capacity_mw']:.1f} MW"
        )


if __name__ == "__main__":
    main()
