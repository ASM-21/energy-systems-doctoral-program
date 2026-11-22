"""Small, transparent survival-analysis estimators for competing interconnection outcomes.

Events: approval, withdrawal, denial. Censoring is represented by event='censored'.
Times are discrete or continuous durations measured from a common, defined origin.
At tied times, events are processed before censoring removals.
"""
from __future__ import annotations

from collections import defaultdict
from math import exp, isfinite
import random

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
        if not isinstance(time, (int, float)) or not isfinite(time) or time <= 0:
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



def simulate_exponential_competing_risks(n, rates, censor_time, seed=21):
    """Generate a synthetic cohort with independent exponential cause hazards.

    rates maps each cause in CAUSES to a nonnegative constant hazard per time
    unit. Administrative censoring occurs at censor_time. This generator is
    for estimator validation and teaching, not an empirical data model.
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    if not isinstance(censor_time, (int, float)) or not isfinite(censor_time) or censor_time <= 0:
        raise ValueError("censor_time must be finite and positive")
    if set(rates) != set(CAUSES):
        raise ValueError(f"rates must contain exactly {CAUSES}")
    if any(not isinstance(value, (int, float)) or not isfinite(value) or value < 0
           for value in rates.values()):
        raise ValueError("cause-specific rates must be finite and nonnegative")
    total_rate = sum(rates.values())
    if total_rate <= 0:
        raise ValueError("at least one cause-specific rate must be positive")

    rng = random.Random(seed)
    cumulative = []
    running = 0.0
    for cause in CAUSES:
        running += rates[cause] / total_rate
        cumulative.append((running, cause))

    records = []
    for _ in range(n):
        event_time = rng.expovariate(total_rate)
        if event_time > censor_time:
            records.append({"time": float(censor_time), "event": "censored"})
            continue
        draw = rng.random()
        event = next((cause for cutoff, cause in cumulative if draw <= cutoff), CAUSES[-1])
        records.append({"time": event_time, "event": event})
    return records


def curve_value_at(curve, time, field):
    """Return the last right-continuous step-curve value at or before time."""
    if not isinstance(time, (int, float)) or not isfinite(time) or time < 0:
        raise ValueError("evaluation time must be finite and nonnegative")
    eligible = [row for row in curve if row["time"] <= time]
    return float(eligible[-1][field]) if eligible else 0.0


def exponential_competing_risk_cif(cause_rate, rates, horizon):
    """Analytic cause-specific CIF for constant independent exponential hazards."""
    if set(rates) != set(CAUSES):
        raise ValueError(f"rates must contain exactly {CAUSES}")
    if any(not isinstance(value, (int, float)) or not isfinite(value) or value < 0
           for value in rates.values()):
        raise ValueError("cause-specific rates must be finite and nonnegative")
    total_rate = sum(rates.values())
    if total_rate <= 0 or cause_rate not in rates:
        raise ValueError("positive total hazard and a named cause are required")
    if not isinstance(horizon, (int, float)) or not isfinite(horizon) or horizon < 0:
        raise ValueError("horizon must be finite and nonnegative")
    return rates[cause_rate] / total_rate * (1.0 - exp(-total_rate * horizon))


def check_probability_mass(curve, tolerance=1e-10):
    """Raise if cumulative incidence plus event-free probability exceeds one."""
    for row in curve:
        total = (row["cif_approval"] + row["cif_withdrawal"]
                 + row["cif_denial"] + row["event_free_probability"])
        if total > 1.0 + tolerance or total < -tolerance:
            raise AssertionError(f"Probability mass is not conserved at t={row['time']}")
    return True
