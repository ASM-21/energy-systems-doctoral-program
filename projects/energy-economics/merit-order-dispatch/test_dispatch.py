import unittest
from pathlib import Path
from dispatch import load_generators, solve_dispatch


class DispatchTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.units = load_generators(Path(__file__).parent / "data" / "generators.csv")

    def test_baseline_dispatch_and_cost(self):
        result = solve_dispatch(self.units, 1000)
        generation = [u["generation_mw"] for u in result["dispatch"]]
        self.assertAlmostEqual(sum(generation), 1000)
        self.assertAlmostEqual(generation[0], 500)
        self.assertAlmostEqual(generation[1], 400)
        self.assertAlmostEqual(generation[2], 100)
        self.assertAlmostEqual(result["total_cost_usd_per_hour"], 30000)
        self.assertAlmostEqual(result["marginal_price_usd_per_mwh"], 60)

    def test_carbon_price_changes_merit_order_and_emissions(self):
        baseline = solve_dispatch(self.units, 1000)
        carbon = solve_dispatch(self.units, 1000, carbon_price_usd_per_tco2=100)
        self.assertEqual([u["generation_mw"] for u in baseline["dispatch"]], [500, 400, 100])
        self.assertEqual([u["generation_mw"] for u in carbon["dispatch"]], [300, 400, 300])
        self.assertLess(carbon["total_emissions_tco2_per_hour"], baseline["total_emissions_tco2_per_hour"])
        self.assertAlmostEqual(carbon["carbon_cost_usd_per_hour"], 52000)
        self.assertAlmostEqual(carbon["marginal_price_usd_per_mwh"], 110)

    def test_flexible_demand_enters_when_cheaper_than_marginal_generation(self):
        result = solve_dispatch(
            self.units, 1000, demand_response_max_mw=200,
            demand_response_cost_usd_per_mwh=50,
        )
        self.assertAlmostEqual(result["demand_response_mw"], 100)
        self.assertAlmostEqual(result["served_demand_mw"], 900)
        self.assertAlmostEqual(result["marginal_price_usd_per_mwh"], 50)
        self.assertAlmostEqual(result["demand_response_cost_usd_per_hour"], 5000)

    def test_zero_demand(self):
        result = solve_dispatch(self.units, 0)
        self.assertAlmostEqual(result["total_cost_usd_per_hour"], 0)
        self.assertAlmostEqual(sum(x["generation_mw"] for x in result["dispatch"]), 0)

    def test_infeasible_demand(self):
        with self.assertRaises(ValueError):
            solve_dispatch(self.units, 1500)

    def test_infeasible_without_enough_dr(self):
        with self.assertRaises(ValueError):
            solve_dispatch(self.units, 1500, demand_response_max_mw=100)

    def test_negative_parameters(self):
        with self.assertRaises(ValueError):
            solve_dispatch(self.units, 100, carbon_price_usd_per_tco2=-1)
        with self.assertRaises(ValueError):
            solve_dispatch(self.units, 100, demand_response_max_mw=-1)
        with self.assertRaises(ValueError):
            solve_dispatch(self.units, 100, demand_response_cost_usd_per_mwh=-1)


if __name__ == "__main__":
    unittest.main()
