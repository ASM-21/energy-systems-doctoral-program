import csv
import re
import unittest
from pathlib import Path

DATA = Path(__file__).parent / "data" / "ppl_net_metering_harmonized.csv"


class PPLNetMeteringSnapshotTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with DATA.open(newline="", encoding="utf-8") as handle:
            cls.rows = list(csv.DictReader(handle))

    def test_snapshot_has_one_ppl_row_for_each_year_2015_to_2025(self):
        years = [int(row["year"]) for row in self.rows]
        self.assertEqual(years, list(range(2015, 2026)))
        self.assertTrue(all(row["eia_utility_id"] == "14715" for row in self.rows))

    def test_ac_basis_and_2015_break_are_explicit(self):
        self.assertEqual(self.rows[0]["pv_capacity_basis"], "not separately reported")
        self.assertEqual(self.rows[0]["annual_standard_pv_capacity_change_mw"], "")
        self.assertEqual(self.rows[0]["capacity_basis_source_field"], "")
        self.assertEqual(self.rows[0]["virtual_pv_source_field"], "")
        self.assertTrue(all(row["pv_capacity_basis"] == "AC" for row in self.rows[1:]))
        self.assertEqual(self.rows[1]["annual_standard_pv_capacity_change_mw"], "")

    def test_endpoints_match_research_note(self):
        self.assertEqual(float(self.rows[1]["standard_net_metered_pv_capacity_mw"]), 92.915)
        self.assertEqual(float(self.rows[-1]["standard_net_metered_pv_capacity_mw"]), 505.746)
        self.assertEqual(float(self.rows[-1]["annual_standard_pv_capacity_change_mw"]), 91.415)
        self.assertEqual(float(self.rows[1]["pv_residential_capacity_mw"]), 29.061)
        self.assertEqual(float(self.rows[1]["pv_commercial_capacity_mw"]), 52.823)
        self.assertEqual(float(self.rows[-1]["pv_residential_capacity_mw"]), 277.812)
        self.assertEqual(float(self.rows[-1]["pv_commercial_capacity_mw"]), 195.427)
        self.assertEqual(float(self.rows[-1]["pv_industrial_capacity_mw"]), 32.507)
        self.assertEqual(self.rows[-1]["pv_transportation_capacity_mw"], "")

    def test_source_archive_hashes_are_sha256(self):
        for row in self.rows:
            self.assertRegex(row["archive_sha256"], re.compile(r"^[0-9a-f]{64}$"))

    def test_count_measure_break_is_retained(self):
        self.assertTrue(all(row["pv_count_measure"] == "customers" for row in self.rows[:6]))
        self.assertTrue(all(row["pv_count_measure"] == "installations" for row in self.rows[6:]))


if __name__ == "__main__":
    unittest.main()
