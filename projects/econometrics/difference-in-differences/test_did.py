import unittest

from did import group_time_att, make_synthetic_panel, two_by_two_did, validate_panel


class DifferenceInDifferencesTests(unittest.TestCase):
    def test_two_by_two_did(self):
        self.assertAlmostEqual(two_by_two_did(10, 14, 8, 10), 2.0)

    def test_group_time_att_recovers_heterogeneous_effects(self):
        result = group_time_att(make_synthetic_panel(12))
        lookup = {(row["cohort"], row["period"]): row["att"] for row in result}
        self.assertAlmostEqual(lookup[(2, 2)], 2.0)
        self.assertAlmostEqual(lookup[(2, 3)], 3.0)
        self.assertAlmostEqual(lookup[(2, 4)], 4.0)
        self.assertAlmostEqual(lookup[(3, 3)], 1.0)
        self.assertAlmostEqual(lookup[(3, 4)], 2.0)

    def test_cohort_specific_baseline_and_never_treated_controls(self):
        result = group_time_att(make_synthetic_panel(3))
        self.assertTrue(all(row["n_control"] == 3 for row in result))
        self.assertEqual(
            {row["baseline_period"] for row in result if row["cohort"] == 2}, {1}
        )
        self.assertEqual(
            {row["baseline_period"] for row in result if row["cohort"] == 3}, {2}
        )

    def test_unbalanced_and_duplicate_panels_fail(self):
        panel = make_synthetic_panel(2)
        with self.assertRaises(ValueError):
            validate_panel(panel[:-1])
        with self.assertRaises(ValueError):
            validate_panel(panel + [dict(panel[0])])

    def test_missing_never_treated_control_fails(self):
        panel = [row for row in make_synthetic_panel(2) if row["cohort"] is not None]
        with self.assertRaises(ValueError):
            group_time_att(panel)


if __name__ == "__main__":
    unittest.main()
