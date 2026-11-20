import unittest
from io import BytesIO
from openpyxl import Workbook

from audit_historical_coverage import inspect_workbook_bytes


class HistoricalCoverageTests(unittest.TestCase):
    def make_workbook(self, rows):
        workbook = Workbook()
        sheet = workbook.active
        sheet.title = "Utility Level"
        for row in rows:
            sheet.append(row)
        buffer = BytesIO()
        workbook.save(buffer)
        workbook.close()
        return buffer.getvalue()

    def test_detects_ppl_utility_row(self):
        data = self.make_workbook([
            ["Utility Number", "Utility Name", "Capacity MW"],
            [14715, "PPL Electric Utilities Corp", 505.746],
            [99999, "Other Utility", 1.0],
        ])
        rows = inspect_workbook_bytes(data, 2025, "Net_Metering_2025.xlsx")
        self.assertEqual(rows[0]["ppl_rows_found"], 1)
        self.assertEqual(rows[0]["ppl_utility_name"], "PPL Electric Utilities Corp")

    def test_missing_utility_row_is_explicit(self):
        data = self.make_workbook([
            ["Utility Number", "Utility Name", "Capacity MW"],
            [99999, "Other Utility", 1.0],
        ])
        rows = inspect_workbook_bytes(data, 2020, "Example.xlsx")
        self.assertEqual(rows[0]["ppl_rows_found"], 0)
        self.assertIn("absence is not zero", rows[0]["status"])

    def test_aggregate_sheet_is_not_misclassified_as_utility_level(self):
        data = self.make_workbook([["State", "Capacity"], ["PA", 10]])
        rows = inspect_workbook_bytes(data, 2025, "Aggregate.xlsx")
        self.assertFalse(rows[0]["utility_id_column_found"])
        self.assertEqual(rows[0]["ppl_rows_found"], 0)

    def test_rejects_conflicting_name_for_ppl_id(self):
        data = self.make_workbook([
            ["Utility Number", "Utility Name", "Capacity MW"],
            [14715, "Wrong Company", 1.0],
        ])
        with self.assertRaises(ValueError):
            inspect_workbook_bytes(data, 2025, "Bad.xlsx")


if __name__ == "__main__":
    unittest.main()
