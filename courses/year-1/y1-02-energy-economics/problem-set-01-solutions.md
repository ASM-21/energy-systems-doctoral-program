# Y1-02 Problem Set 1 — Solution Notes

## Problem 1

From P = 120 - 0.02Q, Q = (120-P)/0.02.

- At $40/MWh: Q = 4,000 MWh.
- At $60/MWh: Q = 3,000 MWh.
- At $80/MWh: Q = 2,000 MWh.

Point elasticity is:

    epsilon = (dQ/dP)(P/Q) = -50(P/Q)

At P=$60 and Q=3,000, epsilon = -1.0. A linear demand curve has constant slope but changing P/Q, so point elasticity varies along the curve.

A fixed charge changes the customer's average bill but not the marginal price of another MWh. A volumetric charge changes the marginal incentive directly. Real responses depend on contract terms, metering, automation, and adjustment costs.

## Problem 2

Set demand equal to supply:

    100 - 0.1Q = 20 + 0.05Q
    Q* = 533.333
    P* = $46.667/MWh

Consumer surplus:

    CS = 0.5 * (100 - 46.667) * 533.333 = $14,222.22

Producer surplus:

    PS = 0.5 * (46.667 - 20) * 533.333 = $7,111.11

Total surplus is $21,333.33.

At P=$40, Qd=600 and Qs=400, so shortage is 200 units. This partial-equilibrium result ignores dispatch feasibility, transmission, time coupling, and reliability constraints.

## Problem 3

External damage = 0.55 * $80 = $44/MWh. Social marginal cost = $35 + $44 = $79/MWh. The assumed Pigouvian carbon price is $80/tCO2.

For generator 2, social marginal cost = $55 + 0.10*80 = $63/MWh. Under these assumptions, generator 2 has lower social marginal cost ($63 versus $79), despite higher private marginal cost. This comparison is illustrative; actual dispatch depends on system constraints and market rules.

Marginal emissions/damages vary with dispatch stack, location, time, fuel, plant efficiency, atmospheric chemistry, exposure, and the valuation method.

## Problem 4

Annual O&M = $2.0 million. The present value of an end-of-year annuity is:

    PV = A * [1 - (1+r)^(-n)] / r

    PV = $2.0m * [1 - (1.05)^(-40)] / 0.05
       ~= $34.28m

Total present cost including initial capital is approximately $134.28m.

This is not automatically a marginal energy price: a substation is a lumpy network asset that provides capacity, reliability, voltage support, and option value. Cost allocation and tariff recovery are regulatory questions. Throughput, coincident peak, beneficiaries, and avoided alternatives matter.

Sensitivity variables include discount rate, capital cost, construction delay, O&M escalation, asset life, load forecast, utilization, equipment replacement, and salvage/decommissioning cost.

## Review standard

Check algebra, signs, units, discounting convention, and whether each economic quantity is private or social. Numerical precision should not imply forecast certainty.