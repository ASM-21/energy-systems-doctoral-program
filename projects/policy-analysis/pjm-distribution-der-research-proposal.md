# Research Proposal: Distribution Infrastructure, Interconnection, and DER Deployment in Pennsylvania

**Status:** Initial proposal; research question and data feasibility must be refined before empirical work.  
**Program stage:** Year 1 integration project / potential Year 2 research paper.

## 1. Motivation

Distributed energy resources (DERs), electrification, and new large loads can create value while also changing distribution-system planning requirements. Interconnection processes, upgrade costs, utility investment incentives, and regulatory treatment can affect project timelines and deployment. These mechanisms connect power engineering, utility economics, regulation, and state/federal policy.

The project should avoid assuming that interconnection delays are caused by a single factor or that faster interconnection is always least-cost. Engineering constraints, study practices, cost allocation, queue management, equipment availability, and regulatory rules may interact.

## 2. Candidate research questions

Primary candidate:
**What observable factors are associated with interconnection timelines and upgrade-cost outcomes for distributed energy resources in Pennsylvania, and what can public data support about the mechanisms?**

Potential subquestions:
- Are project type, size, location, or application cohort associated with timeline differences?
- What information is publicly available on study milestones, withdrawals, upgrades, and project outcomes?
- How do utility tariffs, state policy, and technical screening requirements differ across relevant jurisdictions?
- What are the limits of public queue data for identifying causal effects?

Do not promise a causal estimate until the data and identification strategy justify one.

## 3. Research design

Begin with an institutional and data-feasibility study. Map the applicable interconnection rules and identify public datasets. Construct a data dictionary before analysis. Define the unit of observation (application, project, feeder, utility-year, or another defensible unit) and the outcome precisely.

Potential outcomes include elapsed days between documented milestones, project completion/withdrawal, upgrade-cost categories, or capacity reaching operation. Do not combine unlike milestone definitions across utilities without harmonization.

## 4. Data inventory to investigate

- Pennsylvania Public Utility Commission orders, dockets, and public reports.
- Utility interconnection tariffs, manuals, hosting-capacity maps, and public queue data where available.
- PJM interconnection queue and relevant transmission data, while carefully distinguishing wholesale transmission interconnection from distribution-level processes.
- EIA state and utility-level energy data for context.
- NREL, LBNL, and DOE studies for prior evidence and methods.
- Census and other public geographic/demographic data only where justified and appropriately aggregated.

Public availability, completeness, definitions, and licensing must be verified. Do not infer that a utility dataset exists because a report refers to it.

## 5. Method sequence

1. Institutional map and legal/regulatory source review.
2. Literature review on interconnection queues, distribution planning, DER adoption, and utility incentives.
3. Data inventory and feasibility memo.
4. Descriptive statistics and process mapping.
5. Engineering/economic interpretation of observed patterns.
6. If data support it, estimate appropriate statistical models; explicitly address selection, censoring, missingness, cohort effects, and confounding.
7. Sensitivity checks and limitations.
8. Policy brief with options and trade-offs.

## 6. Deliverables

- Research protocol and question statement.
- Literature review with annotated bibliography.
- Regulatory/tariff source matrix.
- Dataset inventory and data dictionary.
- Reproducible analysis code and tests.
- Technical paper (target 4,000–6,000 words if data permit).
- Policy brief (1,000–1,500 words).
- Presentation and limitations statement.

## 7. Decision gate

Proceed to empirical analysis only if a documented data audit demonstrates sufficient coverage, comparable definitions, and a credible analysis strategy. Otherwise, produce a rigorous institutional/engineering case study rather than force an invalid regression.

## 8. Research integrity and confidentiality

Use public information only unless written authorization and appropriate safeguards permit otherwise. Never include nonpublic employer data, customer records, critical infrastructure details, or sensitive operational information in this public repository.

## 9. Current primary-source starting point (verified 2026-11-20)

A focused Pennsylvania/PJM casebook now provides the first source packet: [Pennsylvania DER interconnection and PJM wholesale aggregation](../../research/casebooks/pa-der-interconnection/README.md).

The public PPL Electric tariff, Electric Pa. P.U.C. No. 201, Supplement No. 414 (issued March 31, 2026; effective April 10, 2026), contains Rule 12 on DER Interconnection Service at pages 14C.1–14C.3. Rule 12 states an effective date of January 3, 2026 for the new DER interconnection service provisions and describes smart-inverter, DER Management Device, and DERMS-related requirements. Use the exact tariff text and verify later supplements before making any current compliance claim. [Official tariff PDF](https://www.pplelectric.com/site/-/media/PPLElectric/At-Your-Service/Docs/Current-Electric-Tariff/2026/Apr/master414-posted-2026-4-10.pdf).

PJM's March 9, 2026 *DER Aggregator Participation Model: Full Model Design* presentation distinguishes the state/utility distribution interconnection process from PJM wholesale aggregation participation and describes an implementation timeline culminating in February 1, 2028 full model go-live. This is an informational implementation presentation; verify current tariff, manual, and FERC orders before treating a milestone as binding. [Official PJM presentation](https://www.pjm.com/-/media/DotCom/committees-groups/subcommittees/disrs/2026/20260309/20260309-item-05---updated-der-aggregator-participation-model---full-model-design---informational-only.pdf).

FERC Order No. 2222 and its compliance orders provide the federal wholesale-market framework for DER aggregations. FERC Order No. 2023 concerns reforms to transmission-provider generator interconnection procedures and should not be casually conflated with state-regulated distribution DER interconnection. See the casebook for the source crosswalk and required analysis.

This addition narrows the first research milestone to a public-source institutional and rule-design study. It does not assume access to utility-internal application, feeder, operating, or customer data. The empirical question remains conditional on a documented data-feasibility review.


A more direct source for the operative Rule 12 language is PPL's [Rule 12 tariff PDF, Supplement No. 411](https://www.pplelectric.com/site/-/media/PPLElectric/At-Your-Service/Docs/Current-Electric-Tariff/rule12.pdf), issued January 2, 2026 and effective January 3, 2026. PPL's [DER Management Program page](https://www.pplelectric.com/site/More/For-Construction/DER-Management) describes the Second DER Management Program and the utility's stated DERMS/device approach. PPL's [REMSI page](https://www.pplelectric.com/site/More/About-Us/Electric-Rates-and-Rules/REMSI) states implementation began January 5, 2026. Keep the tariff effective date distinct from the utility's stated implementation date. The casebook source register records both and identifies the 2024 Pennsylvania Bulletin notice as a petition notice, not a final approval order.
