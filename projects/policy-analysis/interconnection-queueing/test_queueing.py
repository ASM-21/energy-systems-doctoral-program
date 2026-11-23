import unittest

from queueing import mmc_metrics, simulate_mmc, staffing_cost


class QueueingTests(unittest.TestCase):
    def test_mm2_exact_erlang_c_values(self):
        result = mmc_metrics(12.0, 8.0, 2)
        self.assertAlmostEqual(result["utilization"], 0.75)
        self.assertAlmostEqual(result["probability_wait"], 9 / 14)
        self.assertAlmostEqual(result["mean_queue_wait"], 9 / 56)
        self.assertAlmostEqual(result["mean_system_time"], 2 / 7)
        self.assertAlmostEqual(result["mean_queue_length"], 27 / 14)
        self.assertAlmostEqual(result["mean_system_size"], 24 / 7)

    def test_mm3_staffing_effect(self):
        result = mmc_metrics(12.0, 8.0, 3)
        self.assertAlmostEqual(result["utilization"], 0.5)
        self.assertAlmostEqual(result["probability_wait"], 9 / 38)
        self.assertAlmostEqual(result["mean_queue_wait"], 3 / 152)
        self.assertAlmostEqual(result["mean_queue_length"], 9 / 38)

    def test_little_law_residuals_are_zero(self):
        result = mmc_metrics(6.0, 8.0, 1)
        self.assertAlmostEqual(result["little_law_queue_residual"], 0.0)
        self.assertAlmostEqual(result["little_law_system_residual"], 0.0)

    def test_queue_unstable_at_or_above_capacity(self):
        for rate in (16.0, 18.0):
            with self.assertRaises(ValueError):
                mmc_metrics(rate, 8.0, 2)

    def test_invalid_inputs(self):
        for args in ((0, 8, 2), (12, 0, 2), (12, 8, 0), (12, 8, 2.5)):
            with self.assertRaises(ValueError):
                mmc_metrics(*args)

    def test_staffing_cost_tradeoff(self):
        two = mmc_metrics(12.0, 8.0, 2)
        three = mmc_metrics(12.0, 8.0, 3)
        cost_two = staffing_cost(two, 500, 300)
        cost_three = staffing_cost(three, 500, 300)
        self.assertLess(cost_three, cost_two)
        self.assertAlmostEqual(cost_two, 1578.5714285714)
        self.assertAlmostEqual(cost_three, 1571.0526315789)

    def test_simulation_is_reproducible(self):
        first = simulate_mmc(12, 8, 2, customers=5000, warmup=500, seed=42)
        second = simulate_mmc(12, 8, 2, customers=5000, warmup=500, seed=42)
        self.assertEqual(first, second)

    def test_simulation_approaches_erlang_c(self):
        analytic = mmc_metrics(12, 8, 2)
        simulated = simulate_mmc(12, 8, 2, customers=120_000, warmup=10_000)
        self.assertAlmostEqual(simulated["mean_queue_wait"],
                               analytic["mean_queue_wait"], delta=0.012)
        self.assertAlmostEqual(simulated["probability_wait"],
                               analytic["probability_wait"], delta=0.015)

    def test_simulation_rejects_unstable_queue(self):
        with self.assertRaises(ValueError):
            simulate_mmc(16, 8, 2)


if __name__ == "__main__":
    unittest.main()
