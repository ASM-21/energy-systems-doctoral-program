"""Synthetic radial feeder DER hosting-capacity screen using LinDistFlow-style approximations."""
from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Bus:
    bus_id: int
    load_p_kw: float
    load_q_kvar: float


@dataclass(frozen=True)
class Line:
    from_bus: int
    to_bus: int
    r_ohm: float
    x_ohm: float
    thermal_limit_mva: float


def read_inputs(data_dir: Path) -> tuple[dict[int, Bus], list[Line]]:
    with (data_dir / "buses.csv").open(newline="", encoding="utf-8") as f:
        buses = {
            int(row["bus_id"]): Bus(
                int(row["bus_id"]), float(row["load_p_kw"]), float(row["load_q_kvar"])
            )
            for row in csv.DictReader(f)
        }
    with (data_dir / "lines.csv").open(newline="", encoding="utf-8") as f:
        lines = [
            Line(
                int(row["from_bus"]), int(row["to_bus"]), float(row["r_ohm"]),
                float(row["x_ohm"]), float(row["thermal_limit_mva"])
            )
            for row in csv.DictReader(f)
        ]
    validate_radial_network(buses, lines)
    return buses, lines


def validate_radial_network(buses: dict[int, Bus], lines: list[Line]) -> None:
    if not buses or 1 not in buses:
        raise ValueError("Bus 1 must be the slack/root bus.")
    if len(lines) != len(buses) - 1:
        raise ValueError("A connected radial tree must have n_bus - 1 branches.")
    seen = {1}
    remaining = list(lines)
    while remaining:
        progressed = False
        for line in remaining[:]:
            if line.from_bus not in buses or line.to_bus not in buses:
                raise ValueError("Every branch endpoint must exist in buses.csv.")
            if line.r_ohm < 0 or line.x_ohm < 0 or line.thermal_limit_mva <= 0:
                raise ValueError("Line impedances must be nonnegative and ratings positive.")
            if line.from_bus in seen and line.to_bus not in seen:
                seen.add(line.to_bus)
                remaining.remove(line)
                progressed = True
            elif line.to_bus in seen:
                raise ValueError("Branches must be oriented away from root bus 1.")
        if not progressed:
            raise ValueError("Lines must form one connected, acyclic tree oriented from bus 1.")
    if seen != set(buses):
        raise ValueError("Every bus must be connected to root bus 1.")


def solve_feeder(
    buses: dict[int, Bus],
    lines: list[Line],
    der_bus: int,
    der_kw: float,
    v_base_kv: float = 12.47,
    v_min_pu: float = 0.95,
    v_max_pu: float = 1.05,
) -> dict:
    """Solve a single snapshot; positive P/Q are consumption, DER is positive injection."""
    if der_bus not in buses:
        raise ValueError(f"DER bus {der_bus} is not in the feeder.")
    if der_kw < 0 or v_base_kv <= 0 or not (0 < v_min_pu < v_max_pu):
        raise ValueError("Invalid DER, base-voltage, or voltage-band input.")

    children: dict[int, list[int]] = {bus_id: [] for bus_id in buses}
    line_by_child = {}
    for line in lines:
        children[line.from_bus].append(line.to_bus)
        line_by_child[line.to_bus] = line

    downstream_p = {bus_id: bus.load_p_kw for bus_id, bus in buses.items()}
    downstream_q = {bus_id: bus.load_q_kvar for bus_id, bus in buses.items()}
    downstream_p[der_bus] -= der_kw

    # Post-order aggregation on the validated radial tree.
    order = []
    stack = [1]
    while stack:
        node = stack.pop()
        order.append(node)
        stack.extend(children[node])
    for node in reversed(order[1:]):
        parent = line_by_child[node].from_bus
        downstream_p[parent] += downstream_p[node]
        downstream_q[parent] += downstream_q[node]

    voltage = {1: 1.0}
    branch_results = []
    for node in order[1:]:
        line = line_by_child[node]
        p_kw = downstream_p[node]
        q_kvar = downstream_q[node]
        p_mw, q_mvar = p_kw / 1000.0, q_kvar / 1000.0
        drop_pu = (line.r_ohm * p_mw + line.x_ohm * q_mvar) / (v_base_kv ** 2)
        voltage[node] = voltage[line.from_bus] - drop_pu
        apparent_mva = (p_mw ** 2 + q_mvar ** 2) ** 0.5
        branch_results.append({
            "from_bus": line.from_bus,
            "to_bus": node,
            "p_kw": p_kw,
            "q_kvar": q_kvar,
            "apparent_mva": apparent_mva,
            "thermal_limit_mva": line.thermal_limit_mva,
            "reverse_flow": p_kw < 0,
            "thermal_violation": apparent_mva > line.thermal_limit_mva + 1e-12,
            "voltage_from_pu": voltage[line.from_bus],
            "voltage_to_pu": voltage[node],
        })

    voltage_violations = [
        {"bus_id": bus_id, "voltage_pu": value}
        for bus_id, value in voltage.items()
        if value < v_min_pu - 1e-12 or value > v_max_pu + 1e-12
    ]
    thermal_violations = [b for b in branch_results if b["thermal_violation"]]
    return {
        "der_bus": der_bus,
        "der_kw": der_kw,
        "minimum_voltage_pu": min(voltage.values()),
        "maximum_voltage_pu": max(voltage.values()),
        "voltage_violations": voltage_violations,
        "thermal_violations": thermal_violations,
        "reverse_flow_branches": [b for b in branch_results if b["reverse_flow"]],
        "branches": branch_results,
        "within_screening_limits": not voltage_violations and not thermal_violations,
    }


def run_sweep(buses, lines, der_bus, maximum_kw, step_kw, **kwargs):
    if maximum_kw < 0 or step_kw <= 0 or int(step_kw) != step_kw:
        raise ValueError("Sweep maximum must be nonnegative and step must be a positive whole number.")
    levels = list(range(0, int(maximum_kw) + 1, int(step_kw)))
    if not levels or levels[-1] != maximum_kw:
        levels.append(maximum_kw)
    return [solve_feeder(buses, lines, der_bus, level, **kwargs) for level in levels]


def write_outputs(results: list[dict], output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    with (output_dir / "scenario_summary.csv").open("w", newline="", encoding="utf-8") as f:
        fields = ["der_bus", "der_kw", "minimum_voltage_pu", "maximum_voltage_pu",
                  "within_screening_limits", "voltage_violation_count",
                  "thermal_violation_count", "reverse_flow_branch_count"]
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for result in results:
            writer.writerow({
                "der_bus": result["der_bus"], "der_kw": result["der_kw"],
                "minimum_voltage_pu": result["minimum_voltage_pu"],
                "maximum_voltage_pu": result["maximum_voltage_pu"],
                "within_screening_limits": result["within_screening_limits"],
                "voltage_violation_count": len(result["voltage_violations"]),
                "thermal_violation_count": len(result["thermal_violations"]),
                "reverse_flow_branch_count": len(result["reverse_flow_branches"]),
            })
    with (output_dir / "branch_detail.csv").open("w", newline="", encoding="utf-8") as f:
        fields = ["der_kw", "from_bus", "to_bus", "p_kw", "q_kvar", "apparent_mva",
                  "thermal_limit_mva", "reverse_flow", "thermal_violation",
                  "voltage_from_pu", "voltage_to_pu"]
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for result in results:
            for branch in result["branches"]:
                writer.writerow({"der_kw": result["der_kw"], **branch})


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data-dir", type=Path, default=Path(__file__).parent / "data")
    parser.add_argument("--output-dir", type=Path, default=Path(__file__).parent / "outputs")
    parser.add_argument("--der-bus", type=int, default=4)
    parser.add_argument("--sweep-max-kw", type=float, default=3000)
    parser.add_argument("--step-kw", type=float, default=100)
    parser.add_argument("--v-base-kv", type=float, default=12.47)
    parser.add_argument("--v-min-pu", type=float, default=0.95)
    parser.add_argument("--v-max-pu", type=float, default=1.05)
    args = parser.parse_args()
    buses, lines = read_inputs(args.data_dir)
    results = run_sweep(
        buses, lines, args.der_bus, args.sweep_max_kw, args.step_kw,
        v_base_kv=args.v_base_kv, v_min_pu=args.v_min_pu, v_max_pu=args.v_max_pu
    )
    write_outputs(results, args.output_dir)
    first_violation = next((r["der_kw"] for r in results if not r["within_screening_limits"]), None)
    print(f"Scenarios: {len(results)}")
    print(f"First screened voltage/thermal violation: {first_violation if first_violation is not None else 'not observed'} kW")
    print(f"Outputs: {args.output_dir.resolve()}")


if __name__ == "__main__":
    main()
