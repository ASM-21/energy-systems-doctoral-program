# Casebook: Pennsylvania Distribution DER Interconnection and PJM Wholesale Aggregation

**Research setting:** Pennsylvania / PJM  
**Verification date:** 2026-11-20  
**Purpose:** A primary-source case study connecting distribution interconnection, state regulation, utility operations, and wholesale market participation.

!!! warning "Public-source research only"
    Use only publicly available tariffs, orders, manuals, data, and publications. Do not use employer-confidential processes, internal system data, customer information, nonpublic project records, or work product. This casebook is an independent academic exercise, not an assessment of any employer's performance.

## Why this case matters

Two different institutional processes can affect a distributed resource:

1. The distribution-level process for physically connecting a DER to a utility distribution system.
2. The RTO/ISO wholesale-market process through which an aggregation may participate in energy, capacity, or ancillary-service markets.

They are related but not interchangeable. A DER's physical interconnection and distribution-system operating requirements do not disappear because the resource participates through an aggregator in a wholesale market.

## Primary-source packet

### A. PPL Electric Utilities — current Rule 12 tariff

**Current document:** PPL Electric Utilities Corporation, Supplement No. 2 to Electric Pa. P.U.C. No. 202, Rule 12 — Distributed Energy Resource Interconnection Service. Issued June 30, 2026; effective July 1, 2026.  
**Official PDF:** [Current Rule 12, Supplement No. 2 to Electric Pa. P.U.C. No. 202](https://www.pplelectric.com/site/-/media/PPLElectric/At-Your-Service/Docs/Current-Electric-Tariff/2026/August/Rule-12---Distributed-Energy-Resource-Interconnection-Service.pdf).

The current tariff states that Rule 12 applies to new DER interconnections effective January 3, 2026 and to inverter-based DER applications received on or after that date, subject to the specified rate schedules. It specifies IEEE 1547-2018 and UL 1741 Supplement B (or current utility certification requirements) for smart inverters and describes utility-owned DER Management Devices and DERMS functions.

**Version-control note:** Earlier 2026 PUC No. 201 tariff supplements remain useful for historical chronology, but the current Rule 12 reference located in this review is Supplement No. 2 to PUC No. 202, effective July 1, 2026. Do not label the April 2026 PUC No. 201 tariff as the current Rule 12 document.

### B. PPL public DER Management Program and implementation

- [PPL DER Management Program](https://www.pplelectric.com/site/More/For-Construction/DER-Management)
- [PPL REMSI page](https://www.pplelectric.com/site/More/About-Us/Electric-Rates-and-Rules/REMSI)

PPL describes its DERMS, utility-owned/maintained DER Management Devices, and communication with participating customer smart inverters. PPL's REMSI page states that implementation of its Second DER Management Program began January 5, 2026. Keep that implementation milestone separate from the Rule 12 tariff effective date of January 3, 2026.

### C. Pennsylvania PUC — Second DER Management Plan order

**Docket:** P-2024-3049223.  
**Order date:** December 3, 2025, as cited in the PUC Chairman's prepared testimony to the House Energy Committee on March 16, 2026.  
**Official public source located:** [Prepared Testimony of PUC Chairman Stephen M. DeFrank, March 16, 2026](https://www.palegis.us/house/committees/committee-archives/archive-file?file=2026_0572_0009_TSTMNY.pdf), page 3 and footnote 5.

The Chairman's testimony states that the Commission approved PPL's Second DER Management Plan at its November 20, 2025 public meeting, with the order entered December 3, 2025. It reports that the plan is projected to increase hosting capacity by up to 258 MW and that the Commission directed PPL to conduct an RFP for third-party aggregators.

**Evidence qualification:** The 258 MW figure is a projection reported in the Chairman's testimony, not an independently measured ex-post increase. The testimony is not a substitute for the controlling order. Retrieve the original order and docket record from the [PA PUC Document Search](https://www.puc.beta.pa.gov/search/document-search/) before making detailed claims about ordering paragraphs, cost recovery, evaluation requirements, reporting, or RFP terms.

### D. PPL hosting-capacity transparency and Pennsylvania HB 2429

PPL's [public interconnection FAQ](https://pplelectric.com/site/More/About-Us/Electric-Rates-and-Rules/Customer-Owned-Generation/frequently-asked-questions) states that it does not currently publish hosting-capacity maps or specific feeder hosting-capacity information. It says that limited site-specific information may be provided during pre-application, including substation name, feeder name and voltage, and line-distance information.

[House Bill 2429, Printer's No. 3230](https://www.palegis.us/legislation/bills/text/PDF/2025/0/HB2429/PN3230) was introduced and referred to the House Energy Committee on April 20, 2026. As introduced, it would require EDC hosting-capacity maps by July 1, 2027, updated every two months, with DER and new-load capacity, queued DER, distribution constraints, feeder-level granularity, planned upgrades, voltage levels, and limiting criteria. The version reviewed shows committee referral, not enactment. Treat this as proposed legislation unless an updated official bill history confirms otherwise.

See the [public-data feasibility assessment](data-feasibility.md) for the dataset inventory, research design, and unresolved evidence gaps.

### E. Pennsylvania PUC — proposed Chapter 57 rules for wholesale DER aggregations

**Docket:** L-2023-3044115.  
**Order:** Notice of Proposed Rulemaking adopted and entered December 18, 2025; published April 11, 2026 in 56 Pa.B. 1985.  
**Official sources:** [Pennsylvania Bulletin NOPR, Doc. No. 26-527](https://www.pacodeandbulletin.gov/secure/pabulletin/data/vol56/56-15/527.html); [IRRC Regulation No. 57-346 status page](https://www.irrc.state.pa.us/regulations/RegSrchRslts.cfm?ID=3496).

The proposed rules would create 52 Pa. Code §§ 57.261–57.266 for DER Aggregation Resources participating in PJM energy, capacity, and/or ancillary-services markets. The proposal is not final law. The IRRC page currently lists the regulation as proposed, with the public-comment period closed July 9, 2026, no final-form regulation received, and a final-form due date of July 9, 2028.

Key features of the proposal include:
- Net-metered customer-generators would generally be excluded from wholesale energy and capacity participation as DER Aggregator Resources, while ancillary-services participation could be allowed under the proposed conditions.
- A Component DER would require EDC approval to participate as part of a DER Aggregation Resource.
- An EDC would establish an electronic review process, complete review within 60 days, and explain denials.
- An EDC could propose application/review fees through a tariff filing.
- EDCs would provide DERA access to Component DER data with DER-operator consent, in a Commission-approved format.
- EDCs would retain distribution-safety and reliability operating/dispatch-override procedures.

**Jurisdictional boundary:** The NOPR expressly states that the Commission will address interconnection of Component DERs in another proceeding. Do not treat this proposed wholesale-aggregation rulemaking as the distribution interconnection rule or as a replacement for PPL Rule 12. Also distinguish the proposed 60-day DERA participation review from a site-specific interconnection study timeline.

The IRRC status page is important because it prevents a proposed rule from being represented as enacted. Recheck the regulation's status and any final-form publication before relying on these requirements.

### F. PJM — DER Aggregator Participation Model

**Document:** PJM, *DER Aggregator Participation Model: Full Model Design*, March 9, 2026.  
**Official public PDF:** [PJM model design presentation](https://www.pjm.com/-/media/DotCom/committees-groups/subcommittees/disrs/2026/20260309/20260309-item-05---updated-der-aggregator-participation-model---full-model-design---informational-only.pdf).

The presentation describes the PJM implementation timeline and the division between wholesale aggregation participation and distribution interconnection. It is an informational presentation, not itself a tariff. Verify current tariff/manual language and later stakeholder/FERC actions before relying on dates or requirements.

### G. FERC — Order No. 2222

- [FERC Order No. 2222 fact sheet](https://www.ferc.gov/media/ferc-order-no-2222-fact-sheet).
- [FERC Order No. 2222 explainer](https://www.ferc.gov/ferc-order-no-2222-explainer-facilitating-participation-electricity-markets-distributed-energy).
- [FERC Order No. 2222 original order, Docket RM18-9-000](https://www.ferc.gov/sites/default/files/2020-09/E-1_0.pdf).

The order establishes a framework for DER aggregations to participate in organized wholesale markets. The fact sheet and explainer are useful orientation materials, but the order and subsequent compliance orders are the controlling sources.

### H. FERC — Order No. 2023

- [FERC explainer on the generator interconnection final rule](https://ferc.gov/explainer-interconnection-final-rule).
- [Order No. 2023, Docket RM22-14-000](https://ferc.gov/sites/default/files/2023-07/20230728-3060.PDF).
- [FERC March 21, 2024 update on Order 2023-A and compliance filings](https://ferc.gov/news-events/news/ferc-affirms-generator-interconnection-rule-acts-compliance-filings).

Study this rule to understand transmission-provider generator interconnection reforms. Do not casually conflate its large- and small-generator transmission interconnection procedures with a state-regulated distribution DER process. Determine jurisdiction from the asset, transaction, tariff, and actual order language.

## Working artifacts

- [Versioned primary-source register](source-register.csv)
- [Institutional responsibility matrix](responsibility-matrix.csv)
- [Public-data feasibility assessment](data-feasibility.md)
- [PA PUC wholesale DER aggregation NOPR, L-2023-3044115](https://www.pacodeandbulletin.gov/secure/pabulletin/data/vol56/56-15/527.html)

The responsibility matrix is a research aid, not a legal opinion. Verify each assignment against the current controlling authority before relying on it.

## Research questions

1. How do distribution interconnection requirements and wholesale aggregation requirements interact for a DER in Pennsylvania?
2. Which entity is responsible for each decision: distribution utility, PJM, FERC, Pennsylvania PUC, aggregator, or resource owner?
3. What public evidence is available to evaluate interconnection process outcomes, operating constraints, and market participation?
4. What information must be exchanged between utility, aggregator, PJM, and retail regulatory authority?
5. Which aspects of the process are technically necessary, and which are institutional or economic design choices?
6. What performance evidence would be required to validate the projected hosting-capacity benefits of active DER management?

## Required analysis

### 1. Build an institutional responsibility matrix

For each process stage, identify the decision-maker, governing source, data required, affected parties, and escalation path. Include application, technical review, study, upgrades, approval, commissioning, DERMS/control requirements, aggregator registration, telemetry, dispatch, and settlement.

### 2. Build a rule crosswalk

Compare:
- PPL current Rule 12 tariff and REMSI;
- the December 3, 2025 PUC order in P-2024-3049223;
- the proposed Chapter 57 wholesale DER aggregation rules in L-2023-3044115 and their current IRRC status;
- applicable Pennsylvania PUC regulations and the wholesale DER participation rulemaking;
- PJM tariff and manuals for DER aggregations;
- FERC Order 2222 and relevant compliance orders;
- IEEE 1547 and applicable certification standards.

For each provision, identify its legal status, effective date, applicability, and relationship to the other documents.

### 3. Draw the process map

Show the physical interconnection pathway separately from wholesale market participation. Use explicit handoffs and mark where the two processes interact.

### 4. Conduct a data-feasibility review

Identify what is publicly observable: application counts, milestones, capacity, completion/withdrawal, upgrade costs, feeder location, operating limits, DER output, and market participation. For each field, document whether it is public, aggregated, incomplete, unavailable, or confidential. Do not assume data exist.

### 5. Evaluate economics and policy

Analyze how interconnection costs, upgrade allocation, operating requirements, and aggregation compensation affect project economics, ratepayers, utility planning, and system reliability. Distinguish costs caused by an individual project from shared infrastructure benefits and broader policy objectives.

## Deliverables

- 1,500–2,000 word primary-source institutional review.
- Versioned source matrix with exact sections and effective dates.
- Swimlane process diagram.
- Data-feasibility memo and data dictionary.
- 1,000–1,500 word policy brief.
- Research protocol stating whether an empirical study is feasible.

## Research integrity

The goal is to understand the public regulatory and technical framework. Do not attempt to reconstruct internal employer procedures from memory or include any nonpublic details. If public data are insufficient, reframe the project as a regulatory design and institutional analysis rather than implying empirical results.
