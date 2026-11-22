# Problem Set 5: Worked Solutions and Mathematical Notes

## Problem 1. Net-load uncertainty and covariance

Since \(N=L-W\),

\[
E[N]=E[L]-E[W]=1000-300=700\text{ MW},
\]

and

\[
\operatorname{Var}(N)=\sigma_L^2+\sigma_W^2-2\operatorname{Cov}(L,W).
\]

Under independence, the covariance is zero:

\[
\operatorname{Var}(N)=80^2+150^2=28900\text{ MW}^2,
\qquad \sigma_N=170\text{ MW}.
\]

The standardized threshold is

\[
z=\frac{900-700}{170}=1.1765.
\]

Thus \(P(N>900)=1-\Phi(1.1765)\approx0.1198\).

With correlation 0.4,

\[
\operatorname{Cov}(L,W)=0.4(80)(150)=4800\text{ MW}^2,
\]

so

\[
\operatorname{Var}(N)=6400+22500-9600=19300,
\qquad \sigma_N\approx138.924\text{ MW}.
\]

Now \(z=200/138.924\approx1.4396\), giving \(P(N>900)\approx0.0750\). Positive load-wind covariance enters the variance of a difference with a negative sign. When load and wind tend to be high together, their movements partly offset in net load. This conclusion depends on the sign and magnitude of covariance, not on a general claim that correlation always reduces uncertainty.

The joint-normal model may be inadequate because renewable output is bounded and often skewed; load and weather relationships can be nonlinear and seasonal; extreme weather can create tail dependence; forecast errors can be heteroskedastic; and spatially correlated renewable output and outages may matter.

## Problem 2. Conditional probability and demand response

The conditional failure probabilities are

\[
P(S^c\mid P)=1-0.80=0.20,
\qquad
P(S^c\mid P^c)=1-0.95=0.05.
\]

By total probability,

\[
P(S^c)=0.20(0.10)+0.05(0.90)=0.02+0.045=0.065.
\]

Bayes' theorem gives

\[
P(P\mid S^c)=\frac{P(S^c\mid P)P(P)}{P(S^c)}
=\frac{0.20(0.10)}{0.065}
\approx0.3077.
\]

A failed response is more likely during a peak-stress event under the stated assumptions, so observing failure increases the posterior probability of peak stress from 0.10 to about 0.308. These are conditional associations built into the assumptions. They are not automatically causal estimates: program enrollment, event selection, participant composition, and the definition of successful delivery could all create selection effects.

## Problem 3. Poisson outage arrivals and waiting times

For a homogeneous Poisson process,

\[
P(N(t)=k)=\frac{(\lambda t)^k e^{-\lambda t}}{k!}.
\]

Over five years, \(\lambda t=0.2(5)=1\). Therefore

\[
P(N(5)=2)=\frac{e^{-1}}{2}\approx0.18394.
\]

The probability of at least two events is

\[
P(N(5)\geq2)=1-P(N=0)-P(N=1)
=1-e^{-1}(1+1)
\approx0.26424.
\]

The waiting time \(T\) to the next event is exponential with rate \(\lambda\). Its expected value is \(1/\lambda=5\) years, and

\[
P(T>3)=e^{-0.2(3)}=e^{-0.6}\approx0.54881.
\]

The homogeneous Poisson assumptions include a constant event rate, independent increments, and negligible probability of simultaneous events in an infinitesimal interval. Weather clustering, aging-related hazard rates, common-cause failures, maintenance regimes, and cascading outages can violate these assumptions. Counts also omit duration, customers interrupted, energy not served, critical-load exposure, and severity.

## Problem 4. Markov weather regimes and renewable output

Each row of \(P\) sums to one and all entries are nonnegative, so it is a valid transition matrix.

Let \(\pi_H=h\), so \(\pi_L=1-h\). The stationary high-state equation is

\[
h=0.1(1-h)+0.7h,
\]

which gives \(0.4h=0.1\), hence

\[
\pi=(0.75,0.25).
\]

Long-run expected output is

\[
E[W]=0.75(100)+0.25(400)=175\text{ MW}.
\]

For a geometric run length with exit probability q per step, expected duration is \(1/q\). The low state has exit probability 0.1, so its expected run is 10 steps. The high state has exit probability 0.3, so its expected run is \(1/0.3\approx3.333\) steps.

Starting in L, the probability of being in H after two steps is the L-to-H entry of \(P^2\):

\[
P^{(2)}_{LH}=0.9(0.1)+0.1(0.7)=0.16.
\]

Independent resampling would erase serial persistence: it would not preserve the conditional transition probabilities or the distribution of consecutive high- and low-output periods. Before resource-adequacy use, the model would need timestamped weather and renewable data, a justified time step, out-of-sample transition validation, seasonal or spatial extensions where appropriate, and explicit linkage to load and outage processes.

## Problem 5. Chance constraints and reserve sizing

For a normally distributed net load, the chance constraint is equivalent to

\[
K\geq E[N]+z_{0.95}\sigma_N.
\]

Under independence,

\[
K_{0.95}=700+1.645(170)=979.65\text{ MW}.
\]

With correlation 0.4,

\[
K_{0.95}=700+1.645(138.924)\approx928.53\text{ MW}.
\]

The difference is approximately 51.12 MW. The positive correlation reduces the variance of the difference \(L-W\) in this example. It would be incorrect to generalize this result without examining the covariance structure and the signs of the underlying quantities.

A 95% one-hour chance constraint permits a 5% modeled exceedance probability for that interval. It is not a guarantee that capacity will be adequate in every interval, nor does it directly determine annual loss-of-load expectation or expected unserved energy. A system-wide reliability criterion must specify the time horizon, dependence across hours, weather-year sampling, forced outages, transmission constraints, demand response, load-shedding treatment, and the economic or policy basis for the target.

## Problem 6. Monte Carlo estimation and uncertainty

Define \(I_i=1\) if scenario i experiences the event and 0 otherwise. For independent, identically distributed Bernoulli trials,

\[
\hat p=\frac1n\sum_{i=1}^n I_i,
\qquad
\operatorname{SE}(\hat p)\approx\sqrt{\frac{\hat p(1-\hat p)}n}.
\]

A normal-approximation 95% margin of error is \(1.96\sqrt{p(1-p)/n}\). Using the conservative upper bound 0.25, require

\[
1.96\sqrt{0.25/n}\leq0.01
\quad\Longrightarrow\quad
n\geq\frac{1.96^2(0.25)}{0.01^2}=9604.
\]

This controls sampling error under the assumed generator. It does not correct bias from incorrect distributions, omitted dependence, unrepresentative scenarios, or a flawed physical model. Reproducible simulation should record random seeds, software versions, input-data provenance, scenario-generation logic, convergence diagnostics, sensitivity to assumptions, and validation on data or scenarios not used in calibration.

