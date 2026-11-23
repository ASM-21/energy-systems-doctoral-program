"""Two-period mixed-integer unit commitment teaching model."""
from __future__ import annotations

import argparse
import json
import math
from typing import Mapping, Sequence

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp


DEFAULT_UNITS = [
    {"name": "G1", "energy_offer": 20.0, "minimum_mw": 30.0, "maximum_mw": 100.0,
     "no_load_cost": 100.0, "startup_cost": 500.0},
    {"name": "G2", "energy_offer": 50.0, "minimum_mw": 0.0, "maximum_mw": 100.0,
     "no_load_cost": 40.0, "startup_cost": 100.0},
]


def _finite_nonnegative(value: float, label: str) -> float:
    value = float(value)
    if not math.isfinite(value) or value < 0:
        raise ValueError(f"{label} must be finite and nonnegative")
    return value


def solve_unit_commitment(
    demand_mw: Sequence[float] = (80.0, 150.0),
    units: Sequence[Mapping[str, float | str]] = DEFAULT_UNITS,
    initial_on: Sequence[int] | None = None,
    relax_commitment: bool = False,
) -> dict:
    """Solve a deterministic unit commitment MILP or its LP relaxation.

    No ramping, minimum up/down times, reserves, network constraints,
    startup trajectories, or uncertainty are modeled.
    """
    demand = [_finite_nonnegative(v, "demand") for v in demand_mw]
    if not demand:
        raise ValueError("At least one demand period is required")
    units = [dict(unit) for unit in units]
    if not units:
        raise ValueError("At least one generator is required")
    names = [str(unit["name"]) for unit in units]
    if len(names) != len(set(names)):
        raise ValueError("Generator names must be unique")
    n, t_count = len(units), len(demand)
    initial = [0] * n if initial_on is None else list(initial_on)
    if len(initial) != n or any(v not in (0, 1) for v in initial):
        raise ValueError("initial_on must contain one binary value per unit")

    energy, minimum, maximum, no_load, startup = [], [], [], [], []
    for unit in units:
        energy.append(_finite_nonnegative(unit["energy_offer"], "energy_offer"))
        minimum.append(_finite_nonnegative(unit["minimum_mw"], "minimum_mw"))
        maximum.append(_finite_nonnegative(unit["maximum_mw"], "maximum_mw"))
        no_load.append(_finite_nonnegative(unit["no_load_cost"], "no_load_cost"))
        startup.append(_finite_nonnegative(unit["startup_cost"], "startup_cost"))
    if any(lo > hi for lo, hi in zip(minimum, maximum)):
        raise ValueError("Minimum output cannot exceed maximum output")
    if max(maximum) <= 0:
        raise ValueError("At least one generator must have positive capacity")

    # Flatten in blocks: p[i,t], y[i,t], u[i,t].
    p_count = n * t_count
    y_offset, u_offset = p_count, 2 * p_count
    variable_count = 3 * p_count

    def idx(block_offset: int, i: int, t: int) -> int:
        return block_offset + i * t_count + t

    objective = np.zeros(variable_count)
    lower = np.zeros(variable_count)
    upper = np.full(variable_count, np.inf)
    integrality = np.zeros(variable_count, dtype=int)
    for i in range(n):
        for t in range(t_count):
            objective[idx(0, i, t)] = energy[i]
            objective[idx(y_offset, i, t)] = no_load[i]
            objective[idx(u_offset, i, t)] = startup[i]
            upper[idx(y_offset, i, t)] = 1.0
            upper[idx(u_offset, i, t)] = 1.0
            if not relax_commitment:
                integrality[idx(y_offset, i, t)] = 1

    rows, row_lb, row_ub = [], [], []
    # Energy balance equalities.
    for t in range(t_count):
        row = np.zeros(variable_count)
        for i in range(n):
            row[idx(0, i, t)] = 1.0
        rows.append(row)
        row_lb.append(demand[t])
        row_ub.append(demand[t])

    # Commitment-linked output and startup logic.
    for i in range(n):
        for t in range(t_count):
            # p <= Pmax*y
            row = np.zeros(variable_count)
            row[idx(0, i, t)] = 1.0
            row[idx(y_offset, i, t)] = -maximum[i]
            rows.append(row)
            row_lb.append(-np.inf)
            row_ub.append(0.0)

            # p >= Pmin*y
            row = np.zeros(variable_count)
            row[idx(0, i, t)] = -1.0
            row[idx(y_offset, i, t)] = minimum[i]
            rows.append(row)
            row_lb.append(-np.inf)
            row_ub.append(0.0)

            # y_t - y_(t-1) - u_t <= 0
            row = np.zeros(variable_count)
            row[idx(y_offset, i, t)] = 1.0
            row[idx(u_offset, i, t)] = -1.0
            if t == 0:
                row_ub_value = float(initial[i])
            else:
                row[idx(y_offset, i, t - 1)] = -1.0
                row_ub_value = 0.0
            rows.append(row)
            row_lb.append(-np.inf)
            row_ub.append(row_ub_value)

    result = milp(
        c=objective,
        integrality=integrality,
        bounds=Bounds(lower, upper),
        constraints=LinearConstraint(np.asarray(rows), np.asarray(row_lb), np.asarray(row_ub)),
    )
    if not result.success:
        raise ValueError(f"Unit commitment did not solve: {result.message}")

    schedules = []
    energy_cost_total = no_load_total = startup_total = 0.0
    for i, name in enumerate(names):
        periods = []
        for t in range(t_count):
            p = float(result.x[idx(0, i, t)])
            y = float(result.x[idx(y_offset, i, t)])
            u = float(result.x[idx(u_offset, i, t)])
            energy_cost_total += p * energy[i]
            no_load_total += y * no_load[i]
            startup_total += u * startup[i]
            periods.append({"period": t + 1, "dispatch_mw": p, "commitment": y, "startup": u})
        schedules.append({"name": name, "periods": periods})
    return {
        "demand_mw": demand,
        "schedules": schedules,
        "energy_cost": energy_cost_total,
        "no_load_cost": no_load_total,
        "startup_cost": startup_total,
        "objective": float(result.fun),
        "relaxed": bool(relax_commitment),
        "solver_status": result.message,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--relax-commitment", action="store_true")
    parser.add_argument("--g1-startup-cost", type=float, default=500.0)
    parser.add_argument("--period-2-demand", type=float, default=150.0)
    parser.add_argument("--output-json")
    args = parser.parse_args()
    units = [dict(unit) for unit in DEFAULT_UNITS]
    units[0]["startup_cost"] = args.g1_startup_cost
    result = solve_unit_commitment(
        demand_mw=(80.0, args.period_2_demand),
        units=units,
        relax_commitment=args.relax_commitment,
    )
    rendered = json.dumps(result, indent=2, sort_keys=True)
    if args.output_json:
        with open(args.output_json, "w", encoding="utf-8") as output:
            output.write(rendered + "\n")
    print(rendered)


if __name__ == "__main__":
    main()
