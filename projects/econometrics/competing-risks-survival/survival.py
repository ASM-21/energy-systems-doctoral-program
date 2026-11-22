"""Small, transparent survival-analysis estimators for competing interconnection outcomes.

Events: approval, withdrawal, denial. Censoring is represented by event='censored'.
Times are discrete or continuous durations measured from a common, defined origin.
At tied times, events are processed before censoring removals.
"""
from __future__ import annotations

from collections import defaultdict

CAUSES = ("approval", "withdrawal", "denial")
ALLOWED = set(CAUSES) | {"censored"}


def validate_records(records):
    cleaned = []
    if not records:
        raise ValueError("At least one record is required")
    for index, row in enumerate(records):
        if "time" not in row or "event" not in row:
            raise ValueError(f"Record {index} requires time and event")
        time = row["time"]
        event = row["event"]
        if not isinstance(time, (int, float)) or time <= 0:
            raise ValueError(f"Record {index} time must be positive")
        if event not in ALLOWED:
            raise ValueError(f"Record {index} has unknown event: {event}")
        cleaned.append({"time": float(time), "event": event})
    return cleaned


def _group(records):
    groups = defaultdict(lambda: {"approval": 0, "withdrawal": 0,
                                   "denial": 0, "censored": 0})
    for row in records:
        groups[row["time"]][row["event"]] += 1
    return groups


def kaplan_meier_net_approval(records):
    """Return 1-KM net approval risk, censoring competing outcomes.

    This is a hypothetical net-risk estimand under independent censoring of
    competing events, not the observed cumulative incidence of approval.
    """
    cleaned = validate_records(records)
    groups = _group(cleaned)
    at_risk = len(cleaned)
    survival = 1.0
    output = []
    for time in sorted(groups):
        counts = groups[time]
        approvals = counts["approval"]
        competing = counts["withdrawal"] + counts["denial"]
        censored = counts["censored"]
        before = at_risk
        survival *= 1.0 - approvals / before
        output.append({
            "time": time,
            "at_risk": before,
            "approvals": approvals,
            "competing_events_censored": competing,
            "right_censored": censored,
            "net_approval_probability": 1.0 - survival,
            "survival_without_approval": survival,
        })
        at_risk -= approvals + competing + censored
    return output


def aalen_johansen(records):
    """Estimate cause-specific cumulative incidence functions.

    The event-free probability is updated using all observed causes. Censoring
    removes observations from later risk sets but does not directly change the
    event-free probability at that instant.
    """
    cleaned = validate_records(records)
    groups = _group(cleaned)
    at_risk = len(cleaned)
    event_free = 1.0
    incidence = {cause: 0.0 for cause in CAUSES}
    output = []
    for time in sorted(groups):
        counts = groups[time]
        before = at_risk
        total_events = sum(counts[cause] for cause in CAUSES)
        if total_events > before:
            raise ValueError("Events exceed the risk set")
        for cause in CAUSES:
            incidence[cause] += event_free * counts[cause] / before
        event_free *= 1.0 - total_events / before
        output.append({
            "time": time,
            "at_risk": before,
            "approvals": counts["approval"],
            "withdrawals": counts["withdrawal"],
            "denials": counts["denial"],
            "right_censored": counts["censored"],
            "cif_approval": incidence["approval"],
            "cif_withdrawal": incidence["withdrawal"],
            "cif_denial": incidence["denial"],
            "event_free_probability": event_free,
        })
        at_risk -= total_events + counts["censored"]
    return output


def check_probability_mass(curve, tolerance=1e-10):
    """Raise if cumulative incidence plus event-free probability exceeds one."""
    for row in curve:
        total = (row["cif_approval"] + row["cif_withdrawal"]
                 + row["cif_denial"] + row["event_free_probability"])
        if total > 1.0 + tolerance or total < -tolerance:
            raise AssertionError(f"Probability mass is not conserved at t={row['time']}")
    return True
