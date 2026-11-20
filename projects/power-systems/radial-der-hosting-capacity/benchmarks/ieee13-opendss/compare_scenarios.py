"""Compare two OpenDSS benchmark scenarios at node level."""
from __future__ import annotations
import argparse
import csv
import json
from pathlib import Path

def read_voltages(path: Path) -> dict[str, float]:
    with path.open(newline="", encoding="utf-8") as handle:
        return {row["node"]: float(row["voltage_pu"]) for row in csv.DictReader(handle)}

def compare(baseline_dir: Path, scenario_dir: Path, output_dir: Path) -> dict:
    base = json.loads((baseline_dir / "summary.json").read_text(encoding="utf-8"))
    case = json.loads((scenario_dir / "summary.json").read_text(encoding="utf-8"))
    for key in ("engine_version", "master_file", "load_multiplier"):
        if base[key] != case[key]:
            raise ValueError(f"Scenario mismatch for {key}: {base[key]!r} != {case[key]!r}")
    base_v = read_voltages(baseline_dir / "bus_voltages.csv")
    case_v = read_voltages(scenario_dir / "bus_voltages.csv")
    if set(base_v) != set(case_v):
        raise ValueError("Baseline and scenario node sets do not match.")
    rows = [{"node": node, "baseline_voltage_pu": base_v[node],
             "scenario_voltage_pu": case_v[node],
             "delta_voltage_pu": case_v[node] - base_v[node]}
            for node in sorted(base_v)]
    rows.sort(key=lambda row: row["delta_voltage_pu"], reverse=True)
    output_dir.mkdir(parents=True, exist_ok=True)
    with (output_dir / "node_voltage_comparison.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    summary = {
        "engine_version": base["engine_version"],
        "master_file": base["master_file"],
        "load_multiplier": base["load_multiplier"],
        "baseline_pv_kw": base["pv_kw"],
        "scenario_pv_kw": case["pv_kw"],
        "baseline_min_voltage_pu": base["minimum_node_voltage_pu"],
        "scenario_min_voltage_pu": case["minimum_node_voltage_pu"],
        "baseline_max_voltage_pu": base["maximum_node_voltage_pu"],
        "scenario_max_voltage_pu": case["maximum_node_voltage_pu"],
        "baseline_real_losses_kw": base["circuit_real_losses_kw"],
        "scenario_real_losses_kw": case["circuit_real_losses_kw"],
        "minimum_voltage_change_pu": min(row["delta_voltage_pu"] for row in rows),
        "maximum_voltage_change_pu": max(row["delta_voltage_pu"] for row in rows),
        "largest_voltage_increases": rows[:5],
        "smallest_voltage_changes": rows[-5:],
        "baseline_min_voltage_node": min(base_v, key=base_v.get),
        "scenario_min_voltage_node": min(case_v, key=case_v.get),
        "baseline_max_voltage_node": max(base_v, key=base_v.get),
        "scenario_max_voltage_node": max(case_v, key=case_v.get),
        "baseline_max_exceeds_1_05_pu": base["maximum_node_voltage_pu"] > 1.05,
        "scenario_max_exceeds_1_05_pu": case["maximum_node_voltage_pu"] > 1.05,
    }
    (output_dir / "comparison_summary.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(f"PV change: {base['pv_kw']:.1f} -> {case['pv_kw']:.1f} kW")
    print(f"Minimum voltage: {base['minimum_node_voltage_pu']:.5f} -> {case['minimum_node_voltage_pu']:.5f} pu")
    print(f"Maximum voltage: {base['maximum_node_voltage_pu']:.5f} -> {case['maximum_node_voltage_pu']:.5f} pu")
    print(f"Real losses: {base['circuit_real_losses_kw']:.3f} -> {case['circuit_real_losses_kw']:.3f} kW")
    print(f"Node-level voltage delta range: {summary['minimum_voltage_change_pu']:.5f} to {summary['maximum_voltage_change_pu']:.5f} pu")
    print(f"Baseline maximum-voltage node: {summary['baseline_max_voltage_node']}")
    print(f"Scenario maximum-voltage node: {summary['scenario_max_voltage_node']}")
    print(f"Baseline already exceeds 1.05 pu: {summary['baseline_max_exceeds_1_05_pu']}")
    print(f"Comparison files: {output_dir.resolve()}")
    return summary

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--baseline-dir", type=Path, required=True)
    parser.add_argument("--scenario-dir", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, default=Path("outputs/comparison"))
    args = parser.parse_args()
    compare(args.baseline_dir, args.scenario_dir, args.output_dir)

if __name__ == "__main__":
    main()