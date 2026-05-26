# 🤝 Project 5 — Third-Party Risk Management (TPRM) Program

**Organization:** FinServ Co. | **Frameworks:** ISO 27001:2022 · NIST SP 800-161 · DORA · SOC 2 CC9.2  
**Role:** GRC Analyst | **Period:** Q1–Q2 2022  
**Status:** ✅ Complete

---

## 📌 Project Overview

A financial services firm with 200+ active vendors and no formal vendor risk program faced increasing pressure from its banking partner and an upcoming ISO 27001 audit. The GRC team was engaged to design and implement a Third-Party Risk Management (TPRM) program from scratch — covering vendor discovery, tiering, due diligence, contract requirements, ongoing monitoring, and offboarding processes.

---

## 🎯 Objectives

1. Build a complete vendor inventory and apply a risk-based tiering model
2. Design a standardized due diligence process with a security questionnaire (DDQ)
3. Define mandatory contract security clauses by vendor tier
4. Establish ongoing monitoring cadence for Tier 1 and Tier 2 vendors
5. Achieve compliance with ISO 27001 supplier controls (5.19–5.22) and DORA requirements

---

## 🔍 Scope

| Item | Detail |
|------|--------|
| **Total Vendors in Scope** | 215 vendors across all business functions |
| **Tier 1 (Critical)** | 18 vendors — process customer data or support critical systems |
| **Tier 2 (High)** | 45 vendors — access to internal systems or sensitive data |
| **Tier 3 (Medium)** | 89 vendors — limited data access |
| **Tier 4 (Low)** | 63 vendors — commodity suppliers, no data access |
| **Frameworks** | ISO 27001:2022, NIST SP 800-161, DORA, SOC 2 CC9.2, GDPR Article 28 |
| **Regulatory Drivers** | ISO 27001 audit, banking partner requirements, DORA compliance |

---

## 🛠️ Methodology

### Step 1 — Vendor Discovery & Inventory
Compiled a complete vendor inventory from procurement records, legal contracts, IT asset management, and business unit interviews. Identified 215 active vendors — many previously unknown to the GRC team.

### Step 2 — Vendor Tiering
Applied a risk-based tiering model scoring vendors on:
- Data sensitivity (type and volume of data accessed)
- System criticality (impact if vendor fails or is breached)
- Access level (logical, physical, or data access)
- Regulatory exposure (GDPR, PCI DSS, DORA requirements)

### Step 3 — Due Diligence Assessment
- **Tier 1:** Full 10-section DDQ + SOC 2 / ISO 27001 report review + security interview
- **Tier 2:** Abbreviated DDQ + compliance report review
- **Tier 3:** Self-attestation questionnaire
- **Tier 4:** Standard contract terms only

### Step 4 — Contract Review
Reviewed all Tier 1 and Tier 2 vendor contracts for required security clauses including DPAs, breach notification requirements, right-to-audit, and sub-processor approval.

### Step 5 — Ongoing Monitoring Framework
Defined review frequencies, event triggers, and escalation procedures for each vendor tier.

---

## 📋 Key Findings

### Initial Vendor Assessment Results

| Finding | Detail |
|---------|--------|
| Vendors with no security assessment | 47% of Tier 1 vendors |
| Contracts with no security obligations | 23 vendors |
| Vendors processing data with no written agreement | 6 vendors |
| Vendors not reviewed in 3+ years | 12 vendors |
| Formal offboarding process | 0 vendors had been formally offboarded |

### Critical Risk Identified — VENDOR-005 (DataVendor Ltd)

**Risk Level: 🔴 Critical**

DataVendor Ltd was receiving bulk customer PII exports for analytics purposes with:
- No Data Processing Agreement (DPA)
- No security questionnaire completed
- No breach notification clause in contract
- No SOC 2 report or ISO 27001 certification

**Action Taken:** Data transfers immediately suspended pending emergency assessment and DPA negotiation.

### TPRM Program Maturity — Before vs. After

| Domain | Before | After |
|--------|--------|-------|
| Vendor inventory | Ad hoc | Complete — 215 vendors tiered |
| Due diligence | None | Risk-based DDQ by tier |
| Contract security | Inconsistent | Standardized clauses enforced |
| Ongoing monitoring | None | Quarterly (Tier 1), Annual (Tier 2) |
| Incident notification | None | 72-hour requirement in all Tier 1 contracts |
| Offboarding process | None | Formal checklist with data deletion confirmation |
| **Overall Maturity** | **Level 1** | **Level 3 (target)** |

---

## 📁 Project Deliverables

| File | Description |
|------|-------------|
| [`tprm-program-charter.md`](./tprm-program-charter.md) | Full TPRM program charter — governance, lifecycle, KPIs |
| [`vendor-risk-register.md`](./vendor-risk-register.md) | Vendor inventory with tiering, risk ratings, and open issues |
| [`templates/vendor-questionnaire.md`](./templates/vendor-questionnaire.md) | 10-section vendor security due diligence questionnaire |
| [`templates/vendor-risk-assessment.md`](./templates/) | Vendor risk scoring and assessment template |
| [`templates/vendor-offboarding-checklist.md`](./templates/) | Vendor offboarding and exit checklist |
| [`reports/tprm-maturity-assessment.md`](./reports/) | TPRM program maturity assessment report |
| [`docs/tprm-policy.md`](./docs/) | Third-Party Risk Management Policy |

---

## 💡 Skills Demonstrated

`TPRM` `Vendor Risk Management` `Vendor Tiering` `Due Diligence` `DDQ Development` `Contract Security` `ISO 27001` `DORA` `NIST SP 800-161` `SOC 2 CC9.2` `GDPR Article 28` `Ongoing Monitoring`

---

## 📌 Key Takeaways

- Most organizations significantly underestimate their vendor count — shadow IT and informal vendor relationships are common
- A risk-based tiering model ensures proportionate due diligence — not every vendor needs the same level of scrutiny
- The most dangerous vendors are often Tier 1 vendors that have been in place for years with no formal assessment
- DORA (EU) is significantly raising the bar for third-party risk management in financial services — early preparation is essential
