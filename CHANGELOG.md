# Changelog

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
