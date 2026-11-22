# Problem Set 6: Numerical Optimization, Conditioning, and Convergence

**Course:** Advanced Mathematical Methods for Energy Systems and Infrastructure Research  
**Module:** 6, Numerical optimization  
**Suggested effort:** 7–9 hours  
**Prerequisites:** Problem Sets 1–3, eigenvalues, gradients and Hessians, convexity, basic numerical linear algebra

## Instructions

Distinguish algorithmic convergence from physical-model validity and from global optimality. Derive step-size and convergence claims from the stated assumptions. Report stopping criteria and numerical tolerances explicitly.

## Problem 1. Gradient descent on a strongly convex quadratic (20 points)

Consider

\[
f(x)=\frac12x^TQx-b^Tx,
\quad
Q=\begin{bmatrix}1&0\\0&10\end{bmatrix},
\quad
b=\begin{bmatrix}1\\10\end{bmatrix}.
\]

1. Derive the gradient and Hessian. Find the unique minimizer.
2. Show that the objective is strongly convex and has an L-Lipschitz gradient. Identify the strong-convexity parameter \(m\) and gradient-Lipschitz constant \(L\) in the Euclidean norm.
3. Write the gradient-descent iteration with constant step size \(\alpha\).
4. For \(\alpha=2/(L+m)\), calculate the spectral contraction factor for the error vector.
5. Starting from \(x_0=(0,0)^T\), calculate \(x_1\) and the error \(x_1-x^*\).
6. Explain how the condition number \(\kappa=L/m\) affects the convergence rate. What happens if the step size is too large?

## Problem 2. Newton's method and curvature (15 points)

Use the objective in Problem 1.

1. Derive the Newton update.
2. Starting from an arbitrary \(x_0\), show algebraically that exact Newton's method reaches the minimizer in one iteration.
3. Explain why this one-step result is special to a quadratic objective with a constant nonsingular Hessian.
4. Describe the trade-off between gradient descent and Newton's method for a large-scale optimal-power-flow or infrastructure-planning problem. Address Hessian factorization, memory, sparsity, and globalization.

## Problem 3. Backtracking line search and sufficient decrease (15 points)

Consider \(f(x)=\frac12x^2\), starting from \(x_0=2\), with descent direction \(p_0=-\nabla f(x_0)\).

Backtracking starts with \(\alpha=1\), multiplies the step by \(\beta=0.5\) after a rejected trial, and uses the Armijo condition

\[
f(x_0+\alpha p_0)
\leq f(x_0)+c\alpha\nabla f(x_0)^Tp_0,
\qquad c=10^{-4}.
\]

1. Evaluate the Armijo condition at the initial trial step.
2. State the accepted step and the next iterate.
3. Explain what sufficient decrease protects against and what it does not guarantee.
4. Why is a descent direction required? What can happen if an approximate Newton direction is not a descent direction?

## Problem 4. Scaling and preconditioning (20 points)

Consider

\[
\min_{x\in\mathbb R^2}
\frac12x^TQx-b^Tx,
\qquad
Q=\begin{bmatrix}1&0\\0&1000\end{bmatrix}.
\]

1. Calculate the spectral condition number of the Hessian.
2. Explain why unscaled gradient descent can make slow progress in one coordinate while oscillating or taking very small steps in another.
3. Define a change of variables \(z=Q^{1/2}x\). Show that the quadratic term becomes \(\frac12z^Tz\) and identify the transformed linear term.
4. Explain the role of preconditioning in numerical optimization and distinguish a mathematically equivalent change of variables from changing the underlying physical problem.
5. Give two examples of scaling problems that can arise when combining power, energy, dollars, and emissions in a planning model.

## Problem 5. Least-squares calibration and numerical linear algebra (15 points)

A researcher calibrates parameters \(\theta\) to measured outputs \(y\) using the linear model \(y=X\theta+\varepsilon\).

1. Derive the ordinary least-squares objective and its normal equations.
2. Show that the condition number of \(X^TX\) in the 2-norm is the square of the condition number of \(X\), when \(X\) has full column rank.
3. Explain why explicitly forming \(X^TX\) can worsen numerical reliability.
4. Compare solving by normal equations, QR factorization, and singular-value decomposition.
5. Explain how measurement scaling and nearly collinear explanatory variables affect parameter uncertainty and identifiability.

## Problem 6. Stopping criteria and research reporting (15 points)

An optimization solver returns a feasible solution and reports that the relative change in objective is below \(10^{-8}\).

Write a technical assessment addressing:

- why a small objective change does not alone establish stationarity or optimality;
- primal feasibility, dual feasibility, stationarity, and complementary-slackness residuals;
- scaling and the meaning of absolute versus relative tolerances;
- sensitivity to initialization and algorithm settings for nonconvex problems;
- independent verification of physical constraints and model assumptions;
- what should be recorded for reproducibility.

## Submission standard

Include the gradient-descent convergence derivation, Newton one-step proof, Armijo calculation, preconditioning transformation, least-squares conditioning result, and a concise solver-reporting checklist. Avoid presenting an algorithm's stopping flag as proof that the underlying energy-system model is valid.

