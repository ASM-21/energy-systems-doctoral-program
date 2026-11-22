# Competing-Risks Survival Analysis for DER Interconnection

A transparent standard-library implementation of the Kaplan-Meier net-approval curve and Aalen-Johansen cause-specific cumulative-incidence functions. The examples are synthetic. This lab exists to teach the methods needed for future application-level interconnection data; it does not estimate PPL or Pennsylvania processing outcomes.

## Run

```bash
python -m unittest -v
python run_example.py
```

## Why competing risks matter

An application may end in approval, withdrawal, or denial. These are distinct terminal events. An application still open at the data cutoff is right-censored. Treating withdrawal and denial as ordinary independent censoring in a Kaplan-Meier analysis estimates a hypothetical net approval risk under an independent-censoring assumption. It does not estimate the observed probability that an application is approved by time t in the presence of competing outcomes.

The Aalen-Johansen estimator updates the event-free probability using all observed causes and allocates probability mass to each cause-specific cumulative-incidence function. With the included six-record test fixture, the approval cumulative incidence is 5/12 at day 3, while one-minus-Kaplan-Meier net approval risk is 7/12. The difference is not a coding defect; it is a different estimand.

## Data structure required for a real application cohort

Each record needs a unique application identifier, a defensible time origin (for example, complete-application date), elapsed follow-up time, terminal event type, censoring date, and covariates known at or before the relevant decision point. Repeated applications from the same project/customer, EDC/feeder clustering, review-level transitions, and changing rule eligibility require explicit treatment.

The example CSV contains synthetic identifiers and durations only. It must never be merged with or described as actual utility application data.

## Monte Carlo estimator validation

The example also simulates 10,000 synthetic applications under constant independent exponential cause-specific hazards, applies administrative censoring, and compares the estimated approval cumulative incidence with its closed-form value. The one-minus-Kaplan-Meier curve is compared with the corresponding net-risk quantity. This tests the estimators against a known data-generating process and demonstrates that the two curves target different probabilities. The simulation is deterministic for a fixed seed and remains a teaching example, not a calibration to Pennsylvania applications.

## Core references

- Aalen, O. O. and Johansen, S. (1978). “An empirical transition matrix for non-homogeneous Markov chains based on censored observations.” *Scandinavian Journal of Statistics*, 5, 141–150. [Journal record](https://www.jstor.org/stable/4615704). Foundational transition-matrix estimator.
- Putter, H., Fiocco, M., and Geskus, R. B. (2007). “Tutorial in biostatistics: competing risks and multi-state models.” *Statistics in Medicine*, 26(11), 2389–2430. [DOI](https://doi.org/10.1002/sim.2712). Practical review of data preparation, cumulative incidence, and multi-state models.
- Fine, J. P. and Gray, R. J. (1999). “A proportional hazards model for the subdistribution of a competing risk.” *Journal of the American Statistical Association*, 94, 496–509. [DOI](https://doi.org/10.1080/01621459.1999.10474144). Regression model for subdistribution hazards; not implemented in this basic lab.
- Gray, R. J. (1988). “A class of K-sample tests for comparing the cumulative incidence of a competing risk.” *The Annals of Statistics*, 16(3), 1141–1154. [DOI](https://doi.org/10.1214/aos/1176350951). Group comparison for cumulative-incidence functions.

## Statistical limitations

- Non-informative censoring is required for the relevant estimator; censoring may be informative if difficult applications remain open longer.
- Cause definitions must be mutually exclusive and consistently recorded.
- Time origin and eligibility must be consistent across cohorts.
- The basic estimators are unadjusted. Covariate adjustment, competing-risks regression, frailty, time-varying treatment, and cluster-robust inference require additional methods and diagnostics.
- The simple implementation assumes events at tied times occur before censoring removals at that time.
- Aalen-Johansen estimates descriptive cumulative incidence; it does not identify a causal effect of a policy change.

See the [Pennsylvania DER interconnection capstone](../../policy-analysis/pa-distribution-interconnection-capstone/README.md) for the public aggregate-data baseline and the application-level data requirements.
