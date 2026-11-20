# Radial Distribution Feeder: DER Hosting Capacity and Operating Limits

## Research question

How does increasing behind-the-meter PV at a remote node change feeder voltage, branch loading, reverse power flow, and the first binding operating constraint?

This is a transparent, balanced, steady-state **LinDistFlow-style screening model** for a small radial feeder. It is an educational model, not an AC power-flow solver, protection study, utility planning model, or interconnection approval tool.

## Model

The feeder is a rooted tree. Each bus has constant-P and constant-Q demand. A controllable DER injection is applied at one bus. For each branch, downstream net demand is aggregated:

\[
P_{ij}=\sum_{k\in\mathcal{D}(j)}(P_{L,k}-P_{DER,k}),\qquad
Q_{ij}=\sum_{k\in\mathcal{D}(j)}Q_{L,k}
\]

The approximate line-to-line voltage recursion is:

\[
V_{j,pu}=V_{i,pu}-\frac{R_{ij}P_{ij}+X_{ij}Q_{ij}}{V_{LL}^{2}}
\]

where branch power is converted to MW/Mvar and nominal line-to-line voltage is in kV. Branch apparent power is screened against the supplied MVA rating. Negative branch P denotes reverse real-power flow.

## Run

```bash
python -m pip install -r requirements.txt
python feeder.py
python feeder.py --der-bus 4 --sweep-max-kw 3000 --step-kw 100
python -m unittest discover -s . -p "test_*.py" -v
```

The script reads the synthetic feeder from `data/buses.csv` and `data/lines.csv`. It writes a scenario summary and detailed branch results to the requested output directory (default: `outputs/`). All input data are synthetic and chosen for instruction, not calibrated to PPL or any other utility.

## Required interpretation

1. Identify the first PV level at which voltage exceeds the screening band or a branch exceeds its thermal rating.
2. Identify when reverse flow begins and distinguish it from a thermal violation.
3. Explain why a hosting-capacity number depends on the chosen criterion, topology, load snapshot, DER location, inverter controls, and model assumptions.
4. Run sensitivities to feeder impedance, load level, DER location, and voltage band.
5. Explain why this static screen cannot establish a real feeder's hosting capacity.

## Limitations and extensions

The model assumes balanced three-phase operation, fixed voltage magnitude in the impedance denominator, constant-P/Q loads, no losses in branch-power aggregation, unity-power-factor DER, no regulator/capacitor controls, no unbalanced phases, no protection constraints, and no time-series coincidence. It uses an approximate voltage-drop equation and does not solve nonlinear AC DistFlow equations. Thermal screening uses apparent power, not conductor ampacity adjusted for weather or installation.

A defensible next step is to validate the model against a published benchmark feeder (for example, an IEEE distribution test feeder) using an AC-capable package such as OpenDSS or pandapower, then perform time-series hosting-capacity analysis with explicit voltage, thermal, protection, and operational criteria. Do not describe this synthetic exercise as a utility-grade study.
