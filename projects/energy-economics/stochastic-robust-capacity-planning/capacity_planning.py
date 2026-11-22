"""Two-scenario capacity planning: stochastic, expected-value, and robust LPs."""
from scipy.optimize import linprog


SCENARIOS = (
    {"name": "low", "demand": 80.0, "probability": 0.4},
    {"name": "high", "demand": 120.0, "probability": 0.6},
)
CAPACITY_COST = 70.0
GENERATION_COST = 5.0
UNSERVED_COST = 100.0
CAPACITY_MAX = 120.0


def _require_success(result, model_name):
    if not result.success:
        raise RuntimeError(f"{model_name} optimization failed: {result.message}")
    return result


def solve_stochastic():
    """Solve the extensive-form two-stage stochastic LP."""
    # Variables: K, g_low, u_low, g_high, u_high.
    objective = [
        CAPACITY_COST,
        0.4 * GENERATION_COST, 0.4 * UNSERVED_COST,
        0.6 * GENERATION_COST, 0.6 * UNSERVED_COST,
    ]
    constraints = [
        [0, -1, -1, 0, 0],   # low demand served or unserved
        [0, 0, 0, -1, -1],   # high demand served or unserved
        [-1, 1, 0, 0, 0],    # low dispatch <= common capacity
        [-1, 0, 0, 1, 0],    # high dispatch <= common capacity
        [1, 0, 0, 0, 0],     # capacity upper bound
    ]
    rhs = [-80, -120, 0, 0, CAPACITY_MAX]
    result = _require_success(
        linprog(objective, A_ub=constraints, b_ub=rhs,
                bounds=[(0, None)] * 5, method="highs"),
        "stochastic",
    )
    k, gl, ul, gh, uh = result.x
    return {
        "capacity": float(k),
        "expected_cost": float(result.fun),
        "recourse": {
            "low": {"generation": float(gl), "unserved": float(ul)},
            "high": {"generation": float(gh), "unserved": float(uh)},
        },
    }


def solve_expected_value():
    """Solve at mean demand, then evaluate that capacity under original scenarios."""
    mean_demand = sum(s["demand"] * s["probability"] for s in SCENARIOS)
    objective = [CAPACITY_COST, GENERATION_COST, UNSERVED_COST]
    constraints = [
        [0, -1, -1],
        [-1, 1, 0],
        [1, 0, 0],
    ]
    rhs = [-mean_demand, 0, CAPACITY_MAX]
    result = _require_success(
        linprog(objective, A_ub=constraints, b_ub=rhs,
                bounds=[(0, None)] * 3, method="highs"),
        "expected-value",
    )
    capacity = float(result.x[0])
    evaluated_cost = CAPACITY_COST * capacity
    for scenario in SCENARIOS:
        generation = min(scenario["demand"], capacity)
        unserved = max(scenario["demand"] - capacity, 0.0)
        recourse_cost = GENERATION_COST * generation + UNSERVED_COST * unserved
        evaluated_cost += scenario["probability"] * recourse_cost
    return {
        "capacity": capacity,
        "deterministic_objective": float(result.fun),
        "evaluated_expected_cost": float(evaluated_cost),
    }


def solve_wait_and_see():
    """Return expected cost when capacity can be selected after demand is known."""
    expected_cost = 0.0
    decisions = {}
    for scenario in SCENARIOS:
        demand = scenario["demand"]
        objective = [CAPACITY_COST, GENERATION_COST, UNSERVED_COST]
        constraints = [
            [0, -1, -1],
            [-1, 1, 0],
            [1, 0, 0],
        ]
        rhs = [-demand, 0, CAPACITY_MAX]
        result = _require_success(
            linprog(objective, A_ub=constraints, b_ub=rhs,
                    bounds=[(0, None)] * 3, method="highs"),
            f"wait-and-see {scenario['name']}",
        )
        expected_cost += scenario["probability"] * float(result.fun)
        decisions[scenario["name"]] = {
            "capacity": float(result.x[0]),
            "cost": float(result.fun),
        }
    return {"expected_cost": expected_cost, "decisions": decisions}


def solve_robust():
    """Minimize the worst scenario cost with one common first-stage capacity."""
    # Variables: K, g_low, u_low, g_high, u_high, z (worst-case cost).
    objective = [0, 0, 0, 0, 0, 1]
    constraints = [
        [0, -1, -1, 0, 0, 0],
        [0, 0, 0, -1, -1, 0],
        [-1, 1, 0, 0, 0, 0],
        [-1, 0, 0, 1, 0, 0],
        [1, 0, 0, 0, 0, 0],
        [CAPACITY_COST, GENERATION_COST, UNSERVED_COST, 0, 0, -1],
        [CAPACITY_COST, 0, 0, GENERATION_COST, UNSERVED_COST, -1],
    ]
    rhs = [-80, -120, 0, 0, CAPACITY_MAX, 0, 0]
    result = _require_success(
        linprog(objective, A_ub=constraints, b_ub=rhs,
                bounds=[(0, None)] * 6, method="highs"),
        "robust",
    )
    return {
        "capacity": float(result.x[0]),
        "worst_case_cost": float(result.fun),
    }


def compare_models():
    stochastic = solve_stochastic()
    expected_value = solve_expected_value()
    wait_and_see = solve_wait_and_see()
    robust = solve_robust()
    return {
        "stochastic": stochastic,
        "expected_value": expected_value,
        "wait_and_see": wait_and_see,
        "robust": robust,
        "value_of_stochastic_solution": (
            expected_value["evaluated_expected_cost"] - stochastic["expected_cost"]
        ),
        "expected_value_of_perfect_information": (
            stochastic["expected_cost"] - wait_and_see["expected_cost"]
        ),
    }


if __name__ == "__main__":
    results = compare_models()
    for label, result in results.items():
        print(f"{label}: {result}")
