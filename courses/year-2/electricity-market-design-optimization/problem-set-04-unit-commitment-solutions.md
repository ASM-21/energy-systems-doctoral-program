# Solution Notes: Unit Commitment, Startup Costs, and Nonconvex Dispatch

All results use the two-period, two-unit synthetic case. Each period is one hour.

## Problem 1 — MILP formulation

Minimize:

`Σ_{i,t}(c_i p_{i,t} + NL_i y_{i,t} + SU_i u_{i,t})`

subject to demand balance for each period:

`Σ_i p_{i,t} = D_t`

commitment-linked output:

`Pmin_i y_{i,t} ≤ p_{i,t} ≤ Pmax_i y_{i,t}`

startup logic:

`u_{i,t} ≥ y_{i,t} - y_{i,t-1}`

with initial commitment `y_{i,0}=0), binary `y_{i,t}∈{0,1}`, startup indicator `u_{i,t}∈[0,1]`, and `p_{i,t}≥0). Since commitment is binary and startup cost is positive, the startup indicator takes 1 when a start occurs in an optimal solution. A production model may also explicitly require binary startup variables and model shutdowns, minimum up/down times, and startup categories.

## Problem 2 — Integer solution

| Unit | Period | Dispatch | Commitment | Startup |
|---|---:|---:|---:|---:|
| G1 | 1 | 80 MW | 1 | 1 |
| G1 | 2 | 100 MW | 1 | 0 |
| G2 | 1 | 0 MW | 0 | 0 |
| G2 | 2 | 50 MW | 1 | 1 |

Period 1 demand: 80+0=80 MW. Period 2 demand: 100+50=150 MW.

Cost reconciliation:
- Energy: G1 period 1 = $1,600; G1 period 2 = $2,000; G2 period 2 = $2,500; total $6,100.
- No-load: G1 two periods = $200; G2 period 2 = $40; total $240.
- Startup: G1 one start = $500; G2 one start = $100; total $600.
- **Total = $6,940.**

G1's lower energy offer justifies commitment in both periods. G2 is not economical in Period 1 but is needed for the additional 50 MW in Period 2.

## Problem 3 — LP relaxation

With commitment variables relaxed to [0,1], one optimum is:
- G1 output: 80 MW in Period 1 and 100 MW in Period 2.
- G2 output: 0 MW in Period 1 and 50 MW in Period 2.
- G1 commitment: 0.8 in Period 1 and 1.0 in Period 2.
- G2 commitment: 0 in Period 1 and 0.5 in Period 2.
- Startup indicators: G1 0.8 then 0.2; G2 0 then 0.5.

The relaxed objective is $6,850. The integer optimum is $6,940, so the integrality gap is $90, or approximately 1.31% of the relaxed lower bound:

`(6940 - 6850) / 6850 × 100 = 1.314%`.

Fractional commitment does not mean a single physical generator is 80% on. It is a mathematical relaxation that can provide a lower bound for branch-and-bound. It is not an implementable commitment schedule.

## Problem 4 — Prices and uplift

A marginal energy price reflects the marginal cost of serving an additional unit of demand under the pricing formulation. Startup and no-load costs are nonconvex and may not be recovered by that marginal energy price, especially for units committed for reliability or intertemporal needs. A make-whole or uplift mechanism can compensate eligible resources for specified costs not recovered through market revenues under the applicable rules.

Uplift is not an additional energy LMP. It is a separate settlement adjustment governed by eligibility, cost definitions, revenue offsets, and market rules. Convex-hull pricing and other nonconvex pricing approaches seek to reduce uplift or improve incentives, but their properties differ and no generic model determines the actual market settlement.

## Problem 5 — Operational extensions

Ramp constraints can be written as:
- `p_{i,t} - p_{i,t-1} ≤ RU_i`;
- `p_{i,t-1} - p_{i,t} ≤ RD_i`.

A minimum up-time constraint requires a unit that starts to remain committed for a specified number of periods. One common formulation links startup indicators to future commitment states, with careful treatment of the horizon boundary. Minimum down time similarly constrains shutdowns and subsequent starts. Startup trajectories may distinguish hot, warm, and cold starts and associate different costs and times with each. Reserve capability requires headroom and response constraints, not merely unused nameplate capacity. Forced outages and uncertain demand require scenarios or stochastic/robust formulations.

## Problem 6 — Sensitivity

If G1 startup cost rises to $1,000, the cost of the current schedule increases by $500. The best alternative that avoids committing G1 in Period 1 is to use G2 for 80 MW in Period 1, then G1 for 100 MW and G2 for 50 MW in Period 2. Its energy cost is $8,500, no-load cost is $180, and startup cost is $1,100, for total $9,780. The original schedule becomes $7,440 and remains cheaper, so commitment does not change under this case.

If Period 2 demand falls to 120 MW, G1 can supply all demand in both periods. The schedule can keep G1 on and avoid starting G2. Costs are energy $1,600 + $2,400 = $4,000, no-load $200, startup $500, total $4,700. G2 remains off.

Commitment decisions are discrete. Small changes in demand, startup cost, or operating constraints can trigger a unit start or shutdown and cause discontinuous changes in dispatch and cost. A more detailed model may improve operational fidelity but increase data requirements, solve time, and risk of false precision. The right formulation depends on the decision being studied.