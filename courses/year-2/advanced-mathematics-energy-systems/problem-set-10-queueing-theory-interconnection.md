# Problem Set 10: Queueing Theory and Interconnection Process Capacity

**Level:** Advanced graduate / doctoral extension  
**Suggested effort:** 2–3 hours  
**Prerequisites:** Probability, stochastic processes, expected values, and basic Python  
**Status:** Optional Year 2 extension; it should displace other work rather than increase the weekly study budget.

## Learning objectives

1. Derive steady-state metrics for M/M/1 and M/M/c queues.
2. Explain why waiting time rises nonlinearly as utilization approaches one.
3. Apply Little's Law and Erlang-C staffing calculations.
4. Distinguish queue delay from service time and end-to-end process duration.
5. Evaluate staffing trade-offs without treating illustrative waiting penalties as observed customer damages.
6. Critique exponential-arrival/service assumptions and design a more credible empirical process model.

## Problem 1. Single-reviewer queue

A hypothetical intake stage receives 6 complete applications per business day. One reviewer completes an average of 8 applications per business day. Assume an M/M/1 FCFS queue.

1. Calculate utilization \(\rho\), the probability an arriving application must wait, expected number in the queue \(L_q\), and expected number in the system \(L\).
2. Calculate expected queue waiting time \(W_q\) and expected total time in the stage \(W\).
3. Verify Little's Law for both the queue and the full system.
4. Explain why the mean service time is not the same as mean total time in the stage.
5. Determine whether the queue has a steady state if arrivals rise to 8 applications per day while service capacity remains unchanged.

## Problem 2. Two parallel reviewers

A technical review stage receives 12 applications per business day. Each reviewer completes an average of 8 applications per business day. There are two identical reviewers and one FCFS queue.

1. Calculate offered load \(a=\lambda/\mu\), utilization \(\rho=\lambda/(c\mu)\), and the empty-system probability \(P_0\).
2. Use Erlang C to calculate the probability an arrival waits.
3. Calculate \(W_q\), \(W\), \(L_q\), and \(L\).
4. Explain why two reviewers with a combined average service capacity of 16 applications per day do not imply that every application waits zero time.
5. Verify Little's Law.

## Problem 3. Add a third reviewer

Keep the arrival rate and per-reviewer service rate from Problem 2, but increase staffing to three reviewers.

1. Recalculate utilization, \(P_0\), probability of waiting, \(W_q\), \(W\), \(L_q\), and \(L\).
2. Calculate the percentage reduction in expected queue wait relative to two reviewers.
3. Explain why the percentage reduction in queue wait can be much larger than the percentage increase in nominal service capacity.
4. Identify at least two reasons why a real utility might not realize the theoretical improvement from adding one reviewer.

## Problem 4. Staffing cost and the value of reduced delay

Assume each reviewer costs $500 per modeled business day. For illustration only, assume waiting imposes a cost of $300 per application-day in the queue.

1. Calculate total modeled daily cost for the two-reviewer and three-reviewer cases:
   \[
   C(c)=500c+300L_q(c).
   \]
2. Which staffing level has the lower modeled cost?
3. Derive the break-even waiting-cost coefficient at which two and three reviewers have equal modeled cost.
4. Explain why the $300 coefficient must not be described as an observed customer harm, a utility cost, or a regulator-approved value without evidence.
5. Explain how a decision-maker should present the result if the true waiting cost is unknown.

## Problem 5. Arrival-rate sensitivity and congestion

Return to two reviewers, each with service rate 8 applications per business day.

1. Recalculate the queue metrics if the arrival rate rises by 10%, from 12 to 13.2 applications per day.
2. Compare the increase in utilization with the increase in expected waiting time.
3. Explain the stability boundary and why planning at utilization near 100% is risky even if average capacity technically exceeds average arrivals.
4. Propose an arrival-rate stress test that captures seasonal application surges rather than assuming a constant Poisson rate.

## Problem 6. Multi-stage interconnection process

A hypothetical application moves through three stages: completeness screening, distribution engineering review, and agreement preparation. Each stage has different staffing and service-time characteristics. Applications may be returned for missing information, trigger a supplemental study, or be withdrawn.

1. Draw a process network showing the three stages, customer-pause state, rework loop, withdrawal, denial, and permission-to-operate.
2. Explain why three independent M/M/c queues may still be an inadequate representation.
3. Identify the event timestamps needed to decompose elapsed time into utility queue delay, active service, customer-controlled pause, external dependency, and rework.
4. Explain how stage-specific bottlenecks can be hidden by an aggregate end-to-end average.
5. Propose a discrete-event simulation design and a held-out validation plan.

## Problem 7. Empirical identification and measurement limits

The only available public data are annual EDC-level request counts and aggregate review-level mean days. There are no linked application identifiers or event timestamps.

1. State which queueing parameters can and cannot be estimated from these data.
2. Explain why dividing request counts by mean review days does not recover reviewer utilization or service capacity.
3. Specify a minimum event-history data schema for estimating arrival rates, service-time distributions, queue waits, rework, and right-censoring.
4. Explain how project-size mix, review-level assignment, and policy eligibility can confound EDC comparisons.
5. Define at least five model-risk checks before a queueing model informs staffing or policy.

## Problem 8. Computational verification

Run the [interconnection queueing lab](../../../projects/policy-analysis/interconnection-queueing/README.md).

1. Reproduce the analytical M/M/2 and M/M/3 metrics.
2. Compare the analytical results with the fixed-seed discrete-event simulation.
3. Explain finite-sample error, warm-up bias, and why reproducibility does not imply empirical validity.
4. Modify the simulation to test a peak-arrival regime or a heavier-tailed service-time distribution. State which M/M/c assumptions are violated and what new validation is needed.

## Submission

Submit the derivations, a compact staffing sensitivity table, a process map, and a 500–700 word methodological critique. Label every numerical example as synthetic. Do not infer actual PPL reviewer staffing, queue times, or service rates from this assignment.
