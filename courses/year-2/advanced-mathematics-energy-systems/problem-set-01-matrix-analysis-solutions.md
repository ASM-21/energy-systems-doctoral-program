# Problem Set 1: Worked Solutions and Mathematical Notes

These notes show one complete derivation. Equivalent sign conventions are acceptable if they are used consistently throughout the incidence matrix, injections, and branch-flow equations.

## Problem 1. Vector spaces, rank, and identifiability

The third row of \(A\) is the sum of the first two, so the rows are dependent. The first two rows are independent; hence \(\operatorname{rank}(A)=2\).

Solving \(Ax=0\) gives \(x_1=x_2=x_3\). Therefore

\[
\mathcal N(A)=\operatorname{span}\{(1,1,1)^T\},
\qquad \dim\mathcal N(A)=1.
\]

A row-space basis is \((1,-1,0)\) and \((0,1,-1)\). The rank-nullity identity is \(2+1=3\).

Adding the same constant to every bus angle leaves every pairwise angle difference unchanged. Thus absolute angle is not identifiable from differences alone. Selecting a reference/slack bus, conventionally setting its angle to zero, removes the one-dimensional gauge freedom.

## Problem 2. Incidence matrices and graph Laplacians

With +1 at the sending node and −1 at the receiving node,

\[
C=\begin{bmatrix}
1&0&1\\
-1&1&0\\
0&-1&-1
\end{bmatrix},
\qquad
D=\begin{bmatrix}10&0&0\\0&10&0\\0&0&5\end{bmatrix}.
\]

Multiplication gives

\[
L=CDC^T=
\begin{bmatrix}
15&-10&-5\\
-10&20&-10\\
-5&-10&15
\end{bmatrix}.
\]

For any vector \(x\),

\[
x^TLx=x^TCDC^Tx=(C^Tx)^TD(C^Tx)
=10(x_1-x_2)^2+10(x_2-x_3)^2+5(x_1-x_3)^2\geq0.
\]

Since \(D\) has strictly positive diagonal entries, equality holds exactly when every connected branch has equal endpoint values. The graph is connected, so \(x_1=x_2=x_3\). In particular, \(L\mathbf 1=0\), and the null space is the span of the all-ones vector.

For a graph with \(n\) vertices and \(k\) connected components, the Laplacian rank is \(n-k\). Thus a connected three-node graph has rank 2. Removing branch 1–3 leaves this particular graph connected through 1–2–3, so its rank remains 2. Removing both 1–3 and either 1–2 or 2–3 would disconnect the graph and reduce the rank to 1. The number of components, not simply the number of removed edges, determines the rank.

## Problem 3. Slack-bus reduction and DC power flow

The full nodal equation is \(L\theta=p\). Fix \(\theta_1=0\), then retain rows and columns 2 and 3:

\[
\begin{bmatrix}20&-10\\-10&15\end{bmatrix}
\begin{bmatrix}\theta_2\\\theta_3\end{bmatrix}
=
\begin{bmatrix}-0.50\\0.10\end{bmatrix}.
\]

The determinant is \(300-100=200\), so

\[
B_r^{-1}=\frac1{200}
\begin{bmatrix}15&10\\10&20\end{bmatrix}.
\]

Consequently,

\[
\theta_2=\frac{15(-0.5)+10(0.1)}{200}=-0.0325,
\qquad
\theta_3=\frac{10(-0.5)+20(0.1)}{200}=-0.0150.
\]

Angles are in radians. For a branch oriented \(i\to j\), the DC flow is \(f_{ij}=b_{ij}(\theta_i-\theta_j)\) p.u.:

- 1→2: \(10(0-(-0.0325))=0.325\) p.u. = +32.5 MW.
- 2→3: \(10(-0.0325-(-0.0150))=-0.175\) p.u. = −17.5 MW, meaning actual flow is 17.5 MW from 3 to 2.
- 1→3: \(5(0-(-0.0150))=0.075\) p.u. = +7.5 MW.

At bus 2, the net injection is outgoing flow 2→1 of −32.5 MW plus outgoing flow 2→3 of −17.5 MW, totaling −50 MW. At bus 3, outgoing flow 3→2 is +17.5 MW and 3→1 is −7.5 MW, totaling +10 MW. Bus 1 supplies 32.5+7.5=40 MW. Total injection is therefore \(40-50+10=0\).

The lossless DC model has no resistive losses, so total generation/injection must equal total withdrawal. In a lossy model, the required net injection sum equals total network losses rather than zero.

## Problem 4. Eigenvalues, positive definiteness, and conditioning

For \(B_r\), the characteristic polynomial is

\[
\det(B_r-\lambda I)=(20-\lambda)(15-\lambda)-100
=\lambda^2-35\lambda+200.
\]

Thus

\[
\lambda_{\pm}=\frac{35\pm\sqrt{425}}2
=\frac{35\pm5\sqrt{17}}2.
\]

Numerically, \(\lambda_{\max}\approx27.81\) and \(\lambda_{\min}\approx7.192\). Both are positive, so the matrix is positive definite.

Sylvester's criterion gives the same result: the leading principal minors are \(20>0\) and \(\det(B_r)=200>0\). Hence \(B_r\succ0\).

The spectral condition number is

\[
\kappa_2(B_r)=\frac{35+5\sqrt{17}}{35-5\sqrt{17}}
\approx3.866.
\]

This is modest for this small example. In general, a large condition number means some perturbation directions in the right-hand side or matrix can produce much larger relative changes in the solution. In power systems, weakly connected areas, very high impedance paths, or near-islanding topologies can produce poorly conditioned network equations. Poor conditioning means the system is invertible but sensitive; singularity means no unique inverse exists.

## Problem 5. Quadratic forms and energy interpretation

Using the Laplacian,

\[
\theta^TL\theta
=10(\theta_1-\theta_2)^2
+10(\theta_2-\theta_3)^2
+5(\theta_1-\theta_3)^2.
\]

Each term is nonnegative. Because the graph is connected, the sum is zero only when all three angles are equal. Once \(\theta_1=0\) is fixed, only the zero vector in the reduced coordinates makes the form zero. This is why the reduced matrix is positive definite.

The quadratic form is a mathematical measure of weighted angle-difference dispersion. It supports proofs of positive definiteness and uniqueness, and it helps explain why the reduced linear system has a unique solution. It should not be described as the full stored electromagnetic energy of an AC network: the derivation belongs to the linearized DC network model and its weighted graph structure.

## Problem 6. Matrix sensitivity

With \(B_r\) fixed,

\[
B_r(\theta+\delta\theta)=p_r+\delta p,
\quad B_r\theta=p_r,
\]

so subtraction gives the exact relation

\[
\delta\theta=B_r^{-1}\delta p.
\]

For any compatible induced matrix norm,

\[
\|\delta\theta\|\leq\|B_r^{-1}\|\,\|\delta p\|.
\]

Because \(p_r=B_r\theta\), the standard relative bound is

\[
\frac{\|\delta\theta\|}{\|\theta\|}
\leq \kappa(B_r)\frac{\|\delta p\|}{\|p_r\|},
\]

provided the denominators are nonzero. This is a worst-case bound; actual sensitivity depends on the perturbation direction.

This result is not a complete feeder-voltage forecast. First, the DC approximation fixes voltage magnitudes and omits reactive power, resistance, and voltage-drop effects that matter in distribution systems. Second, real DER response can change controls, topology, operating point, and constraints, making the governing equations nonlinear and potentially piecewise or time-dependent. Measurement error and model misspecification add further uncertainty.

## Grading emphasis and common errors

- **Sign consistency:** Reversing a branch orientation is harmless only if the corresponding incidence column and flow sign are both reversed.
- **Per-unit conversion:** The specified injections are −0.50 and +0.10 p.u. on a 100 MVA base.
- **Slack bus:** The slack injection is solved from balance; it is not an independent specified injection in this exercise.
- **Graph connectivity:** Removing one edge from a triangle does not disconnect it.
- **Positive semidefinite vs. definite:** The full Laplacian is singular positive semidefinite; the slack-reduced matrix is positive definite because the reference removes the common-angle null direction.
- **Conditioning vs. model validity:** A well-conditioned matrix does not imply that the physical model is accurate.

