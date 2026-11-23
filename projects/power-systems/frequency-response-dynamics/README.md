# Computational Lab: Frequency Response and State-Space Dynamics

**Course:** Advanced Mathematical Methods for Energy Systems and Infrastructure Research  
**Model:** Illustrative two-state linear frequency-response model  
**Inputs:** Synthetic, normalized parameters; no operational grid data

## Objective

Connect the differential-equation problem set to a reproducible numerical implementation. Construct a state-space model, calculate its eigenvalues and equilibrium response to a step load disturbance, and compare continuous-time stability with the stability of explicit Euler integration.

## Run

```bash
python frequency_response.py
python frequency_response.py --inertia 10 --droop 0.04 --duration 10 --step 0.001
python -m unittest discover -s . -p "test_*.py" -v
```

No third-party packages are required.

## Model

The state is \(x=[\Delta f,\Delta p_m]^T\), where both quantities are normalized per-unit deviations. The input \(\Delta p_d\) is a normalized step load disturbance:

\[
\dot x=Ax+B\Delta p_d,
\quad
A=\begin{bmatrix}-0.2&0.2\\-40&-2\end{bmatrix},
\quad
B=\begin{bmatrix}-0.2\\0\end{bmatrix}.
\]

The matrix corresponds to the illustrative parameter values \(M=5\) s, \(D=1\), \(T_g=0.5\) s, and \(R=0.05\). The eigenvalues are approximately \(-1.1\pm2.6814i\), so the continuous-time linear model is asymptotically stable.

For a constant disturbance, the equilibrium is

\[
\Delta f^*=-\frac{\Delta p_d}{D+1/R},
\qquad
\Delta p_m^*=-\frac{\Delta f^*}{R}.
\]

The implementation integrates the state equations with fourth-order Runge-Kutta (RK4). It also calculates the explicit-Euler step-size boundary for this complex eigenvalue pair. The CLI exposes inertia, damping, governor time constant, and droop so parameter changes are applied consistently to both the state matrix and disturbance input. Both integrators include a final partial step when the requested duration is not an integer multiple of the step size.

## Required analysis

1. Re-derive the state matrix from the swing-equation/governor approximation in Problem Set 4.
2. Compare the simulated terminal state with the analytical steady state.
3. Run explicit Euler below and above the calculated stability boundary. Explain why the time step affects numerical stability, not the physical model's continuous-time eigenvalues.
4. Run the CLI with at least two inertia and droop combinations. Compare eigenvalues, transient trajectories, and the steady-state frequency deviation. Explain why inertia changes transient behavior but not this model's equilibrium frequency expression.
5. Discuss which measurements would be needed to calibrate this model and validate its response.

## Limitations

This is a deliberately small, linear, single-area illustration. It omits network topology, multiple machines, inverter-based resources, detailed governor/turbine and load dynamics, deadbands, saturation, delays, protection, voltage behavior, and spatial modes. The parameter values are synthetic. The results are not a forecast, operating limit, or frequency-security assessment for PJM or any utility system.
