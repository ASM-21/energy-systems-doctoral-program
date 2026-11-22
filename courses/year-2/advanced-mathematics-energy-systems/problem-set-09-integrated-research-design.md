# Problem Set 9: Integrated Energy Infrastructure Research Design

**Level:** Advanced graduate / doctoral synthesis  
**Suggested effort:** 4–6 hours, staged across multiple weeks  
**Prerequisites:** Problem Sets 1–8 and introductory econometrics  
**Case:** Pennsylvania distribution DER interconnection, public PUC data, and a prospective utility-planning decision

## Purpose

This is the synthesis assessment for the advanced mathematical sequence. It requires the learner to connect graph theory, constrained optimization, uncertainty, numerical analysis, empirical measurement, institutional design, and economic interpretation.

Use the Pennsylvania PUC 2023–2025 EDC interconnection dataset in the repository casebook. The dataset contains aggregate request counts for 11 EDC service territories over three PUC reporting years. The reporting year runs June 1 through May 31. It is not an application-level cohort dataset.

The assignment is deliberately designed around what the data can and cannot support. A technically sophisticated answer that makes an invalid causal claim does not pass.

## Part A. Data audit and descriptive estimands

1. Verify the panel dimensions, unique EDC-year keys, review-level totals, and statewide reconciliation for each year.
2. Calculate for each reporting year:
   - statewide requests;
   - PPL request count, rank, and statewide request share;
   - top-three EDC request share;
   - HHI of EDC request-count shares, using the conventional 0–10,000 arithmetic but explicitly labeling it as an application-count concentration statistic.
3. Calculate the PPL year-over-year request-count changes and the 2023–2025 percentage change.
4. Explain why the HHI is not a retail-market concentration measure and why request counts should not be interpreted as utility performance without exposure denominators and application outcomes.
5. Identify at least five data fields that would be required to calculate a defensible time-to-decision measure.

## Part B. Identification and econometric design

A policy change becomes applicable to a subset of new DER applications in January 2026. The available detailed EDC panel ends May 31, 2025.

1. State whether the existing panel identifies a treatment effect. Explain using treatment timing, observation window, unit of analysis, and available outcomes.
2. Define a plausible estimand for a future evaluation. Examples include the change in restricted mean time to permission-to-operate for eligible applications, or the change in probability of withdrawal within a fixed follow-up window.
3. Design an application-level survival-analysis dataset. Specify the event, time origin, censoring rule, competing events, treatment assignment, covariates, and clustering structure.
4. Explain when a difference-in-differences design could be defensible and list the evidence needed for parallel trends, treatment timing, comparison-group validity, and absence of confounding concurrent changes.
5. Explain why 33 aggregate observations do not support a credible high-dimensional fixed-effects causal model merely because software can estimate one.

## Part C. Network model and physical constraints

Consider a radial three-bus feeder with substation bus 0, intermediate bus 1, and terminal bus 2. Use a linearized distribution-flow approximation for screening.

1. Define an oriented graph, incidence matrix, nodal injections, and branch-flow vector. State your sign convention.
2. Write the nodal balance equations and explain the role of the reduced incidence matrix.
3. Write linearized voltage-drop equations in terms of branch resistance, reactance, active and reactive flow. State the assumptions that make the approximation useful and the conditions under which it can fail.
4. Formulate branch thermal limits, voltage bounds, DER active-power availability, curtailment, and non-export constraints where relevant.
5. Explain why a max-flow solution is not an electrical feasibility certificate and why a first-order voltage screen is not a substitute for an unbalanced AC power-flow study.

## Part D. Investment under uncertain DER adoption

Suppose the utility can reinforce one or both branches before DER adoption is realized. Let (x_ell) denote a first-stage reinforcement decision for branch (ell). Let scenario (s) describe a joint realization of DER output, load, and equipment availability. Let (c_{i,s}) denote DER curtailment and (v_{i,s}) voltage deviation or violation slack where permitted by the formulation.

1. Formulate a two-stage stochastic planning model with one first-stage reinforcement decision shared across scenarios and scenario-specific operational recourse.
2. Include capital cost, operating cost, curtailment penalty, and any explicitly justified reliability penalty. Do not treat a penalty coefficient as an observed customer damage value unless evidence supports it.
3. Write at least one branch-capacity constraint and one voltage constraint for each scenario. Explain how reinforcement changes the feasible set.
4. State the nonanticipativity conditions and explain the perfect-foresight error that would arise if first-stage decisions differed by scenario.
5. Construct a robust alternative using a budgeted uncertainty set. Compare its conservatism with a stochastic formulation using calibrated scenario probabilities.
6. Identify the dual variables that would be economically informative, including the marginal value of branch capacity and voltage headroom. Explain why duals at a binding artificial slack penalty are not automatically a market price or regulated cost.

## Part E. Numerical verification and model risk

1. Propose at least six unit or property tests for the network and optimization model.
2. Specify solver diagnostics: termination status, primal feasibility residuals, dual feasibility, integrality gap if applicable, and sensitivity to scaling/tolerances.
3. Define out-of-sample or stress-scenario validation. Explain how to prevent tuning the model and evaluating it on the same scenarios.
4. Separate parameter uncertainty, stochastic uncertainty, and structural model uncertainty.
5. Provide a model-risk register with at least five failure modes, their possible direction of bias, and a mitigation or validation step.

## Part F. Institutional and economic interpretation

Create a process map separating:

- physical distribution interconnection and utility study;
- state tariff and PUC oversight;
- DER management / distribution operating envelopes;
- wholesale aggregation participation under PJM/FERC rules;
- customer adoption and project economics.

Explain where the state, utility, PJM, and FERC have distinct responsibilities. Identify which conclusions are supported by the PUC dataset, which require utility or application-level data, and which require tariff/order interpretation.

## Part G. Final research package

Produce the following:

1. A 6,000–8,000 word paper or equivalent technical report.
2. A 2-page policy brief with evidence strength labeled for every recommendation.
3. Reproducible code, tests, environment specification, and machine-readable outputs.
4. A data provenance manifest with source URL, access date, file hash, reporting period, transformations, and exclusions.
5. A mathematical appendix deriving the network constraints and stochastic/robust formulation.
6. A 10-minute presentation and a 15-minute oral defense.

## Evaluation rubric

| Dimension | Weight | Passing evidence |
|---|---:|---|
| Data integrity and measurement | 15% | Reconciled panel, transparent units, no fabricated denominators |
| Empirical identification | 15% | Explicit estimand and honest treatment of identification limits |
| Network formulation | 15% | Correct signs, balances, voltage/thermal constraints, stated approximations |
| Optimization and uncertainty | 20% | Correct recourse, nonanticipativity, robust/stochastic comparison, dual interpretation |
| Numerical verification | 15% | Tests, residuals, solver diagnostics, out-of-sample checks |
| Institutional/economic interpretation | 10% | Accurate division of physical, regulatory, and wholesale-market roles |
| Communication and reproducibility | 10% | Reproducible package, defensible claims, clear technical/policy translation |

A score below 70% in data integrity, empirical identification, or network formulation is a capstone failure regardless of the total score. A correct optimizer output cannot compensate for an invalid dataset or an invalid physical model.

## Submission rule

Use only public data. Do not use employer-confidential processes, internal system models, customer information, or nonpublic project records. Treat the casebook's existing descriptive analysis as a starting point to audit, not as an answer to reproduce uncritically.
