# Y1-04 Problem Set 2 — Solution Notes

## Problem 1

Treatment change = 900 - 1,000 = -100 kWh/month. Comparison change = 850 - 900 = -50 kWh/month. Difference-in-differences:

    DID = (-100) - (-50) = -50 kWh/month

The estimate is a treatment effect only under assumptions including parallel untreated trends, no anticipation, no differential concurrent shocks, stable composition, and no spillovers that contaminate the comparison. One pre-period cannot show whether trends were parallel. Treatment selection based on expected consumption changes can bias the estimate.

## Problem 2

A common two-way fixed-effects specification is:

    y_it = alpha_i + lambda_t + beta*Treat_it + X_it'gamma + epsilon_it

Unit fixed effects absorb time-invariant customer attributes; time fixed effects absorb shocks common to all units in a period. Identification comes from within-unit changes in treatment relative to contemporaneous comparison changes, subject to the design assumptions. Time-varying occupancy, income, weather exposure, prices, or equipment changes may still confound results.

For staggered adoption with heterogeneous effects, conventional two-way fixed-effects estimators can combine comparisons in problematic ways. Use an estimator appropriate to the treatment timing and effect structure.

## Problem 3

Serial correlation means errors across periods are dependent; conventional standard errors can understate uncertainty. Energy load requires careful treatment of daily/weekly/annual seasonality, holidays, temperature nonlinearities, calendar composition, and structural change. HAC/Newey-West estimators adjust covariance estimates for specified autocorrelation structures under asymptotic conditions, but do not fix misspecification, endogeneity, short samples, or invalid causal designs. Lags and differencing change the conditional relationship and may discard long-run information.

## Problem 4

A defensible design specifies an estimand and a decision rule before estimation. The researcher should distinguish a failed identification strategy from a null treatment effect and report deviations from the plan.