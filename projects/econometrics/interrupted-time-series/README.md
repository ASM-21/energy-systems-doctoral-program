# Interrupted Time Series and Dynamic Regression Lab

A synthetic monthly utility-outcome example comparing segmented OLS with Newey–West HAC inference against feasible GLS with AR(1) errors. It reports raw and whitened residual diagnostics, HAC bandwidth sensitivity, and placebo intervention dates.

**All observations are synthetic.** The example demonstrates estimator behavior under a known data-generating process; it is not an estimate of any real utility or policy.

## Run

```bash
python -m pip install -r requirements.txt
python interrupted_time_series.py --output-dir /tmp/its-results
python -m unittest discover -s . -p 'test_*.py' -v
```

## Mean model and estimands

[
Y_t=\beta_0+\beta_1t+\beta_2D_t+\beta_3(t-T_0)D_t+u_t.
]

The design matrix separates baseline trend, immediate level change, and trend change. The coefficient \(\beta_2\) is the modeled immediate shift at \(T_0\); \(\beta_3\) is the change in slope per period. They are descriptive conditional parameters unless a credible counterfactual design justifies causal interpretation.

## Two error treatments

1. **Segmented OLS with HAC covariance.** OLS estimates the conditional mean; Newey–West HAC changes the estimated covariance matrix. It does not remove serial correlation, change fitted values, or correct a misspecified conditional mean.
2. **AR(1)-error feasible GLS.** The lab estimates \(u_t=\rho u_{t-1}+\varepsilon_t\) iteratively. This can improve efficiency when the AR(1) model is adequate, but it is more model-dependent. A misspecified AR order, structural break in the error process, heteroskedasticity, or outliers can distort estimates and standard errors.

The output reports Ljung–Box diagnostics for raw OLS residuals, raw GLS residuals, and GLS-whitened residuals. A non-rejection is not proof of white noise; a rejection is a specification warning, not an automatic instruction to increase AR order until a preferred result appears. The AR coefficient and residual plots should be interpreted with domain knowledge and sensitivity checks.

## Interpretation controls

- A significant level or slope coefficient is not sufficient for causal attribution.
- The intervention date is externally specified in the synthetic example; placebo dates are diagnostic, not a formal multiple-testing-adjusted test.
- Neither HAC nor AR(1) GLS fixes confounding, concurrent shocks, outcome revisions, anticipation, endogenous policy timing, or invalid counterfactual trends.
- Unit-root and cointegration tests are not bundled into the estimator: deterministic terms, lag choices, structural breaks, and integration order require substantive specification.
- The lab uses a single intervention and a single series. It does not implement controlled ITS, ARIMA intervention models, Bayesian structural time series, or state-space forecasting.

## Outputs

- `summary.json`: OLS/HAC and AR(1)-GLS coefficient estimates, uncertainty, estimated AR coefficient, residual diagnostics, HAC bandwidth sensitivity, and placebo-date results.
- `series.csv`: synthetic observations, both fitted series, and residuals.
