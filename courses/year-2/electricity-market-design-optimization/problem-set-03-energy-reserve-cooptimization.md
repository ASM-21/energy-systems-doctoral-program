# Problem Set 3: Energy and Operating-Reserve Co-Optimization

**Level:** Advanced graduate  
**Suggested effort:** 4–5 hours  
**Prerequisites:** Y2-04 Problem Sets 1–2, linear programming duality, and Y1-03 reserve/resource-adequacy concepts

This assignment studies a single-node, single-hour convex co-optimization model. It does not reproduce PJM's actual reserve products, response-time requirements, reserve zones, or settlement rules. Offers and capacities are synthetic.

## Case A — Benchmark co-optimization

Three generators offer energy and upward reserve:

| Unit | Energy offer | Reserve offer | Capacity |
|---|---:|---:|---:|
| A | $18/MWh | $8/(MW·h) | 80 MW |
| B | $32/MWh | $5/(MW·h) | 70 MW |
| C | $55/MWh | $2/(MW·h) | 50 MW |

Demand is 160 MW and the upward-reserve requirement is 20 MW. For the one-hour interval, minimize total energy and reserve offer cost. Each unit's energy plus reserve award cannot exceed its capacity.

## Problem 1 — Primal co-optimization formulation

1. Define energy dispatch p_i and upward reserve r_i for each unit.
2. Write the objective and constraints for energy balance, reserve sufficiency, joint capacity, and nonnegativity.
3. Explain why energy and reserve capacity are coupled.
4. Explain why an energy-only dispatch followed by an independent reserve award can fail to find the least-cost feasible joint solution.

## Problem 2 — Benchmark solution and feasibility

1. Solve the co-optimization and report energy and reserve awards for each unit.
2. Verify energy balance, reserve sufficiency, and each unit's joint capacity.
3. Calculate total objective value for the one-hour interval.
4. Compare the energy dispatch with the energy-only merit-order result.
5. Explain why the reserve requirement can change energy dispatch even though reserve itself does not serve energy demand.

## Problem 3 — Lagrangian duality

Use a consistent sign convention and derive the KKT conditions for:
- the energy balance equality;
- the minimum reserve requirement;
- joint generator capacity;
- energy and reserve lower bounds.

1. Identify the energy-balance dual and reserve-requirement dual.
2. Calculate the capacity shadow values for A, B, and C.
3. Interpret the economic meaning and units of each dual.
4. Explain why a capacity constraint can bind while its shadow value is zero.
5. Explain why the reserve marginal value is not the same as the reserve offer of every awarded unit.

## Problem 4 — Finite-difference validation

1. Increase energy demand from 160 to 161 MW. Calculate the objective change.
2. Increase the reserve requirement from 20 to 21 MW. Calculate the objective change.
3. Increase A's capacity from 80 to 81 MW. Calculate the objective change.
4. Compare each finite difference with its relevant dual.
5. Identify where the current active basis ceases to apply. Explain why the 150 MW energy-demand case can have a non-unique energy dual.

## Case B — Why sequential procurement can be more expensive

Use the same energy offers and capacities, but change reserve offers to:
- A: $100/(MW·h);
- B: $1/(MW·h);
- C: $50/(MW·h).

Demand remains 160 MW and reserve remains 20 MW.

## Problem 5 — Sequential versus joint optimization

1. Dispatch energy first using the energy offers only. Report the energy-only dispatch.
2. If reserve is then procured without redispatch, allocate reserve to the cheapest units with available headroom. Calculate the total cost.
3. Solve the joint co-optimization and report energy/reserve awards and total cost.
4. Explain why the joint solution may redispatch energy to create headroom for a low-cost reserve provider.
5. Quantify the cost difference and identify the opportunity cost of holding capacity for reserve.

## Problem 6 — Product design and market translation

Prepare a 500–800 word note that:
- distinguishes upward reserve from energy, regulation, frequency response, and capacity/resource adequacy;
- explains why reserve response time, duration, deliverability, telemetry, performance, and location matter;
- identifies how network constraints and reserve zones would change the model;
- explains why reserve prices and energy LMPs are not interchangeable;
- identifies the PJM tariff/manual sections and version dates that must be verified before interpreting actual awards or settlements.

## Submission

Submit the primal and KKT derivations, an award/feasibility table, dual-value and finite-difference checks, a sequential-versus-joint comparison, and the market-translation note. Include units, sign conventions, active constraints, and model limitations.

## Evaluation

Primal formulation and feasibility (20%), duality and economic interpretation (25%), finite-difference validation (20%), sequential/joint comparison (15%), market-product and institutional reasoning (10%), reproducibility and presentation (10%).