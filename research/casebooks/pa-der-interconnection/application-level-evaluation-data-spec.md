# Application-Level Evaluation Data Specification

**Purpose:** Define the minimum data structure needed to evaluate distribution DER interconnection outcomes without conflating requests, approvals, installations, and operational performance.  
**Status:** Research design specification; no application-level dataset is currently available in this casebook.  
**Privacy:** Use de-identified records and public or expressly authorized data only. This specification does not authorize collection of confidential utility, customer, or employer information.

## 1. Unit of observation and relational structure

A single flat row per application is insufficient when an application changes review level, pauses for customer action, receives multiple study requests, or progresses through several milestones. Use a relational event-history structure:

| Table | Primary key | Grain | Purpose |
|---|---|---|---|
| application | application_id | One row per submitted application | Stable project characteristics, eligibility, EDC and feeder assignment |
| application_event | event_id | One row per dated process event | Completeness, study, approval, denial, withdrawal, agreement, construction, PTO |
| review_episode | review_episode_id | One row per review episode | Review level, start/end, screen results, supplemental study |
| policy_regime | regime_id | One row per rule/tariff version and eligibility definition | Controlling rule text, dates, scope, and application eligibility |
| feeder_snapshot | feeder_snapshot_id | One row per feeder and effective date | Public or authorized engineering characteristics, with provenance |
| upgrade | upgrade_id | One row per identified network upgrade | Scope, cost estimate, responsible party, status, completion |

Never use customer name, street address, account number, or personally identifying details as analysis keys. Keep any re-identification crosswalk outside the research environment under the data owner's controls.

## 2. Application table: minimum fields

| Field | Type | Definition / validation |
|---|---|---|
| application_id | string | Random stable identifier; unique and non-identifying |
| edc_id | category | EDC service territory; crosswalk version documented |
| feeder_id | pseudonymous category | Stable within the data provider's environment; no public map disclosure implied |
| submitted_date | date | First received date; cannot follow final disposition |
| complete_date | date | Date all required information was accepted; nullable while incomplete |
| technology | category | PV, storage, hybrid, other; controlled vocabulary |
| inverter_based | boolean | Definition and certification rule version recorded |
| nameplate_kw | numeric | AC/DC basis explicitly stated; positive |
| export_mode | category | Export, non-export, limited export, dynamic/flexible export |
| storage_kw | numeric nullable | Rated active power; unit and sign convention specified |
| storage_kwh | numeric nullable | Energy capacity; unit and usable/gross basis specified |
| review_level_initial | category | Initial review level and governing rule version |
| customer_action_required | boolean | Whether an applicant action/pause was recorded |
| tariff_regime_id | foreign key | Rule version that legally applies to this application |
| policy_eligibility_basis | category | Explicit reason the application is or is not covered |
| project_cohort | category | Defined cohort, not a post-hoc label |

Do not impute missing complete dates from approval dates. Do not use an application date as the treatment assignment date unless the controlling rule's applicability clause establishes that criterion.

## 3. Event-history table

Each event has a unique event ID, application ID, event timestamp, event type, source system, and a controlled reason code. At minimum, record:

- application received;
- completeness review started and completed;
- application deemed complete;
- initial technical screen started and completed;
- supplemental study requested and received;
- review-level transition;
- upgrade identified and estimate issued;
- approval, denial, or withdrawal;
- interconnection agreement executed;
- construction started and completed;
- permission to operate (PTO);
- application closed for another documented reason.

Store both event timestamp and effective timestamp if records can be entered retrospectively. Preserve original timezone and normalize consistently. Store event source and audit status. Distinguish applicant-pause days, utility-processing days, and calendar days. A process can have multiple episodes; one duration should not erase the underlying event sequence.

## 4. Outcomes and estimands

Pre-specify distinct outcomes rather than a single ambiguous "interconnection time":

1. **Completeness duration:** submitted to complete.
2. **First-disposition duration:** complete to approval, denial, or withdrawal.
3. **Agreement duration:** approval to executed agreement.
4. **Construction/PTO duration:** agreement or approval to PTO, with origin explicitly stated.
5. **End-to-end duration:** submitted to PTO, including incomplete and applicant-controlled intervals.

Potential estimands:

- Restricted mean time to first disposition by a fixed horizon, with competing events explicitly defined.
- Cumulative incidence of approval by 90/180/365 days, with withdrawal and denial as competing outcomes.
- Probability of PTO by a fixed horizon among a clearly defined eligible cohort.
- Upgrade incidence and cost conditional on project and feeder characteristics.

An approval is not a completed installation. PTO is not proof of unconstrained dispatch or sustained export. Do not combine them.

## 5. Target-trial style protocol for a policy evaluation

Before selecting a regression method, specify the hypothetical trial:

| Element | Required definition |
|---|---|
| Eligibility | DER technology, size, export mode, EDC, feeder, application status, and controlling rule scope |
| Treatment | Exposure to the verified process/tariff regime, determined by the actual applicability clause |
| Assignment | Observational assignment; describe why applications enter each regime |
| Time zero | A common date such as complete-application acceptance, if this occurs before the relevant process exposure and is defined consistently |
| Follow-up | Fixed horizon; specify administrative end date |
| Outcome | One pre-specified event or estimand; distinguish competing terminal events |
| Censoring | Administrative censoring and loss-to-follow-up rules; assess informative censoring |
| Contrast | Risk difference, cumulative incidence difference, restricted mean time difference, or another pre-specified contrast |
| Analysis | Survival/competing-risks or quasi-experimental method consistent with treatment assignment |
| Sensitivity | Alternative time origins, cohort definitions, censoring assumptions, and policy dates |

**Important:** The PPL Rule 12 applicability date, the tariff document's effective date, the DER Management Program implementation milestone, and any later tariff supplement are not interchangeable. Each application needs a legally reviewed regime assignment based on the controlling document and the relevant clause. The January 3, 2026 applicability and January 5, 2026 implementation milestones are separate events in the existing casebook chronology. A later tariff supplement may restate or amend terms; it must not silently reset the treatment date for earlier applications.

## 6. Causal structure and confounding

A minimum causal diagram should consider:

- project size and technology affect review level, study burden, upgrade likelihood, and outcome time;
- feeder condition and available capacity affect study requirements, upgrade cost, and outcome time;
- applicant experience/resources affect application completeness, response time, withdrawal, and completion;
- seasonal workload and application volume affect utility queue times;
- policy regime affects process steps, information requirements, operating controls, and potentially outcomes;
- utility investment and DERMS availability may change concurrently with the policy regime;
- customer incentives, interest rates, and equipment costs affect which projects apply and which proceed.

This creates selection and confounding. A before/after comparison may combine policy effects with changes in project composition, feeder conditions, workload, applicant behavior, and macroeconomic conditions. EDC fixed effects do not remove time-varying confounding or changing selection.

## 7. Statistical method selection

- **Kaplan-Meier:** useful for a single event with right censoring under an independent-censoring assumption. Treating withdrawals/denials as censored estimates a net-risk quantity, not observed approval incidence.
- **Aalen-Johansen:** estimates cause-specific cumulative incidence when approval, withdrawal, and denial are mutually exclusive competing events.
- **Cause-specific hazards:** useful for modeling instantaneous event rates, but do not directly equal cumulative incidence.
- **Fine-Gray subdistribution hazards:** can model cumulative-incidence associations, but requires careful interpretation and proportionality diagnostics.
- **Multi-state models:** appropriate when the sequence from submission to completeness, study, approval, agreement, construction, and PTO is central.
- **Difference-in-differences/event study:** only if treatment timing and comparison groups are defensible, pre-treatment outcome trends are available, measurement is stable, and concurrent interventions are addressed.

Cluster uncertainty at the level where treatment or process shocks occur (often EDC, feeder, or policy unit), while recognizing that a small number of clusters makes conventional asymptotics unreliable. Consider randomization inference or small-cluster corrections where appropriate, but do not mistake them for a solution to confounding.

## 8. Data quality and disclosure checks

- Reconcile event sequences; flag impossible date orderings rather than silently correcting them.
- Quantify missingness by EDC, review level, policy regime, and calendar period.
- Test duplicate application IDs and duplicated event IDs.
- Record left truncation, delayed entry, and administrative censoring.
- Audit changes in event definitions and source systems.
- Report counts suppressed for privacy and any aggregation rules.
- Do not publish feeder identifiers or small-cell results that could reveal customer/project details.
- Retain a data dictionary, extraction code, source hash, and versioned transformation log.

## 9. Link to existing teaching resources

- [PA DER interconnection capstone](../../../projects/policy-analysis/pa-distribution-interconnection-capstone/README.md): aggregate PUC baseline and follow-on research design.
- [Competing-risks survival lab](../../../projects/econometrics/competing-risks-survival/README.md): synthetic Kaplan-Meier and Aalen-Johansen implementation.
- [PA PUC interconnection report](puc-interconnection-report-2023-2025.md): source definitions, peer counts, and measurement caveats.
- [Data feasibility memo](data-feasibility.md): available public data and unresolved limitations.

This specification is a research design, not a claim that these application-level data are public or currently available.
