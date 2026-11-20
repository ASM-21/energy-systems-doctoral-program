# Y1-01 Problem Set 2 — Network Models, Power Flow, and DER Constraints

**Instructions:** Use consistent three-phase bases and positive-sequence assumptions. State when an approximation is being used.

## Problem 1 — Three-bus DC power flow

Consider a three-bus network with bus 1 as the reference. Reactances are x12=0.1 pu, x13=0.2 pu, and x23=0.1 pu on a common base. Bus 2 has a 50 MW load; bus 3 has a 50 MW load and a 100 MW generator. Bus 1 has a generator. Ignore losses and use a 100 MVA base.

1. Convert the real-power injections to per unit.
2. Construct the bus susceptance matrix for the DC approximation.
3. Solve for bus voltage angles relative to bus 1.
4. Calculate line flows and identify the direction of each.
5. Explain why the DC approximation does not calculate voltage magnitude, reactive power, or losses.
6. Identify what additional checks would be needed before using the result in a planning decision.

## Problem 2 — Transformer base conversion

A transformer has 8% impedance on a 50 MVA, 115/13.8 kV base. Convert the impedance to a 100 MVA system base while keeping the corresponding voltage bases at the transformer terminals.

Use:

    Z_pu,new = Z_pu,old * (S_base,new/S_base,old) * (V_base,old/V_base,new)^2

1. Calculate the new per-unit impedance.
2. Explain why the voltage-base ratio term is one when bases are changed consistently across transformer terminals.
3. Describe the error that occurs when engineers mix per-unit values on inconsistent bases.

## Problem 3 — DER hosting capacity

A radial feeder has a midday minimum load of 2.5 MW and a proposed PV installation of 4 MW. The PV is located near the feeder end. The utility's simplified screening indicates potential reverse power flow and voltage rise.

1. Explain why comparing PV nameplate rating with minimum feeder load is only a first screen.
2. Identify the data required to evaluate voltage, thermal, protection, and operational constraints.
3. Explain how smart-inverter reactive-power controls may help and what trade-offs they introduce.
4. Explain why hosting capacity is location-, time-, and configuration-dependent.

## Problem 4 — Model selection

Compare AC power flow, DC power flow, short-circuit analysis, and time-series quasi-static simulation. For each, state:
- primary question answered;
- required inputs;
- key assumptions;
- outputs;
- a decision it can inform;
- a major limitation.

## Submission

Submit calculations, a network diagram, a one-page model-selection matrix, and a 1,000-word engineering interpretation.