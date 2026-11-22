"""Monte Carlo adequacy screen with Markov weather and a repairable unit.

All inputs are synthetic. This is a teaching model, not a planning standard.
"""
from __future__ import annotations

import argparse
import json
import math
import random
import statistics
from dataclasses import asdict, dataclass
from pathlib import Path


@dataclass(frozen=True)
class Parameters:
    hours_per_year: int = 8760
    load_mean_mw: float = 1000.0
    load_sd_mw: float = 80.0
    renewable_low_mw: float = 100.0
    renewable_high_mw: float = 400.0
    firm_capacity_mw: float = 950.0
    outage_block_mw: float = 100.0
    weather_low_to_high: float = 0.10
    weather_high_to_low: float = 0.30
    unit_failure_probability_per_hour: float = 0.001
    unit_repair_probability_per_hour: float = 0.03233333333333333

    def validate(self) -> None:
        if self.hours_per_year <= 0:
            raise ValueError("hours_per_year must be positive")
        if self.load_mean_mw <= 0 or self.load_sd_mw < 0:
            raise ValueError("load mean must be positive and standard deviation nonnegative")
        if min(self.renewable_low_mw, self.renewable_high_mw, self.firm_capacity_mw,
               self.outage_block_mw) < 0:
            raise ValueError("capacities and renewable outputs must be nonnegative")
        if self.renewable_high_mw < self.renewable_low_mw:
            raise ValueError("high-regime renewable output must not be below low-regime output")
        if self.outage_block_mw > self.firm_capacity_mw:
            raise ValueError("outage block cannot exceed total firm capacity")
        probabilities = (
            self.weather_low_to_high, self.weather_high_to_low,
            self.unit_failure_probability_per_hour,
            self.unit_repair_probability_per_hour,
        )
        if any(p < 0 or p > 1 for p in probabilities):
            raise ValueError("transition probabilities must lie in [0, 1]")
        if self.weather_low_to_high + self.weather_high_to_low == 0:
            raise ValueError("weather chain must permit a transition")
        if self.unit_failure_probability_per_hour + self.unit_repair_probability_per_hour == 0:
            raise ValueError("unit availability chain must permit a transition")


def stationary_high_probability(low_to_high: float, high_to_low: float) -> float:
    if min(low_to_high, high_to_low) < 0 or low_to_high + high_to_low <= 0:
        raise ValueError("transition probabilities must be nonnegative and not both zero")
    return low_to_high / (low_to_high + high_to_low)


def stationary_outage_probability(failure: float, repair: float) -> float:
    if min(failure, repair) < 0 or failure + repair <= 0:
        raise ValueError("failure and repair probabilities must be nonnegative and not both zero")
    return failure / (failure + repair)


def shortfall_mw(load_mw: float, renewable_mw: float, available_firm_mw: float) -> float:
    return max(0.0, load_mw - renewable_mw - available_firm_mw)


def simulate_year(params: Parameters, rng: random.Random) -> dict[str, float | int]:
    params.validate()
    high_probability = stationary_high_probability(
        params.weather_low_to_high, params.weather_high_to_low
    )
    outage_probability = stationary_outage_probability(
        params.unit_failure_probability_per_hour,
        params.unit_repair_probability_per_hour,
    )
    high_weather = rng.random() < high_probability
    unit_out = rng.random() < outage_probability
    shortage_hours = 0
    unserved_energy_mwh = 0.0
    total_net_load_mwh = 0.0

    for _ in range(params.hours_per_year):
        if high_weather:
            if rng.random() < params.weather_high_to_low:
                high_weather = False
        elif rng.random() < params.weather_low_to_high:
            high_weather = True

        if unit_out:
            if rng.random() < params.unit_repair_probability_per_hour:
                unit_out = False
        elif rng.random() < params.unit_failure_probability_per_hour:
            unit_out = True

        renewable = params.renewable_high_mw if high_weather else params.renewable_low_mw
        load = max(0.0, rng.gauss(params.load_mean_mw, params.load_sd_mw))
        available_firm = params.firm_capacity_mw - (params.outage_block_mw if unit_out else 0.0)
        net_load = max(0.0, load - renewable)
        unserved = shortfall_mw(load, renewable, available_firm)
        total_net_load_mwh += net_load
        if unserved > 1e-9:
            shortage_hours += 1
            unserved_energy_mwh += unserved

    return {
        "shortage_hours": shortage_hours,
        "unserved_energy_mwh": unserved_energy_mwh,
        "total_net_load_mwh": total_net_load_mwh,
        "loss_of_load_probability": shortage_hours / params.hours_per_year,
    }


def summarize(values: list[float]) -> dict[str, float]:
    ordered = sorted(values)

    def percentile(p: float) -> float:
        if len(ordered) == 1:
            return ordered[0]
        position = (len(ordered) - 1) * p
        lower = math.floor(position)
        upper = math.ceil(position)
        if lower == upper:
            return ordered[lower]
        weight = position - lower
        return ordered[lower] * (1 - weight) + ordered[upper] * weight

    se = statistics.stdev(values) / math.sqrt(len(values)) if len(values) > 1 else 0.0
    return {
        "mean": statistics.fmean(values),
        "standard_error_across_years": se,
        "p05": percentile(0.05),
        "median": percentile(0.50),
        "p95": percentile(0.95),
    }


def simulate(years: int = 20, seed: int = 20261122,
             params: Parameters | None = None) -> dict:
    if years <= 0:
        raise ValueError("years must be positive")
    params = params or Parameters()
    params.validate()
    rng = random.Random(seed)
    annual = [simulate_year(params, rng) for _ in range(years)]
    lole = [float(row["shortage_hours"]) for row in annual]
    eue = [float(row["unserved_energy_mwh"]) for row in annual]
    lolp = [float(row["loss_of_load_probability"]) for row in annual]
    return {
        "model": "synthetic_markov_weather_repairable_unit_adequacy_screen",
        "seed": seed,
        "simulated_years": years,
        "parameters": asdict(params),
        "stationary_high_weather_probability": stationary_high_probability(
            params.weather_low_to_high, params.weather_high_to_low
        ),
        "stationary_unit_outage_probability": stationary_outage_probability(
            params.unit_failure_probability_per_hour,
            params.unit_repair_probability_per_hour,
        ),
        "metrics": {
            "lole_hours_per_year": summarize(lole),
            "eue_mwh_per_year": summarize(eue),
            "hourly_lolp_by_year": summarize(lolp),
        },
        "limitations": [
            "Synthetic load and renewable profiles; no empirical calibration.",
            "Load is sampled independently of weather and renewable output.",
            "Renewable output has two fixed regimes and omits spatial correlation.",
            "Only one repairable capacity block is represented.",
            "No transmission constraints, demand response, storage, or cascading events.",
            "Results are not PJM, utility, or regulatory resource-adequacy metrics.",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--years", type=int, default=20)
    parser.add_argument("--seed", type=int, default=20261122)
    parser.add_argument("--output-dir", type=Path)
    args = parser.parse_args()
    result = simulate(args.years, args.seed)
    rendered = json.dumps(result, indent=2)
    if args.output_dir:
        args.output_dir.mkdir(parents=True, exist_ok=True)
        (args.output_dir / "adequacy_summary.json").write_text(rendered + "\n", encoding="utf-8")
    print(rendered)


if __name__ == "__main__":
    main()
