import unittest
from io import BytesIO

from openpyxl import Workbook
from extract_pa_utility_net_metering import extract_state_workbook


def make_workbook() -> bytes:
    workbook = Workbook()
    sheet = workbook.active
    sheet.title = "Net_Metering_States"
    sheet.append(["Utility Number", "Utility Name", "State", "PV Capacity MW Total"])
    sheet.append([14715, "PPL Electric Utilities Corp", "PA", 505.746])
    sheet.append([14341, "PECO Energy Company", "PA", 310.25])
    sheet.append([99999, "Example New York Utility", "NY", 12.0])
    output = BytesIO()
    workbook.save(output)
    return output.getvalue()


class PennsylvaniaUtilityExtractionTests(unittest.TestCase):
    def test_extracts_all_state_utility_rows_and_excludes_other_states(self):
        rows, schemas = extract_state_workbook(
            make_workbook(), 2025, "Net_Metering_2025.xlsx", "a" * 64, "PA"
        )
        self.assertEqual(len(rows), 2)
        self.assertEqual({row["eia_utility_id"] for row in rows}, {"14715", "14341"})
        self.assertTrue(all(row["state"] == "PA" for row in rows))
        self.assertEqual({row["utility_name"] for row in rows},
                         {"PPL Electric Utilities Corp", "PECO Energy Company"})
        self.assertEqual(rows[0]["source_sheet"], "Net_Metering_States")
        self.assertEqual(len(schemas), 1)

    def test_empty_state_selection_returns_empty_rows(self):
        rows, schemas = extract_state_workbook(
            make_workbook(), 2025, "Net_Metering_2025.xlsx", "b" * 64, "NJ"
        )
        self.assertEqual(rows, [])
        self.assertEqual(schemas, [])


if __name__ == "__main__":
    unittest.main()
