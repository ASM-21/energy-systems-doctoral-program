# Curriculum Map and Course Dependencies

This page is the program's navigation map. It distinguishes the current foundation sequence from planned advanced study and optional extensions. Course status describes curriculum design, not the learner's personal completion. Use the [competency framework](competency-framework.md) to see how courses, assessments, and projects map to program outcomes.

## Program structure

| Stage | Main purpose | Expected evidence | Status |
|---|---|---|---|
| Orientation and prerequisites | Identify gaps and establish a reproducible study environment | Diagnostic, environment check, study plan | Active |
| Year 1 foundations | Understand grid physics, energy economics, institutions, and applied quantitative analysis | Four course deliverables and an integrated public-data project | Active |
| Year 2 analytical methods | Develop mathematical maturity, causal identification, optimization, and advanced market analysis | Derivations, tested models, research design, reproducible study | Planned sequence |
| Year 3 policy and strategic systems | Evaluate transition policy, infrastructure strategy, and energy security | Comparative policy or infrastructure study | Roadmap |
| Year 4+ specialization | Produce original research in a focused concentration | Working paper, presentation, reproducibility package | Open-ended |

## Year 1: foundation sequence

The four course guides allow approximately 140–182 hours combined. The assessment tracker uses a 168-hour planning baseline, plus 25 hours for the Year 1 integration project. At 3–5 hours per week, the current planning calendar is approximately 38–66 weeks including the project. The [Year 1 study plan](../progress/year-1-study-plan.md) reconciles each course estimate and explains the range. The integration project should reuse course methods and evidence rather than become an unrelated fifth course.

| Course | Prerequisites | Planned effort | Main output | Role in sequence |
|---|---|---:|---|---|
| [Y1-01 Power Systems](../courses/year-1/y1-01-power-systems/README.md) | Calculus, linear algebra, ODE basics, circuits, probability, programming | 42 h (35–45 h range) | Small network/feeder model and technical report | Establishes physical and engineering foundations |
| [Y1-02 Energy Economics](../courses/year-1/y1-02-energy-economics/README.md) | Intermediate microeconomics, calculus, basic statistics | 35 h (30–40 h range) | Dispatch, welfare, or tariff analysis | Connects physical constraints to incentives and costs |
| [Y1-04 Quantitative Methods](../courses/year-1/y1-04-quantitative-methods/README.md) | Calculus, linear algebra, probability/statistics, Python or R | 40 h (35–45 h range) | Reproducible descriptive or OLS analysis | Can overlap with Y1-01/Y1-02 after basic data setup |
| [Y1-03 Markets, Regulation, and PJM](../courses/year-1/y1-03-markets-regulation-pjm/README.md) | Y1-02 or equivalent; basic electricity-system literacy | 51 h (40–52 h range) | Source-supported regulatory and market analysis | Applies engineering and economics to real institutions |

**Recommended order:** Y1-01, then Y1-02; begin Y1-04 once the data/programming prerequisites are comfortable; complete Y1-03 after the basic engineering and economic concepts are established. Limited overlap is acceptable. Do not run all four at full intensity simultaneously.

### Year 1 integration gate

Before treating Year 1 as complete, demonstrate that you can:

- Represent a simplified power system and explain the assumptions behind its network model.
- Explain dispatch, marginal cost, welfare, and key electricity-market characteristics.
- Distinguish the roles of FERC, state commissions, utilities, and PJM using primary sources.
- Acquire and audit public data, produce reproducible analysis, and communicate uncertainty.
- Define a narrow research question and explain what evidence would and would not identify its answer.

The integration project should produce a literature/institutional review, a transparent dataset or model, an analysis, a policy or technical brief, and a reproducibility package. The [Year 1 guide](../courses/year-1/README.md) contains the project specification.

## Year 2: advanced analytical methods

Year 2 is a flexible advanced-study stage rather than a fixed 12-month calendar. The four planned courses represent approximately 195–250 hours before a research capstone, or roughly 9–19 months at 3–5 hours per week. A 25–40 hour research synthesis extends the full stage to approximately 10–22 months. The [Year 2 guide](../courses/year-2/README.md) is the operational sequencing reference.

| ID | Course | Dependencies | Planned effort | Status |
|---|---|---|---:|---|
| Y2-01 | [Advanced Mathematical Methods](../courses/year-2/advanced-mathematics-energy-systems/README.md) | Year 1 math foundations; prerequisite diagnostic | 60–75 h | Planned |
| Y2-02 | [Graduate Econometrics and Causal Inference](../courses/year-2/graduate-econometrics-causal-inference/README.md) | Y1-04 regression, probability, Python/R | 60–75 h | Planned |
| Y2-03 | [Infrastructure Economics and Utility Investment](../courses/year-2/infrastructure-economics-utility-investment/README.md) | Y1-02 economics, Y1-03 regulation, introductory finance | 30–40 h | Planned; initial guide and PS1 available |
| Y2-04 | [Electricity Market Design and Optimization](../courses/year-2/electricity-market-design-optimization/README.md) | Y1-01/Y1-02/Y1-03 and relevant Y2-01 optimization modules | 45–60 h | Roadmap; assessments not yet published |

**Recommended order:** meet the Year 1 progression gate; begin Y2-01 mathematics; then choose Y2-02 econometrics or Y2-04 market design as the primary methods branch. Add Y2-03 when the research question requires utility finance, rate design, or investment incentives. At most one course should be the primary weekly workload. Do not stack two nominal 2–3 hour courses inside the total 3–5 hour program budget.

The queueing theory assignment in Y2-01 is an optional extension, not a prerequisite for the core sequence. Planned effort estimates will be reconciled to the assessment tracker as the remaining course materials are developed.

## Cross-course dependency logic

- Power-flow and distribution analysis depend on circuit concepts, complex numbers, linear algebra, and numerical methods.
- Dispatch and market-clearing models depend on microeconomics, constrained optimization, and the physical limits of electricity.
- Causal policy evaluation depends on statistical foundations, institutional knowledge, treatment/measurement definitions, and a defensible assignment mechanism.
- Spatial and network-interference analysis additionally depends on graph representation and engineering knowledge of the relevant exposure pathways.
- Infrastructure investment analysis depends on engineering feasibility, cost modeling, utility regulation, finance, and uncertainty analysis.

## Specialization pathways

Choose one primary concentration after the foundations, then use a complementary field to avoid a narrow toolkit.

| Primary concentration | Complementary field | Candidate research questions |
|---|---|---|
| Distribution planning and DER interconnection | Causal inference / utility regulation | How do queue rules, hosting constraints, and flexible interconnection affect project outcomes? |
| Utility regulation and investment incentives | Infrastructure economics / econometrics | How do rate design and cost recovery shape distribution investment? |
| Wholesale market design and resource adequacy | Optimization / power systems | How do capacity accreditation, scarcity pricing, and transmission constraints interact? |
| Decarbonization and system planning | Climate economics / stochastic optimization | How do reliability, emissions, and cost trade off under uncertainty? |
| Energy security and industrial competitiveness | Supply-chain economics / public policy | How do critical infrastructure and industrial policies affect resilience and investment? |

Specialization should follow a feasibility review. Do not select a topic solely because a dataset or model is available; establish the decision relevance, literature gap, and measurement limits first.

## Status definitions

- **Active:** structured materials are available for current study.
- **Planned:** course architecture exists, but it is not yet a fully developed or validated course.
- **Roadmap:** intended future area with scope still to be developed.
- **Optional:** useful extension that is not required to complete the main sequence.

See [How to Use the Program](learning-guide.md) for study workflow and completion rules.
