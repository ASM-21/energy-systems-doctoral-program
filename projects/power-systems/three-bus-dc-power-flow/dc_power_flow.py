"""Small transparent DC power-flow solver using per-unit branch reactances."""
from __future__ import annotations

import csv
from pathlib import Path


def load_case(data_dir: str | Path) -> tuple[dict[int, float], list[dict]]:
    data_dir = Path(data_dir)
    with (data_dir / "buses.csv").open(newline="", encoding="utf-8") as handle:
        buses = {
            int(row["bus_id"]): float(row["injection_mw"])
            for row in csv.DictReader(handle)
        }
    with (data_dir / "lines.csv").open(newline="", encoding="utf-8") as handle:
        lines = [
            {
                "from_bus": int(row["from_bus"]),
                "to_bus": int(row["to_bus"]),
                "x_pu": float(row["x_pu"]),
                "limit_mw": float(row["limit_mw"]) if row["limit_mw"] else None,
            }
            for row in csv.DictReader(handle)
        ]
    return buses, lines


def solve_dc_power_flow(
    injections_mw: dict[int, float],
    lines: list[dict],
    base_mva: float = 100.0,
    slack_bus: int | None = None,
    tolerance: float = 1e-8,
) -> dict:
    if len(injections_mw) < 2:
        raise ValueError("At least two buses are required.")
    if base_mva <= 0:
        raise ValueError("Base MVA must be positive.")
    buses = sorted(injections_mw)
    if slack_bus is None:
        slack_bus = buses[0]
    if slack_bus not in injections_mw:
        raise ValueError("Slack bus must exist in the bus injection map.")
    if abs(sum(injections_mw.values())) > tolerance:
        raise ValueError("Net active-power injections must sum to zero.")
    if not lines:
        raise ValueError("At least one branch is required.")

    index = {bus: i for i, bus in enumerate(buses)}
    b_matrix = [[0.0 for _ in buses] for _ in buses]
    seen = set()
    for line in lines:
        i_bus, j_bus = line["from_bus"], line["to_bus"]
        x = float(line["x_pu"])
        if i_bus not in index or j_bus not in index or i_bus == j_bus:
            raise ValueError("Each line must connect two distinct known buses.")
        if x <= 0:
            raise ValueError("Branch reactance must be positive.")
        key = tuple(sorted((i_bus, j_bus)))
        if key in seen:
            raise ValueError("Parallel branches are not supported in this lab.")
        seen.add(key)
        susceptance = 1.0 / x
        i, j = index[i_bus], index[j_bus]
        b_matrix[i][i] += susceptance
        b_matrix[j][j] += susceptance
        b_matrix[i][j] -= susceptance
        b_matrix[j][i] -= susceptance

    slack_index = index[slack_bus]
    retained = [i for i in range(len(buses)) if i != slack_index]
    reduced = [[b_matrix[i][j] for j in retained] for i in retained]
    injections_pu = [injections_mw[bus] / base_mva for bus in buses]
    rhs = [injections_pu[i] for i in retained]

    # Gaussian elimination with partial pivoting for a small educational matrix.
    matrix = [row[:] + [rhs[k]] for k, row in enumerate(reduced)]
    n = len(matrix)
    for col in range(n):
        pivot = max(range(col, n), key=lambda row: abs(matrix[row][col]))
        if abs(matrix[pivot][col]) < tolerance:
            raise ValueError("Network susceptance matrix is singular; check connectivity.")
        matrix[col], matrix[pivot] = matrix[pivot], matrix[col]
        pivot_value = matrix[col][col]
        matrix[col] = [value / pivot_value for value in matrix[col]]
        for row in range(n):
            if row == col:
                continue
            factor = matrix[row][col]
            matrix[row] = [
                matrix[row][k] - factor * matrix[col][k]
                for k in range(n + 1)
            ]

    angles = {slack_bus: 0.0}
    for k, i in enumerate(retained):
        angles[buses[i]] = matrix[k][-1]

    branch_results = []
    for line in lines:
        i_bus, j_bus = line["from_bus"], line["to_bus"]
        flow = (angles[i_bus] - angles[j_bus]) / line["x_pu"] * base_mva
        limit = line["limit_mw"]
        branch_results.append(
            {
                "from_bus": i_bus,
                "to_bus": j_bus,
                "flow_mw": float(flow),
                "limit_mw": limit,
                "limit_violated": bool(limit is not None and abs(flow) > limit + tolerance),
            }
        )

    return {
        "base_mva": float(base_mva),
        "slack_bus": slack_bus,
        "angles_rad": angles,
        "line_flows": branch_results,
        "net_injection_mw": float(sum(injections_mw.values())),
    }


def main() -> None:
    case_dir = Path(__file__).parent / "data"
    buses, lines = load_case(case_dir)
    result = solve_dc_power_flow(buses, lines)
    print(f"Base: {result['base_mva']:.1f} MVA; slack bus: {result['slack_bus']}")
    print("Angles (radians):")
    for bus, angle in sorted(result["angles_rad"].items()):
        print(f"  Bus {bus}: {angle:.6f}")
    print("Line flows (positive from listed from_bus to to_bus):")
    for line in result["line_flows"]:
        status = "LIMIT VIOLATION" if line["limit_violated"] else "within limit"
        print(
            f"  {line['from_bus']} -> {line['to_bus']}: "
            f"{line['flow_mw']:.3f} MW ({status})"
        )


if __name__ == "__main__":
    main()
