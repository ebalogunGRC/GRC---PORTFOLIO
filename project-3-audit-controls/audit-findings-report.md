# Internal Audit Report — IT General Controls
**Organization:** HealthTech Co. | **Audit Ref:** IA-2025-002  
**Audit Period:** January 1 – June 30, 2025 | **Report Date:** July 31, 2025  
**Distribution:** CISO, CTO, Audit Committee | **Classification:** Confidential

---

## Overall Audit Opinion

> **NEEDS IMPROVEMENT**
>
> The internal audit identified four High-severity and three Medium-severity control deficiencies. The volume and severity of findings indicate that IT General Controls are not operating effectively across key domains. These deficiencies represent meaningful risk to the organization and would likely result in exceptions noted in an external SOC 2 Type II audit. Management should prioritize remediation of High findings before the external audit window commences.

---

## Executive Summary

| Metric | Result |
|--------|--------|
| Control domains assessed | 7 |
| Controls tested | 24 |
| Controls operating effectively | 14 (58%) |
| Controls with deficiencies | 10 (42%) |
| High findings | 4 |
| Medium findings | 3 |
| Low findings | 1 |
| Remediated during audit | 1 |

---

## Findings

---

### FIND-001 — No Formal Change Approval Process
**Severity:** 🔴 High | **Domain:** Change Management | **Status:** Open

**Condition:**  
Of 87 change tickets reviewed for the period January 1 – June 30, 2025, 61 (70%) had no documented approval prior to deployment to production. Changes were deployed directly by engineers without peer review or CAB approval. No change management policy or procedure was in place.

**Criteria:**  
SOC 2 CC8.1 requires that changes to infrastructure and software are authorized, tested, and approved prior to deployment. COBIT 2019 BAI06 (Managed IT Changes) requires formal change authorization.

**Cause:**  
The organization relies on developer judgment for deployment decisions. No change management tool or process has been formalized. Rapid startup growth has prioritized velocity over governance.

**Effect:**  
Unauthorized or untested changes could introduce security vulnerabilities, cause service disruptions, or create audit trail gaps that would be identified as exceptions by SOC 2 auditors. High risk of undetected unauthorized changes.

**Recommendation:**  
1. Implement a formal change management policy within 30 days
2. Configure Jira or ServiceNow for mandatory change ticket creation and approval workflow
3. Establish a lightweight Change Advisory Board (CAB) for significant changes
4. Require peer approval for all production deployments (enforced in GitHub branch protection rules)

**Management Response:**  
*[To be completed by IT Manager — due August 15, 2025]*

**Target Remediation Date:** September 30, 2025

---

### FIND-002 — Stale User Accounts Not Deprovisioned
**Severity:** 🔴 High | **Domain:** Logical Access Management | **Status:** Open

**Condition:**  
A review of Okta user accounts against the active employee list from BambooHR identified 23 accounts belonging to former employees that remained active in Okta. Account ages ranged from 14 to 287 days past termination date. Of these, 11 accounts still had active sessions within the past 90 days.

**Criteria:**  
SOC 2 CC6.2 and CC6.3 require that access is provisioned and de-provisioned in a timely manner. ISO 27001 control 5.18 requires access rights to be removed upon termination.

**Cause:**  
The offboarding process relies on a manual BambooHR notification to IT. Review of 8 termination events found that IT was not notified in 5 cases. No automated integration exists between HRIS and Okta. No periodic access review was conducted during the audit period.

**Effect:**  
Former employees with active accounts could access company systems, customer data, or proprietary information. This represents a significant insider threat and data breach risk. Active sessions in 11 accounts indicate potential unauthorized access occurred.

**Recommendation:**  
1. Immediately disable all 23 identified stale accounts and investigate the 11 with active sessions
2. Implement automated HRIS-to-Okta deprovisioning integration (API or SCIM)
3. Set target SLA of same-day deprovisioning for all terminations
4. Conduct quarterly user access reviews and document results
5. Implement Joiner-Mover-Leaver (JML) process with formal sign-off

**Management Response:**  
*[To be completed by IT Manager — due August 15, 2025]*

**Target Remediation Date:** August 31, 2025 (immediate action on stale accounts: August 1)

---

### FIND-003 — No SIEM — Security Events Not Logged Centrally
**Severity:** 🔴 High | **Domain:** Incident Management / Monitoring | **Status:** Open

**Condition:**  
The organization has no Security Information and Event Management (SIEM) system. Application logs exist in AWS CloudWatch but are siloed per service, not correlated, and not monitored in real time. No alerting rules are configured. During the audit period, 4 security incidents were logged — all were identified by users, not by automated monitoring.

**Criteria:**  
SOC 2 CC7.2 requires monitoring of system components for anomalous behavior. ISO 27001 controls 8.15 (Logging) and 8.16 (Monitoring Activities) require centralized log management and monitoring. NIST CSF DE.CM requires continuous monitoring capability.

**Cause:**  
SIEM procurement was deprioritized due to cost and resource constraints. Engineering team has focused on product delivery rather than security monitoring infrastructure.

**Effect:**  
Without centralized logging and monitoring, security incidents may go undetected for extended periods, forensic investigation is impaired, and compliance with SOC 2 and ISO 27001 monitoring controls cannot be demonstrated.

**Recommendation:**  
1. Select and deploy a SIEM solution (e.g., Microsoft Sentinel, Splunk, Elastic SIEM) within 90 days
2. Configure log ingestion from all in-scope systems (AWS, Okta, GitHub, application logs)
3. Define and implement baseline alerting rules (failed logins, privilege escalation, data exfiltration indicators)
4. Establish on-call rotation for alert triage
5. Define log retention period (minimum 12 months for SOC 2 / ISO 27001)

**Management Response:**  
*[To be completed by CISO — due August 15, 2025]*

**Target Remediation Date:** October 31, 2025

---

### FIND-004 — Three Former Employee Accounts Active in Production Systems
**Severity:** 🔴 High | **Domain:** Logical Access Management | **Status:** Open

**Condition:**  
In addition to the 23 stale Okta accounts identified in FIND-002, direct review of production AWS IAM users and GitHub organization members identified 3 additional former employee accounts with access not captured in Okta (service accounts created manually). Two accounts had AWS programmatic access keys that had been used within the past 30 days.

**Criteria:**  
SOC 2 CC6.3 requires that access is removed when no longer needed. ISO 27001 control 8.2 requires that privileged access rights are managed and reviewed regularly.

**Cause:**  
These accounts were created directly in AWS IAM and GitHub outside of the standard Okta provisioning workflow. They were not covered by the Okta-based offboarding checklist and therefore not detected or removed.

**Effect:**  
Active programmatic access keys used by former employees represent a critical unauthorized access risk. Attackers who compromised former employee credentials could leverage these keys to access production systems. The 30-day activity suggests potential unauthorized use that must be investigated.

**Recommendation:**  
1. **Immediately** disable all three accounts and rotate affected AWS access keys
2. Initiate security investigation into the access key activity within the past 30 days
3. Implement requirement that all user accounts must be provisioned via Okta (eliminate direct IAM user creation)
4. Add AWS IAM and GitHub organization to quarterly access review scope
5. Deploy automated orphan account detection tooling

**Management Response:**  
*[To be completed by CISO — due August 15, 2025]*

**Target Remediation Date:** Immediate (accounts) — August 1, 2025; Systemic fix — September 30, 2025

---

### FIND-005 — Backup Restoration Not Tested
**Severity:** 🟠 Medium | **Domain:** Backup & Recovery | **Status:** Open

**Condition:**  
AWS automated backups are configured and running for production databases (verified via backup logs). However, no backup restoration test has been performed in the past 18 months. No documentation of a successful restoration exists.

**Criteria:**  
SOC 2 A1.2 requires that recovery procedures are documented and tested. ISO 27001 control 8.13 requires backup testing. NIST CSF RC.RP requires recovery plans to be executed and validated.

**Cause:**  
Restoration testing has not been prioritized; no formal backup testing schedule exists.

**Effect:**  
Without tested restoration capability, backups may fail during actual recovery events, resulting in data loss or extended outages. This would also be noted as a SOC 2 exception.

**Recommendation:**  
1. Schedule and conduct a full backup restoration test within 60 days
2. Document restoration test results (time taken, data integrity verified, issues encountered)
3. Establish a quarterly restoration testing schedule
4. Define RTO/RPO targets and validate backups can meet them

**Target Remediation Date:** September 30, 2025

---

### FIND-006 — Critical Patches Not Applied Within SLA
**Severity:** 🟠 Medium | **Domain:** Vulnerability Management | **Status:** Open

**Condition:**  
Review of vulnerability scan reports and patch tickets for the audit period identified 6 critical-severity vulnerabilities (CVSS ≥ 9.0) that were not remediated within 30 days of identification. Average time to patch for critical vulnerabilities was 54 days. No formal patch SLA policy exists.

**Criteria:**  
ISO 27001 control 8.8 requires that technical vulnerabilities are managed in a timely manner. SOC 2 CC7.1 requires monitoring of system configurations. Industry best practice requires critical vulnerabilities to be patched within 15–30 days.

**Cause:**  
No patch management policy or SLA has been defined. Patching is handled ad hoc by the engineering team alongside product development work.

**Recommendation:**  
1. Define and approve a patch management policy with tiered SLAs (Critical: 15 days, High: 30 days, Medium: 90 days)
2. Implement automated patch management tooling
3. Track patch compliance in a vulnerability management dashboard
4. Escalate SLA breaches to CISO weekly

**Target Remediation Date:** October 31, 2025

---

### FIND-007 — Vendor Contracts Lack Security SLAs
**Severity:** 🟠 Medium | **Domain:** Third-Party / Vendor Management | **Status:** Open

**Condition:**  
Review of contracts for the 12 Tier 1 vendors (those processing or storing customer data) found that 9 of 12 contracts (75%) contain no security-specific SLAs, right-to-audit clauses, or incident notification requirements. Only 3 vendors have provided SOC 2 reports.

**Criteria:**  
ISO 27001 controls 5.19–5.22 require supplier security to be addressed in agreements. SOC 2 CC9.2 requires assessment and management of vendor risks.

**Recommendation:**  
1. Update all Tier 1 vendor contracts to include security SLAs, incident notification requirements (72-hour breach notification), and right-to-audit clauses at next renewal
2. Require SOC 2 reports (or equivalent) from all Tier 1 vendors annually
3. Implement vendor tiering and risk questionnaire process

**Target Remediation Date:** December 31, 2025

---

### FIND-008 — Security Training Completion Not Tracked in LMS *(Remediated)*
**Severity:** 🟢 Low | **Domain:** Security Awareness | **Status:** ✅ Remediated

**Condition (at time of fieldwork):**  
Security awareness training was assigned via email links rather than LMS, making completion tracking impossible. No completion records existed.

**Remediation:**  
During audit fieldwork, the organization migrated training to its LMS (Workday Learning). Completion tracking is now enabled. Completion rate as of July 15, 2025: 91%.

**Auditor Note:**  
Confirm 100% completion and implement escalation for non-completers. Consider quarterly phishing simulations as enhancement.

---

## Finding Summary Tracker

| Finding | Severity | Domain | Owner | Due Date | Status |
|---------|----------|--------|-------|----------|--------|
| FIND-001 | 🔴 High | Change Management | IT Manager | Sep 30, 2025 | Open |
| FIND-002 | 🔴 High | Access Management | IT Manager | Aug 31, 2025 | Open |
| FIND-003 | 🔴 High | Monitoring | CISO | Oct 31, 2025 | Open |
| FIND-004 | 🔴 High | Access Management | CISO | Aug 1 / Sep 30, 2025 | Open — Urgent |
| FIND-005 | 🟠 Medium | Backup & Recovery | CTO | Sep 30, 2025 | Open |
| FIND-006 | 🟠 Medium | Vuln. Management | IT Ops | Oct 31, 2025 | Open |
| FIND-007 | 🟠 Medium | Vendor Management | GRC Analyst | Dec 31, 2025 | Open |
| FIND-008 | 🟢 Low | Security Awareness | HR | — | ✅ Remediated |

---

## Auditor Sign-off

| Role | Name | Date |
|------|------|------|
| Lead Auditor | GRC Analyst | July 31, 2025 |
| Audit Sponsor (CISO) | | |
| Audit Committee Chair | | |

*This report represents the findings of an internal audit conducted for governance and improvement purposes. It does not constitute an external assurance opinion.*
