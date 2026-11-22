# Computational Lab: Stochastic Resource-Adequacy Screening

**Course:** Advanced Mathematical Methods for Energy Systems and Infrastructure Research  
**Methods:** Markov chains, repairable two-state unit availability, Monte Carlo simulation  
**Data:** Fully synthetic; no utility or PJM operating data

## Objective

Estimate illustrative loss-of-load hours and expected unserved energy under uncertain load, persistent renewable-output regimes, and a repairable generation outage. The lab connects probability, Markov processes, Monte Carlo uncertainty, and resource-adequacy concepts.

## Run

```bash
python adequacy.py --years 20 --seed 20261122
python -m unittest discover -s . -p "test_*.py" -v
```

The implementation uses only the Python standard library. The default run simulates 20 synthetic years of 8,760 hourly intervals each. Results are deterministic for a fixed seed and parameter set.

## Model

Weather regime has two states, Low and High renewable output, with transition matrix

[
P=\begin{bmatrix}0.9&0.1\\0.3&0.7\end{bmatrix}.
]

The stationary probability of the High state is 0.25. Renewable output is fixed at 100 MW in Low and 400 MW in High. Load is independently sampled from a normal distribution with mean 1,000 MW and standard deviation 80 MW.

A 100 MW generation block follows a two-state availability chain. Its hourly failure transition probability is 0.001 and its repair transition probability is 0.0323333, giving a stationary outage probability of approximately 3%. The remaining firm capacity is 950 MW. Initial weather and unit states are sampled from their stationary distributions.

The model records:
- **LOLE:** shortage hours per simulated year;
- **EUE:** expected unserved energy, in MWh per simulated year;
- **Hourly LOLP:** fraction of simulated hours with a shortage.

The reported standard errors describe variation across simulated annual outcomes. They do not measure model uncertainty or correct misspecified assumptions.

## Required analysis

1. Reproduce the stationary weather and outage probabilities analytically.
2. Run at least 100 simulated years and report mean and 5th/50th/95th percentile annual LOLE and EUE.
3. Change the weather transition probabilities while preserving the stationary distribution. Explain how persistence changes the distribution of annual shortage outcomes even if the long-run state share is unchanged.
4. Change the failure and repair rates while preserving the stationary outage probability. Explain the effect of outage duration and clustering.
5. Increase firm capacity in 25 MW increments and plot or tabulate LOLE and EUE. Discuss Monte Carlo noise and the value of common random numbers for scenario comparisons.
6. Explain why independent load sampling is a major limitation when weather affects both load and renewable availability.

## Limitations

This is a synthetic screening exercise, not a probabilistic resource-adequacy assessment. It omits empirical calibration, weather-load dependence, spatial renewable correlation, transmission constraints, storage, demand response, multiple generator classes, common-cause failures, cascading outages, and policy-defined reliability metrics. Its outputs must not be represented as PJM or utility LOLE/EUE estimates.
