# Problem Set 3: Panel Data, Difference-in-Differences, and Event Studies

**Level:** Graduate econometrics / doctoral preparation  
**Suggested effort:** 3–4 hours  
**Prerequisites:** Problem Sets 1–2, OLS, fixed effects, potential outcomes  
**Application:** Utility policy changes and DER interconnection outcomes

## Problem 1. Two-group, two-period difference-in-differences

A policy is introduced for one group of utilities between periods 0 and 1. A second group is not exposed during the observation window. The mean outcome is:

| Group | Pre-policy | Post-policy |
|---|---:|---:|
| Treated | 10 | 14 |
| Comparison | 8 | 10 |

1. Calculate the treated group's before-after change.
2. Calculate the comparison group's before-after change.
3. Calculate the difference-in-differences estimate.
4. Write the 2×2 regression specification with group, period, and interaction terms. Identify the coefficient of interest.
5. Explain the parallel-trends assumption in potential-outcomes notation.
6. Explain why a significant interaction coefficient does not establish that parallel trends holds.

## Problem 2. Violation of parallel trends

Suppose the treated group's observed outcome rises from 10 to 14, while the comparison group's outcome rises from 8 to 10. However, absent treatment, the treated group would have experienced a three-unit increase, not a two-unit increase.

1. Calculate the true treatment effect in the treated group.
2. Calculate the DID estimate from the observed group means.
3. Calculate the bias.
4. Explain why adding group fixed effects and time fixed effects does not solve this violation.
5. Identify evidence and design choices that could make parallel trends more plausible.

## Problem 3. Event-study specification

A policy is adopted at different dates by different utilities. Let \(G_i\) denote the first treated period for unit i. Consider an event-study regression with event-time indicators relative to \(G_i\), omitting event time -1.

1. Write a generic event-study equation with unit and calendar-time fixed effects.
2. Explain the role of the omitted reference period.
3. Explain what pre-treatment event-time coefficients can and cannot tell you.
4. Explain why conventional two-way fixed-effects event-study coefficients can be contaminated by heterogeneous treatment effects under staggered adoption.
5. Describe the logic of group-time ATT estimators and interaction-weighted event studies.
6. Explain why already-treated units may be invalid controls for later-treated units.

## Problem 4. Clustered inference

A policy is assigned at the EDC level, but the dataset contains 2,000 applications across 10 EDCs.

1. Explain why standard errors clustered by application are generally inappropriate.
2. State the relevant clustering level and why it follows the assignment mechanism.
3. Explain why 10 clusters create a serious small-cluster inference problem.
4. Discuss wild cluster bootstrap, randomization inference, and design-based alternatives.
5. Explain why adding more applications within the same 10 EDCs does not necessarily solve the limited-independent-cluster problem.

## Problem 5. Staggered adoption and negative weights

Three utility groups adopt a policy in periods 2, 3, and never, respectively. Treatment effects grow over event time and differ across groups.

1. Explain the comparisons that a conventional two-way fixed-effects estimator may use.
2. Explain how already-treated units can become controls for later-treated units.
3. Explain why negative or non-convex weights can make the TWFE coefficient difficult to interpret as an average treatment effect.
4. Propose a group-time ATT design and identify the comparison group at each treatment date.
5. State the assumptions required for group-time causal effects and dynamic aggregation.

## Problem 6. Application to Pennsylvania DER interconnection

The PUC aggregate panel covers reporting years 2023–2025, ending May 31, 2025. Relevant PPL Rule 12 applicability and DER Management implementation milestones occur in January 2026.

1. Explain why the existing panel cannot estimate a post-policy effect.
2. Identify the minimum additional time periods and outcome measures needed for a difference-in-differences design.
3. Explain why another Pennsylvania EDC is not automatically an untreated comparison group.
4. Define a plausible application-level or EDC-level estimand, and explain the trade-off.
5. State how you would handle overlapping policies, project composition, changing review definitions, and feeder-level spillovers.

## Problem 7. Research design memo

Write a 500–700 word memo proposing a panel or event-study evaluation of an energy-policy intervention. Specify treatment timing, comparison units, outcome, estimand, pre-period, post-period, clustering, parallel-trends diagnostics, staggered-adoption method, and sensitivity analysis. If the available data do not support the design, state that conclusion.

## Submission standard

A difference-in-differences estimator is not identified by the presence of panel data alone. State the counterfactual trend assumption, define the treatment timing, justify the comparison group, and use inference appropriate to the assignment level.
