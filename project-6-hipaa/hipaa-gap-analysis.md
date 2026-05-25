# HIPAA Security Rule — Gap Analysis
**Organization:** HealthStart Co. | **Date:** Q2 2025  
**Reference:** 45 CFR Part 164 Subpart C | **Assessor:** GRC Analyst

---

## Assessment Key

| Status | Symbol |
|--------|--------|
| Compliant | ✅ |
| Partially Compliant | 🟡 |
| Non-Compliant | ❌ |

**Specification Type — R:** Required | **A:** Addressable *(must implement or document equivalent)*

---

## Administrative Safeguards — 45 CFR §164.308

| Standard | Implementation Specification | Type | Status | Gap | Priority |
|----------|------------------------------|------|--------|-----|----------|
| Security Management Process | Risk Analysis | R | ❌ | No formal SRA ever conducted | 🔴 Critical |
| Security Management Process | Risk Management | R | ❌ | No risk treatment plan | 🔴 Critical |
| Security Management Process | Sanction Policy | R | ❌ | No documented sanction policy for HIPAA violations | 🟠 High |
| Security Management Process | Information System Activity Review | R | ❌ | No audit log review process | 🔴 Critical |
| Assigned Security Responsibility | Designate Security Officer | R | 🟡 | CISO assigned informally; not documented in policy | 🟠 High |
| Workforce Security | Authorization and Supervision | A | 🟡 | Access granted based on role; no formal authorization procedure documented | 🟠 High |
| Workforce Security | Workforce Clearance | A | ✅ | Background checks conducted for all clinical staff | — |
| Workforce Security | Termination Procedures | A | 🟡 | Manual checklist; no automated deprovisioning | 🔴 Critical |
| Information Access Management | Isolating Healthcare Clearinghouse | A | ✅ | Not applicable — not a clearinghouse | — |
| Information Access Management | Access Authorization | A | 🟡 | RBAC in place; not formally documented | 🟠 High |
| Information Access Management | Access Establishment and Modification | A | 🟡 | Provisioning process exists; not formally documented | 🟠 High |
| Security Awareness Training | Security Reminders | A | ❌ | No ongoing security reminders to workforce | 🟠 High |
| Security Awareness Training | Protection from Malicious Software | A | 🟡 | EDR in place; no training on malware awareness | 🟠 High |
| Security Awareness Training | Log-in Monitoring | A | ❌ | No training on monitoring login attempts | 🟡 Medium |
| Security Awareness Training | Password Management | A | 🟡 | Password policy exists; no training provided | 🟠 High |
| Security Incident Procedures | Response and Reporting | R | ❌ | No documented HIPAA incident response procedure | 🔴 Critical |
| Contingency Plan | Data Backup Plan | R | 🟡 | Backups running; not formally documented or tested | 🔴 Critical |
| Contingency Plan | Disaster Recovery Plan | R | ❌ | No DR plan; RTO/RPO not defined | 🔴 Critical |
| Contingency Plan | Emergency Mode Operation | R | ❌ | No emergency mode operation plan | 🟠 High |
| Contingency Plan | Testing and Revision | A | ❌ | No BCP/DR testing conducted | 🟠 High |
| Contingency Plan | Applications and Data Criticality | A | ❌ | No criticality analysis documented | 🟡 Medium |
| Evaluation | Periodic Technical and Non-Technical Evaluation | R | ❌ | No formal periodic evaluation program | 🟠 High |
| Business Associate Contracts | BAA with Business Associates | R | ❌ | 14 BAs processing ePHI without signed BAAs | 🔴 Critical |

---

## Physical Safeguards — 45 CFR §164.310

| Standard | Implementation Specification | Type | Status | Gap | Priority |
|----------|------------------------------|------|--------|-----|----------|
| Facility Access Controls | Contingency Operations | A | 🟡 | Badge access in place; no contingency access procedure | 🟡 Medium |
| Facility Access Controls | Facility Security Plan | A | 🟡 | Physical security exists; not formally documented | 🟠 High |
| Facility Access Controls | Access Control and Validation | A | ✅ | Badge access + visitor log; server room restricted | — |
| Facility Access Controls | Maintenance Records | A | 🟡 | Maintenance conducted; records not retained | 🟡 Medium |
| Workstation Use | Workstation Use Policy | R | ✅ | Acceptable Use Policy in place and signed | — |
| Workstation Security | Physical Safeguards for Workstations | R | ✅ | Cable locks in office; clean desk policy | — |
| Device and Media Controls | Disposal | R | 🟡 | Devices wiped before disposal; no certificate of destruction | 🟠 High |
| Device and Media Controls | Media Re-use | R | ✅ | Full wipe before reuse confirmed | — |
| Device and Media Controls | Accountability | A | 🟡 | Asset inventory exists; not linked to ePHI data | 🟡 Medium |
| Device and Media Controls | Data Backup and Storage | A | 🟡 | Backups configured; not formally documented | 🟠 High |

---

## Technical Safeguards — 45 CFR §164.312

| Standard | Implementation Specification | Type | Status | Gap | Priority |
|----------|------------------------------|------|--------|-----|----------|
| Access Control | Unique User Identification | R | ✅ | Individual accounts for all users; no shared accounts | — |
| Access Control | Emergency Access Procedure | R | ❌ | No documented emergency access procedure for ePHI systems | 🟠 High |
| Access Control | Automatic Logoff | A | 🟡 | Session timeout configured for EHR; not all systems | 🟡 Medium |
| Access Control | Encryption and Decryption | A | 🟡 | Encryption at rest partial; not all ePHI systems covered | 🔴 Critical |
| Audit Controls | Audit Controls | R | ❌ | No centralized audit logging of ePHI access; per-application logs only | 🔴 Critical |
| Integrity | Authentication of ePHI | A | 🟡 | Data integrity checks in EHR; not all systems | 🟡 Medium |
| Person or Entity Authentication | Authentication | R | 🟡 | MFA not enforced on all systems (Google Workspace gap) | 🔴 Critical |
| Transmission Security | Encryption | A | ✅ | TLS 1.2+ enforced on all ePHI transmissions | — |
| Transmission Security | Integrity Controls | A | ✅ | TLS provides transmission integrity | — |

---

## Organizational Requirements — 45 CFR §164.314

| Standard | Implementation Specification | Type | Status | Gap | Priority |
|----------|------------------------------|------|--------|-----|----------|
| Business Associate Contracts | BAA Requirements | R | ❌ | 14 of 28 BAs have no signed BAA | 🔴 Critical |
| Requirements for Group Health Plans | — | R | ✅ | Not applicable — not a group health plan | — |

---

## Policies and Procedures — 45 CFR §164.316

| Standard | Implementation Specification | Type | Status | Gap | Priority |
|----------|------------------------------|------|--------|-----|----------|
| Policies and Procedures | Implement policies and procedures | R | 🟡 | Some policies exist; not comprehensive; not formally reviewed | 🟠 High |
| Documentation | Time limit (retain for 6 years) | R | 🟡 | No formal document retention policy | 🟠 High |
| Documentation | Availability | R | ✅ | Policies stored on intranet; accessible to workforce | — |
| Documentation | Updates | R | 🟡 | Policies not consistently updated when practices change | 🟠 High |

---

## HIPAA Compliance Scorecard

| Safeguard Category | Total Specs | ✅ Compliant | 🟡 Partial | ❌ Non-Compliant |
|-------------------|------------|------------|-----------|----------------|
| Administrative | 23 | 1 (4%) | 9 (39%) | 13 (57%) |
| Physical | 10 | 3 (30%) | 6 (60%) | 1 (10%) |
| Technical | 9 | 2 (22%) | 4 (44%) | 3 (33%) |
| Organizational | 2 | 1 (50%) | 0 | 1 (50%) |
| Policies & Procedures | 4 | 1 (25%) | 3 (75%) | 0 |
| **Total** | **48** | **8 (17%)** | **22 (46%)** | **18 (38%)** |

---

## Top 8 Priority Remediation Actions

| # | Action | Requirement | Risk if Not Addressed |
|---|--------|------------|----------------------|
| 1 | Complete and document formal Security Risk Assessment | §164.308(a)(1) | Direct HIPAA violation — OCR's #1 enforcement action |
| 2 | Execute BAAs with all 14 business associates | §164.314(a) | Direct HIPAA violation — significant fine exposure |
| 3 | Enforce MFA on all systems with ePHI access | §164.312(d) | High breach risk via credential compromise |
| 4 | Deploy centralized audit logging for ePHI access | §164.312(b) | Cannot detect or investigate unauthorized access |
| 5 | Develop breach notification procedure | §164.308(a)(6) | Regulatory violation if breach occurs |
| 6 | Encrypt ePHI at rest on all systems | §164.312(a)(2)(iv) | Data exposure if system compromised |
| 7 | Develop and test DR plan with RTO/RPO | §164.308(a)(7) | ePHI unavailability; continuity failure |
| 8 | Ban PHI in Slack; implement HIPAA-compliant messaging | §164.312 | Unprotected PHI in non-HIPAA platform |
