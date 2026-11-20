import unittest
from io import BytesIO
from openpyxl import Workbook

from extract_historical_net_metering import extract_net_metering_workbook


class HistoricalNetMeteringTests(unittest.TestCase):
    def workbook_bytes(self):
        workbook = Workbook()
        sheet = workbook.active
        sheet.title = "States- Utility Level"
        sheet.append(["Utility Characteristics", None, "Net Metering", None])
        sheet.append(["Utility Number", "Utility Name", "PV Capacity MW", "PV Installations"])
        sheet.append([14715, "PPL Electric Utilities Corp", 505.746, 31400])
        sheet.append([99999, "Other Utility", 1.0, 10])
        buffer = BytesIO()
        workbook.save(buffer)
        workbook.close()
        return buffer.getvalue()

    def test_extracts_raw_ppl_row_with_provenance(self):
        rows, schemas = extract_net_metering_workbook(
            self.workbook_bytes(), 2025, "Net_Metering_2025.xlsx", "abc123"
        )
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["year"], 2025)
        self.assertEqual(rows[0]["eia_utility_id"], "14715")
        self.assertEqual(rows[0]["utility_name"], "PPL Electric Utilities Corp")
        self.assertEqual(rows[0]["archive_sha256"], "abc123")
        self.assertEqual(rows[0]["Net_Metering__PV_Capacity_MW"], "505.746")
        self.assertEqual(rows[0]["PV_Installations"], "31400")
        self.assertEqual(schemas[0]["sheet"], "States- Utility Level")

    def test_does_not_treat_other_utility_as_ppl(self):
        rows, _ = extract_net_metering_workbook(
            self.workbook_bytes(), 2025, "Net_Metering_2025.xlsx", "14715"
        )
        self.assertEqual(len(rows), 1)


if __name__ == "__main__":
    unittest.main()
