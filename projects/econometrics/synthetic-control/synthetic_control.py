"""Synthetic-control teaching lab with pre-period-only weight fitting."""
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

import numpy as np
from scipy.optimize import minimize


def synthetic_panel(seed: int = 20261123, n_donors: int = 8,
                    n_pre: int = 20, n_post: int = 10):
    """Create donors and a treated unit from a known convex donor mixture."""
    if n_donors < 3 or n_pre < 5 or n_post < 1:
        raise ValueError("Need >=3 donors, >=5 pre-periods, and >=1 post-period")
    rng = np.random.default_rng(seed)
    t = np.arange(n_pre + n_post, dtype=float)
    donors = []
    for j in range(n_donors):
        level = 40.0 + 2.7 * j
        trend = 0.18 + 0.025 * j
        cyc = (1.5 + 0.1 * j) * np.sin(2 * np.pi * t / 8 + 0.2 * j)
        common = 0.35 * np.cos(2 * np.pi * t / 13)
        donors.append(level + trend * t + cyc + common
                      + rng.normal(0, 0.12, size=t.size))
    donor_matrix = np.asarray(donors)
    true_weights = np.zeros(n_donors)
    true_weights[:3] = [0.45, 0.35, 0.20]
    treated = true_weights @ donor_matrix
    treated = treated + rng.normal(0, 0.025, size=t.size)
    treated[n_pre:] += 3.0
    return t, treated, donor_matrix, true_weights, n_pre


def fit_weights(y_treated_pre, donor_pre):
    """Solve simplex-constrained least squares using pre-period data only."""
    y = np.asarray(y_treated_pre, dtype=float)
    x = np.asarray(donor_pre, dtype=float)
    if x.ndim != 2 or y.ndim != 1 or x.shape[1] != y.size:
        raise ValueError("donor_pre must be donors x periods and match treated series")
    if x.shape[0] < 1 or not np.all(np.isfinite(x)) or not np.all(np.isfinite(y)):
        raise ValueError("Inputs must be finite and include at least one donor")
    j = x.shape[0]
    objective = lambda w: float(np.sum((y - w @ x) ** 2))
    result = minimize(objective, np.full(j, 1 / j), method="SLSQP",
                      bounds=[(0.0, 1.0)] * j,
                      constraints=[{"type": "eq", "fun": lambda w: np.sum(w) - 1.0}],
                      options={"ftol": 1e-12, "maxiter": 300})
    if not result.success:
        raise RuntimeError(f"Simplex optimization failed: {result.message}")
    weights = np.clip(result.x, 0.0, 1.0)
    weights /= weights.sum()
    return weights


def rmspe(observed, predicted):
    return float(np.sqrt(np.mean((np.asarray(observed) - np.asarray(predicted)) ** 2)))


def analyze(seed: int = 20261123):
    t, treated, donors, true_weights, n_pre = synthetic_panel(seed=seed)
    weights = fit_weights(treated[:n_pre], donors[:, :n_pre])
    synthetic = weights @ donors
    pre = rmspe(treated[:n_pre], synthetic[:n_pre])
    post = rmspe(treated[n_pre:], synthetic[n_pre:])
    ratio = post / pre if pre > 0 else float("inf")
    gaps = treated - synthetic

    placebo = []
    for unit in range(donors.shape[0]):
        other = np.delete(donors, unit, axis=0)
        w = fit_weights(donors[unit, :n_pre], other[:, :n_pre])
        placebo_pre = rmspe(donors[unit, :n_pre], w @ other[:, :n_pre])
        placebo_post = rmspe(donors[unit, n_pre:], w @ other[:, n_pre:])
        placebo_ratio = placebo_post / placebo_pre if placebo_pre > 0 else float("inf")
        placebo.append({"unit": f"donor_{unit+1}", "pre_rmspe": placebo_pre,
                        "post_rmspe": placebo_post, "ratio": placebo_ratio,
                        "pre_fit_eligible": placebo_pre <= max(2.0 * pre, 0.25)})
    eligible = [p for p in placebo if p["pre_fit_eligible"]]
    rank = (1 + sum(p["ratio"] >= ratio for p in eligible)) / (1 + len(eligible))
    return {
        "synthetic_data": True, "seed": seed, "n_pre": n_pre,
        "n_post": int(t.size - n_pre), "weights": weights.tolist(),
        "known_weights": true_weights.tolist(), "pre_rmspe": pre,
        "post_rmspe": post, "post_pre_rmspe_ratio": ratio,
        "average_post_gap": float(np.mean(gaps[n_pre:])),
        "placebos": placebo, "eligible_placebos": len(eligible),
        "descriptive_placebo_rank": rank,
        "warning": "Placebo rank is descriptive, not a design-based p-value."
    }, t, treated, synthetic, gaps


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", default="outputs")
    parser.add_argument("--seed", type=int, default=20261123)
    args = parser.parse_args()
    result, t, treated, synthetic, gaps = analyze(args.seed)
    out = Path(args.output_dir)
    out.mkdir(parents=True, exist_ok=True)
    (out / "summary.json").write_text(json.dumps(result, indent=2) + "\n")
    with (out / "series.csv").open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["period", "treated", "synthetic_control", "gap"])
        writer.writerows(zip(t.astype(int), treated, synthetic, gaps))
    with (out / "weights.csv").open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["donor", "weight"])
        writer.writerows((f"donor_{i+1}", w) for i, w in enumerate(result["weights"]))
    print(json.dumps({k: result[k] for k in (
        "pre_rmspe", "post_rmspe", "post_pre_rmspe_ratio",
        "average_post_gap", "eligible_placebos", "descriptive_placebo_rank")}, indent=2))


if __name__ == "__main__":
    main()
