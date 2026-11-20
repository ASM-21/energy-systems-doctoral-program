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


if __name__ == "__main__":
    unittest.main()