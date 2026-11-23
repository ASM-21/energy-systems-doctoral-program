# Problem Set 5: Synthetic Control and Comparative Case Studies

**Level:** Advanced graduate / doctoral preparation  
**Suggested effort:** 3–4 hours  
**Prerequisites:** Potential outcomes, panel data, difference-in-differences, constrained optimization  
**Application:** Evaluating a utility-specific DER policy, grid investment, or regulatory intervention when one or a few jurisdictions are treated

## Problem 1. Constructing the estimator

A treated utility has annual pre-intervention outcomes \(Y_{1t}\). A donor pool contains \(J\) untreated utilities with outcomes \(Y_{jt}\). Synthetic control chooses weights \(w_j\) to minimize pre-intervention predictor imbalance:

\[
\min_{w} (X_1-X_0w)'V(X_1-X_0w)
\quad\text{s.t.}\quad w_j\geq0,\;\sum_{j=1}^Jw_j=1.
\]

1. Explain the convex-hull interpretation of the simplex constraints.
2. Derive the synthetic outcome \(\widehat Y_{1t}^{N}=\sum_jw_jY_{jt}\) and treatment-gap estimator \(\widehat\tau_t=Y_{1t}-\widehat Y_{1t}^{N}\).
3. Explain why predictor selection and the matrix \(V\) are consequential.
4. Explain why minimizing pre-treatment outcome error is not equivalent to identifying a causal effect.
5. State the no-interference and donor-pool stability assumptions in this setting.

## Problem 2. Numerical weight construction

Three donor utilities have pre-period predictor vectors:

\[
X_1=(10,20)',\quad X_2=(8,18)',\quad X_3=(12,24)',\quad X_T=(9.5,20.5)'.
\]

1. Determine whether the treated predictor lies in the convex hull of the three donors.
2. Find nonnegative weights summing to one that exactly reproduce \(X_T\), if possible.
3. Explain why multiple exact solutions may exist and why a numerical optimizer can select one based on its objective and regularization.
4. Add a third predictor that is poorly matched by all donors. Explain why a visually good two-dimensional fit can conceal poor multivariate balance.

## Problem 3. Pre-fit, post-fit, and inference

A treated unit has pre-treatment RMSPE 0.8 and post-treatment RMSPE 4.0. A placebo unit has pre-RMSPE 0.2 and post-RMSPE 1.0.

1. Calculate the post/pre RMSPE ratio for each unit.
2. Explain why a large ratio is suggestive but not by itself a conventional p-value.
3. Explain why placebo units with extremely poor pre-fit should generally not be treated as equally informative.
4. Describe in-space placebo inference and its exchangeability limitation.
5. Explain the difference between placebo permutation inference and sampling-based confidence intervals.

## Problem 4. Donor-pool design and spillovers

A Pennsylvania utility changes its DER interconnection process. Candidate donors include neighboring EDCs, utilities in other PJM states, and utilities in non-PJM regions.

1. Identify institutional, market, weather, load, and regulatory dimensions that should inform donor eligibility.
2. Explain why a neighboring utility may be a poor control if the policy or market shock spills across its service territory.
3. Define a pre-specified donor inclusion/exclusion rule.
4. Propose sensitivity analyses using alternative donor pools and leave-one-out re-estimation.
5. Explain why a donor should not be removed merely because it weakens the preferred result.

## Problem 5. Multiple treated units and augmented methods

1. Explain how generalized synthetic control and interactive fixed-effects models extend the single-treated-unit setting.
2. Describe the bias-variance trade-off introduced by regularization or augmentation.
3. Explain why extrapolating beyond the donor convex hull can improve fit but increase model dependence.
4. Compare synthetic control with two-way fixed effects and modern group-time DID estimators.
5. Identify settings where synthetic control is inappropriate or dominated by a simpler design.

## Problem 6. Energy-policy design memo

Write a 600–800 word proposal for a synthetic-control evaluation of one policy or infrastructure intervention. Specify:

- treatment unit, intervention date, outcome, estimand, and observation frequency;
- donor pool and institutional eligibility criteria;
- pre-treatment period length and predictor set;
- weight objective, constraints, and tuning protocol;
- pre-fit acceptance rule established before viewing post-treatment gaps;
- in-space and in-time placebo strategies;
- leave-one-out and donor-pool sensitivity analyses;
- inference limitations, spillovers, concurrent interventions, and data quality.

Do not use the 2023–2025 Pennsylvania EDC aggregate panel to claim a causal effect of a 2026 intervention: it contains no post-intervention observations. A descriptive pre-period is not a completed counterfactual design.

## Submission standard

Report the full donor list, weights, predictor balance, pre-treatment fit, time path of the treatment gap, placebo distribution, and sensitivity results. State the identification assumptions in plain language. Do not interpret a large post/pre RMSPE ratio as definitive proof of causality.
