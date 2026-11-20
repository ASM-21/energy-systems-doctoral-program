import unittest
from pathlib import Path

from dc_power_flow import load_case, solve_dc_power_flow


class DCPowerFlowTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.buses, cls.lines = load_case(Path(__file__).parent / "data")

    def test_expected_angles_and_flows(self):
        result = solve_dc_power_flow(self.buses, self.lines)
        self.assertAlmostEqual(result["angles_rad"][1], 0)
        self.assertAlmostEqual(result["angles_rad"][2], -0.0325)
        self.assertAlmostEqual(result["angles_rad"][3], -0.015)
        flows = result["line_flows"]
        self.assertAlmostEqual(flows[0]["flow_mw"], 32.5)
        self.assertAlmostEqual(flows[1]["flow_mw"], 7.5)
        self.assertAlmostEqual(flows[2]["flow_mw"], -17.5)

    def test_thermal_limit_flags(self):
        result = solve_dc_power_flow(self.buses, self.lines)
        self.assertFalse(result["line_flows"][0]["limit_violated"])
        self.assertFalse(result["line_flows"][1]["limit_violated"])
        self.assertFalse(result["line_flows"][2]["limit_violated"])

    def test_tightened_line_limit_is_flagged(self):
        lines = [dict(line) for line in self.lines]
        lines[0]["limit_mw"] = 30
        result = solve_dc_power_flow(self.buses, lines)
        self.assertTrue(result["line_flows"][0]["limit_violated"])

    def test_unbalanced_injections_rejected(self):
        with self.assertRaises(ValueError):
            solve_dc_power_flow({1: 40, 2: -40, 3: 5}, self.lines)

    def test_nonpositive_reactance_rejected(self):
        bad_lines = [dict(line, x_pu=0) for line in self.lines]
        with self.assertRaises(ValueError):
            solve_dc_power_flow(self.buses, bad_lines)


if __name__ == "__main__":
    unittest.main()
