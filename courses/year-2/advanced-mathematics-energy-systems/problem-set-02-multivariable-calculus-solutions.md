# Problem Set 2: Worked Solutions and Mathematical Notes

## Problem 1. Gradients and directional sensitivity

For \(f=x^2+xy+2y^2\),

\[
\nabla f=
\begin{bmatrix}2x+y\\x+4y\end{bmatrix}.
\]

At \((1,-1)\), this is \((1,-3)^T\). The unit vector in the direction \((3,4)^T\) is \(u=(3/5,4/5)^T\). Thus

\[
D_uf(1,-1)=\nabla f^Tu=1(3/5)-3(4/5)=-9/5=-1.8.
\]

The function decreases initially along this particular direction. This does not imply that increasing both coordinates independently reduces the function; the directional result applies only to the specified combined direction.

The first-order expansion is

\[
f((1,-1)+h)\approx f(1,-1)+\nabla f(1,-1)^Th.
\]

Since \(f(1,-1)=2\), the predicted change for \(h=(0.02,-0.01)^T\) is \(0.02+0.03=0.05\), giving an approximation of 2.05. The exact change is

\[
f(1.02,-1.01)-2
=1.0404-1.0302+2(1.0201)-2=0.0504.
\]

The first-order estimate is low by 0.0004; the discrepancy is the second-order contribution.

## Problem 2. Hessians and convexity

The Hessian is constant:

\[
H_f=\begin{bmatrix}2&1\\1&4\end{bmatrix}.
\]

Its leading principal minors are 2 and \(8-1=7\), both positive. Therefore it is positive definite by Sylvester's criterion. Its eigenvalues solve \(\lambda^2-6\lambda+7=0\), giving \(3\pm\sqrt2\), both positive. Hence \(f\) is strictly convex.

Set the gradient to zero:

\[
2x+y=0,\qquad x+4y=0.
\]

The unique solution is \((0,0)\), and \(f(0,0)=0\).

A positive-definite Hessian means positive curvature in every nonzero direction and, for this quadratic, a unique minimizer. A positive-semidefinite Hessian can have zero-curvature directions, so multiple points may have the same objective value along a flat direction. In an energy-planning problem this could represent substitutable investments or resource mixes that the objective does not distinguish; additional constraints or cost terms may be needed.

For \(f-4x-2y\), the gradient condition becomes

\[
2x+y=4,\qquad x+4y=2.
\]

Solving gives \(x=14/7=2\) and \(y=0\). The Hessian remains unchanged because linear functions have zero second derivatives.

## Problem 3. Jacobian and Newton linearization

The Jacobian is

\[
J_F(x,y)=\begin{bmatrix}2x&1\\1&2y\end{bmatrix}.
\]

At \((1,1)\),

\[
F(1,1)=\begin{bmatrix}-1\\-1\end{bmatrix},
\qquad
J_F(1,1)=\begin{bmatrix}2&1\\1&2\end{bmatrix}.
\]

The Newton equation is

\[
\begin{bmatrix}2&1\\1&2\end{bmatrix}
\begin{bmatrix}\Delta x\\\Delta y\end{bmatrix}
=\begin{bmatrix}1\\1\end{bmatrix}.
\]

It gives \(\Delta x=\Delta y=1/3\), so the new point is \((4/3,4/3)\). At that point each residual is

\[
(4/3)^2+4/3-3=16/9+12/9-27/9=1/9.
\]

The initial residual components were −1, so their absolute values have fallen from 1 to 1/9 in this step.

The ordinary Newton update requires an invertible Jacobian so that the linear system has a unique step. Local convergence results require additional regularity and a sufficiently good starting point; an arbitrary initial point can diverge, encounter a singular Jacobian, or move into an invalid region.

AC power flow also uses a nonlinear system and a Jacobian-based Newton method. But a real formulation includes network admittances, voltage magnitudes and phase angles, specified active/reactive injections, bus types, and operating limits. The two-equation example has no electrical parameterization, reactive-power model, controls, or operational constraints.

## Problem 4. Taylor approximation and error control

For \(g=e^x\cos y\),

\[
\nabla g=
\begin{bmatrix}e^x\cos y\\-e^x\sin y\end{bmatrix},
\quad
H_g=e^x\begin{bmatrix}\cos y&-\sin y\\-\sin y&-\cos y\end{bmatrix}.
\]

At the origin, \(g=1\), \(\nabla g=(1,0)^T\), and

\[
H_g(0,0)=\begin{bmatrix}1&0\\0&-1\end{bmatrix}.
\]

The second-order Taylor polynomial is therefore

\[
T_2(x,y)=1+x+\tfrac12(x^2-y^2).
\]

At \((0.1,0.2)\), this is \(1+0.1+0.5(0.01-0.04)=1.085\). The exact value is \(e^{0.1}\cos(0.2)\approx1.0853\), so the approximation error is approximately 0.0003 (the precise value depends on rounding).

The Hessian encodes local curvature, including directions of positive and negative curvature. A Taylor polynomial is local: higher-order terms can become material as the displacement grows. A standard second-order Taylor result with a remainder applies when the function has sufficiently regular second derivatives in a neighborhood of the expansion point; continuity of the second partial derivatives is a common sufficient condition.

## Problem 5. Linear dynamical stability

The characteristic polynomial is

\[
\det(\lambda I-A)
=(\lambda+0.2)(\lambda+0.5)+2
=\lambda^2+0.7\lambda+2.1.
\]

The roots are

\[
\lambda=-0.35\pm\frac{\sqrt{7.91}}2 i
\approx -0.35\pm1.407i.
\]

Both eigenvalues have negative real part, so the origin is an asymptotically stable equilibrium of this continuous-time linear system. The negative real part produces exponential decay; the nonzero imaginary part produces oscillation. The qualitative response is a decaying oscillation, with an envelope proportional to \(e^{-0.35t}\).

If \(A\) is the Jacobian of a nonlinear system evaluated at an equilibrium, this eigenvalue result describes sufficiently small perturbations under the usual linearization assumptions. It does not establish global stability or rule out other equilibria, saturation, protection actions, or large-disturbance behavior.

Before applying such a matrix to a real device or grid, one would need (at minimum): a documented physical model and parameter values; a defined operating point and state/input/output meanings with units; and validation against manufacturer, laboratory, or field data over the intended operating envelope. Control limits, delays, sampling, and network coupling may also be essential.

## Problem 6. Research interpretation

A nonsingular Jacobian means the local linearization is invertible. Under suitable smoothness assumptions, the inverse-function theorem supports local isolation and local solvability of the corresponding equation near the point. It does not establish that no other solutions exist elsewhere. Nor does convergence of a root-finding algorithm prove global optimality: root finding and optimization are different mathematical tasks, and a stationary point may be a local maximum or saddle point.

Poor scaling can make numerically equivalent equations difficult to solve, while ill-conditioning can amplify data and rounding errors. A defensible analysis should report variable and residual scales, solver tolerances, conditioning diagnostics, and sensitivity to starting values. It should also test physical feasibility, operational constraints, data provenance, alternative initializations, and whether the solution remains meaningful under plausible parameter perturbations.

