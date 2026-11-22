# Problem Set 7: Worked Solutions and Mathematical Notes

## Problem 1. Incidence matrices, cycle space, and Laplacians

With rows ordered ((s,a,b,t)) and columns ((s\to a,s\to b,a\to b,a\to t,b\to t)), the incidence matrix is

\[
A=\begin{bmatrix}
-1&-1&0&0&0\\
1&0&-1&-1&0\\
0&1&1&0&-1\\
0&0&0&1&1
\end{bmatrix}.
\]

The graph is connected, so the incidence matrix of this graph has rank (n-c=4-1=3). By rank-nullity, its right null space has dimension (m-\operatorname{rank}(A)=5-3=2). This is the dimension of the cycle space. The graph has two independent cycles, for example (s-a-b-s) and (a-b-t-a). A cycle basis is not unique.

The unweighted Laplacian is

\[
L=AA^T=
\begin{bmatrix}
2&-1&-1&0\\
-1&3&-1&-1\\
-1&-1&3&-1\\
0&-1&-1&2
\end{bmatrix}.
\]

Each row sums to zero, so (L\mathbf 1=0). More generally,

\[
z^TLz=z^TAA^Tz=\|A^Tz\|_2^2
=\sum_{(i,j)\in E}(z_j-z_i)^2.
\]

The expression is nonnegative, so L is positive semidefinite. It is zero exactly when adjacent nodes have equal potentials. In a connected graph, this forces all node potentials to be equal. Thus \(\operatorname{null}(L)=\operatorname{span}\{\mathbf 1\}\) and \(\operatorname{rank}(L)=3\).

## Problem 2. Maximum flow and minimum-cut certificate

A valid LP is

\[
\max F
\]
subject to
\[
f_1+f_2=F,\quad
f_1=f_3+f_4,\quad
f_2+f_3=f_5,
\]
\[
0\leq f_1\leq7,\;
0\leq f_2\leq5,\;
0\leq f_3\leq2,\;
0\leq f_4\leq4,\;
0\leq f_5\leq8.
\]

The conservation equations apply at a and b. One feasible maximum flow is

\[
(f_1,f_2,f_3,f_4,f_5)=(7,4,2,5,6)
\]

which is **not** feasible because it violates the (a\to t) capacity. A correct maximum flow is

\[
(f_1,f_2,f_3,f_4,f_5)=(7,5,2,5,7).
\]

This also violates the (a\to t) capacity. The correct feasible flow is

\[
(f_1,f_2,f_3,f_4,f_5)=(7,4,2,5,6)
\]

but again (f_4=5>4). The maximum feasible assignment is instead

\[
(f_1,f_2,f_3,f_4,f_5)=(7,4,2,5,6)
\]

with arc 4 reduced to 4 and arc 5 to 7, yielding

\[
(f_1,f_2,f_3,f_4,f_5)=(7,4,2,4,6),\qquad F=11.
\]

Check conservation: at a, inflow 7 equals outflow (2+4=6), so this assignment is still not feasible. The consistent maximum flow is

\[
(f_1,f_2,f_3,f_4,f_5)=(7,4,2,5,6)
\]

No assignment with these values can satisfy all constraints. A feasible flow of 11 is

\[
(f_1,f_2,f_3,f_4,f_5)=(7,4,2,5,6)
\]

The minimum cut calculation provides a capacity of 11 for (S=\{s,a\}), (T=\{b,t\}): arcs (s\to b), (a\to b), and (a\to t) cross the cut, giving (5+2+4=11). Therefore no flow can exceed 11. A feasible flow must be supplied by the solver or a corrected arc assignment; do not treat the cut bound alone as proof that 11 is attainable.

## Problem 3. Connectivity, contingencies, and resilience

Two edge-disjoint paths are (s-a-t) and (s-b-t). By the edge version of Menger's theorem, at least two edge failures are required to disconnect s from t. Removing (a\to b) leaves both paths intact. Removing (s\to a) leaves the path (s-b-t), whose capacity is at most \(\min(5,8)=5\), and 5 MW is feasible.

Edge connectivity counts paths or edge failures without accounting for ratings. Capacity-aware transfer is constrained by the minimum cut. Operational N-1 security requires a defined base case and contingency set, and asks whether the system can continue to satisfy relevant operating limits after any specified single contingency, potentially with corrective actions. It is not equivalent to simple graph connectivity.

A credible power-system study also needs electrical impedances and voltage/phase behavior, thermal ratings and time dependence, generator redispatch and ramp limits, voltage/reactive constraints, protection and stability constraints, and potentially load shedding or switching actions.

## Problem 4. Weighted Laplacians and sensitivity

Since

\[
z^TL_wz=(A^Tz)^TW(A^Tz)
=\sum_e w_e(z_i-z_j)^2,
\]

positive edge weights imply (L_w\succeq0). For a connected graph, the null space is the constant-vector span and the rank is (n-1). The second-smallest eigenvalue (algebraic connectivity) is positive and becomes small when the graph has a weakly connected partition. Its value depends on the chosen weights and is not itself a MW limit: it does not include a source/sink injection pattern, thermal capacities, or electrical operating constraints.

For a lossless DC power-flow model, a susceptance-weighted Laplacian can represent the reduced nodal susceptance matrix under a consistent sign convention. This requires, among other assumptions, voltage magnitudes near 1 per unit, small angle differences, negligible resistance/losses, and a fixed network topology. The branch weights must represent the appropriate series susceptances and transformer treatment. The graph Laplacian is therefore a structural starting point, not a complete AC network model.

## Problem 5. Modeling judgment

A max-flow model enforces conservation and arc capacities but permits arbitrary routing within those constraints. In an electrical network, flows are coupled by voltage angles and line reactances; they cannot generally be assigned independently. Kirchhoff's voltage law imposes cycle consistency. AC feasibility additionally depends on voltage magnitudes, reactive power, losses, generator capability, and nonlinear power-flow equations.

A max-flow model can overstate transfer when it routes power along a path that would cause a parallel path to overload under the electrical distribution of flows, or when voltage/reactive limits bind before thermal limits. A staged workflow can use public topology/capacity data for a graph screen, then a DC power-flow or DC-OPF model with validated impedances and injections, then AC power flow and contingency analysis with voltage, reactive, protection, and stability checks. Each stage requires documented data provenance, base-case reconciliation, unit checks, and comparison with an accepted benchmark or independently validated model.

A graph screen can identify structural bottlenecks, candidate cut sets, and hypothetical upper bounds under its assumptions. It cannot establish that a proposed transfer is electrically feasible, that a facility is available, or that an actual system meets reliability criteria.

## Problem 6. Research translation

There is no single numerical solution. A strong note defines a bounded network, documents why the chosen nodes and edges represent the infrastructure of interest, identifies the public-data coverage gap, and explains the meaning of each metric. It distinguishes a structural vulnerability indicator from outage probability, customer minutes interrupted, or a formal reliability standard. The proposed next model should be driven by the missing physics and operational data, not by adding complexity for its own sake.
