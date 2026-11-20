# Y1-04 Problem Set 2 — Panel Data, Difference-in-Differences, and Time Series

## Problem 1 — Difference-in-differences

A utility introduces a time-of-use tariff to a treatment group. A comparison group remains on the standard tariff.

| Group | Pre-policy mean (kWh/month) | Post-policy mean (kWh/month) |
|---|---:|---:|
| Treatment | 1,000 | 900 |
| Comparison | 900 | 850 |

1. Calculate the treatment group's before/after change.
2. Calculate the comparison group's change.
3. Calculate the difference-in-differences estimate.
4. State the identifying assumption.
5. Explain why a single pre-period cannot establish parallel trends.
6. Discuss anticipation, spillovers, composition changes, and treatment selection.

## Problem 2 — Fixed effects

Write a panel regression with unit and time fixed effects for customer i in month t. Explain what variation identifies the treatment coefficient and why time-invariant customer characteristics are absorbed by unit fixed effects. Identify a time-varying confounder that remains a threat.

## Problem 3 — Time series and autocorrelation

An analyst regresses monthly electricity load on temperature and a time trend. Residuals show strong serial correlation.

1. Explain why conventional independent-error standard errors may be misleading.
2. Discuss seasonality, holidays, calendar effects, structural breaks, and weather nonlinearities.
3. Describe Newey-West/HAC standard errors and their limitations.
4. Explain why adding lags or differencing changes the estimand and interpretation.

## Problem 4 — Reproducible research design

Prepare a pre-analysis design note for a real energy-policy question. Include the estimand, unit of observation, sample, treatment/control definition, data source, model, identifying assumptions, threats, robustness tests, and a decision rule for abandoning causal language if assumptions fail.

## Submission

Provide calculations, model equations, a DAG or causal diagram, and a 1,000–1,500 word methods critique.