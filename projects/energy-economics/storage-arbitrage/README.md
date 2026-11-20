# Computational Lab: Battery Arbitrage and Intertemporal Optimization

**Course:** Y1-02 Energy Economics and Market Fundamentals  
**Model:** Deterministic single-node linear program  
**Input prices:** Synthetic teaching vector; not actual market prices

## Objective

Model the intertemporal value of storage. Unlike a generator, a battery shifts energy across time and is constrained by charging/discharging power, energy capacity, efficiency, and terminal state of charge.

## Run

    python -m pip install -r requirements.txt
    python dispatch.py
    python dispatch.py --degradation-cost 15
    python -m unittest discover -s . -p "test_*.py" -v

## Model

For each interval t:

    s_t = s_(t-1) + eta_charge*c_t - d_t/eta_discharge

Maximize:

    sum_t [price_t*(d_t-c_t) - degradation_cost*(c_t+d_t)]

subject to power limits, state-of-charge limits, and initial/final state of charge. The model assumes nonnegative prices, a price-taking battery, and no simultaneous charging/discharging. Under these assumptions and efficiencies below or equal to one, simultaneous operation is not profitable in the continuous relaxation.

## Default case

Prices: $20, $30, $80, and $100/MWh. Battery energy capacity 10 MWh, charge/discharge power limit 5 MW, charging and discharging efficiencies 90%, and initial/final state of charge zero.

The optimal schedule charges 5 MWh in each of the first two intervals, discharges 3.1 MWh at $80/MWh, and discharges 5 MWh at $100/MWh. Gross arbitrage margin is $498. This is higher than discharging evenly because the power limit makes the highest-price interval more valuable.

## Required analysis

1. Interpret the state-of-charge recursion and terminal constraint.
2. Compare gross margin with degradation-adjusted margin.
3. Change energy capacity and power limits separately.
4. Vary charging/discharging efficiency.
5. Add an additional price interval and test price forecast errors.
6. Explain why a deterministic arbitrage LP omits ancillary services, reserve obligations, network constraints, bidding, imbalance settlement, taxes, degradation physics, and market participation rules.

## Submission

Include dispatch and state-of-charge tables, sensitivity figures, unit tests, and a 1,000-word explanation. Distinguish gross arbitrage margin from total project economics.