# Internal Audit Plan — IT General Controls
**Organization:** HealthTech Co. | **Audit Ref:** IA-2025-002  
**Audit Period:** January 1 – June 30, 2025 | **Report Date:** July 31, 2025  
**Lead Auditor:** GRC Analyst | **Approved By:** CISO / Audit Committee

---

## 1. Audit Background and Authorization

This internal audit was commissioned by the Audit Committee in response to the upcoming SOC 2 Type II external audit scheduled for Q4 2025. The purpose is to proactively identify control deficiencies and remediate them before the external audit window begins.

Authorization: Audit Committee Resolution dated January 15, 2025.

---

## 2. Audit Objectives

1. **Assess design adequacy** — Are controls designed to prevent or detect material misstatements or risk events?
2. **Assess operating effectiveness** — Have controls operated consistently throughout the audit period?
3. **Identify deficiencies** — Document control gaps with business impact
4. **Recommend remediations** — Provide practical, prioritized recommendations

---

## 3. Audit Scope

### In-Scope Systems
| System | Purpose | Classification |
|--------|---------|---------------|
| AWS (Production) | Hosting SaaS platform | Critical |
| Okta | Identity and access management | Critical |
| GitHub | Source code management | Critical |
| Jira | Project and change tracking | Important |
| BambooHR | Employee records and offboarding | Important |
| Datadog | Monitoring and alerting | Important |

### In-Scope Control Domains
1. **Logical Access Management** — provisioning, deprovisioning, access reviews, privileged access
2. **Change Management** — change authorization, testing, deployment, emergency change
3. **Incident Management** — detection, response, escalation, closure
4. **Backup & Recovery** — backup execution, monitoring, restoration testing
5. **Vulnerability Management** — scanning, patch prioritization, SLA compliance
6. **Vendor Management** — vendor inventory, due diligence, contract controls
7. **Security Awareness** — training assignment, completion tracking

### Out of Scope
- Financial controls / SOX compliance
- Physical security (tested in separate audit)
- Customer-facing product features

---

## 4. Audit Methodology

### 4.1 Approach
This audit follows a **risk-based approach** aligned with the COSO Internal Control — Integrated Framework (2013) and COBIT 2019.

### 4.2 Testing Methods
| Method | Description |
|--------|-------------|
| **Inquiry** | Interviews with control owners and process personnel |
| **Observation** | Walkthrough of control processes in real time |
| **Inspection** | Review of policies, procedures, tickets, logs |
| **Re-performance** | Independently execute control to verify it functions as described |
| **Sampling** | Select statistically or judgmentally drawn samples from populations |

### 4.3 Sampling Approach
- Populations <25 items: test all
- Populations 25–100: sample 25 items
- Populations >100: sample 40–60 items or use statistical sampling at 95% confidence

---

## 5. Audit Team and Responsibilities

| Role | Name | Responsibility |
|------|------|---------------|
| Lead Auditor | GRC Analyst | Planning, fieldwork, findings, reporting |
| Technical SME | Senior Cloud Engineer | AWS, Okta, GitHub technical walkthroughs |
| Audit Sponsor | CISO | Stakeholder management, escalations |
| Auditee Liaison | IT Manager | Scheduling, evidence coordination |

---

## 6. Audit Schedule

| Phase | Activities | Timeline |
|-------|-----------|----------|
| Planning | Scope confirmation, risk assessment, audit program | Week 1–2 |
| Opening Meeting | Kick-off with auditees, explain objectives | Week 2 |
| Fieldwork | Evidence collection, interviews, testing | Week 3–7 |
| Finding Review | Draft findings, auditee validation | Week 8 |
| Reporting | Draft report, management response | Week 9–10 |
| Closing Meeting | Present findings to leadership | Week 10 |
| Follow-up | Track remediation of findings | Ongoing quarterly |

---

## 7. Audit Risk Assessment

| Control Domain | Inherent Risk | Control Risk | Audit Priority |
|---------------|--------------|-------------|----------------|
| Logical Access | High | High | 🔴 Priority 1 |
| Change Management | High | High | 🔴 Priority 1 |
| Incident Management | High | Medium | 🔴 Priority 1 |
| Backup & Recovery | Medium | High | 🟠 Priority 2 |
| Vulnerability Management | Medium | Medium | 🟠 Priority 2 |
| Vendor Management | Medium | High | 🟠 Priority 2 |
| Security Awareness | Low | Medium | 🟢 Priority 3 |

---

## 8. Evidence Requirements

| Control Domain | Evidence Requested |
|---------------|-------------------|
| Logical Access | User provisioning tickets, access review logs, deprovisioning records, Okta admin reports |
| Change Management | Change tickets, approvals, CAB meeting minutes, deployment logs |
| Incident Management | Incident tickets, IRP document, post-incident reviews |
| Backup & Recovery | Backup logs, restoration test reports, BCP/DR plan |
| Vulnerability Management | Vulnerability scan reports, patch tickets, SLA tracking |
| Vendor Management | Vendor list, contracts, vendor questionnaires, SOC 2 reports received |
| Security Awareness | LMS completion reports, training curriculum |

---

## 9. Reporting

Findings will be rated:
- 🔴 **High** — Significant control failure; material risk; immediate remediation required
- 🟠 **Medium** — Control gap; moderate risk; remediation required within 90 days
- 🟢 **Low** — Minor observation; best practice recommendation; remediation within 180 days

Final report will include:
- Executive summary with overall opinion
- Individual finding write-ups (condition, criteria, cause, effect, recommendation)
- Management response and remediation commitments
- Summary finding tracker
