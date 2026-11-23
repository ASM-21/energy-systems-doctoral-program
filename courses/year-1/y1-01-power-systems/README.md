# Y1-01 — Power Systems and Electricity Infrastructure

**Status:** Active Year 1 course

**Level:** Graduate foundation / early doctoral preparation  
**Duration:** 10–12 weeks | **Effort:** 35–45 hours  
**Prerequisites:** Calculus, linear algebra, differential equations, basic circuits, probability, programming familiarity.

## Purpose
Develop working technical literacy in structure, modeling, operation, and constraints of transmission and distribution systems. Connect physical network behavior to interconnection, DER integration, reliability, and planning.

## Learning outcomes
1. Explain the physical path from generation to end use and distinguish transmission/distribution.
2. Use three-phase and per-unit concepts to interpret system quantities.
3. Explain network representation, power-flow balance, voltage limits, and thermal constraints.
4. Describe feeders, unbalanced systems, voltage regulation, transformers, and protection conceptually.
5. Formulate a simplified power-flow or distribution-analysis problem computationally.
6. Explain how DERs, storage, flexible loads, and large new loads affect planning and operations.
7. Communicate assumptions, limitations, and engineering implications.

## Weekly sequence
| Week | Topic | Work |
|---|---|---|
| 1 | Grid architecture, components, topology, AC fundamentals | One-line diagram and system actors |
| 2 | Three-phase quantities, complex power, power factor | Problem set 1 |
| 3 | Per-unit system, transformers, impedance | Conversion exercises |
| 4 | Network models and power-flow formulation | Derive nodal balance equations |
| 5 | Newton–Raphson power flow and convergence | Implement/reproduce small case |
| 6 | Distribution systems, radial feeders, voltage regulation | Problem set 2 |
| 7 | Unbalanced distribution and DER interconnection | Feeder case |
| 8 | Reliability, contingencies, protection concepts | Reliability memo |
| 9 | Optimal power flow and dispatch interface | Simplified optimization |
| 10 | Storage, inverter-based resources, flexible demand | Integration comparison |
| 11 | Planning, hosting capacity, load growth | Project analysis |
| 12 | Synthesis | Final technical report |

## Verified course benchmarks and references
- Purdue ECE 51020, *Power Distribution System Analysis*: [official catalog page](https://engineering.purdue.edu/ECE/Academics/Undergraduates/UGO/CourseInfo/courseInfo?courseid=841&show=true&type=undergrad). Catalog page includes prerequisites, text, lecture outline, and assessment description.
- Purdue ECE 51032, *Computational Methods for Power System Analysis*: listed in Purdue's [official graduate ECE catalog](https://engineering.purdue.edu/ECE/Academics/Undergraduates/UGO/CourseInfo/coursesGradByArea) under Power and Energy Devices and Systems (3 credits; catalog lists Fall).
- Kersting, *Distribution System Modeling and Analysis*, 5th ed.; Grainger & Stevenson, *Power System Analysis*; Wood, Wollenberg & Sheblé, *Power Generation, Operation, and Control*.

These are curriculum references, not enrollment or claims that every chapter is freely accessible. Catalog schedules and details can change.

## Assessments
1. Three-phase power, power factor, per-unit conversion, transformer impedance.
2. Feeder voltage drop, line losses, voltage regulation, simplified DER impact.
3. Computational lab: build/adapt a small radial feeder model; document inputs, solver, convergence, validation.
4. Technical memo: explain a real interconnection/distribution constraint and operational/economic significance.
5. Final project: model a small distribution/transmission case and evaluate a DER, storage, load-growth, or upgrade scenario.

## Final project rubric
Physical model/assumptions 25%; mathematical/computational correctness 25%; validation/sensitivity 20%; engineering interpretation 20%; reproducibility/communication 10%.

## Suggested project
Construct a small feeder model with baseline load, then add PV or storage and a large load. Evaluate voltage/thermal constraints under selected conditions. Do not claim a simplified model represents a real utility feeder. Identify synthetic/public inputs and limitations.

## Completion evidence
Problem-set solutions, code, data dictionary, figures, technical memo, final report, and self-assessment.

## Problem sets and worked checks

Complete the assignments in sequence. Problem Sets 1–2 establish electrical quantities and network-model reasoning; Problem Sets 3–5 apply those foundations to distribution DER, unbalanced benchmark analysis, and flexible interconnection. Problem Set 4 requires the separate OpenDSS engine; the other assignments use the stated lightweight Python models or hand calculations.

| Assignment | Focus | Estimated effort | Assignment | Worked solution |
|---|---|---:|---|---|
| PS1 | Three-phase fundamentals and per-unit quantities | 2–3 h | [Problem](problem-set-01.md) | [Solution notes](problem-set-01-solutions.md) |
| PS2 | Network models, power flow, and DER constraints | 2–3 h | [Problem](problem-set-02.md) | [Solution guidance](problem-set-02-solutions.md) |
| PS3 | Radial feeder DER integration | 3–4 h | [Problem](problem-set-03-radial-der.md) | [Solution notes](problem-set-03-radial-der-solutions.md) |
| PS4 | IEEE 13-node OpenDSS benchmark | 4–6 h | [Problem](problem-set-04-ieee13-opendss.md) | [Solution guide](problem-set-04-ieee13-opendss-solutions.md) |
| PS5 | Flexible interconnection and dynamic export envelopes | 4–5 h | [Problem](problem-set-05-flexible-interconnection.md) | [Solution notes](problem-set-05-flexible-interconnection-solutions.md) |

## Computational labs

- [Three-bus DC power flow](../../../projects/power-systems/three-bus-dc-power-flow/README.md)
- [Radial feeder DER hosting-capacity screen](../../../projects/power-systems/radial-der-hosting-capacity/README.md)
- [IEEE 13-node OpenDSS benchmark](../../../projects/power-systems/radial-der-hosting-capacity/benchmarks/ieee13-opendss/README.md)
- [Flexible interconnection and dynamic export envelopes](../../../projects/power-systems/flexible-interconnection/README.md)

**Important distinction:** the balanced first-order feeder screen is a screening approximation, while the IEEE 13-node OpenDSS benchmark is a nonlinear unbalanced AC simulation of a published test feeder. They are not a direct numerical validation pair because their network data and assumptions differ. The next validation step would be to construct a matched reduced network and compare the approximation against an AC-capable solution.

## How to use the assessments

Attempt each problem set before opening the linked worked solution. For computational work, reproduce the stated result, inspect the assumptions, change at least one parameter, and explain the effect. Retain corrected derivations, code, and short technical explanations as completion evidence.

## Next step

Proceed to [Y1-02 — Energy Economics and Market Fundamentals](../y1-02-energy-economics/README.md). Use the [curriculum map](../../../curriculum/course-map.md) if prerequisite gaps suggest a different pace.
