# Y1-02 Problem Set 4 — Non-Exporting Behind-the-Meter Storage

**Estimated time:** 3–4 hours  
**Computational lab:** [Non-exporting BTM storage optimization](../../../projects/energy-economics/non-exporting-btm-storage/README.md)  
**Data:** Synthetic 24-hour load, PV, and import-price profile

## Problem 1 — Energy balance and no-export constraint

Run the baseline with no battery and then with the default 80 kW / 160 kWh battery. Verify the interval energy balance and show that grid import is never negative. Explain the economic role of PV curtailment when PV production exceeds onsite load and the battery cannot absorb all surplus.

## Problem 2 — Storage value

Compare grid imports, PV curtailment, PV used onsite, battery charge/discharge, import cost, degradation cost, and total objective cost. Separate bill savings from any distribution-system benefit. Explain why a no-export battery may still change local feeder loading and voltage.

## Problem 3 — Power versus energy

Run four configurations: 40 kW / 160 kWh, 80 kW / 160 kWh, 80 kW / 80 kWh, and 160 kW / 160 kWh. Explain which constraint binds and why power and energy capacity have different marginal values. Do not assume doubling inverter power doubles economic value.

## Problem 4 — Efficiency and degradation

Compare 90%, 95%, and 98% charge/discharge efficiencies. Then compare degradation cost assumptions of $0, $15, and $40/MWh throughput. Explain when cycling is not economic and why throughput degradation is only a rough proxy for electrochemical aging.

## Problem 5 — Interconnection and policy memo

Write a 750–1,000 word memo explaining what a utility would need to verify before approving a non-exporting BTM battery. Address export-limiting controls, inadvertent export, fail-safe behavior, metering, protection, communications loss, commissioning, inverter standards, and the difference between a policy review and an interconnection approval. Use the Pennsylvania casebook's settlement paragraph 124 and PPL's Energy Storage Interconnection Policy as sources. Appendix D cross-references this commitment as paragraph 123; the operative settlement body labels it paragraph 124.

## Deliverables

- Four dispatch outputs and a comparison table.
- Sensitivity plot for power, energy, efficiency, and degradation cost.
- Technical note with energy-balance checks and no-export verification.
- Policy memo with source citations.

## Grading rubric

| Criterion | Weight |
|---|---:|
| Model formulation and energy balance | 20% |
| No-export constraint and curtailment | 20% |
| Storage sensitivity analysis | 25% |
| Interconnection and protection analysis | 25% |
| Reproducibility and source discipline | 10% |