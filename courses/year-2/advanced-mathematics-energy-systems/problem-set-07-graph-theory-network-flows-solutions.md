# Problem Set 7: Worked Solutions and Mathematical Notes

## Problem 1. Incidence matrices, cycle space, and Laplacians

With rows ordered `(s,a,b,t)` and columns ordered `(s→a,s→b,a→b,a→t,b→t)), the incidence matrix is

\[
A=\begin{bmatrix}
-1&-1&0&0&0\\
1&0&-1&-1&0\\
0&1&1&0&-1\\
0&0&0&1&1
\end{bmatrix}.
\]

The graph is connected, so the incidence matrix has rank \(n-c=4-1=3\). By rank-nullity, its right null space has dimension \(m-\operatorname{rank}(A)=5-3=2\), the dimension of the cycle space. Two independent cycles are \(s-a-b-s\) and \(a-b-t-a\).

The unweighted graph Laplacian is

\[
L=AA^T=
\begin{bmatrix}
2&-1&-1&0\\
-1&3&-1&-1\\
-1&-1&3&-1\\
0&-1&-1&2
\end{bmatrix}.
\]

Every row sums to zero. More generally,

\[
z^TLz=z^TAA^Tz=\|A^Tz\|_2^2
=\sum_{(i,j)\in E}(z_j-z_i)^2.
\]

Thus L is positive semidefinite. In a connected graph, \(A^Tz=0\) requires equal values at every pair of adjacent nodes, hence z is constant. Therefore \(\operatorname{null}(L)=\operatorname{span}\{\mathbf 1\}\) and \(\operatorname{rank}(L)=3\).

## Problem 2. Maximum flow and minimum-cut certificate

A valid linear program is

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
0\leq f_1\leq7,\quad
0\leq f_2\leq5,\quad
0\leq f_3\leq2,\quad
0\leq f_4\leq4,\quad
0\leq f_5\leq8.
\]

The conservation equations apply at a and b. A feasible flow is

\[
(f_1,f_2,f_3,f_4,f_5)=(6,5,2,4,7).
\]

At node a, inflow is 6 and outflow is \(2+4=6\). At node b, inflow is \(5+2=7\) and outflow is 7. All arc capacities are respected, and the total source flow is \(F=6+5=11\) MW.

Consider the cut \(S=\{s,a\}\), \(T=\{b,t\}\). The arcs directed from S to T are \(s\to b\), \(a\to b\), and \(a\to t\), with total capacity

\[
c(S,T)=5+2+4=11\text{ MW}.
\]

Every feasible flow is bounded above by every s-t cut capacity. Since a feasible flow of 11 MW matches this cut bound, the max-flow/min-cut theorem certifies that the maximum flow is exactly 11 MW.

The cut identifies a set of facilities whose combined capacity limits transfer. Increasing an arc capacity that does not cross the active minimum cut may not increase maximum transfer; the bottleneck must be relieved or another cut may become binding.

## Problem 3. Connectivity, contingencies, and resilience

Two edge-disjoint paths are \(s-a-t\) and \(s-b-t\). By the edge form of Menger's theorem, at least two edge failures are required to disconnect s from t. Removing \(a\to b\) leaves both paths intact, so s-t connectivity is preserved. However, the maximum flow falls from 11 MW to 9 MW: the cut \(S=\{s,a\}, T=\{b,t\}\) then has capacity \(5+4=9\) MW, and 9 MW is feasible by sending 4 MW on \(s\to a\to t\) and 5 MW on \(s\to b\to t\). Connectivity remains, but transfer capability falls.

If \(s\to a\) is removed, only \(s\to b\to t\) can carry source flow, so the maximum is \(\min(5,8)=5\) MW. This flow is feasible.

Edge connectivity counts independent paths or failures without accounting for ratings. Capacity-aware transfer depends on the minimum cut. Operational N-1 security is a system criterion defined over a base case, specified contingencies, operating limits, and permitted corrective actions. It is not equivalent to simple graph connectivity.

A credible power-system contingency study also needs impedances and voltage/phase behavior, thermal ratings and their time dependence, generator redispatch and ramp limits, voltage/reactive constraints, protection and stability constraints, and potentially load shedding or switching actions.

## Problem 4. Weighted Laplacians and sensitivity

For positive weights,

\[
z^TL_wz=(A^Tz)^TW(A^Tz)
=\sum_e w_e(z_i-z_j)^2\geq0,
\]

so \(L_w\) is positive semidefinite. For a connected graph, its null space is the span of the all-ones vector and its rank is \(n-1\). The second-smallest eigenvalue (algebraic connectivity) is positive and becomes small when the graph has a weakly connected partition. This is a spectral/topological diagnostic, not an MW transfer limit: it does not encode a source/sink injection pattern, thermal capacities, or operating constraints.

For a lossless DC power-flow model, a susceptance-weighted Laplacian can represent the nodal susceptance matrix under a consistent sign convention. This requires assumptions such as voltage magnitudes near 1 per unit, small angle differences, negligible resistance/losses, and fixed topology. The branch weights must represent the appropriate series susceptances and transformer treatment. The graph Laplacian is a structural starting point, not a complete AC network model.

## Problem 5. Modeling judgment

A max-flow model enforces conservation and arc capacities but permits arbitrary routing subject to those constraints. In an electrical network, flows are coupled by voltage angles and line reactances; they cannot generally be assigned independently. Kirchhoff's voltage law imposes cycle consistency. AC feasibility additionally depends on voltage magnitudes, reactive power, losses, generator capability, and nonlinear power-flow equations.

A max-flow model can overstate transfer when it routes power along a path that would cause a parallel path to overload under the electrical distribution of flows, or when voltage/reactive limits bind before thermal limits. A staged workflow can use documented topology/capacity data for a graph screen, then a DC power-flow or DC-OPF model with validated impedances and injections, then AC power flow and contingency analysis with voltage, reactive, protection, and stability checks. Each stage requires documented data provenance, base-case reconciliation, unit checks, and comparison with an accepted benchmark or independently validated model.

A graph screen can identify structural bottlenecks, candidate cut sets, and hypothetical upper bounds under its assumptions. It cannot establish that a proposed transfer is electrically feasible, that a facility is available, or that an actual system meets reliability criteria.

## Problem 6. Research translation

There is no single numerical solution. A strong note defines a bounded network, documents why the chosen nodes and edges represent the infrastructure of interest, identifies public-data coverage gaps, and explains the meaning of each metric. It distinguishes a structural vulnerability indicator from outage probability, customer minutes interrupted, or a formal reliability standard. The proposed next model should be driven by missing physics and operational data, not by adding complexity for its own sake.
