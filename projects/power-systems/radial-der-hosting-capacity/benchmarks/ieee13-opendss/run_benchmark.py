"""Run a snapshot benchmark on a pinned public IEEE 13-node feeder with DSS-Python."""
from __future__ import annotations

import argparse
import csv
import json
import shutil
import zipfile
from io import BytesIO
from pathlib import Path
from urllib.request import Request, urlopen

from dss import dss

DEFAULT_TEST_CASE_REF = "3b208397160213cae4a9e2d0a7d1aa3528ce26e1"
TEST_CASE_REPOSITORY = "dss-extensions/electricdss-tst"

def download_test_case_snapshot(target_root: Path, commit: str) -> Path:
    """Download and unpack an immutable GitHub commit archive."""
    target_root.parent.mkdir(parents=True, exist_ok=True)
    url = f"https://codeload.github.com/{TEST_CASE_REPOSITORY}/zip/{commit}"
    request = Request(url, headers={"User-Agent": "energy-systems-doctoral-program/benchmark"})
    with urlopen(request, timeout=90) as response:
        archive_bytes = response.read()
    with zipfile.ZipFile(BytesIO(archive_bytes)) as archive:
        first_entry = next((name for name in archive.namelist() if name), None)
        if first_entry is None:
            raise RuntimeError("Downloaded test-case archive is empty.")
        extracted_name = first_entry.split("/")[0]
        destination_root = target_root.parent.resolve()
        for member in archive.infolist():
            member_path = (target_root.parent / member.filename).resolve()
            if destination_root not in member_path.parents and member_path != destination_root:
                raise RuntimeError("Archive contains a path outside the extraction directory.")
        archive.extractall(target_root.parent)
    extracted_root = target_root.parent / extracted_name
    if not extracted_root.is_dir():
        raise FileNotFoundError("Expected extracted repository directory was not created.")
    if target_root.exists():
        shutil.rmtree(target_root)
    extracted_root.rename(target_root)
    (target_root / ".source_ref").write_text(commit + "\n", encoding="utf-8")
    return target_root

def locate_ieee13(root: Path) -> Path:
    # Follow the canonical Version8 test-case path used in DSS-Python's own example.
    master_file = root / "Version8" / "Distrib" / "IEEETestCases" / "13Bus" / "IEEE13Nodeckt.dss"
    if not master_file.is_file():
        raise FileNotFoundError(
            f"Canonical IEEE 13-node master file was not found: {master_file}"
        )
    return master_file

def solve_case(master_file: Path, pv_kw: float, load_multiplier: float, test_case_ref: str) -> dict:
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
    losses = list(circuit.Losses)  # OpenDSS reports W and var.
    return {
        "engine_version": str(dss.Version),
        "test_case_repository": TEST_CASE_REPOSITORY,
        "test_case_commit": test_case_ref,
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
    (output_dir / "summary.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pv-kw", type=float, default=0.0)
    parser.add_argument("--load-multiplier", type=float, default=1.0)
    parser.add_argument("--output-dir", type=Path, default=Path("outputs/ieee13"))
    parser.add_argument("--test-case-ref", default=DEFAULT_TEST_CASE_REF,
                        help="Immutable electricdss-tst Git commit SHA.")
    parser.add_argument("--test-case-root", type=Path, default=None,
                        help="Local extracted test-case directory; its .source_ref must match the commit.")
    args = parser.parse_args()
    root = args.test_case_root or Path("data") / f"electricdss-tst-{args.test_case_ref[:8]}"
    if not root.exists():
        download_test_case_snapshot(root, args.test_case_ref)
    marker = root / ".source_ref"
    if not marker.is_file() or marker.read_text(encoding="utf-8").strip() != args.test_case_ref:
        raise ValueError(
            "Test-case directory is not verified against --test-case-ref. Remove it to download a clean pinned snapshot."
        )
    master_file = locate_ieee13(root)
    result = solve_case(master_file, args.pv_kw, args.load_multiplier, args.test_case_ref)
    write_case(result, args.output_dir)
    print(f"OpenDSS engine: {result['engine_version']}")
    print(f"Test-case commit: {result['test_case_commit']}")
    print(f"Converged: {result['converged']} ({result['iterations']} iterations)")
    print(f"PV rating: {result['pv_kw']:.1f} kW")
    print(f"Node voltage range: {result['minimum_node_voltage_pu']:.5f}–{result['maximum_node_voltage_pu']:.5f} pu")
    print(f"Real losses: {result['circuit_real_losses_kw']:.3f} kW")
    print(f"Results: {args.output_dir.resolve()}")

if __name__ == "__main__":
    main()