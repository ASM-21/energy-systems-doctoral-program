# Y1-01 — Power Systems and Electricity Infrastructure

**Status:** Active Year 1 course  
**Level:** Graduate foundation / early doctoral preparation  
**Prerequisites:** Calculus, linear algebra, introductory differential equations, basic circuits, probability, and programming familiarity. Use the [prerequisite diagnostic](../../../curriculum/prerequisites.md) to identify targeted gaps.  
**Planned effort:** **42 hours** (35–45 hour planning range), normally 9–14 weeks at 3–5 hours per week.
**Position in sequence:** First technical course. Its network and constraint concepts support energy economics, market design, and distribution DER analysis.

## Purpose

Develop the physical and mathematical literacy needed to understand how electricity moves through transmission and distribution networks, how engineers represent operating constraints, and how new generation, storage, and load affect infrastructure. The course moves from electrical quantities to network models and then to applied DER and interconnection cases.

This is a focused graduate foundation, not a complete power engineering degree or a utility-grade planning qualification.

## Learning outcomes

By the end, the learner should be able to:

1. Trace the physical path from generation to end use and distinguish transmission from distribution functions.
2. Calculate three-phase power, power factor, complex power, and per-unit quantities with consistent bases and units.
3. Formulate nodal balance and simplified power-flow equations and interpret bus voltages, angles, and branch flows.
4. Explain why distribution feeders are often unbalanced and identify the limitations of balanced positive-sequence approximations.
5. Analyze first-order feeder voltage and thermal constraints under load and DER injections.
6. Explain the roles of voltage regulation, protection, reliability, and inverter-based resources at a conceptual level.
7. Reproduce a small computational network case, validate important outputs, and state what the model excludes.
8. Communicate engineering findings without presenting a screening model as an operational interconnection study.

## Learning sequence

| Stage | Topic | Required evidence |
|---|---|---|
| 1 | Grid architecture, one-line diagrams, AC quantities, three-phase power | Annotated one-line diagram and PS1 |
| 2 | Per-unit system, transformers, impedance, network representation | Conversion exercises and network derivation |
| 3 | Power-flow balance, DC approximation, numerical solution concepts | PS2 and three-bus lab |
| 4 | Radial distribution, voltage drop, losses, thermal limits, DER injection | PS3 and feeder-screen lab |
| 5 | Unbalanced feeder analysis and benchmark interpretation | PS4 and OpenDSS benchmark |
| 6 | Flexible interconnection, export envelopes, storage and control | PS5 and scenario lab |
| 7 | Synthesis and engineering communication | Final technical report and self-assessment |

The stages are ordered conceptually. Spread them over the planned duration; do not treat each row as a one-week deadline.

## Core materials

- Kersting, William H. *Distribution System Modeling and Analysis*, 5th ed. CRC Press. Core reference for distribution modeling and unbalanced feeders.
- Grainger, John J., and William D. Stevenson. *Power System Analysis*. McGraw-Hill. Reference for network and power-flow foundations.
- Wood, Allen J., Bruce F. Wollenberg, and Gerald B. Sheblé. *Power Generation, Operation, and Control*. Wiley. Reference for operations and optimization context.
- Purdue ECE 51020, *Power Distribution System Analysis*: [official course catalog](https://engineering.purdue.edu/ECE/Academics/Undergraduates/UGO/CourseInfo/courseInfo?courseid=841&show=true&type=undergrad).
- Purdue ECE 51032, *Computational Methods for Power System Analysis*: [official graduate ECE catalog](https://engineering.purdue.edu/ECE/Academics/Undergraduates/UGO/CourseInfo/coursesGradByArea).
- [IEEE 13-node distribution test feeder resources](https://cmte.ieee.org/pes-testfeeders/resources/).

Use textbooks for derivations and the benchmark documentation for model conventions. Verify the exact software and feeder-data version used in a computational submission.

## Required assessments

| ID | Assignment | Planned hours | Purpose |
|---|---|---:|---|
| PS1 | [Three-phase fundamentals and per-unit quantities](problem-set-01.md) / [solution notes](problem-set-01-solutions.md) | 3 | Electrical quantities and base conversion |
| PS2 | [Network models, power flow, and DER constraints](problem-set-02.md) / [solution notes](problem-set-02-solutions.md) | 3 | Nodal balance and network reasoning |
| PS3 | [Radial feeder DER integration](problem-set-03-radial-der.md) / [solution notes](problem-set-03-radial-der-solutions.md) | 3 | Voltage and thermal screening |
| PS4 | [IEEE 13-node OpenDSS benchmark](problem-set-04-ieee13-opendss.md) / [solution guide](problem-set-04-ieee13-opendss-solutions.md) | 4 | Unbalanced AC benchmark analysis |
| PS5 | [Flexible interconnection and dynamic export envelopes](problem-set-05-flexible-interconnection.md) / [solution notes](problem-set-05-flexible-interconnection-solutions.md) | 3 | Operating envelopes and DER flexibility |
| LAB1 | [Three-bus DC power flow](../../../projects/power-systems/three-bus-dc-power-flow/README.md) | 3 | Matrix formulation and branch-flow checks |
| LAB2 | [Radial DER hosting-capacity screen](../../../projects/power-systems/radial-der-hosting-capacity/README.md) | 4 | Parameter and scenario sensitivity |
| LAB3 | [IEEE 13-node OpenDSS benchmark](../../../projects/power-systems/radial-der-hosting-capacity/benchmarks/ieee13-opendss/README.md) | 4 | Nonlinear unbalanced feeder simulation |
| LAB4 | [Flexible interconnection scenarios](../../../projects/power-systems/flexible-interconnection/README.md) | 3 | Export constraints and operational flexibility |
| COURSE | Technical report and self-assessment | 12 | Integrated engineering analysis |

Total planned effort: **42 hours**. The course tracker is the source for the planning baseline. Optional reading and extensions are not included.

## Assessment and final project

The required work combines analytical problem solving, computational reproduction, and technical communication. The final report should compare a baseline feeder/network case with a defined DER, storage, or load-growth scenario.

Suggested final-project weighting:
- Physical formulation and assumptions: 25%.
- Mathematical/computational correctness: 25%.
- Validation and sensitivity: 20%.
- Engineering interpretation: 20%.
- Reproducibility and communication: 10%.

The report must include equations, units, input provenance, solver/software version, at least one independent check, a sensitivity test, and a model-limitations section. Do not use confidential employer or customer information.

## Model boundaries

The balanced first-order radial feeder screen is a screening approximation. The IEEE 13-node OpenDSS benchmark is a nonlinear unbalanced AC simulation of a published test feeder. They are not a direct numerical validation pair because their network data and assumptions differ. A matched reduced-network comparison is a separate validation exercise.

The three-bus DC power-flow lab omits voltage magnitude, reactive power, losses, and AC feasibility. The learner must identify these exclusions when interpreting results.

## Completion gate

A course is complete only when the learner has attempted and corrected all five problem sets, reproduced and modified the required labs, submitted the technical report, and completed a self-assessment against the [program rubric](../../../ACADEMIC_STANDARDS.md). Record actual hours and evidence links in the progress tracker. Reading the solution files is not completion evidence.

## Next step

Proceed to [Y1-02 — Energy Economics and Market Fundamentals](../y1-02-energy-economics/README.md). The next course uses the physical constraints developed here to analyze dispatch, prices, welfare, and investment.
