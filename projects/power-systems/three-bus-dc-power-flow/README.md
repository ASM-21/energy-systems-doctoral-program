# Computational Lab: Three-Bus DC Power Flow

**Course:** Y1-01 Power Systems and Electricity Infrastructure  
**Model:** Lossless DC power-flow approximation  
**Inputs:** Synthetic network data

## Objective

Implement a transparent DC power-flow solver from bus injections and branch reactances. The exercise builds on the three-phase and per-unit problem sets and makes network topology explicit.

## Run

    python -m pip install -r requirements.txt
    python dc_power_flow.py
    python -m unittest discover -s . -p "test_*.py" -v

## Model

For each branch i-j with series reactance x_ij:

    f_ij = (theta_i - theta_j) / x_ij

On a common per-unit base, assemble the bus susceptance matrix B' and solve:

    B' * theta = P

after removing the slack-bus row and column. Branch flow in MW is the per-unit flow multiplied by system base MVA.

## Default case

The 100 MVA three-bus case has injections +40 MW at bus 1, -50 MW at bus 2, and +10 MW at bus 3. Branch reactances are 0.1, 0.2, and 0.1 pu for lines 1-2, 1-3, and 2-3.

Expected angles with bus 1 as reference:
- Bus 1: 0 rad.
- Bus 2: -0.0325 rad.
- Bus 3: -0.0150 rad.

Expected flows:
- 1 to 2: 32.5 MW.
- 1 to 3: 7.5 MW.
- 3 to 2: 17.5 MW.

## Required analysis

1. Derive the B' matrix from branch susceptances.
2. Explain the role of the slack bus.
3. Verify nodal power balance and line-flow sign conventions.
4. Add thermal limits and report violations; do not imply the solver enforces them.
5. Change a branch reactance and explain how flow redistributes.
6. Explain why DC power flow does not establish voltage magnitude, reactive-power feasibility, losses, fault duty, or AC convergence.

## Limitations

This implementation assumes a connected network, positive branch reactances, fixed topology, balanced positive-sequence conditions, small angle differences, fixed voltage magnitudes, and no losses. It is not an AC power-flow solver, contingency analysis, protection study, or utility planning tool.