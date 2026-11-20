"""Compare fixed, scheduled, dynamic, and upgraded export limits with PV + BTM storage."""
from __future__ import annotations
import argparse
import csv
import json
from pathlib import Path

import numpy as np
from scipy.optimize import linprog


def load_profile(path: Path) -> list[dict]:
    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    required = {"hour", "site_load_mw", "pv_available_mw", "existing_feeder_net_export_mw"}
    if not rows or not required.issubset(rows[0]):
        raise ValueError(f"Profile must contain columns: {sorted(required)}")
    parsed = []
    for row in rows:
        parsed.append({
            "hour": int(row["hour"]),
            "site_load_mw": float(row["site_load_mw"]),
            "pv_available_mw": float(row["pv_available_mw"]),
            "existing_feeder_net_export_mw": float(row["existing_feeder_net_export_mw"]),
        })
    if len(parsed) != 24 or [row["hour"] for row in parsed] != list(range(24)):
        raise ValueError("Expected exactly 24 ordered hourly observations (0 through 23).")
    if any(row["site_load_mw"] < 0 or row["pv_available_mw"] < 0 for row in parsed):
        raise ValueError("Load and PV availability must be nonnegative.")
    return parsed


def export_envelopes(profile: list[dict], feeder_export_limit_mw: float = 1.0) -> dict[str, list[float]]:
    if feeder_export_limit_mw <= 0:
        raise ValueError("Feeder export limit must be positive.")
    baseline = [row["existing_feeder_net_export_mw"] for row in profile]
    headroom = [feeder_export_limit_mw - value for value in baseline]
    if min(headroom) < -1e-9:
        raise ValueError("Baseline feeder profile already exceeds the physical export limit.")
    fixed = [min(0.35, max(0.0, value)) for value in headroom]
    scheduled = [
        min(0.40 if 10 <= row["hour"] <= 16 else 0.90, max(0.0, headroom[i]))
        for i, row in enumerate(profile)
    ]
    dynamic = [max(0.0, value) for value in headroom]
    upgrade = [1.5 - value for value in baseline]
    return {
        "fixed_0.35_mw": fixed,
        "scheduled_0.40_0.90_mw": scheduled,
        "dynamic_operating_envelope": dynamic,
        "firm_upgrade_1.50_mw": upgrade,
    }


def solve_scenario(
    profile: list[dict],
    export_limit: list[float],
    *,
    battery_power_mw: float = 0.5,
    battery_energy_mwh: float = 1.5,
    eta_charge: float = 0.95,
    eta_discharge: float = 0.95,
    initial_soc_fraction: float = 0.5,
    import_price_per_mwh: float = 80.0,
    export_price_per_mwh: float = 30.0,
    degradation_cost_per_mwh: float = 10.0,
) -> dict:
    n = len(profile)
    if len(export_limit) != n:
        raise ValueError("Export-limit vector must match profile length.")
    if battery_power_mw < 0 or battery_energy_mwh < 0:
        raise ValueError("Battery power and energy must be nonnegative.")
    if not (0 < eta_charge <= 1 and 0 < eta_discharge <= 1):
        raise ValueError("Battery efficiencies must be in (0, 1].")
    if not (0 <= initial_soc_fraction <= 1):
        raise ValueError("Initial SOC fraction must be in [0, 1].")

    # Variable blocks: PV direct, charge, discharge, grid import, grid export,
    # PV curtailment, then SOC at each interval boundary.
    pv0, ch0, dis0, imp0, exp0, cur0, soc0 = 0, n, 2*n, 3*n, 4*n, 5*n, 6*n
    size = 7*n + 1
    def ix(start: int, t: int) -> int:
        return start + t

    objective = np.zeros(size)
    objective[ch0:ch0+n] = degradation_cost_per_mwh
    objective[dis0:dis0+n] = degradation_cost_per_mwh
    objective[imp0:imp0+n] = import_price_per_mwh
    objective[exp0:exp0+n] = -export_price_per_mwh

    a_eq, b_eq = [], []
    for t, row in enumerate(profile):
        pv_balance = np.zeros(size)
        pv_balance[ix(pv0, t)] = 1
        pv_balance[ix(ch0, t)] = 1
        pv_balance[ix(cur0, t)] = 1
        a_eq.append(pv_balance)
        b_eq.append(row["pv_available_mw"])

        site_balance = np.zeros(size)
        site_balance[ix(pv0, t)] = 1
        site_balance[ix(dis0, t)] = 1
        site_balance[ix(imp0, t)] = 1
        site_balance[ix(ch0, t)] = -1
        site_balance[ix(exp0, t)] = -1
        a_eq.append(site_balance)
        b_eq.append(row["site_load_mw"])

        soc_balance = np.zeros(size)
        soc_balance[ix(soc0, t+1)] = 1
        soc_balance[ix(soc0, t)] = -1
        soc_balance[ix(ch0, t)] = -eta_charge
        soc_balance[ix(dis0, t)] = 1 / eta_discharge
        a_eq.append(soc_balance)
        b_eq.append(0.0)

    initial_soc = battery_energy_mwh * initial_soc_fraction
    initial_row = np.zeros(size)
    initial_row[ix(soc0, 0)] = 1
    a_eq.append(initial_row)
    b_eq.append(initial_soc)
    terminal_row = np.zeros(size)
    terminal_row[ix(soc0, n)] = 1
    a_eq.append(terminal_row)
    b_eq.append(initial_soc)


    bounds = []
    for t, row in enumerate(profile):
        bounds.append((0, row["pv_available_mw"]))  # PV direct
    bounds.extend([(0, battery_power_mw)] * n)      # PV charging
    bounds.extend([(0, battery_power_mw)] * n)      # battery discharge
    bounds.extend([(0, 3.0)] * n)                   # grid import
    bounds.extend([(0, max(0.0, value)) for value in export_limit])  # grid export
    bounds.extend([(0, row["pv_available_mw"]) for row in profile])  # PV curtailment
    bounds.extend([(0, battery_energy_mwh)] * (n + 1))              # SOC

    result = linprog(
        objective,
        A_eq=np.asarray(a_eq), b_eq=np.asarray(b_eq),
        bounds=bounds, method="highs",
    )
    if not result.success:
        raise RuntimeError(f"Flexible-interconnection LP failed: {result.message}")
    x = result.x
    rows = []
    for t, row in enumerate(profile):
        pv_direct = x[ix(pv0, t)]
        charge = x[ix(ch0, t)]
        discharge = x[ix(dis0, t)]
        grid_import = x[ix(imp0, t)]
        grid_export = x[ix(exp0, t)]
        curtail = x[ix(cur0, t)]
        soc_start = x[ix(soc0, t)]
        soc_end = x[ix(soc0, t+1)]
        feeder_net_export = row["existing_feeder_net_export_mw"] + grid_export - grid_import
        rows.append({
            **row,
            "export_limit_mw": export_limit[t],
            "pv_direct_mw": pv_direct,
            "battery_charge_mw": charge,
            "battery_discharge_mw": discharge,
            "grid_import_mw": grid_import,
            "grid_export_mw": grid_export,
            "pv_curtailment_mw": curtail,
            "soc_start_mwh": soc_start,
            "soc_end_mwh": soc_end,
            "feeder_net_export_mw": feeder_net_export,
        })
    summary = {
        "pv_available_mwh": sum(row["pv_available_mw"] for row in profile),
        "pv_utilized_mwh": sum(row["pv_direct_mw"] + row["battery_charge_mw"] for row in rows),
        "pv_curtailment_mwh": sum(row["pv_curtailment_mw"] for row in rows),
        "grid_import_mwh": sum(row["grid_import_mw"] for row in rows),
        "grid_export_mwh": sum(row["grid_export_mw"] for row in rows),
        "battery_charge_mwh": sum(row["battery_charge_mw"] for row in rows),
        "battery_discharge_mwh": sum(row["battery_discharge_mw"] for row in rows),
        "battery_throughput_mwh": sum(row["battery_charge_mw"] + row["battery_discharge_mw"] for row in rows),
        "peak_customer_export_mw": max(row["grid_export_mw"] for row in rows),
        "peak_feeder_net_export_mw": max(row["feeder_net_export_mw"] for row in rows),
        "max_selected_export_limit_mw": max(export_limit),
        "min_selected_export_limit_mw": min(export_limit),
        "objective_value": float(result.fun),
        "initial_soc_mwh": initial_soc,
        "terminal_soc_mwh": x[ix(soc0, n)],
    }
    return {"summary": summary, "hourly": rows}


def run_model(input_csv: Path, output_dir: Path, *, battery_power_mw: float = 0.5,
              battery_energy_mwh: float = 1.5) -> dict:
    profile = load_profile(input_csv)
    envelopes = export_envelopes(profile)
    output_dir.mkdir(parents=True, exist_ok=True)
    summaries, hourly_rows = [], []
    for name, limit in envelopes.items():
        result = solve_scenario(
            profile, limit, battery_power_mw=battery_power_mw,
            battery_energy_mwh=battery_energy_mwh
        )
        summary = {"scenario": name, **result["summary"]}
        summaries.append(summary)
        for row in result["hourly"]:
            hourly_rows.append({"scenario": name, **row})
    no_battery = solve_scenario(
        profile, envelopes["fixed_0.35_mw"], battery_power_mw=0.0, battery_energy_mwh=0.0
    )
    summaries.append({"scenario": "no_battery_fixed_0.35_mw", **no_battery["summary"]})
    for row in no_battery["hourly"]:
        hourly_rows.append({"scenario": "no_battery_fixed_0.35_mw", **row})
    with (output_dir / "scenario_summary.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(summaries[0]))
        writer.writeheader()
        writer.writerows(summaries)
    with (output_dir / "hourly_dispatch.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(hourly_rows[0]))
        writer.writeheader()
        writer.writerows(hourly_rows)
    metadata = {
        "scenarios": summaries,
        "assumptions": {
            "customer_pv_nameplate_mw": 3.0,
            "battery_power_mw": battery_power_mw,
            "battery_energy_mwh": battery_energy_mwh,
            "battery_efficiency": 0.95,
            "feeder_export_limit_mw": 1.0,
            "upgrade_export_limit_mw": 1.5,
            "import_price_per_mwh": 80.0,
            "export_price_per_mwh": 30.0,
            "degradation_cost_per_mwh_throughput": 10.0,
            "all_inputs_synthetic": True,
        },
        "limitations": "Single-customer 24-hour LP; no AC power flow, voltage, branch thermal, phase, protection, forecast, or communications model.",
    }
    (output_dir / "summary.json").write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")
    print("Scenario | PV utilized MWh | curtailed MWh | import MWh | export MWh")
    for row in summaries:
        print(f"{row['scenario']} | {row['pv_utilized_mwh']:.3f} | {row['pv_curtailment_mwh']:.3f} | {row['grid_import_mwh']:.3f} | {row['grid_export_mwh']:.3f}")
    print(f"Outputs: {output_dir.resolve()}")
    return metadata


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=Path("data/day_ahead_profile.csv"))
    parser.add_argument("--output-dir", type=Path, default=Path("outputs/flexible-interconnection"))
    parser.add_argument("--battery-power-mw", type=float, default=0.5)
    parser.add_argument("--battery-energy-mwh", type=float, default=1.5)
    args = parser.parse_args()
    run_model(args.input, args.output_dir, battery_power_mw=args.battery_power_mw,
              battery_energy_mwh=args.battery_energy_mwh)


if __name__ == "__main__":
    main()
