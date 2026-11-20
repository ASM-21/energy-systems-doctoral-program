# Solution Notes — Flexible Interconnection and Dynamic Export Envelopes

## Problem 1 — Export envelope

If the feeder's physical export limit is F and its existing net export before the new customer is B_t, the incremental export headroom is:

    H_t = F - B_t

With F = 1.0 MW:
- Hour 0: B_0 = -0.20 MW, so H_0 = 1.20 MW.
- Hour 13: B_13 = 0.78 MW, so H_13 = 0.22 MW.
- Hour 14: B_14 = 0.80 MW, so H_14 = 0.20 MW.

Negative baseline net export means the feeder is importing. The new customer can therefore export more than 1.0 MW before total feeder export reaches the 1.0 MW limit. The formula is a simplified single-bottleneck representation; a real feeder may have several thermal, voltage, and protection constraints.

## Problem 2 — Scenario comparison

The fixed cap is the smaller of 0.35 MW and physical headroom. The scheduled cap is the smaller of its time-of-day setting and physical headroom. The dynamic envelope uses all calculated physical headroom. The firm-upgrade scenario uses a 1.5 MW physical feeder export limit.

At hour 13 the dynamic envelope is 0.22 MW, below the fixed 0.35 MW cap and the scheduled 0.40 MW midday cap. At hour 0 the dynamic envelope is 1.20 MW, but PV availability is zero, so the extra headroom has no immediate PV value. This illustrates that a dynamic envelope is locational and time-varying, not uniformly more permissive than a fixed cap.

The firm-upgrade scenario expands physical capacity but has no capital cost in the model. It is a technical counterfactual, not a complete economic alternative.

The checked-in synthetic profile has 23.200 MWh PV available. The CI-verified baseline outputs are:

| Arrangement | PV absorbed (MWh) | Curtailed (MWh) | Imports (MWh) | Exports (MWh) |
|---|---:|---:|---:|---:|
| Fixed 0.35 MW | 14.148 | 9.052 | 2.895 | 3.240 |
| Scheduled 0.40 / 0.90 MW | 14.918 | 8.282 | 2.895 | 4.010 |
| Dynamic envelope | 15.278 | 7.922 | 2.895 | 4.370 |
| Firm upgrade 1.50 MW | 19.138 | 4.062 | 2.895 | 8.230 |
| Fixed 0.35 MW, no battery | 10.990 | 12.210 | 4.320 | 3.240 |

The battery reduces fixed-cap curtailment by 3.158 MWh and grid imports by 1.425 MWh. The dynamic envelope absorbs 1.130 MWh more PV than the fixed cap in this daily profile. "PV absorbed" means direct PV plus PV charging; battery conversion losses mean this is not the same as final delivered energy. The results depend on the synthetic load, PV, feeder baseline, and price assumptions.

## Problem 3 — Battery dispatch

The battery can absorb PV that would otherwise be curtailed during high-output hours and discharge later to serve site load. Cyclic SOC prevents the model from ending the day with free stored energy. The battery cannot charge from the grid. More energy capacity is useful only if there is sufficient charging power, discharge opportunity, export headroom, and temporal spread to use it.

The model's assumed import price, export price, and throughput degradation cost drive customer dispatch. A higher import price tends to increase the value of discharging to serve load; a higher export price can make direct exports more attractive; higher degradation cost discourages cycling. These assumptions do not represent actual PPL tariffs or customer compensation.

## Problem 4 — Upgrade versus flexible connection

A firm upgrade can provide a larger export envelope throughout the modeled day. A dynamic envelope can use existing capacity more efficiently without assuming a physical upgrade, but may expose the customer to curtailment when feeder conditions are constrained. A complete comparison needs upgrade capital cost, operating cost, expected utilization, interconnection delay, customer revenue, curtailment probability and duration, control/telemetry cost, and the value of earlier energization.

Risk allocation should specify the utility's obligation to calculate and communicate the envelope, the customer's obligation to provide compliant controls and telemetry, the response to communication loss, curtailment priority, notice, compensation if any, and the dispute process.

## Problem 5 — Engineering and regulatory synthesis

A strong memo will use DOE's terminology: a dynamic operating envelope is a time-varying upper/lower import/export bound at a point of interconnection; flexible interconnection is a control arrangement that enables a DER to operate within those bounds; flexible service connections apply similar controls to large loads. It will distinguish customer-controlled approaches (the customer adjusts DER output to a published envelope) from utility-direct-controlled approaches (the utility sends or enforces curtailment/derate commands). It will not assume that dynamic envelopes eliminate all upgrades or that fixed limits are always inefficient. It will identify the specific binding constraints, distinguish feeder-level export headroom from customer inverter capability, account for uncertainty and fail-safe behavior, and compare lifecycle costs and customer risk. It will state that the teaching model has no AC power flow, unbalanced phases, voltage/thermal/protection calculations, forecast error, or real utility data and cannot establish hosting capacity for an actual feeder.
