# Solution Notes: Three-Bus DC Optimal Power Flow and Locational Marginal Prices

The calculations below use the stated 100 MVA base and a lossless DC approximation. They are a synthetic benchmark, not an AC validation or PJM market result.

## Problem 1 — Network formulation

The branch susceptances are 10, 5, and 10 pu for lines 1–2, 1–3, and 2–3. With bus order 1, 2, 3:

`B' = [[15, -10, -5], [-10, 20, -10], [-5, -10, 15]]`

The DC injection equation is `P = S_base B' θ`, with S_base = 100 MVA and θ1=0. Therefore:

- Bus 1: `P1 = -1000 θ2 - 500 θ3`.
- Bus 2: `P2 = 2000 θ2 - 1000 θ3`.
- Bus 3: `P3 = -1000 θ2 + 1500 θ3`.

Flows oriented from the lower-numbered to higher-numbered bus are:
- `f12 = -1000 θ2`.
- `f13 = -500 θ3`.
- `f23 = 1000(θ2 - θ3)`.

Each flow must lie between -60 and +60 MW. The DC model assumes fixed voltage magnitudes, small angle differences, lossless branches, and a balanced positive-sequence representation. It does not solve reactive power, voltage magnitude, nonlinear losses, or AC feasibility.

## Problem 2 — Primal formulation

Minimize:

`20g1 + 50g2 + 80g3`

subject to nodal balances:

`g1 = -1000θ2 - 500θ3`

`g2 - 100 = 2000θ2 - 1000θ3`

`g3 - 100 = -1000θ2 + 1500θ3`

generator bounds:

`0≤g1≤150, 0≤g2≤100, 0≤g3≤100`

and branch limits:

`-60≤-1000θ2≤60`

`-60≤-500θ3≤60`

`-60≤1000(θ2-θ3)≤60`.

All constraints and the objective are linear in the decision variables. Fixing θ1=0 removes the arbitrary angle reference and makes the reduced network equations nonsingular for a connected network. A single aggregate energy balance would not enforce the location-specific injection/withdrawal pattern or line limits.

## Problem 3 — Base dispatch

The optimum is:

| Quantity | Result |
|---|---:|
| G1 at bus 1 | 113.333 MW |
| G2 at bus 2 | 86.667 MW |
| G3 at bus 3 | 0 MW |
| θ1 | 0 rad |
| θ2 | -0.060000 rad |
| θ3 | -0.106667 rad |
| Flow 1→2 | 60.000 MW |
| Flow 1→3 | 53.333 MW |
| Flow 2→3 | 46.667 MW |
| Objective | $6,600/hour |

Line 1–2 binds at its positive thermal limit. Lines 1–3 and 2–3 are below their limits.

Nodal balance checks:
- Bus 1 injects 113.333 MW and exports 60 + 53.333 = 113.333 MW.
- Bus 2 has net injection 86.667 - 100 = -13.333 MW. It receives 60 MW and exports 46.667 MW, a net import of 13.333 MW.
- Bus 3 has net injection -100 MW and imports 53.333 + 46.667 = 100 MW.

Production cost:

`113.333×20 + 86.667×50 = $6,600/hour`.

The nodal balance duals are:
- Bus 1: $20/MWh.
- Bus 2: $50/MWh.
- Bus 3: $40/MWh.

These values can be verified by perturbing each nodal demand by a small amount while the active set remains unchanged.

## Problem 4 — Dual values and finite differences

The 1–2 line's positive-direction upper limit has a shadow value of $40 per hour per additional MW of transfer capability. Relaxing that limit from 60 to 61 MW changes the optimal cost from $6,600/hour to $6,560/hour, a $40/hour reduction.

Demand perturbations:
- Bus 2 demand from 100 to 101 MW increases cost from $6,600 to $6,650/hour: $50/MWh, matching the bus 2 LMP.
- Bus 3 demand from 100 to 101 MW increases cost from $6,600 to $6,640/hour: $40/MWh, matching the bus 3 LMP.

The line shadow price is the marginal value of relaxing one specific branch constraint. Nodal prices are marginal values of demand at nodes. In a meshed network, a line-limit change affects flows at multiple branches according to network sensitivities, so its shadow price is not generally equal to a simple difference between two selected nodal prices.

The duals are local. The reported values remain valid only while the relevant active set and model assumptions remain unchanged. A sufficiently large demand or capacity change can alter the marginal generator, congestion pattern, or binding constraints.

## Problem 5 — Relaxed line limit

With the 1–2 limit raised to 61 MW, the optimum becomes:
- G1 = 114.667 MW.
- G2 = 85.333 MW.
- G3 = 0 MW.
- θ2 = -0.061000 rad.
- θ3 = -0.107333 rad.
- Flow 1→2 = 61.000 MW.
- Flow 1→3 = 53.667 MW.
- Flow 2→3 = 46.333 MW.
- Cost = $6,560/hour.
- Nodal prices remain $20/MWh at bus 1, $50/MWh at bus 2, and $40/MWh at bus 3 over this one-MW change.

The additional transfer capability permits more low-cost generation at bus 1 to displace generation at bus 2. The $40/MW-hour shadow value matches the observed cost reduction. In a meshed network, injections and withdrawals distribute across multiple paths. PTDFs and the set of binding constraints determine congestion effects; physical distance or one branch's reactance alone is not sufficient.

## Problem 6 — Market translation

A strong note distinguishes the mathematical optimization result from real market operation. The DC-OPF provides a least-cost dispatch under its stated linear network approximation and constraints. It does not establish AC voltage feasibility, reactive-power adequacy, losses, N-1 security, transient stability, protection coordination, or actual equipment ratings.

Actual wholesale market outcomes depend on offers, commitment decisions, operating constraints, reserve requirements, losses, scarcity rules, market power mitigation, uplift, and settlement protocols. A nodal dual from this model is a local marginal value under a particular formulation, not a complete participant settlement. Any PJM application requires version-controlled review of the tariff, manuals, product definitions, and effective dates.