"""Extract raw PPL utility-level net-metering rows from EIA-861 annual ZIPs."""
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

from audit_historical_coverage import archive_url
from extract_ppl_eia861 import TARGET_UTILITY_ID, find_header_row, build_headers


def unique_headers(headers: list[str]) -> list[str]:
    seen: dict[str, int] = {}
    output = []
    for header in headers:
        seen[header] = seen.get(header, 0) + 1
        output.append(header if seen[header] == 1 else f"{header}__duplicate_{seen[header]}")
    return output


def extract_net_metering_workbook(data: bytes, year: int, workbook_name: str,
                                  archive_sha256: str, utility_id: str = TARGET_UTILITY_ID) -> tuple[list[dict], list[dict]]:
    workbook = load_workbook(BytesIO(data), read_only=True, data_only=True)
    rows, schemas = [], []
    try:
        for sheet in workbook.worksheets:
            header_row = find_header_row(sheet)
            if header_row is None:
                continue
            headers = unique_headers(build_headers(sheet, header_row))
            utility_cols = [i for i, name in enumerate(headers) if name.lower().endswith("utility_number")]
            if not utility_cols:
                continue
            utility_col = utility_cols[0]
            for row_number, values in enumerate(sheet.iter_rows(min_row=header_row + 1, values_only=True), start=header_row + 1):
                if utility_col >= len(values) or values[utility_col] is None:
                    continue
                raw_id = values[utility_col]
                normalized_id = str(int(raw_id)) if isinstance(raw_id, float) and raw_id.is_integer() else str(raw_id).strip()
                if normalized_id != str(utility_id):
                    continue
                record = {"year": year, "eia_utility_id": utility_id,
                          "utility_name": "", "source_workbook": workbook_name,
                          "source_sheet": sheet.title, "source_row": row_number,
                          "archive_sha256": archive_sha256}
                for index, header in enumerate(headers):
                    value = values[index] if index < len(values) else None
                    record[header] = "" if value is None else str(value)
                    if header.lower().endswith("utility_name") and value is not None:
                        record["utility_name"] = str(value).strip()
                if utility_id == TARGET_UTILITY_ID and record["utility_name"] and "PPL Electric" not in record["utility_name"]:
                    raise ValueError(f"EIA ID {utility_id} mapped to unexpected name {record['utility_name']!r} in {year}/{sheet.title}")
                rows.append(record)
                schemas.append({"year": year, "workbook": workbook_name, "sheet": sheet.title,
                                "header_row": header_row, "field_count": len(headers),
                                "fields": headers})
    finally:
        workbook.close()
    return rows, schemas


def download_archive(year: int, cache_dir: Path) -> tuple[bytes, dict]:
    cache_dir.mkdir(parents=True, exist_ok=True)
    archive_path = cache_dir / f"f861{year}.zip"
    url = archive_url(year)
    if archive_path.exists():
        raw = archive_path.read_bytes()
        retrieved = None
    else:
        request = urllib.request.Request(url, headers={"User-Agent": "energy-systems-doctoral-program/1.0"})
        with urllib.request.urlopen(request, timeout=120) as response:
            raw = response.read()
        archive_path.write_bytes(raw)
        retrieved = datetime.now(timezone.utc).isoformat()
    return raw, {"year": year, "url": url, "sha256": hashlib.sha256(raw).hexdigest(),
                 "bytes": len(raw), "retrieved_utc": retrieved}


def extract_year(year: int, cache_dir: Path) -> tuple[list[dict], list[dict], dict]:
    raw, manifest = download_archive(year, cache_dir)
    rows, schemas = [], []
    with zipfile.ZipFile(BytesIO(raw)) as archive:
        bad = archive.testzip()
        if bad:
            raise RuntimeError(f"EIA-861 {year} ZIP CRC failed at {bad}")
        members = [name for name in archive.namelist()
                   if Path(name).name.lower().startswith("net_metering")
                   and name.lower().endswith((".xlsx", ".xlsm"))]
        if not members:
            raise FileNotFoundError(f"No Net_Metering workbook found in EIA-861 {year} archive")
        for member in members:
            extracted, schema = extract_net_metering_workbook(
                archive.read(member), year, Path(member).name, manifest["sha256"]
            )
            rows.extend(extracted)
            schemas.extend(schema)
    manifest["net_metering_workbooks"] = len(members)
    manifest["ppl_rows"] = len(rows)
    manifest["sheets_with_ppl_rows"] = len({(row["source_workbook"], row["source_sheet"]) for row in rows})
    return rows, schemas, manifest


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--start-year", type=int, default=2015)
    parser.add_argument("--end-year", type=int, default=2025)
    parser.add_argument("--cache-dir", type=Path, default=Path("data/historical-archives"))
    parser.add_argument("--output-dir", type=Path, default=Path("outputs/historical-net-metering"))
    args = parser.parse_args()
    if args.start_year > args.end_year:
        parser.error("start year must be <= end year")
    all_rows, all_schemas, manifests = [], [], []
    for year in range(args.start_year, args.end_year + 1):
        rows, schemas, manifest = extract_year(year, args.cache_dir)
        all_rows.extend(rows)
        all_schemas.extend(schemas)
        manifests.append(manifest)
        print(f"{year}: {len(rows)} PPL utility-level net-metering rows across {manifest['sheets_with_ppl_rows']} worksheets")
    args.output_dir.mkdir(parents=True, exist_ok=True)
    base_fields = ["year", "eia_utility_id", "utility_name", "source_workbook", "source_sheet", "source_row", "archive_sha256"]
    all_fields = list(base_fields)
    for row in all_rows:
        for field in row:
            if field not in all_fields:
                all_fields.append(field)
    with (args.output_dir / "ppl_net_metering_raw.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=all_fields)
        writer.writeheader()
        writer.writerows(all_rows)
    (args.output_dir / "schema_by_year.json").write_text(json.dumps(all_schemas, indent=2) + "\n", encoding="utf-8")
    summary = {"utility_id": TARGET_UTILITY_ID, "start_year": args.start_year,
               "end_year": args.end_year, "archive_manifests": manifests,
               "raw_row_count": len(all_rows), "years_with_ppl_rows": sorted({row['year'] for row in all_rows}),
               "warning": "Raw schedule values are not yet harmonized. Do not compare fields across years until definitions, units, and schedule structure are reconciled."}
    (args.output_dir / "manifest.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(f"Raw historical extract: {args.output_dir.resolve()}")


if __name__ == "__main__":
    main()
