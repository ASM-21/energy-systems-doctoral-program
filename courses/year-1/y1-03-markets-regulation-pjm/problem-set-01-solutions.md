# Y1-03 Problem Set 1 — Solution Notes

## Problem 1

Dispatch A at 100 MW, B at 100 MW, and C at 50 MW. The marginal unit is C, so the simplified uniform clearing price is $60/MWh. Total variable cost:

    100*20 + 100*35 + 50*60 = $8,500/hour

The price is the marginal value of another MWh in this simplified market; inframarginal units receive the same market price even though their offer costs differ. Actual settlement depends on market design and uplift/commitment rules. Omitted features include network constraints, losses, ramping, minimum run levels, start-up costs, reserves, uncertainty, demand response, market power, and offer mitigation.

## Problem 2

Let f be positive flow from node 1 to node 2. Nodal balances:

    g1 - f = 100
    g2 + f = 100
    0 <= g1 <= 250, 0 <= g2 <= 150
    -50 <= f <= 50

The cheap generator at node 1 is dispatched to 150 MW, the line carries 50 MW, and the expensive generator at node 2 produces 50 MW. Total cost is $6,500/hour. The node 1 marginal price is $20/MWh; node 2 marginal price is $70/MWh. The $50/MWh difference is the shadow value of the binding transfer limit in this simplified lossless model. Node 1's generator has spare capacity, so one additional MW of node 1 demand can be served locally at $20/MWh. One additional MW of node 2 demand requires an additional MW from the $70/MWh local generator because the line is at its 50 MW transfer limit.

If line capacity rises to 150 MW, the line is no longer binding at the optimal 100 MW transfer. The low-cost node 1 generator supplies all 200 MW of system demand, node 2 generation falls to zero, and 100 MW flows from node 1 to node 2. Both nodal marginal prices are $20/MWh. The node 1 generator's 250 MW capacity is sufficient to serve one additional MW, and the line has 50 MW of unused transfer capability. This comparison isolates the effect of congestion without simultaneously binding the cheap generator's capacity.

A full security-constrained model would include network topology and contingencies, AC power-flow/voltage constraints or a validated approximation, reserve requirements, unit commitment, ramping, uncertainty, losses, and market settlement rules.

## Problem 3

A defensible answer identifies the controlling statute/regulation/order and jurisdictional boundary, not simply the agency name. FERC generally regulates interstate wholesale sales and transmission under the Federal Power Act, while states retain important authority over retail rates, local distribution, and facility siting subject to federal preemption and specific statutory exceptions. NERC develops reliability standards subject to FERC approval; RTOs administer approved tariffs and market rules. The exact classification depends on the asset, transaction, and governing authority.

## Problem 4

Answers vary. A valid submission must cite the exact controlling version and distinguish binding tariff/order language from explanatory manual prose, stakeholder materials, and commentary.

## Important correction

The two-node exercise is a stylized economic dispatch problem, not a complete DC optimal power flow. It has a single transfer constraint and no network susceptance or nodal angle equations. The nodal-price interpretation follows from the constrained optimization formulation, not from a full AC network model.