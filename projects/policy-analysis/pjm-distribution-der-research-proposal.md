# Research Proposal: Distribution Infrastructure, Interconnection, and DER Deployment in Pennsylvania

**Status:** Revised proposal. PPL's 2015–2025 utility-level net-metered PV series is established; a Pennsylvania peer-utility extraction is underway. Public data do not currently support a causal analysis of PPL distribution interconnection timelines or feeder hosting capacity.  
**Program stage:** Year 1 integration project / potential Year 2 research paper.

## 1. Motivation

Distributed energy resources (DERs), electrification, and new large loads can create value while changing distribution-system planning and operating requirements. Interconnection processes, upgrade costs, utility investment incentives, export controls, and regulatory treatment can affect project timelines and deployment. These mechanisms connect power engineering, utility economics, regulation, and state/federal policy.

The project should avoid assuming that interconnection delays are caused by a single factor or that faster interconnection is always least-cost. Engineering constraints, study practices, cost allocation, queue management, equipment availability, and regulatory rules may interact.

## 2. Revised research question

**What can public data and regulatory records establish about net-metered PV adoption and distribution-level DER interconnection governance in Pennsylvania, and what additional evidence is needed to evaluate interconnection performance and DER orchestration?**

Subquestions:
- How has PPL's reported standard net-metered PV capacity changed by year and customer sector?
- How does PPL compare with other Pennsylvania utilities, if historical coverage, EIA utility identifiers, units, and field definitions can be reconciled?
- How do PPL Rule 12, its Second DER Management Plan, the DER Orchestration Plan commitments, and the behind-the-meter battery review shape distribution DER operating and interconnection requirements?
- How do fixed, scheduled, and dynamic export limits interact with PV, battery dispatch, and curtailment in transparent engineering models?
- What public data gaps prevent direct evaluation of application timelines, feeder constraints, upgrade costs, and project outcomes?

The original question about interconnection timelines and upgrade-cost outcomes remains a possible future research direction, not a currently supported empirical claim.

## 3. Research design: three connected tracks

### Track A — Descriptive DER adoption

Use EIA Form 861 annual utility-level Net Metering schedule data. The PPL series covers 2015–2025, with one utility-level row per year (EIA utility ID 14715). The comparable AC-basis standard PV capacity series is 92.915 MW in 2016 and 505.746 MW in 2025. The 2015 capacity basis is not separately reported and is excluded from AC-basis growth calculations. PV count labels change from Customers to Installations in 2021; virtual PV capacity changes from a combined field to size bands in 2023.

A Pennsylvania-wide raw utility-row extraction is now being added to assess peer coverage. Those rows are not yet harmonized. Do not calculate cross-utility growth or build a panel until utility IDs, mergers, service territories, schedule definitions, and AC/DC basis are checked.

This track is descriptive. It does not estimate the effect of the Second DER Management Plan, Rule 12, or the DER Orchestration Plan.

### Track B — Institutional and regulatory case study

Use primary sources to map:
- PPL physical distribution interconnection under Rule 12;
- PPL's Second DER Management Plan and DERMS/device framework;
- the DER Orchestration Plan stakeholder commitment in the rate-case settlement;
- the BTM non-exporting battery review commitment and its public-record status;
- the PUC's proposed Chapter 57 rules for wholesale DER aggregator participation;
- PJM wholesale DERA registration and FERC Order 2222 jurisdiction.

Maintain a strict distinction between physical distribution interconnection, utility approval for a component DER to join a wholesale aggregation, and PJM market registration. Treat proposed rules and informational presentations as such, not as final tariff requirements.

### Track C — Engineering and operational mechanisms

Use transparent synthetic models to demonstrate mechanisms:
- radial feeder DER hosting-capacity screening;
- IEEE 13-node OpenDSS nonlinear unbalanced benchmark;
- flexible interconnection LP comparing fixed, scheduled, dynamic export envelopes, and a hypothetical firm upgrade;
- BTM battery dispatch and non-export constraints.

These models demonstrate methods and trade-offs. They are not PPL feeder models, do not use employer data, and do not establish utility-specific hosting capacity or interconnection feasibility.

## 4. Data inventory and feasibility

- **EIA Form 861:** historical PPL net-metering utility-year series and sector capacity fields; a Pennsylvania peer-utility panel is under coverage/schema audit.
- **Pennsylvania PUC:** public orders, dockets, tariffs, settlement filings, and proposed rulemakings.
- **PPL Electric:** current tariff, technical policies, DER Management Program and REMSI pages.
- **PJM/FERC:** wholesale DER aggregation and transmission interconnection sources, carefully separated from distribution interconnection.
- **DOE/NREL/LBNL and CPUC:** technical frameworks and external comparators for dynamic operating envelopes, flexible interconnection, hosting capacity, and DER orchestration.

The current public EIA-861 series does not provide feeder-level voltage/loading, interconnection application milestones, project-level upgrade costs, queue withdrawals, curtailment events, or protection constraints. Do not infer those outcomes from utility-level net-metered PV capacity.

## 5. Method sequence

1. Maintain the Pennsylvania regulatory source register and institutional responsibility map.
2. Complete the PPL EIA-861 descriptive series and publish the data dictionary, archive hashes, and source-row provenance.
3. Audit all Pennsylvania utility rows for peer coverage, utility ID continuity, and schema comparability.
4. If the peer panel passes the audit, produce a descriptive utility-year panel and compare adoption trends with explicit caveats.
5. Develop the technical models and sensitivity analysis for export envelopes, battery dispatch, and feeder constraints.
6. Integrate engineering mechanisms with the regulatory case study.
7. Pursue causal analysis only if a credible treatment/control design and comparable outcome data become available.
8. Publish a policy brief with options, trade-offs, and a limitations statement.

Potential descriptive statistics include annual reported capacity, year-over-year changes, compound growth over comparable AC-basis years, customer-sector shares, and cross-utility distributions if the panel is validated. Avoid causal language.

## 6. Deliverables

- Research protocol and revised question statement.
- Annotated literature review and regulatory source matrix.
- Reproducible EIA-861 extraction, harmonization, data dictionary, and data snapshot.
- Pennsylvania peer-utility coverage report and, if justified, harmonized utility-year panel.
- Engineering model repository with tests and limitations.
- Technical paper (target 4,000–6,000 words if evidence permits).
- Policy brief (1,000–1,500 words).
- Presentation and explicit research-integrity statement.

## 7. Decision gates

- **Peer panel gate:** proceed only if utility identifiers, respondent coverage, field definitions, units, capacity basis, and service territories can be reconciled. Otherwise retain the PPL descriptive series and case study.
- **Interconnection outcome gate:** proceed with timeline/upgrade-cost analysis only if project-level milestones and costs are publicly available or can be lawfully obtained with appropriate safeguards. Do not substitute net-metered PV capacity for interconnection outcomes.
- **Causal gate:** no causal estimate without a defensible counterfactual, treatment timing, comparable outcomes, and explicit treatment of selection, censoring, missingness, and confounding.

## 8. Research integrity and confidentiality

Use public information only unless written authorization and appropriate safeguards permit otherwise. Never include nonpublic employer data, customer records, critical infrastructure details, or sensitive operational information in this public repository. Do not use PPL internal feeder models, queue data, customer information, or operational telemetry in the public project.

## 9. Current primary-source starting point (verified 2026-11-20)

### Pennsylvania casebook and empirical data

- [Pennsylvania DER interconnection and PJM wholesale aggregation casebook](../../research/casebooks/pa-der-interconnection/README.md).
- [PPL net-metered PV capacity trend, 2015–2025](../../research/casebooks/pa-der-interconnection/eia861-ppl-net-metering-trend.md).
- [Committed harmonized EIA-861 PPL dataset](../../research/data-pipelines/eia861/data/ppl_net_metering_harmonized.csv).
- [EIA-861 extraction and harmonization pipeline](../../research/data-pipelines/eia861/README.md).

### PPL tariffs and DER policy

PPL's current Rule 12 is Supplement No. 2 to Electric Pa. P.U.C. No. 202, issued June 30, 2026 and effective July 1, 2026. It retains the January 3, 2026 DERIS applicability date and expressly includes storage resources in the DER definition. Use the current tariff, not an older supplement, for current compliance claims. [Official current Rule 12 PDF](https://www.pplelectric.com/site/-/media/PPLElectric/At-Your-Service/Docs/Current-Electric-Tariff/2026/August/Rule-12---Distributed-Energy-Resource-Interconnection-Service.pdf).

PPL's [DER Management Program page](https://www.pplelectric.com/site/More/For-Construction/DER-Management) describes the Second DER Management Program and the utility's stated DERMS/device approach. PPL's [REMSI page](https://www.pplelectric.com/site/More/About-Us/Electric-Rates-and-Rules/REMSI) states implementation began January 5, 2026. Keep the tariff effective date distinct from the utility's stated implementation date.

PPL's public [Energy Storage Interconnection Policy, Revision 0](https://www.pplelectric.com/site/-/media/ppl-jss-app/assets/Home/More/About-Us/Electric-rates-and-rules/Point-of-contact-requirements/PPL-Electric-Energy-Storage-Policy-Rev-0.ashx) is effective February 1, 2023. It should be read alongside the current Rule 12 tariff; the public revision status warrants follow-up.

### DER orchestration and wholesale participation

The rate-case settlement in R-2025-3057164 contains operative body paragraph 119 on a stakeholder working group before the DER Orchestration Plan filing and paragraph 124 on review of BTM non-exporting battery projects currently under interconnection review within 120 days of the June 11, 2026 PUC order. The resulting October 9, 2026 date is a deadline calculation. Appendix D cross-references these commitments one paragraph earlier; the casebook records the discrepancy and uses the operative body numbering. No separate public plan or review report was located in indexed sources as of November 20, 2026; this is not proof of non-filing.

PJM's March 9, 2026 *DER Aggregator Participation Model: Full Model Design* presentation distinguishes the state/utility distribution interconnection process from PJM wholesale aggregation participation and describes an implementation timeline culminating in February 1, 2028 full model go-live. This is an informational implementation presentation; verify current tariff, manual, and FERC orders before treating a milestone as binding. [Official PJM presentation](https://www.pjm.com/-/media/DotCom/committees-groups/subcommittees/disrs/2026/20260309/20260309-item-05---updated-der-aggregator-participation-model---full-model-design---informational-only.pdf).

The PUC's proposed Chapter 57 DER Aggregation Resources rulemaking (L-2023-3044115) remains proposed, not final law. The casebook records the IRRC status and explains why this wholesale aggregation framework must not be confused with physical distribution interconnection.

### Technical comparators

- U.S. Department of Energy, [Flexible DER & EV Connections (July 2024)](https://www.energy.gov/sites/default/files/2024-08/Flexible%20DER%20%20EV%20Connections%20July%202024.pdf), for dynamic operating envelopes and customer-/utility-controlled flexible connections.
- California Public Utilities Commission, [Resolution E-5296 (March 21, 2024)](https://docs.cpuc.ca.gov/PublishedDocs/Published/G000/M527/K981/527981713.PDF), for Limited Generation Profiles. A pre-agreed schedule is not the same as a continuously recalculated dynamic operating envelope.
- FERC Order No. 2222 provides the federal wholesale-market framework for DER aggregations. FERC Order No. 2023 concerns transmission-provider generator interconnection procedures and should not be casually conflated with state-regulated distribution DER interconnection.

The project now has a credible descriptive and institutional foundation. It does not yet have public project-level evidence to estimate PPL interconnection timelines, upgrade costs, or causal effects of the utility's DER programs.
