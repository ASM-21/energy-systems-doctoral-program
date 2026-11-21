import unittest

from audit_pa_utility_panel import audit_panel


class PennsylvaniaPanelAuditTests(unittest.TestCase):
    def setUp(self):
        self.rows = [
            {"year": "2022", "eia_utility_id": "14715",
             "utility_name": "PPL Electric Utilities Corp", "state": "PA",
             "pv_capacity": "300"},
            {"year": "2023", "eia_utility_id": "14715",
             "utility_name": "PPL Electric Utilities", "state": "PA",
             "pv_capacity": "350"},
            {"year": "2023", "eia_utility_id": "14341",
             "utility_name": "PECO Energy Company", "state": "PA",
             "pv_capacity": "200"},
            {"year": "2023", "eia_utility_id": "14341",
             "utility_name": "PECO Energy Company", "state": "PA",
             "pv_capacity": "201"},
            {"year": "2023", "eia_utility_id": "99999",
             "utility_name": "Out of state", "state": "NJ",
             "pv_capacity": "1"},
        ]

    def test_reports_year_coverage_and_missing_year(self):
        result = audit_panel(self.rows, 2022, 2024)
        self.assertEqual(
            [item["unique_utility_ids"] for item in result["year_coverage"]],
            [1, 2, 0],
        )
        self.assertEqual(result["year_coverage"][2]["utility_rows"], 0)

    def test_flags_duplicate_year_utility_key(self):
        result = audit_panel(self.rows, 2022, 2023)
        self.assertEqual(result["duplicate_year_utility_rows"], [
            {"year": 2023, "eia_utility_id": "14341", "row_count": 2}
        ])

    def test_preserves_name_variants_without_merging(self):
        result = audit_panel(self.rows, 2022, 2023)
        ppl = next(x for x in result["identity_history"]
                   if x["eia_utility_id"] == "14715")
        self.assertTrue(ppl["name_changes_or_variants"])
        self.assertEqual(len(ppl["names_observed"]), 2)

    def test_flags_out_of_range_and_invalid_identity_rows(self):
        rows = self.rows + [
            {"year": "2025", "eia_utility_id": "1", "state": "PA"},
            {"year": "bad", "eia_utility_id": "2", "state": "PA"},
        ]
        result = audit_panel(rows, 2022, 2023)
        self.assertEqual(len(result["invalid_rows"]), 2)
        self.assertIn("no variable harmonization", result["measurement_status"])


if __name__ == "__main__":
    unittest.main()
