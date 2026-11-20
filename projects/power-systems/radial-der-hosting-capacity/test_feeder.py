import tempfile
import unittest
from pathlib import Path

from feeder import read_inputs, run_sweep, solve_feeder, write_outputs


DATA = Path(__file__).parent / "data"


class RadialFeederTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.buses, cls.lines = read_inputs(DATA)

    def test_zero_der_has_forward_flow_and_valid_voltages(self):
        result = solve_feeder(self.buses, self.lines, der_bus=4, der_kw=0)
        self.assertTrue(result["within_screening_limits"])
        self.assertEqual(result["reverse_flow_branches"], [])
        self.assertEqual(len(result["branches"]), 3)
        self.assertLess(result["minimum_voltage_pu"], 1.0)

    def test_remote_der_causes_reverse_flow(self):
        result = solve_feeder(self.buses, self.lines, der_bus=4, der_kw=1500)
        self.assertTrue(any(b["reverse_flow"] for b in result["branches"]))
        self.assertTrue(any(b["p_kw"] < 0 for b in result["branches"]))

    def test_der_increases_remote_voltage_in_this_case(self):
        low = solve_feeder(self.buses, self.lines, der_bus=4, der_kw=0)
        high = solve_feeder(self.buses, self.lines, der_bus=4, der_kw=2000)
        self.assertGreater(high["maximum_voltage_pu"], low["maximum_voltage_pu"])

    def test_sweep_and_output_files(self):
        results = run_sweep(self.buses, self.lines, 4, 500, 100)
        self.assertEqual(len(results), 6)
        with tempfile.TemporaryDirectory() as tmp:
            write_outputs(results, Path(tmp))
            self.assertTrue((Path(tmp) / "scenario_summary.csv").exists())
            self.assertTrue((Path(tmp) / "branch_detail.csv").exists())

    def test_first_thermal_violation_is_at_900_kw_for_supplied_case(self):
        results = run_sweep(self.buses, self.lines, 4, 1200, 100)
        first = next(r["der_kw"] for r in results if not r["within_screening_limits"])
        self.assertEqual(first, 900)
        at_800 = solve_feeder(self.buses, self.lines, 4, 800)
        at_900 = solve_feeder(self.buses, self.lines, 4, 900)
        self.assertFalse(any(b["thermal_violation"] for b in at_800["branches"]))
        self.assertTrue(any(b["thermal_violation"] for b in at_900["branches"]))

    def test_voltage_limit_event_at_high_pv_penetration(self):
        result = solve_feeder(self.buses, self.lines, 4, 5000)
        self.assertTrue(any(v["voltage_pu"] > 1.05 for v in result["voltage_violations"]))

    def test_rejects_non_radial_or_invalid_inputs(self):
        with self.assertRaises(ValueError):
            solve_feeder(self.buses, self.lines, der_bus=99, der_kw=100)
        with self.assertRaises(ValueError):
            run_sweep(self.buses, self.lines, 4, 100, 0)
        with self.assertRaises(ValueError):
            run_sweep(self.buses, self.lines, 4, 100, 0.5)


if __name__ == "__main__":
    unittest.main()
