"""Run a snapshot benchmark on the public IEEE 13-node feeder with DSS-Python."""
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

from dss import dss
from dss.examples import download_repo_snapshot


def locate_ieee13(root: Path) -> Path:
    candidates = [
        root / "Version8" / "Distrib" / "IEEETestCases" / "13Bus" / "IEEE13Nodeckt.dss",
        root / "Version8" / "Distrib" / "IEEETestCases" / "13Bus" / "IEEE13Nodeckt.DSS",
    ]
    for candidate in candidates:
        if candidate.is_file():
            return candidate
    raise FileNotFoundError(
        "IEEE 13-node master file was not found in the downloaded electricdss-tst snapshot."
    )


def solve_case(master_file: Path, pv_kw: float, load_multiplier: float) -> dict:
    if pv_kw < 0 or load_multiplier <= 0:
        raise ValueError("PV rating must be nonnegative and load multiplier must be positive.")

    dss("Clear")
    dss(f'Redirect "{master_file.as_posix()}"')
    dss(f"Set LoadMult={load_multiplier}")
    if pv_kw > 0:
        dss(
            "New PVSystem.CurriculumPV phases=3 bus1=675.1.2.3 "
            f"kV=4.16 kVA={pv_kw:.6f} Pmpp={pv_kw:.6f} "
            "irradiance=1 pf=1"
        )
    circuit = dss.ActiveCircuit
    circuit.Solution.Solve()
    if not circuit.Solution.Converged:
        raise RuntimeError(
            f"OpenDSS did not converge for PV={pv_kw:g} kW and load multiplier={load_multiplier:g}."
        )

    node_names = list(circuit.AllNodeNames)
    voltage_pu = [float(value) for value in circuit.AllBusVmagPu]
    if len(node_names) != len(voltage_pu):
        raise RuntimeError("OpenDSS returned mismatched node-name and voltage arrays.")

    # OpenDSS Circuit.Losses is reported in W and var.
    losses = list(circuit.Losses)
    return {
        "engine_version": str(dss.Version),
        "master_file": master_file.name,
        "pv_kw": float(pv_kw),
        "load_multiplier": float(load_multiplier),
        "converged": True,
        "iterations": int(circuit.Solution.Totaliterations),
        "node_count": len(node_names),
        "minimum_node_voltage_pu": min(voltage_pu),
        "maximum_node_voltage_pu": max(voltage_pu),
        "circuit_real_losses_kw": float(losses[0]) / 1000.0,
        "circuit_reactive_losses_kvar": float(losses[1]) / 1000.0,
        "nodes": list(zip(node_names, voltage_pu)),
    }


def write_case(result: dict, output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    with (output_dir / "bus_voltages.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["node", "voltage_pu"])
        writer.writerows(result["nodes"])
    summary = {key: value for key, value in result.items() if key != "nodes"}
    (output_dir / "summary.json").write_text(
        json.dumps(summary, indent=2) + "\n", encoding="utf-8"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pv-kw", type=float, default=0.0)
    parser.add_argument("--load-multiplier", type=float, default=1.0)
    parser.add_argument("--output-dir", type=Path, default=Path("outputs/ieee13"))
    parser.add_argument("--test-case-root", type=Path, default=Path("data/electricdss-tst"))
    args = parser.parse_args()

    if not args.test_case_root.exists():
        args.test_case_root.parent.mkdir(parents=True, exist_ok=True)
        snapshot = download_repo_snapshot(
            str(args.test_case_root.parent),
            repo_name="electricdss-tst",
            use_version=False,
        )
        args.test_case_root = Path(snapshot)

    master_file = locate_ieee13(args.test_case_root)
    result = solve_case(master_file, args.pv_kw, args.load_multiplier)
    write_case(result, args.output_dir)
    print(f"OpenDSS engine: {result['engine_version']}")
    print(f"Converged: {result['converged']} ({result['iterations']} iterations)")
    print(f"PV rating: {result['pv_kw']:.1f} kW")
    print(
        "Node voltage range: "
        f"{result['minimum_node_voltage_pu']:.5f}–{result['maximum_node_voltage_pu']:.5f} pu"
    )
    print(f"Real losses: {result['circuit_real_losses_kw']:.3f} kW")
    print(f"Results: {args.output_dir.resolve()}")


if __name__ == "__main__":
    main()
