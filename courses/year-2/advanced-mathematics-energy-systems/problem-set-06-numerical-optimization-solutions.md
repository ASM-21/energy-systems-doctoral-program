# Problem Set 6: Worked Solutions and Mathematical Notes

## Problem 1. Gradient descent on a strongly convex quadratic

The gradient and Hessian are

\[
\nabla f(x)=Qx-b,
\qquad
\nabla^2 f(x)=Q.
\]

The first-order condition gives \(Qx^*=b\), so \(x^*=(1,1)^T\). Since the eigenvalues of Q are 1 and 10, the Hessian is positive definite. The objective is strongly convex with \(m=1\), and its gradient is L-Lipschitz with \(L=10\), both in the Euclidean norm.

Gradient descent is

\[
x_{k+1}=x_k-\alpha(Qx_k-b).
\]

For a quadratic, the error satisfies

\[
e_{k+1}=(I-\alpha Q)e_k.
\]

With \(\alpha=2/(L+m)=2/11\), the eigenvalues of the iteration matrix are \(1-2/11=9/11\) and \(1-20/11=-9/11\). The spectral contraction factor is therefore \(9/11\approx0.8182\).

From \(x_0=(0,0)^T\), the gradient is \((-1,-10)^T\), giving

\[
x_1=\begin{bmatrix}2/11\\20/11\end{bmatrix},
\qquad
e_1=x_1-x^*
=\begin{bmatrix}-9/11\\9/11\end{bmatrix}.
\]

The condition number is \(\kappa=L/m=10\). A larger condition number generally worsens first-order convergence because the objective has directions with very different curvature. A step size that is too large can cause oscillation or divergence; for this quadratic, stability requires \(0<\alpha<2/L\).

## Problem 2. Newton's method and curvature

Newton's method is

\[
x_{k+1}=x_k-[\nabla^2f(x_k)]^{-1}\nabla f(x_k).
\]

For this quadratic, the Hessian is Q everywhere and the gradient is \(Qx_k-b\). Therefore

\[
x_{k+1}=x_k-Q^{-1}(Qx_k-b)=Q^{-1}b=x^*.
\]

Exact arithmetic reaches the minimizer in one step from any initial point. This occurs because the quadratic model is the objective itself, not merely a local approximation. For a nonlinear objective the Hessian changes with x and the Newton step is based on a local second-order approximation; multiple steps and globalization may be needed.

Gradient methods use relatively inexpensive iterations and can exploit matrix-vector products, but may converge slowly on ill-conditioned problems. Newton methods can converge rapidly near a solution but require Hessian construction or Hessian-vector products and linear-system solves. Large sparse OPF models can make factorization expensive in memory and computation. Line searches, trust regions, regularization, and suitable initialization may be needed to maintain robust progress.

## Problem 3. Backtracking line search and sufficient decrease

At \(x_0=2\), \(f(x_0)=2\), \(\nabla f(x_0)=2\), and \(p_0=-2\). With \(\alpha=1\), the trial point is zero and

\[
f(0)=0
\leq2+10^{-4}(1)(2)(-2)=1.9996.
\]

The initial step is accepted, so \(\alpha=1\) and \(x_1=0\).

The Armijo condition requires a meaningful decrease relative to the directional derivative. It prevents acceptance of a step that fails the chosen sufficient-decrease test. It does not prove global optimality, guarantee a unique solution, or validate the physical model. A descent direction has \(\nabla f^Tp<0\). If an approximate Newton direction is not a descent direction, a line search may fail to find an acceptable positive step; a modified Hessian, trust-region method, or alternative direction may be required.

## Problem 4. Scaling and preconditioning

The eigenvalues of Q are 1 and 1000, so \(\kappa_2(Q)=1000\). The objective is much steeper in the second coordinate than the first. A step size small enough to remain stable in the steep direction can make progress very slowly in the shallow direction; a larger step may overshoot in the steep direction.

Let \(z=Q^{1/2}x\), so \(x=Q^{-1/2}z\). Then

\[
\frac12x^TQx=\frac12z^Tz,
\qquad
-b^Tx=-(Q^{-1/2}b)^Tz.
\]

The transformed Hessian is the identity, so the quadratic curvature is perfectly conditioned in these coordinates. Preconditioning seeks an equivalent representation with more favorable numerical scaling. It should not alter the physical constraints or the actual decision problem; if variables and constraints are transformed consistently, the underlying optimization problem is equivalent.

Energy models can mix MW, MWh, dollars, dollars per MWh, tonnes of CO2, and dimensionless variables. Poorly scaled coefficients can cause solver tolerances to be meaningful for one constraint but ineffective for another. Large differences between annual dollar totals and per-unit electrical quantities are a common source of numerical scaling problems.

## Problem 5. Least-squares calibration and numerical linear algebra

Ordinary least squares minimizes

\[
\min_\theta\|y-X\theta\|_2^2.
\]

Differentiating and setting the gradient to zero gives

\[
X^TX\hat\theta=X^Ty.
\]

If X has full column rank, its singular values are positive. The eigenvalues of \(X^TX\) are the squared singular values of X, so

\[
\kappa_2(X^TX)=\frac{\sigma_{\max}(X)^2}{\sigma_{\min}(X)^2}
=\kappa_2(X)^2.
\]

Forming \(X^TX\) squares the condition number and can lose numerical precision. QR factorization solves the least-squares problem without explicitly forming the normal equations and is a strong general-purpose choice. SVD is more computationally intensive but reveals rank deficiency and near-collinearity particularly clearly, and supports principled truncation or regularization. Normal equations may be efficient for well-conditioned problems but should not be the default when conditioning is uncertain.

Poorly scaled measurements can make coefficients numerically difficult to estimate. Nearly collinear regressors make separate effects weakly identified, inflate uncertainty, and can produce large changes in parameter estimates under small data perturbations.

## Problem 6. Stopping criteria and research reporting

A small relative objective change may occur because steps are tiny, the algorithm is stalled, the problem is poorly scaled, or the objective is locally flat. It does not alone establish a small gradient or satisfaction of constrained first-order conditions.

For constrained problems, report primal constraint violations, dual-feasibility violations, stationarity residuals, and complementary-slackness residuals, with definitions and scaling. State absolute and relative tolerances and explain the scales used. For nonconvex models, compare multiple initializations and algorithm settings, examine alternative stationary points, and avoid claiming global optimality without a suitable certificate.

Independently verify physical bounds, balance equations, units, data provenance, and whether the model represents the intended operating regime. Reproducibility requires the model formulation, input data or data hashes, software and solver versions, solver options, tolerances, random seeds, initialization, termination status, objective value, constraint residuals, and post-solve validation results.

