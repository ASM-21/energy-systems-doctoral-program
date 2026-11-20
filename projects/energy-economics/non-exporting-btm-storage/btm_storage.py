"""Optimize behind-the-meter storage under a strict no-export constraint."""
from __future__ import annotations
import argparse
import csv
import json
from pathlib import Path
import numpy as np
from scipy.optimize import linprog

def load_profile(path: str | Path) -> dict[str, np.ndarray]:
    with open(path, newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    if not rows:
        raise ValueError("Profile CSV must contain at least one interval.")
    return {
        "hour": np.array([int(row["hour"]) for row in rows]),
        "load_kw": np.array([float(row["load_kw"]) for row in rows]),
        "pv_kw": np.array([float(row["pv_kw"]) for row in rows]),
        "price_usd_per_mwh": np.array([float(row["price_usd_per_mwh"]) for row in rows]),
    }

def solve_btm_storage(
    load_kw, pv_kw, price_usd_per_mwh, *,
    power_kw: float, energy_kwh: float, initial_soc_kwh: float = 0.0,
    eta_charge: float = 0.95, eta_discharge: float = 0.95,
    degradation_cost_usd_per_mwh: float = 15.0, interval_hours: float = 1.0,
) -> dict:
    """Minimize import bill plus throughput degradation cost.

    Grid import is constrained nonnegative in every interval. PV curtailment
    absorbs surplus that cannot be used onsite or stored. The LP is a
    single-meter energy model; it has no feeder voltage or thermal constraints.
    """
    load = np.asarray(load_kw, dtype=float)
    pv = np.asarray(pv_kw, dtype=float)
    price = np.asarray(price_usd_per_mwh, dtype=float)
    if load.ndim != 1 or pv.ndim != 1 or price.ndim != 1:
        raise ValueError("Load, PV, and price profiles must be one-dimensional.")
    if len(load) == 0 or not (len(load) == len(pv) == len(price)):
        raise ValueError("Load, PV, and price profiles must have equal nonzero length.")
    if not all(np.all(np.isfinite(x)) for x in (load, pv, price)):
        raise ValueError("Profiles must contain only finite values.")
    if np.any(load < 0) or np.any(pv < 0) or np.any(price < 0):
        raise ValueError("Load, PV, and import prices must be nonnegative.")
    if power_kw < 0 or energy_kwh < 0 or degradation_cost_usd_per_mwh < 0:
        raise ValueError("Battery ratings and degradation cost must be nonnegative.")
    if not (0 < eta_charge <= 1 and 0 < eta_discharge <= 1):
        raise ValueError("Charge and discharge efficiencies must be in (0, 1].")
    if not np.isfinite(interval_hours) or interval_hours <= 0:
        raise ValueError("Interval duration must be positive and finite.")
    if not 0 <= initial_soc_kwh <= energy_kwh:
        raise ValueError("Initial state of charge must be within battery energy capacity.")

    n = len(load)
    # Variable blocks: grid import, charge, discharge, PV curtailment, SOC[0..n].
    g0, c0, d0, k0, e0 = 0, n, 2*n, 3*n, 4*n
    size = 5*n + 1
    objective = np.zeros(size)
    objective[g0:g0+n] = price * interval_hours / 1000.0
    objective[c0:c0+n] = degradation_cost_usd_per_mwh * interval_hours / 1000.0
    objective[d0:d0+n] = degradation_cost_usd_per_mwh * interval_hours / 1000.0
    a_eq = []
    b_eq = []
    for t in range(n):
        balance = np.zeros(size)
        balance[g0+t] = 1.0
        balance[c0+t] = -1.0
        balance[d0+t] = 1.0
        balance[k0+t] = -1.0
        a_eq.append(balance)
        b_eq.append(load[t] - pv[t])

        state = np.zeros(size)
        state[e0+t] = -1.0
        state[e0+t+1] = 1.0
        state[c0+t] = -eta_charge * interval_hours
        state[d0+t] = interval_hours / eta_discharge
        a_eq.append(state)
        b_eq.append(0.0)

    bounds = (
        [(0.0, None)] * n
        + [(0.0, power_kw)] * n
        + [(0.0, power_kw)] * n
        + [(0.0, float(value)) for value in pv]
        + [(0.0, energy_kwh)] * (n+1)
    )
    bounds[e0] = (initial_soc_kwh, initial_soc_kwh)
    bounds[e0+n] = (initial_soc_kwh, initial_soc_kwh)
    result = linprog(
        objective, A_eq=np.asarray(a_eq), b_eq=np.asarray(b_eq),
        bounds=bounds, method="highs"
    )
    if not result.success:
        raise RuntimeError(f"Storage optimization failed: {result.message}")

    grid = result.x[g0:g0+n]
    charge = result.x[c0:c0+n]
    discharge = result.x[d0:d0+n]
    curtail = result.x[k0:k0+n]
    soc = result.x[e0:e0+n+1]
    pv_used = pv - curtail
    energy_imported = float(np.sum(grid) * interval_hours / 1000.0)
    energy_curtailed = float(np.sum(curtail) * interval_hours / 1000.0)
    energy_charged = float(np.sum(charge) * interval_hours / 1000.0)
    energy_discharged = float(np.sum(discharge) * interval_hours / 1000.0)
    import_cost = float(np.dot(price, grid) * interval_hours / 1000.0)
    degradation_cost = float(degradation_cost_usd_per_mwh *
                             (energy_charged + energy_discharged))
    return {
        "intervals": n,
        "grid_import_kw": grid.tolist(),
        "battery_charge_kw": charge.tolist(),
        "battery_discharge_kw": discharge.tolist(),
        "pv_curtailment_kw": curtail.tolist(),
        "pv_used_kw": pv_used.tolist(),
        "state_of_charge_kwh": soc.tolist(),
        "grid_import_mwh": energy_imported,
        "pv_curtailed_mwh": energy_curtailed,
        "pv_used_mwh": float(np.sum(pv_used) * interval_hours / 1000.0),
        "battery_charge_mwh": energy_charged,
        "battery_discharge_mwh": energy_discharged,
        "import_energy_cost_usd": import_cost,
        "degradation_cost_usd": degradation_cost,
        "total_objective_cost_usd": import_cost + degradation_cost,
        "maximum_grid_export_kw": 0.0,
        "minimum_soc_kwh": float(np.min(soc)),
        "maximum_soc_kwh": float(np.max(soc)),
        "initial_soc_kwh": float(soc[0]),
        "final_soc_kwh": float(soc[-1]),
        "power_kw": float(power_kw),
        "energy_kwh": float(energy_kwh),
    }

def write_outputs(profile: dict, result: dict, output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    keys = ["hour", "load_kw", "pv_kw", "price_usd_per_mwh", "grid_import_kw",
            "battery_charge_kw", "battery_discharge_kw", "pv_curtailment_kw",
            "pv_used_kw", "state_of_charge_kwh"]
    with (output_dir / "dispatch.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(keys)
        for i in range(result["intervals"]):
            writer.writerow([int(profile["hour"][i]), float(profile["load_kw"][i]),
                             float(profile["pv_kw"][i]), float(profile["price_usd_per_mwh"][i]),
                             result["grid_import_kw"][i], result["battery_charge_kw"][i],
                             result["battery_discharge_kw"][i], result["pv_curtailment_kw"][i],
                             result["pv_used_kw"][i], result["state_of_charge_kwh"][i]])
    summary = {key: value for key, value in result.items()
               if not isinstance(value, list)}
    (output_dir / "summary.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", type=Path, default=Path(__file__).parent / "data" / "daily_profile.csv")
    parser.add_argument("--power-kw", type=float, default=80.0)
    parser.add_argument("--energy-kwh", type=float, default=160.0)
    parser.add_argument("--degradation-cost", type=float, default=15.0)
    parser.add_argument("--output-dir", type=Path, default=Path("outputs/btm-storage"))
    args = parser.parse_args()
    profile = load_profile(args.profile)
    result = solve_btm_storage(profile["load_kw"], profile["pv_kw"], profile["price_usd_per_mwh"],
                               power_kw=args.power_kw, energy_kwh=args.energy_kwh,
                               initial_soc_kwh=args.energy_kwh / 2,
                               degradation_cost_usd_per_mwh=args.degradation_cost)
    write_outputs(profile, result, args.output_dir)
    print(f"Grid imports: {result['grid_import_mwh']:.3f} MWh")
    print(f"PV curtailed: {result['pv_curtailed_mwh']:.3f} MWh")
    print(f"PV used onsite: {result['pv_used_mwh']:.3f} MWh")
    print(f"Battery charge/discharge: {result['battery_charge_mwh']:.3f} / {result['battery_discharge_mwh']:.3f} MWh")
    print(f"Import cost: ${result['import_energy_cost_usd']:.2f}")
    print(f"Degradation cost: ${result['degradation_cost_usd']:.2f}")
    print(f"No-export constraint: maximum export {result['maximum_grid_export_kw']:.1f} kW")
    print(f"Results: {args.output_dir.resolve()}")

if __name__ == "__main__":
    main()