# Problem Set 4: Worked Solutions and Mathematical Notes

## Problem 1. First-order storage dynamics

For constant \(u_0\), solve \(\dot e+ke=u_0\). The equilibrium is \(e^*=u_0/k\), and

\[
e(t)=e^*+(e_0-e^*)e^{-kt}
=\frac{u_0}{k}+\left(e_0-\frac{u_0}{k}\right)e^{-kt}.
\]

The homogeneous mode has eigenvalue \(-k=-0.2\;\text{h}^{-1}\), so the equilibrium is asymptotically stable. For \(e_0=0.4\), \(u_0=0.1\;\text{h}^{-1}\), the equilibrium is 0.5 and

\[
e(5)=0.5+(0.4-0.5)e^{-1}
\approx0.46321.
\]

The unconstrained model can predict values outside the physical interval [0,1]. A real controller must enforce state-of-charge limits, and the input may be curtailed or changed when a bound is reached. This model omits charge/discharge efficiency asymmetry, power limits, degradation, temperature, voltage dependence, and detailed electrochemical dynamics.

## Problem 2. Linear state-space model and eigenvalue stability

Let \(x=[\Delta f,\Delta p_m]^T\). Dividing the first equation by \(M\) and the second by \(T_g\) gives

\[
\dot x=Ax+B\Delta p_d,
\quad
A=\begin{bmatrix}
-D/M&1/M\\
-1/(T_gR)&-1/T_g
\end{bmatrix}
=\begin{bmatrix}-0.2&0.2\\-40&-2\end{bmatrix},
\quad
B=\begin{bmatrix}-1/M\\0\end{bmatrix}
=\begin{bmatrix}-0.2\\0\end{bmatrix}.
\]

The characteristic polynomial is

\[
\det(sI-A)=(s+0.2)(s+2)+8
=s^2+2.2s+8.4.
\]

The roots are

\[
s=-1.1\pm\frac{\sqrt{7.19}}{1}i
\approx-1.1\pm2.6814i.
\]

Both real parts are negative, so the unforced equilibrium is asymptotically stable. The negative real part determines exponential decay, while the imaginary part indicates an oscillatory component.

For a constant disturbance, set both derivatives to zero. The governor equation gives \(\Delta p_m=-\Delta f/R=-20\Delta f\). Substitution into the first equation gives

\[
0=-20\Delta f-D\Delta f-0.01,
\quad
\Delta f^*=-\frac{0.01}{21}\approx-0.00047619\;\text{p.u.}
\]

and

\[
\Delta p_m^*=-20\Delta f^*\approx0.00952381\;\text{p.u.}
\]

This simplified model omits network modes, multiple generators, inverter controls, nonlinear limits, detailed turbine-governor dynamics, protection, and spatially varying frequency/voltage behavior. It is an analytical illustration, not a security assessment.

## Problem 3. Matrix exponential and modal response

The unforced solution is

\[
x(t)=e^{At}x(0).
\]

If \(A=V\Lambda V^{-1}\), then

\[
e^{At}=Ve^{\Lambda t}V^{-1},
\]

where each diagonal entry of \(e^{\Lambda t}\) is \(e^{\lambda_i t}\). The initial condition determines the contribution of each mode, while the output equation determines how strongly a mode appears in a measured quantity. A stable mode can still matter if it is weakly damped or strongly excited and visible in the output.

If a repeated eigenvalue has insufficient independent eigenvectors, the matrix has a Jordan block. The exponential then includes polynomial factors multiplying exponentials, such as \(t e^{\lambda t}\), rather than only independent modal exponentials.

## Problem 4. Explicit Euler and numerical stability

The Euler update matrix is \(I+hA\). Asymptotic stability requires every eigenvalue \(1+h\lambda_i(A)\) to lie strictly inside the unit circle:

\[
|1+h\lambda_i|<1.
\]

For \(\lambda=-1.1\pm2.6814i\),

\[
(1-1.1h)^2+(2.6814h)^2<1.
\]

Expanding and simplifying gives

\[
-2.2h+8.4h^2<0.
\]

For positive \(h\), this requires

\[
0<h<\frac{2.2}{8.4}\approx0.26190\;\text{s}.
\]

Thus 0.1 s is stable under this linear test, while 0.3 s is not. Explicit Euler can introduce numerical growth because its discrete-time amplification factor lies outside the unit circle even though the continuous-time eigenvalues have negative real parts.

Backward Euler has amplification factor \(1/(1-h\lambda)\) and is A-stable for linear systems with eigenvalues in the left half-plane. It is generally more robust for stiff stable systems, although it introduces numerical damping and requires solving an implicit system at each step.

## Problem 5. Equilibria, linearization, and local stability

Let \(x=x^*+\delta x\). A first-order Taylor expansion gives

\[
F(x^*+\delta x)=F(x^*)+J_F(x^*)\delta x+o(\|\delta x\|).
\]

Since \(F(x^*)=0\), the local perturbation model is

\[
\delta\dot x=J_F(x^*)\delta x.
\]

If the Jacobian has all eigenvalues with strictly negative real parts, the equilibrium is locally asymptotically stable under the standard smoothness assumptions. If an eigenvalue has zero real part, linearization alone is inconclusive; nonlinear higher-order terms may determine stability.

A controller may be stable for small deviations but behave differently after a large disturbance triggers current limits, inverter ride-through logic, generator protection, or saturation. The operating equations and active controls then change, so the local Jacobian no longer describes the full trajectory.

## Problem 6. Model validation and research interpretation

Stable eigenvalues characterize the fitted linear model at its specified operating point. They do not establish that the model is valid across loading conditions or control modes. Parameter identifiability must be assessed: different parameter combinations can produce similar outputs, particularly when data do not sufficiently excite all modes.

The study should document sensor sampling rates, filtering, timestamp alignment, missing data, noise, and any resampling. It should test whether actuator saturation, deadbands, communication delays, current limits, and protection logic are represented. Calibration and validation data should be separated, and validation should cover the intended operating envelope and relevant disturbances. Finally, eigenvalue stability does not by itself guarantee acceptable damping, overshoot, settling time, frequency nadir, voltage limits, thermal limits, or system-wide security. Those require output-specific performance criteria and appropriate network and device models.

