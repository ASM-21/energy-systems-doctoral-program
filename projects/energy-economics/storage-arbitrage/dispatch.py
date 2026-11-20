"""Deterministic battery arbitrage LP for nonnegative energy prices."""
from __future__ import annotations

import argparse
from scipy.optimize import linprog


def solve_storage(
    prices: list[float],
    energy_capacity_mwh: float = 10.0,
    power_limit_mw: float = 5.0,
    charge_efficiency: float = 0.9,
    discharge_efficiency: float = 0.9,
    degradation_cost_per_mwh: float = 0.0,
    initial_soc_mwh: float = 0.0,
    final_soc_mwh: float = 0.0,
) -> dict:
    if not prices:
        raise ValueError("At least one price interval is required.")
    if any(price < 0 for price in prices):
        raise ValueError("This continuous formulation assumes nonnegative prices.")
    if energy_capacity_mwh <= 0 or power_limit_mw <= 0:
        raise ValueError("Energy capacity and power limit must be positive.")
    if not 0 < charge_efficiency <= 1 or not 0 < discharge_efficiency <= 1:
        raise ValueError("Efficiencies must be in (0, 1].")
    if degradation_cost_per_mwh < 0:
        raise ValueError("Degradation cost must be nonnegative.")
    if not 0 <= initial_soc_mwh <= energy_capacity_mwh:
        raise ValueError("Initial state of charge is outside capacity.")
    if not 0 <= final_soc_mwh <= energy_capacity_mwh:
        raise ValueError("Final state of charge is outside capacity.")

    periods = len(prices)
    # Decision vector: [charge_0..T-1, discharge_0..T-1, SOC_0..T-1].
    objective = (
        [p + degradation_cost_per_mwh for p in prices]
        + [-p + degradation_cost_per_mwh for p in prices]
        + [0.0] * periods
    )

    a_eq = []
    b_eq = []
    for t in range(periods):
        row = [0.0] * (3 * periods)
        row[t] = charge_efficiency
        row[periods + t] = -1.0 / discharge_efficiency
        row[2 * periods + t] = -1.0
        if t > 0:
            row[2 * periods + t - 1] = 1.0
            b_eq.append(0.0)
        else:
            b_eq.append(-initial_soc_mwh)
        a_eq.append(row)

    terminal = [0.0] * (3 * periods)
    terminal[-1] = 1.0
    a_eq.append(terminal)
    b_eq.append(final_soc_mwh)

    bounds = (
        [(0.0, power_limit_mw)] * periods
        + [(0.0, power_limit_mw)] * periods
        + [(0.0, energy_capacity_mwh)] * periods
    )
    result = linprog(
        c=objective,
        A_eq=a_eq,
        b_eq=b_eq,
        bounds=bounds,
        method="highs",
    )
    if not result.success:
        raise RuntimeError(result.message)

    charge = [float(x) for x in result.x[:periods]]
    discharge = [float(x) for x in result.x[periods:2 * periods]]
    soc = [float(x) for x in result.x[2 * periods:]]
    gross_margin = sum(
        price * (d - c) for price, c, d in zip(prices, charge, discharge)
    )
    throughput = sum(charge) + sum(discharge)
    degradation_cost = degradation_cost_per_mwh * throughput

    return {
        "prices_usd_per_mwh": [float(p) for p in prices],
        "charge_mw": charge,
        "discharge_mw": discharge,
        "state_of_charge_mwh": soc,
        "gross_margin_usd": float(gross_margin),
        "throughput_mwh": float(throughput),
        "degradation_cost_usd": float(degradation_cost),
        "net_margin_usd": float(gross_margin - degradation_cost),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--prices",
        type=float,
        nargs="+",
        default=[20.0, 30.0, 80.0, 100.0],
        help="Nonnegative prices in $/MWh, one per one-hour interval",
    )
    parser.add_argument("--degradation-cost", type=float, default=0.0)
    args = parser.parse_args()

    result = solve_storage(
        args.prices,
        degradation_cost_per_mwh=args.degradation_cost,
    )
    for key, value in result.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
