"""Synthetic interrupted-time-series comparison: HAC OLS versus AR(1)-error GLS."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.stats.diagnostic import acorr_ljungbox


def generate_series(seed=20261123, n=120, intervention=72):
    if n < 30 or not 10 <= intervention <= n - 10:
        raise ValueError("Require n >= 30 and intervention at least 10 periods from edges")
    rng = np.random.default_rng(seed)
    t = np.arange(n, dtype=float)
    eps = rng.normal(0.0, 1.0, n)
    u = np.zeros(n)
    for i in range(1, n):
        u[i] = 0.55 * u[i - 1] + eps[i]
    level = 4.0 * (t >= intervention)
    slope = 0.12 * np.maximum(t - intervention, 0.0)
    y = 50.0 + 0.20 * t + level + slope + u
    return pd.DataFrame({"period": t.astype(int), "outcome": y}), intervention


def design_matrix(period, intervention):
    t = np.asarray(period, dtype=float)
    post = (t >= intervention).astype(float)
    return pd.DataFrame({
        "intercept": 1.0,
        "time": t,
        "post_level": post,
        "post_slope": np.maximum(t - intervention, 0.0),
    })


def fit_its(frame, intervention, maxlags=6):
    if maxlags < 0:
        raise ValueError("maxlags must be nonnegative")
    x = design_matrix(frame["period"], intervention)
    return sm.OLS(frame["outcome"].astype(float), x).fit(
        cov_type="HAC", cov_kwds={"maxlags": maxlags}
    )


def fit_ar1_error(frame, intervention, maxiter=20):
    """Feasible GLS with AR(1) errors; rho is estimated iteratively."""
    if maxiter < 1:
        raise ValueError("maxiter must be positive")
    x = design_matrix(frame["period"], intervention)
    model = sm.GLSAR(frame["outcome"].astype(float), x, rho=1)
    result = model.iterative_fit(maxiter=maxiter)
    return result


def _ljung_box(values, lag):
    result = acorr_ljungbox(np.asarray(values), lags=[lag], return_df=True).iloc[0]
    return {"statistic": float(result["lb_stat"]), "p_value": float(result["lb_pvalue"])}


def analyze(seed=20261123):
    frame, intervention = generate_series(seed=seed)
    hac_model = fit_its(frame, intervention, maxlags=6)
    ar1_model = fit_ar1_error(frame, intervention)
    lb_lag = min(12, max(1, len(frame) // 5))
    hac_residuals = np.asarray(hac_model.resid)
    ar1_residuals = np.asarray(ar1_model.resid)
    whitened_residuals = np.asarray(ar1_model.model.whiten(ar1_residuals))
    coefficients = {}
    for name in hac_model.params.index:
        coefficients[name] = {
            "estimate": float(hac_model.params[name]),
            "hac_se": float(hac_model.bse[name]),
            "t_stat": float(hac_model.tvalues[name]),
            "p_value": float(hac_model.pvalues[name]),
            "ar1_gls_estimate": float(ar1_model.params[name]),
            "ar1_gls_se": float(ar1_model.bse[name]),
        }
    bandwidth = {}
    for lag in [0, 3, 6, 12]:
        fit = fit_its(frame, intervention, maxlags=lag)
        bandwidth[str(lag)] = {
            "se_level": float(fit.bse["post_level"]),
            "se_slope": float(fit.bse["post_slope"])
        }
    placebo = {}
    for date in [48, 60, 84, 96]:
        fit = fit_its(frame, date, maxlags=6)
        placebo[str(date)] = {
            "level": float(fit.params["post_level"]),
            "slope": float(fit.params["post_slope"]),
            "level_p": float(fit.pvalues["post_level"])
        }
    return {
        "synthetic_data": True,
        "seed": seed,
        "n_observations": int(len(frame)),
        "intervention_period": intervention,
        "coefficients": coefficients,
        "hac_ols_r_squared": float(hac_model.rsquared),
        "ar1_gls_rho": float(np.asarray(ar1_model.model.rho).reshape(-1)[0]),
        "residual_diagnostics": {
            "lag": lb_lag,
            "hac_ols_raw_residuals": _ljung_box(hac_residuals, lb_lag),
            "ar1_gls_raw_residuals": _ljung_box(ar1_residuals, lb_lag),
            "ar1_gls_whitened_residuals": _ljung_box(whitened_residuals, lb_lag),
        },
        "hac_bandwidth_sensitivity": bandwidth,
        "placebo_dates": placebo,
        "interpretation": (
            "HAC changes the covariance estimate, not the residual process. "
            "AR(1)-error GLS imposes a parametric serial-correlation model; "
            "inspect whitened residuals and sensitivity because misspecified "
            "error dynamics can invalidate its efficiency and inference claims."
        ),
        "warning": "Neither covariance correction nor AR(1) GLS establishes causal identification."
    }, frame, hac_model, ar1_model


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", default="outputs")
    parser.add_argument("--seed", type=int, default=20261123)
    args = parser.parse_args()
    result, frame, hac_model, ar1_model = analyze(args.seed)
    out = Path(args.output_dir)
    out.mkdir(parents=True, exist_ok=True)
    (out / "summary.json").write_text(json.dumps(result, indent=2) + "\n")
    frame = frame.copy()
    frame["fitted_hac_ols"] = hac_model.fittedvalues
    frame["residual_hac_ols"] = hac_model.resid
    frame["fitted_ar1_gls"] = ar1_model.fittedvalues
    frame["residual_ar1_gls"] = ar1_model.resid
    frame.to_csv(out / "series.csv", index=False)
    print(json.dumps({
        "intervention_period": result["intervention_period"],
        "level_hac_ols": result["coefficients"]["post_level"]["estimate"],
        "level_ar1_gls": result["coefficients"]["post_level"]["ar1_gls_estimate"],
        "estimated_ar1_rho": result["ar1_gls_rho"],
        "diagnostics": result["residual_diagnostics"]
    }, indent=2))


if __name__ == "__main__":
    main()
