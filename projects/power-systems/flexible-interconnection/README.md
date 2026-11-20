# Flexible Interconnection and Dynamic Export Envelopes

**Course:** Y1-01 Power Systems and Electricity Infrastructure; Y1-03 Electricity Markets and Utility Regulation  
**Level:** Applied graduate optimization lab  
**Data:** Synthetic 24-hour feeder and customer profile  
**Solver:** SciPy HiGHS linear programming

## Research question

How much customer-sited PV energy can be utilized under different export arrangements when feeder export headroom varies over the day? Compare a fixed export cap, a pre-agreed scheduled cap, a dynamic operating envelope, and a hypothetical physical upgrade. A behind-the-meter battery is available in each scenario.

This lab demonstrates operational flexibility, not an actual PPL tariff or a utility-grade hosting-capacity analysis. All profiles and costs are synthetic.

## Scenarios

1. **Fixed export limit:** customer export capped at 0.35 MW in every interval, further constrained by physical feeder headroom.
2. **Scheduled export limit:** customer export capped at 0.40 MW from 10:00–16:00 and 0.90 MW in other intervals, subject to physical headroom.
3. **Dynamic operating envelope:** customer export limit changes each hour with available feeder headroom, calculated as feeder export limit less the existing feeder net export.
4. **Firm upgrade:** feeder export limit increases from 1.0 MW to 1.5 MW. This is a hypothetical infrastructure alternative, not a flexible connection.

The customer has 1.5 MW of available PV, a 0.5 MW / 1.5 MWh battery, 95% charge/discharge efficiency, and a cyclic state-of-charge constraint. The battery can charge only from available PV. Customer load is served before exports; the optimization chooses PV use, battery dispatch, grid imports/exports, and curtailment.

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
    python -m unittest discover -s . -p "test_*.py" -v

Outputs:
- scenario_summary.csv: PV utilization, curtailment, grid imports/exports, battery throughput, peak feeder export, and objective value by scenario.
- hourly_dispatch.csv: hourly limits, PV, load, battery, grid exchange, curtailment, and state of charge.
- summary.json: scenario assumptions and results.

## Interpretation

- A dynamic envelope can be less restrictive than a fixed cap in hours with more feeder headroom and more restrictive when existing feeder export is high.
- A scheduled limit is predictable but may not reflect actual feeder conditions in every interval.
- A firm upgrade increases physical capacity but is not costed in this model.
- A battery can shift PV energy across hours, but its usefulness depends on power/energy limits, efficiency, degradation, and the later export envelope.
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
