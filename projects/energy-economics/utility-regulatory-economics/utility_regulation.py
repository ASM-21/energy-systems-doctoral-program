"""Stylized utility cost-allocation, rate-design, incentive, and NPV models.

Teaching models only. Not a cost-of-service study, tariff calculator, utility
earnings forecast, or regulatory accounting engine.
"""
from __future__ import annotations
import argparse, json, math
from typing import Mapping, Sequence


def _nn(value: float, name: str) -> float:
    value = float(value)
    if not math.isfinite(value) or value < 0:
        raise ValueError(f"{name} must be finite and nonnegative")
    return value


def allocate_cost_pools(cost_pools: Mapping[str, float], class_determinants: Mapping[str, Mapping[str, float]]) -> dict[str, dict[str, float]]:
    """Allocate each pool to classes using its corresponding determinant."""
    if not cost_pools or set(cost_pools) != set(class_determinants):
        raise ValueError("Cost pools and determinant pool names must match")
    result = {}
    for pool, raw_cost in cost_pools.items():
        cost = _nn(raw_cost, f"{pool} cost")
        determinants = class_determinants[pool]
        if not determinants:
            raise ValueError(f"{pool} must contain at least one class")
        values = {str(k): _nn(v, f"{pool}/{k}") for k, v in determinants.items()}
        denominator = sum(values.values())
        if denominator <= 0:
            raise ValueError(f"{pool} determinant total must be positive")
        result[pool] = {k: cost * v / denominator for k, v in values.items()}
    return result


def class_totals(allocations: Mapping[str, Mapping[str, float]]) -> dict[str, float]:
    totals = {}
    for pool in allocations.values():
        for customer_class, amount in pool.items():
            totals[customer_class] = totals.get(customer_class, 0.0) + float(amount)
    return totals


def three_part_rates(customer_cost: float, demand_cost: float, energy_cost: float,
                     accounts: float, demand_kw: float, energy_kwh: float,
                     months: int = 12) -> dict[str, float]:
    costs = [_nn(v, n) for v, n in [(customer_cost, "customer_cost"), (demand_cost, "demand_cost"), (energy_cost, "energy_cost")]]
    determinants = [_nn(v, n) for v, n in [(accounts, "accounts"), (demand_kw, "demand_kw"), (energy_kwh, "energy_kwh")]]
    if not isinstance(months, int) or isinstance(months, bool) or months <= 0:
        raise ValueError("months must be a positive integer")
    if min(determinants) <= 0:
        raise ValueError("Each aggregate billing determinant must be positive")
    return {
        "fixed_per_account_month": costs[0] / (determinants[0] * months),
        "demand_per_kw_month": costs[1] / (determinants[1] * months),
        "energy_per_kwh": costs[2] / determinants[2],
    }


def representative_bill(rates: Mapping[str, float], annual_kwh: float, monthly_kw: float, months: int = 12) -> dict[str, float]:
    annual_kwh, monthly_kw = _nn(annual_kwh, "annual_kwh"), _nn(monthly_kw, "monthly_kw")
    if not isinstance(months, int) or isinstance(months, bool) or months <= 0:
        raise ValueError("months must be a positive integer")
    required = {"fixed_per_account_month", "demand_per_kw_month", "energy_per_kwh"}
    if set(rates) != required:
        raise ValueError(f"rates must contain exactly {sorted(required)}")
    fixed = _nn(rates["fixed_per_account_month"], "fixed rate") * months
    demand = _nn(rates["demand_per_kw_month"], "demand rate") * monthly_kw * months
    energy = _nn(rates["energy_per_kwh"], "energy rate") * annual_kwh
    total = fixed + demand + energy
    return {"fixed_annual": fixed, "demand_annual": demand, "energy_annual": energy,
            "total_annual": total, "average_monthly": total / months}


def incentive_scenarios(baseline_costs: Sequence[float], savings: Sequence[float],
                        implementation_costs: Sequence[float], fixed_allowance: float,
                        customer_share: float = 0.5) -> list[dict[str, float]]:
    """Compare fixed allowance, annual cost reset, and savings sharing."""
    if not baseline_costs or not (len(baseline_costs) == len(savings) == len(implementation_costs)):
        raise ValueError("Cost, savings, and implementation sequences must have equal nonzero length")
    allowance, share = _nn(fixed_allowance, "fixed_allowance"), float(customer_share)
    if not math.isfinite(share) or not 0 <= share <= 1:
        raise ValueError("customer_share must be between zero and one")
    results = []
    for year, (base, saving, implementation) in enumerate(zip(baseline_costs, savings, implementation_costs), 1):
        base, saving, implementation = _nn(base, "baseline cost"), _nn(saving, "savings"), _nn(implementation, "implementation cost")
        actual = base - saving + implementation
        if actual < 0:
            raise ValueError("Savings plus implementation cannot imply negative operating cost")
        net = base - actual
        results.append({
            "year": float(year), "cost_without_initiative": base, "cost_with_initiative": actual,
            "fixed_allowance_less_cost_without": allowance - base,
            "fixed_allowance_less_cost_with": allowance - actual,
            "incremental_utility_operating_position": net,
            "annual_reset_customer_savings": net,
            "sharing_customer_savings": net * share,
            "sharing_utility_retained": net * (1 - share),
        })
    return results


def annuity_factor(discount_rate: float, years: int) -> float:
    """Present-value factor for a level end-of-year annuity."""
    rate = float(discount_rate)
    if not math.isfinite(rate) or rate <= -1:
        raise ValueError("discount_rate must be finite and greater than -100%")
    if not isinstance(years, int) or isinstance(years, bool) or years <= 0:
        raise ValueError("years must be a positive integer")
    return float(years) if rate == 0 else (1 - (1 + rate) ** (-years)) / rate


def npv(initial_cost: float, annual_net_benefits: Sequence[float], discount_rate: float) -> float:
    initial = _nn(initial_cost, "initial_cost")
    rate = float(discount_rate)
    if not math.isfinite(rate) or rate <= -1:
        raise ValueError("discount_rate must be finite and greater than -100%")
    value = -initial
    for year, benefit in enumerate(annual_net_benefits, 1):
        benefit = float(benefit)
        if not math.isfinite(benefit):
            raise ValueError("annual benefits must be finite")
        value += benefit / ((1 + rate) ** year)
    return value


def expected_npv(initial_cost: float, scenario_annual_net_benefits: Mapping[str, float],
                 probabilities: Mapping[str, float], discount_rate: float, years: int) -> dict[str, float]:
    """Expected NPV where each mutually exclusive state persists for all years."""
    if not scenario_annual_net_benefits or set(scenario_annual_net_benefits) != set(probabilities):
        raise ValueError("Scenario and probability names must match and be nonempty")
    probs = {k: float(v) for k, v in probabilities.items()}
    if any(not math.isfinite(v) or v < 0 for v in probs.values()):
        raise ValueError("Probabilities must be finite and nonnegative")
    if not math.isclose(sum(probs.values()), 1.0, rel_tol=0, abs_tol=1e-9):
        raise ValueError("Probabilities must sum to one")
    annuity_factor(discount_rate, years)  # Validate the horizon even when benefits are zero.
    state_values = {k: npv(initial_cost, [float(b)] * years, discount_rate)
                    for k, b in scenario_annual_net_benefits.items()}
    return {"expected_npv": sum(probs[k] * state_values[k] for k in state_values),
            **{f"npv_{k}": v for k, v in state_values.items()}}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-json", help="Optional output JSON path")
    args = parser.parse_args()
    pools = {"customer": 40_000_000, "demand": 35_000_000, "energy": 25_000_000}
    determinants = {
        "customer": {"residential": 100_000, "commercial": 20_000},
        "demand": {"residential": 200_000, "commercial": 100_000},
        "energy": {"residential": 1_200_000_000, "commercial": 800_000_000},
    }
    allocations = allocate_cost_pools(pools, determinants)
    rates = three_part_rates(40_000_000, 35_000_000, 25_000_000, 120_000, 300_000, 2_000_000_000)
    result = {
        "allocated_class_costs": class_totals(allocations),
        "three_part_rates": rates,
        "residential_representative_bill": representative_bill(rates, 10_000, 5),
        "capital_budgeting_example_npv": npv(30_000_000, [5_000_000] * 10, 0.07),
        "limitations": "Stylized teaching calculations only; not a tariff, cost-of-service study, rate-case model, or investment recommendation.",
    }
    rendered = json.dumps(result, indent=2, sort_keys=True)
    if args.output_json:
        with open(args.output_json, "w", encoding="utf-8") as output:
            output.write(rendered + "\n")
    print(rendered)


if __name__ == "__main__":
    main()
