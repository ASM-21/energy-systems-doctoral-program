"""Run a reproducible PV-rating sweep on the pinned IEEE 13-node feeder."""
from __future__ import annotations
import argparse
import csv
import json
from pathlib import Path

from run_benchmark import (
    DEFAULT_TEST_CASE_REF,
    download_test_case_snapshot,
    locate_ieee13,
    solve_case,
)

DEFAULT_PV_LEVELS_KW = (0, 100, 250, 500, 750, 1000)


def summarize_sweep(results: list[dict], voltage_limit_pu: float = 1.05) -> dict:
    if not results:
        raise ValueError("At least one PV scenario is required.")
    if voltage_limit_pu <= 0:
        raise ValueError("Voltage limit must be positive.")
    ordered = sorted(results, key=lambda row: row["pv_kw"])
    if len({row["pv_kw"] for row in ordered}) != len(ordered):
        raise ValueError("PV scenario ratings must be unique.")
    baseline = next((row for row in ordered if row["pv_kw"] == 0), None)
    if baseline is None:
        raise ValueError("A zero-PV baseline scenario is required.")
    baseline_exceeds = baseline["maximum_node_voltage_pu"] > voltage_limit_pu
    first_new_exceedance = next(
        (row["pv_kw"] for row in ordered
         if row["maximum_node_voltage_pu"] > voltage_limit_pu
         and not baseline_exceeds),
        None,
    )
    return {
        "voltage_limit_pu": voltage_limit_pu,
        "baseline_already_exceeds_limit": baseline_exceeds,
        "first_pv_rating_exceeding_limit_if_baseline_complies_kw": first_new_exceedance,
        "scenario_count": len(ordered),
        "scenarios": ordered,
    }


def run_sweep(test_case_root: Path, test_case_ref: str, output_dir: Path,
              pv_levels_kw: tuple[float, ...], load_multiplier: float,
              voltage_limit_pu: float) -> dict:
    master = locate_ieee13(test_case_root)
    results = [solve_case(master, rating, load_multiplier, test_case_ref)
               for rating in pv_levels_kw]
    summary = summarize_sweep(results, voltage_limit_pu)
    output_dir.mkdir(parents=True, exist_ok=True)
    fields = ["pv_kw", "minimum_node_voltage_pu", "maximum_node_voltage_pu",
              "circuit_real_losses_kw", "circuit_reactive_losses_kvar", "iterations", "node_count"]
    with (output_dir / "pv_sweep.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in results:
            writer.writerow({field: row[field] for field in fields})
    (output_dir / "pv_sweep_summary.json").write_text(
        json.dumps({key: value for key, value in summary.items() if key != "scenarios"}, indent=2)
        + "\n", encoding="utf-8"
    )
    print(f"PV scenarios: {len(results)}")
    print(f"Voltage screen: {voltage_limit_pu:.3f} pu")
    print(f"Baseline already exceeds screen: {summary['baseline_already_exceeds_limit']}")
    print("PV kW | min pu | max pu | losses kW")
    for row in results:
        print(f"{row['pv_kw']:6.1f} | {row['minimum_node_voltage_pu']:.5f} | "
              f"{row['maximum_node_voltage_pu']:.5f} | {row['circuit_real_losses_kw']:.3f}")
    print(f"Sweep outputs: {output_dir.resolve()}")
    return summary


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pv-levels-kw", default="0,100,250,500,750,1000")
    parser.add_argument("--load-multiplier", type=float, default=1.0)
    parser.add_argument("--voltage-limit-pu", type=float, default=1.05)
    parser.add_argument("--test-case-ref", default=DEFAULT_TEST_CASE_REF)
    parser.add_argument("--test-case-root", type=Path, default=None)
    parser.add_argument("--output-dir", type=Path, default=Path("outputs/pv-sweep"))
    args = parser.parse_args()
    levels = tuple(float(value.strip()) for value in args.pv_levels_kw.split(","))
    if any(value < 0 for value in levels):
        parser.error("PV levels must be nonnegative.")
    root = args.test_case_root or Path("data") / f"electricdss-tst-{args.test_case_ref[:8]}"
    if not root.exists():
        download_test_case_snapshot(root, args.test_case_ref)
    marker = root / ".source_ref"
    if not marker.is_file() or marker.read_text(encoding="utf-8").strip() != args.test_case_ref:
        parser.error("Test-case directory does not match the pinned source commit.")
    run_sweep(root, args.test_case_ref, args.output_dir, levels,
              args.load_multiplier, args.voltage_limit_pu)


if __name__ == "__main__":
    main()
