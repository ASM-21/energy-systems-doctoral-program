import unittest
from pv_sweep import summarize_sweep


class SweepSummaryTests(unittest.TestCase):
    def row(self, pv, maximum, minimum=0.98):
        return {"pv_kw": pv, "minimum_node_voltage_pu": minimum,
                "maximum_node_voltage_pu": maximum}

    def test_detects_baseline_violation_without_attributing_it_to_pv(self):
        result = summarize_sweep([self.row(0, 1.06), self.row(100, 1.061), self.row(500, 1.07)])
        self.assertTrue(result["baseline_already_exceeds_limit"])
        self.assertIsNone(result["first_pv_rating_exceeding_limit_if_baseline_complies_kw"])

    def test_finds_first_new_violation_when_baseline_complies(self):
        result = summarize_sweep([self.row(500, 1.06), self.row(0, 1.02), self.row(100, 1.04)])
        self.assertFalse(result["baseline_already_exceeds_limit"])
        self.assertEqual(result["first_pv_rating_exceeding_limit_if_baseline_complies_kw"], 500)

    def test_rejects_duplicate_scenarios(self):
        with self.assertRaises(ValueError):
            summarize_sweep([self.row(0, 1.0), self.row(0, 1.01)])

    def test_rejects_empty_sweep(self):
        with self.assertRaises(ValueError):
            summarize_sweep([])

    def test_requires_zero_pv_baseline(self):
        with self.assertRaises(ValueError):
            summarize_sweep([self.row(100, 1.01)])


if __name__ == "__main__":
    unittest.main()
