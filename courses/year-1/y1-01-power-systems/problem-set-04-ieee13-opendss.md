# Y1-01 Problem Set 4 — IEEE 13-Node Feeder Benchmark

**Estimated time:** 4–6 hours  
**Benchmark:** [IEEE 13-node OpenDSS benchmark](../../../projects/power-systems/radial-der-hosting-capacity/benchmarks/ieee13-opendss/README.md)  
**Required engine:** DSS-Python 0.15.4

## Problem 1 — Establish the AC benchmark

Run the baseline IEEE 13-node case with zero added PV and the default load multiplier. Record the DSS-Python/OpenDSS engine version, source test-case snapshot, convergence status, iteration count, number of nodes, minimum and maximum node voltage, and real/reactive circuit losses.

Explain why the voltage vector is node-level rather than simply one scalar per named bus. Distinguish phase-node voltages from bus-level aggregates.

## Problem 2 — PV injection experiment

Run 100, 250, 500, 750, and 1,000 kW three-phase PV cases at bus 675. Keep the load multiplier and all other settings fixed.

1. Create a combined table of PV rating, minimum node voltage, maximum node voltage, real losses, reactive losses, and convergence iterations.
2. Plot minimum and maximum node voltage against PV rating.
3. Identify the nodes with the largest voltage increase relative to baseline.
4. Determine whether losses increase or decrease over the tested range and explain why the relationship need not be monotonic.
5. Apply a 1.05 pu upper-voltage screening criterion, but first inspect the zero-PV baseline. The initial verified CI run has a baseline maximum node voltage of 1.05605 pu, so this threshold is already exceeded before PV is added. Explain why this prevents interpreting the first 1.05 pu crossing as a PV-created hosting-capacity limit. Identify incremental voltage changes and propose a defensible criterion that separates pre-existing baseline conditions from DER-caused changes. Do not interpolate a precise hosting-capacity value from a coarse sweep.

## Problem 3 — Load sensitivity

Repeat the baseline and 500 kW PV cases at load multipliers 0.75 and 1.25. Explain how load level changes voltage response, reverse power-flow risk, and losses. Be explicit that the benchmark's load multiplier scales the published test-case loads uniformly and is not a measured daily load shape.

## Problem 4 — Engineering interpretation

Compare the unbalanced OpenDSS benchmark with the curriculum's balanced first-order radial screen. Discuss:
- phase-specific voltage effects and unbalanced loading;
- regulators, capacitors, transformers, and line models;
- nonlinear power flow and losses;
- inverter phase connection, power factor, and reactive-power controls;
- why a voltage-only criterion does not establish hosting capacity;
- why this benchmark cannot be treated as a PPL feeder model.

## Deliverables

- Reproducible command history and environment versions.
- Baseline and PV scenario output files.
- Combined scenario CSV and voltage sensitivity plot.
- 1,000–1,500 word technical note with assumptions, limitations, and a reproducibility appendix.

## Grading rubric

| Criterion | Weight |
|---|---:|
| Reproducible OpenDSS runs and provenance | 20% |
| Correct node-level data handling | 20% |
| Scenario analysis and visualization | 20% |
| Power-system interpretation | 25% |
| Limitations and reproducibility | 15% |
