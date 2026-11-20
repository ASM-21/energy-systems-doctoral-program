# Flexible Interconnection and Dynamic Export Envelopes

**Course:** Y1-01 Power Systems and Electricity Infrastructure; Y1-03 Electricity Markets and Utility Regulation  
**Level:** Applied graduate optimization lab  
**Data:** Synthetic 24-hour feeder and customer profile  
**Solver:** SciPy HiGHS linear programming

## Research question

How much customer-sited PV energy can be utilized under different export arrangements when feeder export headroom varies over the day? Compare a fixed export cap, a pre-agreed scheduled cap, a dynamic operating envelope, and a hypothetical physical upgrade. Four arrangements are compared with a behind-the-meter battery, and a fifth fixed-cap reference is run without a battery.

This lab demonstrates operational flexibility, not an actual PPL tariff or a utility-grade hosting-capacity analysis. All profiles and costs are synthetic.

## Scenarios

1. **Fixed export limit:** customer export capped at 0.35 MW in every interval, further constrained by physical feeder headroom.
2. **Scheduled export limit:** customer export capped at 0.40 MW from 10:00–16:00 and 0.90 MW in other intervals, subject to physical headroom.
3. **Dynamic operating envelope:** customer export limit changes each hour with available feeder headroom, calculated as feeder export limit less the existing feeder net export.
4. **Firm upgrade:** feeder export limit increases from 1.0 MW to 1.5 MW. This is a hypothetical infrastructure alternative, not a flexible connection.

The customer has 3.0 MW of available PV, a 0.5 MW / 1.5 MWh battery, 95% charge/discharge efficiency, and a cyclic state-of-charge constraint. The battery can charge only from available PV. Customer load is served before exports; the optimization chooses PV use, battery dispatch, grid imports/exports, and curtailment.

## Model

For each hour t:

    PV_direct[t] + charge[t] + curtailment[t] = PV_available[t]
    PV_direct[t] + discharge[t] + import[t] - charge[t] - export[t] = load[t]
    SOC[t+1] = SOC[t] + eta_charge * charge[t] - discharge[t] / eta_discharge
    export[t] <= export_envelope[t]
    0 <= SOC[t] <= energy_capacity

The objective minimizes assumed retail import cost, minus export revenue, plus battery throughput degradation cost. These prices are pedagogical assumptions, not PPL rates or a social-welfare objective. The model does not allow grid charging.

The dynamic export envelope is:

    export_envelope[t] = feeder_export_limit - existing_feeder_net_export[t]

The baseline feeder profile must already comply with the physical export limit. If it does not, the script rejects the scenario rather than attributing a pre-existing violation to the new customer.

## Run

    python -m pip install -r requirements.txt
    python flexible_interconnection.py --output-dir outputs/flexible-interconnection
    python flexible_interconnection.py --battery-power-mw 0 --battery-energy-mwh 0 --output-dir outputs/no-battery
    python -m unittest discover -s . -p "test_*.py" -v

Outputs:
- scenario_summary.csv: PV utilization, curtailment, grid imports/exports, battery throughput, peak feeder export, and objective value by scenario.
- hourly_dispatch.csv: hourly limits, PV, load, battery, grid exchange, curtailment, and state of charge.
- summary.json: scenario assumptions and results.

## Reproducible baseline results

The checked-in synthetic 24-hour profile has 23.200 MWh of PV available. With the default 0.5 MW / 1.5 MWh battery and stated price assumptions, the CI smoke test produced:

| Arrangement | PV absorbed (MWh) | PV curtailed (MWh) | Grid imports (MWh) | Grid exports (MWh) |
|---|---:|---:|---:|---:|
| Fixed 0.35 MW | 14.148 | 9.052 | 2.895 | 3.240 |
| Scheduled 0.40 / 0.90 MW | 14.918 | 8.282 | 2.895 | 4.010 |
| Dynamic operating envelope | 15.278 | 7.922 | 2.895 | 4.370 |
| Firm upgrade to 1.50 MW | 19.138 | 4.062 | 2.895 | 8.230 |
| Fixed 0.35 MW, no battery | 10.990 | 12.210 | 4.320 | 3.240 |

"PV absorbed" is PV supplied directly or sent to battery charging, before battery conversion losses. It is not identical to final energy delivered to load. In this synthetic case, adding the battery to the fixed-cap arrangement reduces curtailment by 3.158 MWh and grid imports by 1.425 MWh. The dynamic envelope absorbs 1.130 MWh more PV than the fixed cap, but it is not more permissive in every hour: at hour 13 its 0.22 MW limit is below the fixed 0.35 MW cap. Its aggregate result reflects the full 24-hour profile.

These are deterministic outputs of the stated synthetic LP, not measured utility performance or a recommendation to adopt a specific export limit.

## Interpretation

- A dynamic envelope can be less restrictive than a fixed cap in hours with more feeder headroom and more restrictive when existing feeder export is high. The synthetic profile deliberately includes a large midday PV surplus so that the fixed, scheduled, dynamic, and upgrade cases can exhibit different curtailment outcomes.
- A scheduled limit is predictable but may not reflect actual feeder conditions in every interval.
- A firm upgrade increases physical capacity but is not costed in this model.
- A battery can shift PV energy across hours, but its usefulness depends on power/energy limits, efficiency, degradation, and the later export envelope. The no-battery fixed-cap reference isolates the modeled contribution of storage.
- Compare PV energy utilized, curtailment, customer imports, exports, and battery throughput. Do not rank arrangements using only one metric.

## Limitations

This is a single-customer, single-feeder-headroom, balanced, 24-hour linear model. It omits AC power flow, phase imbalance, voltage constraints, line/transformer thermal constraints at individual branches, protection coordination, inverter volt-var/watt behavior, forecast error, communications failure, customer response, market settlement, and upgrade costs. The dynamic envelope is calculated from a synthetic baseline profile, not from a real utility operating system.

A real flexible-interconnection design would need a transparent method for determining and updating export envelopes, measurement/telemetry requirements, fail-safe behavior, curtailment priority, customer notice, compensation, appeal mechanisms, and treatment of forecast and communication errors.

## Extension assignment

1. Increase PV nameplate to 2.0 MW.
2. Reduce battery energy to 0.5 MWh while retaining 0.5 MW power.
3. Add a forecast-error reserve margin to the dynamic envelope.
4. Compare fixed, scheduled, and dynamic limits under low-, medium-, and high-load days.
5. Write a 1,000-word memo identifying when flexible interconnection is preferable to a firm upgrade and who bears curtailment risk.
