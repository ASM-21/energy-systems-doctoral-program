# Utility Regulatory Economics: Cost Allocation, Incentives, and Investment

**Status:** Reproducible synthetic teaching model  
**Course connection:** Y2-03 Infrastructure Economics and Utility Investment, Problem Sets 1–4  
**Dependencies:** Python 3.10+; standard library only

## Research question

How do class cost allocation, tariff billing determinants, regulatory lag, savings-sharing mechanisms, and capital-budgeting assumptions change the distribution and timing of utility costs and benefits?

This project provides small, transparent functions for the calculations in Y2-03. It is intended to make assumptions visible and results reproducible, not to automate an actual rate case.

## Model components

- **Cost allocation:** allocates separate customer-, demand-, and energy-related pools using their stated class determinants; checks pool reconciliation.
- **Three-part rate design:** calculates fixed, demand, and volumetric rates from aggregate billing determinants.
- **Representative bills:** separates fixed, demand, and energy components.
- **Regulatory incentive comparison:** compares a fixed operating-cost allowance, a stylized annual cost reset, and an earnings-sharing allocation.
- **Capital budgeting:** calculates annuity factors, NPV, and scenario-weighted NPV when a discrete benefit state is assumed to persist over the modeled horizon.

## Run

From this directory:

```bash
python -m unittest discover -s . -p "test_*.py" -v
python utility_regulation.py
python utility_regulation.py --output-json /tmp/utility-regulation-example.json
```

No third-party package is required.

## Validation

The tests check:
- pool-level and class-level cost reconciliation;
- the three-part tariff's aggregate recovery of the stipulated $100 million;
- a representative residential bill against the hand calculation;
- the three-year savings-sharing example;
- annuity factors, base-case NPV, scenario NPVs, and expected NPV;
- rejection of invalid determinants, negative cost inputs, malformed sharing fractions, invalid discount rates, and probabilities that do not sum to one.

## Interpretation and limitations

The code does not implement:
- a jurisdiction-specific functionalization/classification/allocation study;
- rate-base accounting, income-tax normalization, deferred taxes, CWIP, or revenue requirement construction;
- tariff riders, time-of-use schedules, minimum bills, ratchets, losses, billing determinants, or class migration;
- customer-level load distributions or affordability analysis;
- prudence review, used-and-useful determinations, formula-rate protocols, or legal authority;
- a utility's actual income statement, capital structure, tax position, or regulatory lag;
- stochastic paths with year-to-year transitions, correlation, real options, or risk-adjusted discount rates.

The incentive function is a deliberately narrow operating-cost illustration. Its annual-reset case assumes a full contemporaneous reset to actual prudent operating cost; actual rate proceedings use test years, forecasts, adjustments, review, and procedural lag. The capital-budgeting model assumes level end-of-year net benefits. Its scenario-weighted function assumes a single state persists across all years; it is not a Monte Carlo model or a complete risk analysis.

A shadow value, allocated cost, rate, or NPV is conditional on the model's assumptions. None should be presented as an actual utility tariff, approved cost responsibility, customer bill forecast, or regulatory finding.

## Suggested extensions

1. Add a class-specific rate-design engine using customer-level synthetic load shapes and compare class revenue reconciliation.
2. Add revenue decoupling separately from cost trackers and quantify how sales-volume deviations affect collections.
3. Add a multi-year rate plan with an inflation factor, productivity offset, and efficiency carryover.
4. Add stochastic annual benefit paths with correlated states and a pilot/abandonment decision tree.
5. Compare project NPV with bill impacts and distributional incidence without treating transfers as net societal benefits.

## Related curriculum

- [Y2-03 course guide](../../../courses/year-2/infrastructure-economics-utility-investment/README.md)
- [PS1: Revenue requirement, rate base, and WACC](../../../courses/year-2/infrastructure-economics-utility-investment/problem-set-01-revenue-requirement.md)
- [PS2: Cost allocation and rate design](../../../courses/year-2/infrastructure-economics-utility-investment/problem-set-02-cost-allocation-rate-design.md)
- [PS3: Regulatory lag and incentives](../../../courses/year-2/infrastructure-economics-utility-investment/problem-set-03-regulatory-lag-incentives.md)
- [PS4: Capital budgeting under uncertainty](../../../courses/year-2/infrastructure-economics-utility-investment/problem-set-04-capital-budgeting-uncertainty.md)
