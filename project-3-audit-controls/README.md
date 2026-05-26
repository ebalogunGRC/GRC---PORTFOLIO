# 🔍 Project 3 — Internal Audit & Controls Testing

**Organization:** HealthTech Co. | **Frameworks:** COSO 2013 · COBIT 2019 · SOC 2  
**Role:** Lead GRC Analyst | **Period:** Q1–Q2 2021  
**Status:** ✅ Complete

---

## 📌 Project Overview

A healthcare technology company processing sensitive patient data commissioned an internal audit of its IT General Controls (ITGCs) ahead of an external SOC 2 Type II audit scheduled for Q4 2021. The GRC team led the full audit lifecycle — from planning and scoping through fieldwork, evidence review, findings documentation, and reporting — producing a formal audit report with 8 findings presented to the CISO and Audit Committee.

---

## 🎯 Objectives

1. Assess the design adequacy of IT General Controls across 7 domains
2. Test the operating effectiveness of controls over a 6-month audit period
3. Identify control deficiencies and rate by severity
4. Produce formal audit findings in IIA 5-component format
5. Provide actionable remediation recommendations before the external SOC 2 audit

---

## 🔍 Scope

| Item | Detail |
|------|--------|
| **Audit Period** | January 1 – June 30, 2021 |
| **In-Scope Systems** | AWS (Production), Okta (IAM), GitHub (Source Code), Jira, BambooHR, Datadog |
| **Control Domains** | Logical Access, Change Management, Incident Management, Backup & Recovery, Vulnerability Management, Vendor Management, Security Awareness |
| **Controls Tested** | 24 IT General Controls |
| **Population Sizes** | 87 change tickets, 156 access events, 4 security incidents |
| **Frameworks** | COSO 2013, COBIT 2019, SOC 2 Trust Service Criteria, IIA Standards |

---

## 🛠️ Methodology

### Approach
Risk-based audit methodology aligned to the **COSO Internal Control — Integrated Framework (2013)** and **COBIT 2019**, with control testing procedures designed to satisfy SOC 2 Trust Service Criteria evidence requirements.

### Testing Methods Used

| Method | Description |
|--------|-------------|
| **Inquiry** | Interviews with control owners and process personnel |
| **Observation** | Walkthroughs of control processes in real time |
| **Inspection** | Review of policies, procedures, tickets, and logs |
| **Re-performance** | Independently executed controls to verify they function as described |
| **Sampling** | Populations >25 items sampled at 25 items; >100 items sampled at 40 |

### Audit Phases
1. **Planning** — Risk assessment, scope confirmation, audit program development
2. **Fieldwork** — Evidence collection, interviews, control testing
3. **Finding Review** — Draft findings validated with control owners
4. **Reporting** — Final report issued to CISO and Audit Committee

---

## 📋 Key Findings

### Overall Audit Opinion: **NEEDS IMPROVEMENT**

| Control Domain | Total Controls | ✅ Effective | 🟡 Partial | ❌ Deficient |
|---------------|--------------|------------|-----------|------------|
| Access Management | 6 | 2 | 1 | 3 |
| Change Management | 4 | 0 | 2 | 2 |
| Incident Management | 3 | 0 | 1 | 2 |
| Monitoring | 3 | 0 | 1 | 2 |
| Backup & Recovery | 3 | 1 | 0 | 2 |
| Vulnerability Management | 3 | 1 | 0 | 2 |
| Security Awareness | 1 | 0 | 1 | 0 |
| **Total** | **24** | **4 (17%)** | **6 (25%)** | **14 (58%)** |

### Summary of Audit Findings

| Finding | Severity | Domain |
|---------|----------|--------|
| FIND-001: No formal change approval process | 🔴 High | Change Management |
| FIND-002: 23 stale user accounts not deprovisioned | 🔴 High | Access Management |
| FIND-003: No SIEM — incidents not logged centrally | 🔴 High | Monitoring |
| FIND-004: 3 former employee accounts active in production | 🔴 High | Access Management |
| FIND-005: Backup restoration not tested in 18 months | 🟠 Medium | Backup & Recovery |
| FIND-006: Critical patches not applied within SLA | 🟠 Medium | Vulnerability Management |
| FIND-007: Vendor contracts lack security SLAs | 🟠 Medium | Vendor Management |
| FIND-008: Security training completion not tracked | 🟢 Low | Awareness — ✅ Remediated |

**Most Critical Finding — FIND-004:**  
3 former employee accounts with active AWS programmatic access keys — used within the past 30 days. Immediate account disablement and security investigation initiated during fieldwork.

---

## 📁 Project Deliverables

| File | Description |
|------|-------------|
| [`audit-plan.md`](./audit-plan.md) | Internal audit plan — scope, methodology, risk assessment, schedule |
| [`audit-findings-report.md`](./audit-findings-report.md) | Formal audit report — 8 findings in IIA 5-component format |
| [`docs/itgc-control-matrix.md`](./docs/itgc-control-matrix.md) | 24-control ITGC matrix mapped to SOC 2 and COBIT 2019 |
| [`templates/finding-template.md`](./templates/finding-template.md) | Reusable IIA-aligned finding write-up template |
| [`templates/audit-program-template.md`](./templates/) | Reusable audit program template |

---

## 💡 Skills Demonstrated

`Audit Planning` `ITGC Testing` `Control Assessment` `IIA Standards` `Workpaper Documentation` `Finding Writing` `SOC 2 Audit Support` `COSO Framework` `COBIT 2019` `Evidence Review` `Risk-Based Auditing`

---

## 📌 Key Takeaways

- 58% of controls tested were deficient — a result typical of organizations that have never undergone a formal ITGC audit
- Access management is consistently the highest-risk domain — orphaned accounts represent real, immediate threat
- The IIA 5-component finding format (Condition, Criteria, Cause, Effect, Recommendation) produces findings that are clear, defensible, and actionable
- Internal audits conducted before external SOC 2 audits dramatically reduce the risk of qualified opinions
