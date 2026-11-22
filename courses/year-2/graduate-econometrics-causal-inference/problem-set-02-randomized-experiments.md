# Problem Set 2: Randomized Experiments, Regression Adjustment, and Power

**Level:** Graduate econometrics / doctoral preparation  
**Suggested effort:** 2–3 hours  
**Prerequisites:** Problem Set 1, sampling distributions, OLS, robust standard errors  
**Application:** Randomized application-assistance pilot

## Problem 1. Difference in means under random assignment

A regulator randomly offers optional application-completion assistance to 1,000 eligible DER applicants. Five hundred are assigned an offer and 500 are assigned to the control group. The outcome is an indicator for receiving a utility decision within 90 days.

The observed treatment-group outcome mean is 0.64 and the control-group mean is 0.57. The sample variances are 0.2304 and 0.2451, respectively.

1. Calculate the intention-to-treat (ITT) estimate.
2. Calculate the Neyman standard error for the difference in means.
3. Construct an approximate 95% confidence interval using 1.96 standard errors.
4. State the null hypothesis and interpret the interval.
5. Explain why random assignment identifies the ITT in expectation even if some applicants do not use the assistance.

## Problem 2. Regression adjustment and precision

Suppose X is a pre-treatment measure of application readiness. Consider the regression

\[
Y_i=\alpha+\tau D_i+\beta(X_i-\bar X)+\epsilon_i.
\]

1. Explain why including a pre-treatment covariate can improve precision in a randomized experiment.
2. Explain why regression adjustment is not required for unbiasedness under valid random assignment.
3. If treatment-effect heterogeneity is plausible, explain how you would pre-specify interactions and standardize predictions to a target population.
4. Explain why controlling for a post-assignment variable such as whether an applicant requested an upgrade study may change the estimand or induce bias.
5. Describe how you would handle missing baseline X and missing outcome Y.

## Problem 3. Randomized encouragement and treatment-on-the-treated

Only some applicants assigned to the offer actually use the assistance. Take-up is 70% in the offer group and 20% in the control group. The ITT outcome effect is 0.07.

1. Calculate the first-stage effect of assignment on assistance receipt.
2. Calculate the Wald instrumental-variable estimate.
3. State the assumptions needed to interpret the Wald estimate as a local average treatment effect (LATE) for compliers.
4. Explain why the ITT remains policy-relevant even if the exclusion restriction for the IV interpretation is not credible.
5. Explain how monotonicity could fail in this setting.

## Problem 4. Minimum detectable effect and power

Use the sample variances and allocation in Problem 1.

1. Calculate the standard error under the null using the pooled average variance approximation.
2. Calculate the approximate minimum detectable effect (MDE) for 80% power and a two-sided 5% test using \(z_{0.975}=1.96\) and \(z_{0.80}=0.84\).
3. Compare the MDE with the observed ITT estimate.
4. Explain why a non-significant result would not establish that the intervention has no practically meaningful effect.
5. Identify at least four design changes that could improve power without compromising the estimand.

## Problem 5. Cluster randomization and interference

Applicants share feeders. The treatment may alter feeder-level queue congestion or available hosting capacity, affecting outcomes for control applicants on the same feeder.

1. Explain why individual-level randomization may violate no-interference.
2. Suppose clusters contain an average of 20 applicants and the intra-cluster correlation is 0.05. Calculate the design effect \(1+(m-1)\rho\).
3. Calculate the approximate effective sample size corresponding to 1,000 applicants under this design effect.
4. Explain the trade-off between cluster randomization, number of clusters, and statistical power.
5. Define a feeder-level estimand that would be meaningful to a regulator.

## Problem 6. Randomization inference and pre-analysis plans

1. Describe a permutation/randomization-inference procedure for testing the sharp null of no effect.
2. Explain why the treatment assignment mechanism must be preserved in the permutations, especially under cluster randomization or stratified assignment.
3. Define one primary outcome, one primary estimand, one follow-up horizon, and a limited set of pre-specified secondary outcomes for the pilot.
4. Explain how multiple outcomes and subgroup analysis can inflate false-positive risk.
5. Explain what should be included in a pre-analysis plan before outcome data are examined.

## Problem 7. Design memo

Write a 400–600 word memo specifying a randomized or randomized-encouragement design for an application-assistance pilot. State the unit of randomization, eligibility, treatment, control, estimand, outcome, time origin, follow-up, noncompliance, censoring, interference strategy, power calculation, and ethical safeguards.

## Submission standard

Distinguish the effect of being offered assistance (ITT) from the effect of actually receiving assistance (LATE/TOT). Report standard errors, confidence intervals, and power assumptions. A randomized offer does not automatically randomize receipt.
