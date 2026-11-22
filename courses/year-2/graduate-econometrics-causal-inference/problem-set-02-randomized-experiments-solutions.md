# Problem Set 2: Worked Solutions and Design Notes

## Problem 1. Difference in means

The ITT estimate is
\[
\widehat{ITT}=0.64-0.57=0.07.
\]
With \(n_1=n_0=500\), the Neyman standard error is
\[
SE(\widehat{ITT})=
\sqrt{\frac{0.2304}{500}+\frac{0.2451}{500}}
=\sqrt{0.000951}
\approx0.03084.
\]
The approximate 95% confidence interval is
\[
0.07\pm1.96(0.03084)
=[0.0096,0.1304].
\]
The null is \(H_0:ITT=0\). Under the stated approximation, the interval excludes zero. The estimated effect is a 7-percentage-point increase in the probability of a utility decision within 90 days for applicants assigned an offer.

Random assignment makes assignment independent of potential outcomes in expectation. The ITT compares outcomes by assigned group, retaining noncompliers in their original assignment group. It therefore estimates the effect of the offer policy, not necessarily the effect of actually receiving assistance.

## Problem 2. Regression adjustment

A strong pre-treatment predictor of Y can reduce residual variance and improve precision. In a randomized experiment, D is independent of potential outcomes by design, so the unadjusted difference in means is unbiased in expectation. Covariate adjustment is a precision strategy, not a substitute for randomization.

If treatment effects vary with X, pre-specify treatment-by-X interactions or estimate conditional treatment effects and standardize them over the target population's X distribution. Report the target population and weighting rule; do not present a single additive coefficient as a universal effect without justification. A post-assignment variable may be affected by treatment or share causes with the outcome. Conditioning on it can block a mediated effect or induce collider bias. Upgrade-study requests are likely downstream of application and network conditions and should not be automatically included as a baseline control.

Missing baseline covariates should be described by treatment arm and handled using a pre-specified strategy such as missingness indicators, multiple imputation under defensible assumptions, or complete-case analysis with sensitivity checks. Missing outcomes require explicit follow-up and missing-data assumptions; withdrawals are not automatically missing outcomes.

## Problem 3. Encouragement design

The first stage is
\[
E[D_{\text{received}}\mid Z=1]-E[D_{\text{received}}\mid Z=0]
=0.70-0.20=0.50.
\]
The Wald estimate is
\[
\widehat{LATE}=\frac{ITT}{\text{first stage}}
=\frac{0.07}{0.50}=0.14.
\]
A complier LATE interpretation requires randomized assignment Z, relevance, exclusion of any direct effect of the offer except through receipt, monotonicity (no defiers), and a well-defined treatment. The ITT remains valid for the effect of the offer under valid randomization even if exclusion fails. Monotonicity could fail if some applicants would use assistance only when not offered by the program but avoid it when formally offered, although this behavior would need a substantive explanation and evidence.

## Problem 4. Power

The pooled average variance approximation is
\[
\bar\sigma^2=\frac{0.2304+0.2451}{2}=0.23775.
\]
With 500 observations per arm:
\[
SE_0=\sqrt{\frac{2(0.23775)}{500}}
\approx0.03084.
\]
The approximate MDE is
\[
MDE=(1.96+0.84)(0.03084)\approx0.0864.
\]
The observed 0.07 estimate is below this approximate 80%-power MDE. The experiment may not reliably detect a 7-percentage-point effect at the stated sample size, even though its realized approximate confidence interval happens to exclude zero. A non-significant result would not prove zero effect; it could reflect imprecision.

Potential design improvements include increasing the sample, improving outcome measurement, stratifying randomization on strong pre-treatment predictors, reducing attrition, increasing the number of independent feeder clusters, or selecting a more informative follow-up outcome. Do not improve apparent power by conditioning on post-treatment variables or changing the primary outcome after observing results.

## Problem 5. Clustering and interference

Individual assignment may violate no-interference if treated applicants affect feeder congestion, study queues, or hosting capacity for control applicants. With \(m=20\) and \(\rho=0.05\):
\[
DE=1+(m-1)\rho=1+19(0.05)=1.95.
\]
The rough effective sample size is
\[
n_{\mathrm{eff}}=\frac{1000}{1.95}\approx512.8.
\]
This approximation does not account for a small number of clusters or unequal cluster sizes. Cluster randomization reduces within-feeder contamination but requires enough independent feeders. A feeder-level estimand could be the effect of an assistance or flexible-export program on the share of eligible feeder applications receiving a decision within 90 days, or on total approved export capacity subject to a defined engineering constraint.

## Problem 6. Randomization inference and pre-analysis

Under a sharp null, repeatedly reassign treatment labels according to the actual randomization mechanism, recompute the test statistic, and compare the observed statistic with the permutation distribution. Preserve strata, blocks, cluster assignments, and treatment probabilities. Arbitrarily permuting individual labels when assignment occurred by feeder does not reproduce the design.

A suitable pre-analysis plan defines the primary outcome, ITT estimand, complete-application time origin, 90-day horizon, assignment unit, analysis model, randomization-inference procedure, missing-data strategy, subgroup set, multiple-testing adjustment, and all exclusions before outcome analysis. Secondary outcomes may include completeness duration, withdrawal, and agreement execution, but should be labeled secondary.

## Problem 7. Design memo: minimum standard

A defensible memo defines a feasible eligible population and a transparent assignment mechanism. If feeder spillovers are plausible, randomize at feeder or another defensible cluster level, or use a partial-interference design with an explicit exposure mapping. Define the ITT as the effect of the offer, not receipt. Treat take-up as a first-stage outcome. Specify follow-up and administrative censoring, distinguish withdrawal from missingness, and calculate power using the number of independent assignment units. Preserve normal interconnection rights and engineering standards for all participants. Ensure the pilot does not delay or disadvantage control applicants.
