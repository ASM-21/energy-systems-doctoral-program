# Solution Notes — Non-Exporting Behind-the-Meter Storage

## Problem 1 — Energy balance

For each interval, grid import plus battery discharge plus PV used onsite must equal load plus battery charging. PV used onsite is PV production minus curtailment. Grid import is bounded below by zero, so the model cannot export. If PV exceeds load and the battery cannot absorb the surplus, the curtailment variable reduces PV output to maintain the meter balance.

## Problem 2 — Storage value

The battery can absorb daytime PV surplus and discharge later, reducing curtailment and/or high-price imports. Its economic value is private bill optimization under the synthetic price profile. The model does not calculate avoided feeder upgrades, voltage support, reliability benefits, or market services. A non-export constraint does not eliminate grid impacts: charging increases net demand and discharging decreases it, changing current and voltage along the feeder.

## Problem 3 — Power and energy

Power capacity limits the instantaneous charge/discharge rate; energy capacity limits how long the battery can sustain that rate. A high-power, low-energy system can absorb short peaks but may fill quickly. A low-power, high-energy system can shift energy over longer intervals but may not capture a brief PV surplus or meet a sharp evening peak. The marginal value of either rating depends on the time coincidence of load, PV, and price.

## Problem 4 — Efficiency and degradation

Lower efficiency increases the energy required to charge the battery for a given discharge and reduces the amount of PV energy shifted. Higher throughput degradation cost discourages cycling and can make marginal cycles uneconomic. A linear throughput penalty omits temperature, depth of discharge, state-of-charge dwell, calendar aging, chemistry, warranty conditions, and replacement cost.

## Problem 5 — Interconnection and policy

A defensible process should specify the operating configuration and credible failure modes. Evidence can include inverter certifications, export-limit settings, protection settings, meter configuration, commissioning tests, fail-safe response to loss of communications or controller failure, and the utility's verification rights. A non-export BTM battery is not identical to an exporting generator, but it can still alter local demand and voltage. The PPL rate-case settlement paragraph 123 calls for review of projects already under review; it does not itself create a new tariff or grant interconnection approval.