# IEEE 13-Node Distribution Feeder: OpenDSS Benchmark

This benchmark runs the published IEEE 13-node test feeder using DSS-Python, an open-source Python interface to an OpenDSS-compatible distribution-system simulation engine. It provides a nonlinear, unbalanced three-phase benchmark for the curriculum's simpler balanced radial-feeder screening model.

**Important:** This is a separate benchmark model. It does not validate the synthetic feeder's numerical outputs, and the IEEE 13-node feeder is not representative of PPL's system. The benchmark's purpose is to establish a repeatable AC-capable simulation workflow and expose the limitations of first-order balanced approximations.

## Reproducibility and source

- Test case: `dss-extensions/electricdss-tst`, commit `3b208397160213cae4a9e2d0a7d1aa3528ce26e1`, file `Version8/Distrib/IEEETestCases/13Bus/IEEE13Nodeckt.dss`.
- The test-case repository is a filtered copy of OpenDSS SVN examples and tests and includes project-specific modifications; it is not an unmodified upstream SVN mirror.
- Engine interface: DSS-Python 0.15.4; DSS C-API 0.14.3 in the first CI run.
- The runner downloads the exact Git commit archive and writes a `.source_ref` marker. The feeder files are not redistributed in this repository.

References:
- [EPRI OpenDSS examples and test cases](https://opendss.epri.com/ExamplesDocsandTestCases.html)
- [DSS-Python Getting Started](https://dss-extensions.org/DSS-Python/examples/GettingStarted.html)
- [DSS-Python Python API overview](https://dss-extensions.org/python_apis.html)
- [DSS-Python API: circuit voltages](https://dss-extensions.org/DSS-Python/apidocs/dss/dss.ICircuit.html)
- [Pinned test-case repository and history](https://github.com/dss-extensions/electricdss-tst/tree/3b208397160213cae4a9e2d0a7d1aa3528ce26e1)

## Install and run

From this directory:

    python -m pip install -r requirements.txt
    python run_benchmark.py --pv-kw 0 --output-dir outputs/baseline
    python run_benchmark.py --pv-kw 500 --output-dir outputs/pv-500kw
    python run_benchmark.py --pv-kw 1000 --output-dir outputs/pv-1000kw
    python compare_scenarios.py --baseline-dir outputs/baseline --scenario-dir outputs/pv-500kw --output-dir outputs/comparison

The runner downloads the public test-case snapshot through the helper included with DSS-Python, compiles the IEEE 13-node circuit, solves a snapshot power flow, adds a balanced three-phase PVSystem at bus 675 for nonzero PV scenarios, solves again, and writes:
- `bus_voltages.csv`: node-level per-unit voltage magnitudes;
- `summary.json`: convergence, engine version, voltage extrema, circuit losses, and scenario parameters.

The comparison script aligns node labels, checks that engine version, pinned source commit, and load multiplier match, and writes a node-by-node voltage-delta CSV plus a machine-readable comparison summary. Use a fresh output directory for each run. The default source commit is immutable and recorded in every output.

## Verified CI baseline and 500 kW scenario

The pinned GitHub Actions run completed successfully on 2026-11-20 using test-case commit `3b208397160213cae4a9e2d0a7d1aa3528ce26e1`, DSS-Python 0.15.4, and DSS C-API 0.14.3 (OpenDSS SVN 3723). Both cases converged:

| Metric | Baseline, 0 kW PV | 500 kW PV at bus 675 |
|---|---:|---:|
| Solver iterations | 2 | 4 |
| Minimum node voltage | 0.96084 pu | 0.96788 pu |
| Maximum node voltage | 1.05605 pu | 1.05608 pu |
| Real circuit losses | 112.392 kW | 86.471 kW |

For this particular snapshot, 500 kW PV increased the minimum node voltage and reduced real losses by 25.920 kW. The lowest-voltage node was 611.3 (0.96084 to 0.96788 pu); the highest-voltage node was rg60.3 (1.05605 to 1.05608 pu). The largest node-level increase was at 675.1 (+0.00904 pu), followed by 675.3 (+0.00833 pu). All reported node voltages increased slightly or materially in this scenario. The maximum node voltage was already above a simple 1.05 pu screen in the zero-PV baseline and changed only slightly in the 500 kW case. Therefore, 1.05 pu cannot be interpreted as a PV-created violation threshold here. The maximum-voltage condition requires separate investigation of the benchmark's base controls, regulator settings, and node-level voltage profile before any hosting-capacity conclusion.

These are reproducible outputs from the first successful workflow run, not generalized feeder performance claims. [Workflow run and downloadable artifact](https://github.com/ASM-21/energy-systems-doctoral-program/actions/runs/44831385326).

## Interpretation

1. Compare minimum and maximum node voltages between baseline and PV cases.
2. Identify which nodes experience the largest voltage change.
3. Explain why a balanced three-phase PV system does not represent single-phase rooftop PV.
4. Compare the OpenDSS solution's complexity with the balanced first-order screen in the parent project.
5. Identify what is still absent from a static snapshot study: time-series coincidence, stochastic PV/load variation, protection coordination, hosting-capacity criteria, and utility-specific operating practices.

The runner reports voltages and losses. It does not automatically certify a hosting-capacity threshold, thermal adequacy, protection adequacy, or interconnection feasibility. A voltage-only sweep is not a complete hosting-capacity study.

## Limitations

The IEEE 13-node feeder is a small benchmark distribution circuit with unbalanced loads and distribution equipment. Its results are useful for methods training, not direct inference about a utility territory. The included PV scenario is an analyst-defined modification, not an official IEEE benchmark case. Document any additional regulators, capacitor controls, load multipliers, or inverter settings you change.

## Extension assignment

Run a PV sweep at bus 675, with 0, 100, 250, 500, 750, and 1,000 kW. Build a combined results table, graph minimum/maximum node voltage against PV rating, identify the first voltage criterion breach under an explicitly stated criterion, and explain why the resulting threshold is specific to this benchmark and snapshot.
