# Econometrics and Causal Inference Projects

These projects build from regression diagnostics toward experimental design, panel estimators, counterfactual construction, time-series intervention analysis, and event-history methods.

## Recommended progression

1. [OLS and robust inference](ols-energy-demand/README.md) — regression, heteroskedasticity-robust standard errors, and diagnostics.
2. [Randomized experiments](randomized-experiments/README.md) — ITT, Neyman inference, randomization inference, power, and cluster design.
3. [Difference-in-differences](difference-in-differences/README.md) — 2×2 DID and cohort-time ATT with never-treated controls.
4. [Synthetic control](synthetic-control/README.md) — pre-period-only donor weights, fit diagnostics, and placebo comparisons.
5. [Interrupted time series](interrupted-time-series/README.md) — segmented regression, HAC inference, autocorrelation, and placebo dates.
6. [Competing-risks survival analysis](competing-risks-survival/README.md) — censoring, Kaplan-Meier net risk, and Aalen-Johansen cumulative incidence.

## Prerequisites

OLS requires Y1-04 regression foundations. Randomized experiments and DID require potential-outcomes notation and sampling/inference. Synthetic control requires optimization and panel structure. Interrupted time series requires time-series regression and serial-correlation diagnostics. Competing risks requires probability, event-history data structure, and censoring concepts.

## Identification discipline

A working estimator is not proof of causal identification. Each application must state the estimand, assignment mechanism, comparison group, assumptions, treatment timing, missingness/censoring, uncertainty estimator, and relevant falsification or sensitivity analysis. The supplied examples are synthetic unless the project explicitly identifies a public empirical dataset. Placebo ranks and model diagnostics are not automatically valid p-values or causal tests.
