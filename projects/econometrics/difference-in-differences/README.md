# Difference-in-Differences and Staggered Adoption Lab

A transparent implementation of a two-group/two-period DID contrast and cohort-time ATT estimator for balanced panels with never-treated controls. The example deliberately uses heterogeneous treatment effects across adoption cohorts and event time.

## Run

```bash
python -m unittest -v
python run_example.py
```

## Design

Each unit has a first treatment period (cohort) or is never treated. For cohort g, the estimator uses period g-1 as its baseline and never-treated units as controls to estimate ATT(g,t) for periods t at or after g:

\[
ATT(g,t)=
\left[\bar Y_{g,t}-\bar Y_{g,g-1}\right]
-
\left[\bar Y_{C,t}-\bar Y_{C,g-1}\right].
\]

The synthetic panel includes two adoption cohorts and a never-treated group. Treatment effects grow over event time and differ across cohorts. The estimator recovers the known cohort-time effects because the synthetic data satisfy common untreated trends by construction.

## Why this is not conventional TWFE

The implementation does not estimate a single two-way fixed-effects regression. It explicitly uses never-treated controls and cohort-specific baselines. This avoids using already-treated units as controls in the example. In real applications, never-treated units may not exist or may not be comparable; not-yet-treated controls can be used only with assumptions and methods designed for the corresponding treatment timing.

## Limitations

- Balanced panel required.
- Never-treated comparison units required.
- No covariate adjustment or conditional parallel-trends model.
- No cluster-robust standard errors or confidence intervals.
- No anticipation, treatment reversals, spillovers, or missing outcomes.
- The estimator is illustrative and does not validate parallel trends in empirical data.
- A correct estimator cannot repair invalid comparison groups or policy timing.

For theory and current staggered-adoption methods, see Callaway and Sant'Anna (2021), [DOI](https://doi.org/10.1016/j.jeconom.2020.12.001), and Sun and Abraham (2021), [DOI](https://doi.org/10.1016/j.jeconom.2020.09.006).

See [Graduate Econometrics Problem Set 3](../../../courses/year-2/graduate-econometrics-causal-inference/problem-set-03-panel-did-event-studies.md) and its [worked solutions](../../../courses/year-2/graduate-econometrics-causal-inference/problem-set-03-panel-did-event-studies-solutions.md).
