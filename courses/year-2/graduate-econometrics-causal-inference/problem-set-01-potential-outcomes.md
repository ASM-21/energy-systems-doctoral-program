# Problem Set 1: Potential Outcomes, Selection, and Causal Graphs

**Level:** Graduate econometrics / doctoral preparation  
**Suggested effort:** 2–3 hours  
**Prerequisites:** OLS, conditional expectation, probability, basic regression  
**Application:** DER interconnection process evaluation

## Problem 1. Potential outcomes and estimands

Let \(D_i\in\{0,1\}\) denote whether application i is exposed to an expedited interconnection review process. Let \(Y_i(1)\) and \(Y_i(0)\) be potential outcomes, where Y is an indicator for receiving a first disposition within 90 days of a complete application.

1. Define the individual treatment effect, average treatment effect (ATE), average treatment effect on the treated (ATT), and average treatment effect on the untreated (ATU).
2. State the fundamental problem of causal inference.
3. Explain why the observed difference \(E[Y\mid D=1]-E[Y\mid D=0]\) is not generally the ATE.
4. Give one policy question for which ATT is more relevant than ATE and one for which ATE is more relevant.

## Problem 2. Decomposing selection bias

Suppose the population potential-outcome means are:

| Group | \(E[Y(1)\mid D]\) | \(E[Y(0)\mid D]\) |
|---|---:|---:|
| Treated applicants (\(D=1\)) | 0.72 | 0.60 |
| Untreated applicants (\(D=0\)) | 0.66 | 0.56 |

Assume half the population is treated.

1. Calculate ATT and ATU.
2. Calculate ATE.
3. Calculate the observed difference in means.
4. Decompose the observed difference into ATT plus selection bias, using the untreated potential outcome means.
5. Explain why random assignment would remove selection bias in expectation but would not make treatment effects homogeneous.

## Problem 3. Conditional independence and regression adjustment

Let X contain pre-treatment project characteristics: technology, nameplate capacity, export mode, review level eligibility, feeder congestion proxy, and applicant experience.

1. State the conditional independence assumption required for identification of the ATE by adjustment on X.
2. State the overlap/positivity condition.
3. Write the g-formula for the ATE.
4. Explain why adding every available variable to a regression is not a valid substitute for a causal graph and a timing argument.
5. Explain why a post-treatment variable such as an upgrade recommendation may be a mediator or collider and should not automatically be controlled for.

## Problem 4. Directed acyclic graph

Consider the following variables:

- R: expedited review policy exposure;
- S: project size and technology;
- F: pre-existing feeder constraint;
- A: applicant resources/experience;
- C: application completeness;
- U: utility workload;
- Y: time to first disposition;
- W: withdrawal before disposition.

1. Draw a DAG with plausible arrows among these variables.
2. Identify confounding paths between R and Y.
3. Identify at least one possible mediator and one possible collider.
4. Explain why conditioning on withdrawal W or restricting to completed applications may induce selection bias.
5. Explain why an EDC fixed effect cannot remove time-varying workload or project-composition confounding.

## Problem 5. Randomized pilot design

A regulator considers offering optional application-assistance support to eligible small DER applicants. The support is intended to improve application completeness, not to change engineering review standards.

1. Propose a randomized encouragement design that preserves equal access to the standard interconnection process.
2. Define the intention-to-treat estimand.
3. Explain how treatment-on-the-treated differs from ITT and what assumptions are required for an instrumental-variable interpretation of randomized encouragement.
4. State how you would handle noncompliance, withdrawals, and applications still open at the follow-up date.
5. Identify ethical, operational, and external-validity constraints.

## Problem 6. Interference and SUTVA

Two DER applications connect to the same constrained feeder. Approval or export from one project can affect the available hosting capacity and study outcome for the other.

1. Explain which part of SUTVA is violated.
2. Define an exposure mapping that could represent feeder-level DER penetration or queue congestion.
3. Explain why application-level randomization may be inappropriate when projects share a feeder.
4. Propose a cluster-randomized or partial-interference design, and state what the treatment effect would mean.

## Problem 7. Research memo

Write a 400–600 word memo answering:

“Can the Pennsylvania PUC's 2023–2025 aggregate EDC interconnection panel identify the causal effect of PPL's 2026 Rule 12 / DER Management changes?”

Your memo must define the proposed treatment, outcome, unit, timing, and estimand. It must state what the panel can describe, what it cannot identify, and the minimum additional data needed for a credible evaluation.

## Submission standard

Write the estimand and assignment mechanism before selecting an estimator. Distinguish treatment effects, selection bias, and measurement error. A regression table without an identification argument is incomplete.
