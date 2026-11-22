# Problem Set 1: Matrix Analysis and Network Structure

**Course:** Advanced Mathematical Methods for Energy Systems and Infrastructure Research  
**Module:** 1, Linear algebra and matrix analysis  
**Level:** Advanced graduate / doctoral preparation  
**Suggested effort:** 6–8 hours, spread across two or three study sessions  
**Prerequisites:** Matrix algebra, systems of linear equations, introductory power-system per-unit notation

## Instructions

Show derivations. A numerical answer without the matrix formulation and interpretation is incomplete. You may use Python, MATLAB, or a calculator to verify arithmetic, but the submitted work must explain the mathematics. State units and distinguish physical quantities from per-unit quantities.

Unless otherwise stated, use the DC power-flow approximation: voltage magnitudes are fixed at 1 p.u., angle differences are small, resistance and reactive-power effects are ignored, and branch flow is linear in the angle difference. These assumptions make the exercise analytically tractable; they do not make the model an AC power-flow solution.

## Problem 1. Vector spaces, rank, and identifiability (15 points)

Consider the matrix

\[
A=\begin{bmatrix}
1&-1&0\\
0&1&-1\\
1&0&-1
\end{bmatrix}.
\]

1. Determine the rank of \(A\), its null space, and its row space. Give a basis for each space.
2. Verify the rank-nullity theorem for the linear map \(A:\mathbb{R}^3\to\mathbb{R}^3\).
3. Interpret the null vector physically if the columns represent bus voltage angles and rows represent oriented pairwise angle differences.
4. Explain why pairwise differences cannot identify an absolute reference angle. What additional modeling choice removes this ambiguity?

## Problem 2. Incidence matrices and graph Laplacians (20 points)

A three-bus network has branches oriented as 1→2, 2→3, and 1→3. Their series reactances are respectively 0.1, 0.1, and 0.2 p.u.

1. Construct the node-edge incidence matrix \(C\), using +1 at the sending bus and −1 at the receiving bus.
2. Define \(D=\operatorname{diag}(10,10,5)\), where each diagonal entry is branch susceptance in p.u. Construct the weighted Laplacian \(L=CDC^T\).
3. Prove that \(L\) is positive semidefinite. Your proof should use the quadratic form, not an appeal to a numerical eigenvalue calculation.
4. Show that \(L\mathbf{1}=0\). Explain why this does not mean the network has no power-transfer capability.
5. For a connected graph, state and justify the relationship between graph connectivity and \(\operatorname{rank}(L)\). What changes if one branch is removed so the graph becomes disconnected?

## Problem 3. Slack-bus reduction and DC power flow (20 points)

Use the network in Problem 2, with bus 1 as the slack bus and a 100 MVA system base. Net injections are:

| Bus | Net injection |
|---|---:|
| 1 | determined by balance |
| 2 | −50 MW |
| 3 | +10 MW |

1. Starting from \(L\theta=p\), remove the slack-bus row and column and write the reduced system.
2. Convert the specified injections to p.u. and solve for \(\theta_2\) and \(\theta_3\), with \(\theta_1=0\).
3. Calculate the active-power flow on each branch. Use the stated branch orientation and retain the sign.
4. Recover the slack-bus injection from system balance.
5. Check Kirchhoff's current/power-balance analogue at each bus. Explain why the sum of all bus injections must be zero in this lossless model.

## Problem 4. Eigenvalues, positive definiteness, and conditioning (20 points)

The reduced matrix from Problem 3 is

\[
B_r=\begin{bmatrix}20&-10\\-10&15\end{bmatrix}.
\]

1. Compute its eigenvalues exactly in radical form and approximately to four significant figures.
2. Establish that \(B_r\) is positive definite using both (i) its eigenvalues and (ii) Sylvester's criterion.
3. Compute its spectral condition number \(\kappa_2(B_r)=\lambda_{\max}/\lambda_{\min}\).
4. Explain what a large condition number would imply for a numerical solution of \(B_r\theta=p\), including the role of measurement and parameter error.
5. Give one physically meaningful reason a power-network matrix might become poorly conditioned. Distinguish poor conditioning from singularity.

## Problem 5. Quadratic forms and energy interpretation (15 points)

Let \(\theta=[\theta_1,\theta_2,\theta_3]^T\) and use the full Laplacian from Problem 2.

1. Expand \(\theta^TL\theta\) and show that it equals the sum over branches of \(b_{ij}(\theta_i-\theta_j)^2\).
2. Show that the expression is nonnegative and identify all angle vectors for which it is zero in this connected network.
3. Explain why fixing the slack angle produces a positive-definite reduced quadratic form.
4. Discuss why this quadratic form is useful for reasoning about uniqueness and numerical stability, while avoiding the claim that it is the full physical stored energy of an AC grid.

## Problem 6. Research-method extension: matrix sensitivity (10 points)

For the reduced system \(B_r\theta=p_r\), suppose the injection vector is perturbed by \(\delta p\), while the network matrix is fixed.

1. Derive the exact relation between \(\delta\theta\) and \(\delta p\).
2. Derive a norm bound involving \(\|B_r^{-1}\|\), \(\|\delta p\|\), and \(\|\delta\theta\|\).
3. Explain how the condition number connects relative perturbations in the input and solution.
4. Identify two reasons why this linear sensitivity result should not be interpreted as a complete forecast of real distribution-feeder voltage response to DER injections.

## Submission standard

A complete submission includes:

- a derivation of the incidence and Laplacian matrices;
- proofs of the null-space and positive-(semi)definiteness claims;
- the solved DC power-flow system with signed branch flows and balance checks;
- an eigenvalue and condition-number calculation;
- a short paragraph on model limitations and the distinction between mathematical sensitivity and empirical prediction.

## Suggested references

- Gilbert Strang, *Introduction to Linear Algebra*, 6th ed., selected sections on vector spaces, rank, eigenvalues, and positive-definite matrices.
- Boyd and Vandenberghe, *Convex Optimization*, Appendix A, for linear algebra and matrix inequalities: https://web.stanford.edu/~boyd/cvxbook/
- Grainger and Stevenson, *Power System Analysis*, for network representations and DC power-flow foundations.
- The course's three-bus DC power-flow computational lab: `projects/power-systems/three-bus-dc-power-flow/README.md`.

