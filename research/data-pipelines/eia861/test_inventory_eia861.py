import json
import tempfile
import unittest
import zipfile
from pathlib import Path
from openpyxl import Workbook
from inventory_eia861 import inventory_archive


class EIA861InventoryTests(unittest.TestCase):
    def test_inventory_extracts_workbook_and_records_sheet_preview(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            workbook_path = root / "Utility_Data_2025.xlsx"
            workbook = Workbook()
            sheet = workbook.active
            sheet.title = "Utility Data"
            sheet.append(["Utility Number", "Utility Name", "State"])
            sheet.append([14715, "PPL Electric Utilities Corp", "PA"])
            workbook.save(workbook_path)
            archive_path = root / "fixture.zip"
            with zipfile.ZipFile(archive_path, "w", zipfile.ZIP_DEFLATED) as archive:
                archive.write(workbook_path, arcname="Utility_Data_2025.xlsx")
            output = root / "out"
            result = inventory_archive(archive_path, output)
            self.assertEqual(result["workbook_count"], 1)
            self.assertEqual(result["sheet_count"], 1)
            inventory = json.loads((output / "workbook_inventory.json").read_text())
            self.assertEqual(inventory[0]["sheet"], "Utility Data")
            self.assertEqual(inventory[0]["preview_rows"][1][1], "PPL Electric Utilities Corp")
            self.assertTrue((output / "workbooks" / "Utility_Data_2025.xlsx").exists())

    def test_rejects_corrupt_zip(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            archive_path = root / "bad.zip"
            archive_path.write_bytes(b"not a zip file")
            with self.assertRaises(zipfile.BadZipFile):
                inventory_archive(archive_path, root / "out")


if __name__ == "__main__":
    unittest.main()