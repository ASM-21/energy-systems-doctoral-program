# Pre-Analysis Plan Template for Energy Policy Research

Use this template before examining outcome data or estimating treatment effects. For observational studies, a pre-analysis plan does not create randomization or eliminate confounding; it makes the proposed estimand, assumptions, and analytic choices auditable.

## 1. Study identity

- Project title:
- Version and date:
- Authors / roles:
- Data owner and authorization:
- Public registration or repository location:
- Planned analysis freeze date:

## 2. Research question and institutional setting

- Decision or policy question:
- Relevant utility, regulator, RTO/ISO, or federal institution:
- Governing policy/tariff version:
- Treatment applicability clause and legal verification:
- Related interventions or concurrent changes:
- Why the question is important:

## 3. Target population and unit

- Target population:
- Eligibility criteria:
- Unit of assignment:
- Unit of observation:
- Unit of analysis:
- Time period and reporting calendar:
- Clustering or network structure:
- Exclusion criteria and rationale:

## 4. Treatment and assignment mechanism

- Treatment definition:
- Control/comparison definition:
- Assignment mechanism:
- Treatment start and end:
- Application-specific eligibility:
- Noncompliance and crossover:
- Treatment intensity or dose:
- Interference/spillover exposure mapping:

## 5. Estimand

Choose and define the target parameter before selecting the estimator.

- Primary estimand: ATE / ATT / ATU / ITT / LATE / group-time ATT / cumulative incidence contrast / restricted mean time / other.
- Formal notation:
- Target population over which the effect is averaged:
- Outcome scale and units:
- Treatment contrast:
- Follow-up horizon:
- Interpretation in policy terms:

## 6. Outcomes

| Role | Outcome | Definition | Unit | Data source | Time window |
|---|---|---|---|---|---|
| Primary | | | | | |
| Secondary 1 | | | | | |
| Secondary 2 | | | | | |
| Safety / balancing | | | | | |

Do not conflate application submission, completeness, first disposition, approval, agreement, construction, permission to operate, installed capacity, and operating performance.

## 7. Data and measurement

- Source files and URLs:
- Retrieval date:
- File hashes:
- Data dictionary:
- Reporting period:
- Data transformations:
- Missingness:
- Duplicate handling:
- Event-history construction:
- Changes in definitions or source systems:
- Reconciliation checks:
- Disclosure controls:

## 8. Identification strategy

State the identifying assumptions in words and equations.

- Random assignment / conditional independence / parallel trends / exclusion restriction / continuity / synthetic-control assumptions / censoring assumptions:
- Why each assumption is plausible:
- Evidence that could contradict it:
- Confounding variables:
- Mediators and colliders not to be controlled for:
- Positivity/overlap:
- Treatment selection:
- Policy timing:
- Concurrent interventions:
- Interference and spillovers:
- External validity and transportability:

## 9. Primary estimator and inference

- Estimator:
- Regression or mathematical specification:
- Covariate adjustment set and timing:
- Fixed effects:
- Weighting:
- Standard error estimator:
- Clustering level and number of clusters:
- Small-sample corrections:
- Randomization inference or permutation design:
- Confidence level:
- Software, version, and solver:

Do not select an estimator because it produces a preferred sign or significance level. If the identification assumptions do not hold, report that the causal estimand is not identified by the available design.

## 10. Missing data, censoring, and competing events

- Administrative censoring date:
- Time origin:
- Delayed entry / left truncation:
- Right-censoring rule:
- Competing events:
- Withdrawal and denial definitions:
- Informative censoring assessment:
- Missing-outcome strategy:
- Sensitivity analysis:

## 11. Power and sample size

- Expected sample size:
- Number of independent assignment clusters:
- Baseline outcome mean/variance:
- Treatment allocation:
- Minimum detectable effect:
- Alpha and target power:
- Intra-cluster correlation:
- Attrition assumptions:
- Sensitivity to effect heterogeneity:
- Feasibility constraints:

## 12. Robustness and falsification

Pre-specify a limited set of checks, each tied to a threat.

- Alternative outcome/time-origin definitions:
- Alternative comparison groups or bandwidths:
- Pre-trend/event-study diagnostics:
- Placebo outcomes and dates:
- Negative controls:
- Sensitivity to unobserved confounding:
- Alternative weighting or functional forms:
- Alternative censoring/competing-risk assumptions:
- Out-of-sample or stress-test design:
- Multiple-testing adjustment:

## 13. Model and data risk register

| Risk | Expected bias direction | Diagnostic | Mitigation |
|---|---|---|---|
| | | | |
| | | | |
| | | | |

## 14. Deviations and transparency

After the analysis begins, record every deviation from this plan:

| Date | Planned choice | Actual change | Reason | Whether outcome data had been examined |
|---|---|---|---|---|
| | | | | |

Distinguish confirmatory analyses from exploratory analyses. Label any new subgroup, outcome, estimator, or exclusion introduced after examining results as exploratory unless independently justified.

## 15. Reproducibility and disclosure

- Repository commit:
- Environment lockfile:
- Code and tests:
- Data provenance manifest:
- Output-generation command:
- Reproduction instructions:
- Privacy review:
- Confidentiality review:
- Public release restrictions:

## 16. Decision rule

State what result would support, weaken, or invalidate the proposed policy interpretation. Include practical significance and uncertainty, not only a p-value. Identify findings that would cause the research team to withdraw its preferred interpretation.
