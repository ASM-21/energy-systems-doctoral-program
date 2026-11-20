import unittest

from dispatch import solve_two_node


class TwoNodeDispatchTests(unittest.TestCase):
    def test_congested_line_separates_prices(self):
        result = solve_two_node(50)
        self.assertAlmostEqual(result["generation_node_1_mw"], 150)
        self.assertAlmostEqual(result["generation_node_2_mw"], 50)
        self.assertAlmostEqual(result["flow_node_1_to_2_mw"], 50)
        self.assertAlmostEqual(result["total_cost_usd_per_hour"], 6500)
        self.assertAlmostEqual(result["price_node_1_usd_per_mwh"], 20)
        self.assertAlmostEqual(result["price_node_2_usd_per_mwh"], 70)

    def test_relaxed_line_removes_congestion_price_spread(self):
        result = solve_two_node(100)
        self.assertAlmostEqual(result["generation_node_1_mw"], 150)
        self.assertAlmostEqual(result["generation_node_2_mw"], 50)
        self.assertAlmostEqual(result["price_node_1_usd_per_mwh"], 70)
        self.assertAlmostEqual(result["price_node_2_usd_per_mwh"], 70)

    def test_negative_line_limit_rejected(self):
        with self.assertRaises(ValueError):
            solve_two_node(-1)


if __name__ == "__main__":
    unittest.main()
