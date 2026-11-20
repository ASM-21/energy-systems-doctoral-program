# Y1-01 Problem Set 5 — Flexible Interconnection and Dynamic Export Envelopes

**Estimated time:** 4–5 hours  
**Computational lab:** [Flexible interconnection and dynamic export envelopes](../../../projects/power-systems/flexible-interconnection/README.md)  
**Data:** Synthetic 24-hour feeder and customer profile.

## Problem 1 — Derive the export envelope

The feeder's physical export limit is 1.0 MW. Existing feeder net export varies by hour. Positive values indicate export; negative values indicate net import.

1. Derive the maximum incremental customer export that can be accommodated in hour t without exceeding the physical limit.
2. Calculate the available headroom for hour 0, hour 13, and hour 14 from the supplied CSV.
3. Explain why a feeder with high existing export can have less incremental DER export headroom even when the new customer's own load is unchanged.
4. Explain why a negative existing feeder net export can create more export headroom than the physical limit alone might suggest.

## Problem 2 — Compare four interconnection arrangements

Run the model for:
- fixed export cap of 0.35 MW;
- scheduled cap of 0.40 MW from 10:00–16:00 and 0.90 MW in other hours;
- dynamic operating envelope based on hourly feeder headroom;
- hypothetical firm upgrade from 1.0 MW to 1.5 MW physical export limit.

For each scenario, report PV available, PV utilized, PV curtailed, grid imports, grid exports, battery throughput, peak customer export, and peak feeder net export.

Explain why the scheduled cap can be more restrictive than dynamic headroom in some hours and less restrictive in others. Identify when the dynamic envelope is more permissive than the fixed cap and when it is more restrictive.

## Problem 3 — Battery dispatch and customer economics

The model includes a 0.5 MW / 1.5 MWh battery with 95% charge/discharge efficiency. It may charge only from available PV and must finish the day at its initial state of charge.

1. Explain how the battery can reduce PV curtailment under a restrictive export cap.
2. Explain why the battery can discharge later to reduce customer imports.
3. Compare PV utilization with battery power set to zero and with the default battery.
4. Increase battery energy to 3.0 MWh while keeping power at 0.5 MW. Explain why additional energy capacity may have little value if power or export headroom is the binding constraint.
5. Vary import price, export price, and degradation cost. Explain how the customer-optimal dispatch changes and why a customer objective may differ from a utility objective.

## Problem 4 — Flexible connection versus physical upgrade

The firm-upgrade scenario increases the feeder export limit to 1.5 MW. The model does not include upgrade capital cost.

1. Compare the PV utilization and curtailment outcomes of the upgrade and dynamic-envelope scenarios.
2. Identify the information needed to compare the present value of an upgrade with the customer costs and curtailment risk of flexible interconnection.
3. Explain who bears the risk of curtailment, forecast error, communications failure, and equipment incompatibility under each arrangement.
4. Propose a minimum set of customer protections and operating rules for a real dynamic export envelope.

## Problem 5 — Engineering limitations and regulatory memo

Write a 1,000–1,500 word memo answering: under what conditions should a utility offer a flexible export envelope instead of requiring a distribution upgrade?

Your memo must distinguish:
- static export limits;
- scheduled export limits;
- dynamic operating envelopes;
- actively managed interconnection;
- physical upgrades.

Discuss voltage, thermal, protection, phase imbalance, forecast error, telemetry, fail-safe behavior, curtailment priority, compensation, customer notice, and dispute resolution. Explain why this lab is not an AC power-flow or hosting-capacity study.

## Deliverables

- Reproducible scenario summary and hourly dispatch CSVs.
- Sensitivity table for PV size, battery energy, and export-envelope uncertainty.
- Export-envelope plot and PV-curtailment comparison.
- Policy memo with an explicit cost/risk allocation framework.

## Grading rubric

| Criterion | Weight |
|---|---:|
| Export-headroom derivation and interpretation | 20% |
| Optimization formulation and results | 25% |
| Battery and customer economics | 20% |
| Upgrade/flexible-interconnection comparison | 20% |
| Engineering limitations and policy analysis | 15% |
