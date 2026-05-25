# HIPAA Security Risk Assessment (SRA)
**Organization:** HealthStart Co. | **Date:** Q2 2025 | **Version:** 1.0  
**Required By:** 45 CFR §164.308(a)(1)(ii)(A) | **Assessor:** GRC Analyst  
**NIST Reference:** NIST SP 800-66 Rev. 2

---

## 1. Purpose and Legal Requirement

The HIPAA Security Rule requires all Covered Entities and Business Associates to conduct an **accurate and thorough assessment of the potential risks and vulnerabilities to the confidentiality, integrity, and availability of ePHI.** (45 CFR §164.308(a)(1)(ii)(A))

This Security Risk Assessment (SRA) fulfills that requirement and serves as the foundation for HealthStart Co.'s HIPAA compliance program.

---

## 2. Scope

**In-Scope:** All systems, locations, and processes that create, receive, maintain, or transmit electronic Protected Health Information (ePHI).

**ePHI Definition:** Any individually identifiable health information stored or transmitted in electronic form, including patient names, dates of birth, diagnoses, treatment records, appointment history, and insurance information.

**Assessment Period:** Q2 2025  
**Patient Population:** 85,000 patients  
**Staff with ePHI Access:** 210 employees

---

## 3. ePHI Asset Inventory

| Asset ID | System | ePHI Type | Location | Access Level |
|----------|--------|-----------|----------|-------------|
| ePHI-001 | Epic EHR Integration | Full patient records | AWS + Epic Cloud | Clinical staff |
| ePHI-002 | Telehealth Platform | Consultation notes, video sessions | Vendor cloud | Clinicians + patients |
| ePHI-003 | AWS Production Backend | All ePHI (application layer) | AWS us-east-1 | Engineers + DBAs |
| ePHI-004 | Google Workspace | Patient emails, appointment confirmations | Google Cloud | All staff |
| ePHI-005 | Slack | Informal PHI sharing in channels | Slack Cloud | All staff |
| ePHI-006 | Intercom | Patient support chat | Intercom Cloud | Support team |
| ePHI-007 | On-premise file server | Legacy patient documents (pre-2022) | Office server room | Admin staff |

---

## 4. Threat and Vulnerability Identification

### 4.1 Threats to ePHI

| Threat Category | Specific Threats Identified |
|----------------|---------------------------|
| **External — Malicious** | Ransomware, phishing targeting clinical staff, credential theft, brute-force attacks |
| **External — Environmental** | Power outage, natural disaster affecting office data |
| **Internal — Malicious** | Unauthorized ePHI access by workforce members, data theft by departing employees |
| **Internal — Accidental** | Accidental email of PHI to wrong recipient, misconfigured cloud storage |
| **Third-Party** | Business associate breach, supply chain attack on EHR vendor |
| **Technical** | Unpatched vulnerabilities, software failures, data corruption |

### 4.2 Vulnerabilities Identified

| ID | Vulnerability | System Affected | Exploitability |
|----|--------------|----------------|---------------|
| V-001 | No audit logging of ePHI access | AWS Backend, Google Workspace | High |
| V-002 | ePHI transmitted via Slack (no BAA, no encryption) | Slack | High |
| V-003 | Legacy file server not encrypted | On-premise server | High |
| V-004 | No MFA on Google Workspace for all staff | Google Workspace | High |
| V-005 | No formal workforce HIPAA training records | Organisation-wide | Medium |
| V-006 | Intercom support chat processes ePHI without BAA | Intercom | High |
| V-007 | No documented breach notification procedure | Policy gap | Medium |
| V-008 | Incomplete patch management for backend systems | AWS Backend | Medium |
| V-009 | Business Associates using ePHI without signed BAAs | 14 vendors | High |
| V-010 | No documented sanction policy for HIPAA violations | Policy gap | Low |

---

## 5. Risk Assessment

### Risk Scoring Methodology
**Likelihood (1–5):** Probability of threat exploiting vulnerability  
**Impact (1–5):** Consequence to confidentiality, integrity, or availability of ePHI  
**Risk Score:** Likelihood × Impact

| Risk Level | Score |
|-----------|-------|
| 🔴 High | 15–25 |
| 🟠 Medium | 8–14 |
| 🟢 Low | 1–7 |

---

### Risk Register

| Risk ID | Threat | Vulnerability | Likelihood | Impact | Score | Level | Current Controls |
|---------|--------|--------------|-----------|--------|-------|-------|-----------------|
| R-001 | Ransomware encrypts ePHI | Unpatched systems, no immutable backup | 4 | 5 | **20** | 🔴 High | EDR deployed; backups exist but not tested |
| R-002 | ePHI transmitted via Slack to unauthorized parties | No BAA with Slack; staff use for clinical comms | 4 | 4 | **16** | 🔴 High | No controls |
| R-003 | Unauthorized ePHI access by former employee | No automated deprovisioning; accounts not removed | 3 | 5 | **15** | 🔴 High | Manual offboarding checklist only |
| R-004 | Business associate breach exposes ePHI | 14 BAs with no BAA; unknown security posture | 3 | 5 | **15** | 🔴 High | No BA security assessment program |
| R-005 | Phishing attack compromises clinical staff credentials | No MFA on Google Workspace for all users | 4 | 4 | **16** | 🔴 High | MFA optional; not enforced |
| R-006 | Legacy file server data exposed or lost | No encryption at rest; single copy | 2 | 5 | **10** | 🟠 Medium | Physical access controls only |
| R-007 | Accidental PHI disclosure via wrong email recipient | No DLP; staff send PHI via personal email | 4 | 3 | **12** | 🟠 Medium | No controls |
| R-008 | Audit trail insufficient for breach investigation | No centralized logging of ePHI access | 3 | 4 | **12** | 🟠 Medium | Application logs only |
| R-009 | Delayed breach notification due to no procedure | No breach notification SOP | 2 | 4 | **8** | 🟠 Medium | No formal procedure |
| R-010 | Insider threat — ePHI exfiltration | No DLP; no user behaviour monitoring | 2 | 4 | **8** | 🟠 Medium | RBAC in place |
| R-011 | AWS misconfiguration exposes ePHI | No CSPM; ad hoc cloud configuration reviews | 3 | 3 | **9** | 🟠 Medium | Manual reviews |
| R-012 | Power outage causes ePHI unavailability | No UPS for on-premise server | 2 | 3 | **6** | 🟢 Low | Cloud systems unaffected |

---

## 6. Risk Summary

| Risk Level | Count |
|-----------|-------|
| 🔴 High | 5 |
| 🟠 Medium | 6 |
| 🟢 Low | 1 |
| **Total** | **12** |

---

## 7. Recommended Risk Response

| Risk | Response | Priority Action |
|------|----------|----------------|
| R-001 | Mitigate | Deploy immutable backups; enforce patch SLA |
| R-002 | Mitigate / Avoid | Ban PHI in Slack; implement HIPAA-compliant messaging tool |
| R-003 | Mitigate | Automate deprovisioning; conduct access review |
| R-004 | Mitigate | Execute BAAs with all 14 business associates immediately |
| R-005 | Mitigate | Enforce MFA on Google Workspace for all staff immediately |
| R-006 | Mitigate | Encrypt legacy file server; migrate to cloud with proper controls |
| R-007 | Mitigate | Deploy DLP; train staff on PHI handling via email |
| R-008 | Mitigate | Deploy SIEM with ePHI access audit trail |
| R-009 | Mitigate | Develop and test breach notification procedure |
| R-010 | Mitigate | Deploy UEBA monitoring for ePHI access |
| R-011 | Mitigate | Deploy CSPM; implement automated misconfiguration detection |
| R-012 | Accept | Low risk; monitor and review at next SRA |

---

## 8. SRA Review and Approval

This SRA must be reviewed and updated:
- At least annually
- When operations, facilities, or technology changes occur significantly
- Following a security incident involving ePHI

| Role | Name | Date | Signature |
|------|------|------|-----------|
| GRC Analyst (Preparer) | | | |
| CISO / Privacy Officer (Reviewer) | | | |
| CEO (Approver) | | | |

*Retaining this completed SRA is a HIPAA regulatory requirement. Retain for minimum 6 years from date of creation or last effective date.*
