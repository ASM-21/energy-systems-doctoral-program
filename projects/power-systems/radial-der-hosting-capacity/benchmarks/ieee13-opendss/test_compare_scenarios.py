import csv
import json
import tempfile
import unittest
from pathlib import Path

from compare_scenarios import compare


class CompareScenarioTests(unittest.TestCase):
    def _write_case(self, root: Path, name: str, pv_kw: float, nodes: dict[str, float],
                    master_file: str = "IEEE13Nodeckt.dss") -> Path:
        folder = root / name
        folder.mkdir()
        summary = {
            "engine_version": "test-engine",
            "master_file": master_file,
            "load_multiplier": 1.0,
            "pv_kw": pv_kw,
            "minimum_node_voltage_pu": min(nodes.values()),
            "maximum_node_voltage_pu": max(nodes.values()),
            "circuit_real_losses_kw": 10.0 - pv_kw / 100.0,
        }
        (folder / "summary.json").write_text(json.dumps(summary), encoding="utf-8")
        with (folder / "bus_voltages.csv").open("w", newline="", encoding="utf-8") as handle:
            writer = csv.writer(handle)
            writer.writerow(["node", "voltage_pu"])
            writer.writerows(nodes.items())
        return folder

    def test_node_alignment_and_delta_outputs(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            baseline = self._write_case(root, "base", 0, {"650.1": 1.0, "632.1": 0.98})
            scenario = self._write_case(root, "pv", 100, {"650.1": 1.0, "632.1": 1.01})
            result = compare(baseline, scenario, root / "comparison")
            self.assertAlmostEqual(result["maximum_voltage_change_pu"], 0.03)
            self.assertAlmostEqual(result["minimum_voltage_change_pu"], 0.0)
            self.assertTrue((root / "comparison" / "node_voltage_comparison.csv").exists())
            self.assertTrue((root / "comparison" / "comparison_summary.json").exists())

    def test_rejects_mismatched_case_source(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            baseline = self._write_case(root, "base", 0, {"650.1": 1.0})
            scenario = self._write_case(root, "pv", 100, {"650.1": 1.01}, "other.dss")
            with self.assertRaises(ValueError):
                compare(baseline, scenario, root / "comparison")

    def test_rejects_mismatched_node_sets(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            baseline = self._write_case(root, "base", 0, {"650.1": 1.0})
            scenario = self._write_case(root, "pv", 100, {"650.2": 1.01})
            with self.assertRaises(ValueError):
                compare(baseline, scenario, root / "comparison")


if __name__ == "__main__":
    unittest.main()