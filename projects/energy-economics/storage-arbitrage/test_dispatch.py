import unittest

from dispatch import solve_storage


class StorageArbitrageTests(unittest.TestCase):
    def test_optimal_default_schedule(self):
        result = solve_storage([20, 30, 80, 100])
        self.assertAlmostEqual(result["charge_mw"][0], 5)
        self.assertAlmostEqual(result["charge_mw"][1], 5)
        self.assertAlmostEqual(result["discharge_mw"][2], 3.1)
        self.assertAlmostEqual(result["discharge_mw"][3], 5)
        self.assertAlmostEqual(result["state_of_charge_mwh"][-1], 0)
        self.assertAlmostEqual(result["gross_margin_usd"], 498)

    def test_degradation_cost_reduces_margin(self):
        result = solve_storage([20, 30, 80, 100], degradation_cost_per_mwh=15)
        self.assertAlmostEqual(result["degradation_cost_usd"], 271.5)
        self.assertAlmostEqual(result["net_margin_usd"], 226.5)

    def test_negative_prices_rejected(self):
        with self.assertRaises(ValueError):
            solve_storage([-10, 20])

    def test_invalid_efficiency_rejected(self):
        with self.assertRaises(ValueError):
            solve_storage([10, 20], charge_efficiency=1.1)


if __name__ == "__main__":
    unittest.main()
