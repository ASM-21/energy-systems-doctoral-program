"""Download and inventory the official EIA-861 final workbook package."""
from __future__ import annotations
import argparse
import csv
import hashlib
import json
import urllib.request
import zipfile
from datetime import datetime, timezone
from pathlib import Path
from openpyxl import load_workbook

DATA_URL = "https://www.eia.gov/electricity/data/eia861/zip/f8612025.zip"
TARGET_EIA_UTILITY_ID = "14715"  # PPL Electric Utilities Corp; verify against the downloaded utility frame.

def download(url: str, destination: Path) -> dict:
    destination.parent.mkdir(parents=True, exist_ok=True)
    request = urllib.request.Request(url, headers={"User-Agent": "energy-systems-doctoral-program/1.0"})
    digest = hashlib.sha256()
    size = 0
    with urllib.request.urlopen(request, timeout=120) as response, destination.open("wb") as output:
        while True:
            chunk = response.read(1024 * 1024)
            if not chunk:
                break
            output.write(chunk)
            digest.update(chunk)
            size += len(chunk)
    return {"url": url, "retrieved_utc": datetime.now(timezone.utc).isoformat(),
            "bytes": size, "sha256": digest.hexdigest()}

def inventory_archive(archive_path: Path, output_dir: Path) -> dict:
    output_dir.mkdir(parents=True, exist_ok=True)
    records = []
    with zipfile.ZipFile(archive_path) as archive:
        bad_member = archive.testzip()
        if bad_member:
            raise RuntimeError(f"ZIP CRC check failed for {bad_member}")
        workbook_members = [name for name in archive.namelist()
                            if name.lower().endswith((".xlsx", ".xlsm"))]
        for member in workbook_members:
            extracted = output_dir / "workbooks" / Path(member).name
            extracted.parent.mkdir(parents=True, exist_ok=True)
            extracted.write_bytes(archive.read(member))
            workbook = load_workbook(extracted, read_only=True, data_only=True)
            for sheet in workbook.worksheets:
                preview = []
                for row in sheet.iter_rows(min_row=1, max_row=min(sheet.max_row or 1, 12),
                                           values_only=True):
                    preview.append([None if value is None else str(value)[:200] for value in row[:20]])
                records.append({
                    "workbook": Path(member).name,
                    "archive_member": member,
                    "sheet": sheet.title,
                    "max_row_reported": sheet.max_row,
                    "max_column_reported": sheet.max_column,
                    "preview_rows": preview,
                })
            workbook.close()
    (output_dir / "workbook_inventory.json").write_text(
        json.dumps(records, indent=2) + "\n", encoding="utf-8"
    )
    with (output_dir / "workbook_inventory.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=["workbook", "archive_member", "sheet",
                                                    "max_row_reported", "max_column_reported"])
        writer.writeheader()
        for record in records:
            writer.writerow({key: record[key] for key in writer.fieldnames})
    return {"workbook_count": len(workbook_members), "sheet_count": len(records),
            "target_eia_utility_id": TARGET_EIA_UTILITY_ID}

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--archive", type=Path, default=Path("data/raw/f8612025.zip"))
    parser.add_argument("--output-dir", type=Path, default=Path("outputs/eia861-2025"))
    parser.add_argument("--url", default=DATA_URL)
    args = parser.parse_args()
    if not args.archive.exists():
        provenance = download(args.url, args.archive)
    else:
        data = args.archive.read_bytes()
        provenance = {"url": args.url, "retrieved_utc": None, "bytes": len(data),
                      "sha256": hashlib.sha256(data).hexdigest(), "reused_local_archive": True}
    result = inventory_archive(args.archive, args.output_dir)
    result["provenance"] = provenance
    (args.output_dir / "manifest.json").write_text(
        json.dumps(result, indent=2) + "\n", encoding="utf-8"
    )
    print(f"EIA-861 archive SHA-256: {provenance['sha256']}")
    print(f"Workbooks: {result['workbook_count']}; worksheets: {result['sheet_count']}")
    print(f"Inventory: {args.output_dir.resolve()}")

if __name__ == "__main__":
    main()