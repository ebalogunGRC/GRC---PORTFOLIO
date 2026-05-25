# Project 3 — Internal Audit & Controls Testing

**Scenario:** A healthcare technology company (HIPAA-covered entity) commissioned an internal audit of its IT General Controls (ITGCs) and security controls ahead of an external SOC 2 audit. The GRC team led the audit planning, fieldwork, evidence review, and findings reporting.

**Frameworks:** COSO 2013 · COBIT 2019 · SOC 2 Trust Service Criteria · HIPAA Security Rule

---

## 📋 Deliverables

| File | Description |
|------|-------------|
| [`audit-plan.md`](./audit-plan.md) | Internal audit plan and scope |
| [`control-testing-workpapers.md`](./control-testing-workpapers.md) | Control testing workpapers with results |
| [`audit-findings-report.md`](./audit-findings-report.md) | Formal audit findings and recommendations |
| [`templates/audit-program-template.md`](./templates/audit-program-template.md) | Reusable audit program template |
| [`templates/finding-template.md`](./templates/finding-template.md) | Individual finding write-up template |
| [`docs/itgc-control-matrix.md`](./docs/itgc-control-matrix.md) | IT General Controls matrix |

---

## 🎯 Audit Objectives

1. Assess design and operating effectiveness of IT General Controls
2. Evaluate access management, change management, and incident management processes
3. Test evidence of control operation over the audit period
4. Identify control deficiencies and provide remediation recommendations

---

## Audit Scope

- **In-Scope Systems:** Production SaaS platform, AWS cloud environment, GitHub (source code), Okta (IAM)
- **In-Scope Processes:** Logical access, change management, backups, incident response, vendor management
- **Audit Period:** January 1 – June 30, 2025 (6 months)
- **Population:** 87 change tickets, 156 access provisioning/deprovisioning events, 4 security incidents

---

## Key Audit Results

| Finding | Severity | Control Domain | Status |
|---------|----------|---------------|--------|
| FIND-001: No formal change approval process | 🔴 High | Change Management | Open |
| FIND-002: Stale user accounts not deprovisioned | 🔴 High | Access Management | Open |
| FIND-003: No SIEM — incidents not logged centrally | 🔴 High | Monitoring | Open |
| FIND-004: Incomplete offboarding — 3 accounts active | 🔴 High | Access Management | Open |
| FIND-005: Backup restoration not tested | 🟠 Medium | Business Continuity | Open |
| FIND-006: Patch SLA not met for 6 critical patches | 🟠 Medium | Vulnerability Management | Open |
| FIND-007: Vendor contracts lack security SLAs | 🟠 Medium | Third-Party Management | Open |
| FIND-008: Security training not tracked in LMS | 🟢 Low | Awareness | Remediated |

**Overall Opinion: Needs Improvement**  
Multiple High-severity findings indicate control deficiencies that represent meaningful risk to the organization and would likely result in qualified opinion in external SOC 2 audit.

---

## Skills Demonstrated

`Audit Planning` `Control Testing` `Workpaper Documentation` `Finding Writing` `ITGC Assessment` `SOC 2 Audit Support` `COSO Framework` `COBIT 2019` `Evidence Review` `Audit Reporting`
