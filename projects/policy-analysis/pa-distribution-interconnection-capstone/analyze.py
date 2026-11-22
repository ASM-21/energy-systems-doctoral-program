"""Reproducible descriptive analysis of Pennsylvania EDC DER interconnection counts.

Reads the 2023-2025 PA PUC peer panel maintained in the casebook. Computes
EDC request shares, PPL rank, request-count concentration, year-over-year
changes, and the 2025 >=500 kW review-level composition. It does not estimate
approval rates, project-level processing times, or causal effects.
"""
from __future__ import annotations

import argparse
import csv
import json
import hashlib
from pathlib import Path
from typing import Iterable

REPO_ROOT = Path(__file__).resolve().parents[3]
DEFAULT_INPUT = (
    REPO_ROOT / "research" / "casebooks" / "pa-der-interconnection"
    / "pa_edc_interconnection_2023_2025.csv"
)


def load_panel(path: Path) -> list[dict]:
    with path.open(newline="", encoding="utf-8-sig") as handle:
        rows = list(csv.DictReader(handle))
    if not rows:
        raise ValueError("Input panel is empty")
    return rows


def _integer(row: dict, key: str) -> int:
    value = row.get(key, "")
    return int(value) if value not in (None, "") else 0


def validate_panel(rows: Iterable[dict]) -> list[dict]:
    records = list(rows)
    required = {
        "reporting_year", "edc", "level1_requests", "level2_requests",
        "level3_requests", "level4_requests", "total_requests",
        "reported_statewide_total",
    }
    if not records:
        raise ValueError("Input panel is empty")
    missing = required.difference(records[0])
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    keys = set()
    years = sorted({int(row["reporting_year"]) for row in records})
    if years != [2023, 2024, 2025]:
        raise ValueError(f"Expected reporting years 2023-2025; received {years}")

    edcs_by_year = {}
    for row in records:
        year = int(row["reporting_year"])
        edc = row["edc"].strip()
        if not edc:
            raise ValueError("EDC name cannot be blank")
        key = (year, edc)
        if key in keys:
            raise ValueError(f"Duplicate EDC-year row: {key}")
        keys.add(key)
        edcs_by_year.setdefault(year, set()).add(edc)

        components = sum(_integer(row, field) for field in (
            "level1_requests", "level2_requests", "level3_requests", "level4_requests"
        ))
        total = _integer(row, "total_requests")
        if components != total:
            raise ValueError(f"Review-level counts do not reconcile for {key}")
        if total < 0 or any(_integer(row, field) < 0 for field in (
            "level1_requests", "level2_requests", "level3_requests", "level4_requests"
        )):
            raise ValueError(f"Negative request count for {key}")

    expected_edcs = edcs_by_year[2023]
    for year, edcs in edcs_by_year.items():
        if edcs != expected_edcs:
            raise ValueError(f"EDC coverage changes in {year}; panel is not balanced")
        official_totals = {_integer(row, "reported_statewide_total")
                           for row in records if int(row["reporting_year"]) == year}
        if len(official_totals) != 1:
            raise ValueError(f"Inconsistent official statewide total in {year}")
        observed_total = sum(
            _integer(row, "total_requests") for row in records
            if int(row["reporting_year"]) == year
        )
        if observed_total != official_totals.pop():
            raise ValueError(f"EDC totals do not reconcile to statewide total in {year}")
    return sorted(records, key=lambda row: (int(row["reporting_year"]), row["edc"]))


def analyze(rows: Iterable[dict]) -> dict:
    records = validate_panel(rows)
    years = sorted({int(row["reporting_year"]) for row in records})
    annual = []
    panel = []
    prior_by_edc = {}

    for year in years:
        cohort = [row for row in records if int(row["reporting_year"]) == year]
        total = sum(_integer(row, "total_requests") for row in cohort)
        ranked = sorted(cohort, key=lambda row: _integer(row, "total_requests"), reverse=True)
        ppl = next(row for row in cohort if row["edc"] == "PPL")
        shares = [_integer(row, "total_requests") / total for row in cohort]
        hhi = 10000.0 * sum(share ** 2 for share in shares)
        top_three_share = 100.0 * sum(
            _integer(row, "total_requests") for row in ranked[:3]
        ) / total

        annual.append({
            "reporting_year": year,
            "edc_count": len(cohort),
            "statewide_requests": total,
            "ppl_requests": _integer(ppl, "total_requests"),
            "ppl_rank": next(i for i, row in enumerate(ranked, 1) if row["edc"] == "PPL"),
            "ppl_request_share_pct": round(_integer(ppl, "total_requests") / total * 100, 2),
            "request_count_hhi": round(hhi, 2),
            "top_three_edc_request_share_pct": round(top_three_share, 2),
        })

        for row in cohort:
            edc = row["edc"]
            count = _integer(row, "total_requests")
            previous = prior_by_edc.get(edc)
            change_pct = (
                round((count / previous - 1) * 100, 2)
                if previous not in (None, 0) else None
            )
            panel.append({
                "reporting_year": year,
                "edc": edc,
                "total_requests": count,
                "level1_requests": _integer(row, "level1_requests"),
                "level2_requests": _integer(row, "level2_requests"),
                "level3_requests": _integer(row, "level3_requests"),
                "level4_requests": _integer(row, "level4_requests"),
                "share_of_statewide_requests_pct": round(count / total * 100, 2),
                "change_from_prior_reporting_year_pct": change_pct,
            })
            prior_by_edc[edc] = count

    latest = [row for row in records if int(row["reporting_year"]) == 2025]
    ppl_latest = next(row for row in latest if row["edc"] == "PPL")
    statewide_l2_ge500 = sum(_integer(row, "level2_ge500kw_requests") for row in latest)
    statewide_l3_ge500 = sum(_integer(row, "level3_ge500kw_requests") for row in latest)
    ppl_l2_ge500 = _integer(ppl_latest, "level2_ge500kw_requests")
    ppl_l3_ge500 = _integer(ppl_latest, "level3_ge500kw_requests")

    return {
        "title": "Pennsylvania EDC DER interconnection request-count analysis",
        "source": "Pennsylvania PUC Net-Metering and Interconnection Report 2023-2025",
        "unit_of_analysis": "EDC service territory by PUC reporting year",
        "reporting_year_definition": "June 1 through May 31",
        "annual_summary": annual,
        "edc_year_panel": panel,
        "ppl_2025_large_request_composition": {
            "level2_ge500kw_requests": ppl_l2_ge500,
            "statewide_level2_ge500kw_requests": statewide_l2_ge500,
            "ppl_level2_share_pct": round(ppl_l2_ge500 / statewide_l2_ge500 * 100, 2),
            "level3_ge500kw_requests": ppl_l3_ge500,
            "statewide_level3_ge500kw_requests": statewide_l3_ge500,
            "ppl_level3_share_pct": round(ppl_l3_ge500 / statewide_l3_ge500 * 100, 2),
        },
        "interpretation_limits": [
            "The HHI is concentration of reported request counts across EDC territories, not a market-power measure.",
            "EDC request counts are not normalized by customer count, load, land area, or installed DER base.",
            "The 2025 500 kW split is not available on a comparable basis for 2023-2024.",
            "The panel contains 33 aggregate EDC-year observations, not application-level cohorts.",
            "Do not calculate approval rates or mean processing times from these aggregate request counts.",
            "No causal effect of tariffs, DERMS, utility investment, or regulatory changes is identified.",
        ],
    }


def build_provenance(input_path: Path) -> dict:
    digest = hashlib.sha256(input_path.read_bytes()).hexdigest()
    try:
        relative_path = str(input_path.resolve().relative_to(REPO_ROOT))
    except ValueError:
        relative_path = str(input_path.resolve())
    return {
        "source_title": "Pennsylvania PUC Net-Metering and Interconnection Report 2023-2025",
        "source_url": "https://www.puc.pa.gov/media/3770/net-metering-interconnection-report-2023-2025_final.pdf",
        "source_access_date": "2026-11-21",
        "source_dataset_path": relative_path,
        "source_dataset_sha256": digest,
        "source_dataset_bytes": input_path.stat().st_size,
        "reporting_period": "June 1 through May 31; reporting years 2023-2025",
        "unit_of_analysis": "EDC service territory by PUC reporting year",
        "transformations": [
            "Structured transcription of PUC EDC-level request-count tables into one row per EDC and reporting year.",
            "Blank size-band cells in 2023-2024 are retained as unavailable and are treated as zero only in arithmetic that explicitly sums reported count fields.",
            "Review-level counts are reconciled to each EDC total and statewide totals are reconciled to the PUC report.",
            "Shares, ranks, HHI, top-three share, and year-over-year changes are derived by this script.",
        ],
        "exclusions_and_caveats": [
            "No application-level records or linked status cohorts are present.",
            "No approval rate, completion rate, or causal effect is estimated.",
            "The 500 kW subcategory split is only reported comparably in the 2025 table.",
        ],
    }


def write_outputs(result: dict, output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "summary.json").write_text(
        json.dumps(result, indent=2) + "\n", encoding="utf-8"
    )
    panel = result["edc_year_panel"]
    with (output_dir / "edc_year_panel.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(panel[0]))
        writer.writeheader()
        writer.writerows(panel)
    annual = result["annual_summary"]
    with (output_dir / "annual_summary.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(annual[0]))
        writer.writeheader()
        writer.writerows(annual)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input-csv", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output-dir", type=Path, default=Path("outputs"))
    args = parser.parse_args()
    result = analyze(load_panel(args.input_csv))
    result["data_provenance"] = build_provenance(args.input_csv)
    write_outputs(result, args.output_dir)
    print(f"Wrote {len(result['edc_year_panel'])} EDC-year rows to {args.output_dir}")


if __name__ == "__main__":
    main()
