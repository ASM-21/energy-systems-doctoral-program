import unittest

from adequacy import (
    Parameters,
    shortfall_mw,
    simulate,
    simulate_year,
    stationary_high_probability,
    stationary_outage_probability,
)


class AdequacyTests(unittest.TestCase):
    def test_stationary_probabilities(self):
        self.assertAlmostEqual(stationary_high_probability(0.1, 0.3), 0.25)
        self.assertAlmostEqual(stationary_outage_probability(0.001, 0.03233333333333333), 0.03)

    def test_shortfall_calculation(self):
        self.assertEqual(shortfall_mw(1000, 300, 800), 0)
        self.assertEqual(shortfall_mw(1000, 100, 800), 100)

    def test_simulation_reproducible(self):
        first = simulate(years=2, seed=17)
        second = simulate(years=2, seed=17)
        self.assertEqual(first, second)

    def test_metrics_are_nonnegative_and_bounded(self):
        result = simulate(years=3, seed=5)
        metrics = result["metrics"]
        self.assertGreaterEqual(metrics["lole_hours_per_year"]["mean"], 0)
        self.assertLessEqual(metrics["lole_hours_per_year"]["mean"], 8760)
        self.assertGreaterEqual(metrics["eue_mwh_per_year"]["mean"], 0)
        self.assertGreaterEqual(metrics["hourly_lolp_by_year"]["mean"], 0)
        self.assertLessEqual(metrics["hourly_lolp_by_year"]["mean"], 1)

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            simulate(years=0)
        with self.assertRaises(ValueError):
            Parameters(hours_per_year=0).validate()
        with self.assertRaises(ValueError):
            stationary_high_probability(0, 0)

    def test_single_year_metrics(self):
        result = simulate(years=1, seed=9)
        self.assertEqual(result["metrics"]["lole_hours_per_year"]["standard_error_across_years"], 0.0)


if __name__ == "__main__":
    unittest.main()
