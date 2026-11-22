"""Transparent randomized-experiment estimators and design calculations."""
from __future__ import annotations

import random
from math import isfinite, sqrt


def random_assignment(n, n_treated, seed=21):
    if not isinstance(n, int) or n <= 1:
        raise ValueError("n must be an integer greater than one")
    if not isinstance(n_treated, int) or not 0 < n_treated < n:
        raise ValueError("n_treated must be between zero and n")
    treated = set(random.Random(seed).sample(range(n), n_treated))
    return [1 if i in treated else 0 for i in range(n)]


def _sample_variance(values):
    if len(values) < 2:
        raise ValueError("at least two observations are required per arm")
    mean = sum(values) / len(values)
    return sum((value - mean) ** 2 for value in values) / (len(values) - 1)


def estimate_difference_in_means(outcomes, assignment):
    if len(outcomes) != len(assignment) or not outcomes:
        raise ValueError("outcomes and assignment must have the same nonzero length")
    if any(not isinstance(y, (int, float)) or not isfinite(y) for y in outcomes):
        raise ValueError("outcomes must be finite numeric values")
    if any(d not in (0, 1) for d in assignment):
        raise ValueError("assignment must contain only 0 and 1")
    treated = [float(y) for y, d in zip(outcomes, assignment) if d == 1]
    control = [float(y) for y, d in zip(outcomes, assignment) if d == 0]
    if len(treated) < 2 or len(control) < 2:
        raise ValueError("at least two observations are required in each arm")
    estimate = sum(treated) / len(treated) - sum(control) / len(control)
    standard_error = sqrt(
        _sample_variance(treated) / len(treated)
        + _sample_variance(control) / len(control)
    )
    return {
        "estimate": estimate,
        "standard_error": standard_error,
        "n_treated": len(treated),
        "n_control": len(control),
    }


def randomization_test(outcomes, assignment, permutations=5000, seed=21):
    """Two-sided Monte Carlo Fisher test under complete random assignment."""
    observed = estimate_difference_in_means(outcomes, assignment)["estimate"]
    n = len(assignment)
    n_treated = sum(assignment)
    if not isinstance(permutations, int) or permutations <= 0:
        raise ValueError("permutations must be a positive integer")
    rng = random.Random(seed)
    extreme = 0
    indices = list(range(n))
    for _ in range(permutations):
        treated = set(rng.sample(indices, n_treated))
        permuted = [1 if i in treated else 0 for i in indices]
        statistic = estimate_difference_in_means(outcomes, permuted)["estimate"]
        if abs(statistic) >= abs(observed) - 1e-12:
            extreme += 1
    return {
        "observed_statistic": observed,
        "permutations": permutations,
        "extreme_count": extreme,
        "p_value": (extreme + 1) / (permutations + 1),
        "null": "sharp null of no effect for any unit",
    }


def mde_two_sided_80_power(sigma, n_treated, n_control):
    """Normal-approximation MDE for two-sided alpha=.05 and 80% power."""
    if not isinstance(sigma, (int, float)) or not isfinite(sigma) or sigma <= 0:
        raise ValueError("sigma must be finite and positive")
    if n_treated <= 0 or n_control <= 0:
        raise ValueError("arm sample sizes must be positive")
    z_alpha = 1.96
    z_power = 0.84
    return (z_alpha + z_power) * sigma * sqrt(1 / n_treated + 1 / n_control)


def cluster_design_effect(mean_cluster_size, intraclass_correlation):
    if not isinstance(mean_cluster_size, (int, float)) or not isfinite(mean_cluster_size) or mean_cluster_size < 1:
        raise ValueError("mean cluster size must be finite and at least one")
    if (not isinstance(intraclass_correlation, (int, float))
            or not isfinite(intraclass_correlation)
            or not 0 <= intraclass_correlation <= 1):
        raise ValueError("ICC must be between zero and one")
    return 1 + (mean_cluster_size - 1) * intraclass_correlation


def simulate_outcomes(x, assignment, effect, heterogeneity=0.0, noise_sd=1.0, seed=21):
    """Synthetic continuous outcomes with baseline covariate and heterogeneous effect."""
    if len(x) != len(assignment) or not x:
        raise ValueError("x and assignment must have the same nonzero length")
    if any(not isinstance(value, (int, float)) or not isfinite(value) for value in x):
        raise ValueError("x values must be finite")
    if any(d not in (0, 1) for d in assignment):
        raise ValueError("assignment must contain only 0 and 1")
    if not isfinite(effect) or not isfinite(heterogeneity):
        raise ValueError("effect parameters must be finite")
    if not isfinite(noise_sd) or noise_sd < 0:
        raise ValueError("noise_sd must be finite and nonnegative")
    rng = random.Random(seed)
    return [
        0.5 + 0.3 * value + d * (effect + heterogeneity * value)
        + rng.gauss(0, noise_sd)
        for value, d in zip(x, assignment)
    ]
