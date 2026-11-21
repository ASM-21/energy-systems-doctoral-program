"""Audit coverage and identifier continuity in raw state-level EIA-861 extracts.

This is a measurement audit, not a harmonizer. It deliberately does not create
cross-utility growth rates or infer missing observations as zero.
"""
from __future__ import annotations

import argparse
import csv
import json
from collections import defaultdict
from pathlib import Path


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle))


def audit_panel(rows: list[dict[str, str]], start_year: int, end_year: int,
                state: str = "PA") -> dict:
    expected_years = list(range(start_year, end_year + 1))
    year_ids: dict[int, set[str]] = {year: set() for year in expected_years}
    id_names: dict[str, dict[int, set[str]]] = defaultdict(lambda: defaultdict(set))
    duplicate_counts: dict[tuple[int, str], int] = defaultdict(int)
    row_count_by_year = {year: 0 for year in expected_years}
    fields_by_year: dict[int, set[str]] = defaultdict(set)
    invalid_rows = []

    for index, row in enumerate(rows, start=2):
        try:
            year = int(row["year"])
        except (KeyError, TypeError, ValueError):
            invalid_rows.append({"csv_row": index, "reason": "invalid year"})
            continue
        utility_id = str(row.get("eia_utility_id", "")).strip()
        row_state = str(row.get("state", "")).strip().upper()
        if year not in year_ids:
            invalid_rows.append({"csv_row": index, "reason": "year outside requested range"})
            continue
        if not utility_id or row_state != state.upper():
            invalid_rows.append({"csv_row": index, "reason": "missing utility ID or state mismatch"})
            continue
        year_ids[year].add(utility_id)
        duplicate_counts[(year, utility_id)] += 1
        name = str(row.get("utility_name", "")).strip()
        if name:
            id_names[utility_id][year].add(name)
        row_count_by_year[year] += 1
        fields_by_year[year].update(key for key, value in row.items()
                                    if value not in (None, ""))

    duplicate_keys = [
        {"year": year, "eia_utility_id": utility_id, "row_count": count}
        for (year, utility_id), count in sorted(duplicate_counts.items())
        if count > 1
    ]
    identity_history = []
    for utility_id, yearly_names in sorted(id_names.items()):
        observations = []
        for year, names in sorted(yearly_names.items()):
            observations.append({
                "year": year,
                "names": sorted(names),
                "multiple_names_same_year": len(names) > 1,
            })
        all_names = sorted({name for names in yearly_names.values() for name in names})
        identity_history.append({
            "eia_utility_id": utility_id,
            "years_observed": sorted(yearly_names),
            "names_observed": all_names,
            "name_changes_or_variants": len(all_names) > 1,
            "history": observations,
        })

    return {
        "state": state.upper(),
        "start_year": start_year,
        "end_year": end_year,
        "measurement_status": "coverage and identifier audit only; no variable harmonization performed",
        "raw_row_count": len(rows),
        "valid_row_count": sum(row_count_by_year.values()),
        "invalid_rows": invalid_rows,
        "year_coverage": [
            {
                "year": year,
                "utility_rows": row_count_by_year[year],
                "unique_utility_ids": len(year_ids[year]),
                "utility_ids": sorted(year_ids[year]),
                "nonempty_field_count": len(fields_by_year[year]),
            }
            for year in expected_years
        ],
        "utility_id_universe": sorted(id_names),
        "utility_id_year_count": len(id_names),
        "duplicate_year_utility_rows": duplicate_keys,
        "identity_history": identity_history,
        "interpretation_warning": (
            "A repeated EIA utility ID does not establish a stable service territory, "
            "respondent form, or comparable variable definition. Name variants and "
            "missing years require source-level review. Do not calculate cross-utility "
            "growth or causal effects from this audit output."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input-csv", type=Path, required=True)
    parser.add_argument("--start-year", type=int, required=True)
    parser.add_argument("--end-year", type=int, required=True)
    parser.add_argument("--state", default="PA")
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    if args.start_year > args.end_year:
        parser.error("start year must be <= end year")
    rows = read_rows(args.input_csv)
    report = audit_panel(rows, args.start_year, args.end_year, args.state)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir / "panel_coverage_audit.json").write_text(
        json.dumps(report, indent=2) + "\\n", encoding="utf-8"
    )
    with (args.output_dir / "utility_identity_history.csv").open(
        "w", newline="", encoding="utf-8"
    ) as handle:
        writer = csv.DictWriter(handle, fieldnames=[
            "eia_utility_id", "years_observed", "names_observed",
            "name_changes_or_variants"
        ])
        writer.writeheader()
        for item in report["identity_history"]:
            writer.writerow({
                "eia_utility_id": item["eia_utility_id"],
                "years_observed": ";".join(map(str, item["years_observed"])),
                "names_observed": ";".join(item["names_observed"]),
                "name_changes_or_variants": item["name_changes_or_variants"],
            })
    print(
        f"Audited {report['valid_row_count']} rows, "
        f"{report['utility_id_year_count']} utility IDs, "
        f"{len(report['duplicate_year_utility_rows'])} duplicate year-ID keys"
    )


if __name__ == "__main__":
    main()
