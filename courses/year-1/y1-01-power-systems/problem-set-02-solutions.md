# Y1-01 Problem Set 2 — Solution Guidance

## Problem 1

The bus injections are P2=-0.5 pu and P3=+0.5 pu if the bus 3 generator supplies its local 50 MW load plus 50 MW export. Bus 1 balances the system. This statement must be reconciled with the actual dispatch assumption: specify whether the bus 3 generator output is 100 MW or whether 100 MW is its capacity. If it is 100 MW output, the net bus 3 injection is +0.5 pu; bus 1 supplies the remaining network balance.

For the DC model, form B' from branch susceptances 1/x. With bus 1 reference, solve the reduced system:

    B'_red * theta_red = P_red

Branch flow from i to j is approximately (theta_i - theta_j)/x_ij. Check that flows satisfy nodal balances and that the sum of injections is zero.

A numerical solution is intentionally not supplied until the dispatch interpretation is fixed. This is a modeling lesson: a network problem is not well-posed if generator output, capacity, and local load are conflated.

## Problem 2

The voltage bases are changed consistently with the transformer ratio, so the voltage-base ratio term is one. The new impedance is:

    Z_pu,new = 0.08 * (100/50) = 0.16 pu

The physical ohmic impedance has not changed. Only its per-unit representation on the selected system base changes.

## Problem 3

Minimum load and DER nameplate do not determine feeder voltage or thermal headroom. Required information includes feeder topology and impedances, conductor and transformer ratings, regulator/capacitor controls, time-series load and DER output, phase imbalance, protection settings, fault current, existing DER, switching states, and applicable operating criteria.

Inverter reactive-power absorption can reduce voltage rise in some conditions but may increase current and losses, consume inverter capability, and affect real-power output depending on the control mode and operating point. Hosting capacity depends on location, time, topology, operating assumptions, and the violation criteria used.

## Problem 4

AC power flow solves nonlinear steady-state voltage magnitude and angle, real/reactive flows, and losses under specified controls. DC power flow approximates active-power/angle behavior under restrictive assumptions. Short-circuit analysis estimates fault currents for protection/equipment duty. Time-series quasi-static simulation evaluates evolving operating conditions and control interactions over many time steps. None alone establishes all aspects of interconnection feasibility.

## Instructor/learner note

Problem 1 is deliberately a model-formulation checkpoint. Before solving, clarify whether generator output is fixed, bounded, or decision-variable and specify the reference-bus balancing convention. Revise the problem statement in the submission and explain the chosen formulation.