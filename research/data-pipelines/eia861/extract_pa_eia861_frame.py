"""Join Pennsylvania net-metering respondents to annual EIA-861 respondent frames.

The frame provides respondent identity, survey form, ownership, and schedule
participation. It does not itself establish service-territory comparability.
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import zipfile
from collections import defaultdict
from io import BytesIO
from pathlib import Path

from openpyxl import load_workbook
from extract_historical_net_metering import download_archive


def norm(value) -> str:
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").casefold()).strip()


def utility_id(value) -> str:
    if isinstance(value, float) and value.is_integer():
        return str(int(value))
    return str(value).strip()


def parse_frame_workbook(data: bytes, year: int) -> list[dict]:
    workbook = load_workbook(BytesIO(data), read_only=True, data_only=True)
    output = []
    try:
        for sheet in workbook.worksheets:
            header_row = None
            headers = None
            for row_number, values in enumerate(sheet.iter_rows(values_only=True), start=1):
                normalized = [norm(v) for v in values]
                if "utility number" in normalized and "utility name" in normalized:
                    header_row, headers = row_number, normalized
                    break
                if row_number >= 15:
                    break
            if header_row is None:
                continue
            positions = {name: i for i, name in enumerate(headers) if name}
            required = ["utility number", "utility name"]
            if not all(name in positions for name in required):
                continue
            def cell(values, name):
                index = positions.get(name)
                return values[index] if index is not None and index < len(values) else None
            for values in sheet.iter_rows(min_row=header_row + 1, values_only=True):
                raw_id = cell(values, "utility number")
                if raw_id in (None, ""):
                    continue
                output.append({
                    "year": year,
                    "eia_utility_id": utility_id(raw_id),
                    "frame_utility_name": str(cell(values, "utility name") or "").strip(),
                    "short_form": str(cell(values, "short form") or "").strip(),
                    "ownership": str(cell(values, "ownership") or "").strip(),
                    "ownership_code": str(cell(values, "ownership code") or "").strip(),
                    "net_metering_reported": str(cell(values, "net metering") or "").strip(),
                    "frame_sheet": sheet.title,
                })
            break
    finally:
        workbook.close()
    return output


def audit_frame_year(year: int, panel_ids: set[str], frame_rows: list[dict]) -> list[dict]:
    by_id = defaultdict(list)
    for row in frame_rows:
        by_id[row["eia_utility_id"]].append(row)
    output = []
    for uid in sorted(panel_ids):
        matches = by_id.get(uid, [])
        if len(matches) == 1:
            item = dict(matches[0])
            item["frame_match_status"] = "matched"
        elif len(matches) > 1:
            item = {
                "year": year, "eia_utility_id": uid,
                "frame_match_status": "duplicate_frame_id",
                "frame_row_count": len(matches),
            }
        else:
            item = {
                "year": year, "eia_utility_id": uid,
                "frame_match_status": "not_found_in_frame",
            }
        output.append(item)
    return output


def read_panel_ids(path: Path) -> dict[int, set[str]]:
    result = defaultdict(set)
    with path.open(newline="", encoding="utf-8-sig") as handle:
        for row in csv.DictReader(handle):
            result[int(row["year"])].add(str(row["eia_utility_id"]).strip())
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--panel-csv", type=Path, required=True)
    parser.add_argument("--start-year", type=int, default=2016)
    parser.add_argument("--end-year", type=int, default=2025)
    parser.add_argument("--cache-dir", type=Path, default=Path("data/historical-archives"))
    parser.add_argument("--output-dir", type=Path, default=Path("outputs/pa-utility-net-metering/frame-audit"))
    args = parser.parse_args()
    if args.start_year > args.end_year:
        parser.error("start year must be <= end year")
    panel_ids = read_panel_ids(args.panel_csv)
    records, manifests = [], []
    for year in range(args.start_year, args.end_year + 1):
        raw, archive_manifest = download_archive(year, args.cache_dir)
        with zipfile.ZipFile(BytesIO(raw)) as archive:
            bad = archive.testzip()
            if bad:
                raise RuntimeError(f"EIA-861 {year} ZIP CRC failed at {bad}")
            members = [name for name in archive.namelist()
                       if Path(name).name.casefold().startswith("frame")
                       and name.casefold().endswith((".xlsx", ".xlsm"))]
            if not members:
                manifests.append({"year": year, "frame_workbook_found": False,
                                  "panel_ids": len(panel_ids.get(year, set()))})
                records.extend({
                    "year": year, "eia_utility_id": uid,
                    "frame_match_status": "frame_workbook_not_found"
                } for uid in sorted(panel_ids.get(year, set())))
                continue
            frame_rows = []
            for member in members:
                frame_rows.extend(parse_frame_workbook(archive.read(member), year))
            year_records = audit_frame_year(year, panel_ids.get(year, set()), frame_rows)
            records.extend(year_records)
            manifests.append({
                "year": year, "frame_workbook_found": True,
                "frame_workbooks": [Path(m).name for m in members],
                "frame_row_count": len(frame_rows),
                "pa_net_metering_ids": len(panel_ids.get(year, set())),
                "matched_ids": sum(r["frame_match_status"] == "matched" for r in year_records),
                "not_found_ids": sum(r["frame_match_status"] == "not_found_in_frame" for r in year_records),
                "duplicate_frame_ids": sum(r["frame_match_status"] == "duplicate_frame_id" for r in year_records),
                "archive_sha256": archive_manifest["sha256"],
            })
    args.output_dir.mkdir(parents=True, exist_ok=True)
    fields = sorted({key for row in records for key in row})
    with (args.output_dir / "pa_utility_frame_audit.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(records)
    summary = {
        "start_year": args.start_year, "end_year": args.end_year,
        "measurement_status": "respondent-frame linkage only; no outcome harmonization",
        "annual_manifests": manifests,
        "warning": "Frame presence, short-form status, and schedule participation do not establish stable service territory or comparable net-metering measures. Confirm frame definitions and annual survey instructions before panel analysis."
    }
    (args.output_dir / "frame_audit_manifest.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {len(records)} Pennsylvania utility-year frame matches to {args.output_dir}")


if __name__ == "__main__":
    main()
