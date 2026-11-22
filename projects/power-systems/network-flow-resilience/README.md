# Network-Flow and Resilience Screening Lab

A small, dependency-free implementation of the Edmonds-Karp maximum-flow algorithm. It returns a maximum flow, residual-reachable source partition, arc flows, and a minimum-cut certificate.

## Run

```bash
python -m unittest -v
python max_flow.py
```

Expected case-study result:

- Maximum s-t flow: 11 MW.
- Arc flows: s→a 6 MW, s→b 5 MW, a→b 2 MW, a→t 4 MW, b→t 7 MW.
- Minimum cut: source side {s, a}; crossing arcs s→b, a→b, and a→t; total capacity 11 MW.

The implementation uses breadth-first search to find augmenting paths in the residual graph. It supports parallel directed arcs, checks basic input validity, and verifies the max-flow/min-cut equality through its returned cut.

## Contingency experiment

Remove the internal arc a→b. The graph remains connected from s to t, but maximum flow falls to 9 MW. Remove s→a and maximum flow falls to 5 MW. This illustrates why topological connectivity and capacity-aware transfer are different metrics.

## Scope and limitations

This is an abstract directed network-flow model. It does not solve AC or DC power flow, enforce Kirchhoff's voltage law, represent impedance-driven flow distribution, voltage/reactive constraints, losses, protection, dynamic stability, or operational N-1 criteria. The capacities are synthetic. Results are algorithm demonstrations, not utility planning or reliability conclusions.

For the mathematical derivation, see [Problem Set 7](../../../courses/year-2/advanced-mathematics-energy-systems/problem-set-07-graph-theory-network-flows.md) and its [worked solutions](../../../courses/year-2/advanced-mathematics-energy-systems/problem-set-07-graph-theory-network-flows-solutions.md).
