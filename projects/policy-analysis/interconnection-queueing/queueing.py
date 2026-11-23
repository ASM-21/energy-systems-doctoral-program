"""M/M/c queueing calculations and reproducible discrete-event simulation.

All examples are synthetic. Rates use a common time unit, such as applications
per business day and services per business day per reviewer.
"""
from __future__ import annotations

import heapq
import math
import random


def mmc_metrics(arrival_rate: float, service_rate: float, servers: int) -> dict:
    """Return steady-state M/M/c metrics using the Erlang-C formula."""
    if not math.isfinite(arrival_rate) or arrival_rate <= 0:
        raise ValueError("arrival_rate must be finite and positive")
    if not math.isfinite(service_rate) or service_rate <= 0:
        raise ValueError("service_rate must be finite and positive")
    if not isinstance(servers, int) or isinstance(servers, bool) or servers < 1:
        raise ValueError("servers must be a positive integer")
    utilization = arrival_rate / (servers * service_rate)
    if utilization >= 1:
        raise ValueError("M/M/c system is unstable: arrival rate must be below total service capacity")

    offered_load = arrival_rate / service_rate
    partial_sum = sum(offered_load ** n / math.factorial(n) for n in range(servers))
    tail_term = offered_load ** servers / (
        math.factorial(servers) * (1.0 - utilization)
    )
    p_zero = 1.0 / (partial_sum + tail_term)
    probability_wait = tail_term * p_zero
    mean_queue_wait = probability_wait / (servers * service_rate - arrival_rate)
    mean_system_time = mean_queue_wait + 1.0 / service_rate
    mean_queue_length = arrival_rate * mean_queue_wait
    mean_system_size = arrival_rate * mean_system_time

    return {
        "arrival_rate": arrival_rate,
        "service_rate_per_server": service_rate,
        "servers": servers,
        "utilization": utilization,
        "probability_wait": probability_wait,
        "probability_zero_in_system": p_zero,
        "mean_queue_wait": mean_queue_wait,
        "mean_system_time": mean_system_time,
        "mean_queue_length": mean_queue_length,
        "mean_system_size": mean_system_size,
        "little_law_queue_residual": mean_queue_length - arrival_rate * mean_queue_wait,
        "little_law_system_residual": mean_system_size - arrival_rate * mean_system_time,
    }



def mg1_metrics(arrival_rate: float, mean_service_time: float,
                service_coefficient_of_variation: float) -> dict:
    """Return Pollaczek-Khinchine steady-state metrics for an M/G/1 FCFS queue."""
    values = (arrival_rate, mean_service_time, service_coefficient_of_variation)
    if any(not math.isfinite(value) for value in values):
        raise ValueError("M/G/1 inputs must be finite")
    if arrival_rate <= 0 or mean_service_time <= 0:
        raise ValueError("arrival rate and mean service time must be positive")
    if service_coefficient_of_variation < 0:
        raise ValueError("service coefficient of variation must be nonnegative")
    utilization = arrival_rate * mean_service_time
    if utilization >= 1:
        raise ValueError("M/G/1 system is unstable: utilization must be below one")
    second_moment = mean_service_time ** 2 * (
        1.0 + service_coefficient_of_variation ** 2
    )
    mean_queue_wait = (
        arrival_rate * second_moment / (2.0 * (1.0 - utilization))
    )
    mean_system_time = mean_queue_wait + mean_service_time
    mean_queue_length = arrival_rate * mean_queue_wait
    mean_system_size = arrival_rate * mean_system_time
    return {
        "arrival_rate": arrival_rate,
        "mean_service_time": mean_service_time,
        "service_coefficient_of_variation": service_coefficient_of_variation,
        "utilization": utilization,
        "service_time_second_moment": second_moment,
        "mean_queue_wait": mean_queue_wait,
        "mean_system_time": mean_system_time,
        "mean_queue_length": mean_queue_length,
        "mean_system_size": mean_system_size,
    }


def staffing_cost(metrics: dict, server_cost_per_period: float,
                  waiting_cost_per_application_period: float) -> float:
    """Illustrative server + queueing cost per common period.

    Waiting cost is a scenario parameter, not an observed customer-damage value.
    """
    if server_cost_per_period < 0 or waiting_cost_per_application_period < 0:
        raise ValueError("cost parameters must be nonnegative")
    return (
        metrics["servers"] * server_cost_per_period
        + metrics["mean_queue_length"] * waiting_cost_per_application_period
    )


def simulate_mmc(arrival_rate: float, service_rate: float, servers: int,
                 customers: int = 100_000, warmup: int = 10_000,
                 seed: int = 20261122) -> dict:
    """Simulate FCFS M/M/c arrivals and service using server availability times."""
    if not math.isfinite(arrival_rate) or arrival_rate <= 0:
        raise ValueError("arrival_rate must be finite and positive")
    if not math.isfinite(service_rate) or service_rate <= 0:
        raise ValueError("service_rate must be finite and positive")
    if not isinstance(servers, int) or isinstance(servers, bool) or servers < 1:
        raise ValueError("servers must be a positive integer")
    if arrival_rate >= servers * service_rate:
        raise ValueError("simulation requires a stable queue")
    if not isinstance(customers, int) or customers <= 1:
        raise ValueError("customers must be an integer greater than one")
    if not isinstance(warmup, int) or warmup < 0 or warmup >= customers:
        raise ValueError("warmup must be an integer in [0, customers)")

    rng = random.Random(seed)
    server_free = [0.0] * servers
    heapq.heapify(server_free)
    time = 0.0
    waits = []
    waited = 0

    for i in range(customers):
        time += rng.expovariate(arrival_rate)
        next_free = heapq.heappop(server_free)
        start = max(time, next_free)
        wait = start - time
        service = rng.expovariate(service_rate)
        heapq.heappush(server_free, start + service)
        if i >= warmup:
            waits.append(wait)
            waited += wait > 0.0

    return {
        "customers_observed": len(waits),
        "mean_queue_wait": sum(waits) / len(waits),
        "probability_wait": waited / len(waits),
        "seed": seed,
        "warmup_customers": warmup,
    }
