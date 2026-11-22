# Problem Set 4: Differential Equations, State-Space Models, and Numerical Stability

**Course:** Advanced Mathematical Methods for Energy Systems and Infrastructure Research  
**Module:** 3, Differential equations and dynamical systems  
**Suggested effort:** 7–9 hours  
**Prerequisites:** Problem Sets 1–2, eigenvalues/eigenvectors, first-order ODEs, matrix exponentials

## Instructions

Distinguish continuous-time physical stability from numerical stability of a discretization. State units and sign conventions. Use exact derivations where possible and numerical computation only to verify results.

## Problem 1. First-order storage dynamics (15 points)

A normalized storage state \(e(t)\) follows

\[
\dot e(t)=-ke(t)+u(t),
\]

where \(k=0.2\;\text{h}^{-1}\), \(e\) is stored energy normalized by rated energy, and \(u\) is a normalized charging input per hour.

1. For constant input \(u(t)=u_0\), derive the closed-form solution for arbitrary initial condition \(e(0)=e_0\).
2. Determine the equilibrium and its stability for constant \(u_0\).
3. If \(e_0=0.4\) and \(u_0=0.1\;\text{h}^{-1}\), calculate \(e(5)\).
4. Explain how a state-of-charge bound \(0\leq e(t)\leq1\) changes the interpretation of the unconstrained solution.
5. Describe why this first-order model is not a complete battery model.

## Problem 2. Linear state-space model and eigenvalue stability (20 points)

Consider a simplified frequency-response model:

\[
\begin{aligned}
M\dot{\Delta f}&=\Delta p_m-D\Delta f-\Delta p_d,\\
T_g\dot{\Delta p_m}&=-\Delta p_m-\frac{1}{R}\Delta f,
\end{aligned}
\]

with \(M=5\;\text{s}\), \(D=1\), \(T_g=0.5\;\text{s}\), and \(R=0.05\). Variables are per-unit deviations; time is in seconds.

1. Write the model in state-space form \(\dot x=Ax+B\Delta p_d\), defining the state vector and disturbance input.
2. Compute the characteristic polynomial and eigenvalues of \(A\).
3. Classify the unforced equilibrium. Explain the physical interpretation of the real and imaginary parts of the eigenvalues.
4. For a constant disturbance \(\Delta p_d=0.01\) p.u., derive the steady-state frequency deviation and governor power deviation.
5. Explain why this two-state model is useful for analysis but insufficient for an operational frequency-security study.

## Problem 3. Matrix exponential and modal response (15 points)

For the state matrix in Problem 2:

1. State the general solution of the unforced system in terms of the matrix exponential.
2. Explain how eigen-decomposition can be used to express the solution when \(A\) is diagonalizable.
3. Explain the physical meaning of modal participation: why might a stable mode still be important to an observed output?
4. Describe what changes in the solution structure if a matrix has a repeated eigenvalue but is not diagonalizable.

## Problem 4. Explicit Euler and numerical stability (20 points)

Apply explicit Euler to the unforced system \(\dot x=Ax\):

\[
x_{k+1}=(I+hA)x_k,
\]

where \(h\) is the time step.

1. State the condition on the eigenvalues of \(I+hA\) required for asymptotic numerical stability.
2. Use the eigenvalues from Problem 2 to derive the maximum stable positive step size \(h\).
3. Determine whether \(h=0.1\;\text{s}\) and \(h=0.3\;\text{s}\) satisfy the condition.
4. Explain how a numerically unstable simulation can occur even when the underlying continuous-time system is asymptotically stable.
5. Briefly compare explicit Euler with an implicit method such as backward Euler for stiff systems.

## Problem 5. Equilibria, linearization, and local stability (15 points)

Consider a nonlinear system \(\dot x=F(x)\), with equilibrium \(x^*\) satisfying \(F(x^*)=0\).

1. Derive the first-order local model for perturbations \(\delta x=x-x^*\).
2. State the eigenvalue condition that establishes local asymptotic stability for a continuously differentiable system when no eigenvalue has zero real part.
3. Explain why an eigenvalue on the imaginary axis requires more analysis.
4. Give an energy-system example where a local stability result may fail to describe behavior after a large disturbance or a control limit is reached.

## Problem 6. Model validation and research interpretation (15 points)

A study calibrates a linear state-space model to measured frequency and inverter-response data and reports stable eigenvalues.

Write a technical review that addresses:

- operating-point dependence and model linearization;
- parameter identifiability and uncertainty;
- sampling rate, filtering, time synchronization, and measurement noise;
- actuator saturation, deadbands, delays, and protection logic;
- validation on data not used for calibration;
- why stable eigenvalues alone do not prove acceptable transient performance or system-wide security.

## Submission standard

Include the closed-form scalar solution, a state-space derivation, eigenvalue calculations, a numerical integration stability bound, and a model-validation critique. All state variables, parameters, and units must be defined.

