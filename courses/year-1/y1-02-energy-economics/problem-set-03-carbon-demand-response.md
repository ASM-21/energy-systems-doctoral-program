# Y1-02 Problem Set 3 — Carbon Pricing and Flexible Demand

**Estimated time:** 3–4 hours  
**Computational lab:** [Economic dispatch and marginal pricing](../../../projects/energy-economics/merit-order-dispatch/README.md)  
**Data:** Synthetic generator fleet

Use the provided CSV and dispatch model. Show all units, effective marginal costs, and binding constraints. Treat the model as a one-hour, single-node LP.

## Problem 1 — Baseline merit order

For 1,000 MW of demand, determine dispatch by unit, total variable production cost, total emissions, and the marginal energy price. Explain why the energy-balance dual is the marginal cost of serving a small additional increment of demand in this model.

## Problem 2 — Carbon price and merit-order changes

Apply a carbon price of 100 USD/tCO2.

1. Calculate each unit's carbon-inclusive effective marginal cost.
2. Reorder the merit order and solve dispatch for 1,000 MW.
3. Calculate total emissions, fuel cost, carbon payment, objective cost, and marginal price.
4. Compare emissions with the baseline and explain the dispatch substitution.
5. Explain why a carbon price may change the dispatch order in one fleet but not another.

## Problem 3 — Demand response as a dispatchable resource

Return the carbon price to zero. Allow up to 200 MW of flexible demand reduction at a cost of 50 USD/MWh.

1. Solve for generator dispatch and demand-response quantity.
2. Calculate served demand, fuel cost, demand-response cost, total objective cost, and marginal price.
3. Explain why the model uses less than the full 200 MW demand-response capability.
4. Interpret the demand-response cost parameter. Distinguish it from involuntary load shedding and from a retail tariff.

## Problem 4 — Combined carbon price and demand response

Apply a 100 USD/tCO2 carbon price, allow up to 200 MW demand response, and set its cost to 80 USD/MWh. Determine the optimal resource order and dispatch. Identify which resource or constraint is marginal. Compare the result with Problems 2 and 3.

## Problem 5 — Economic and policy interpretation

Write a 750–1,000 word memo discussing:
- how a carbon price changes private dispatch incentives and the social cost represented in this model;
- how demand response competes with generation;
- who pays and who receives the carbon payment or demand-response compensation in an actual market design;
- why an LP's marginal price is not automatically a retail price or a complete PJM LMP;
- omitted constraints, including network congestion, ramping, minimum generation, start-up costs, reserves, uncertainty, market power, and demand elasticity.

## Deliverables

- Reproducible code output for all four cases.
- A dispatch comparison table.
- An emissions and cost decomposition.
- A policy memo with assumptions and limitations.

## Grading rubric

| Criterion | Weight |
|---|---:|
| Dispatch and dual calculations | 25% |
| Carbon-cost and emissions accounting | 20% |
| Demand-response formulation | 20% |
| Combined scenario and sensitivity | 15% |
| Economic interpretation and limitations | 20% |
