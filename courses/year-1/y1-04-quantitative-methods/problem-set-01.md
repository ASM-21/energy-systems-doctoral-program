# Y1-04 Problem Set 1 — Statistical Reasoning and OLS

## Problem 1 — Sampling and uncertainty

A utility reports average monthly household electricity consumption of 850 kWh from a random sample of 100 customers. The sample standard deviation is 240 kWh.

1. Calculate the standard error of the sample mean.
2. Construct an approximate 95% confidence interval using 1.96 standard errors.
3. Explain what the interval does and does not mean.
4. Describe how nonresponse or a non-random sample could invalidate the interpretation.

## Problem 2 — OLS derivation and interpretation

Consider the model:

    y_i = beta_0 + beta_1 x_i + u_i

1. Write the least-squares objective.
2. Derive the first-order conditions and the slope estimator.
3. Interpret beta_1 when y is annual household electricity consumption (MWh) and x is household floor area (square feet).
4. State the conditions under which the OLS slope is unbiased.
5. Explain why correlation between floor area and household income can complicate interpretation.

## Problem 3 — Heteroskedasticity and robust inference

An analyst regresses annual electricity expenditure on household income. Residual variance appears to increase with income.

1. Explain the distinction between heteroskedasticity and omitted-variable bias.
2. What happens to OLS coefficients under exogeneity but heteroskedastic errors?
3. Why might heteroskedasticity-robust standard errors be appropriate?
4. Why do robust standard errors not solve endogeneity?

## Problem 4 — Causal identification

A researcher compares average electricity use before and after a utility introduces time-of-use rates. Usage falls after implementation.

1. Why is the before/after difference not automatically a causal effect?
2. Identify plausible confounders and concurrent changes.
3. Describe a randomized rollout or credible comparison-group design.
4. State the assumptions required for a difference-in-differences design.
5. Explain how treatment selection and anticipation could bias estimates.

## Submission

Show derivations, interpret coefficients in real units, and submit a one-page identification critique. Do not use p-values as a substitute for design reasoning.