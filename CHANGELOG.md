# Changelog

## 2026-11-22 — Staggered-adoption DID computational lab
- Added a transparent 2×2 DID contrast and cohort-time ATT estimator using never-treated controls and cohort-specific pre-treatment baselines.
- Added a synthetic staggered-adoption panel with heterogeneous effects, unit tests, and explicit limitations on balance, controls, inference, and parallel trends.
- Integrated the lab into Makefile, CI, project index, and graduate econometrics course.


## 2026-11-22 — Panel data and difference-in-differences assessment
- Added Problem Set 3 and worked solutions on 2×2 DID, parallel-trends violations, event-study specifications, staggered adoption, heterogeneous effects, TWFE weighting, and small-cluster inference.
- Applied the design critique to Pennsylvania's 2023–2025 pre-policy aggregate panel and documented why it cannot estimate a 2026 treatment effect.


## 2026-11-22 — Energy policy pre-analysis plan template
- Added a pre-analysis plan template covering estimands, assignment, treatment timing, outcomes, identification, inference, censoring, power, robustness, model risk, and deviations.
- Linked the template to the graduate econometrics course to reinforce design-first empirical practice.


## 2026-11-22 — Randomized experiment reproducibility outputs
- Documented fixed-seed synthetic example outputs for the randomized experiments lab so users can verify the CLI run without treating the simulation as empirical evidence.


## 2026-11-22 — Randomized experiments computational lab
- Added a standard-library implementation of complete randomization, difference-in-means ITT, Neyman standard errors, Monte Carlo Fisher randomization inference, MDE, and cluster design effects.
- Added deterministic unit tests and a synthetic smoke example; explicitly documented the sharp-null, assignment-mechanism, and cluster-design limitations.
- Integrated the lab into Makefile, CI, project index, and graduate econometrics course.


## 2026-11-22 — Randomized experiments and power assessment
- Added Problem Set 2 and worked solutions covering ITT, Neyman standard errors, regression adjustment, treatment-effect heterogeneity, randomized encouragement/LATE, MDE and power, cluster design effects, interference, and pre-analysis plans.
- Integrated the assignment into the graduate econometrics course and site navigation.


## 2026-11-22 — Year 2 program integration
- Integrated graduate econometrics and causal research design into the Year 2 roadmap and program learning outcomes.


## 2026-11-22 — Causal inference literature expansion
- Added potential-outcomes, target-trial, staggered difference-in-differences, event-study, regression-discontinuity, and synthetic-control references to the Year 2 core reading list.
- Linked the expanded reading list to the graduate econometrics course.


## 2026-11-22 — Graduate econometrics and causal inference course
- Added a Year 2 graduate course spanning potential outcomes, randomized experiments, panel methods, difference-in-differences, IV, RD, synthetic controls, survival analysis, time series, and interference.
- Added Problem Set 1 and worked solutions on estimands, selection bias, conditional independence, DAGs, randomized encouragement, and feeder-level interference.
- Connected the course to the Pennsylvania DER interconnection capstone and competing-risks methods lab.


## 2026-11-22 — Advanced mathematics pacing plan
- Added a 24–30 week paced schedule for Problem Sets 1–9, capstone implementation, validation, and defense.
- Explicitly preserves the 2–3 hour weekly target within the overall 3–5 hour program budget; extensions shift later blocks rather than increasing weekly load.


## 2026-11-22 — Competing-risks estimator validation
- Extended the survival methods lab with deterministic exponential competing-risk cohort simulation, closed-form cause-specific cumulative incidence, and step-curve evaluation.
- Added a 20,000-record seeded Monte Carlo test that checks Aalen-Johansen and Kaplan-Meier net-risk estimates against their respective analytic targets.
- Added validation for simulation inputs and retained the explicit distinction between observed cumulative incidence and hypothetical net approval risk.


## 2026-11-22 — Competing-risks literature integration
- Added foundational Aalen-Johansen, Putter-Fiocco-Geskus, Fine-Gray, and Gray references to the methods lab and core reading list.
- Distinguished the nonparametric estimator implemented in the lab from regression methods that remain outside its scope.


## 2026-11-22 — Capstone measurement and model-risk controls
- Added a field-level data dictionary documenting units, source table provenance, comparability breaks, missingness, and prohibited inferences for the 33-row PA EDC panel.
- Added a ten-item model-risk register covering engineering approximation, policy exposure, project selection, censoring, correlated uncertainty, input validity, and synthetic parameter misuse.


## 2026-11-22 — Capstone publication and defense templates
- Added structured templates for the 6,000–8,000 word research paper, two-page policy brief, oral defense, and reproducibility checklist.
- Added an evidence classification framework to prevent descriptive results, provisional interpretation, and proposed recommendations from being conflated.


## 2026-11-22 — Application-level interconnection evaluation protocol
- Added a relational event-history data specification for DER applications, review episodes, policy regimes, feeder snapshots, and network upgrades.
- Defined outcomes, time origins, censoring, competing events, target-trial elements, causal structure, statistical method selection, and privacy/data-quality safeguards.
- Explicitly separated tariff applicability, tariff document effective dates, and DER Management Program implementation milestones.
- Linked the protocol to the Pennsylvania casebook, capstone, and published research navigation.


## 2026-11-22 — Competing-risks survival methods lab
- Added standard-library Kaplan-Meier net-approval and Aalen-Johansen cause-specific cumulative-incidence estimators for a synthetic interconnection cohort.
- Added tests for tied events, right censoring, competing risks, probability-mass conservation, and the difference between net risk and observed cumulative incidence.
- Linked the methods lab to the Pennsylvania interconnection capstone and integrated it into Makefile, CI, and MkDocs navigation.


## 2026-11-22 — Integrated doctoral research design capstone
- Added Problem Set 9 and a detailed assessment guide integrating empirical data validation, causal identification, distribution network equations, two-stage stochastic and robust investment, dual interpretation, numerical verification, and regulatory institutions.
- Connected the assessment to the public Pennsylvania EDC interconnection capstone and documented a strict rubric that rejects unsupported causal claims or invalid physical formulations.
- Integrated the capstone into the advanced mathematics course, Year 2 evidence plan, and MkDocs navigation.


## 2026-11-22 — Pennsylvania distribution interconnection research capstone
- Added a reproducible 11-EDC, 2023–2025 PUC request-count analysis using the existing casebook source dataset without duplicating the raw data.
- Added balanced-panel and statewide reconciliation checks, PPL peer rank/share, request-count concentration, top-three share, year-over-year changes, and the 2025 >=500 kW review-level composition.
- Added explicit measurement and identification limits: request counts are not outcomes or rates; the request-count HHI is not market power; aggregate annual data do not identify causal effects.
- Added tests, a standalone CLI, Makefile and CI integration, and the published project index.


## 2026-11-22 — Stochastic and robust capacity-planning lab
- Added SciPy/HiGHS linear-programming formulations for two-stage stochastic capacity procurement, deterministic expected-value benchmarking, wait-and-see information value, and min-max robust capacity planning.
- Added unit tests for the 80 MW stochastic optimum, 104 MW expected-value decision, 120 MW robust decision, $312 value of the stochastic solution, and $600 expected value of perfect information.
- Integrated the lab into the project index, Year 2 computational companions, Makefile, Python CI matrix, and MkDocs navigation. All parameters and outputs are explicitly synthetic.


## 2026-11-22 — Stochastic and robust optimization assessment
- Added Problem Set 8 and worked solutions on two-stage stochastic capacity planning, expected-value and wait-and-see comparisons, VSS/EVPI, budgeted uncertainty, chance constraints, CVaR, and nonanticipativity.
- Added SIAM references for stochastic programming and robust optimization to the course and core reading list.
- Integrated the assignment into the advanced mathematics course sequence and MkDocs navigation.


## 2026-11-22 — Graph theory and network-flow resilience
- Added Problem Set 7 and worked solutions on incidence matrices, cycle spaces, graph Laplacians, maximum flow/minimum cut, connectivity, contingencies, and the limits of graph-based power-system screening.
- Added a standard-library Edmonds-Karp lab with arc-flow outputs, residual-reachable minimum-cut certificates, contingency experiments, and unit tests.
- Integrated the assignment and lab into the Year 2 course guide, project index, Makefile, Python CI matrix, and MkDocs navigation.
- Explicitly separated structural connectivity and abstract transfer bounds from AC/DC electrical feasibility and operational N-1 security.


## 2026-11-22 — Numerical optimization assessment
- Added a sixth advanced-mathematics problem set with worked solutions on gradient descent, strong convexity, Newton updates, Armijo line search, scaling and preconditioning, least-squares conditioning, and solver diagnostics.
- Integrated the assignment into the Year 2 course sequence and MkDocs navigation. Emphasis is on deriving convergence conditions and distinguishing solver termination from optimality and model validity.


## 2026-11-22 — Stochastic adequacy simulation lab
- Added a standard-library-only Monte Carlo resource-adequacy screening model with persistent two-state weather regimes and a repairable generation outage block.
- Added deterministic seeded simulation, annual LOLE/EUE distributions, cross-year sampling-error summaries, parameter validation, and unit tests.
- Connected the lab to the probability/stochastic-processes assignment, project index, MkDocs navigation, Makefile, and Python CI matrix.
- Documented that the model is synthetic and omits weather-load dependence, spatial correlation, transmission, storage, demand response, and common-cause failures; its outputs are not PJM or utility reliability metrics.


## 2026-11-22 — Probability and stochastic-process foundations
- Added a fifth advanced-mathematics problem set and worked solutions covering covariance in net-load uncertainty, conditional probability, Poisson outage arrivals, Markov weather regimes, chance-constrained reserve sizing, and Monte Carlo precision.
- Added the assignment to the Year 2 course sequence and published navigation.
- Emphasized model-risk distinctions: stochastic sampling error is not model validity, a one-hour chance constraint is not a system-wide adequacy guarantee, and event counts do not alone measure customer reliability.


## 2026-11-21 — Planned advanced mathematics sequence
- Added a reproducible frequency-response state-space lab with eigenvalue calculations, analytical steady-state response, RK4 integration, explicit-Euler stability bounds, and unit tests; added it to the CI test matrix and research project index. The model uses synthetic normalized inputs and explicitly disclaims operational-security use.
- Added four assessed advanced-mathematics problem sets with worked solutions: matrix analysis and network structure; multivariable calculus and local models; constrained optimization, KKT conditions and electricity-market duality; and differential equations, state-space dynamics and numerical stability.
- Added mathematical derivations that connect abstract results to three-bus network equations, nonlinear model linearization, economic dispatch shadow prices, storage dynamics, and frequency-response stability. Corrected and checked the Taylor approximation numerical comparison in the calculus solutions.

- Added a dedicated Year 2 course in Advanced Mathematical Methods for Energy Systems and Infrastructure Research, explicitly marked as planned rather than part of the current Year 1 workload.
- Specified a two-semester modular sequence covering proof techniques, matrix analysis, multivariable calculus, real-analysis foundations, differential equations, dynamical systems, probability and stochastic processes, convex analysis, KKT conditions, duality, numerical optimization, graph theory, and stochastic/robust optimization.
- Connected every mathematical block to energy-system applications including power flow, OPF, dispatch, storage, reliability, DER planning, congestion, and infrastructure investment.
- Added prerequisite diagnostics, assessment standards, capstone directions, and graduate-level references including MIT OpenCourseWare benchmarks.
- Integrated the course into the Year 2 roadmap, quantitative-methods department, prerequisites, reading list, and site navigation without increasing the planned 3–5 hour/week workload.


## 2026-11-21 — Pennsylvania interconnection outcomes and respondent-frame audit

- Validated the corrected EIA-861 Pennsylvania extraction: 249 utility-year rows, 33 EIA IDs, zero duplicate year/ID keys, zero invalid rows, and 17 IDs observed in all 11 years; TPO worksheets and adjustment rows are explicitly excluded and logged.
- Added annual EIA respondent-frame linkage for 2016–2025 to capture short-form status, ownership, and net-metering schedule participation, with unmatched/duplicate IDs retained as audit findings.
- Resolved the major FirstEnergy EIA respondent discontinuity against its 2023 Form 10-K: Pennsylvania operating companies consolidated into FE PA effective 2024-01-01. Documented why EIA respondent IDs and legacy PUC service-territory series must not be treated as a one-to-one panel.
- Added the Pennsylvania PUC 2023–2025 Net-Metering and Interconnection Report as the primary public interconnection-outcome source, including structured request counts for all 11 EDC service territories and detailed PPL metrics.
- Added reproducible peer-ranking and PPL descriptive scripts with unit tests; all EDC review-level counts reconcile to published statewide totals and PPL ranks first in request volume in all three reporting years.
- Flagged the PPL 2025 status-table discrepancy: status categories are 357 below submitted requests, and the reported Completed field includes pending-EDC cases. CI tests ensure this issue is exposed rather than silently normalized.
- Added a Y1-03 empirical problem set and worked solutions on PUC interconnection outcomes, stock/flow distinctions, review-level counts, status reconciliation, policy timing, and causal-identification requirements.
- Identified and documented conflicting Level 3 capacity thresholds in the PUC report and 52 Pa. Code §§ 75.34(3) and 75.39(a); added the relevant code sections to the primary-source register and the assignment.
- Revised the public-data research design: PUC EDC service territories are the preferred unit for interconnection-process analysis; EIA-861 is complementary for cumulative utility-level adoption and other indicators.

## 2026-11-21 — EIA-861 schedule population correction

- Inspected the first Pennsylvania peer-panel artifact and found that TPO schedules and administrative adjustment rows were being counted alongside EDC utility respondents.
- Tightened extraction to exclude TPO worksheets and adjustment rows (including EIA ID 99999), while recording exclusions in the annual manifests.
- Expanded unit tests to cover duplicate TPO representations and administrative adjustment rows. The Pennsylvania peer panel remains a raw coverage audit until utility IDs, service territories, form status, and annual field definitions are reconciled.


## 2026-11-21 — PJM capacity-market source refresh

- Added Peter Cramton's 2017 electricity-market-design article to the core reading list.
- Verified the current PJM capacity/resource-adequacy manual sequence: Manual 18 Rev. 63 (effective 2026-09-24), Manual 20A Rev. 3 (effective 2026-06-24), and Manual 21B Rev. 06 (effective 2026-11-18).
- Explicitly marked Manuals 20 and 21A as retired in the curriculum's source guidance and updated Y1-03 Problem Set 5 to require current, revision-specific citations.


## 2026-11-21 — Pennsylvania EIA-861 peer-panel audit

- Added a raw utility-year coverage and respondent-identity audit for Pennsylvania EIA-861 net-metering rows.
- The audit reports annual utility-ID coverage, missing years, duplicate year/utility keys, respondent-name variants, and invalid/out-of-range records.
- Integrated the audit into the historical EIA-861 workflow and artifact bundle; added unit tests and documented that the output is not a harmonized panel or causal dataset.


## 2026-11-21 — Advanced electricity-market design

- Added a graduate-level Y1-03 problem set on scarcity pricing, energy and operating-reserve co-optimization, planning reserve margins, capacity procurement, resource accreditation, and reliability/market-design trade-offs.
- Added a worked numerical solution for merit-order dispatch, reserve shortfall scenarios, capacity procurement arithmetic, and the co-optimization LP, including primal and dual interpretation checks.
- Added primary-source guidance requiring delivery-year-specific PJM manuals, auction results, and FERC-approved rules rather than stale market parameters.

## 2026-11-20 — Distribution engineering and Pennsylvania research expansion

- Added a radial distribution feeder DER hosting-capacity screening lab with synthetic inputs, first-order voltage calculations, branch thermal screening, reverse-flow flags, scenario sweeps, and regression tests.
- Added a reproducible IEEE 13-node OpenDSS benchmark runner using DSS-Python, with baseline and PV cases, node-level voltage exports, loss summaries, and a dedicated GitHub Actions workflow. The IEEE benchmark is explicitly distinguished from validation of the synthetic feeder.
- Added node-aligned scenario comparison, regression tests, and a verified baseline/500 kW result table. The baseline already exceeds a simple 1.05 pu maximum-voltage screen, so the coursework explicitly separates pre-existing operating conditions from incremental DER effects.
- Added a six-point PV penetration sweep (0–1,000 kW), baseline-aware voltage-screen interpretation, CSV exports, and CI execution.
- Added an applied IEEE 13-node benchmark assignment and solution guide to Y1-01, with voltage and load sensitivity experiments and explicit model-comparison requirements.
- Added an applied radial-feeder DER problem set and worked solution notes to Y1-01.
- Extended economic dispatch with carbon pricing and flexible-demand optimization, including cost/emissions decomposition and automated tests.
- Added a carbon-pricing and demand-response problem set with worked solution notes to Y1-02.
- Added a non-exporting behind-the-meter storage optimization lab with PV curtailment, grid-import no-export constraint, cyclic state of charge, throughput degradation cost, synthetic time-series inputs, and unit tests.
- Added a Y1-02 assignment and solution notes that connect the BTM storage model to the Pennsylvania interconnection policy casebook.
- Expanded continuous integration to test and smoke-run six computational projects.
- Added a Pennsylvania public-data feasibility memo separating what can be observed from what remains unavailable or requires docket-level retrieval.
- Updated the Pennsylvania DER casebook with the December 3, 2025 Commission-order milestone and the distinction between a proposed hosting-capacity increase and independently measured feeder headroom.
- Added analysis of Pennsylvania's proposed Chapter 57 DER aggregation rules, current IRRC status, and a Y1-03 problem set with worked solutions. The materials explicitly distinguish proposed wholesale aggregation rules from distribution interconnection requirements.
- Added current Pennsylvania hosting-capacity legislative context and refreshed PJM / PPL source verification.

## 2026-11-20 — Year 1 curriculum and research infrastructure expansion

- Added Problem Sets 1 and 2 with worked solution notes to all four Year 1 courses.
- Added a three-bus DC power-flow lab with a per-unit network model, slack-bus solution, branch-flow checks, and automated tests.
- Added a battery arbitrage optimization lab with intertemporal state-of-charge constraints, efficiency, and degradation-cost scenarios.
- Added a two-node congestion dispatch lab with nodal-price duals and automated tests.
- Added a reproducible OLS / HC3 inference lab with deterministic synthetic data, data dictionary, and tests.
- Expanded CI to test all computational labs and run smoke tests.
- Added a core reading list with publisher/journal verification.
- Added literature-review, research-protocol, and dataset-intake templates.
- Added a Pennsylvania distribution DER interconnection / PJM wholesale aggregation casebook based on public tariff, FERC, and PJM sources, including a versioned source register and institutional responsibility matrix.
- Added a Year 1 study plan and granular assessment tracker.
- Corrected arithmetic and model-formulation issues identified during review.
- Strict MkDocs build and GitHub Pages deployment both succeeded in GitHub Actions; published site URL: https://asm-21.github.io/energy-systems-doctoral-program/.
