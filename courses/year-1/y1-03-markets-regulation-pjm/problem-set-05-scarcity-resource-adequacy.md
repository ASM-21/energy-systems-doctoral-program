# Y1-03 Problem Set 5 — Scarcity Pricing, Resource Adequacy, and Ancillary-Service Co-Optimization

**Estimated time:** 5–7 hours  
**Level:** Graduate applied electricity-market design  
**Prerequisites:** Merit-order dispatch, marginal pricing, basic constrained optimization, and the Y1-03 market-institutions sequence.

## Learning objectives

By completing this assignment, you should be able to distinguish energy adequacy from resource adequacy, calculate a planning-reserve requirement, explain the economic logic of scarcity pricing, formulate a simplified energy-and-reserve co-optimization problem, and assess the limits of market-price signals as investment incentives.

Use the simplified assumptions below. These are teaching models, not representations of current PJM tariff parameters or actual market-clearing algorithms.

## Problem 1 — Energy dispatch and scarcity conditions

A system has 1,000 MW of demand and three available generators:

| Unit | Marginal cost ($/MWh) | Available capacity (MW) |
|---|---:|---:|
| A | 20 | 400 |
| B | 50 | 400 |
| C | 100 | 300 |

1. Calculate the economic dispatch and uniform energy price under a single-period, unconstrained merit-order model.
2. Calculate total production cost and identify the marginal unit.
3. Now suppose an unexpected 30 MW outage occurs at Unit B, leaving only 370 MW available from B. Recalculate dispatch and price if all 1,000 MW of demand can still be served.
4. Explain why a scarcity price is not simply the marginal cost of the most expensive generator. Discuss the roles of operating-reserve scarcity, demand response, involuntary curtailment, and a value-of-lost-load (VOLL) framework.
5. Explain why a price cap can protect consumers from extreme settlement prices while also weakening the energy-market revenue signal during scarcity. Identify at least two complementary mechanisms that may support resource adequacy.

## Problem 2 — Planning reserve margin and capacity procurement

A hypothetical system forecasts a coincident peak load of 10,000 MW. Its planning reserve margin requirement is 15%.

The resource accreditation review produces the following values:

- Existing accredited capacity: 11,200 MW.
- New accredited capacity already under construction and expected to enter before the delivery year: 100 MW.
- Retirements before the delivery year: 50 MW.
- A demand-response resource is accredited at 100 MW.

For this exercise, assume all listed quantities are additive and comparable, and the demand-response accreditation counts toward the planning requirement.

1. Calculate the planning-reserve requirement in MW.
2. Calculate the net accredited capacity before any new procurement.
3. Calculate the remaining capacity shortfall or surplus.
4. If the system procures the shortfall at a hypothetical clearing price of $140,000 per MW-year, calculate the annual capacity procurement cost.
5. Recalculate the shortfall if the demand-response resource is unavailable for the delivery year.
6. Explain why nameplate MW, accredited MW, dependable capacity, and energy availability are not interchangeable. Discuss at least three accreditation risks for batteries, intermittent renewables, demand response, or thermal generators.
7. Explain why a planning-reserve margin is a reliability planning construct rather than a guarantee that energy will be available at every location and hour.

## Problem 3 — Energy and operating-reserve co-optimization

A system operator must serve fixed demand while procuring upward operating reserve. It has three generators:

| Unit | Energy offer ($/MWh) | Reserve offer ($/MW-h) | Capacity (MW) |
|---|---:|---:|---:|
| A | 18 | 8 | 80 |
| B | 32 | 5 | 70 |
| C | 55 | 2 | 50 |

Demand is 150 MW and the upward reserve requirement is 20 MW. Let (p_i) be energy dispatch and (r_i) be upward reserve awarded to unit (i).

Formulate a linear optimization model that minimizes total energy and reserve offer cost, subject to:

- energy balance;
- generator capacity limits (p_i+r_i \leq K_i);
- nonnegative energy and reserve awards;
- the system reserve requirement.

1. Write the objective and all constraints.
2. Explain why the capacity constraint couples energy and reserve decisions.
3. Solve the model using a spreadsheet Solver or a linear-programming package. Report (p_i), (r_i), total objective value, and binding constraints.
4. Compare the result with a sequential process that dispatches energy first and procures reserve only from residual headroom. Explain when the sequential process can be infeasible or more expensive.
5. Interpret the dual values on the energy-balance and reserve-requirement constraints. Explain why these shadow prices are not necessarily identical to a complete real-world locational marginal price or ancillary-service settlement price.

## Problem 4 — Scarcity, reliability, and market-design trade-offs

Write a 1,200–1,800 word analytical memo addressing the following:

1. Compare energy-only, capacity-market, and administratively determined resource-adequacy approaches. Identify the key incentive mechanism and principal failure mode for each.
2. Explain how scarcity pricing, operating-reserve demand curves, price caps, and out-of-market actions can interact.
3. Distinguish resource adequacy from operational reliability. Include fuel assurance, transmission deliverability, ramping, inertia/system strength, and extreme-weather correlated outages.
4. Evaluate how storage, demand response, flexible load, and distributed energy resources should be accredited and compensated without double-counting the same capability across energy, capacity, and ancillary services.
5. Identify distributional consequences: who pays for capacity, who receives scarcity rents, who bears outage risk, and how retail rate design affects exposure.
6. Propose a public-data research question that could be investigated for PJM without using confidential utility or market-participant information.

## Required deliverables

- Dispatch and capacity calculations with units.
- Reproducible optimization model or spreadsheet for Problem 3.
- A one-page diagram showing the relationship among energy, ancillary services, and resource adequacy.
- Analytical memo with a source register and a limitations paragraph.

## Suggested primary sources

- [PJM Manuals and Governing Documents](https://www.pjm.com/library/manuals) — as checked 2026-11-21, use Manual 18 Rev. 63 (effective 2026-09-24) for the capacity market, Manual 20A Rev. 3 (effective 2026-06-24) for resource-adequacy studies, and Manual 21B Rev. 06 (effective 2026-11-18) for generating capability/accreditation/ELCC classifications. Manuals 20 and 21A are retired effective 2025-06-01. Read the current revisions and cite exact sections; do not rely on archived or retired procedures.
- [PJM Data Miner](https://dataminer2.pjm.com/) — public market and system data, subject to product-specific definitions and access conditions.
- [Monitoring Analytics, PJM State of the Market](https://www.monitoringanalytics.com/reports/PJM_State_of_the_Market/) — independent market-monitor analysis.
- [FERC, Wholesale Electricity Markets: Overview and Guide](https://www.ferc.gov/wholesale-electricity-markets-overview-and-guide).
- [NERC Reliability Assessment](https://www.nerc.com/pa/RAPA/ra/Pages/default.aspx) — distinguish resource adequacy from operating reliability.

Do not quote a current PJM capacity price, reserve requirement, scarcity trigger, or offer cap from memory. Retrieve the applicable delivery-year auction results, tariff, manual, or FERC-approved order and record its date and governing status.

## Grading rubric

| Criterion | Weight |
|---|---:|
| Dispatch, capacity, and units | 20% |
| Optimization formulation and interpretation | 25% |
| Market-design reasoning | 25% |
| Reliability and accreditation analysis | 20% |
| Source discipline and reproducibility | 10% |
