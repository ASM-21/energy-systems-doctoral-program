# Computational Lab: Two-Period Unit Commitment

**Course:** Y2-04 Electricity Market Design and Optimization  
**Model:** Mixed-integer linear unit commitment with startup and no-load costs  
**Data:** Synthetic two-unit, two-period case  
**Dependencies:** Python 3.10+, NumPy, SciPy (HiGHS MILP solver)

## Objective

Show how binary commitment decisions and nonconvex startup/no-load costs change dispatch and distinguish a unit-commitment solution from a convex economic-dispatch LP.

## Run

```bash
python -m pip install -r requirements.txt
python unit_commitment.py
python unit_commitment.py --relax-commitment
python unit_commitment.py --g1-startup-cost 1000
python unit_commitment.py --period-2-demand 120
python -m unittest discover -s . -p "test_*.py" -v
```

## Benchmark

Demand is 80 MW in Period 1 and 150 MW in Period 2. Both units start off.

- G1: energy $20/MWh, minimum 30 MW, maximum 100 MW, no-load $100/hour, startup $500.
- G2: energy $50/MWh, minimum 0 MW, maximum 100 MW, no-load $40/hour, startup $100.

Expected integer solution:
- G1: 80 MW in Period 1 and 100 MW in Period 2; on in both periods; one startup.
- G2: off in Period 1; 50 MW and on in Period 2; one startup.
- Energy cost $6,100; no-load cost $240; startup cost $600; total $6,940.

The LP relaxation has objective $6,850 and fractional commitment. This is a lower bound, not a physical schedule.

## Formulation and validation

The model uses continuous dispatch p, commitment y, and startup u. It imposes per-period energy balance, minimum/maximum output linked to y, and startup logic relative to the prior-period commitment. Unit commitment variables are binary unless --relax-commitment is selected.

Tests check the integer benchmark, cost components, LP-relaxation objective, fractional commitment, startup-cost sensitivity, lower-demand sensitivity, initial commitment, and invalid/infeasible inputs.

## Limitations

This teaching model omits ramping, minimum up/down times, shutdown costs, startup trajectories, reserve constraints, network constraints, transmission losses, contingencies, forced outages, uncertainty, and detailed market settlement. It is not a production unit-commitment model or a PJM market simulator. The model has only two periods and two synthetic units.

## Related curriculum

- [Y2-04 Problem Set 4: Unit commitment](../../../courses/year-2/electricity-market-design-optimization/problem-set-04-unit-commitment.md)
- [Y2-04 Problem Set 1: Economic dispatch and duality](../../../courses/year-2/electricity-market-design-optimization/problem-set-01-economic-dispatch-duality.md)
- [Energy and reserve co-optimization](../../../projects/energy-economics/energy-reserve-cooptimization/README.md)
