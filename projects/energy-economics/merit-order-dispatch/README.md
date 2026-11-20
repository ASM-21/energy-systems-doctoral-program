# Computational Lab: Economic Dispatch, Carbon Pricing, and Flexible Demand

**Course:** Y1-02 Energy Economics and Market Fundamentals  
**Level:** Introductory optimization lab  
**Status:** Synthetic single-node teaching case; not a model of any real market or generator fleet.

## Questions

Given inelastic demand and generator marginal costs/capacities, what is least-cost dispatch, the marginal energy price, and emissions? How does a carbon price change the merit order? When does flexible demand reduction compete with generation?

## Model

For generator i, let p_i be generation, c_i marginal fuel/operating cost, e_i emissions rate, and P_i capacity. Let d be flexible demand reduction, tau the carbon price, and k the compensation/opportunity cost of demand response.

    min sum_i (c_i + tau e_i) p_i + k d
    subject to sum_i p_i + d = D
               0 <= p_i <= P_i
               0 <= d <= d_max

The model reports fuel cost, carbon payment, demand-response cost, total objective cost, emissions, and the dual value of the energy-balance constraint. The carbon payment is a modeled transfer; the demand-response cost is an assumed supply price for flexibility. Neither should be confused with a complete social-welfare or retail-rate model.

## Run

    python -m pip install -r requirements.txt
    python dispatch.py --demand 1000
    python dispatch.py --demand 1000 --carbon-price 100
    python dispatch.py --demand 1000 --demand-response-max 200 --demand-response-cost 50
    python dispatch.py --demand 1000 --carbon-price 100 --demand-response-max 200 --demand-response-cost 80
    python -m unittest discover -s . -p "test_*.py" -v

The default dataset is data/generators.csv. Specify another CSV with --generators. All data are synthetic.

## Baseline and experiments

The baseline 1,000 MW dispatch is Unit A 500 MW, Unit B 400 MW, and Unit C 100 MW, with 30,000 USD/hour variable fuel cost and 680 tCO2/hour emissions.

At a carbon price of 100 USD/tCO2, effective costs reorder the fleet. The model dispatches Unit C 300 MW, Unit B 400 MW, and Unit A 300 MW. Emissions fall to 520 tCO2/hour; the energy-balance dual is 110 USD/MWh.

With zero carbon price and flexible demand reduction costing 50 USD/MWh (maximum 200 MW), the model reduces demand by 100 MW. Unit A and B operate at capacity; the next available generator costs 60 USD/MWh, so 50 USD/MWh demand response is selected. The dual is 50 USD/MWh.

## Required analysis

1. Explain the baseline merit order and energy-balance dual.
2. Apply a carbon price and identify when relative emissions rates change dispatch order.
3. Treat demand response as a controllable resource and interpret its marginal bid/cost.
4. Combine carbon pricing and demand response.
5. Explain omitted network constraints, losses, ramp limits, minimum stable generation, start-up costs, reserves, uncertainty, market power, bids, and settlement rules.

## Limitations

This is a single-period, single-node linear program. It is not a production-cost model, unit-commitment model, security-constrained dispatch, PJM LMP simulation, or welfare analysis of a complete carbon policy. The carbon payment is not itself a social resource cost; revenue recycling and distributional effects are not modeled. Demand response is represented by one perfectly dispatchable block with a fixed cost and no baseline measurement, rebound, customer heterogeneity, or performance uncertainty.

## Submission

Commit code, input data, output table/plot, a 1,000–1,500 word analysis, and limitations. Include Python and SciPy versions. Do not describe the model as a real market simulation.
