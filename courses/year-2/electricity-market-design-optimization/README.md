# Y2-04 — Electricity Market Design and Optimization

**Status:** Planned; Problem Sets 1–2 and worked solutions are available. The remaining analytical assignments, PJM case, and complete computational assessment sequence are in development.  
**Level:** Advanced graduate / doctoral preparation  
**Prerequisites:** Y1-01 Power Systems, Y1-02 Energy Economics, and Y1-03 Markets/Regulation or equivalent; linear algebra, calculus, constrained optimization, and introductory probability. Complete the relevant modules of [Y2-01 Advanced Mathematical Methods](../advanced-mathematics-energy-systems/README.md) before beginning the optimization sequence.  
**Planned effort:** 45–60 hours over approximately 20–24 modular weeks, usually 2–3 hours per week within the total program budget.  
**Position in sequence:** Integrative technical/economic course linking network physics, optimization, wholesale market rules, and investment incentives.

## Purpose and scope

Study how electricity markets coordinate generation, transmission, reserves, and investment under physical network constraints. The course moves from economic dispatch and locational marginal pricing to optimal power flow, unit commitment, reserve procurement, market power, resource adequacy, and transmission expansion.

The objective is not to memorize PJM rules. It is to understand the economic and mathematical logic behind market mechanisms, identify where the assumptions of simplified models fail, and connect model results to actual tariffs, manuals, and regulatory authority.

This course will not reproduce the full PJM market software or substitute for operational training. All teaching models must identify omitted network, reliability, market, and settlement features.

## Learning outcomes

By the end, the learner should be able to:

1. Formulate economic dispatch as a constrained optimization problem and derive the relationship between marginal costs and prices.
2. Derive a DC optimal power-flow formulation from network balance and line-flow approximations.
3. Interpret locational marginal prices as dual values and explain the effects of congestion and losses.
4. Explain the differences between energy, operating reserves, capacity/resource adequacy, and ancillary-service products.
5. Formulate simplified reserve co-optimization and interpret energy and reserve shadow prices.
6. Explain unit commitment's mixed-integer structure, intertemporal constraints, and nonconvex costs.
7. Analyze market power, pivotal suppliers, offer behavior, and the role of market monitoring.
8. Compare capacity mechanisms and resource-adequacy approaches while identifying reliability and accreditation assumptions.
9. Evaluate transmission expansion and cost allocation using engineering benefits, market effects, and regulatory institutions.
10. Critique the external validity of simplified market models against actual RTO/ISO rules and data.

## Learning sequence

| Stage | Topic | Energy-system application | Evidence planned |
|---|---|---|---|
| 1 | Constrained dispatch and marginal pricing | Merit-order clearing and scarcity | Analytical dispatch derivation |
| 2 | Network-constrained dispatch | DC power flow, congestion, LMP | DC-OPF model and dual interpretation |
| 3 | AC OPF and model limits | Voltage, reactive power, losses, security | Formulation comparison and model-risk memo |
| 4 | Operating reserves and co-optimization | Energy/reserve capacity coupling | LP model and finite-difference checks |
| 5 | Unit commitment | Startup, minimum output, ramping, minimum up/down time | Small mixed-integer model |
| 6 | Market power and monitoring | Pivotal supply, withholding incentives, mitigation | Market-monitor report critique |
| 7 | Resource adequacy and capacity mechanisms | Accreditation, scarcity, capacity procurement | PJM manual and design comparison |
| 8 | Transmission planning and cost allocation | Congestion, reliability, beneficiaries, regional planning | Public project case analysis |
| 9 | Synthesis | Compare market design alternatives | Research paper or technical memo |

## Required materials and references

- Stoft, Steven. *Power System Economics: Designing Markets for Electricity*. Wiley-IEEE Press, 2002.
- Kirschen, Daniel S., and Goran Strbac. *Fundamentals of Power System Economics*, 2nd ed. Wiley, 2018.
- Wood, Allen J., Bruce F. Wollenberg, and Gerald B. Sheblé. *Power Generation, Operation, and Control*. Wiley.
- Conejo, Antonio J., Miguel Carrión, and Juan M. Morales. *Decision Making Under Uncertainty in Electricity Markets*. Springer, 2010. Use selected chapters for stochastic market decisions.
- FERC, [Wholesale Electricity Markets: Overview and Guide](https://www.ferc.gov/wholesale-electricity-markets-overview-and-guide).
- PJM, [manuals and tariffs](https://www.pjm.com/library/manuals) and [Data Miner](https://dataminer2.pjm.com/).
- Monitoring Analytics, [PJM State of the Market reports](https://www.monitoringanalytics.com/reports/PJM_State_of_the_Market/).

The official RTO/ISO documents control claims about actual market rules. Textbooks explain general mechanisms; they do not establish the current PJM tariff or manual requirements. Record version, section, effective date, and access date.

## Existing computational foundations

These projects provide prerequisites and examples, but they do not yet constitute the complete Y2-04 assessment set:

- [Merit-order dispatch](../../../projects/energy-economics/merit-order-dispatch/README.md)
- [Two-node congestion and nodal prices](../../../projects/power-systems/two-node-congestion/README.md)
- [Three-bus DC power flow](../../../projects/power-systems/three-bus-dc-power-flow/README.md)
- [Energy and reserve co-optimization](../../../projects/energy-economics/energy-reserve-cooptimization/README.md)
- [Three-bus DC-OPF](../../../projects/power-systems/three-bus-dc-opf/README.md)
- [Stochastic and robust capacity planning](../../../projects/energy-economics/stochastic-robust-capacity-planning/README.md)

The models are intentionally simplified. Their READMEs state the assumptions and omissions. In particular, a single-period LP is not a unit-commitment model, and a DC network approximation is not an AC security-constrained dispatch model.

## Published assessment

- [Problem Set 1: Economic dispatch, Lagrangian duality, and marginal prices](problem-set-01-economic-dispatch-duality.md)
- [Problem Set 1 solution notes](problem-set-01-economic-dispatch-duality-solutions.md)
- [Problem Set 2: Three-bus DC optimal power flow and LMPs](problem-set-02-three-bus-dc-opf.md)
- [Problem Set 2 solution notes](problem-set-02-three-bus-dc-opf-solutions.md)
- [Computational lab: Three-bus DC-OPF](../../../projects/power-systems/three-bus-dc-opf/README.md)

The first assignment is an advanced convex dispatch/KKT exercise. It is not a substitute for the later network-constrained, intertemporal, and institutional modules.

## Planned assessment architecture

The full course should include:
- analytical problem sets for dispatch, LMP, duality, reserve co-optimization, and unit commitment;
- at least two computational assignments with automated tests and benchmark checks;
- one version-specific PJM tariff/manual analysis;
- one market-monitoring or market-power critique;
- a final paper or technical study with reproducible code, sensitivity analysis, and model-risk discussion.

Problem Sets 1–2 establish the convex single-node dispatch and three-bus DC-OPF foundations. The full assessment sequence remains incomplete. Do not mark this course active or schedule it as required work until the remaining assignments, solution notes, and validation checks are complete.

## Completion standard

The eventual final project should contain a mathematical formulation, reproducible implementation, independent numerical checks, a comparison to actual market rules, and an interpretation of the economic and institutional implications. It must distinguish model output from real market outcomes and identify the conditions under which its conclusions would fail.

## Next step

The next development step is a network-constrained dispatch and LMP assignment that builds on the existing two-node congestion and DC power-flow labs. This course should follow the relevant mathematical foundations in Y2-01 and can be selected after the learner identifies whether the primary research direction is wholesale market design, resource adequacy, transmission, or infrastructure investment. For utility finance and regulation, see [Y2-03 Infrastructure Economics and Utility Investment](../infrastructure-economics-utility-investment/README.md).
