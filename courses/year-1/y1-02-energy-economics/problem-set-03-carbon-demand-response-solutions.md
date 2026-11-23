# Solution Notes: Carbon Pricing and Flexible Demand

## Problem 1 — Baseline

The least-cost dispatch is Unit A 500 MW, Unit B 400 MW, and Unit C 100 MW. Total variable production cost is 30,000 USD/hour. Emissions are:

- A: 500 × 0.90 = 450 tCO2/hour
- B: 400 × 0.55 = 220 tCO2/hour
- C: 100 × 0.10 = 10 tCO2/hour
- Total: 680 tCO2/hour

Unit C is marginal at 60 USD/MWh, so the energy-balance dual is 60 USD/MWh. This interpretation holds locally while the same marginal unit and LP basis remain valid.

## Problem 2 — Carbon price

At 100 USD/tCO2, effective marginal costs are:

| Unit | Fuel cost (USD/MWh) | Emissions (tCO2/MWh) | Carbon-inclusive cost (USD/MWh) |
|---|---:|---:|---:|
| A | 20 | 0.90 | 110 |
| B | 35 | 0.55 | 90 |
| C | 60 | 0.10 | 70 |

The merit order becomes C, B, A. Dispatch is C 300 MW, B 400 MW, and A 300 MW. Emissions are 30 + 220 + 270 = 520 tCO2/hour, a reduction of 160 tCO2/hour relative to baseline.

Fuel cost is 18,000 + 14,000 + 6,000 = 38,000 USD/hour. Carbon payment is 52,000 USD/hour. The objective cost is 90,000 USD/hour, and Unit A is marginal at 110 USD/MWh.

A carbon price does not necessarily change dispatch order. The result depends on the relative slopes of fuel cost and emissions rates. If emissions rates rise in the same order as fuel costs, a positive carbon price may preserve the order while increasing the marginal price.

## Problem 3 — Demand response

At zero carbon price, generation costs are 20, 35, and 60 USD/MWh. Flexible demand reduction costs 50 USD/MWh. The optimal solution dispatches A at 500 MW, B at 400 MW, C at 0 MW, and reduces demand by 100 MW. Served demand is 900 MW.

Fuel cost is 10,000 + 14,000 = 24,000 USD/hour. Demand-response cost is 5,000 USD/hour. Total objective cost is 29,000 USD/hour and the marginal price is 50 USD/MWh.

The optimum uses 100 MW of demand response, not the full 200 MW capability. The dispatch is A = 500 MW, B = 400 MW, C = 0 MW, and demand response = 100 MW. The served demand is 900 MW. To see why, compare marginal alternatives: after A and B supply 900 MW, the next 100 MW of baseline demand can be met either by Unit C at $60/MWh or by demand response at $50/MWh, so demand response displaces C. Once 100 MW of demand has been reduced, any further reduction would displace some Unit B output, whose marginal cost is $35/MWh. It is not economic to pay $50/MWh for demand response to displace $35/MWh generation. Thus the optimum is 100 MW of demand response. Enabling the first 100 MW of demand response saves $10/MWh relative to serving those MWh with Unit C. Additional demand response beyond 100 MW would displace Unit B at $35/MWh and increase cost by $15/MWh. At the stated 200 MW capability limit, the demand-response upper bound is not binding because only 100 MW is economic; its shadow value for a further increase in the 200 MW cap is therefore zero.

The compensation/opportunity-cost parameter is a simplified supply price for flexibility. It may represent customer opportunity cost, aggregator payment, or an assumed bid, but it is not automatically a retail tariff or an involuntary load-shedding penalty.

## Problem 4 — Combined scenario

At a 100 USD/tCO2 carbon price, generation costs are C 70, B 90, A 110 USD/MWh. Demand response costs 80 USD/MWh. The resource order is C, demand response, B, A. The solution uses C 300 MW, demand response 200 MW, B 400 MW, and A 100 MW. Served demand is 800 MW. Emissions are 340 tCO2/hour. Fuel cost is 34,000 USD/hour, carbon payment 34,000 USD/hour, and demand-response cost 16,000 USD/hour. Total objective cost is 84,000 USD/hour. Unit A is marginal at 110 USD/MWh because the demand-response maximum binds.

## Problem 5 — Interpretation

A carbon price internalizes an assumed per-ton emissions cost into each generator's offer cost. In this simplified model, the payment is treated as a transfer and added to the dispatch objective; actual welfare accounting would distinguish real resource costs from transfers and would specify how revenues are recycled.

Demand response competes with generation when the cost of reducing consumption is lower than the cost of serving the marginal MWh. Actual participation depends on baseline measurement, customer inconvenience, rebound effects, telemetry, dispatchability, performance risk, aggregation rules, and settlement.

The LP's dual is a local marginal value in this model. It is not automatically a retail price or a PJM locational marginal price. The model omits transmission/distribution constraints, losses, reserves, unit commitment, ramping, start-up costs, minimum output, uncertainty, strategic bidding, and detailed demand response baselines. A production-cost or market model would need these features and validation against market rules and data.
