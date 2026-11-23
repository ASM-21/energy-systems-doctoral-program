# Computational Project Template

Use this template for substantial computational projects. Keep sections that apply and mark genuinely inapplicable sections as "Not applicable" with a reason. Do not fill space with generic claims. A short, precise project page is preferable to a long page that obscures the model.

## Project identity

- **Project ID:** [stable identifier]
- **Type:** [power systems / energy economics / econometrics / data engineering / policy analysis]
- **Status:** [planned / in development / reproducible baseline / reviewed]
- **Course mapping:** [course and assignment, or independent research]
- **Level and expected effort:** [graduate level; estimated hours]
- **Last verified:** [YYYY-MM-DD]

## Research or engineering question

State one answerable question. Identify the decision, mechanism, or quantity the model is intended to illuminate. Separate the motivating real-world issue from what this implementation actually estimates or computes.

## Learning objectives and prerequisites

List observable skills the learner should demonstrate. Name required concepts, software, and earlier course material. Link to the relevant course page and prerequisite assignment.

## Scope and system boundary

Define the unit of analysis, time and spatial resolution, decision horizon, included actors/assets, and excluded processes. State whether this is a synthetic teaching model, a public-data analysis, or a calibrated empirical model. Do not imply calibration or operational validity without evidence.

## Data and provenance

For every input, record its source, version/date, retrieval date, license or use constraints, units, transformations, and missing-value treatment. For synthetic inputs, state the data-generating assumptions and random seed. Keep raw inputs immutable where possible and write derived outputs to a separate directory. Never include confidential employer, customer, or system data.

## Model specification

Present the mathematical or computational formulation, variable definitions, objective/estimand, constraints, and key assumptions. Explain sign conventions and units. For empirical work, state the estimand, comparison group, identification assumptions, and inference procedure. For simulation, state the event logic, stochastic distributions, and replication design.

## Implementation and reproducibility

List dependencies and supported runtime versions. Give commands that work from a clean checkout, including installation, execution, and tests. Identify generated outputs and distinguish source files from generated artifacts.

## Validation and benchmark

Provide at least one independently checkable benchmark: analytical solution, conservation/balance identity, known limiting case, external reference case, or test fixture. Report tolerances and numerical conventions. Tests should cover invalid inputs and edge cases, not only the default example. For empirical analysis, include schema checks, reconciliation, sensitivity analysis, and falsification or placebo diagnostics appropriate to the design.

## Results and interpretation

Report the default result with units and enough context to reproduce it. Explain what changes under sensitivity analysis. Distinguish a model output from an observed fact, a descriptive association from a causal effect, and a local shadow value from a general market price.

## Limitations and non-goals

List material omitted mechanisms, assumptions that may fail, data limitations, and conclusions the project cannot support. Identify the evidence required before using the model for a real planning, regulatory, investment, or operational decision.

## Extensions and research questions

Prioritize extensions by the uncertainty or limitation they address. Avoid feature lists that do not connect to a research question.

## Course assessment mapping

Identify the problem set, learning outcome, or capstone deliverable this project supports. State what evidence a learner should submit: code, tests, derivation, figures, technical note, or oral defense.

## Reproducibility checklist

- [ ] Inputs and provenance are documented.
- [ ] Environment and run commands are tested from a clean checkout.
- [ ] Core calculations have automated tests.
- [ ] At least one independent benchmark or validation is reported.
- [ ] Units, sign conventions, and assumptions are explicit.
- [ ] Generated outputs are distinguishable from source data.
- [ ] Limitations and prohibited inferences are explicit.
- [ ] Course mapping and learner deliverables are identified.
