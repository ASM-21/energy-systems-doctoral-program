# Y1-01 Problem Set 2 — Solution Guidance

## Problem 1

The specified dispatch is 40 MW at bus 1 and 60 MW at bus 3. Loads are 50 MW at buses 2 and 3. On a 100 MVA base:

    P1 = +0.4 pu
    P2 = -0.5 pu
    P3 = +0.1 pu

The injections sum to zero. With bus 1 as reference, branch susceptances are 1/x12=10, 1/x13=5, and 1/x23=10 pu. The reduced DC susceptance matrix for buses 2 and 3 is:

    B_red = [[20, -10],
             [-10, 15]]

Solve B_red * [theta2, theta3]' = [-0.5, 0.1]'. The result is:

    theta2 = -0.0325 rad
    theta3 = -0.0150 rad

Using flow i-to-j = (theta_i-theta_j)/x_ij:

- Flow 1 to 2: 0.325 pu = 32.5 MW.
- Flow 1 to 3: 0.075 pu = 7.5 MW.
- Flow 2 to 3: -0.175 pu = -17.5 MW, i.e. 17.5 MW from bus 3 to bus 2.

Check balances: bus 2 receives 32.5+17.5=50 MW; bus 3's 60 MW generation supplies its 50 MW load and exports 10 MW net (7.5 MW to bus 1 and 17.5 MW to bus 2), while bus 1 exports 40 MW. The network balances.

The DC approximation uses fixed voltage magnitudes, small angle differences, lossless branches, and a simplified relationship between active power and angles. It does not calculate voltage magnitude, reactive power, or losses.

## Problem 2

The voltage bases are changed consistently with the transformer ratio, so the voltage-base ratio term is one. The new impedance is:

    Z_pu,new = 0.08 * (100/50) = 0.16 pu

The physical ohmic impedance has not changed. Only its per-unit representation on the selected system base changes.

## Problem 3

Minimum load and DER nameplate do not determine feeder voltage or thermal headroom. Required information includes feeder topology and impedances, conductor and transformer ratings, regulator/capacitor controls, time-series load and DER output, phase imbalance, protection settings, fault current, existing DER, switching states, and applicable operating criteria.

Inverter reactive-power absorption can reduce voltage rise in some conditions but may increase current and losses, consume inverter capability, and affect real-power output depending on the control mode and operating point. Hosting capacity depends on location, time, topology, operating assumptions, and the violation criteria used.

## Problem 4

AC power flow solves nonlinear steady-state voltage magnitude and angle, real/reactive flows, and losses under specified controls. DC power flow approximates active-power/angle behavior under restrictive assumptions. Short-circuit analysis estimates fault currents for protection/equipment duty. Time-series quasi-static simulation evaluates evolving operating conditions and control interactions over many time steps. None alone establishes all aspects of interconnection feasibility.
