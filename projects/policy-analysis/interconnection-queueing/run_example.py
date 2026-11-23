import json

from queueing import mmc_metrics, simulate_mmc, staffing_cost


def main():
    arrival_rate = 12.0
    service_rate = 8.0
    results = {}
    for servers in (2, 3):
        metrics = mmc_metrics(arrival_rate, service_rate, servers)
        metrics["illustrative_daily_cost"] = staffing_cost(metrics, 500, 300)
        metrics["simulation"] = simulate_mmc(
            arrival_rate, service_rate, servers, customers=100_000, warmup=10_000
        )
        results[str(servers)] = metrics
    sensitivity = {}
    for rate in (10.0, 12.0, 13.2, 14.0):
        sensitivity[str(rate)] = {
            str(servers): mmc_metrics(rate, service_rate, servers)
            for servers in (2, 3)
        }
    print(json.dumps({
        "arrival_rate_sensitivity": sensitivity,
        "note": "Synthetic M/M/c illustration; not utility staffing or service-time data.",
        "rates": {"arrivals_per_period": arrival_rate,
                  "service_rate_per_server_per_period": service_rate},
        "scenarios": results,
    }, indent=2))


if __name__ == "__main__":
    main()
