"""Extract all Pennsylvania utility-level rows from EIA-861 Net Metering schedules."""
from __future__ import annotations
import argparse
import csv
import json
import zipfile
from collections import Counter
from io import BytesIO
from pathlib import Path

from extract_historical_net_metering import download_archive, unique_headers
from extract_ppl_eia861 import find_header_row, build_headers


def first_populated(values, indices):
    for index in indices:
        if index < len(values) and values[index] not in (None, "", "."):
            return values[index]
    return None


def normalize_utility_id(value) -> str:
    if isinstance(value, float) and value.is_integer():
        return str(int(value))
    return str(value).strip()


def extract_state_workbook(data: bytes, year: int, workbook_name: str,
                           archive_sha256: str, state: str = "PA") -> tuple[list[dict], list[dict], list[dict]]:
    from openpyxl import load_workbook
    workbook = load_workbook(BytesIO(data), read_only=False, data_only=True)
    rows, schemas, exclusions = [], [], []
    try:
        for sheet in workbook.worksheets:
            if "tpo" in sheet.title.casefold():
                exclusions.append({
                    "year": year, "workbook": workbook_name, "sheet": sheet.title,
                    "reason": "third-party-owned schedule; not the EDC utility respondent panel",
                })
                continue
            header_row = find_header_row(sheet)
            if header_row is None:
                continue
            headers = unique_headers(build_headers(sheet, header_row))
            utility_cols = [i for i, name in enumerate(headers)
                            if name.lower().endswith("utility_number")]
            name_cols = [i for i, name in enumerate(headers)
                         if name.lower().endswith("utility_name")]
            state_cols = [i for i, name in enumerate(headers)
                          if name.lower().endswith("state")]
            if not utility_cols or not state_cols:
                continue
            sheet_rows = 0
            for row_number, values in enumerate(
                sheet.iter_rows(min_row=header_row + 1, values_only=True),
                start=header_row + 1,
            ):
                raw_id = first_populated(values, utility_cols)
                raw_state = first_populated(values, state_cols)
                if raw_id is None or raw_state is None or str(raw_state).strip().upper() != state.upper():
                    continue
                utility_id = normalize_utility_id(raw_id)
                raw_name = first_populated(values, name_cols)
                utility_name = "" if raw_name is None else str(raw_name).strip()
                if utility_id == "99999" or utility_name.casefold() == "adjustment":
                    exclusions.append({
                        "year": year, "workbook": workbook_name, "sheet": sheet.title,
                        "source_row": row_number, "eia_utility_id": utility_id,
                        "utility_name": utility_name,
                        "reason": "EIA administrative adjustment row; not a utility respondent",
                    })
                    continue
                record = {
                    "year": year,
                    "eia_utility_id": utility_id,
                    "utility_name": utility_name,
                    "state": state.upper(),
                    "source_workbook": workbook_name,
                    "source_sheet": sheet.title,
                    "source_row": row_number,
                    "archive_sha256": archive_sha256,
                }
                for index, header in enumerate(headers):
                    value = values[index] if index < len(values) else None
                    record[header] = "" if value is None else str(value)
                rows.append(record)
                sheet_rows += 1
            if sheet_rows:
                schemas.append({
                    "year": year,
                    "workbook": workbook_name,
                    "sheet": sheet.title,
                    "header_row": header_row,
                    "field_count": len(headers),
                    "row_count": sheet_rows,
                    "fields": headers,
                })
    finally:
        workbook.close()
    return rows, schemas, exclusions


def extract_year(year: int, cache_dir: Path, state: str = "PA"):
    raw, manifest = download_archive(year, cache_dir)
    rows, schemas, exclusions = [], [], []
    with zipfile.ZipFile(BytesIO(raw)) as archive:
        bad = archive.testzip()
        if bad:
            raise RuntimeError(f"EIA-861 {year} ZIP CRC failed at {bad}")
        members = [
            name for name in archive.namelist()
            if Path(name).name.lower().startswith("net_metering")
            and name.lower().endswith((".xlsx", ".xlsm"))
        ]
        if not members:
            raise FileNotFoundError(f"No Net_Metering workbook found in EIA-861 {year} archive")
        for member in members:
            extracted, schema, excluded = extract_state_workbook(
                archive.read(member), year, Path(member).name, manifest["sha256"], state
            )
            rows.extend(extracted)
            schemas.extend(schema)
            exclusions.extend(excluded)
    counts = Counter(row["eia_utility_id"] for row in rows)
    manifest.update({
        "net_metering_workbooks": len(members),
        "state": state.upper(),
        "state_utility_rows": len(rows),
        "unique_utility_ids": len(counts),
        "duplicate_utility_ids": {key: value for key, value in counts.items() if value > 1},
        "sheets_with_state_rows": len({(row["source_workbook"], row["source_sheet"]) for row in rows}),
        "excluded_tpo_sheets": [item for item in exclusions if "source_row" not in item],
        "excluded_adjustment_rows": [item for item in exclusions if "source_row" in item],
        "excluded_tpo_sheet_count": sum(1 for item in exclusions if "source_row" not in item),
        "excluded_adjustment_row_count": sum(1 for item in exclusions if "source_row" in item),
    })
    return rows, schemas, manifest


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--start-year", type=int, default=2015)
    parser.add_argument("--end-year", type=int, default=2025)
    parser.add_argument("--state", default="PA")
    parser.add_argument("--cache-dir", type=Path, default=Path("data/historical-archives"))
    parser.add_argument("--output-dir", type=Path, default=Path("outputs/pa-utility-net-metering"))
    args = parser.parse_args()
    if args.start_year > args.end_year:
        parser.error("start year must be <= end year")
    all_rows, all_schemas, manifests = [], [], []
    for year in range(args.start_year, args.end_year + 1):
        rows, schemas, manifest = extract_year(year, args.cache_dir, args.state)
        all_rows.extend(rows)
        all_schemas.extend(schemas)
        manifests.append(manifest)
        print(f"{year}: {len(rows)} {args.state.upper()} utility-level rows across {manifest['unique_utility_ids']} utility IDs")
    args.output_dir.mkdir(parents=True, exist_ok=True)
    base_fields = ["year", "eia_utility_id", "utility_name", "state", "source_workbook",
                   "source_sheet", "source_row", "archive_sha256"]
    all_fields = list(base_fields)
    for row in all_rows:
        for field in row:
            if field not in all_fields:
                all_fields.append(field)
    with (args.output_dir / "pa_net_metering_utility_rows.csv").open(
        "w", newline="", encoding="utf-8"
    ) as handle:
        writer = csv.DictWriter(handle, fieldnames=all_fields)
        writer.writeheader()
        writer.writerows(all_rows)

    coverage = []
    for row in all_rows:
        coverage.append({
            "year": row["year"],
            "eia_utility_id": row["eia_utility_id"],
            "utility_name": row["utility_name"],
            "state": row["state"],
            "source_sheet": row["source_sheet"],
            "source_row": row["source_row"],
        })
    with (args.output_dir / "pa_utility_year_coverage.csv").open(
        "w", newline="", encoding="utf-8"
    ) as handle:
        writer = csv.DictWriter(handle, fieldnames=list(coverage[0]) if coverage else
                                ["year", "eia_utility_id", "utility_name", "state", "source_sheet", "source_row"])
        writer.writeheader()
        writer.writerows(coverage)

    summary = {
        "state": args.state.upper(),
        "start_year": args.start_year,
        "end_year": args.end_year,
        "archive_manifests": manifests,
        "raw_row_count": len(all_rows),
        "utility_ids": sorted({row["eia_utility_id"] for row in all_rows}),
        "year_utility_counts": {
            str(year): len({row["eia_utility_id"] for row in all_rows if row["year"] == year})
            for year in range(args.start_year, args.end_year + 1)
        },
        "warning": "Raw schedule values are not harmonized. Utility IDs, service territories, field definitions, units, and survey coverage must be reconciled before panel analysis.",
    }
    (args.output_dir / "schema_by_year.json").write_text(
        json.dumps(all_schemas, indent=2) + "\n", encoding="utf-8"
    )
    (args.output_dir / "manifest.json").write_text(
        json.dumps(summary, indent=2) + "\n", encoding="utf-8"
    )
    print(f"Raw state utility panel extract: {args.output_dir.resolve()}")


if __name__ == "__main__":
    main()
