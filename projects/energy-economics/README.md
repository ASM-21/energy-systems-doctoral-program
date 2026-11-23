# Energy Economics and Market Optimization Projects

These projects progress from single-period dispatch to intertemporal storage, reserve co-optimization, and uncertainty-aware capacity decisions.

## Recommended progression

1. [Merit-order dispatch](merit-order-dispatch/README.md) — least-cost dispatch, marginal price, carbon price, and flexible demand.
2. [Battery arbitrage](storage-arbitrage/README.md) — intertemporal state of charge, efficiency, and degradation.
3. [Non-exporting behind-the-meter storage](non-exporting-btm-storage/README.md) — customer load/PV/storage balance and no-export operation.
4. [Energy and operating-reserve co-optimization](energy-reserve-cooptimization/README.md) — joint energy/reserve constraints, dual values, and finite-difference checks.
5. [Stochastic and robust capacity planning](stochastic-robust-capacity-planning/README.md) — nonanticipativity, recourse, expected-value benchmarks, VSS, EVPI, and worst-case cost.
6. [Utility regulatory economics](utility-regulatory-economics/README.md) — cost allocation, three-part rates, regulatory lag, earnings sharing, and capital-budgeting sensitivity.
7. [Unit commitment](unit-commitment/README.md) — startup and no-load costs, binary commitment, and LP-relaxation comparison.

## Prerequisites

Start with Y1-02 energy economics. The reserve co-optimization lab also assumes Y1-03 electricity-market and reserve concepts. The stochastic/robust project assumes probability, linear programming, and duality from Y2-01.

## Model boundaries

The projects are synthetic teaching models. They do not represent an actual PJM settlement engine, production-cost model, tariff, capacity auction, or utility investment plan. Shadow prices are local derivatives of the stated optimization model and should not be generalized beyond its formulation and active constraints.

For each project, inspect the objective, balance equations, bounds, time resolution, and treatment of losses/uncertainty before interpreting results.
