# HIPAA Security Rule — 12-Month Compliance Roadmap
**Organization:** HealthStart Co. | **Period:** Q3 2025 – Q2 2026  
**Goal:** HIPAA Security Rule compliance across all safeguards  
**Owner:** GRC Team | **Sponsor:** CEO / Privacy Officer

---

## Overview

```
Q3 2025 (Jul–Sep): FOUNDATION — SRA, BAAs, critical policy gaps
Q4 2025 (Oct–Dec): TECHNICAL CONTROLS — encryption, logging, MFA
Q1 2026 (Jan–Mar): TRAINING, DR & TESTING
Q2 2026 (Apr–Jun): AUDIT READINESS & ONGOING COMPLIANCE
```

---

## Phase 1 — Foundation (Q3 2025: Jul–Sep)

| # | Action | HIPAA Ref | Owner | Due | Priority |
|---|--------|-----------|-------|-----|----------|
| 1.1 | Complete and formally document Security Risk Assessment (this document) | §164.308(a)(1) | GRC Analyst | Jul 31 | 🔴 Critical |
| 1.2 | Execute BAAs with all 14 business associates lacking agreements | §164.314(a) | Legal + GRC | Aug 15 | 🔴 Critical |
| 1.3 | Review and update BAAs for remaining 14 business associates | §164.314(a) | Legal | Sep 30 | 🔴 Critical |
| 1.4 | Designate and formally document HIPAA Security Officer and Privacy Officer | §164.308(a)(2) | CEO | Jul 15 | 🟠 High |
| 1.5 | Develop HIPAA Sanctions Policy | §164.308(a)(1)(ii)(C) | HR + GRC | Aug 31 | 🟠 High |
| 1.6 | Develop and publish Breach Notification Procedure | §164.308(a)(6) | GRC + Legal | Aug 31 | 🔴 Critical |
| 1.7 | Ban PHI transmission via Slack — communicate policy to all staff | §164.312 | CISO + HR | Jul 15 | 🔴 Critical |
| 1.8 | Evaluate and onboard HIPAA-compliant messaging platform (e.g., TigerConnect, Klara) | §164.312 | Engineering | Sep 30 | 🔴 Critical |
| 1.9 | Develop Risk Management Plan based on SRA findings | §164.308(a)(1)(ii)(B) | GRC Analyst | Aug 31 | 🔴 Critical |

---

## Phase 2 — Technical Controls (Q4 2025: Oct–Dec)

| # | Action | HIPAA Ref | Owner | Due | Priority |
|---|--------|-----------|-------|-----|----------|
| 2.1 | Enforce MFA on Google Workspace for all staff | §164.312(d) | IT Manager | Oct 15 | 🔴 Critical |
| 2.2 | Deploy centralized audit logging for all ePHI access (SIEM) | §164.312(b) | Engineering | Nov 30 | 🔴 Critical |
| 2.3 | Encrypt ePHI at rest on all remaining systems (AWS, legacy file server) | §164.312(a)(2)(iv) | Cloud Engineer | Nov 30 | 🔴 Critical |
| 2.4 | Migrate legacy on-premise file server to encrypted cloud storage | §164.312(a)(2)(iv) | IT Manager | Dec 15 | 🟠 High |
| 2.5 | Implement automatic session logoff on all ePHI systems | §164.312(a)(2)(iii) | Engineering | Oct 31 | 🟡 Medium |
| 2.6 | Implement Emergency Access Procedure for ePHI systems | §164.312(a)(2)(ii) | CISO | Nov 30 | 🟠 High |
| 2.7 | Deploy DLP to detect and block PHI in unauthorised channels | §164.312 | CISO | Dec 31 | 🟠 High |
| 2.8 | Automate employee deprovisioning — revoke ePHI access same day | §164.308(a)(3)(ii)(C) | IT Manager | Oct 31 | 🔴 Critical |
| 2.9 | Implement audit log review process — weekly review of ePHI access logs | §164.308(a)(1)(ii)(D) | Security Analyst | Nov 30 | 🟠 High |
| 2.10 | Develop device disposal and media sanitisation procedure | §164.310(d)(1) | IT Manager | Oct 31 | 🟠 High |
| 2.11 | Obtain certificate of destruction process for decommissioned devices | §164.310(d)(1) | IT Manager | Dec 15 | 🟡 Medium |

---

## Phase 3 — Training, DR & Testing (Q1 2026: Jan–Mar)

| # | Action | HIPAA Ref | Owner | Due | Priority |
|---|--------|-----------|-------|-----|----------|
| 3.1 | Develop and deliver HIPAA workforce training — all staff | §164.308(a)(5) | HR + GRC | Jan 31 | 🔴 Critical |
| 3.2 | Develop role-based HIPAA training for clinical staff and admins | §164.308(a)(5) | HR + GRC | Feb 28 | 🟠 High |
| 3.3 | Track and document training completion — 100% required | §164.308(a)(5) | HR | Mar 15 | 🔴 Critical |
| 3.4 | Develop documented Disaster Recovery Plan with RTO/RPO targets | §164.308(a)(7)(ii)(B) | CTO | Jan 31 | 🔴 Critical |
| 3.5 | Conduct and document backup restoration test | §164.308(a)(7)(ii)(A) | Cloud Engineer | Feb 15 | 🔴 Critical |
| 3.6 | Conduct tabletop breach notification exercise | §164.308(a)(6) | GRC + Legal | Feb 28 | 🟠 High |
| 3.7 | Conduct periodic technical evaluation (penetration test) | §164.308(a)(8) | External Pen Tester | Mar 31 | 🟠 High |
| 3.8 | Develop Applications and Data Criticality Analysis | §164.308(a)(7)(ii)(E) | GRC Analyst | Jan 31 | 🟡 Medium |
| 3.9 | Implement security reminder program (quarterly) | §164.308(a)(5)(ii)(A) | CISO | Jan 31 | 🟠 High |

---

## Phase 4 — Audit Readiness & Ongoing Compliance (Q2 2026: Apr–Jun)

| # | Action | HIPAA Ref | Owner | Due | Priority |
|---|--------|-----------|-------|-----|----------|
| 4.1 | Conduct internal HIPAA compliance review across all safeguards | §164.308(a)(8) | GRC Analyst | Apr 30 | 🟠 High |
| 4.2 | Update SRA based on any changes in risk landscape | §164.308(a)(1) | GRC Analyst | Apr 30 | 🔴 Required annually |
| 4.3 | Review and update all HIPAA policies | §164.316(b)(2) | GRC Analyst | May 31 | 🟠 High |
| 4.4 | Confirm all BA agreements current and up to date | §164.314(a) | Legal + GRC | Apr 30 | 🟠 High |
| 4.5 | Establish annual HIPAA compliance review calendar | §164.308(a)(8) | GRC Manager | Jun 30 | 🟡 Medium |
| 4.6 | Submit documentation to Privacy Officer — confirm compliance posture | §164.308 | GRC Analyst | Jun 30 | 🟠 High |

---

## OCR Enforcement Risk Reference

The most common HIPAA enforcement actions by the HHS Office for Civil Rights (OCR):

| Violation | Penalty Range |
|-----------|-------------|
| No Security Risk Assessment | $100 – $50,000 per violation |
| Missing Business Associate Agreements | $100 – $50,000 per violation |
| Insufficient access controls | $100 – $50,000 per violation |
| Failure to encrypt ePHI | $100 – $50,000 per violation |
| No workforce training | $100 – $50,000 per violation |
| **Annual maximum per violation category** | **$1,919,173** |

*Building a documented compliance program significantly reduces penalty exposure even if a breach occurs — demonstrating good faith and due diligence.*
