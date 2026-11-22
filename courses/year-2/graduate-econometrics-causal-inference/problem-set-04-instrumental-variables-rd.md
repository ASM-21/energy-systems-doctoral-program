# Problem Set 4: Instrumental Variables and Regression Discontinuity

**Level:** Graduate econometrics / doctoral preparation  
**Suggested effort:** 3–4 hours  
**Prerequisites:** Problem Sets 1–3, OLS, conditional expectation, asymptotic inference  
**Application:** Quasi-experimental evaluation of DER programs and interconnection rules

## Problem 1. Instrumental variables and the Wald estimand

A regulator randomly assigns an encouragement Z to eligible applicants to use an application-support service. Take-up D is 70% among encouraged applicants and 10% among controls. The outcome Y is a binary indicator for receiving a utility decision within 90 days. The reduced-form effect of Z on Y is 0.12.

1. Calculate the first-stage effect.
2. Calculate the Wald IV estimate.
3. State the population for which this estimate is a LATE.
4. State the relevance, independence, exclusion, and monotonicity assumptions.
5. Explain why the IV estimate need not equal the ATE or ATT.
6. Explain why a strong first stage does not establish the exclusion restriction.

## Problem 2. Two-stage least squares

Let Z be an instrument, D endogenous treatment, X a vector of pre-treatment covariates, and Y the outcome.

1. Write the first-stage regression.
2. Write the second-stage regression using the fitted treatment.
3. Explain why the second-stage standard errors must account for the first-stage estimation.
4. Explain why simply inserting fitted D into OLS and using ordinary OLS standard errors is incorrect.
5. Explain the role of partial R-squared and the first-stage F statistic.
6. Explain why the conventional F>10 rule is only a rough diagnostic, not a proof of instrument validity or a universal weak-instrument threshold.

## Problem 3. Exclusion restriction and instrument validity

Consider using distance to a utility customer-service office as an instrument for receiving application assistance.

1. Explain why distance may predict take-up.
2. Identify at least three pathways through which distance could affect interconnection outcomes other than assistance receipt.
3. Explain why adding observed covariates may not repair an implausible exclusion restriction.
4. Propose a more credible instrument or randomized encouragement design.
5. Explain how you would assess instrument strength and report uncertainty under weak identification.

## Problem 4. Sharp regression discontinuity

A hypothetical DER program offers a standardized application service to projects with nameplate capacity at or above a threshold c=100 kW. Let X be project capacity and D=1[X≥c]. The mean outcome just below the cutoff is 12, and the mean just above is 16.

1. Calculate the sharp RD discontinuity estimate.
2. State the continuity assumptions required for a local causal interpretation.
3. Explain why the estimate is local to the cutoff.
4. Describe a local-linear specification with separate slopes on each side.
5. Explain how bandwidth choice affects bias and variance.
6. Identify at least five RD diagnostics or robustness checks.

## Problem 5. Fuzzy regression discontinuity

At the same hypothetical threshold, treatment receipt increases from 35% just below c to 85% just above c. The outcome discontinuity is 2 units.

1. Calculate the first-stage discontinuity.
2. Calculate the fuzzy RD Wald ratio.
3. State the assumptions required for a local complier effect.
4. Explain why the reduced-form outcome jump is not the same as the treatment effect when compliance is imperfect.
5. Explain why a threshold appearing in a descriptive PUC table does not establish that the threshold assigns treatment.

## Problem 6. Manipulation and policy eligibility

Suppose project developers can choose reported nameplate capacity or stage applications to fall just below an eligibility cutoff.

1. Explain how precise sorting around the cutoff threatens RD identification.
2. Describe density and covariate-continuity diagnostics.
3. Explain why a donut RD may help in some cases and what it sacrifices.
4. Explain how measurement error in the running variable affects the design.
5. State how tariff definitions, AC/DC capacity conventions, aggregation rules, and application dates must be verified before constructing treatment assignment.

## Problem 7. Design memo

Write a 500–700 word memo proposing either an IV or RD design for an energy-policy question. Define the instrument or running variable, treatment, outcome, estimand, assumptions, first-stage evidence, diagnostics, inference, and sensitivity analysis. Explain which assumptions cannot be tested directly.

## Submission standard

An instrument is not valid merely because it is correlated with treatment. A discontinuity is not causal merely because outcomes differ around a cutoff. The institutional assignment rule and the exclusion/continuity assumptions must be defended.
