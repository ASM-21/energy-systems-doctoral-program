"""Reproducible OLS demonstration on synthetic household energy data."""
from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd
import statsmodels.api as sm


def generate_data(n: int = 500, seed: int = 20261120) -> pd.DataFrame:
    if n < 30:
        raise ValueError("Use at least 30 observations for this teaching exercise.")
    rng = np.random.default_rng(seed)
    income = np.clip(rng.lognormal(mean=3.8, sigma=0.45, size=n), 10, 300)
    floor_area = np.clip(900 + 5.0 * income + rng.normal(0, 300, n), 400, 4500)
    hdd = np.clip(rng.normal(5000, 900, n), 2500, 8000)
    electric_heat = rng.binomial(1, 0.35, n)
    sigma = 500 + 25 * income
    noise = rng.normal(0, sigma, n)
    annual_kwh = (
        1800
        + 1.25 * floor_area
        + 3.0 * income
        + 0.22 * hdd
        + 2800 * electric_heat
        + noise
    )
    return pd.DataFrame(
        {
            "annual_kwh": annual_kwh,
            "floor_area_sqft": floor_area,
            "income_1000s_usd": income,
            "heating_degree_days": hdd,
            "electric_heat": electric_heat,
        }
    )


def estimate_models(data: pd.DataFrame) -> dict:
    required = {
        "annual_kwh",
        "floor_area_sqft",
        "income_1000s_usd",
        "heating_degree_days",
        "electric_heat",
    }
    missing = required.difference(data.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")
    if data[list(required)].isna().any().any():
        raise ValueError("Teaching dataset contains missing values.")

    y = data["annual_kwh"]
    simple_x = sm.add_constant(data[["floor_area_sqft"]])
    full_x = sm.add_constant(
        data[["floor_area_sqft", "income_1000s_usd", "heating_degree_days", "electric_heat"]]
    )
    simple = sm.OLS(y, simple_x).fit()
    full = sm.OLS(y, full_x).fit()
    robust = sm.OLS(y, full_x).fit(cov_type="HC3")
    return {"simple": simple, "full": full, "robust": robust}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--n", type=int, default=500)
    parser.add_argument("--seed", type=int, default=20261120)
    parser.add_argument("--output", type=Path, default=Path("results"))
    args = parser.parse_args()

    args.output.mkdir(parents=True, exist_ok=True)
    data = generate_data(args.n, args.seed)
    data_path = args.output / "synthetic_household_energy.csv"
    data.to_csv(data_path, index=False)
    models = estimate_models(data)

    summary_path = args.output / "regression_summary.txt"
    with summary_path.open("w", encoding="utf-8") as handle:
        handle.write("SYNTHETIC TEACHING DATA — NOT EMPIRICAL EVIDENCE\n")
        handle.write(f"n={args.n}; seed={args.seed}\n\n")
        handle.write("BIVARIATE OLS\n")
        handle.write(models["simple"].summary().as_text())
        handle.write("\n\nMULTIVARIATE OLS (CONVENTIONAL SE)\n")
        handle.write(models["full"].summary().as_text())
        handle.write("\n\nMULTIVARIATE OLS (HC3 ROBUST SE)\n")
        handle.write(models["robust"].summary().as_text())
    print(f"Wrote {data_path}")
    print(f"Wrote {summary_path}")
    print(models["robust"].summary())


if __name__ == "__main__":
    main()
