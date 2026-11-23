import unittest
from pathlib import Path

from analyze import DEFAULT_INPUT, analyze, build_provenance, load_panel, validate_panel


class PaDistributionInterconnectionCapstoneTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows = load_panel(DEFAULT_INPUT)
        cls.result = analyze(cls.rows)

    def test_panel_is_balanced_and_census_totals_reconcile(self):
        self.assertEqual(len(self.rows), 33)
        self.assertEqual([x["statewide_requests"] for x in self.result["annual_summary"]],
                         [19202, 18582, 20202])
        self.assertEqual([x["edc_count"] for x in self.result["annual_summary"]], [11, 11, 11])

    def test_ppl_rank_share_and_trend(self):
        annual = self.result["annual_summary"]
        self.assertEqual([x["ppl_rank"] for x in annual], [1, 1, 1])
        self.assertEqual([x["ppl_requests"] for x in annual], [7567, 7519, 6844])
        self.assertEqual([x["ppl_request_share_pct"] for x in annual], [39.41, 40.46, 33.88])
        ppl_2025 = next(row for row in self.result["edc_year_panel"]
                        if row["reporting_year"] == 2025 and row["edc"] == "PPL")
        self.assertAlmostEqual(
            ppl_2025["change_from_prior_reporting_year_pct"], -8.98, places=2
        )

    def test_ppl_long_run_trend_and_top_three_concentration(self):
        annual = self.result["annual_summary"]
        self.assertEqual(
            [row["ppl_change_from_2023_pct"] for row in annual],
            [0.0, -0.63, -9.55],
        )
        self.assertEqual(
            [row["top_three_edc_request_share_pct"] for row in annual],
            [76.68, 77.13, 70.68],
        )

    def test_request_count_concentration_is_not_market_hhi(self):
        annual = self.result["annual_summary"]
        self.assertAlmostEqual(annual[0]["request_count_hhi"], 2487.17, places=2)
        self.assertAlmostEqual(annual[1]["request_count_hhi"], 2496.32, places=2)
        self.assertAlmostEqual(annual[2]["request_count_hhi"], 2072.92, places=2)
        self.assertTrue(any("not a market-power" in item
                            for item in self.result["interpretation_limits"]))

    def test_large_request_split_is_2025_only(self):
        large = self.result["ppl_2025_large_request_composition"]
        self.assertEqual(large["level2_ge500kw_requests"], 135)
        self.assertEqual(large["statewide_level2_ge500kw_requests"], 196)
        self.assertEqual(large["level3_ge500kw_requests"], 411)
        self.assertEqual(large["statewide_level3_ge500kw_requests"], 954)

    def test_provenance_hash_is_reproducible_sha256(self):
        provenance = build_provenance(DEFAULT_INPUT)
        self.assertEqual(len(provenance["source_dataset_sha256"]), 64)
        self.assertEqual(provenance["reporting_period"], "June 1 through May 31; reporting years 2023-2025")
        self.assertEqual(provenance["source_dataset_path"], "research/casebooks/pa-der-interconnection/pa_edc_interconnection_2023_2025.csv")

    def test_reporting_period_and_size_band_integrity(self):
        bad_period = [dict(row) for row in self.rows]
        bad_period[0]["period_start"] = "2022-07-01"
        with self.assertRaises(ValueError):
            validate_panel(bad_period)

        bad_size = [dict(row) for row in self.rows]
        target = next(row for row in bad_size
                      if row["reporting_year"] == "2025" and row["edc"] == "PPL")
        target["level3_ge500kw_requests"] = "410"
        with self.assertRaises(ValueError):
            validate_panel(bad_size)

    def test_negative_subcategory_count_fails(self):
        bad = [dict(row) for row in self.rows]
        target = next(row for row in bad
                      if row["reporting_year"] == "2025" and row["edc"] == "PPL")
        target["level2_ge500kw_requests"] = "-1"
        with self.assertRaises(ValueError):
            validate_panel(bad)

    def test_duplicate_and_nonreconciling_rows_fail(self):
        duplicate = self.rows + [dict(self.rows[0])]
        with self.assertRaises(ValueError):
            validate_panel(duplicate)
        broken = [dict(row) for row in self.rows]
        broken[0]["total_requests"] = str(int(broken[0]["total_requests"]) + 1)
        with self.assertRaises(ValueError):
            validate_panel(broken)


if __name__ == "__main__":
    unittest.main()
