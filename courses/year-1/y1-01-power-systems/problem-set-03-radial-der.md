# Y1-01 Applied Problem Set: Radial Feeder DER Integration

**Estimated time:** 3–4 hours  
**Inputs:** [Radial feeder lab](../../../projects/power-systems/radial-der-hosting-capacity/README.md)  
**Data:** Synthetic, four-bus, balanced radial feeder

Use the provided feeder inputs and code. Show equations, units, intermediate calculations, and assumptions. Round per-unit voltages to six decimals and apparent power to three decimals unless otherwise stated.

## Problem 1 — Baseline branch quantities

With no DER connected, calculate downstream real and reactive power on branches 1–2, 2–3, and 2–4. Calculate apparent power on each branch and determine whether any branch violates its thermal rating.

## Problem 2 — Approximate voltage profile

Using the voltage-drop equation in the lab, calculate the voltage at buses 2, 3, and 4 for the baseline case. Explain why the slack bus remains at 1.0 pu and why the maximum voltage reported by the program may therefore equal exactly 1.0 pu even when all load buses are below nominal.

## Problem 3 — DER penetration and reverse flow

Place a unity-power-factor PV resource at bus 4. Determine the minimum PV output at which:
1. branch 2–4 begins to experience reverse real-power flow;
2. branch 1–2 begins to experience reverse real-power flow.

Explain why the two thresholds differ.

## Problem 4 — Binding screening constraint

Run the model at 800 kW and 900 kW of PV at bus 4. Identify the first thermal constraint to bind. Calculate the apparent power on branch 2–4 at both levels and compare it with the 0.80 MVA limit. Explain why the first violation is not equivalent to a utility hosting-capacity determination.

## Problem 5 — Voltage and thermal constraints are distinct

Run the sweep through 5,000 kW. Identify the first voltage-band violation and the first thermal violation. Explain why the first binding criterion depends on the chosen model and feeder data. Discuss at least two additional criteria that could bind in a real interconnection study.

## Problem 6 — Sensitivity and model criticism

Perform at least three controlled sensitivities:
- move the DER from bus 4 to bus 3;
- increase or decrease one branch resistance by 25%;
- increase all load P and Q by 25%.

For each, report the change in the first screened violation and explain the physical mechanism. Then identify at least five limitations of this model and propose a validation plan using a published distribution test feeder and an AC-capable solver.

## Deliverables

- A reproducible notebook or script output.
- A table of baseline and DER scenario results.
- One voltage-versus-PV penetration figure.
- A 750–1,000 word engineering memo.
- A limitations section that distinguishes screening results from operational findings.

## Grading rubric

| Criterion | Weight |
|---|---:|
| Power aggregation, units, and calculations | 25% |
| Voltage and thermal interpretation | 20% |
| Reproducible computational work | 20% |
| Sensitivity analysis | 15% |
| Model limitations and validation plan | 20% |

Do not use employer or customer data. Do not describe this synthetic feeder as representative of a PPL circuit.
