# 💳 Project 4 — PCI DSS v4.0 Compliance Program

**Organization:** PayTech Co. | **Framework:** PCI DSS v4.0 · NIST SP 800-53  
**Role:** GRC Analyst | **Period:** Q3–Q4 2021  
**Status:** ✅ Complete

---

## 📌 Project Overview

A payments technology company processing over 6 million card transactions annually engaged the GRC team to build a PCI DSS v4.0 compliance program from the ground up. Classified as a **Merchant Level 1** — the highest tier — the organization required an annual Report on Compliance (RoC) by a Qualified Security Assessor (QSA). No formal PCI program existed prior to this engagement.

---

## 🎯 Objectives

1. Define and document the Cardholder Data Environment (CDE) scope
2. Assess compliance posture against all 12 PCI DSS v4.0 requirements and 67 sub-requirements
3. Identify critical gaps and build a prioritized remediation plan
4. Develop required policy documentation and compensating control framework
5. Prepare the organization for QSA engagement and RoC within 9 months

---

## 🔍 Scope

| Item | Detail |
|------|--------|
| **Merchant Level** | Level 1 — over 6 million transactions annually |
| **Assessment Type** | Report on Compliance (RoC) by QSA |
| **Requirements Assessed** | All 12 PCI DSS v4.0 requirements — 67 sub-requirements |
| **CDE Systems** | Payment API servers, token vault, payment databases, load balancer, HSM |
| **Third-Party Providers** | AWS, Stripe, CloudFlare (all with valid AOCs) |
| **Key Gap Area** | Requirement 10 — Logging & Monitoring |

---

## 🛠️ Methodology

### Step 1 — CDE Scoping
Mapped all systems, data flows, people, and third parties that store, process, or transmit cardholder data (CHD). Identified scope reduction opportunities including P2PE implementation and network segmentation.

### Step 2 — Gap Assessment
Each of the 12 requirements was assessed against current controls:
- ✅ **In Place** — Control fully meets PCI DSS requirement
- 🟡 **Partial** — Control partially meets requirement; gaps identified
- ❌ **Not In Place** — Control absent or non-functional

### Step 3 — Remediation Planning
Gaps were prioritised as RoC Blockers, High, Medium, or Low priority. A phased remediation plan was built with owners, timelines, and cost estimates.

### Step 4 — QSA Readiness
Prepared evidence packages, policy documentation, and network diagrams for QSA engagement.

---

## 📋 Key Findings

### PCI DSS Compliance Scorecard

| Requirement | Description | Result |
|-------------|-------------|--------|
| Req 1 | Network Security Controls | 🟡 Partial |
| Req 2 | Secure Configurations | 🟡 Partial |
| Req 3 | Protect Stored Account Data | 🟡 Partial |
| Req 4 | Protect Data in Transmission | ✅ Met |
| Req 5 | Protect Against Malicious Software | ✅ Met |
| Req 6 | Secure Systems and Software | 🟡 Partial |
| Req 7 | Restrict Access by Business Need | ✅ Met |
| Req 8 | Identify Users and Authenticate Access | 🟡 Partial |
| Req 9 | Restrict Physical Access | ✅ Met |
| Req 10 | Log and Monitor All Access | ❌ Not Met |
| Req 11 | Test Security Regularly | 🟡 Partial |
| Req 12 | Support Information Security with Policies | 🟡 Partial |

**Overall: 22% fully compliant | 45% partial | 33% not in place**

### Critical Gaps Identified

**Requirement 10 — Logging & Monitoring (Most Critical):**
- No SIEM deployed
- Logs retained for only 30 days (PCI requires 12 months minimum)
- No automated alerting or anomaly detection
- No audit trail for CDE access

**Requirement 3 — Stored Account Data:**
- 2 legacy systems storing PANs in plain text
- No formal key management policy

**Requirement 8 — Authentication:**
- 3 admin accounts accessing CDE without MFA
- Shared accounts still in use in legacy applications

### Scope Reduction Opportunities Identified

| Opportunity | Estimated Scope Impact |
|------------|----------------------|
| Implement Point-to-Point Encryption (P2PE) | Removes ~60% of in-scope systems |
| Complete legacy PAN migration to tokenization | Removes critical in-scope database |
| Network segmentation from corporate network | Removes connected-to systems from scope |

---

## 📁 Project Deliverables

| File | Description |
|------|-------------|
| [`pci-dss-gap-analysis.md`](./pci-dss-gap-analysis.md) | Full gap analysis — all 12 requirements and 67 sub-requirements |
| [`pci-scope-document.md`](./pci-scope-document.md) | CDE scope definition with data flow diagrams and asset inventory |
| [`reports/pci-remediation-plan.md`](./reports/pci-remediation-plan.md) | Phased remediation plan with $210K–$250K budget estimate |
| [`reports/roc-readiness-report.md`](./reports/) | QSA readiness assessment report |
| [`templates/compensating-control-worksheet.md`](./templates/compensating-control-worksheet.md) | PCI DSS compensating control worksheet (CCW) |
| [`docs/pci-policy-index.md`](./docs/) | Required PCI DSS policy inventory |

---

## 💡 Skills Demonstrated

`PCI DSS v4.0` `CDE Scoping` `Merchant Level 1` `Gap Analysis` `Compensating Controls` `Network Segmentation` `Tokenization` `QSA Readiness` `Remediation Planning` `Payment Security`

---

## 📌 Key Takeaways

- Requirement 10 (Logging & Monitoring) is the most common and impactful PCI DSS gap — no SIEM means no audit trail
- CDE scope reduction through P2PE and tokenization is the single highest-value activity before a QSA engagement
- The cost of PCI compliance ($150K–$250K) is significantly less than the cost of non-compliance (fines up to $100K/month + potential loss of card processing)
- Shared accounts and missing MFA on admin access are two of the fastest findings a QSA will identify
