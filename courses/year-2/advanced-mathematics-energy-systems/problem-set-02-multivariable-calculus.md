# Problem Set 2: Multivariable Calculus, Curvature, and Local Models

**Course:** Advanced Mathematical Methods for Energy Systems and Infrastructure Research  
**Module:** 2, Multivariable calculus and real-analysis foundations  
**Suggested effort:** 6–8 hours  
**Prerequisites:** Problem Set 1, partial derivatives, chain rule, matrix multiplication

## Instructions

Show each derivative and identify the point at which it is evaluated. Use radians for angles. Numerical software may verify results, but must not replace derivations. In every application question, state what the mathematical result does and does not establish about a physical energy system.

## Problem 1. Gradients and directional sensitivity (15 points)

Consider the smooth operating-cost proxy

\[
f(x,y)=x^2+xy+2y^2,
\]

where \(x\) and \(y\) are normalized decision variables representing two controllable resources.

1. Derive the gradient \(\nabla f(x,y)\).
2. Evaluate the gradient at \((1,-1)\).
3. Find the directional derivative at this point in the direction \(d=(3,4)^T\). Normalize the direction before taking the inner product.
4. Interpret the sign of the directional derivative. Does it imply that increasing both resource variables in their positive coordinate directions reduces cost?
5. Derive the first-order Taylor approximation around \((1,-1)\) and use it to estimate the change in \(f\) for a small displacement \(h=(0.02,-0.01)^T\). Compare the estimate with the exact change.

## Problem 2. Hessians and convexity (20 points)

For the same function \(f\):

1. Derive its Hessian.
2. Determine whether \(f\) is strictly convex using (i) principal minors and (ii) eigenvalues.
3. Find the unique unconstrained minimizer and minimum value.
4. Explain why a positive-definite Hessian is stronger than a positive-semidefinite Hessian. Give an energy-planning interpretation of a flat direction in a merely semidefinite objective.
5. Suppose the objective is augmented by a linear term \(-4x-2y\). Determine the new minimizer and explain why adding a linear term does not change the Hessian.

## Problem 3. Jacobian and Newton linearization (20 points)

Consider the nonlinear system

\[
F(x,y)=
\begin{bmatrix}
x^2+y-3\\
x+y^2-3
\end{bmatrix}=0.
\]

1. Derive the Jacobian matrix \(J_F(x,y)\).
2. Evaluate \(F\) and \(J_F\) at \((1,1)\).
3. Derive the Newton step by solving \(J_F(x_k)\Delta x=-F(x_k)\). Calculate the first update from \((1,1)\).
4. Evaluate the exact residual at the updated point. Compare it with the initial residual.
5. Explain why a nonsingular Jacobian is required for the ordinary Newton step, and why local convergence is not guaranteed from an arbitrary starting point.
6. Describe how this procedure relates to solving nonlinear AC power-flow equations, while identifying at least two important differences between this illustrative system and a real power-flow model.

## Problem 4. Taylor approximation and error control (15 points)

Let \(g(x,y)=e^x\cos y\).

1. Derive \(\nabla g\) and the Hessian \(H_g\).
2. Write the second-order Taylor approximation around \((0,0)\).
3. Evaluate the approximation at \((0.1,0.2)\) and compare it with the exact value.
4. Explain the role of the Hessian in capturing local curvature. Why should the Taylor approximation not be extrapolated far outside its expansion neighborhood?
5. State the regularity assumptions needed for a second-order Taylor expansion with a remainder term.

## Problem 5. Linear dynamical stability (20 points)

A simplified two-state linear model is

\[
\dot z=Az,\qquad
A=\begin{bmatrix}-0.2&1\\-2&-0.5\end{bmatrix}.
\]

The states are normalized deviations from an operating equilibrium; they are not specified physical measurements.

1. Compute the characteristic polynomial and eigenvalues of \(A\).
2. Classify the equilibrium as asymptotically stable, unstable, or marginally stable.
3. Explain the role of the real part and imaginary part of each eigenvalue.
4. Show how the solution form depends on the eigenvalues and describe the qualitative trajectory.
5. Explain why eigenvalue stability of a linearized model is a local statement when \(A\) comes from linearizing a nonlinear system.
6. Identify three ingredients missing before this illustrative matrix could be used to make a defensible claim about a real inverter, storage system, or grid-control loop.

## Problem 6. Research interpretation (10 points)

A researcher reports that a nonlinear solver converged and that the Jacobian at the solution is nonsingular.

Write a short technical critique addressing:

- what local information the nonsingular Jacobian provides;
- why solver convergence does not prove global uniqueness or global optimality;
- how scaling and conditioning affect numerical reliability;
- what validation against physical constraints, data, and alternative operating points is still required.

## Submission standard

Submit derivative derivations, Hessian/Jacobian evaluations, the Newton update, a quantitative Taylor-error comparison, an eigenvalue stability classification, and the research critique. Clearly label normalized variables and avoid assigning physical units that the problem does not define.

