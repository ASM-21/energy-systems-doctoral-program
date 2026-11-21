"""Audit Pennsylvania EDC interconnection request counts and PPL peer position.

The source is the PA PUC 2023–2025 Net-Metering and Interconnection Report.
Only request counts are ranked; mean review-time cells are retained in the
source CSV but are not ranked because zero cells and denominators need review.
"""
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


def read_rows(path: Path) -> list[dict]:
    with path.open(newline="", encoding="utf-8-sig") as handle:
        rows = list(csv.DictReader(handle))
    if not rows:
        raise ValueError("No EDC rows found")
    return sorted(rows, key=lambda row: (int(row["reporting_year"]), row["edc"]))


def analyze(rows: list[dict]) -> dict:
    annual = []
    for year in sorted({int(row["reporting_year"]) for row in rows}):
        cohort = [row for row in rows if int(row["reporting_year"]) == year]
        for row in cohort:
            components = sum(int(row[key] or 0) for key in (
                "level1_requests", "level2_requests", "level3_requests", "level4_requests"
            ))
            if components != int(row["total_requests"]):
                raise ValueError(f"Review-level requests do not reconcile for {year} {row['edc']}")
        computed_total = sum(int(row["total_requests"]) for row in cohort)
        official_totals = {int(row["reported_statewide_total"]) for row in cohort}
        if len(official_totals) != 1:
            raise ValueError(f"Inconsistent official statewide total field in {year}")
        official_total = official_totals.pop()
        ppl = next((row for row in cohort if row["edc"] == "PPL"), None)
        if ppl is None:
            raise ValueError(f"PPL row missing for {year}")
        ranked = sorted(cohort, key=lambda row: int(row["total_requests"]), reverse=True)
        rank = next(i for i, row in enumerate(ranked, start=1) if row["edc"] == "PPL")
        annual.append({
            "year": year,
            "edc_count": len(cohort),
            "computed_statewide_requests": computed_total,
            "official_statewide_requests": official_total,
            "statewide_total_reconciles": computed_total == official_total,
            "ppl_requests": int(ppl["total_requests"]),
            "ppl_rank_by_total_requests": rank,
            "ppl_share_of_statewide_requests_pct": round(
                int(ppl["total_requests"]) / computed_total * 100, 2
            ),
        })
    latest_year = max(int(row["reporting_year"]) for row in rows)
    latest = [row for row in rows if int(row["reporting_year"]) == latest_year]
    ppl_latest = next(row for row in latest if row["edc"] == "PPL")
    level3_large_state = sum(int(row["level3_ge500kw_requests"] or 0) for row in latest)
    level2_large_state = sum(int(row["level2_ge500kw_requests"] or 0) for row in latest)
    return {
        "source": "PA PUC Net-Metering and Interconnection Report 2023–2025",
        "unit": "EDC service territory × reporting year",
        "reporting_period": "June 1 through May 31",
        "annual_peer_comparison": annual,
        "latest_year_large_request_composition": {
            "year": latest_year,
            "ppl_level2_ge500kw_requests": int(ppl_latest["level2_ge500kw_requests"] or 0),
            "statewide_level2_ge500kw_requests": level2_large_state,
            "ppl_share_of_level2_ge500kw_pct": round(
                int(ppl_latest["level2_ge500kw_requests"] or 0) / level2_large_state * 100, 2
            ) if level2_large_state else None,
            "ppl_level3_ge500kw_requests": int(ppl_latest["level3_ge500kw_requests"] or 0),
            "statewide_level3_ge500kw_requests": level3_large_state,
            "ppl_share_of_level3_ge500kw_pct": round(
                int(ppl_latest["level3_ge500kw_requests"] or 0) / level3_large_state * 100, 2
            ) if level3_large_state else None,
        },
        "limitations": [
            "EDC service territories are the unit; do not map them one-to-one to EIA utility IDs.",
            "2025 request counts split Levels 2–4 at 500 kW; 2023–2024 counts do not.",
            "Requests may move between review levels; level is not necessarily immutable.",
            "Counts are descriptive and do not identify project-level outcomes or causal effects.",
            "Mean approval-time values are not ranked in this script because zero cells and denominators require additional verification."
        ]
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input-csv", type=Path, default=Path("pa_edc_interconnection_2023_2025.csv"))
    parser.add_argument("--output-json", type=Path, default=Path("pa_edc_peer_summary.json"))
    args = parser.parse_args()
    result = analyze(read_rows(args.input_csv))
    args.output_json.parent.mkdir(parents=True, exist_ok=True)
    args.output_json.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote peer comparison to {args.output_json}")


if __name__ == "__main__":
    main()
