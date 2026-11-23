# Power Systems Projects

These projects move from network equations to distribution screening, operating dynamics, and reliability. They are computational companions, not substitutes for an engineering study or utility operating model.

## Recommended progression

1. [Three-bus DC power flow](three-bus-dc-power-flow/README.md) — start with nodal injections, per-unit reactance, slack bus, and branch-flow signs.
2. [Two-node congestion](two-node-congestion/README.md) — connect constrained transfer to dispatch and nodal-price duals.
3. [Three-bus DC-OPF](three-bus-dc-opf/README.md) — combine nodal balances, line limits, dispatch, LMP duals, and finite-difference validation.
4. [Radial DER hosting-capacity screen](radial-der-hosting-capacity/README.md) — apply downstream aggregation, approximate voltage drop, thermal screening, and reverse flow.
5. [IEEE 13-node OpenDSS benchmark](radial-der-hosting-capacity/benchmarks/ieee13-opendss/README.md) — move to an unbalanced three-phase AC-capable benchmark. This is a separate network, not a matched validation of the synthetic radial feeder.
6. [Flexible interconnection](flexible-interconnection/README.md) — add export envelopes and PV-plus-storage scheduling to a synthetic 24-hour customer/feeder model.
7. [Frequency response](frequency-response-dynamics/README.md) — study state-space dynamics, eigenvalues, and numerical integration.
8. [Stochastic resource adequacy](stochastic-adequacy/README.md) — introduce Monte Carlo adequacy metrics and simulation uncertainty.
9. [Network-flow resilience](network-flow-resilience/README.md) — study graph connectivity and transfer bottlenecks as a structural screen.

## Entry requirements

The first three projects assume Y1-01 power-system foundations and basic Python. The OpenDSS project adds distribution-system modeling and the DSS-Python environment. Flexible interconnection assumes linear optimization and storage fundamentals. Frequency response assumes differential equations and linear algebra. Stochastic adequacy assumes probability and Monte Carlo reasoning. Network flow assumes graph theory and optimization.

## Interpretation rules

- DC power flow is lossless and does not solve voltage magnitude or reactive-power feasibility.
- The radial DER screen is a first-order balanced approximation, not AC hosting capacity.
- The OpenDSS benchmark is AC-capable and unbalanced, but a benchmark feeder is not a utility model.
- Flexible export envelopes are synthetic operating constraints, not approved tariffs or protection settings.
- Reliability and network-flow outputs are not PJM/utility reliability metrics or N-1 security certification.

Use each project README for its equations, data provenance, run commands, tests, benchmark, and limits.
