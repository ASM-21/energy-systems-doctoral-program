# Randomized Experiments, Power, and Randomization Inference

A standard-library teaching implementation for complete random assignment, difference-in-means estimation, Neyman standard errors, Monte Carlo Fisher randomization tests, normal-approximation minimum detectable effects, and cluster design effects.

## Run

```bash
python -m unittest -v
python run_example.py
```

## Methods

- **Complete randomization:** assigns a fixed number of units to treatment while preserving the treatment count.
- **Difference in means:** estimates the ITT under randomized assignment.
- **Neyman standard error:** uses separate sample variances for treatment and control groups.
- **Randomization inference:** permutes assignment labels while preserving the complete-randomization design and tests the sharp null of no effect for any unit.
- **MDE:** uses a normal approximation for a two-sided 5% test and 80% power.
- **Cluster design effect:** uses (1+(m-1)ho) as a first-order approximation; it does not replace cluster-level power analysis.

## Scope and limitations

The code uses synthetic continuous outcomes and is not an empirical evaluation. The randomization test assumes the assignment mechanism implemented in the code; stratified or cluster randomization requires corresponding constrained permutations. The MDE approximation assumes a known/estimated standard deviation and ignores small-sample degrees-of-freedom adjustments. Cluster design effect is only a rough approximation and can be misleading with few clusters, unequal cluster sizes, or heterogeneous ICCs.

The example demonstrates methods, not evidence that application assistance would change utility processing outcomes. Ethical review, operational feasibility, treatment definition, interference, and external validity must be addressed in a real pilot.

See [Graduate Econometrics Problem Set 2](../../../courses/year-2/graduate-econometrics-causal-inference/problem-set-02-randomized-experiments.md) and its [worked solutions](../../../courses/year-2/graduate-econometrics-causal-inference/problem-set-02-randomized-experiments-solutions.md).
