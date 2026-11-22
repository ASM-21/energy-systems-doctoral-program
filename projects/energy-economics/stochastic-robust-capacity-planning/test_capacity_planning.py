import unittest

from capacity_planning import (
    compare_models,
    solve_expected_value,
    solve_robust,
    solve_stochastic,
    solve_wait_and_see,
)


class CapacityPlanningTests(unittest.TestCase):
    def test_stochastic_recourse_solution(self):
        result = solve_stochastic()
        self.assertAlmostEqual(result["capacity"], 80.0, places=6)
        self.assertAlmostEqual(result["expected_cost"], 8400.0, places=6)
        self.assertAlmostEqual(result["recourse"]["low"]["generation"], 80.0)
        self.assertAlmostEqual(result["recourse"]["low"]["unserved"], 0.0)
        self.assertAlmostEqual(result["recourse"]["high"]["generation"], 80.0)
        self.assertAlmostEqual(result["recourse"]["high"]["unserved"], 40.0)

    def test_expected_value_and_wait_and_see(self):
        expected = solve_expected_value()
        wait = solve_wait_and_see()
        self.assertAlmostEqual(expected["capacity"], 104.0, places=6)
        self.assertAlmostEqual(expected["evaluated_expected_cost"], 8712.0, places=6)
        self.assertAlmostEqual(wait["expected_cost"], 7800.0, places=6)
        self.assertAlmostEqual(wait["decisions"]["low"]["capacity"], 80.0, places=6)
        self.assertAlmostEqual(wait["decisions"]["high"]["capacity"], 120.0, places=6)

    def test_robust_solution(self):
        result = solve_robust()
        self.assertAlmostEqual(result["capacity"], 120.0, places=6)
        self.assertAlmostEqual(result["worst_case_cost"], 9000.0, places=6)

    def test_value_metrics(self):
        result = compare_models()
        self.assertAlmostEqual(result["value_of_stochastic_solution"], 312.0, places=6)
        self.assertAlmostEqual(
            result["expected_value_of_perfect_information"], 600.0, places=6
        )


if __name__ == "__main__":
    unittest.main()
