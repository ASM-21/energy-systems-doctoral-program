# Problem Set 5: Probability, Stochastic Processes, and Reliability Modeling

**Course:** Advanced Mathematical Methods for Energy Systems and Infrastructure Research  
**Module:** 4, Probability and stochastic processes  
**Suggested effort:** 7–9 hours  
**Prerequisites:** Probability distributions, expectation and variance, matrix algebra, basic statistical inference

## Instructions

Show probability calculations and state every independence, distributional, and stationarity assumption. Distinguish a model probability from an empirically estimated frequency. Use consistent time units. Numerical computation may verify a result, but must not replace the derivation.

## Problem 1. Net-load uncertainty and covariance (20 points)

For a one-hour operating interval, forecast load \(L\) and available wind generation \(W\), in MW, are modeled as jointly normal random variables with

\[
E[L]=1000,\quad \sigma_L=80,\qquad
E[W]=300,\quad \sigma_W=150.
\]

Define net load \(N=L-W\).

1. Derive \(E[N]\) and \(\operatorname{Var}(N)\) in terms of \(\operatorname{Cov}(L,W)\).
2. Under independence, calculate the standard deviation of net load.
3. Calculate \(P(N>900)\) under independence. State the standardized threshold and the approximate probability.
4. Now suppose the correlation between load and wind is \(\rho_{LW}=0.4\). Recalculate the variance, standard deviation, and exceedance probability.
5. Explain why positive correlation between load and wind can reduce net-load variance, even though positive correlation often increases the variance of a sum.
6. Identify at least three reasons the joint-normal model may be inadequate for operational risk assessment.

## Problem 2. Conditional probability and demand-response performance (15 points)

A system operator uses a demand-response program as an operational resource. Let \(P\) denote a peak-stress event and \(S\) denote successful demand-response delivery. Historical engineering assumptions are

\[
P(P)=0.10,\qquad P(S\mid P)=0.80,\qquad
P(S\mid P^c)=0.95.
\]

1. Calculate \(P(S^c\mid P)\) and \(P(S^c\mid P^c)\).
2. Use the law of total probability to calculate \(P(S^c)\).
3. Apply Bayes' theorem to calculate \(P(P\mid S^c)\).
4. Explain why the posterior probability of a peak event after a failed response differs from the unconditional peak-event probability.
5. Explain why the assumed conditional probabilities should not be treated as causal estimates without information about program selection, event definitions, and the data-generating process.

## Problem 3. Poisson outage arrivals and waiting times (15 points)

Suppose independent equipment outage initiations are approximated by a homogeneous Poisson process with rate \(\lambda=0.2\) events per year.

1. State the probability mass function for the number of events \(N(t)\) in an interval of length \(t\).
2. Calculate the probability of exactly two events in five years.
3. Calculate the probability of at least two events in five years.
4. Derive the expected waiting time to the next event and calculate the probability that the waiting time exceeds three years.
5. Explain the assumptions required for a homogeneous Poisson process. Give two plausible grid-outage mechanisms that could violate them.
6. Explain why event counts alone do not measure customer reliability; duration, affected customers, and event severity also matter.

## Problem 4. Markov weather regimes and renewable output (20 points)

A simplified weather-regime process has two states: Low renewable output (L) and High renewable output (H). The one-step transition matrix, with rows denoting the current state and columns the next state, is

\[
P=\begin{bmatrix}
0.9&0.1\\
0.3&0.7
\end{bmatrix}.
\]

Renewable output is 100 MW in state L and 400 MW in state H.

1. Verify that \(P\) is a valid transition matrix.
2. Find the stationary distribution \(\pi\), satisfying \(\pi=\pi P\) and \(\pi_L+\pi_H=1\).
3. Calculate long-run expected renewable output.
4. Calculate the expected duration, in time steps, of a consecutive L regime and a consecutive H regime.
5. Starting in state L, calculate the probability of being in state H after two steps.
6. Explain why independently sampling the two states each period would fail to preserve the persistence represented by this Markov chain.
7. Identify what additional data and validation would be needed before using such a regime model for resource-adequacy analysis.

## Problem 5. Chance constraints and reserve sizing (20 points)

Use the net-load model from Problem 1. The operator wants firm available capacity \(K\) to satisfy

\[
P(N\leq K)\geq0.95.
\]

1. Under the independent joint-normal assumption, derive the minimum capacity \(K\) that satisfies the chance constraint. Use the standard-normal 95th percentile \(z_{0.95}=1.645\).
2. Repeat using \(\rho_{LW}=0.4\).
3. Quantify the difference in required capacity between the two assumptions.
4. Explain the distinction between a 95% one-hour chance constraint and a deterministic guarantee of adequacy.
5. Discuss at least four modeling or policy choices hidden inside a statement that the system should satisfy a 95% reliability target. Consider time aggregation, correlated weather, forced outages, load shedding, and the cost of reserve.

## Problem 6. Monte Carlo estimation and uncertainty (10 points)

A researcher estimates a rare operating-event probability by simulating independent scenarios.

1. Define the Bernoulli indicator \(I_i\) for whether scenario \(i\) experiences the event, and derive the Monte Carlo estimator \(\hat p\).
2. Derive or state the approximate standard error of \(\hat p\).
3. Using the conservative variance bound \(p(1-p)\leq0.25\), calculate the sample size needed for a 95% normal-approximation margin of error no greater than 0.01.
4. Explain why a small standard error does not correct a biased or misspecified scenario generator.
5. List practical steps for reproducible simulation, including random seeds, scenario provenance, convergence checks, and out-of-sample validation.

## Submission standard

Submit the net-load covariance derivation, Bayes calculation, Poisson probabilities, stationary Markov distribution, chance-constrained capacity calculations, and Monte Carlo precision analysis. Explicitly label assumptions and distinguish mathematical uncertainty from uncertainty about the model itself.

