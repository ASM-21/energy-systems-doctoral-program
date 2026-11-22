# Problem Set 7: Graph Theory, Network Flows, and Infrastructure Resilience

**Level:** Advanced graduate / doctoral preparation  
**Suggested effort:** 2–3 hours, excluding optional coding  
**Prerequisites:** Problem Sets 1, 3, and 6; matrix rank, linear constraints, and constrained optimization  
**Deliverable:** Derivations, a clearly labeled network diagram, and short interpretations

## Learning objectives

After completing this assignment, you should be able to:

1. Construct an oriented incidence matrix and explain its rank and null space.
2. Relate graph connectivity, cycles, cuts, and Laplacian matrices.
3. Formulate and solve a maximum-flow problem; use a minimum cut as an optimality certificate.
4. Distinguish topological redundancy from capacity adequacy and operational N-1 security.
5. Explain why a generic max-flow model is a screening abstraction rather than a power-flow solution.

Use the directed graph with nodes (V=\{s,a,b,t\}) and arcs:

| Arc | Tail → head | Capacity (MW) |
|---|---|---:|
| 1 | (s\to a) | 7 |
| 2 | (s\to b) | 5 |
| 3 | (a\to b) | 2 |
| 4 | (a\to t) | 4 |
| 5 | (b\to t) | 8 |

Treat capacities as illustrative transfer limits, not actual electrical ratings.

## Problem 1. Incidence matrices, cycle space, and Laplacians

Use the node order ((s,a,b,t)) and arc order in the table. Adopt the incidence convention that an arc column has (-1) at its tail and (+1) at its head.

1. Construct the node-arc incidence matrix (A\in\mathbb{R}^{4\times5}).
2. Determine the rank of A and the dimension of its null space. Explain the result using graph connectivity.
3. Determine the cycle-space dimension (m-n+c), where (c) is the number of connected components. Explain why the graph contains two independent cycles even though it has only five arcs.
4. Construct the unweighted graph Laplacian (L=A A^T). Verify that every row sums to zero and that (L\mathbf{1}=0).
5. Show that for any node-potential vector (z\in\mathbb{R}^4),
   [
   z^TLz=\sum_{(i,j)\in E}(z_i-z_j)^2.
   ]
   State what the null space of L represents for a connected graph.

## Problem 2. Maximum flow and minimum-cut certificate

Let (f_e) be the flow on arc e and (F) the total flow from s to t.

1. Write the linear program maximizing F subject to capacity constraints and flow conservation at a and b.
2. Find a feasible flow achieving the maximum. Report each arc flow and verify conservation.
3. Identify a minimum s-t cut and calculate its capacity.
4. Use the max-flow/min-cut theorem to certify optimality.
5. Interpret the binding cut economically. Explain why adding capacity to an arc that does not cross the minimum cut may have no immediate effect on maximum transfer.

## Problem 3. Connectivity, contingencies, and resilience

1. Find two edge-disjoint paths from s to t. What does this imply about the minimum number of edge failures needed to disconnect s from t?
2. Remove arc (a\to b). Is s-t connectivity preserved? Is the maximum flow unchanged? Explain.
3. Remove arc (s\to a). Find a feasible s-t flow and its maximum value.
4. Explain why edge connectivity alone is not a measure of transfer capability. Use the capacities in the case to distinguish:
   - topological connectivity;
   - capacity-constrained transfer capability;
   - an operational N-1 security criterion.
5. Identify at least three additional phenomena that a credible transmission or distribution contingency study would need to represent but this graph model omits.

## Problem 4. Weighted Laplacians and sensitivity

Suppose each undirected edge has a positive weight (w_e), and define
[
L_w=A W A^T,\qquad W=\operatorname{diag}(w_1,\ldots,w_5).
]

1. Prove that (z^TL_wz=\sum_e w_e(z_i-z_j)^2\geq0). What does this establish about (L_w)?
2. For a connected graph with strictly positive weights, state the rank and null space of (L_w).
3. Explain how a small nonzero eigenvalue of (L_w) can indicate a weakly connected graph partition. Why is this a topological/spectral diagnostic rather than a direct measure of MW transfer capability?
4. Explain how the graph Laplacian relates to the susceptance-weighted nodal matrix used in a lossless DC power-flow approximation. State at least two assumptions required before interpreting it as a power-system model.

## Problem 5. Modeling judgment: max flow is not power flow

A planner uses the maximum-flow model to screen whether 500 MW of additional generation can reach a load pocket.

1. Explain why flow conservation and branch-capacity limits are necessary but not sufficient to describe feasible power transfers in an AC network.
2. Discuss the role of Kirchhoff's voltage law, line impedance/reactance, phase angles, voltage magnitudes, reactive power, and losses.
3. Give an example of how a max-flow model could overstate feasible transfer.
4. Propose a staged modeling workflow that starts with a graph screen but progresses to an appropriate electrical study. Identify what data and validation are required at each stage.
5. State precisely what conclusion a graph-based result can support, and what it cannot support.

## Problem 6. Research translation

Write a 500–700 word research note on one infrastructure-resilience question relevant to electricity distribution or transmission. Include:

- a network boundary and a defensible node/edge definition;
- a public-data inventory and a statement of what is not observable;
- at least two graph metrics (for example, bridge edges, edge connectivity, betweenness, connected components, spectral gap);
- at least one capacity-aware metric or flow formulation;
- a contingency set and rationale;
- a distinction between structural exposure and customer interruption risk;
- limitations and a proposed next model.

Do not use confidential utility, customer, or critical-infrastructure data. Do not infer feeder topology from service-territory boundaries or aggregate public statistics.

## Submission standard

Show intermediate algebra, define all matrix and graph conventions, include units, and distinguish a mathematical certificate from an engineering validation. A numerical answer without a feasibility check and interpretation is incomplete.
