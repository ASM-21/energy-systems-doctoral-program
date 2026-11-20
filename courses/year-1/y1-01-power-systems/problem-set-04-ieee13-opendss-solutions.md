# Solution Guide: IEEE 13-Node Feeder Benchmark

This assignment is computational. Numerical answers must be generated from the stated DSS-Python version and the exact test-case snapshot used. Do not substitute guessed or copied voltage values from another OpenDSS release.

## Problem 1 — Baseline

A correct run should compile the IEEE 13-node master file, converge, and export one row per node entry returned by `AllNodeNames`, paired in order with `AllBusVmagPu`. Preserve the full node labels because a single bus can contain multiple phase nodes. Record the exact engine version and downloaded source snapshot. The runner reports circuit real losses in kW and reactive losses in kvar after converting the engine's W/var values.

## Problem 2 — PV sweep

The PV element is added as a balanced three-phase resource at bus 675 with 4.16 kV line-to-line rating, unity power factor, and nameplate kVA equal to the specified kW rating. The experiment holds the published test-case loads constant. The first tested rating above 1.05 pu is only a bracket on the voltage-screening threshold for this snapshot and this PV connection. It is not a general hosting-capacity result.

Voltage may rise at electrically remote nodes as PV injection offsets downstream real-power demand. Losses can fall initially as upstream current is reduced, then rise as reverse flow increases. The exact pattern depends on the case solution and must be taken from the generated output, not assumed in advance.

## Problem 3 — Load sensitivity

At lower load, the same PV injection is larger relative to local consumption and can increase the likelihood of reverse power flow or high voltage. At higher load, local consumption can absorb more PV output, but current and voltage-drop effects may be larger. The actual response depends on network topology, phase imbalance, voltage controls, and the location of the DER.

## Problem 4 — Interpretation

OpenDSS solves a detailed distribution circuit with phase-specific elements and nonlinear network equations. The first-order curriculum screen assumes a balanced radial tree, constant-P/Q load aggregation, unity-power-factor DER, a fixed nominal-voltage denominator, and no losses in branch-power aggregation. The two tools answer different questions. A direct numerical comparison requires constructing a reduced equivalent network with matched topology, impedances, load allocation, base quantities, DER location, and control settings. Merely comparing unrelated synthetic and IEEE feeder outputs is not validation.

A complete hosting-capacity analysis also requires thermal and protection criteria, time-series coincidence, inverter control behavior, equipment operating limits, and explicit utility planning rules. The IEEE benchmark is not a proxy for PPL's confidential network or a substitute for site-specific interconnection review.
