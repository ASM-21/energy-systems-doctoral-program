import unittest

from dc_opf import solve_dc_opf


class ThreeBusDcOpfTests(unittest.TestCase):
    def test_base_case_benchmark(self):
        result = solve_dc_opf()
        self.assertAlmostEqual(result["generation_mw"]["g1_bus_1"], 113.3333333333, places=6)
        self.assertAlmostEqual(result["generation_mw"]["g2_bus_2"], 86.6666666667, places=6)
        self.assertAlmostEqual(result["generation_mw"]["g3_bus_3"], 0.0, places=7)
        self.assertAlmostEqual(result["angles_rad"]["bus_2"], -0.06, places=7)
        self.assertAlmostEqual(result["angles_rad"]["bus_3"], -0.1066666667, places=7)
        self.assertAlmostEqual(result["flows_mw"]["flow_12_mw"], 60.0, places=6)
        self.assertAlmostEqual(result["flows_mw"]["flow_13_mw"], 53.3333333333, places=6)
        self.assertAlmostEqual(result["flows_mw"]["flow_23_mw"], 46.6666666667, places=6)
        self.assertAlmostEqual(result["objective_usd_per_hour"], 6600.0, places=6)

    def test_nodal_balance_and_branch_limits(self):
        result = solve_dc_opf()
        generation = result["generation_mw"]
        flows = result["flows_mw"]
        self.assertAlmostEqual(generation["g1_bus_1"] - flows["flow_12_mw"] - flows["flow_13_mw"], 0.0, places=7)
        self.assertAlmostEqual(generation["g2_bus_2"] + flows["flow_12_mw"] - flows["flow_23_mw"], 100.0, places=7)
        self.assertAlmostEqual(generation["g3_bus_3"] + flows["flow_13_mw"] + flows["flow_23_mw"], 100.0, places=7)
        self.assertLessEqual(abs(flows["flow_12_mw"]), 60.0 + 1e-8)
        self.assertLessEqual(abs(flows["flow_13_mw"]), 60.0 + 1e-8)
        self.assertLessEqual(abs(flows["flow_23_mw"]), 60.0 + 1e-8)

    def test_nodal_prices_and_line_shadow_value(self):
        result = solve_dc_opf()
        prices = result["nodal_prices_usd_per_mwh"]
        self.assertAlmostEqual(prices["lmp_bus_1_usd_per_mwh"], 20.0, places=7)
        self.assertAlmostEqual(prices["lmp_bus_2_usd_per_mwh"], 50.0, places=7)
        self.assertAlmostEqual(prices["lmp_bus_3_usd_per_mwh"], 40.0, places=7)
        shadows = result["line_shadow_values"]
        self.assertAlmostEqual(shadows["line_12_upper_shadow_usd_per_mw_hour"], 40.0, places=7)

    def test_finite_difference_demand_matches_lmps(self):
        base = solve_dc_opf()["objective_usd_per_hour"]
        bus2 = solve_dc_opf(demand_bus_2_mw=101)["objective_usd_per_hour"]
        bus3 = solve_dc_opf(demand_bus_3_mw=101)["objective_usd_per_hour"]
        self.assertAlmostEqual(bus2 - base, 50.0, places=6)
        self.assertAlmostEqual(bus3 - base, 40.0, places=6)

    def test_line_limit_finite_difference_matches_shadow(self):
        base = solve_dc_opf()["objective_usd_per_hour"]
        relaxed = solve_dc_opf(line_12_limit_mw=61)["objective_usd_per_hour"]
        self.assertAlmostEqual(base - relaxed, 40.0, places=6)

    def test_relaxed_line_benchmark(self):
        result = solve_dc_opf(line_12_limit_mw=61)
        self.assertAlmostEqual(result["generation_mw"]["g1_bus_1"], 114.6666666667, places=6)
        self.assertAlmostEqual(result["generation_mw"]["g2_bus_2"], 85.3333333333, places=6)
        self.assertAlmostEqual(result["objective_usd_per_hour"], 6560.0, places=6)

    def test_invalid_and_infeasible_inputs(self):
        for kwargs in [
            {"line_12_limit_mw": 0},
            {"base_mva": float("nan")},
            {"x_12_pu": -0.1},
            {"demand_bus_3_mw": float("inf")},
            {"generator_costs": (20, 50)},
        ]:
            with self.assertRaises(ValueError):
                solve_dc_opf(**kwargs)
        with self.assertRaises(ValueError):
            solve_dc_opf(demand_bus_2_mw=250, demand_bus_3_mw=250)


if __name__ == "__main__":
    unittest.main()
