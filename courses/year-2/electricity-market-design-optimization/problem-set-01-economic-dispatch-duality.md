# Problem Set 1: Economic Dispatch, Lagrangian Duality, and Marginal Prices

**Level:** Advanced graduate  
**Suggested effort:** 3–4 hours  
**Prerequisites:** Y1-02 dispatch economics, linear algebra, constrained optimization, and the relevant Y2-01 modules on KKT conditions and duality

This assignment is a single-period, single-node, lossless dispatch model. It is deliberately simpler than PJM's actual market-clearing process. All quantities are MW, prices are dollars per MWh, and the objective is dollars per hour.

## Case: Three-generator system

The system operator serves fixed demand of 160 MW using three generators:

| Generator | Marginal offer | Maximum output |
|---|---:|---:|
| A | $18/MWh | 80 MW |
| B | $32/MWh | 70 MW |
| C | $55/MWh | 50 MW |

Assume zero minimum output, no startup cost, no ramping constraint, no reserve requirement, no losses, and no transmission constraint. Offers are constant over the dispatch interval.

## Problem 1 — Primal economic dispatch

1. Formulate the dispatch problem as a linear program. Define the decision variables, objective, system balance constraint, and generator bounds.
2. Solve the dispatch using merit order. Report each generator's output, total production cost per hour, and the marginal unit.
3. Verify primal feasibility and calculate unused capacity.
4. Calculate total offered capacity and the demand-to-capacity ratio.
5. Explain why the marginal offer is the system marginal energy price in this convex, unconstrained single-node model, and list the assumptions required for that interpretation.

## Problem 2 — Lagrangian and KKT conditions

Write the Lagrangian using:
- the equality constraint that generation equals demand;
- upper output bounds;
- lower output bounds.

1. State the sign restrictions on inequality multipliers.
2. Derive stationarity, primal feasibility, dual feasibility, and complementary slackness.
3. Evaluate the KKT conditions at the dispatch from Problem 1.
4. Identify the balance multiplier and the upper-bound multipliers for generators A, B, and C.
5. Explain the economic interpretation of the system balance multiplier and generator capacity multipliers.

Use a consistent sign convention and state it. A sign error in the Lagrangian can reverse the interpretation of a shadow price.

## Problem 3 — Sensitivity and finite differences

1. Increase demand from 160 MW to 161 MW. Re-solve the dispatch and calculate the change in objective.
2. Reduce demand from 160 MW to 159 MW. Re-solve and calculate the change in objective.
3. Increase generator A's capacity from 80 MW to 81 MW while holding demand at 160 MW. Calculate the change in objective.
4. Increase generator B's capacity from 70 MW to 71 MW. Calculate the change in objective.
5. Compare the finite differences with the dual values from Problem 2. Explain why the equality-constraint multiplier and capacity-bound multipliers have different economic units or interpretations.
6. Explain why the shadow price is a local marginal value and may change when the active set changes.

## Problem 4 — Capacity scarcity and model boundaries

1. Solve the model at demand levels of 120 MW, 180 MW, and 200 MW.
2. Explain what happens to the marginal generator and the system balance dual as demand approaches total available capacity.
3. At 200 MW, explain why a further increase in demand is infeasible under this model. Show how adding a load-shedding variable with a value of lost load (VOLL) of $10,000/MWh changes the formulation.
4. Explain why a high price created by a load-shedding penalty is a model representation of scarcity, not proof that the actual market uses that exact price or rule.
5. Discuss how reserve requirements could make the system scarce before energy demand reaches installed capacity.

## Problem 5 — From single-node dispatch to locational marginal pricing

Consider a two-node system with a constrained transmission line. Explain how adding network constraints changes the dispatch formulation and the interpretation of the balance duals.

1. Write the conceptual nodal balance equations and a line-flow limit.
2. Explain why a single system-wide energy balance multiplier is no longer sufficient to describe all nodal marginal values.
3. Describe the energy, congestion, and marginal-loss components of an LMP, noting that this assignment's base model has no losses.
4. Reproduce or inspect the [two-node congestion lab](../../../projects/power-systems/two-node-congestion/README.md) and explain how its results differ from this single-node benchmark.
5. Identify why a DC-OPF result is not equivalent to a full AC security-constrained dispatch result.

## Problem 6 — Market interpretation and nonconvexity

1. Explain why a marginal offer is not necessarily the same as a generator's average cost, total revenue, or profit.
2. Describe how startup costs, minimum run times, ramp constraints, minimum generation, and integer commitment decisions break the simple convex dispatch interpretation.
3. Explain why uplift or make-whole payments may be required in markets with nonconvex costs, even when energy prices are derived from marginal pricing.
4. Distinguish an optimization model's dual price from the complete settlement price paid or received by a market participant.
5. Identify at least five real PJM market rules or implementation details that would need to be verified in the current tariff/manual before applying this model to an actual market outcome.

## Submission

Submit a derivation with a clearly stated Lagrangian sign convention, a reproducible dispatch calculation, a finite-difference table, and a 500–800 word model-boundary memo. Include a units table and identify every active constraint.

## Evaluation

Primal formulation and dispatch (20%), KKT/duality derivation (25%), sensitivity and shadow-price interpretation (20%), scarcity/network extensions (15%), market and institutional limitations (10%), reproducibility and presentation (10%).