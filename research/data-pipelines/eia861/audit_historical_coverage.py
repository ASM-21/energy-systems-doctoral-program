"""Audit historical EIA-861 ZIPs for utility-level PPL rows by worksheet.

This is a schema/coverage audit, not a harmonized time-series extractor.
"""
from __future__ import annotations
import argparse
import csv
import hashlib
import json
import urllib.request
import zipfile
from datetime import datetime, timezone
from io import BytesIO
from pathlib import Path
from openpyxl import load_workbook

from extract_ppl_eia861 import TARGET_UTILITY_ID, find_header_row, build_headers

BASE_URL = "https://www.eia.gov/electricity/data/eia861/zip/f861{year}.zip"


def inspect_workbook_bytes(data: bytes, year: int, workbook_name: str,
                           utility_id: str = TARGET_UTILITY_ID) -> list[dict]:
    workbook = load_workbook(BytesIO(data), read_only=True, data_only=True)
    records = []
    try:
        for sheet in workbook.worksheets:
            header_row = find_header_row(sheet)
            if header_row is None:
                records.append({"year": year, "workbook": workbook_name, "sheet": sheet.title,
                                "utility_id_column_found": False, "ppl_rows_found": 0,
                                "ppl_utility_name": "", "status": "no utility-number/name header"})
                continue
            headers = build_headers(sheet, header_row)
            utility_columns = [i for i, header in enumerate(headers)
                               if header.lower().endswith("utility_number")]
            if not utility_columns:
                records.append({"year": year, "workbook": workbook_name, "sheet": sheet.title,
                                "utility_id_column_found": False, "ppl_rows_found": 0,
                                "ppl_utility_name": "", "status": "utility-number column not identified"})
                continue
            utility_col = utility_columns[0]
            name_columns = [i for i, header in enumerate(headers)
                            if header.lower().endswith("utility_name")]
            name_col = name_columns[0] if name_columns else None
            hits = []
            for values in sheet.iter_rows(min_row=header_row + 1, values_only=True):
                if utility_col >= len(values) or values[utility_col] is None:
                    continue
                raw_id = values[utility_col]
                normalized_id = str(int(raw_id)) if isinstance(raw_id, float) and raw_id.is_integer() else str(raw_id).strip()
                if normalized_id == str(utility_id):
                    name = str(values[name_col]).strip() if name_col is not None and name_col < len(values) and values[name_col] is not None else ""
                    hits.append(name)
            names = sorted(set(hits))
            if utility_id == TARGET_UTILITY_ID and any(name and "PPL Electric" not in name for name in names):
                raise ValueError(f"EIA ID {utility_id} mapped to unexpected name(s) {names} in {year}/{workbook_name}/{sheet.title}")
            records.append({"year": year, "workbook": workbook_name, "sheet": sheet.title,
                            "utility_id_column_found": True, "ppl_rows_found": len(hits),
                            "ppl_utility_name": "; ".join(names),
                            "status": "PPL rows found" if hits else "no PPL row; absence is not zero"})
    finally:
        workbook.close()
    return records


def download_archive(year: int, cache_dir: Path) -> tuple[Path, dict]:
    cache_dir.mkdir(parents=True, exist_ok=True)
    destination = cache_dir / f"f861{year}.zip"
    url = BASE_URL.format(year=year)
    if destination.exists():
        raw = destination.read_bytes()
        reused = True
    else:
        request = urllib.request.Request(url, headers={"User-Agent": "energy-systems-doctoral-program/1.0"})
        with urllib.request.urlopen(request, timeout=120) as response:
            raw = response.read()
        destination.write_bytes(raw)
        reused = False
    digest = hashlib.sha256(raw).hexdigest()
    return destination, {"year": year, "url": url, "bytes": len(raw), "sha256": digest,
                         "retrieved_utc": datetime.now(timezone.utc).isoformat() if not reused else None,
                         "reused_local_archive": reused}


def audit_year(year: int, cache_dir: Path) -> tuple[list[dict], dict]:
    archive_path, manifest = download_archive(year, cache_dir)
    records = []
    with zipfile.ZipFile(archive_path) as archive:
        bad = archive.testzip()
        if bad:
            raise RuntimeError(f"EIA-861 {year} ZIP CRC failed at {bad}")
        members = [name for name in archive.namelist() if name.lower().endswith((".xlsx", ".xlsm"))]
        manifest["workbook_count"] = len(members)
        for member in members:
            records.extend(inspect_workbook_bytes(archive.read(member), year, Path(member).name))
    manifest["worksheet_count"] = len(records)
    manifest["worksheets_with_ppl_rows"] = sum(row["ppl_rows_found"] > 0 for row in records)
    manifest["sheets_with_utility_id_field"] = sum(row["utility_id_column_found"] for row in records)
    return records, manifest


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--start-year", type=int, default=2015)
    parser.add_argument("--end-year", type=int, default=2025)
    parser.add_argument("--cache-dir", type=Path, default=Path("data/historical-archives"))
    parser.add_argument("--output-dir", type=Path, default=Path("outputs/historical-coverage"))
    args = parser.parse_args()
    if args.start_year > args.end_year:
        parser.error("start year must be <= end year")
    all_records, manifests = [], []
    for year in range(args.start_year, args.end_year + 1):
        records, manifest = audit_year(year, args.cache_dir)
        all_records.extend(records)
        manifests.append(manifest)
        print(f"{year}: {manifest['workbook_count']} workbooks, {manifest['worksheets_with_ppl_rows']} worksheets with PPL rows")
    args.output_dir.mkdir(parents=True, exist_ok=True)
    fields = ["year", "workbook", "sheet", "utility_id_column_found", "ppl_rows_found", "ppl_utility_name", "status"]
    with (args.output_dir / "historical_ppl_coverage.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(all_records)
    summary = {"utility_id": TARGET_UTILITY_ID, "start_year": args.start_year,
               "end_year": args.end_year, "archives": manifests,
               "total_worksheets_scanned": len(all_records),
               "worksheets_with_ppl_rows": sum(row["ppl_rows_found"] > 0 for row in all_records),
               "warning": "Missing utility-level rows are reporting-coverage gaps, not zero values. Schema and survey definitions may change by year."}
    (args.output_dir / "manifest.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(f"Historical coverage audit: {args.output_dir.resolve()}")


if __name__ == "__main__":
    main()
