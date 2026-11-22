# Problem Set 4: Worked Solutions and Identification Notes

## Problem 1. Wald estimand

The first stage is \(0.70-0.10=0.60\). The Wald estimate is
\[
\widehat{LATE}=\frac{0.12}{0.60}=0.20.
\]
Under the IV assumptions, this is the average treatment effect for compliers: units whose assistance receipt is changed by the encouragement.

The assumptions are:
- **Relevance:** Z changes the probability of D.
- **Independence:** Z is as-if randomly assigned, possibly conditional on pre-treatment X.
- **Exclusion:** Z affects Y only through D.
- **Monotonicity:** no unit is induced to avoid assistance by being encouraged when they would otherwise use it.

The LATE need not equal ATE or ATT because effects can differ across compliers, always-takers, never-takers, and other units. A strong first stage establishes relevance, not exclusion or independence.

## Problem 2. 2SLS

The first stage is
\[
D_i=\pi_0+\pi_1 Z_i+X_i'\pi_2+v_i.
\]
The second stage is
\[
Y_i=\alpha+\tau\widehat D_i+X_i'\beta+u_i.
\]
The second-stage uncertainty must account for the fact that \(\widehat D\) is estimated. Standard 2SLS software computes the appropriate IV covariance estimator. Treating fitted D as observed and applying ordinary OLS standard errors understates or otherwise misstates uncertainty.

The partial R-squared describes the instrument's incremental explanatory power for D after conditioning on X. The first-stage F statistic is a diagnostic for weak relevance under its assumptions. A heuristic threshold is not a universal guarantee; weak instruments can produce biased finite-sample estimates and unreliable conventional confidence intervals. Use weak-IV-robust procedures where appropriate.

## Problem 3. Exclusion restriction

Distance may affect the probability of visiting or using an assistance office, making it relevant. But distance may also proxy for rurality, broadband access, income, contractor availability, utility service-center geography, travel time for inspections, and local labor markets. These channels can directly affect application completeness or time to interconnection, violating exclusion.

Adding observed controls does not prove that all such direct pathways are blocked. A randomized encouragement with a clearly limited offer is often more defensible, although the offer itself must not directly change the outcome outside treatment receipt. Report first-stage estimates, partial R-squared, weak-IV diagnostics, and confidence intervals robust to weak identification.

## Problem 4. Sharp RD

The discontinuity is \(16-12=4\) outcome units. A local causal interpretation requires that, absent treatment, conditional expected potential outcomes vary continuously through the cutoff and that units cannot precisely manipulate the running variable in a way related to potential outcomes. The treatment assignment rule must be correctly specified and measured.

A local-linear specification can be written
\[
Y_i=\alpha+\tau D_i+\beta_-(X_i-c)
+\beta_+D_i(X_i-c)+\epsilon_i
\]
within a selected bandwidth around c, with appropriate kernel weights. The coefficient \(\tau\) is the cutoff discontinuity. Narrow bandwidths reduce extrapolation bias but increase variance; wide bandwidths increase sample size but can introduce functional-form bias.

Diagnostics include density/manipulation tests, covariate continuity, alternative bandwidths, alternative polynomial orders (with local linear preferred over high-order global polynomials), donut specifications, placebo cutoffs, placebo outcomes, and sensitivity to running-variable definitions. No diagnostic proves the continuity assumption.

## Problem 5. Fuzzy RD

The first-stage jump is \(0.85-0.35=0.50\). The fuzzy RD Wald ratio is
\[
\widehat{LATE}_{RD}=\frac{2}{0.50}=4.
\]
The interpretation is a local average treatment effect for compliers at the threshold, subject to continuity of potential outcomes and treatment receipt, a nonzero first stage, monotonicity, and a valid exclusion/assignment rule at the cutoff. The reduced-form jump is the effect of eligibility at the threshold; it is not the effect of treatment receipt when eligibility does not perfectly determine receipt.

A 500 kW category in a PUC report may be a reporting split, not a treatment-eligibility rule. A threshold must come from the controlling statute, tariff, program rules, or actual assignment mechanism.

## Problem 6. Manipulation and eligibility

If developers can precisely select capacity around c, units just below and above may differ in unobserved project characteristics. A density test can identify unusual bunching; predetermined covariates should be smooth at the cutoff. Neither diagnostic fully establishes no manipulation.

A donut RD excludes observations very close to c, which can reduce direct sorting but changes the local comparison and may reduce precision. Measurement error in capacity can misclassify treatment and blur the discontinuity. The analyst must verify whether the rule uses AC or DC nameplate capacity, inverter rating, aggregated project capacity, export capability, application received date, or another legal definition. A published descriptive size-band split is not enough.

## Problem 7. Design memo: minimum standard

A strong memo identifies the legal or institutional assignment mechanism and the exact treatment contrast. For IV, it defends relevance, independence, exclusion, and monotonicity, not merely a first-stage correlation. For RD, it documents the running variable, cutoff, legal treatment rule, continuity assumptions, sorting risks, and local estimand. It pre-specifies bandwidth or weak-IV inference, clustering, placebo checks, and sensitivity analysis. It clearly distinguishes testable implications from assumptions that cannot be verified from observed data alone.
