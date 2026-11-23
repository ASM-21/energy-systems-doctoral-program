# Problem Set 2: Three-Bus DC Optimal Power Flow and Locational Marginal Prices

**Level:** Advanced graduate  
**Suggested effort:** 4–5 hours  
**Prerequisites:** Y2-04 Problem Set 1, Y1-01 DC power flow, linear algebra, and constrained optimization

This assignment combines network physics and economic dispatch in a lossless DC optimal power-flow (DC-OPF) model. The network and offers are synthetic. All power quantities are MW, angles are radians, reactances are per unit, and the system base is 100 MVA.

## Case: Three-bus network

The network is triangular:

| Branch | Series reactance | Thermal limit |
|---|---:|---:|
| 1–2 | 0.10 pu | 60 MW |
| 1–3 | 0.20 pu | 60 MW |
| 2–3 | 0.10 pu | 60 MW |

Bus 1 is the reference bus with angle zero. Each bus has one generator:

| Generator | Bus | Offer | Maximum output |
|---|---:|---:|---:|
| G1 | 1 | $20/MWh | 150 MW |
| G2 | 2 | $50/MWh | 100 MW |
| G3 | 3 | $80/MWh | 100 MW |

Demand is 100 MW at bus 2 and 100 MW at bus 3. Bus 1 demand is zero. Generators have zero minimum output. Ignore reserves, losses, contingencies, ramping, startup costs, and reactive power.

For each branch i–j, define flow from i to j as:

`f_{ij} = S_{base}(θ_i-θ_j)/x_{ij}`

where S_base = 100 MVA. Use the same orientation consistently in nodal balances and line limits.

## Problem 1 — DC network formulation

1. Construct the bus susceptance matrix B' from the branch reactances.
2. Write the nodal injection equation P = B'θ.
3. Remove the reference-bus angle and express the remaining equations in terms of θ2 and θ3.
4. Write each branch flow equation in MW and impose the two-sided thermal limit.
5. Explain the assumptions behind the DC approximation and identify what physical quantities it does not represent.

## Problem 2 — DC-OPF primal formulation

1. Formulate the least-cost dispatch objective.
2. Define the three nodal power-balance constraints using generation, demand, and network injections.
3. Include generator bounds and branch thermal limits.
4. Explain why the reference-bus angle is fixed and why the system-wide energy-balance equation alone is insufficient.
5. Identify which constraints are linear and explain why this formulation is a linear program.

## Problem 3 — Solve and interpret the dispatch

Solve the DC-OPF.

Report:
- generator outputs;
- bus voltage angles;
- branch flows and directions;
- binding and nonbinding line constraints;
- total production cost;
- nodal marginal prices.

Verify each nodal balance independently. Do not rely only on the solver's success flag.

## Problem 4 — Dual values and finite-difference checks

1. Interpret the dual value of each nodal balance as a local marginal cost of serving an additional MW at that bus.
2. Identify the shadow value of the binding 1–2 line limit.
3. Increase the 1–2 line limit by 1 MW and calculate the change in optimal cost.
4. Increase bus 2 demand by 1 MW and calculate the change in optimal cost.
5. Increase bus 3 demand by 1 MW and calculate the change in optimal cost.
6. Reconcile finite differences with the relevant dual values. Explain why the line-limit shadow price is not simply the difference between two selected nodal prices.
7. State the range over which the reported duals are valid and explain how an active-set change can alter them.

## Problem 5 — Congestion and network topology

1. Increase the 1–2 line limit to 61 MW and compare dispatch, flows, cost, and nodal prices with the base case.
2. Explain which generator is displaced when the line constraint is relaxed.
3. Discuss why a line's economic value depends on network topology and power-transfer distribution factors, not only on the line's own reactance or the distance between buses.
4. Explain why a binding line does not necessarily imply that the two endpoints have the largest LMP difference in a meshed network.
5. Identify the additional work required to move from this DC-OPF to an AC or security-constrained OPF.

## Problem 6 — Model-risk and market translation

Prepare a 500–800 word note explaining:
- what the DC-OPF establishes;
- what it does not establish about voltage, reactive power, losses, contingencies, stability, or protection;
- how actual market offers, commitment, uplift, losses, and settlement rules may differ from this model;
- why a nodal dual is not automatically a participant's complete settlement price;
- which PJM tariff/manual sections and version dates you would need before interpreting an actual market event.

## Submission

Submit the derivation, a reproducible LP implementation, a node/branch results table, a finite-difference validation table, and the model-risk note. Include a sign convention and units for every dual variable.

## Evaluation

Network formulation and units (20%), primal dispatch and balance validation (20%), dual and finite-difference reasoning (25%), congestion/topology analysis (15%), market translation and model limitations (10%), reproducibility (10%).