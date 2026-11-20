# IEEE 13-Node Distribution Feeder: OpenDSS Benchmark

This benchmark runs the published IEEE 13-node test feeder using DSS-Python, an open-source Python interface to an OpenDSS-compatible distribution-system simulation engine. It provides a nonlinear, unbalanced three-phase benchmark for the curriculum's simpler balanced radial-feeder screening model.

**Important:** This is a separate benchmark model. It does not validate the synthetic feeder's numerical outputs, and the IEEE 13-node feeder is not representative of PPL's system. The benchmark's purpose is to establish a repeatable AC-capable simulation workflow and expose the limitations of first-order balanced approximations.

## Reproducibility and source

- Test case: DSS-Extensions `electricdss-tst`, `Version8/Distrib/IEEETestCases/13Bus/IEEE13Nodeckt.dss`.
- Test-case path and loading pattern follow the DSS-Python Getting Started example.
- Engine interface: DSS-Python 0.15.4.
- The benchmark downloads the test-case repository at runtime. It does not copy or redistribute the feeder files into this repository.

References:
- [EPRI OpenDSS examples and test cases](https://opendss.epri.com/ExamplesDocsandTestCases.html)
- [DSS-Python Getting Started](https://dss-extensions.org/DSS-Python/examples/GettingStarted.html)
- [DSS-Python Python API overview](https://dss-extensions.org/python_apis.html)
- [DSS-Python API: circuit voltages](https://dss-extensions.org/DSS-Python/apidocs/dss/dss.ICircuit.html)

## Install and run

From this directory:

    python -m pip install -r requirements.txt
    python run_benchmark.py --pv-kw 0 --output-dir outputs/baseline
    python run_benchmark.py --pv-kw 500 --output-dir outputs/pv-500kw
    python run_benchmark.py --pv-kw 1000 --output-dir outputs/pv-1000kw

The runner downloads the public test-case snapshot through the helper included with DSS-Python. It then compiles the IEEE 13-node circuit, solves a snapshot power flow, adds a balanced three-phase PVSystem at bus 675 for nonzero PV scenarios, solves again, and writes:
- `bus_voltages.csv`: node-level per-unit voltage magnitudes;
- `summary.json`: convergence, engine version, voltage extrema, circuit losses, and scenario parameters.

Use a fresh output directory for each run. Do not compare runs with different engine versions or different source snapshots without recording that difference.

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
