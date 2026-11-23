# Problem Set 4: Unit Commitment, Startup Costs, and Nonconvex Dispatch

**Level:** Advanced graduate  
**Suggested effort:** 4–5 hours  
**Prerequisites:** Y2-04 Problem Sets 1–3, linear programming, binary variables, and constrained optimization

This assignment introduces unit commitment as a mixed-integer optimization problem. It uses a two-period synthetic system and omits ramping, minimum up/down times, reserves, network constraints, and uncertainty unless a question explicitly asks how those features would change the model.

## Case: Two generators and two periods

The system must serve demand of 80 MW in Period 1 and 150 MW in Period 2. Both periods are one hour. Both generators are initially off.

| Parameter | Generator 1 | Generator 2 |
|---|---:|---:|
| Energy offer | $20/MWh | $50/MWh |
| Minimum output | 30 MW | 0 MW |
| Maximum output | 100 MW | 100 MW |
| No-load cost | $100/hour | $40/hour |
| Startup cost | $500/start | $100/start |

Assume no shutdown cost. A unit incurs its no-load cost in every period it is committed, whether or not it produces at maximum output. Startup cost is incurred when a unit transitions from off to on.

## Problem 1 — Mixed-integer formulation

Define:
- p_i,t: generator output;
- y_i,t: commitment binary;
- u_i,t: startup indicator.

1. Write the total two-period objective, including energy, no-load, and startup costs.
2. Write energy balance in each period.
3. Write minimum and maximum output constraints linked to commitment.
4. Write startup logic using the prior-period commitment state.
5. Identify which variables are continuous and which are integer/binary.
6. Explain why the model is a mixed-integer linear program and why the convex dispatch dual-price interpretation from PS1 does not directly solve the commitment problem.

## Problem 2 — Solve the commitment schedule

1. Determine the least-cost commitment and dispatch schedule.
2. Report p, y, and u for each unit and period.
3. Calculate energy, no-load, startup, and total costs separately.
4. Verify demand balance and output bounds.
5. Explain why Generator 1 is committed in both periods and Generator 2 starts in Period 2.

## Problem 3 — LP relaxation and integrality gap

Relax the binary commitment variables to the continuous interval [0,1]. Keep all other constraints and costs unchanged.

1. Solve the relaxed model.
2. Report fractional commitment and startup variables.
3. Calculate the relaxed objective and integrality gap in dollars and as a percentage of the relaxed lower bound.
4. Explain why fractional commitment has no direct physical interpretation for a single generator in a single hour.
5. Explain why the LP relaxation is useful for lower bounds and branch-and-bound but is not an implementable operating schedule.

## Problem 4 — Energy prices, uplift, and nonconvex costs

1. Explain why a marginal energy price derived from a convex dispatch LP may not recover a committed unit's startup and no-load costs.
2. Explain the concept of make-whole or uplift payments in a market with nonconvex commitment costs.
3. Distinguish the unit commitment objective, a convex-hull or other pricing approach, and the actual settlement rules.
4. Explain why uplift should not be described as an additional energy LMP.
5. Identify the market-rule and settlement details that would need to be checked before applying this model to PJM.

## Problem 5 — Add operational constraints

Describe how the model would change if it included:
- ramp-up and ramp-down limits;
- minimum up and down times;
- startup/shutdown trajectories;
- reserve requirements and reserve response capability;
- must-run and self-scheduling resources;
- forced outages and uncertain demand.

For at least two constraints, write a mathematical representation and explain the data needed to parameterize it.

## Problem 6 — Sensitivity and model design

1. Identify how the schedule changes if Generator 1's startup cost rises from $500 to $1,000.
2. Identify how the schedule changes if Period 2 demand falls from 150 to 120 MW.
3. Explain why the optimal commitment schedule can change discontinuously as demand or startup cost changes.
4. Discuss the trade-off between model detail, computational tractability, and the fidelity required for a particular market or planning question.

## Submission

Submit a MILP formulation, a commitment/dispatch table, a cost reconciliation, an LP-relaxation comparison, and a 500–800 word explanation of nonconvex pricing and uplift. Include a clear statement of omitted operational constraints.

## Evaluation

Formulation and startup logic (20%), integer schedule and cost reconciliation (20%), LP relaxation and integrality gap (15%), pricing/uplift reasoning (20%), operational extensions (15%), reproducibility and model limits (10%).