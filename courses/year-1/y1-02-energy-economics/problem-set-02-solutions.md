# Y1-02 Problem Set 2 — Solution Notes

## Problem 1

Let c_t and d_t be grid-side charge and discharge MW over one-hour intervals; s_t is stored MWh. A valid model is:

    s_t = s_(t-1) + 0.9*c_t - d_t/0.9
    0 <= s_t <= 10
    0 <= c_t <= 5
    0 <= d_t <= 5
    s_0 = s_4 = 0

Maximize sum_t price_t*(d_t-c_t), subject to the constraints. If simultaneous charging/discharging is prohibited, add binary variables or use a justified condition that makes simultaneous operation suboptimal in the given price-taking case.

One optimal schedule is charge 5 MWh in hour 1 and 5 MWh in hour 2, then discharge 3.1 MWh in hour 3 and 5 MWh in hour 4. Stored energy reaches 9 MWh, falls to approximately 5.556 MWh after hour 3, and returns to zero after hour 4. Purchased energy is 10 MWh; delivered energy is 8.1 MWh. The 5 MW discharge limit is fully used in the highest-price hour, so the remaining energy is discharged in hour 3. Gross margin:

    3.1*80 + 5*100 - 5*20 - 5*30 = $498

Round-trip efficiency is 0.9*0.9=0.81. With a $15/MWh throughput cost applied to both charging and discharging throughput, degradation cost is $271.50 if throughput is defined as 10+8.1 MWh, leaving $226.50. State the throughput convention because commercial degradation models may use equivalent full cycles or cell-side throughput.

The model omits degradation nonlinearity, state-of-health, ancillary services, forecast error, imbalance settlement, taxes, network constraints, interconnection limits, market participation rules, and financing.

## Problem 2

LCOE is a discounted average cost per unit of generated energy under specified assumptions. It does not directly value dispatchability, timing, locational congestion, capacity contribution, ramping, flexibility, reliability, curtailment, or integration cost. Comparisons require consistent system boundaries, financing, lifetime, and fuel/carbon assumptions.

## Problem 3

NPV is:

    NPV = -50 + 8 * [1-(1.07)^(-10)]/0.07
        ~= $6.19 million

At 5%, NPV is approximately $11.77 million. At 10%, NPV is approximately -$0.84 million. Results are sensitive to the discount rate and cash-flow assumptions. Construction delay postpones benefits and may add financing costs; overruns increase initial investment; price and policy uncertainty change expected cash flows and risk. Real options matter when management can stage, defer, expand, or abandon investment as information arrives.

Check calculations with a spreadsheet or script and document whether cash flows are nominal or real and whether the discount rate is consistent.