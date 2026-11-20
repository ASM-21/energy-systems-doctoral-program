"""Lossless two-node economic dispatch LP with nodal balance duals."""
from __future__ import annotations

import argparse
from scipy.optimize import linprog


def solve_two_node(line_limit_mw: float = 50.0) -> dict:
    if line_limit_mw < 0:
        raise ValueError("Line limit must be nonnegative.")

    # Variables: [generation at node 1, generation at node 2, flow 1 -> 2].
    # Nodal balances: g1 - f = demand1; g2 + f = demand2.
    result = linprog(
        c=[20.0, 70.0, 0.0],
        A_eq=[[1.0, 0.0, -1.0], [0.0, 1.0, 1.0]],
        b_eq=[100.0, 100.0],
        bounds=[(0.0, 150.0), (0.0, 150.0), (-line_limit_mw, line_limit_mw)],
        method="highs",
    )
    if not result.success:
        raise RuntimeError(result.message)

    return {
        "generation_node_1_mw": float(result.x[0]),
        "generation_node_2_mw": float(result.x[1]),
        "flow_node_1_to_2_mw": float(result.x[2]),
        "total_cost_usd_per_hour": float(result.fun),
        "price_node_1_usd_per_mwh": float(result.eqlin.marginals[0]),
        "price_node_2_usd_per_mwh": float(result.eqlin.marginals[1]),
        "line_limit_mw": float(line_limit_mw),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--line-limit", type=float, default=50.0)
    args = parser.parse_args()
    result = solve_two_node(args.line_limit)
    for key, value in result.items():
        print(f"{key}: {value:.3f}")


if __name__ == "__main__":
    main()
