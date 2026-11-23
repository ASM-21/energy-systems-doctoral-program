"""Three-bus lossless DC optimal power flow teaching model."""
from __future__ import annotations

import argparse
import json
import math
from typing import Sequence

import numpy as np
from scipy.optimize import linprog


def _positive_finite(value: float, name: str) -> float:
    value = float(value)
    if not math.isfinite(value) or value <= 0:
        raise ValueError(f"{name} must be finite and positive")
    return value


def _nonnegative_finite(value: float, name: str) -> float:
    value = float(value)
    if not math.isfinite(value) or value < 0:
        raise ValueError(f"{name} must be finite and nonnegative")
    return value


def solve_dc_opf(
    demand_bus_2_mw: float = 100.0,
    demand_bus_3_mw: float = 100.0,
    line_12_limit_mw: float = 60.0,
    line_13_limit_mw: float = 60.0,
    line_23_limit_mw: float = 60.0,
    base_mva: float = 100.0,
    x_12_pu: float = 0.10,
    x_13_pu: float = 0.20,
    x_23_pu: float = 0.10,
    generator_costs: Sequence[float] = (20.0, 50.0, 80.0),
    generator_capacities_mw: Sequence[float] = (150.0, 100.0, 100.0),
) -> dict[str, float | dict[str, float]]:
    """Solve DC-OPF with bus 1 as angle reference.

    Decision variables are [g1, g2, g3, theta2, theta3]. Flows are
    oriented 1->2, 1->3, and 2->3. Losses, reactive power, reserves,
    contingencies, and unit commitment are omitted.
    """
    demand2 = _nonnegative_finite(demand_bus_2_mw, "demand_bus_2_mw")
    demand3 = _nonnegative_finite(demand_bus_3_mw, "demand_bus_3_mw")
    limits = [
        _positive_finite(line_12_limit_mw, "line_12_limit_mw"),
        _positive_finite(line_13_limit_mw, "line_13_limit_mw"),
        _positive_finite(line_23_limit_mw, "line_23_limit_mw"),
    ]
    base = _positive_finite(base_mva, "base_mva")
    reactances = [
        _positive_finite(x_12_pu, "x_12_pu"),
        _positive_finite(x_13_pu, "x_13_pu"),
        _positive_finite(x_23_pu, "x_23_pu"),
    ]
    if len(generator_costs) != 3 or len(generator_capacities_mw) != 3:
        raise ValueError("Exactly three generator costs and capacities are required")
    costs = [_nonnegative_finite(v, f"generator_cost_{i+1}") for i, v in enumerate(generator_costs)]
    capacities = [_positive_finite(v, f"generator_capacity_{i+1}") for i, v in enumerate(generator_capacities_mw)]

    b12, b13, b23 = (1.0 / x for x in reactances)
    # B' rows are buses 1, 2, 3; columns below omit reference angle theta1=0.
    b_reduced_columns = np.array([
        [-b12, -b13],
        [b12 + b23, -b23],
        [-b23, b13 + b23],
    ], dtype=float)

    a_eq = np.zeros((3, 5), dtype=float)
    a_eq[:, :3] = np.eye(3)
    a_eq[:, 3:] = -base * b_reduced_columns
    b_eq = np.array([0.0, demand2, demand3], dtype=float)

    # Flow rows in [theta2, theta3] coordinates, including system base.
    flow_rows = np.array([
        [-base / reactances[0], 0.0],
        [0.0, -base / reactances[1]],
        [base / reactances[2], -base / reactances[2]],
    ], dtype=float)
    a_ub = np.zeros((6, 5), dtype=float)
    b_ub = np.repeat(np.asarray(limits, dtype=float), 2)
    for branch in range(3):
        a_ub[2 * branch, 3:] = flow_rows[branch]
        a_ub[2 * branch + 1, 3:] = -flow_rows[branch]

    result = linprog(
        c=np.asarray(costs + [0.0, 0.0], dtype=float),
        A_ub=a_ub,
        b_ub=b_ub,
        A_eq=a_eq,
        b_eq=b_eq,
        bounds=[(0.0, cap) for cap in capacities] + [(None, None), (None, None)],
        method="highs",
    )
    if not result.success:
        raise ValueError(f"DC-OPF did not solve: {result.message}")

    g1, g2, g3, theta2, theta3 = map(float, result.x)
    theta = [0.0, theta2, theta3]
    flows = {
        "flow_12_mw": base * (theta[0] - theta[1]) / reactances[0],
        "flow_13_mw": base * (theta[0] - theta[2]) / reactances[1],
        "flow_23_mw": base * (theta[1] - theta[2]) / reactances[2],
    }
    nodal_prices = {
        "lmp_bus_1_usd_per_mwh": float(result.eqlin.marginals[0]),
        "lmp_bus_2_usd_per_mwh": float(result.eqlin.marginals[1]),
        "lmp_bus_3_usd_per_mwh": float(result.eqlin.marginals[2]),
    }
    line_shadow_values = {
        "line_12_upper_shadow_usd_per_mw_hour": max(0.0, -float(result.ineqlin.marginals[0])),
        "line_12_lower_shadow_usd_per_mw_hour": max(0.0, -float(result.ineqlin.marginals[1])),
        "line_13_upper_shadow_usd_per_mw_hour": max(0.0, -float(result.ineqlin.marginals[2])),
        "line_13_lower_shadow_usd_per_mw_hour": max(0.0, -float(result.ineqlin.marginals[3])),
        "line_23_upper_shadow_usd_per_mw_hour": max(0.0, -float(result.ineqlin.marginals[4])),
        "line_23_lower_shadow_usd_per_mw_hour": max(0.0, -float(result.ineqlin.marginals[5])),
    }
    return {
        "generation_mw": {"g1_bus_1": g1, "g2_bus_2": g2, "g3_bus_3": g3},
        "angles_rad": {"bus_1": 0.0, "bus_2": theta2, "bus_3": theta3},
        "flows_mw": flows,
        "nodal_prices_usd_per_mwh": nodal_prices,
        "line_shadow_values": line_shadow_values,
        "objective_usd_per_hour": float(result.fun),
        "total_demand_mw": demand2 + demand3,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--line-12-limit", type=float, default=60.0)
    parser.add_argument("--output-json", help="Optional output JSON path")
    args = parser.parse_args()
    result = solve_dc_opf(line_12_limit_mw=args.line_12_limit)
    rendered = json.dumps(result, indent=2, sort_keys=True)
    if args.output_json:
        with open(args.output_json, "w", encoding="utf-8") as output:
            output.write(rendered + "\n")
    print(rendered)


if __name__ == "__main__":
    main()
