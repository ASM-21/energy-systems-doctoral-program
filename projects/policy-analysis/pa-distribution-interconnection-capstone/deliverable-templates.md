# Capstone Deliverable Templates

These templates are scaffolds. Replace every bracketed instruction with evidence, calculations, or an explicit statement that the information is unavailable. Do not convert a missing value into a guessed value.

## 1. Research paper structure (6,000–8,000 words)

### Title and abstract (200–250 words)
- Research question: [one sentence]
- Setting and period: [EDC geography, PUC reporting years]
- Data: [source, unit, sample size, reporting period]
- Methods: [descriptive audit, network model, prospective identification design]
- Main verified findings: [only supported results]
- Main limitation: [what the data cannot establish]

### 1. Introduction (600–800 words)
- Explain why distribution interconnection matters for DER deployment and infrastructure planning.
- Separate application volume, process performance, installed capacity, and operational hosting capacity.
- State the research question and contribution.
- List claims the study does not attempt to make.

### 2. Institutional and regulatory setting (700–900 words)
- Physical interconnection and utility study pathway.
- Pennsylvania PUC oversight and controlling tariff/rule versions.
- DERMS and distribution operating constraints.
- PJM wholesale aggregation and FERC jurisdiction.
- Customer economics and adoption incentives.
- Date-stamp every policy milestone and cite the controlling source.

### 3. Literature and conceptual framework (700–900 words)
- Interconnection queues and administrative process.
- Distribution hosting capacity and engineering constraints.
- Utility investment incentives and cost allocation.
- DER aggregation and wholesale-market participation.
- Empirical measurement and selection into application processes.
- Identify the specific gap this study can address with its data.

### 4. Data and measurement (700–900 words)
- Source, extraction, reporting period, and unit of observation.
- Data provenance and SHA-256 manifest.
- Variable definitions and units.
- Reconciliation checks and missingness.
- Distinguish request, review-level count, disposition, approval, PTO, and installed capacity.
- Explain why the panel is balanced or not and what that implies.

### 5. Descriptive results (700–900 words)
- Statewide totals and EDC shares.
- PPL rank and request-share changes.
- Request-count HHI and top-three share, with explicit non-market interpretation.
- Review-level composition and the 2025-only 500 kW split.
- No approval or completion rates without linked cohorts and denominators.

### 6. Empirical identification and data limitations (700–900 words)
- State why the existing 2023–2025 panel does not identify a 2026 treatment effect.
- Define the target estimand for a future application-level evaluation.
- Describe time origin, event definitions, competing risks, censoring, eligibility, and comparison group.
- Explain survival, Aalen-Johansen, multi-state, or quasi-experimental methods as appropriate.
- Discuss confounding, selection, policy timing, and concurrent interventions.

### 7. Engineering and optimization model (900–1,200 words)
- Define network topology, sign conventions, units, and approximation.
- Derive nodal balances, branch limits, and voltage equations.
- Define DER availability, curtailment, storage, and operating constraints.
- Formulate first-stage investment and scenario-specific recourse.
- Explain nonanticipativity, scenario probabilities or robust uncertainty set, and dual variables.
- Separate a screening model from an AC engineering study.

### 8. Computational results and robustness (500–800 words)
- Solver and software versions.
- Feasibility residuals, solver status, tests, and convergence diagnostics.
- Sensitivity to assumptions and uncertainty.
- Out-of-sample/stress scenarios.
- Failure modes and model-risk register.

### 9. Discussion and policy implications (500–700 words)
For each implication, label it:
- **Evidence-supported:** directly follows from validated public data or controlling legal text.
- **Provisional:** plausible interpretation requiring additional evidence.
- **Research recommendation:** a data or process improvement that could be tested.
- **Not established:** tempting conclusion that the analysis cannot support.

### 10. Conclusion (250–350 words)
- Answer the research question narrowly.
- State the contribution.
- Identify the most important missing data.
- Set out the next empirical and engineering validation step.

### Appendices
- Mathematical derivations.
- Data dictionary and provenance.
- Test report and solver diagnostics.
- Model-risk register.
- Reproducibility instructions.
- Source register and legal/tariff chronology.

## 2. Two-page policy brief structure

**Title:** [decision-relevant and neutral]

**Decision question:** [who needs to decide what?]

**What the evidence says (3 bullets):**
- [validated result with source and period]
- [validated result with unit]
- [important data limitation]

**What the evidence does not say (2–3 bullets):**
- [no causal effect]
- [no project-level processing probability]
- [no feeder hosting-capacity conclusion from aggregate counts]

**Options:**
1. [option, cost/benefit channel, evidence strength]
2. [option, cost/benefit channel, evidence strength]
3. [option, cost/benefit channel, evidence strength]

**Recommendation:** [specific action, responsible institution, timing, and evaluation plan]

**Evidence classification:** Label each statement as evidence-supported, provisional, or requiring new data.

**Data needed next:** [fields, owner, privacy protection, reporting cadence]

**Sources:** [primary tariff/order/data sources with access dates]

## 3. Oral defense questions

1. Why is an EDC-year panel the correct unit for the descriptive question, and what questions does it rule out?
2. What is the difference between a request count, a disposition, an approval, a PTO, and installed nameplate capacity?
3. Why is the request-count HHI not a retail-market HHI?
4. Why can an annual before/after comparison not identify the effect of a January 2026 rule change when the panel ends May 2025?
5. How would you assign policy exposure when the tariff document effective date, application applicability clause, DERMS implementation date, and later tariff supplement differ?
6. What is the difference between one-minus-Kaplan-Meier net risk and Aalen-Johansen cumulative incidence?
7. What assumptions underlie your distribution voltage approximation?
8. Why does a maximum-flow solution not prove electrical feasibility?
9. What decisions are first-stage and which are recourse? Where are the nonanticipativity constraints?
10. What does a binding branch-capacity dual mean in your optimization model, and why is it not automatically an LMP or tariff value?
11. Which uncertainty is stochastic, which is parameter uncertainty, and which is structural model uncertainty?
12. What single additional dataset would most improve the empirical design, and why?
13. Which result is most sensitive to a modeling assumption?
14. What result would cause you to abandon your preferred policy recommendation?
15. What is the strongest conclusion that remains valid if the application-level data never become available?

## 4. Final reproducibility checklist

- [ ] The raw public source is identified and its file hash is generated.
- [ ] All reporting dates and units are stated.
- [ ] Every aggregate total reconciles to the primary source.
- [ ] Every output can be regenerated from versioned code.
- [ ] Synthetic and empirical results are labeled separately.
- [ ] No confidential or identifying information is present.
- [ ] All policy dates are tied to the applicable controlling source.
- [ ] No causal effect is claimed without a defensible identification design.
- [ ] Engineering approximations are validated against an appropriate reference model before operational interpretation.
- [ ] The policy brief distinguishes evidence from proposals.
