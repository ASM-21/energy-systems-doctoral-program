import unittest

import numpy as np

from interrupted_time_series import analyze, design_matrix, fit_its, generate_series


class InterruptedTimeSeriesTests(unittest.TestCase):
    def test_design_separates_level_and_slope(self):
        x = design_matrix([0, 9, 10, 11], 10)
        self.assertEqual(x["post_level"].tolist(), [0.0, 0.0, 1.0, 1.0])
        self.assertEqual(x["post_slope"].tolist(), [0.0, 0.0, 0.0, 1.0])

    def test_recovers_synthetic_effects(self):
        result, frame, model = analyze()
        c = result["coefficients"]
        self.assertAlmostEqual(c["post_level"]["estimate"], 4.0, delta=0.8)
        self.assertAlmostEqual(c["post_slope"]["estimate"], 0.12, delta=0.04)
        self.assertEqual(len(frame), 120)
        self.assertTrue(np.isfinite(model.params).all())

    def test_hac_bandwidths_and_placebos_reported(self):
        result, *_ = analyze(12)
        self.assertEqual(set(result["hac_bandwidth_sensitivity"]), {"0", "3", "6", "12"})
        self.assertEqual(set(result["placebo_dates"]), {"48", "60", "84", "96"})
        self.assertIn("does not establish causal", result["warning"])

    def test_reproducibility(self):
        a, *_ = analyze(123)
        b, *_ = analyze(123)
        self.assertEqual(a["coefficients"], b["coefficients"])

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            generate_series(n=20)
        with self.assertRaises(ValueError):
            generate_series(n=60, intervention=5)
        frame, intervention = generate_series()
        with self.assertRaises(ValueError):
            fit_its(frame, intervention, maxlags=-1)


if __name__ == "__main__":
    unittest.main()
