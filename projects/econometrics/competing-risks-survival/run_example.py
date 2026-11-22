import csv
import json
from pathlib import Path

from survival import (
    aalen_johansen,
    curve_value_at,
    exponential_competing_risk_cif,
    kaplan_meier_net_approval,
    simulate_exponential_competing_risks,
)


def main():
    path = Path(__file__).with_name("example_data.csv")
    with path.open(newline="", encoding="utf-8") as handle:
        records = [
            {"time": float(row["days_from_complete_application"]), "event": row["event"]}
            for row in csv.DictReader(handle)
        ]
    rates = {"approval": 0.08, "withdrawal": 0.05, "denial": 0.02}
    horizon = 15.0
    simulated = simulate_exponential_competing_risks(10000, rates, horizon, seed=2026)
    simulated_aj = aalen_johansen(simulated)
    simulated_km = kaplan_meier_net_approval(simulated)
    result = {
        "synthetic_data_only": True,
        "observation_count": len(records),
        "aalen_johansen": aalen_johansen(records),
        "one_minus_kaplan_meier_net_approval": kaplan_meier_net_approval(records),
        "simulation_validation": {
            "n": len(simulated),
            "administrative_censor_time": horizon,
            "cause_specific_rates_per_day": rates,
            "a_j_estimated_approval_cif": curve_value_at(simulated_aj, horizon, "cif_approval"),
            "a_j_analytic_approval_cif": exponential_competing_risk_cif("approval", rates, horizon),
            "km_estimated_net_approval_risk": curve_value_at(simulated_km, horizon, "net_approval_probability"),
        },
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
