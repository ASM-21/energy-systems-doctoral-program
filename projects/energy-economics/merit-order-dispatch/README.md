# Computational Lab: Economic Dispatch and Marginal Pricing

**Course:** Y1-02 Energy Economics and Market Fundamentals  
**Level:** Introductory optimization lab  
**Status:** Synthetic teaching case; not a model of any real market or generator fleet.

## Question
Given inelastic demand and generator marginal costs/capacities, what is the least-cost dispatch, total variable production cost, emissions, and marginal value of one additional MWh of demand?

## Model

Let generator i produce p_i MW with marginal cost c_i $/MWh, capacity P_i, and emissions rate e_i tCO2/MWh. For a single hour:

    min sum_i c_i p_i
    subject to sum_i p_i = D
               0 <= p_i <= P_i

The Lagrange multiplier on the energy-balance constraint is the marginal system cost for a small increase in demand, provided the local marginal solution remains valid and no discrete/nonconvex constraints are present.

## Run

From this folder:

    python -m pip install -r requirements.txt
    python dispatch.py --demand 1000

The default dataset is data/generators.csv. Specify another CSV with --generators.

## Required analysis

1. Explain why the solution follows merit order in this unconstrained single-node model.
2. Interpret the dual value of the energy-balance constraint.
3. Increase demand in 50 MW increments and identify where the marginal price changes.
4. Add a carbon price by modifying effective marginal costs to c_i + tau e_i. Explain the limitations of constant emissions rates.
5. Explain what is missing relative to an actual wholesale market: network constraints, losses, ramp limits, minimum stable generation, start-up costs, reserves, uncertainty, market power, bids, and settlement rules.

## Submission

Commit code, input data, output table/plot, a 1,000–1,500 word analysis, and limitations. Include Python and SciPy versions. Never describe this one-node linear dispatch model as a full PJM market simulation.