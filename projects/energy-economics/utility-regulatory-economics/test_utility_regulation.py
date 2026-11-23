import math
import unittest

from utility_regulation import (
    allocate_cost_pools, annuity_factor, class_totals, expected_npv,
    incentive_scenarios, npv, representative_bill, three_part_rates,
)


class AllocationTests(unittest.TestCase):
    def setUp(self):
        self.pools = {"customer": 40_000_000, "demand": 35_000_000, "energy": 25_000_000}
        self.det = {
            "customer": {"residential": 100_000, "commercial": 20_000},
            "demand": {"residential": 200_000, "commercial": 100_000},
            "energy": {"residential": 1_200_000_000, "commercial": 800_000_000},
        }

    def test_allocation_reconciles_by_pool_and_class(self):
        allocations = allocate_cost_pools(self.pools, self.det)
        totals = class_totals(allocations)
        for pool, amount in self.pools.items():
            self.assertAlmostEqual(sum(allocations[pool].values()), amount, places=5)
        self.assertAlmostEqual(totals["residential"], 71_666_666.6667, places=2)
        self.assertAlmostEqual(totals["commercial"], 28_333_333.3333, places=2)
        self.assertAlmostEqual(sum(totals.values()), 100_000_000, places=5)

    def test_invalid_inputs(self):
        for pools, det in [
            ({"x": 1}, {"y": {"A": 1}}),
            ({"x": math.nan}, {"x": {"A": 1}}),
            ({"x": -1}, {"x": {"A": 1}}),
            ({"x": 1}, {"x": {"A": 0}}),
        ]:
            with self.assertRaises(ValueError):
                allocate_cost_pools(pools, det)


class RateTests(unittest.TestCase):
    def test_rates_and_representative_bill(self):
        rates = three_part_rates(40_000_000, 35_000_000, 25_000_000, 120_000, 300_000, 2_000_000_000)
        self.assertAlmostEqual(rates["fixed_per_account_month"], 27.7777777778)
        self.assertAlmostEqual(rates["demand_per_kw_month"], 9.7222222222)
        self.assertAlmostEqual(rates["energy_per_kwh"], 0.0125)
        total = rates["fixed_per_account_month"] * 120_000 * 12 + rates["demand_per_kw_month"] * 300_000 * 12 + rates["energy_per_kwh"] * 2_000_000_000
        self.assertAlmostEqual(total, 100_000_000, places=5)
        bill = representative_bill(rates, 10_000, 5)
        self.assertAlmostEqual(bill["total_annual"], 1041.6666667, places=5)

    def test_invalid_rate_determinants(self):
        with self.assertRaises(ValueError):
            three_part_rates(1, 1, 1, 0, 1, 1)
        with self.assertRaises(ValueError):
            three_part_rates(1, 1, 1, 1, 1, 1, months=0)


class IncentiveTests(unittest.TestCase):
    def test_savings_and_sharing(self):
        rows = incentive_scenarios([104, 108.16, 112.49], [5, 5, 5], [2, 0, 0], 100, 0.5)
        self.assertEqual([r["incremental_utility_operating_position"] for r in rows], [3, 5, 5])
        self.assertEqual([r["sharing_customer_savings"] for r in rows], [1.5, 2.5, 2.5])
        self.assertEqual([r["sharing_utility_retained"] for r in rows], [1.5, 2.5, 2.5])

    def test_bad_sharing_or_negative_cost(self):
        with self.assertRaises(ValueError):
            incentive_scenarios([10], [1], [0], 10, 1.1)
        with self.assertRaises(ValueError):
            incentive_scenarios([10], [11], [0], 10, 0.5)


class CapitalBudgetingTests(unittest.TestCase):
    def test_npv_and_annuity_factor(self):
        self.assertAlmostEqual(annuity_factor(0.07, 10), 7.0235815409)
        self.assertAlmostEqual(npv(30, [5] * 10, 0.07), 5.1179077047)
        self.assertEqual(annuity_factor(0, 10), 10)

    def test_expected_npv(self):
        result = expected_npv(30, {"low": 3, "base": 5, "high": 8},
                              {"low": 0.25, "base": 0.5, "high": 0.25}, 0.07, 10)
        self.assertAlmostEqual(result["expected_npv"], 6.8738030899)
        self.assertAlmostEqual(result["npv_low"], -8.9292553772)
        self.assertAlmostEqual(result["npv_high"], 26.1886523275)

    def test_invalid_discount_and_probabilities(self):
        with self.assertRaises(ValueError):
            annuity_factor(-1, 10)
        with self.assertRaises(ValueError):
            expected_npv(30, {"a": 1, "b": 2}, {"a": 0.2, "b": 0.2}, 0.07, 10)


if __name__ == "__main__":
    unittest.main()
