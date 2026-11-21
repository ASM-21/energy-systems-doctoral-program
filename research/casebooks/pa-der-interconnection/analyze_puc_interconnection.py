"""Reproduce descriptive checks for the PA PUC 2023–2025 PPL interconnection extract.

This is a data-validation and descriptive-statistics script. It does not estimate
causal effects or treat reported status fields as validated completion rates.
"""
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


def number(row: dict, key: str) -> int | None:
    value = row.get(key, "")
    if value is None or str(value).strip() == "":
        return None
    return int(float(value))


def load_rows(path: Path) -> list[dict]:
    with path.open(newline="", encoding="utf-8-sig") as handle:
        rows = list(csv.DictReader(handle))
    if not rows:
        raise ValueError("No data rows found")
    return sorted(rows, key=lambda row: int(row["reporting_year"]))


def analyze(rows: list[dict]) -> dict:
    annual = []
    for row in rows:
        year = int(row["reporting_year"])
        requests = {key: number(row, key) for key in (
            "level1_requests", "level2_requests", "level3_requests",
            "level4_requests", "total_requests"
        )}
        request_sum = sum(requests[k] or 0 for k in (
            "level1_requests", "level2_requests", "level3_requests", "level4_requests"
        ))
        status = {key: number(row, key) for key in (
            "submitted", "reported_completed", "approved", "denied",
            "cancelled_by_customer", "pending_customer_action", "pending_edc_action"
        )}
        status_components = sum(status[k] or 0 for k in (
            "approved", "denied", "cancelled_by_customer",
            "pending_customer_action", "pending_edc_action"
        ))
        closed_statuses = sum(status[k] or 0 for k in (
            "approved", "denied", "cancelled_by_customer"
        ))
        annual.append({
            "year": year,
            "request_level_sum": request_sum,
            "reported_total_requests": requests["total_requests"],
            "request_total_reconciles": request_sum == requests["total_requests"],
            "status_component_sum": status_components,
            "submitted": status["submitted"],
            "status_gap_vs_submitted": status["submitted"] - status_components,
            "reported_completed": status["reported_completed"],
            "approved_denied_cancelled_sum": closed_statuses,
            "reported_completed_minus_approved_denied_cancelled":
                status["reported_completed"] - closed_statuses,
            "pending_edc_action": status["pending_edc_action"],
            "reported_completed_includes_pending_edc_arithmetic":
                status["reported_completed"] - closed_statuses == (status["pending_edc_action"] or 0),
            "status_reconciles_to_submitted": status_components == status["submitted"],
        })

    first, last = rows[0], rows[-1]
    def pct_change(field: str) -> float:
        start, end = number(first, field), number(last, field)
        if start in (None, 0) or end is None:
            raise ValueError(f"Cannot calculate change for {field}")
        return (end / start - 1.0) * 100.0

    last_year = int(last["reporting_year"])
    level2_lt = number(last, "level2_lt500kw_requests")
    level2_ge = number(last, "level2_ge500kw_requests")
    level3_lt = number(last, "level3_lt500kw_requests")
    level3_ge = number(last, "level3_ge500kw_requests")
    return {
        "scope": "PPL Electric Utilities; Pennsylvania PUC aggregated net-metering interconnection report",
        "years": [int(row["reporting_year"]) for row in rows],
        "reporting_period": "June 1 through May 31",
        "descriptive_changes_first_to_last_pct": {
            "customer_generators": round(pct_change("customer_generators_total"), 2),
            "interconnected_capacity_kw": round(pct_change("capacity_total_kw"), 2),
            "annual_interconnection_requests": round(pct_change("total_requests"), 2),
        },
        "latest_year": {
            "year": last_year,
            "level2_requests_from_size_bands": (level2_lt or 0) + (level2_ge or 0),
            "level3_requests_from_size_bands": (level3_lt or 0) + (level3_ge or 0),
            "level2_lt500kw_requests": level2_lt,
            "level2_ge500kw_requests": level2_ge,
            "level3_lt500kw_requests": level3_lt,
            "level3_ge500kw_requests": level3_ge,
        },
        "annual_quality_checks": annual,
        "interpretation": [
            "Descriptive changes only; no causal effects are identified.",
            "Request counts and mean approval times may describe different cohorts.",
            "Do not calculate completion rates until the PUC status-field definitions and 2025 arithmetic are clarified.",
            "Zero mean-time cells may represent no completed cases or non-applicability, not zero-day reviews."
        ]
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input-csv", type=Path, default=Path("ppl_interconnection_2023_2025.csv"))
    parser.add_argument("--output-json", type=Path, default=Path("ppl_interconnection_summary.json"))
    args = parser.parse_args()
    result = analyze(load_rows(args.input_csv))
    args.output_json.parent.mkdir(parents=True, exist_ok=True)
    args.output_json.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote descriptive checks to {args.output_json}")


if __name__ == "__main__":
    main()
