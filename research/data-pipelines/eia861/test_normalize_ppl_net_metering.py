import csv
import tempfile
import unittest
from pathlib import Path

from normalize_ppl_net_metering import normalized_row, normalize_file, parse_number


class NormalizePPLNetMeteringTests(unittest.TestCase):
    def test_missing_values_remain_missing_not_zero(self):
        self.assertIsNone(parse_number("."))
        self.assertIsNone(parse_number(""))
        self.assertEqual(parse_number("0"), 0.0)

    def test_normalizes_2015_schema_and_flags_unknown_capacity_basis(self):
        raw = {
            "year": "2015", "eia_utility_id": "14715", "utility_name": "PPL Electric Utilities Corp",
            "source_workbook": "Net_Metering_2015.xlsx", "source_sheet": "Net_Metering_States",
            "source_row": "693", "archive_sha256": "hash",
            "Photovoltaic__Capacity_MW__Total": "76.686",
            "Photovoltaic__Customers__Total": "3554", "Total__Capacity_MW": "98.919",
            "Photovoltaic__Virtual_Capacity_(MW)__Total": "",
            "Utility_Characteristics__State": "PA",
        }
        row = normalized_row(raw)
        self.assertEqual(row["standard_net_metered_pv_capacity_mw"], 76.686)
        self.assertEqual(row["pv_count_measure"], "customers")
        self.assertIsNone(row["virtual_pv_capacity_mw"])
        self.assertEqual(row["pv_capacity_basis"], "not separately reported")

    def test_normalizes_new_virtual_capacity_bands(self):
        raw = {
            "year": "2025", "eia_utility_id": "14715", "utility_name": "PPL Electric Utilities Corp",
            "source_workbook": "Net_Metering_2025.xlsx", "source_sheet": "States- Utility Level",
            "source_row": "760", "archive_sha256": "hash",
            "Photovoltaic__Capacity_MW__Total": "505.746",
            "Photovoltaic__Installations__Total": "31400",
            "Photovoltaic__Virtual_Capacity_(MW)__Total": "",
            "Photovoltaic__Virtual_Capacity-_1_MW_and_over_(MW)__Total": "10.3",
            "Photovoltaic__Virtual_Capacity-_under_1_MW_(MW)__Total": "23.174",
            "Photovoltaic__Capacity_MW__Type": "AC",
            "All_Technologies__Capacity_MW__Total": "577.707",
            "Utility_Characteristics__State": "PA", "Utility_Characteristics__BA_Code": "PJM",
        }
        row = normalized_row(raw)
        self.assertEqual(row["standard_net_metered_pv_capacity_mw"], 505.746)
        self.assertEqual(row["pv_count_measure"], "installations")
        self.assertEqual(row["virtual_pv_capacity_mw"], 33.474)
        self.assertEqual(row["all_technology_net_metered_capacity_mw"], 577.707)
        self.assertEqual(row["pv_capacity_basis"], "AC")

    def test_builds_annual_change_and_summary(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "raw.csv"
            fields = ["year", "eia_utility_id", "utility_name", "source_workbook", "source_sheet",
                      "source_row", "archive_sha256", "Photovoltaic__Capacity_MW__Total",
                      "Photovoltaic__Customers__Total", "Photovoltaic__Capacity_MW__Type", "Utility_Characteristics__State"]
            with source.open("w", newline="", encoding="utf-8") as handle:
                writer = csv.DictWriter(handle, fieldnames=fields)
                writer.writeheader()
                writer.writerow({"year": 2015, "eia_utility_id": 14715, "utility_name": "PPL Electric Utilities Corp",
                                 "source_workbook": "2015.xlsx", "source_sheet": "States", "source_row": 1,
                                 "archive_sha256": "a", "Photovoltaic__Capacity_MW__Total": 76.686,
                                 "Photovoltaic__Customers__Total": 3554, "Photovoltaic__Capacity_MW__Type": "AC", "Utility_Characteristics__State": "PA"})
                writer.writerow({"year": 2016, "eia_utility_id": 14715, "utility_name": "PPL Electric Utilities Corp",
                                 "source_workbook": "2016.xlsx", "source_sheet": "States", "source_row": 1,
                                 "archive_sha256": "b", "Photovoltaic__Capacity_MW__Total": 92.915,
                                 "Photovoltaic__Customers__Total": 4496, "Photovoltaic__Capacity_MW__Type": "AC", "Utility_Characteristics__State": "PA"})
            summary = normalize_file(source, root / "out")
            self.assertEqual(summary["observations"], 2)
            self.assertAlmostEqual(summary["ac_capacity_change_mw"], 16.229)
            with (root / "out" / "ppl_net_metering_harmonized.csv").open(encoding="utf-8") as handle:
                rows = list(csv.DictReader(handle))
            self.assertEqual(rows[1]["annual_standard_pv_capacity_change_mw"], "16.229")

    def test_rejects_duplicate_year_observations(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "raw.csv"
            fields = ["year", "eia_utility_id", "utility_name", "source_workbook", "source_sheet",
                      "source_row", "archive_sha256", "Photovoltaic__Capacity_MW__Total"]
            with source.open("w", newline="", encoding="utf-8") as handle:
                writer = csv.DictWriter(handle, fieldnames=fields)
                writer.writeheader()
                for _ in range(2):
                    writer.writerow({"year": 2025, "eia_utility_id": 14715, "utility_name": "PPL Electric Utilities Corp",
                                     "source_workbook": "2025.xlsx", "source_sheet": "States", "source_row": 1,
                                     "archive_sha256": "a", "Photovoltaic__Capacity_MW__Total": 1})
            with self.assertRaises(ValueError):
                normalize_file(source, root / "out")

    def test_does_not_calculate_change_across_unknown_to_ac_basis_break(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "raw.csv"
            fields = ["year", "eia_utility_id", "utility_name", "source_workbook", "source_sheet",
                      "source_row", "archive_sha256", "Photovoltaic__Capacity_MW__Total",
                      "Photovoltaic__Capacity_MW__Type"]
            with source.open("w", newline="", encoding="utf-8") as handle:
                writer = csv.DictWriter(handle, fieldnames=fields)
                writer.writeheader()
                writer.writerow({"year": 2015, "eia_utility_id": 14715, "utility_name": "PPL Electric Utilities Corp",
                                 "source_workbook": "2015.xlsx", "source_sheet": "States", "source_row": 1,
                                 "archive_sha256": "a", "Photovoltaic__Capacity_MW__Total": 76.686,
                                 "Photovoltaic__Capacity_MW__Type": ""})
                writer.writerow({"year": 2016, "eia_utility_id": 14715, "utility_name": "PPL Electric Utilities Corp",
                                 "source_workbook": "2016.xlsx", "source_sheet": "States", "source_row": 1,
                                 "archive_sha256": "b", "Photovoltaic__Capacity_MW__Total": 92.915,
                                 "Photovoltaic__Capacity_MW__Type": "AC"})
            normalize_file(source, root / "out")
            with (root / "out" / "ppl_net_metering_harmonized.csv").open(encoding="utf-8") as handle:
                rows = list(csv.DictReader(handle))
            self.assertEqual(rows[1]["annual_standard_pv_capacity_change_mw"], "")


if __name__ == "__main__":
    unittest.main()
