import unittest

import numpy as np

from synthetic_control import analyze, fit_weights, synthetic_panel


class SyntheticControlTests(unittest.TestCase):
    def test_weights_obey_simplex(self):
        _, treated, donors, _, n_pre = synthetic_panel()
        w = fit_weights(treated[:n_pre], donors[:, :n_pre])
        self.assertTrue(np.all(w >= -1e-10))
        self.assertAlmostEqual(float(w.sum()), 1.0, places=9)

    def test_fit_uses_only_pre_period_data(self):
        _, treated, donors, _, n_pre = synthetic_panel()
        w1 = fit_weights(treated[:n_pre], donors[:, :n_pre])
        changed_treated = treated.copy()
        changed_donors = donors.copy()
        changed_treated[n_pre:] += 1000
        changed_donors[:, n_pre:] -= 500
        w2 = fit_weights(changed_treated[:n_pre], changed_donors[:, :n_pre])
        np.testing.assert_allclose(w1, w2, atol=1e-10)

    def test_recovers_known_post_effect_under_teaching_dgp(self):
        result, *_ = analyze()
        self.assertGreater(result["average_post_gap"], 2.7)
        self.assertLess(result["average_post_gap"], 3.3)
        self.assertLess(result["pre_rmspe"], 0.15)

    def test_placebo_metadata_and_seed_reproducibility(self):
        a, *_ = analyze(7)
        b, *_ = analyze(7)
        self.assertEqual(a["weights"], b["weights"])
        self.assertEqual(len(a["placebos"]), 8)
        self.assertIn("not a design-based", a["warning"])

    def test_invalid_dimensions_and_small_panel(self):
        with self.assertRaises(ValueError):
            fit_weights([1, 2], np.ones((3, 3)))
        with self.assertRaises(ValueError):
            synthetic_panel(n_donors=2)


if __name__ == "__main__":
    unittest.main()
