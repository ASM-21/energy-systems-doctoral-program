"""Single-period economic dispatch with carbon pricing and flexible demand.

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
    units = [{
        "name": row["name"],
        "marginal_cost": float(row["marginal_cost_usd_per_mwh"]),
        "capacity": float(row["capacity_mw"]),
        "emissions_rate": float(row["emissions_tco2_per_mwh"]),
    } for row in rows]
    if not units:
        raise ValueError("Generator input must contain at least one unit.")
    if any(u["capacity"] < 0 or u["marginal_cost"] < 0 for u in units):
        raise ValueError("Capacity and marginal cost must be nonnegative.")
    if any(u["emissions_rate"] < 0 for u in units):
        raise ValueError("Emissions rates must be nonnegative.")
    return units


def solve_dispatch(
    units: Iterable[dict],
    demand_mw: float,
    carbon_price_usd_per_tco2: float = 0.0,
    demand_response_max_mw: float = 0.0,
    demand_response_cost_usd_per_mwh: float = 1000.0,
) -> dict:
    """Minimize fuel cost + carbon payment + flexible-demand reduction cost.

    Demand response is a controllable reduction in one-hour demand with an
    explicit compensation/opportunity-cost parameter, not involuntary shedding.
    """
    units = list(units)
    if not units:
        raise ValueError("At least one generator is required.")
    if demand_mw < 0:
        raise ValueError("Demand must be nonnegative.")
    if carbon_price_usd_per_tco2 < 0:
        raise ValueError("Carbon price must be nonnegative.")
    if demand_response_max_mw < 0 or demand_response_cost_usd_per_mwh < 0:
        raise ValueError("Demand-response capacity and cost must be nonnegative.")

    total_capacity = sum(float(u["capacity"]) for u in units)
    if demand_mw > total_capacity + demand_response_max_mw:
        raise ValueError(
            f"Infeasible demand: {demand_mw:g} MW exceeds generation plus "
            f"demand-response capability {total_capacity + demand_response_max_mw:g} MW."
        )

    fuel_costs = np.array([float(u["marginal_cost"]) for u in units])
    emissions_rates = np.array([float(u["emissions_rate"]) for u in units])
    effective_costs = fuel_costs + carbon_price_usd_per_tco2 * emissions_rates
    objective = np.append(effective_costs, demand_response_cost_usd_per_mwh)
    bounds = [(0.0, float(u["capacity"])) for u in units]
    bounds.append((0.0, float(demand_response_max_mw)))
    result = linprog(
        c=objective,
        A_eq=np.ones((1, len(units) + 1)),
        b_eq=[float(demand_mw)],
        bounds=bounds,
        method="highs",
    )
    if not result.success:
        raise RuntimeError(f"Optimization failed: {result.message}")

    generation = result.x[:len(units)]
    dr_mw = float(result.x[-1])
    dispatch = [{
        "name": unit["name"],
        "generation_mw": float(p),
        "capacity_mw": float(unit["capacity"]),
        "marginal_cost_usd_per_mwh": float(unit["marginal_cost"]),
        "effective_marginal_cost_usd_per_mwh": float(
            unit["marginal_cost"] + carbon_price_usd_per_tco2 * unit["emissions_rate"]
        ),
        "emissions_tco2_per_hour": float(p) * float(unit["emissions_rate"]),
    } for unit, p in zip(units, generation)]
    fuel_cost = float(np.dot(fuel_costs, generation))
    emissions = float(sum(row["emissions_tco2_per_hour"] for row in dispatch))
    carbon_cost = float(carbon_price_usd_per_tco2 * emissions)
    dr_cost = float(dr_mw * demand_response_cost_usd_per_mwh)
    return {
        "demand_mw": float(demand_mw),
        "served_demand_mw": float(demand_mw - dr_mw),
        "demand_response_mw": dr_mw,
        "total_cost_usd_per_hour": float(result.fun),
        "fuel_cost_usd_per_hour": fuel_cost,
        "carbon_cost_usd_per_hour": carbon_cost,
        "demand_response_cost_usd_per_hour": dr_cost,
        "carbon_price_usd_per_tco2": float(carbon_price_usd_per_tco2),
        "marginal_price_usd_per_mwh": float(result.eqlin.marginals[0]),
        "total_emissions_tco2_per_hour": emissions,
        "dispatch": dispatch,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--demand", type=float, default=1000.0, help="Demand in MW")
    parser.add_argument(
        "--generators", type=Path,
        default=Path(__file__).parent / "data" / "generators.csv",
        help="Generator CSV path",
    )
    parser.add_argument("--carbon-price", type=float, default=0.0, help="USD/tCO2")
    parser.add_argument("--demand-response-max", type=float, default=0.0, help="MW")
    parser.add_argument("--demand-response-cost", type=float, default=1000.0,
                        help="Demand-response compensation/opportunity cost in USD/MWh")
    args = parser.parse_args()
    result = solve_dispatch(
        load_generators(args.generators), args.demand,
        carbon_price_usd_per_tco2=args.carbon_price,
        demand_response_max_mw=args.demand_response_max,
        demand_response_cost_usd_per_mwh=args.demand_response_cost,
    )
    print(f"Demand: {result['demand_mw']:.1f} MW")
    print(f"Served demand: {result['served_demand_mw']:.1f} MW")
    print(f"Demand response: {result['demand_response_mw']:.1f} MW")
    print(f"Objective cost: {result['total_cost_usd_per_hour']:,.2f} USD/hour")
    print(f"  Fuel cost: {result['fuel_cost_usd_per_hour']:,.2f} USD/hour")
    print(f"  Carbon cost: {result['carbon_cost_usd_per_hour']:,.2f} USD/hour")
    print(f"  Demand-response cost: {result['demand_response_cost_usd_per_hour']:,.2f} USD/hour")
    print(f"Marginal price: {result['marginal_price_usd_per_mwh']:.2f} USD/MWh")
    print(f"Emissions: {result['total_emissions_tco2_per_hour']:.2f} tCO2/hour")
    print("\nDispatch:")
    for row in result["dispatch"]:
        print(f"  {row['name']}: {row['generation_mw']:.1f} / {row['capacity_mw']:.1f} MW")


if __name__ == "__main__":
    main()
