# 📊 Project 1 — Enterprise Risk Register

**Organization:** FinTech Co. | **Framework:** NIST RMF · ISO 31000 · FAIR  
**Role:** GRC Analyst | **Period:** Q1–Q2 2020  
**Status:** ✅ Complete

---

## 📌 Project Overview

A Series B-stage fintech company with 500 employees had no formal risk management program in place ahead of investor due diligence. The CISO engaged the GRC team to build an enterprise risk register from scratch, identify and assess organizational risks across all key domains, and produce board-ready reporting within 8 weeks.

---

## 🎯 Objectives

1. Identify and catalogue enterprise risks across 6 business domains
2. Score all risks using a consistent 5×5 likelihood and impact matrix
3. Assign formal risk owners and define treatment plans for each risk
4. Produce an executive-ready risk summary report for investor due diligence
5. Develop reusable templates for ongoing risk management

---

## 🔍 Scope

| Item | Detail |
|------|--------|
| **Domains Covered** | Information Security, Third-Party, Operational, Regulatory, Financial, Reputational |
| **Total Risks Assessed** | 15 risks |
| **Risk Scoring Method** | 5×5 Likelihood × Impact Matrix |
| **Frameworks Applied** | NIST SP 800-30, NIST RMF, ISO 31000, FAIR |
| **Stakeholders** | CISO, CTO, VP Procurement, Legal, GRC Team |
| **Deliverable Audience** | Board Risk Committee, Investors |

---

## 🛠️ Methodology

### Step 1 — Risk Identification
Risks were identified through structured interviews with department heads, review of prior incidents and near-misses, threat intelligence review, and analysis of existing control gaps.

### Step 2 — Risk Scoring
Each risk was scored using a **5×5 qualitative matrix:**

| Score | Likelihood | Impact |
|-------|-----------|--------|
| 5 | Almost Certain (>90%) | Catastrophic |
| 4 | Likely (60–90%) | Major |
| 3 | Possible (30–60%) | Moderate |
| 2 | Unlikely (10–30%) | Minor |
| 1 | Rare (<10%) | Negligible |

**Risk Score = Likelihood × Impact**
- 🔴 Critical: 15–25 | 🟠 High: 9–14 | 🟡 Medium: 4–8 | 🟢 Low: 1–3

### Step 3 — Risk Treatment
Each risk was assigned a treatment option (Mitigate, Transfer, Accept, or Avoid), a named risk owner, a remediation plan, and a target residual risk score.

### Step 4 — Reporting
Findings were consolidated into an executive summary report presented to the CISO and board risk committee.

---

## 📋 Key Findings

| Risk Level | Count | % of Total |
|-----------|-------|-----------|
| 🔴 Critical | 3 | 20% |
| 🟠 High | 5 | 33% |
| 🟡 Medium | 7 | 47% |
| 🟢 Low | 0 | 0% |

**Top 3 Critical Risks Identified:**

**1. Ransomware Attack on Production Infrastructure** — Score: 20/25  
No immutable backups in place; EDR deployed but network not segmented. Remediation: deploy immutable backup solution and implement network segmentation.

**2. Third-Party Vendor Data Breach** — Score: 15/25  
No formal TPRM program; vendors processing customer PII with no security assessment. Remediation: launch TPRM program and enforce SOC 2 requirements for Tier 1 vendors.

**3. Insider Threat — Privileged Data Exfiltration** — Score: 15/25  
No DLP or PAM deployed; offboarding process relies on manual checklist only. Remediation: deploy DLP and PAM tools; automate access revocation.

---

## 📁 Project Deliverables

| File | Description |
|------|-------------|
| [`risk-register.md`](./risk-register.md) | Full enterprise risk register — 15 risks with scores, owners, and treatment plans |
| [`docs/risk-methodology.md`](./docs/risk-methodology.md) | Risk scoring methodology aligned to NIST SP 800-30 |
| [`templates/risk-assessment-template.md`](./templates/risk-assessment-template.md) | Reusable risk assessment template |
| [`templates/risk-acceptance-form.md`](./templates/risk-acceptance-form.md) | Risk acceptance and exception form |
| [`reports/risk-summary-report.md`](./reports/risk-summary-report.md) | Executive risk summary report |

---

## 💡 Skills Demonstrated

`Risk Identification` `Risk Scoring` `5×5 Risk Matrix` `Treatment Planning` `Risk Ownership` `NIST RMF` `ISO 31000` `FAIR` `Executive Reporting` `Board Communication`

---

## 📌 Key Takeaways

- A structured risk register provides clarity and accountability that informal risk awareness cannot
- Critical risks without formal owners and treatment plans are effectively unmanaged risks
- Board-level risk reporting must translate technical findings into business impact language
- Risk registers are living documents — quarterly review cadence is essential for ongoing relevance
