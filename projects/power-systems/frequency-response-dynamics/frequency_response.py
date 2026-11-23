"""Illustrative two-state frequency-response model.

All state and disturbance quantities are normalized per-unit deviations.
This teaching model is not an operational grid simulation.
"""
from __future__ import annotations

import argparse
import cmath
import json
from math import isfinite
from pathlib import Path

M = 5.0
D = 1.0
T_G = 0.5
R = 0.05


def state_matrix(inertia: float = M, damping: float = D,
                 governor_time: float = T_G, droop: float = R) -> tuple[tuple[float, float], tuple[float, float]]:
    parameters = (inertia, damping, governor_time, droop)
    if any(not isfinite(value) for value in parameters):
        raise ValueError("state-matrix parameters must be finite")
    if min(inertia, damping, governor_time, droop) <= 0:
        raise ValueError("inertia, damping, governor_time, and droop must be positive")
    return (
        (-damping / inertia, 1.0 / inertia),
        (-1.0 / (governor_time * droop), -1.0 / governor_time),
    )


def eigenvalues_2x2(matrix: tuple[tuple[float, float], tuple[float, float]]) -> tuple[complex, complex]:
    a, b = matrix[0]
    c, d = matrix[1]
    trace = a + d
    determinant = a * d - b * c
    discriminant = trace * trace - 4.0 * determinant
    root = cmath.sqrt(discriminant)
    return ((trace + root) / 2.0, (trace - root) / 2.0)


def steady_state(load_step: float, damping: float = D, droop: float = R) -> tuple[float, float]:
    if any(not isfinite(value) for value in (load_step, damping, droop)):
        raise ValueError("load step, damping, and droop must be finite")
    if damping <= 0 or droop <= 0:
        raise ValueError("damping and droop must be positive")
    frequency = -load_step / (damping + 1.0 / droop)
    mechanical_power = -frequency / droop
    return frequency, mechanical_power


def derivative(state: tuple[float, float], load_step: float,
               matrix: tuple[tuple[float, float], tuple[float, float]],
               inertia: float = M) -> tuple[float, float]:
    """Evaluate the state equation; inertia must match the supplied matrix."""
    if not isfinite(inertia) or inertia <= 0 or not isfinite(load_step):
        raise ValueError("inertia must be positive and load_step must be finite")
    frequency, mechanical_power = state
    return (
        matrix[0][0] * frequency + matrix[0][1] * mechanical_power - load_step / inertia,
        matrix[1][0] * frequency + matrix[1][1] * mechanical_power,
    )


def add_scaled(state: tuple[float, float], slope: tuple[float, float],
               scale: float) -> tuple[float, float]:
    return state[0] + scale * slope[0], state[1] + scale * slope[1]


def rk4_step(state: tuple[float, float], load_step: float, step: float,
             matrix: tuple[tuple[float, float], tuple[float, float]],
             inertia: float = M) -> tuple[float, float]:
    k1 = derivative(state, load_step, matrix, inertia)
    k2 = derivative(add_scaled(state, k1, step / 2), load_step, matrix, inertia)
    k3 = derivative(add_scaled(state, k2, step / 2), load_step, matrix, inertia)
    k4 = derivative(add_scaled(state, k3, step), load_step, matrix, inertia)
    return (
        state[0] + step * (k1[0] + 2*k2[0] + 2*k3[0] + k4[0]) / 6,
        state[1] + step * (k1[1] + 2*k2[1] + 2*k3[1] + k4[1]) / 6,
    )


def simulate_rk4(load_step: float = 0.01, duration: float = 10.0,
                 step: float = 0.001, *, inertia: float = M, damping: float = D,
                 governor_time: float = T_G, droop: float = R) -> tuple[float, float]:
    if any(not isfinite(value) for value in (load_step, duration, step)):
        raise ValueError("load step, duration, and step must be finite")
    if duration < 0 or step <= 0:
        raise ValueError("duration must be nonnegative and step must be positive")
    matrix = state_matrix(inertia, damping, governor_time, droop)
    state = (0.0, 0.0)
    count = int(duration / step)
    for _ in range(count):
        state = rk4_step(state, load_step, step, matrix, inertia)
    remainder = duration - count * step
    if remainder > 1e-12:
        state = rk4_step(state, load_step, remainder, matrix, inertia)
    return state


def euler_stability_limit(matrix: tuple[tuple[float, float], tuple[float, float]]) -> float:
    values = eigenvalues_2x2(matrix)
    if any(value.real >= 0 for value in values):
        return 0.0
    # For a complex-conjugate pair, |1 + h*lambda| < 1.
    value = values[0]
    if abs(value.imag) > 1e-12:
        return -2.0 * value.real / (abs(value) ** 2)
    return min(-2.0 / value.real for value in values)


def simulate_euler(initial: tuple[float, float], duration: float, step: float,
                   matrix: tuple[tuple[float, float], tuple[float, float]] | None = None,
                   inertia: float = M) -> tuple[float, float]:
    if any(not isfinite(value) for value in (*initial, duration, step)):
        raise ValueError("initial state, duration, and step must be finite")
    if duration < 0 or step <= 0:
        raise ValueError("duration must be nonnegative and step must be positive")
    if not isfinite(inertia) or inertia <= 0:
        raise ValueError("inertia must be finite and positive")
    if matrix is None:
        matrix = state_matrix(inertia=inertia)
    state = initial
    count = int(duration / step)
    for _ in range(count):
        slope = derivative(state, 0.0, matrix, inertia)
        state = add_scaled(state, slope, step)
    remainder = duration - count * step
    if remainder > 1e-12:
        slope = derivative(state, 0.0, matrix, inertia)
        state = add_scaled(state, slope, remainder)
    return state


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--load-step", type=float, default=0.01)
    parser.add_argument("--duration", type=float, default=10.0)
    parser.add_argument("--step", type=float, default=0.001)
    parser.add_argument("--inertia", type=float, default=M)
    parser.add_argument("--damping", type=float, default=D)
    parser.add_argument("--governor-time", type=float, default=T_G)
    parser.add_argument("--droop", type=float, default=R)
    parser.add_argument("--output-dir", type=Path)
    args = parser.parse_args()

    matrix = state_matrix(args.inertia, args.damping, args.governor_time, args.droop)
    eigenvalues = eigenvalues_2x2(matrix)
    result = {
        "model": "illustrative_two_state_frequency_response",
        "load_step_pu": args.load_step,
        "parameters": {
            "inertia_seconds": args.inertia,
            "damping": args.damping,
            "governor_time_seconds": args.governor_time,
            "droop": args.droop,
        },
        "state_matrix": matrix,
        "eigenvalues_per_second": [[v.real, v.imag] for v in eigenvalues],
        "explicit_euler_max_step_seconds": euler_stability_limit(matrix),
        "steady_state": steady_state(args.load_step, args.damping, args.droop),
        "rk4_terminal_state": simulate_rk4(
            args.load_step, args.duration, args.step,
            inertia=args.inertia, damping=args.damping,
            governor_time=args.governor_time, droop=args.droop,
        ),
        "duration_seconds": args.duration,
        "rk4_step_seconds": args.step,
        "limitations": "synthetic single-area linear illustration; not an operational security assessment",
    }
    rendered = json.dumps(result, indent=2)
    if args.output_dir:
        args.output_dir.mkdir(parents=True, exist_ok=True)
        (args.output_dir / "frequency_response_summary.json").write_text(rendered + "\n", encoding="utf-8")
    print(rendered)


if __name__ == "__main__":
    main()
