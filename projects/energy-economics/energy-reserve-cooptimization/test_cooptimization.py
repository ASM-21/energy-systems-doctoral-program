import unittest

from cooptimization import DEFAULT_UNITS, solve_cooptimization


class CooptimizationTests(unittest.TestCase):
    def test_benchmark_primal_solution(self):
        result = solve_cooptimization()
        self.assertAlmostEqual(result["energy_dispatch_mw"], 150.0)
        self.assertAlmostEqual(result["reserve_awarded_mw"], 20.0)
        self.assertAlmostEqual(result["objective_usd_for_interval"], 3720.0)
        rows = {row["name"]: row for row in result["units"]}
        expected = {"A": (80.0, 0.0), "B": (70.0, 0.0), "C": (0.0, 20.0)}
        for name, (energy, reserve) in expected.items():
            self.assertAlmostEqual(rows[name]["energy_mw"], energy)
            self.assertAlmostEqual(rows[name]["reserve_mw"], reserve)
            self.assertLessEqual(rows[name]["total_award_mw"], rows[name]["capacity_mw"] + 1e-8)

    def test_dual_values_and_capacity_shadow_values(self):
        result = solve_cooptimization()
        self.assertAlmostEqual(result["energy_balance_dual_usd_per_mwh"], 55.0)
        self.assertAlmostEqual(result["reserve_requirement_dual_usd_per_mw_h"], 2.0)
        rows = {row["name"]: row for row in result["units"]}
        self.assertAlmostEqual(rows["A"]["capacity_shadow_value_usd_per_mw_h"], 37.0)
        self.assertAlmostEqual(rows["B"]["capacity_shadow_value_usd_per_mw_h"], 23.0)
        self.assertAlmostEqual(rows["C"]["capacity_shadow_value_usd_per_mw_h"], 0.0)

    def test_energy_dual_matches_one_mw_finite_difference(self):
        base = solve_cooptimization()
        perturbed = solve_cooptimization(demand_mw=151.0)
        delta = perturbed["objective_usd_for_interval"] - base["objective_usd_for_interval"]
        self.assertAlmostEqual(delta, base["energy_balance_dual_usd_per_mwh"])

    def test_reserve_dual_matches_one_mw_finite_difference(self):
        base = solve_cooptimization()
        perturbed = solve_cooptimization(reserve_mw=21.0)
        delta = perturbed["objective_usd_for_interval"] - base["objective_usd_for_interval"]
        self.assertAlmostEqual(delta, base["reserve_requirement_dual_usd_per_mw_h"])

    def test_non_default_offer_changes_reserve_award(self):
        units = [dict(unit) for unit in DEFAULT_UNITS]
        units[0]["reserve_offer"] = 1.0
        result = solve_cooptimization(units=units)
        rows = {row["name"]: row for row in result["units"]}
        self.assertAlmostEqual(rows["A"]["reserve_mw"], 20.0)
        self.assertAlmostEqual(rows["C"]["reserve_mw"], 0.0)

    def test_infeasible_capacity_requirement_is_rejected(self):
        with self.assertRaises(ValueError):
            solve_cooptimization(demand_mw=150.0, reserve_mw=51.0)

    def test_negative_input_is_rejected(self):
        with self.assertRaises(ValueError):
            solve_cooptimization(demand_mw=-1.0)
        with self.assertRaises(ValueError):
            solve_cooptimization(reserve_mw=-1.0)

    def test_invalid_unit_is_rejected(self):
        bad_units = [dict(DEFAULT_UNITS[0], capacity=-1.0)]
        with self.assertRaises(ValueError):
            solve_cooptimization(units=bad_units)


if __name__ == "__main__":
    unittest.main()
