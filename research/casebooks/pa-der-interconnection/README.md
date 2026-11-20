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

### A. PPL Electric Utilities — current public tariff

**Document:** PPL Electric Utilities Corporation, General Tariff, Electric Pa. P.U.C. No. 201, Supplement No. 414, issued March 31, 2026, effective April 10, 2026.  
**Relevant section:** Rule 12, Distributed Energy Resource (DER) Interconnection Service, pages 14C.1–14C.3.  
**Official PDF:** [PPL tariff PDF](https://www.pplelectric.com/site/-/media/PPLElectric/At-Your-Service/Docs/Current-Electric-Tariff/2026/Apr/master414-posted-2026-4-10.pdf).

Initial observations from the public tariff:
- Rule 12 states that DER Interconnection Service applies to new DER interconnections with the distribution system effective January 3, 2026.
- The rule defines its applicability for inverter-based DER applications received on or after that date and identifies covered rate schedules.
- The device provisions reference IEEE 1547-2018 and UL 1741 Supplement B (or current utility certification requirements).
- The tariff describes a utility DER Management Device and the use of the utility's DERMS to monitor and manage inverter grid-support functions.

These are summaries. Read the exact current tariff language and subsequent supplements before making a compliance claim. The tariff PDF is versioned; do not cite an older cached version as current.

### B. PJM — DER Aggregator Participation Model

**Document:** PJM, *DER Aggregator Participation Model: Full Model Design*, March 9, 2026.  
**Official public PDF:** [PJM model design presentation](https://www.pjm.com/-/media/DotCom/committees-groups/subcommittees/disrs/2026/20260309/20260309-item-05---updated-der-aggregator-participation-model---full-model-design---informational-only.pdf).

The presentation describes the PJM implementation timeline and the division between wholesale aggregation participation and distribution interconnection. It states that resources participating solely through the DER Aggregator model use the applicable state interconnection process rather than entering the PJM generation interconnection queue. The presentation identifies February 1, 2028 as the full model go-live date and includes interim capacity-market milestones. Treat the presentation as an implementation briefing; verify current tariff/manual language and later stakeholder/FERC actions before relying on dates or requirements.

### C. FERC — Order No. 2222

- [FERC Order No. 2222 fact sheet](https://www.ferc.gov/media/ferc-order-no-2222-fact-sheet).
- [FERC Order No. 2222 explainer](https://www.ferc.gov/ferc-order-no-2222-explainer-facilitating-participation-electricity-markets-distributed-energy).
- [FERC Order No. 2222 original order, Docket RM18-9-000](https://www.ferc.gov/sites/default/files/2020-09/E-1_0.pdf).

The order establishes a framework for DER aggregations to participate in organized wholesale markets. The fact sheet and explainer are useful orientation materials, but the order and subsequent compliance orders are the controlling sources.

### D. FERC — Order No. 2023

- [FERC explainer on the generator interconnection final rule](https://ferc.gov/explainer-interconnection-final-rule).
- [Order No. 2023, Docket RM22-14-000](https://ferc.gov/sites/default/files/2023-07/20230728-3060.PDF).
- [FERC March 21, 2024 update on Order 2023-A and compliance filings](https://ferc.gov/news-events/news/ferc-affirms-generator-interconnection-rule-acts-compliance-filings).

Study this rule to understand transmission-provider generator interconnection reforms. Do not casually conflate its large- and small-generator transmission interconnection procedures with a state-regulated distribution DER process. Determine jurisdiction from the asset, transaction, tariff, and actual order language.

## Research questions

1. How do distribution interconnection requirements and wholesale aggregation requirements interact for a DER in Pennsylvania?
2. Which entity is responsible for each decision: distribution utility, PJM, FERC, Pennsylvania PUC, aggregator, or resource owner?
3. What public evidence is available to evaluate interconnection process outcomes, operating constraints, and market participation?
4. What information must be exchanged between utility, aggregator, PJM, and retail regulatory authority?
5. Which aspects of the process are technically necessary, and which are institutional or economic design choices?

## Required analysis

### 1. Build an institutional responsibility matrix

For each process stage, identify the decision-maker, governing source, data required, affected parties, and escalation path. Include application, technical review, study, upgrades, approval, commissioning, DERMS/control requirements, aggregator registration, telemetry, dispatch, and settlement.

### 2. Build a rule crosswalk

Compare:
- PPL tariff Rule 12;
- applicable Pennsylvania PUC regulations and orders;
- PJM tariff and manuals for DER aggregations;
- FERC Order 2222 and relevant compliance orders;
- IEEE 1547 and applicable certification standards.

For each provision, identify its legal status, effective date, applicability, and relationship to the other documents.

### 3. Draw the process map

Show the physical interconnection pathway separately from wholesale market participation. Use explicit handoffs and mark where the two processes interact. Do not represent PJM as the distribution interconnection authority for resources in the PJM DER Aggregator model when the governing sources assign that process to the state/utility pathway.

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