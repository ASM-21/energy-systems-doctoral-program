# Queueing Theory for DER Interconnection Review Capacity

**Purpose:** Teach queueing theory, capacity utilization, waiting-time nonlinearities, and staffing trade-offs.  
**Status:** Synthetic analytical and simulation lab, not an empirical model of PPL or any Pennsylvania EDC.  
**Dependencies:** Python standard library only.

## Research question

How does reviewer capacity affect expected queue delay when applications arrive stochastically and review durations vary? The lab demonstrates why a process operating near full utilization can experience disproportionate waiting-time growth, even when average service capacity remains greater than average arrivals.

## Reproduce

```bash
python -m unittest -v
python run_example.py
```

The analytical implementation uses the Erlang-C formula for an M/M/c queue. The discrete-event simulation generates exponential interarrival and service times, uses a first-come/first-served discipline, and discards a configurable warm-up period. The fixed random seed makes the demonstration reproducible. The example also reports a two- versus three-reviewer sensitivity grid for arrival rates of 10, 12, 13.2, and 14 applications per modeled period.

## Model

- Arrivals follow a homogeneous Poisson process with rate \(\lambda\).
- Each of \(c\) parallel reviewers has an independent exponential service time with rate \(\mu\).
- Applicants join one FCFS queue and are served by the next available reviewer.
- There is no abandonment, priority class, rework, batch processing, or customer-controlled pause.
- A steady state exists only if \(\rho=\lambda/(c\mu)<1\).

The implementation reports utilization, probability an arrival must wait, expected queue wait, expected total time in system, expected queue length, and expected number in the system. Little's Law is checked numerically.

## Illustrative staffing comparison

With 12 arrivals per modeled period and a service rate of 8 applications per period per reviewer:

| Reviewers | Utilization | Probability of waiting | Mean queue wait | Mean system time |
|---:|---:|---:|---:|---:|
| 2 | 75.0% | 64.29% | 0.1607 periods | 0.2857 periods |
| 3 | 50.0% | 23.68% | 0.0197 periods | 0.1447 periods |

Adding a third reviewer reduces expected queue wait substantially in this synthetic case. If arrivals rise from 12 to 13.2 per period with two reviewers unchanged, utilization rises from 75% to 82.5% and expected queue wait rises from 0.1607 to approximately 0.2664 periods. This is a 65.75% increase in expected waiting from a 10% increase in arrivals. The example also calculates an illustrative total cost using a fixed reviewer cost and a per-application-period waiting penalty. Those cost coefficients are assumptions, not measured labor costs, customer damages, or utility values.

## Interpretation for actual interconnection processes

A real interconnection process is not necessarily an M/M/c queue. Service-time variability matters even when the mean service rate is unchanged: the M/G/1 Pollaczek–Khinchine formula depends on the second moment of service time, not only its mean. Problem Set 10 demonstrates a synthetic case in which increasing the service-time coefficient of variation from 1 to 2 raises mean queue wait from 0.375 to 0.9375 business day at the same arrival rate and mean service time. It may contain multiple sequential review stages, rework, priority classes, seasonal arrival peaks, project-size heterogeneity, customer response delays, parallel engineering disciplines, study batching, and right-censored open applications. A single pooled service rate can conceal bottlenecks. If a project waits for both protection and planning review, a network of queues or discrete-event process model may be more appropriate.

Before applying queueing theory to real process data, collect event-level timestamps and distinguish:
- time waiting for utility assignment;
- active engineering service time;
- time awaiting applicant information;
- time awaiting external studies or approvals;
- rework and repeat-study intervals;
- final approval, denial, withdrawal, and still-open status.

The model cannot infer causal effects of staffing, policy, or DERMS from aggregate annual request counts. It is a mechanism illustration and a guide to data requirements.

## Research extensions

1. Fit empirical arrival processes and test for seasonality and overdispersion.
2. Estimate service-time distributions by review level and project class; test exponential assumptions.
3. Build a multi-stage network with rework and customer-pause states.
4. Add priority disciplines and measure whether expedited classes increase delays for other classes.
5. Use discrete-event simulation to test staffing schedules under peak-arrival scenarios.
6. Compare simulated outputs with held-out event-history data before any policy interpretation.

## Data and model-risk controls

- [Event-history data requirements](data-requirements.md) specify the event-level records needed to estimate arrivals, queue waits, active service, pauses, rework, throughput, and censoring.
- [Queueing model-risk register](model-risk-register.csv) lists twelve failure modes and required diagnostics/mitigations.

The public PUC annual panel does not provide the timestamps needed to calibrate this model. These documents are specifications for future authorized data, not claims that such records are available.

## Validation

Tests verify exact M/M/2 and M/M/3 Erlang-C values, Little's Law identities, stability checks, cost arithmetic, reproducibility, and convergence of a large fixed-seed simulation toward analytical M/M/c expectations.
