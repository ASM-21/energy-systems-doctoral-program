# Event-History Data Requirements for Interconnection Queue Analysis

**Status:** Proposed research schema. No application-level utility dataset is included or assumed to be available.  
**Use:** Public data or data explicitly authorized for research. Never use employer-confidential, customer-identifiable, or nonpublic utility records without appropriate authorization.

## 1. Unit and event model

The fundamental unit is a de-identified application moving through a sequence of process states. One row per application is not sufficient because applications can have multiple review episodes, rework, customer pauses, and external dependencies.

Use three linked tables:

| Table | Grain | Required identifiers |
|---|---|---|
| Application | One row per submitted application | application_id |
| Process event | One row per timestamped event | event_id, application_id |
| Review episode | One row per review-stage episode | review_episode_id, application_id |

The application table should include EDC, pseudonymous process/feeder group, application cohort, project technology, nameplate capacity and AC/DC basis, export mode, storage pairing, initial review level, and governing tariff regime. Do not include customer names, street addresses, account numbers, or re-identification keys in the analytical extract.

## 2. Event vocabulary

At minimum, record the following events with a timestamp, source system, actor/process owner, and reason code:

- received;
- completeness review started;
- incomplete notice issued;
- applicant response received;
- complete;
- technical review queued;
- technical review started;
- technical review paused;
- technical review resumed;
- supplemental study requested/received;
- review-level transition;
- upgrade identified and estimate issued;
- approval, denial, or withdrawal;
- agreement issued/executed;
- construction started/completed;
- permission to operate;
- administrative closure.

Store both event time and record-entry time when backfilled data are possible. Preserve source timezone and normalize timestamps consistently. Store the applicable clock rule and whether weekends/holidays count. An elapsed calendar duration and a utility-business-day duration are different estimands.

## 3. Time decomposition

For each stage, derive separate intervals:

1. queue wait: queue-entry to service-start;
2. active service: service-start to service-complete, excluding recorded pauses;
3. customer pause: request-for-information to accepted response;
4. external dependency: referral or external study request to response;
5. rework: return-to-stage or repeat-study interval;
6. end-to-end elapsed time: selected origin to terminal event or observation cutoff.

Do not subtract intervals unless the event definitions are mutually exclusive and timestamps are complete. Preserve total calendar elapsed time as a separate measure. Report how missing or contradictory timestamps are handled.

## 4. Parameters and estimands

| Quantity | Required data | Estimation warning |
|---|---|---|
| Arrival rate | Arrival timestamps by stage and period | Test seasonality, overdispersion, and changing eligibility |
| Service rate | Active service intervals by stage and reviewer class | Mean duration alone does not establish exponential service |
| Queue wait | Queue entry and service start | Queue entry must be operationally defined |
| Utilization | Arrival/service capacity or observed busy time | Aggregate request count divided by aggregate mean days is invalid |
| Throughput | Completed service episodes per period | Distinguish applications, episodes, and rework |
| Abandonment/withdrawal | Withdrawal event and competing outcome | Treat as a competing event, not automatic independent censoring |
| Open-case censoring | Data cutoff and last known state | Keep unresolved applications in the risk set |

For an M/M/c approximation, estimate lambda and mu separately for a sufficiently homogeneous stage and reviewer pool. Test the assumptions before using Erlang-C. If arrival rates vary by time, service times are heavy-tailed, or reviewers have distinct skills, prefer a more flexible queueing network or discrete-event simulation.

## 5. Calibration and validation

1. Split cohorts chronologically into calibration and validation periods.
2. Estimate arrival and service processes using calibration data only.
3. Validate stage-level queue lengths, waiting-time distributions, throughput, and tail quantiles on held-out cohorts.
4. Compare simulation outputs with observed event histories, not only with aggregate mean duration.
5. Repeat under alternative arrival regimes, service distributions, and reviewer availability.
6. Report uncertainty intervals and parameter sensitivity.
7. Preserve a baseline model and a dated change log for every parameter update.

A model that reproduces an average duration but misses the upper tail, queue length, or withdrawal rate is not sufficiently validated for staffing decisions.

## 6. Privacy, legal scope, and institutional separation

- Use pseudonymous application and feeder identifiers.
- Keep any re-identification crosswalk with the data owner, outside the research environment.
- Record the tariff/rule version and application-specific eligibility basis; do not infer treatment from calendar year alone.
- Separate physical interconnection review from DERA wholesale-market participation review and from later operational dispatch.
- Public annual EDC totals cannot be used to infer individual queue waits, reviewer utilization, or application outcomes.
