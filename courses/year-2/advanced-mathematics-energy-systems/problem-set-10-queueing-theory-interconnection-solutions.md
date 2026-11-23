# Problem Set 10: Worked Solutions and Mathematical Notes

## Problem 1. M/M/1

For \(\lambda=6\) and \(\mu=8\) applications per business day,

\[
\rho=\frac{\lambda}{\mu}=0.75.
\]

The stationary M/M/1 results are

\[
P(\text{wait})=\rho=0.75,\quad
L=\frac{\rho}{1-\rho}=3,\quad
L_q=\frac{\rho^2}{1-\rho}=2.25.
\]

The mean service time is \(1/\mu=0.125\) business day. Total time and queue time are

\[
W=\frac{1}{\mu-\lambda}=0.5,\qquad
W_q=W-\frac{1}{\mu}=0.375\text{ business day}.
\]

Little's Law checks: \(L_q=\lambda W_q=6(0.375)=2.25\) and \(L=\lambda W=6(0.5)=3\). Queue wait is the time before service begins; total time includes both queue wait and active service.

At \(\lambda=8=\mu\), utilization is one and the M/M/1 steady-state distribution does not exist. For \(\lambda\geq\mu\), the queue is unstable.

## Problem 2. M/M/2

Here \(\lambda=12\), \(\mu=8\), \(c=2\), offered load \(a=1.5\), and utilization \(\rho=0.75\).

For an M/M/c queue,

\[
P_0=\left[
\sum_{n=0}^{c-1}\frac{a^n}{n!}
+\frac{a^c}{c!(1-\rho)}
\right]^{-1}.
\]

Thus

\[
P_0=\left[1+1.5+\frac{1.5^2}{2(1-0.75)}\right]^{-1}
=\frac17.
\]

Erlang C gives

\[
P(\text{wait})=
\frac{a^c}{c!(1-\rho)}P_0
=\frac{9}{14}\approx0.642857.
\]

The expected queue wait is

\[
W_q=\frac{P(\text{wait})}{c\mu-\lambda}
=\frac{9/14}{4}=\frac9{56}
\approx0.160714\text{ day}.
\]

Then

\[
W=W_q+\frac1\mu=\frac27\approx0.285714,
\]
\[
L_q=\lambda W_q=\frac{27}{14}\approx1.928571,
\qquad
L=\lambda W=\frac{24}{7}\approx3.428571.
\]

Capacity exceeds arrivals on average, but random arrivals can occur while both reviewers are busy. The queue absorbs this stochastic mismatch. Little's Law holds by construction.

## Problem 3. M/M/3

Now \(c=3\), so \(\rho=12/(3\cdot8)=0.5\), while \(a=1.5\) remains unchanged.

\[
P_0=\left[
1+1.5+\frac{1.5^2}{2}
+\frac{1.5^3}{3!(1-0.5)}
\right]^{-1}
=\frac4{19}.
\]

The Erlang-C probability is

\[
P(\text{wait})=
\frac{1.5^3}{3!(1-0.5)}\frac4{19}
=\frac9{38}\approx0.236842.
\]

Then

\[
W_q=\frac{9/38}{24-12}=\frac3{152}
\approx0.019737\text{ day},
\]
\[
W=W_q+\frac18=\frac{11}{76}
\approx0.144737\text{ day},
\]
\[
L_q=12W_q=\frac9{38}\approx0.236842,
\qquad
L=12W=\frac{33}{19}\approx1.736842.
\]

The queue-wait reduction is

\[
1-\frac{W_{q,3}}{W_{q,2}}
=1-\frac{3/152}{9/56}
\approx87.72%.
\]

Nominal capacity rises from 16 to 24 applications per day, a 50% increase, while queue wait falls by about 87.7%. Waiting is nonlinear in utilization because the probability all servers are busy and the expected residual congestion both change. A real process may not realize this idealized gain if qualified reviewers are not interchangeable, work is routed by discipline, service times are non-exponential, cases require multiple sequential approvals, or incoming demand changes in response to faster processing.

## Problem 4. Illustrative staffing cost

For two reviewers,

\[
C(2)=500(2)+300\left(\frac{27}{14}\right)
\approx\$1,578.57.
\]

For three reviewers,

\[
C(3)=500(3)+300\left(\frac9{38}\right)
\approx\$1,571.05.
\]

Under these assumed coefficients, three reviewers have a slightly lower modeled cost. The break-even waiting-cost coefficient \(b^*\) satisfies

\[
1000+b^*\frac{27}{14}
=1500+b^*\frac9{38}.
\]

Therefore

\[
b^*=\frac{500}{27/14-9/38}
=\frac{66,500}{225}
\approx\$295.56\text{ per application-day}.
\]

The result is sensitive to the waiting-cost coefficient. Without a defensible estimate, report a sensitivity curve or break-even threshold rather than claiming a unique optimal staffing level. The illustrative penalty is not an observed customer harm or a regulated cost.

## Problem 5. Arrival-rate sensitivity

At \(\lambda=13.2\), \(\mu=8\), and \(c=2\), utilization is

\[
\rho=\frac{13.2}{16}=0.825.
\]

The M/M/2 formulas give

\[
a=1.65,\quad
P_0=\left[1+1.65+\frac{1.65^2}{2(1-0.825)}\right]^{-1},
\]
\[
P(\text{wait})=
\frac{1.65^2}{2(1-0.825)}P_0,
\qquad
W_q=\frac{P(\text{wait})}{16-13.2}.
\]

Numerically, \(P_0\approx0.09589\), \(P(\text{wait})\approx0.7458\), and \(W_q\approx0.2664\) day. A 10% increase in arrivals raises utilization from 75% to 82.5%, while expected queue wait rises from about 0.1607 to 0.2664 day, an increase of approximately 65.8%. This is the nonlinear congestion effect.

A constant-rate Poisson process can understate peak periods. A more credible stress test would estimate or specify time-varying arrival rates by month/season, preserve observed burst patterns, and compare baseline, peak, and sustained-high-arrival regimes. If service capacity also changes with staffing calendars, model that explicitly.

## Problem 6. Multi-stage process

A defensible process model represents distinct states and event transitions, not merely a single duration. At minimum, track arrival, completeness, each review-stage queue entry and service start/end, customer-pause start/end, rework, supplemental study, agreement, construction, PTO, denial, and withdrawal.

Three independent M/M/c queues assume memoryless arrivals and services at each stage and simplified routing. They may miss correlated stage workloads, shared specialist resources, feedback loops, priority classes, customer delays, and selection into later stages. A discrete-event simulation should represent the event sequence and routing rules explicitly, estimate parameters from a development sample, and compare predictions against held-out cohorts and stage-level wait distributions. Validate not only average time but also medians, upper quantiles, queue lengths, throughput, and terminal outcomes.

## Problem 7. Empirical identification

Annual aggregate request counts can describe reported arrivals only at a coarse annual EDC level. They do not identify service rates, utilization, queue length, waiting time, or the probability an application waits. Aggregate mean review days are not linked to individual service intervals and may use denominators that differ from request counts. Dividing one by the other does not recover utilization.

A minimum event-history dataset needs de-identified application IDs, EDC and pseudonymous process/feeder assignment, event timestamps, review stage, queue entry, service start/end, customer-pause intervals, rework and external-dependency events, project attributes, policy regime, terminal status, and observation cutoff. Open cases require right-censoring rather than deletion.

Model-risk checks should include arrival-rate seasonality, overdispersion relative to Poisson, service-time distribution fit, stage-specific heterogeneity, FCFS/priority discipline, censoring and competing outcomes, parameter uncertainty, and out-of-sample predictive calibration.

## Problem 8. Computational verification

The repository lab tests the exact M/M/2 and M/M/3 results, Little's Law identities, stability boundary, and fixed-seed reproducibility. A discrete-event simulation should approach the Erlang-C values as the number of simulated customers grows, but finite samples differ because of random variation and initialization. A warm-up period reduces bias from an initially empty system; it does not guarantee the simulation is representative of a real process.

Changing arrivals to a non-homogeneous process or service times to a heavy-tailed distribution violates M/M/c assumptions. The analytical Erlang-C values then become a benchmark under the simplified model, not the correct answer for the modified system. Validate the modified simulation against independent calculations, event-history data, or carefully designed stress tests.

## General warning

Queueing models describe the relationship between arrivals, service capacity, routing, and delay under explicit assumptions. They do not establish why applications arrive, whether staffing changes are feasible, what delay costs customers, or whether a policy intervention caused an outcome. Those questions require separate empirical and institutional evidence.
