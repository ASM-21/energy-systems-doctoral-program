# Radial Distribution Feeder: DER Hosting Capacity and Operating Limits

## Research question

How does increasing behind-the-meter PV at a remote node change feeder voltage, branch loading, reverse power flow, and the first binding operating constraint?

This is a transparent, balanced, steady-state **first-order radial voltage-drop screening model** for a small radial feeder. It is an educational model, not an AC power-flow solver, protection study, utility planning model, or interconnection approval tool.

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

A separate [IEEE 13-node OpenDSS benchmark](benchmarks/ieee13-opendss/README.md) now provides a reproducible nonlinear, unbalanced three-phase simulation baseline. It is not a direct numerical validation of this synthetic feeder because the network topology and model assumptions differ. The next research step is to extract matched operating points and compare a reduced balanced approximation against an AC-capable solution on a deliberately aligned network. Do not describe either teaching model as a utility-grade study.

## Project record

- **Type/status:** Distribution engineering screen; synthetic reproducible baseline.
- **Prerequisites:** Three-phase power, per-unit voltage, radial feeder topology, and basic Python. Review Y1-01 radial distribution and DER problem sets.
- **Boundary:** One balanced steady-state snapshot with constant-P/Q loads, one unity-power-factor DER injection, and first-order voltage-drop and branch-MVA screens.
- **Validation:** Check tree connectivity/orientation, nodal downstream aggregation, branch apparent-power arithmetic, and voltage/thermal threshold crossings. The supplied test cases verify the first thermal violation at 900 kW for this particular synthetic snapshot.
- **Assessment link:** Supports Y1-01 radial DER hosting-capacity assessment. Submit equations, branch-by-branch results, threshold sensitivity, and an explicit explanation of why the result is not utility hosting capacity.
