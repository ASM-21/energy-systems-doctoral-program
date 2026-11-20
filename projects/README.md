# Research and Technical Projects

Projects are the main evidence of applied mastery. Each project should have a defined question, scope, inputs, methods, deliverables, reproducibility instructions, and limitations.

## Project standards
- Separate synthetic demonstrations from empirical results using real-world data.
- Document data licensing and provenance before downloading or committing data.
- Avoid confidential utility/employer/customer data.
- Include tests for data transformations and core calculations.
- Use versioned assumptions and explain scenario choices.
- Provide a short policy/decision summary alongside technical artifacts.

## Initial flagship project
See [PJM/Pennsylvania distribution infrastructure and DER research proposal](policy-analysis/pjm-distribution-der-research-proposal.md). This is a candidate project, not a completed finding or predetermined conclusion.

## Computational labs
- [Battery arbitrage optimization](energy-economics/storage-arbitrage/README.md) — intertemporal storage scheduling, efficiency, and degradation
- [Merit-order economic dispatch](energy-economics/merit-order-dispatch/README.md) — single-node least-cost dispatch and marginal price
- [Three-bus DC power flow](power-systems/three-bus-dc-power-flow/README.md) — per-unit network matrix, slack bus, angles, and branch flows
- [Two-node congestion and nodal prices](power-systems/two-node-congestion/README.md) — network-constrained dispatch and dual values
- [Radial feeder DER hosting-capacity screen](power-systems/radial-der-hosting-capacity/README.md) — first-order radial voltage-drop approximation, branch loading, reverse flow, and PV penetration sweep
- [OLS and robust inference](econometrics/ols-energy-demand/README.md) — reproducible synthetic regression workflow

The radial feeder lab is a synthetic screening model. It is not an AC power-flow, protection, or utility interconnection study.
