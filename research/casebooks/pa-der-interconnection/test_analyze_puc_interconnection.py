import unittest
from pathlib import Path

from analyze_puc_interconnection import analyze, load_rows


DATA = Path(__file__).with_name("ppl_interconnection_2023_2025.csv")


class PucInterconnectionAnalysisTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows = load_rows(DATA)
        cls.result = analyze(cls.rows)

    def test_request_level_counts_reconcile(self):
        self.assertTrue(all(row["request_total_reconciles"]
                            for row in self.result["annual_quality_checks"]))

    def test_2025_size_bands_reconcile_to_level_totals(self):
        latest = self.result["latest_year"]
        self.assertEqual(latest["level2_requests_from_size_bands"], 2425)
        self.assertEqual(latest["level3_requests_from_size_bands"], 411)

    def test_two_year_descriptive_changes(self):
        changes = self.result["descriptive_changes_first_to_last_pct"]
        self.assertAlmostEqual(changes["customer_generators"], 46.40, places=2)
        self.assertAlmostEqual(changes["interconnected_capacity_kw"], 53.78, places=2)
        self.assertAlmostEqual(changes["annual_interconnection_requests"], -9.56, places=2)

    def test_2025_status_reconciliation_is_flagged_not_hidden(self):
        checks = {row["year"]: row for row in self.result["annual_quality_checks"]}
        self.assertEqual(checks[2023]["status_gap_vs_submitted"], 0)
        self.assertEqual(checks[2024]["status_gap_vs_submitted"], 0)
        self.assertEqual(checks[2025]["status_gap_vs_submitted"], 357)
        self.assertEqual(
            checks[2025]["reported_completed_minus_approved_denied_cancelled"],
            592
        )
        self.assertTrue(checks[2025]["reported_completed_includes_pending_edc_arithmetic"])
        self.assertFalse(checks[2025]["status_reconciles_to_submitted"])


if __name__ == "__main__":
    unittest.main()
