# Solution Notes: Economic Dispatch, Lagrangian Duality, and Marginal Prices

All calculations are for the stylized single-node model in Problem Set 1. The results are not PJM prices or a reproduction of its market software.

## Problem 1 — Primal dispatch

The primal problem is:

`min 18p_A + 32p_B + 55p_C`

subject to:

`p_A + p_B + p_C = 160`

`0 ≤ p_A ≤ 80, 0 ≤ p_B ≤ 70, 0 ≤ p_C ≤ 50`.

Merit order dispatches A and B to capacity, then uses C for the remaining demand:

| Generator | Output | Capacity | Status |
|---|---:|---:|---|
| A | 80 MW | 80 MW | Upper bound |
| B | 70 MW | 70 MW | Upper bound |
| C | 10 MW | 50 MW | Interior |

Cost:

`80×18 + 70×32 + 10×55 = $4,230/hour`

Total capacity is 200 MW, leaving 40 MW unused. The demand-to-capacity ratio is 160/200 = 80%. C is marginal because its output is positive and below its upper bound.

The marginal offer equals the balance dual in this convex single-node model because the marginal unit can increase or decrease output at the optimum and all offers are linear. This interpretation relies on perfect competition/price-taking behavior, a feasible convex optimization problem, no network constraints, no losses, no reserve coupling, no nonconvex commitment costs, and consistent pricing/settlement conventions.

## Problem 2 — Lagrangian and KKT

Use the Lagrangian:

`L = Σ_i c_i p_i + λ(D - Σ_i p_i) + Σ_i μ_i(p_i - P_i) - Σ_i ν_i p_i`

with `μ_i ≥ 0` and `ν_i ≥ 0`.

Stationarity:

`c_i - λ + μ_i - ν_i = 0`.

Primal feasibility requires balance and all output bounds. Dual feasibility requires nonnegative upper- and lower-bound multipliers. Complementary slackness requires:

`μ_i(p_i-P_i)=0`, and `ν_i p_i=0`.

At the solution:
- A is at its upper bound and has positive output: `μ_A = λ - 18`, `ν_A=0`.
- B is at its upper bound and has positive output: `μ_B = λ - 32`, `ν_B=0`.
- C is interior: `μ_C=ν_C=0`, so stationarity gives `λ=55`.

Therefore:
- `λ = $55/MWh`;
- `μ_A = $37/MW·h`;
- `μ_B = $23/MW·h`;
- `μ_C = 0`;
- all lower-bound multipliers are zero.

The balance dual is the marginal increase in minimized system cost for one additional MW of demand over the local range where the active set remains unchanged. The capacity multiplier is the marginal reduction in minimized cost from relaxing that generator's upper bound by one MW. For A, one additional MW of capacity can displace one MW of C and save $37 per hour for each MW of additional capacity. For B, the corresponding saving is $23 per hour per MW.

The dual variables have compatible marginal-value units when interpreted with the model's hourly objective and MW constraints. A balance multiplier is dollars per MWh; an upper-capacity multiplier is dollars per hour per MW of capacity, numerically equivalent to dollars per MW-hour. State the interval and objective units when reporting them.

## Problem 3 — Finite differences

At 161 MW: A=80, B=70, C=11. Cost is $4,285/hour, an increase of $55/hour.

At 159 MW: A=80, B=70, C=9. Cost is $4,175/hour, a decrease of $55/hour.

At A capacity 81 MW and demand 160: A=81, B=70, C=9. Cost is:

`81×18 + 70×32 + 9×55 = $4,193/hour`

The objective decreases by $37/hour for the one-MW capacity increase.

At B capacity 71 MW: A=80, B=71, C=9. Cost is:

`80×18 + 71×32 + 9×55 = $4,207/hour`

The objective decreases by $23/hour.

These one-unit finite differences match the local dual values because the active set does not change over these perturbations. For larger perturbations, the marginal generator or active constraints may change, so the original dual values need not remain valid.

## Problem 4 — Scarcity

At 120 MW: A=80, B=40, C=0; cost is $2,720/hour; B is marginal at $32/MWh.

At 180 MW: A=80, B=70, C=30; cost is $5,330/hour; C is marginal at $55/MWh.

At 200 MW: A=80, B=70, C=50; cost is $6,430/hour; all capacity is fully utilized. The model has no feasible marginal increase in demand. At this boundary, the balance dual is not uniquely determined by the original LP in the same way as an interior marginal price; a scarcity price requires an explicit representation of shortage, reserve scarcity, or another binding reliability constraint.

Add load shedding `s ≥ 0` with VOLL $10,000/MWh:

`min 18p_A + 32p_B + 55p_C + 10000s`

subject to:

`p_A + p_B + p_C + s = D`

and the generator bounds. If demand exceeds 200 MW, the additional demand is served by load shedding, and the balance dual becomes $10,000/MWh while load shedding is marginal. This is an illustrative penalty formulation, not a claim about the exact PJM scarcity-price design.

Reserve requirements can consume headroom. If the operator must hold upward reserve, a generator at its maximum output may be unable to provide reserve, making reserve constraints bind before energy demand reaches installed capacity.

## Problem 5 — Network and LMP

With two nodes, each node has its own power balance, and line flow is constrained by thermal limits. A DC approximation relates flow to phase-angle differences and line reactance. The nodal balance duals can differ when congestion binds. In a lossless DC model, the price difference is associated with congestion; in an AC or loss-aware formulation, marginal losses also contribute.

The linked two-node lab demonstrates that a constrained line can force a more expensive local generator to run and create different nodal marginal values. DC-OPF still omits voltage magnitude, reactive power, nonlinear losses, and many security constraints unless explicitly modeled.

## Problem 6 — Market interpretation

The marginal offer is the incremental offer for the marginal unit under the model. It is not the generator's average production cost, fixed-cost recovery, total revenue, or net profit. Nonconvex startup and minimum-run constraints can make a unit's total cost exceed its energy-market revenue at the marginal price. Uplift or make-whole payments may compensate eligible resources under applicable market rules.

An optimization dual price is not a complete participant settlement. Actual settlement can include loss treatment, congestion components, uplift, reserve products, capacity obligations, ancillary services, credits, charges, and market-specific rules. Any real PJM application must check the current tariff and manuals, product definitions, offer rules, commitment and dispatch processes, LMP calculation, loss treatment, uplift, and settlement provisions.