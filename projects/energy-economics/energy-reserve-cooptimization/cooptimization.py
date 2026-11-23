"""Single-period energy and upward-reserve co-optimization LP.

Synthetic three-generator teaching model. It is not a PJM market simulator.
"""
from __future__ import annotations

from math import isfinite
from typing import Iterable

from scipy.optimize import linprog


DEFAULT_UNITS = [
    {"name": "A", "energy_offer": 18.0, "reserve_offer": 8.0, "capacity": 80.0},
    {"name": "B", "energy_offer": 32.0, "reserve_offer": 5.0, "capacity": 70.0},
    {"name": "C", "energy_offer": 55.0, "reserve_offer": 2.0, "capacity": 50.0},
]


def _validate(units: list[dict], demand_mw: float, reserve_mw: float) -> None:
    if not units:
        raise ValueError("At least one generator is required.")
    if not isfinite(demand_mw) or not isfinite(reserve_mw):
        raise ValueError("Demand and reserve requirement must be finite.")
    if demand_mw < 0 or reserve_mw < 0:
        raise ValueError("Demand and reserve requirement must be nonnegative.")
    names = set()
    for unit in units:
        name = str(unit["name"])
        if name in names:
            raise ValueError(f"Duplicate generator name: {name}")
        names.add(name)
        for field in ("energy_offer", "reserve_offer", "capacity"):
            value = float(unit[field])
            if not isfinite(value) or value < 0:
                raise ValueError(f"{field} for {name} must be finite and nonnegative.")
    total_capacity = sum(float(unit["capacity"]) for unit in units)
    if demand_mw + reserve_mw > total_capacity + 1e-9:
        raise ValueError(
            "Infeasible requirement: energy demand plus upward reserve "
            "exceeds total generator capacity."
        )


def solve_cooptimization(
    units: Iterable[dict] = DEFAULT_UNITS,
    demand_mw: float = 160.0,
    reserve_mw: float = 20.0,
) -> dict:
    """Solve energy and upward reserve together for one modeled hour.

    The reserve dual is reported as a positive marginal value. SciPy's
    inequality row is -sum(reserve) <= -reserve_requirement, so the
    corresponding marginal is negated to obtain the positive value.
    """
    units = [dict(unit) for unit in units]
    _validate(units, float(demand_mw), float(reserve_mw))
    n = len(units)

    # Decision order: p_1,...,p_n,r_1,...,r_n.
    objective = (
        [float(unit["energy_offer"]) for unit in units]
        + [float(unit["reserve_offer"]) for unit in units]
    )
    capacity_rows = []
    for i in range(n):
        row = [0.0] * (2 * n)
        row[i] = 1.0
        row[n + i] = 1.0
        capacity_rows.append(row)

    result = linprog(
        c=objective,
        A_ub=[[0.0] * n + [-1.0] * n] + capacity_rows,
        b_ub=[-float(reserve_mw)] + [float(unit["capacity"]) for unit in units],
        A_eq=[[1.0] * n + [0.0] * n],
        b_eq=[float(demand_mw)],
        bounds=[(0.0, None)] * (2 * n),
        method="highs",
    )
    if not result.success:
        raise RuntimeError(f"Optimization failed: {result.message}")

    energy = result.x[:n]
    reserve = result.x[n:]
    rows = []
    for i, unit in enumerate(units):
        rows.append({
            "name": str(unit["name"]),
            "energy_mw": float(energy[i]),
            "reserve_mw": float(reserve[i]),
            "total_award_mw": float(energy[i] + reserve[i]),
            "capacity_mw": float(unit["capacity"]),
            "energy_offer_usd_per_mwh": float(unit["energy_offer"]),
            "reserve_offer_usd_per_mw_h": float(unit["reserve_offer"]),
            "capacity_shadow_value_usd_per_mw_h": float(-result.ineqlin.marginals[i + 1]),
            "capacity_binding": abs(
                energy[i] + reserve[i] - float(unit["capacity"])
            ) <= 1e-7,
        })

    return {
        "demand_mw": float(demand_mw),
        "reserve_requirement_mw": float(reserve_mw),
        "energy_dispatch_mw": float(sum(energy)),
        "reserve_awarded_mw": float(sum(reserve)),
        "objective_usd_for_interval": float(result.fun),
        "energy_balance_dual_usd_per_mwh": float(result.eqlin.marginals[0]),
        "reserve_requirement_dual_usd_per_mw_h": float(-result.ineqlin.marginals[0]),
        "units": rows,
        "solver_status": result.message,
    }


def main() -> None:
    result = solve_cooptimization()
    print("Energy demand: {:.1f} MW".format(result["demand_mw"]))
    print("Upward reserve requirement: {:.1f} MW".format(result["reserve_requirement_mw"]))
    print("Objective: USD {:.2f} for the one-hour interval".format(result["objective_usd_for_interval"]))
    print("Energy-balance dual: USD {:.2f}/MWh".format(result["energy_balance_dual_usd_per_mwh"]))
    print("Reserve-requirement marginal value: USD {:.2f}/(MW·h)".format(result["reserve_requirement_dual_usd_per_mw_h"]))
    print("\nDispatch:")
    for unit in result["units"]:
        print(
            "  {}: energy {:.1f} MW, reserve {:.1f} MW, capacity {:.1f} MW".format(
                unit["name"], unit["energy_mw"], unit["reserve_mw"], unit["capacity_mw"]
            )
        )


if __name__ == "__main__":
    main()
