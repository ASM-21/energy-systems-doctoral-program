"""Transparent DID estimators for balanced teaching panels.

The group-time estimator uses never-treated units as controls. It deliberately
does not implement conventional two-way fixed-effects regression.
"""
from __future__ import annotations


def two_by_two_did(treated_pre, treated_post, control_pre, control_post):
    values = (treated_pre, treated_post, control_pre, control_post)
    if any(not isinstance(value, (int, float)) for value in values):
        raise ValueError("cell means must be numeric")
    return (treated_post - treated_pre) - (control_post - control_pre)


def validate_panel(records):
    if not records:
        raise ValueError("panel must contain observations")
    required = {"unit", "period", "outcome", "cohort"}
    if not required.issubset(records[0]):
        raise ValueError(f"records must contain {sorted(required)}")
    keys = set()
    periods_by_unit = {}
    cohort_by_unit = {}
    for row in records:
        key = (row["unit"], row["period"])
        if key in keys:
            raise ValueError(f"duplicate unit-period row: {key}")
        keys.add(key)
        if not isinstance(row["outcome"], (int, float)):
            raise ValueError("outcomes must be numeric")
        periods_by_unit.setdefault(row["unit"], set()).add(row["period"])
        cohort = row["cohort"]
        if row["unit"] in cohort_by_unit and cohort_by_unit[row["unit"]] != cohort:
            raise ValueError("cohort must be constant within unit")
        cohort_by_unit[row["unit"]] = cohort

    all_periods = sorted({row["period"] for row in records})
    expected = set(all_periods)
    for unit, periods in periods_by_unit.items():
        if periods != expected:
            raise ValueError(f"unbalanced panel for unit {unit}")
    return all_periods


def group_time_att(records):
    """Estimate ATT(g,t) using never-treated controls and cohort-specific baseline.

    cohort is the first treated period; None denotes never treated. Each treated
    cohort uses period g-1 as its baseline and never-treated units as controls.
    """
    periods = validate_panel(records)
    never_units = {row["unit"] for row in records if row["cohort"] is None}
    if not never_units:
        raise ValueError("at least one never-treated control unit is required")

    cohorts = sorted({row["cohort"] for row in records if row["cohort"] is not None})
    output = []
    by_unit_period = {(row["unit"], row["period"]): row for row in records}
    for cohort in cohorts:
        baseline = cohort - 1
        if baseline not in periods:
            raise ValueError(f"no observed pre-treatment baseline for cohort {cohort}")
        treated_units = {row["unit"] for row in records if row["cohort"] == cohort}
        for period in periods:
            if period < cohort:
                continue
            treated_change = sum(
                by_unit_period[(unit, period)]["outcome"]
                - by_unit_period[(unit, baseline)]["outcome"]
                for unit in treated_units
            ) / len(treated_units)
            control_change = sum(
                by_unit_period[(unit, period)]["outcome"]
                - by_unit_period[(unit, baseline)]["outcome"]
                for unit in never_units
            ) / len(never_units)
            output.append({
                "cohort": cohort,
                "period": period,
                "baseline_period": baseline,
                "n_treated": len(treated_units),
                "n_control": len(never_units),
                "att": treated_change - control_change,
            })
    return output


def make_synthetic_panel(n_per_cohort=20):
    """Balanced panel with heterogeneous treatment effects and common time shocks."""
    if not isinstance(n_per_cohort, int) or n_per_cohort <= 0:
        raise ValueError("n_per_cohort must be a positive integer")
    records = []
    groups = ((2, 0), (3, 1), (None, 2))
    for cohort, group_id in groups:
        for index in range(n_per_cohort):
            unit = f"g{group_id}-u{index}"
            unit_effect = 0.01 * index + 0.1 * group_id
            for period in (1, 2, 3, 4):
                common_time = 1.5 * (period - 1)
                treatment_effect = 0.0
                if cohort is not None and period >= cohort:
                    event_time = period - cohort
                    treatment_effect = (2.0 if cohort == 2 else 1.0) + event_time
                records.append({
                    "unit": unit,
                    "period": period,
                    "outcome": unit_effect + common_time + treatment_effect,
                    "cohort": cohort,
                })
    return records


if __name__ == "__main__":
    panel = make_synthetic_panel()
    for result in group_time_att(panel):
        print(result)
