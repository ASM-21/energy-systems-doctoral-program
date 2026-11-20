import tempfile
import unittest
from pathlib import Path
from openpyxl import Workbook
from extract_ppl_eia861 import extract_ppl_rows


class ExtractPPLRowsTests(unittest.TestCase):
    def test_extracts_utility_rows_and_preserves_multilevel_headers(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            workbooks = root / "workbooks"
            workbooks.mkdir()
            workbook = Workbook()
            sheet = workbook.active
            sheet.title = "Net Metering"
            sheet.append(["Utility Characteristics", None, "Photovoltaic", None])
            sheet.append(["", None, "Capacity MW", None])
            sheet.append(["Year", "Utility Number", "Residential", "Total"])
            sheet.append([2025, 14715, 12.5, 12.5])
            sheet.append([2025, 99999, 3.0, 3.0])
            workbook.save(workbooks / "Net_Metering_2025.xlsx")
            result = extract_ppl_rows(workbooks, root / "out")
            self.assertEqual(result["sheets_with_ppl_rows"], 1)
            self.assertEqual(result["long_form_records"], 4)
            text = (root / "out" / "ppl_eia861_2025_long.csv").read_text()
            self.assertIn("Photovoltaic__Capacity_MW__Residential", text)
            self.assertIn("12.5", text)

    def test_missing_utility_row_is_not_interpreted_as_zero(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            workbooks = root / "workbooks"
            workbooks.mkdir()
            workbook = Workbook()
            sheet = workbook.active
            sheet.append(["Data Year", "Utility Number", "Utility Name"])
            sheet.append([2025, 99999, "Other Utility"])
            workbook.save(workbooks / "Example.xlsx")
            result = extract_ppl_rows(workbooks, root / "out")
            self.assertEqual(result["long_form_records"], 0)
            coverage = (root / "out" / "ppl_eia861_2025_coverage.csv").read_text()
            self.assertIn("absence is not zero", coverage)

    def test_sheet_without_utility_identity_is_recorded_as_not_applicable(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            workbooks = root / "workbooks"
            workbooks.mkdir()
            workbook = Workbook()
            sheet = workbook.active
            sheet.append(["State", "Sector", "Capacity"])
            sheet.append(["PA", "Residential", 12.5])
            workbook.save(workbooks / "Aggregate.xlsx")
            result = extract_ppl_rows(workbooks, root / "out")
            self.assertEqual(result["sheets_scanned"], 1)
            self.assertEqual(result["sheets_with_ppl_rows"], 0)
            coverage = (root / "out" / "ppl_eia861_2025_coverage.csv").read_text()
            self.assertIn("no utility-number/name header", coverage)

    def test_rejects_unexpected_name_for_ppl_utility_id(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            workbooks = root / "workbooks"
            workbooks.mkdir()
            workbook = Workbook()
            sheet = workbook.active
            sheet.append(["Utility Number", "Utility Name", "Capacity"])
            sheet.append([14715, "Incorrect Utility Name", 1.0])
            workbook.save(workbooks / "Bad.xlsx")
            with self.assertRaises(ValueError):
                extract_ppl_rows(workbooks, root / "out")


if __name__ == "__main__":
    unittest.main()