# Interrupted Time Series and Dynamic Regression Lab

A synthetic monthly utility-outcome example for segmented regression with Newey–West HAC inference, residual autocorrelation diagnostics, placebo intervention dates, and sensitivity to HAC bandwidth.

**All observations are synthetic.** The example demonstrates estimator behavior under a known data-generating process; it is not an estimate of any real utility or policy.

## Run

```bash
python -m pip install -r requirements.txt
python interrupted_time_series.py --output-dir /tmp/its-results
python -m unittest discover -s . -p 'test_*.py' -v
```

## Model

\[
Y_t=\beta_0+\beta_1t+\beta_2D_t+\beta_3(t-T_0)D_t+\epsilon_t.
\]

The design matrix separates baseline trend, immediate level change, and trend change. OLS coefficients are paired with Newey–West HAC covariance estimates. HAC affects uncertainty estimation, not causal identification.

The script reports the primary model, selected coefficient standard errors, Ljung–Box residual diagnostic, alternative HAC maximum lags, and placebo-date coefficients.

## Interpretation controls

- A significant level or slope coefficient is not sufficient for causal attribution.
- The intervention date is externally specified in the synthetic example; placebo dates are diagnostic, not a formal multiple-testing-adjusted test.
- Serial-correlation-robust inference does not fix confounding, concurrent shocks, outcome revisions, or misspecified trend shape.
- Unit-root and cointegration tests are deliberately not bundled into the core estimator: their deterministic terms, lag choices, and break assumptions require substantive specification. See the course assignment for those derivations.
- This lab uses a single intervention and a single series. It does not implement controlled ITS, Bayesian structural time series, ARIMA intervention models, or state-space forecasting.

## Outputs

- `summary.json`: coefficients, HAC standard errors, fit diagnostics, Ljung–Box test, bandwidth sensitivity, and placebo-date results.
- `series.csv`: synthetic observations and fitted values.
