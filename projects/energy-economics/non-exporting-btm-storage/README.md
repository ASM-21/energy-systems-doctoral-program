# Computational Lab: Non-Exporting Behind-the-Meter Battery Storage

**Course:** Y1-02 Energy Economics and Market Fundamentals  
**Model:** 24-interval linear program with an explicit no-export constraint  
**Data:** Synthetic hourly load, PV, and retail import-price profile

## Objective

Model a behind-the-meter battery that shifts onsite PV and grid energy while preventing net export at the customer meter. The model chooses grid imports, battery charging/discharging, PV curtailment, and state of charge to minimize import cost plus a simple throughput-based degradation cost.

## Run

    python -m pip install -r requirements.txt
    python btm_storage.py
    python -m unittest discover -s . -p "test_*.py" -v

Outputs are written to `outputs/btm-storage/`: `dispatch.csv` and `summary.json`.

## Formulation

For each interval t, the meter energy balance is:

    grid_import_t + discharge_t + PV_t - curtailment_t = load_t + charge_t

The no-export condition is enforced directly:

    grid_import_t >= 0

Battery energy evolves as:

    SOC_(t+1) = SOC_t + eta_charge * charge_t * dt - discharge_t * dt / eta_discharge

with power, energy, and cyclic terminal-state constraints. The objective is import energy cost plus a simple throughput degradation proxy. PV curtailment has no separate penalty; foregone PV self-consumption is reflected in higher grid imports.

## Default synthetic case

The 24-hour profile contains a daytime PV surplus and an evening load/price peak. The default battery is 80 kW / 160 kWh, starts and ends at 80 kWh, and has 95% charge/discharge efficiency. The model is a price-taking customer optimization, not an actual tariff calculation.

## Verified default-case results

The CI run on 2026-11-20 executed both the no-battery baseline and default battery case and produced the following results for the synthetic 24-hour profile, 95% charge/discharge efficiency, and $15/MWh throughput degradation assumption:

| Metric | No battery | 80 kW / 160 kWh BTM battery |
|---|---:|---:|
| Grid imports | 1.123 MWh | 1.000 MWh |
| PV curtailment | 0.145 MWh | 0.000 MWh |
| PV used onsite | 0.830 MWh | 0.975 MWh |
| Battery charge / discharge | 0 / 0 MWh | 0.229 / 0.207 MWh |
| Import energy cost | $64.44 | $49.62 |
| Degradation proxy | $0.00 | $6.54 |
| Total objective cost | $64.44 | $56.16 |

The modeled objective improvement is approximately $8.28 for this synthetic day after the throughput degradation proxy. The battery absorbs all 0.145 MWh of baseline PV curtailment and reduces grid imports by approximately 0.123 MWh. These are model outputs, not customer bill savings or a utility-system benefit estimate. The tariff, demand charges, inverter standby losses, export compensation, battery capital cost, and network constraints are omitted. [CI run and test logs](https://github.com/ASM-21/energy-systems-doctoral-program/actions/runs/44832725560).

## Interpretation

## Required analysis

1. Compare no-battery and battery cases for grid imports, PV curtailment, self-consumption, and total cost.
2. Change battery power and energy ratings independently.
3. Vary round-trip efficiency and degradation cost.
4. Change the initial/terminal state of charge and explain the cyclic constraint.
5. Explain why non-exporting operation does not imply zero distribution-system impact: charging changes local demand, discharging changes net load, and controls can fail.
6. Identify what a real interconnection review must address: export-limiting controls, inadvertent export, protection, metering, communications loss, commissioning, inverter certification, voltage, thermal limits, and utility operating procedures.

## Limitations

This model is a single-meter energy optimization. It does not model feeder power flow, phase imbalance, voltage, thermal loading, protection coordination, inverter controls, forecast uncertainty, demand charges, time-varying export compensation, taxes, or a real utility tariff. It does not establish interconnection approval. A no-export constraint at the meter is not proof that the device has no grid impact.

## Submission

Include baseline and battery dispatch tables, a sensitivity plot, code, unit tests, and a 1,000-word technical/economic memo. Clearly distinguish modeled bill savings from system-level benefits and avoid describing synthetic inputs as customer data.