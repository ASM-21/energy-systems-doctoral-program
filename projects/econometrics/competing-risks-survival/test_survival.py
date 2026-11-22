import math
import unittest

from survival import (
    aalen_johansen,
    check_probability_mass,
    kaplan_meier_net_approval,
    curve_value_at,
    exponential_competing_risk_cif,
    simulate_exponential_competing_risks,
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

    def test_simulation_matches_analytic_cumulative_incidence(self):
        rates = {"approval": 0.08, "withdrawal": 0.05, "denial": 0.02}
        horizon = 15.0
        records = simulate_exponential_competing_risks(
            20000, rates, horizon, seed=7
        )
        aj = aalen_johansen(records)
        km = kaplan_meier_net_approval(records)
        estimated_cif = curve_value_at(aj, horizon, "cif_approval")
        estimated_net = curve_value_at(km, horizon, "net_approval_probability")
        true_cif = exponential_competing_risk_cif("approval", rates, horizon)
        true_net = 1.0 - math.exp(-rates["approval"] * horizon)
        self.assertAlmostEqual(estimated_cif, true_cif, delta=0.015)
        self.assertAlmostEqual(estimated_net, true_net, delta=0.015)
        self.assertGreater(estimated_net, estimated_cif + 0.15)

    def test_simulation_is_reproducible_and_validates_inputs(self):
        rates = {"approval": 0.08, "withdrawal": 0.05, "denial": 0.02}
        self.assertEqual(
            simulate_exponential_competing_risks(20, rates, 10, seed=4),
            simulate_exponential_competing_risks(20, rates, 10, seed=4),
        )
        with self.assertRaises(ValueError):
            simulate_exponential_competing_risks(0, rates, 10)
        with self.assertRaises(ValueError):
            simulate_exponential_competing_risks(10, rates, float("inf"))
        with self.assertRaises(ValueError):
            simulate_exponential_competing_risks(10, {"approval": 1}, 10)

    def test_invalid_records_fail(self):
        with self.assertRaises(ValueError):
            aalen_johansen([])
        with self.assertRaises(ValueError):
            aalen_johansen([{"time": 0, "event": "approval"}])
        with self.assertRaises(ValueError):
            aalen_johansen([{"time": 1, "event": "unknown"}])
        with self.assertRaises(ValueError):
            aalen_johansen([{"time": float("nan"), "event": "approval"}])
        with self.assertRaises(ValueError):
            aalen_johansen([{"time": float("inf"), "event": "approval"}])
        with self.assertRaises(ValueError):
            aalen_johansen([{"time": 1}])


if __name__ == "__main__":
    unittest.main()
