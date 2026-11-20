# Computational Lab: Two-Node Dispatch and Congestion

**Course:** Y1-03 Electricity Markets, Utility Regulation, and PJM  
**Model class:** Lossless two-node economic dispatch LP  
**Data:** Entirely synthetic teaching case

## Objective

Show how a binding transfer constraint can separate nodal marginal prices even when the generation fleet and demand are unchanged. Then relax the line limit and observe the effect of a binding generator capacity constraint.

## Run

    python -m pip install -r requirements.txt
    python dispatch.py
    python -m unittest discover -s . -p "test_*.py" -v

## Baseline

Node 1 has a $20/MWh generator with 150 MW capacity. Node 2 has a $70/MWh generator with 150 MW capacity. Each node has 100 MW demand. The line limit is 50 MW in either direction.

Expected baseline:
- Generation: 150 MW at node 1 and 50 MW at node 2.
- Flow: 50 MW from node 1 to node 2.
- Total cost: $6,500/hour.
- Nodal marginal prices: $20/MWh at node 1 and $70/MWh at node 2.

The line is binding. The price difference is the marginal value of relaxing the transfer constraint in this simplified model.

## Experiment

Increase the line limit to 100 MW. The line is no longer binding, but the node 1 generator remains at its 150 MW capacity. Both nodal marginal prices become $70/MWh because the marginal generator is the node 2 unit.

## Model limitations

This is not a full DC optimal power flow, AC power flow, security-constrained economic dispatch, or unit commitment. It has no voltage angles, susceptances, losses, contingencies, reactive power, reserves, ramping, commitment costs, or uncertainty. Do not interpret it as a PJM price model.

## Required report

Explain the primal dispatch, balance constraints, dual variables, binding constraints, and sensitivity to line/generator capacity. Include a table comparing the 50 MW and 100 MW line cases, and state why the model is pedagogical rather than operational.