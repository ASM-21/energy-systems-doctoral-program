# Solution Notes: Energy and Operating-Reserve Co-Optimization

The model is a one-hour, single-node convex LP. Results are conditional on the synthetic offers, capacity constraints, and absence of network and intertemporal restrictions.

## Problem 1 — Primal formulation

For each unit i, choose energy p_i and upward reserve r_i:

`min Σ_i(c_i p_i + q_i r_i)`

subject to:

`Σ_i p_i = D`

`Σ_i r_i ≥ R`

`p_i + r_i ≤ K_i`

`p_i ≥ 0, r_i ≥ 0`.

A MW of capacity awarded as reserve is held as headroom and cannot also be dispatched as energy in the same interval. Joint capacity constraints are therefore necessary.

## Problem 2 — Benchmark solution

| Unit | Energy | Reserve | Total award | Capacity |
|---|---:|---:|---:|---:|
| A | 80 MW | 0 MW | 80 MW | 80 MW |
| B | 70 MW | 0 MW | 70 MW | 70 MW |
| C | 10 MW | 20 MW | 30 MW | 50 MW |

Energy balance is 80+70+10=160 MW. Reserve awards total 20 MW. Joint capacity is respected for every unit.

Objective:

`80×18 + 70×32 + 10×55 + 20×2 = $4,270`

The energy-only dispatch is also A=80, B=70, C=10 in this benchmark, but reserve is assigned to C. This coincidence is specific to the offers and capacities. The reserve award consumes 20 MW of C's headroom. A different reserve offer or tighter capacity can cause the joint optimization to change energy dispatch.

## Problem 3 — Lagrangian and duals

Use:

`L = Σ_i(c_i p_i + q_i r_i) + λ(D-Σ_i p_i) + ρ(R-Σ_i r_i) + Σ_i μ_i(p_i+r_i-K_i) - Σ_i α_i p_i - Σ_i β_i r_i`

with `ρ, μ_i, α_i, β_i ≥ 0`.

Stationarity:

`c_i - λ + μ_i - α_i = 0`

`q_i - ρ + μ_i - β_i = 0`.

At the optimum, C has positive energy and reserve awards and unused capacity, so μ_C = α_C = β_C = 0. Therefore λ = 55 USD/MWh and ρ = 2 USD/(MW·h).

A and B are at their joint capacity limits with positive energy and zero reserve. Their capacity shadow values are:
- A: μ_A = λ - c_A = 55 - 18 = 37 USD/(MW·h).
- B: μ_B = λ - c_B = 55 - 32 = 23 USD/(MW·h).
- C: μ_C = 0.

The lower-bound multipliers for reserve on A and B are positive, reflecting that reserve is not economic for those units at the benchmark offers after accounting for their capacity opportunity cost. For A, β_A = q_A - ρ + μ_A = 8 - 2 + 37 = 43; for B, β_B = 5 - 2 + 23 = 26.

The energy dual is the marginal system cost of one additional MW of energy demand. The reserve dual is the marginal system cost of one additional MW of reserve requirement, over the local range where the same basis remains optimal. Capacity shadow values measure the benefit of one additional MW of a unit's joint energy/reserve capability. A constraint can bind with zero shadow value when relaxing it does not improve the objective at the margin, as for C.

## Problem 4 — Finite differences

- Demand 161 MW: the marginal energy unit C increases from 10 to 11 MW. Objective rises by $55 for the interval.
- Reserve 21 MW: C increases reserve from 20 to 21 MW. Objective rises by $2 for the interval.
- A capacity 81 MW: one additional MW from A displaces one MW from C. Objective falls by $37 for the interval.

These match the local dual values. At 150 MW demand, A=80 and B=70 exactly meet demand, while C is at zero output. The marginal cost function has a kink: reducing demand can displace B, while increasing demand starts C. The energy dual may therefore be non-unique at that point.

## Problem 5 — Sequential versus joint procurement

With reserve offers A=100, B=1, C=50:
- Energy-only dispatch remains A=80, B=70, C=10 MW.
- A and B have no headroom after energy dispatch. C has 40 MW headroom, so sequential reserve procurement awards 20 MW to C.
- Sequential objective is energy cost $4,230 plus reserve cost $1,000 = $5,230 for the interval.

Joint optimization can move 20 MW of energy from B to C, then award 20 MW reserve to B:
- A: 80 MW energy, 0 reserve.
- B: 50 MW energy, 20 MW reserve.
- C: 30 MW energy, 0 reserve.

Joint objective:
- Energy: `80×18 + 50×32 + 30×55 = $4,690`.
- Reserve: `20×1 = $20`.
- Total: **$4,710 for the interval**.

Joint procurement saves $520 relative to sequential procurement. It accepts an additional $460 of energy cost by shifting 20 MW from B to C, but saves $980 of reserve cost by moving the reserve award from C to B. The net saving is $520. The result illustrates the opportunity cost of capacity and the value of simultaneous optimization.

## Problem 6 — Market translation

A strong note distinguishes product purpose, response speed, duration, deliverability, telemetry, and performance requirements. Upward operating reserve is capacity that can respond when called; it is not the same product as energy already dispatched, frequency regulation, or long-term capacity/resource adequacy. A single-node model ignores transmission deliverability and reserve-zone constraints. Real market rules also specify eligible resources, qualification, response and sustainment requirements, performance scoring, scarcity treatment, and settlement. The synthetic reserve dual is not an actual PJM reserve clearing price.