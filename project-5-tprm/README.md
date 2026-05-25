# Project 5 — Third-Party Risk Management (TPRM) Program

**Scenario:** A financial services firm with 200+ active vendors and no formal vendor risk program engaged the GRC team to design and implement a Third-Party Risk Management (TPRM) program from scratch. Regulatory pressure from the firm's banking partner and upcoming ISO 27001 audit made this a priority initiative.

**Frameworks:** ISO 27001:2022 (Controls 5.19–5.22) · NIST SP 800-161 · SOC 2 CC9.2 · DORA (Digital Operational Resilience Act) · FSB Third-Party Risk Principles

---

## 📋 Deliverables

| File | Description |
|------|-------------|
| [`tprm-program-charter.md`](./tprm-program-charter.md) | TPRM program design and governance charter |
| [`vendor-risk-register.md`](./vendor-risk-register.md) | Vendor inventory with tiering and risk ratings |
| [`templates/vendor-questionnaire.md`](./templates/vendor-questionnaire.md) | Security due diligence questionnaire (DDQ) |
| [`templates/vendor-risk-assessment.md`](./templates/vendor-risk-assessment.md) | Vendor risk assessment scoring template |
| [`templates/vendor-offboarding-checklist.md`](./templates/vendor-offboarding-checklist.md) | Vendor offboarding and exit checklist |
| [`reports/tprm-maturity-assessment.md`](./reports/tprm-maturity-assessment.md) | TPRM program maturity assessment |
| [`docs/tprm-policy.md`](./docs/tprm-policy.md) | Third-Party Risk Management Policy |

---

## 🎯 Objectives

1. Design a risk-based TPRM program with vendor tiering methodology
2. Build a vendor inventory and conduct risk assessments on Tier 1 vendors
3. Develop standardized due diligence questionnaire and contract security requirements
4. Establish ongoing monitoring and review cadence
5. Achieve compliance with ISO 27001 supplier controls and DORA requirements

---

## Vendor Tiering Model

| Tier | Risk Level | Criteria | # Vendors | Review Frequency |
|------|-----------|----------|-----------|-----------------|
| Tier 1 | Critical | Access to customer data, critical systems, or payment processing | 18 | Annual + event-triggered |
| Tier 2 | High | Access to internal systems or sensitive business data | 45 | Annual |
| Tier 3 | Medium | Business services with limited data access | 89 | Every 2 years |
| Tier 4 | Low | Commodity suppliers, no data access | 63 | Every 3 years |
| **Total** | | | **215** | |

---

## Key Findings from Initial Vendor Review

- **47% of Tier 1 vendors** had no valid SOC 2 report on file
- **23 vendors** had contracts with no data security obligations or DPA
- **6 vendors** were processing customer data with no written agreement at all
- **12 vendors** had not been reviewed in over 3 years despite high-risk classification
- **0 vendors** had been formally offboarded using a documented process

---

## TPRM Program Maturity (Before vs After)

| Domain | Before | After (Target) |
|--------|--------|----------------|
| Vendor inventory | Ad hoc | Complete, tiered |
| Due diligence | None | Risk-based DDQ |
| Contract security | Inconsistent | Standardized clauses |
| Ongoing monitoring | None | Quarterly for Tier 1 |
| Incident notification | None | 72-hour requirement |
| Offboarding | None | Formal checklist |
| Overall Maturity | Level 1 | Level 3 (target) |

---

## Skills Demonstrated

`TPRM` `Vendor Risk Management` `Due Diligence` `Third-Party Risk` `ISO 27001` `SOC 2 CC9.2` `DORA` `Vendor Tiering` `Contract Security` `Ongoing Monitoring` `NIST SP 800-161`
