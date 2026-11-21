import unittest
from pathlib import Path

from analyze_pa_edc_interconnection import analyze, read_rows


DATA = Path(__file__).with_name("pa_edc_interconnection_2023_2025.csv")


class PaEdcPeerComparisonTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.result = analyze(read_rows(DATA))

    def test_all_edc_level_counts_reconcile_to_official_totals(self):
        self.assertEqual(
            [row["computed_statewide_requests"] for row in self.result["annual_peer_comparison"]],
            [19202, 18582, 20202],
        )
        self.assertTrue(all(row["statewide_total_reconciles"]
                            for row in self.result["annual_peer_comparison"]))

    def test_ppl_remains_largest_edc_by_request_volume(self):
        self.assertEqual(
            [row["ppl_rank_by_total_requests"] for row in self.result["annual_peer_comparison"]],
            [1, 1, 1],
        )

    def test_2025_ppl_share_and_large_project_concentration(self):
        latest = self.result["annual_peer_comparison"][-1]
        self.assertAlmostEqual(latest["ppl_share_of_statewide_requests_pct"], 33.88, places=2)
        large = self.result["latest_year_large_request_composition"]
        self.assertEqual(large["ppl_level2_ge500kw_requests"], 135)
        self.assertEqual(large["statewide_level2_ge500kw_requests"], 196)
        self.assertEqual(large["ppl_level3_ge500kw_requests"], 411)
        self.assertEqual(large["statewide_level3_ge500kw_requests"], 954)


if __name__ == "__main__":
    unittest.main()
