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

    def test_zero_demand(self):
        result = solve_dispatch(self.units, 0)
        self.assertAlmostEqual(result["total_cost_usd_per_hour"], 0)
        self.assertAlmostEqual(sum(x["generation_mw"] for x in result["dispatch"]), 0)

    def test_infeasible_demand(self):
        with self.assertRaises(ValueError):
            solve_dispatch(self.units, 1201)

    def test_negative_demand(self):
        with self.assertRaises(ValueError):
            solve_dispatch(self.units, -1)


if __name__ == "__main__":
    unittest.main()
