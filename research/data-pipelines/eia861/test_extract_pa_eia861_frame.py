import unittest
from io import BytesIO
from openpyxl import Workbook

from extract_pa_eia861_frame import parse_frame_workbook, audit_frame_year


class PennsylvaniaFrameAuditTests(unittest.TestCase):
    def test_extracts_form_ownership_and_schedule_flags(self):
        wb = Workbook()
        ws = wb.active
        ws.append(["Data Year", "Utility Number", "Utility Name", "Short Form",
                   "Ownership Code", "Ownership", "Net Metering"])
        ws.append([2025, 14715, "PPL Electric Utilities Corp", "", "I",
                   "Investor Owned", "X"])
        ws.append([2025, 66101, "FirstEnergy Pennsylvania Electric Co", "",
                   "I", "Investor Owned", "X"])
        stream = BytesIO()
        wb.save(stream)
        rows = parse_frame_workbook(stream.getvalue(), 2025)
        self.assertEqual(len(rows), 2)
        self.assertEqual(rows[0]["eia_utility_id"], "14715")
        self.assertEqual(rows[0]["net_metering_reported"], "X")
        self.assertEqual(rows[0]["short_form"], "")
        self.assertEqual(rows[0]["ownership"], "Investor Owned")

    def test_audit_preserves_missing_and_duplicate_frame_ids(self):
        frame = [
            {"year": 2025, "eia_utility_id": "14715", "frame_utility_name": "PPL"},
            {"year": 2025, "eia_utility_id": "14715", "frame_utility_name": "PPL duplicate"},
        ]
        rows = audit_frame_year(2025, {"14715", "66101"}, frame)
        statuses = {r["eia_utility_id"]: r["frame_match_status"] for r in rows}
        self.assertEqual(statuses["14715"], "duplicate_frame_id")
        self.assertEqual(statuses["66101"], "not_found_in_frame")


if __name__ == "__main__":
    unittest.main()
