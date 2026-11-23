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

The four courses are designed to fit approximately 168 hours in total, before any optional extensions. At 3–5 hours per week, distribute them over the year and adjust the calendar to the actual workload. The integration project should use the same topic and evidence base as course work where practical, rather than creating an unrelated fifth course.

| Course | Prerequisites | Planned effort | Main output | Role in sequence |
|---|---|---:|---|---|
| [Y1-01 Power Systems](../courses/year-1/y1-01-power-systems/README.md) | Calculus, linear algebra, ODE basics, circuits, probability, programming | 35–45 h | Small network/feeder model and technical report | Establishes physical and engineering foundations |
| [Y1-02 Energy Economics](../courses/year-1/y1-02-energy-economics/README.md) | Intermediate microeconomics, calculus, basic statistics | 30–40 h | Dispatch, welfare, or tariff analysis | Connects physical constraints to incentives and costs |
| [Y1-04 Quantitative Methods](../courses/year-1/y1-04-quantitative-methods/README.md) | Calculus, linear algebra, probability/statistics, Python or R | 35–45 h | Reproducible descriptive or OLS analysis | Can overlap with Y1-01/Y1-02 after basic data setup |
| [Y1-03 Markets, Regulation, and PJM](../courses/year-1/y1-03-markets-regulation-pjm/README.md) | Y1-02 or equivalent; basic electricity-system literacy | 40–52 h | Source-supported regulatory and market analysis | Applies engineering and economics to real institutions |

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

Year 2 is deliberately modular. The target remains 3–5 hours per week for the entire program, not per course.

| Course or module | Dependencies | Role | Status |
|---|---|---|---|
| [Advanced Mathematical Methods](../courses/year-2/advanced-mathematics-energy-systems/README.md) | Year 1 math foundations; prerequisite diagnostic | Proof, matrix analysis, probability, dynamics, convexity, duality, numerical methods, graph theory | Planned |
| [Graduate Econometrics and Causal Inference](../courses/year-2/graduate-econometrics-causal-inference/README.md) | Y1-04, regression, probability, Python/R | Identification, panel data, experiments, IV/RD, synthetic control, time series, interference | Planned |
| Electricity Market Design and Optimization | Power systems and energy economics; linear algebra and optimization | OPF, unit commitment, reserves, market power, equilibrium, transmission | Planned |
| [Infrastructure Economics and Utility Investment](../courses/year-2/infrastructure-economics-utility-investment/README.md) | Energy economics and regulatory foundations | Rate base, cost of capital, revenue requirements, incentives, risk allocation | Planned |

**Recommended order:** complete a targeted mathematics diagnostic; strengthen linear algebra, calculus, probability, and optimization; then study econometrics and market design in a staggered sequence. The queueing theory module is an optional extension, not a prerequisite for the core sequence.

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
