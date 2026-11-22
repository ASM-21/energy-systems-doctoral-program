# Stochastic and Robust Capacity Planning Lab

A two-scenario capacity-planning example implemented as linear programs using SciPy/HiGHS. The model compares a two-stage stochastic solution, a deterministic expected-value solution evaluated under uncertainty, a wait-and-see benchmark, and a min-max robust solution.

## Run

```bash
python -m pip install -r requirements.txt
python -m unittest -v
python capacity_planning.py
```

## Synthetic case

A planner procures firm capacity before observing a one-hour demand realization.

| Scenario | Demand | Probability |
|---|---:|---:|
| Low | 80 MW | 0.4 |
| High | 120 MW | 0.6 |

Capacity costs $70/MW for the planning period, generation costs $5/MWh, and unserved demand is penalized at $100/MWh. These are illustrative teaching parameters, not market prices or a reliability standard.

## Expected results

| Formulation | Capacity | Objective / evaluated cost |
|---|---:|---:|
| Two-stage stochastic | 80 MW | $8,400 expected |
| Expected-value decision, evaluated under scenarios | 104 MW | $8,712 expected |
| Wait-and-see | 80 or 120 MW by scenario | $7,800 expected |
| Min-max robust | 120 MW | $9,000 worst-case |

The value of the stochastic solution is $312, and the expected value of perfect information is $600. The robust solution purchases more capacity because it minimizes the worst scenario cost rather than expected cost.

## Modeling interpretation

- The stochastic model makes one capacity decision before uncertainty is observed and permits scenario-specific dispatch and unserved demand afterward.
- The expected-value model replaces uncertain demand with its mean. Its resulting capacity decision is then evaluated against the original scenario distribution.
- The wait-and-see model is an information benchmark, not an implementable first-stage policy.
- The robust model minimizes the maximum scenario cost with a common first-stage capacity decision.

## Limitations

This is a one-period, two-scenario synthetic example. It omits transmission constraints, network losses, unit commitment, ramping, storage, correlated forecast errors, endogenous demand response, multi-period investment, and empirical scenario calibration. The penalty for unserved energy is an assumed objective coefficient, not an estimate of customer damage or a formal reliability criterion. Results are not a PJM or utility planning estimate.

See [Problem Set 8](../../../courses/year-2/advanced-mathematics-energy-systems/problem-set-08-stochastic-robust-optimization.md) and its [worked solutions](../../../courses/year-2/advanced-mathematics-energy-systems/problem-set-08-stochastic-robust-optimization-solutions.md).
