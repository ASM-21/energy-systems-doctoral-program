import unittest

from survival import (
    aalen_johansen,
    check_probability_mass,
    kaplan_meier_net_approval,
)


class CompetingRiskTests(unittest.TestCase):
    def setUp(self):
        self.records = [
            {"time": 1, "event": "approval"},
            {"time": 1, "event": "withdrawal"},
            {"time": 2, "event": "denial"},
            {"time": 2, "event": "censored"},
            {"time": 3, "event": "approval"},
            {"time": 4, "event": "censored"},
        ]

    def test_aalen_johansen_cumulative_incidence(self):
        curve = aalen_johansen(self.records)
        self.assertAlmostEqual(curve[0]["cif_approval"], 1 / 6)
        self.assertAlmostEqual(curve[0]["cif_withdrawal"], 1 / 6)
        self.assertAlmostEqual(curve[1]["cif_denial"], 1 / 6)
        self.assertAlmostEqual(curve[2]["cif_approval"], 5 / 12)
        self.assertAlmostEqual(curve[2]["event_free_probability"], 1 / 4)
        self.assertTrue(check_probability_mass(curve))

    def test_naive_one_minus_km_overstates_observed_approval_cif(self):
        km = kaplan_meier_net_approval(self.records)
        aj = aalen_johansen(self.records)
        self.assertAlmostEqual(km[2]["net_approval_probability"], 7 / 12)
        self.assertAlmostEqual(aj[2]["cif_approval"], 5 / 12)
        self.assertGreater(km[2]["net_approval_probability"], aj[2]["cif_approval"])

    def test_no_competing_events_estimators_agree(self):
        records = [
            {"time": 1, "event": "approval"},
            {"time": 2, "event": "censored"},
            {"time": 3, "event": "approval"},
        ]
        km = kaplan_meier_net_approval(records)
        aj = aalen_johansen(records)
        for left, right in zip(km, aj):
            self.assertAlmostEqual(left["net_approval_probability"], right["cif_approval"])

    def test_all_censored_has_zero_incidence(self):
        curve = aalen_johansen([
            {"time": 1, "event": "censored"},
            {"time": 2, "event": "censored"},
        ])
        self.assertEqual(curve[-1]["cif_approval"], 0.0)
        self.assertEqual(curve[-1]["event_free_probability"], 1.0)

    def test_invalid_records_fail(self):
        with self.assertRaises(ValueError):
            aalen_johansen([])
        with self.assertRaises(ValueError):
            aalen_johansen([{"time": 0, "event": "approval"}])
        with self.assertRaises(ValueError):
            aalen_johansen([{"time": 1, "event": "unknown"}])
        with self.assertRaises(ValueError):
            aalen_johansen([{"time": 1}])


if __name__ == "__main__":
    unittest.main()
