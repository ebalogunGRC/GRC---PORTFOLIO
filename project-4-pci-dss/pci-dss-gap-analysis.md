# PCI DSS v4.0 — Gap Analysis
**Organization:** PayTech Co. | **Assessment Date:** Q2 2025  
**Standard:** PCI DSS v4.0 | **Merchant Level:** Level 1 | **Assessor:** GRC Analyst

---

## Assessment Key

| Status | Symbol | Meaning |
|--------|--------|---------|
| In Place | ✅ | Control fully implemented and effective |
| Partial | 🟡 | Control exists but has gaps |
| Not In Place | ❌ | Control absent or ineffective |

**Priority:** 🔴 RoC Blocker | 🟠 High | 🟡 Medium | 🟢 Low

---

## Requirement 1 — Install and Maintain Network Security Controls

| Sub-Req | Description | Status | Gap | Priority |
|---------|-------------|--------|-----|----------|
| 1.1 | Network security control processes documented and operational | 🟡 Partial | Firewall rules exist; no formal review process documented | 🔴 RoC Blocker |
| 1.2 | Network security controls configured to restrict inbound/outbound traffic | 🟡 Partial | Default-deny not enforced on all CDE-facing rules | 🔴 RoC Blocker |
| 1.3 | Network access to/from the CDE is restricted | 🟡 Partial | CDE not fully segmented from corporate network | 🔴 RoC Blocker |
| 1.4 | Network connections between trusted and untrusted networks controlled | ✅ In Place | DMZ implemented; firewall between internet and CDE | — |
| 1.5 | Security controls for managing network connections | 🟡 Partial | No formal process to review firewall rules every 6 months | 🟠 High |

**Remediation Priority:** Network segmentation between CDE and corporate network is the single most impactful fix — will reduce scope and control requirements significantly.

---

## Requirement 2 — Apply Secure Configurations to All System Components

| Sub-Req | Description | Status | Gap | Priority |
|---------|-------------|--------|-----|----------|
| 2.1 | Configuration standards developed and implemented | 🟡 Partial | Standards exist for servers; not documented for network devices | 🔴 RoC Blocker |
| 2.2 | System components configured and managed securely | 🟡 Partial | Hardening applied inconsistently; no baseline config documented | 🔴 RoC Blocker |
| 2.3 | Wireless environments secured | ✅ In Place | No wireless in CDE; office WiFi on separate VLAN | — |
| 2.4 | Inventory of system components in scope maintained | ❌ Not In Place | No formal CDE asset inventory; cloud assets not catalogued | 🔴 RoC Blocker |
| 2.5 | Security policies for managing vendor defaults | 🟡 Partial | Default passwords changed; process not documented | 🟠 High |
| 2.6 | Shared hosting providers protect the CDE | ✅ In Place | AWS used; AWS PCI DSS AOC obtained | — |

---

## Requirement 3 — Protect Stored Account Data

| Sub-Req | Description | Status | Gap | Priority |
|---------|-------------|--------|-----|----------|
| 3.1 | Processes and mechanisms for protecting stored data defined | 🟡 Partial | Data retention policy exists; no formal destruction schedule | 🔴 RoC Blocker |
| 3.2 | Storage of sensitive authentication data (SAD) minimized | ✅ In Place | CVV/CVC not stored post-authorization (confirmed via code review) | — |
| 3.3 | SAD not retained after authorization | ✅ In Place | Payment gateway confirmed; verified via penetration test | — |
| 3.4 | Primary Account Numbers (PAN) secured | 🟡 Partial | PANs tokenized for most flows; 2 legacy systems store PANs in plain text | 🔴 RoC Blocker |
| 3.5 | PAN secured with strong cryptography | 🟡 Partial | AES-256 used in new systems; legacy systems use outdated encryption | 🔴 RoC Blocker |
| 3.6 | Cryptographic keys managed securely | 🟡 Partial | Keys stored in AWS KMS; no formal key management policy | 🟠 High |
| 3.7 | Key management policies and procedures | ❌ Not In Place | No documented key management lifecycle (generation, rotation, retirement) | 🔴 RoC Blocker |

---

## Requirement 4 — Protect Cardholder Data with Strong Cryptography During Transmission

| Sub-Req | Description | Status | Gap | Priority |
|---------|-------------|--------|-----|----------|
| 4.1 | Processes for protecting CHD in transit defined | ✅ In Place | TLS policy documented and enforced | — |
| 4.2 | PAN protected with strong cryptography during transmission | ✅ In Place | TLS 1.2+ enforced on all payment flows; TLS 1.0/1.1 disabled | — |
| 4.3 | Certificates and keys managed | ✅ In Place | AWS Certificate Manager used; auto-renewal configured | — |

**Result: Requirement 4 fully met — no gaps.**

---

## Requirement 5 — Protect All Systems and Networks from Malicious Software

| Sub-Req | Description | Status | Gap | Priority |
|---------|-------------|--------|-----|----------|
| 5.1 | Anti-malware solution deployed | ✅ In Place | CrowdStrike EDR on all CDE endpoints | — |
| 5.2 | Anti-malware mechanisms active and monitored | ✅ In Place | Real-time scanning enabled; alerts configured | — |
| 5.3 | Anti-malware mechanisms kept current | ✅ In Place | Automatic definition updates; verified via console | — |
| 5.4 | Phishing and social engineering attacks addressed | 🟡 Partial | Email filtering in place; no formal anti-phishing training program | 🟡 Medium |

---

## Requirement 6 — Develop and Maintain Secure Systems and Software

| Sub-Req | Description | Status | Gap | Priority |
|---------|-------------|--------|-----|----------|
| 6.1 | Security vulnerabilities identified and addressed | 🟡 Partial | Vulnerability scanning in place; no formal patch SLA | 🟠 High |
| 6.2 | Bespoke software developed securely | 🟡 Partial | SAST tool in CI/CD; no formal SDLC security policy | 🔴 RoC Blocker |
| 6.3 | Security vulnerabilities identified and protected | 🟡 Partial | Critical patches delayed beyond 30-day target in 4 cases | 🟠 High |
| 6.4 | Public-facing web applications protected | 🟡 Partial | WAF deployed; not configured for all payment-facing endpoints | 🔴 RoC Blocker |
| 6.5 | Changes to all system components managed securely | ❌ Not In Place | No formal change management process for CDE systems | 🔴 RoC Blocker |

---

## Requirement 7 — Restrict Access to System Components and Cardholder Data by Business Need to Know

| Sub-Req | Description | Status | Gap | Priority |
|---------|-------------|--------|-----|----------|
| 7.1 | Access control model defined and implemented | ✅ In Place | RBAC documented and enforced; least privilege applied | — |
| 7.2 | Access to system components and data is appropriately defined | ✅ In Place | Access matrix documented for all CDE roles | — |
| 7.3 | Access to system components and data managed via access control system | ✅ In Place | Okta enforces access; quarterly reviews conducted | — |

**Result: Requirement 7 fully met — no gaps.**

---

## Requirement 8 — Identify Users and Authenticate Access to System Components

| Sub-Req | Description | Status | Gap | Priority |
|---------|-------------|--------|-----|----------|
| 8.1 | Processes for user identification and authentication | 🟡 Partial | Policy exists; shared accounts still used in 2 legacy applications | 🔴 RoC Blocker |
| 8.2 | All user IDs and authentication factors managed securely | 🟡 Partial | SSO via Okta; service accounts not rotated on schedule | 🟠 High |
| 8.3 | User authentication implemented using MFA | 🟡 Partial | MFA on Okta; not enforced for direct database access | 🔴 RoC Blocker |
| 8.4 | MFA implemented for all access into the CDE | ❌ Not In Place | 3 admin accounts access CDE without MFA via legacy jump server | 🔴 RoC Blocker |
| 8.5 | Application and system accounts managed and authenticated | 🟡 Partial | Service accounts inventoried; passwords not rotated annually | 🟠 High |
| 8.6 | Use of application and system accounts controlled | 🟡 Partial | No PAM tool; privileged session recording not in place | 🟠 High |

---

## Requirement 9 — Restrict Physical Access to Cardholder Data

| Sub-Req | Description | Status | Gap | Priority |
|---------|-------------|--------|-----|----------|
| 9.1 | Physical security controls for CDE | ✅ In Place | AWS data center physical controls; AWS AOC covers this | — |
| 9.2 | Physical access controls for on-site CDE | ✅ In Place | Server room badge-access only; CCTV monitored | — |
| 9.3 | Physical access for personnel and visitors managed | ✅ In Place | Visitor log maintained; escorts required | — |
| 9.4 | Media with cardholder data secured | ✅ In Place | No removable media in CDE; USB ports disabled | — |
| 9.5 | Point-of-interaction devices protected | ✅ In Place | No POI devices — card-not-present environment only | — |

**Result: Requirement 9 fully met — no gaps.**

---

## Requirement 10 — Log and Monitor All Access to System Components and Cardholder Data

| Sub-Req | Description | Status | Gap | Priority |
|---------|-------------|--------|-----|----------|
| 10.1 | Logging and monitoring implemented | ❌ Not In Place | No SIEM; logs exist in CloudWatch but not centralised or monitored | 🔴 RoC Blocker |
| 10.2 | Audit logs capture required events | ❌ Not In Place | Logging not configured for all required event types (failed logins, privilege use) | 🔴 RoC Blocker |
| 10.3 | Audit logs protected from destruction and modification | 🟡 Partial | CloudWatch logs enabled; no immutable log storage configured | 🔴 RoC Blocker |
| 10.4 | Audit logs reviewed to identify anomalies | ❌ Not In Place | No log review process; no automated alerting | 🔴 RoC Blocker |
| 10.5 | Audit log history retained for at least 12 months | ❌ Not In Place | Current retention: 30 days only | 🔴 RoC Blocker |
| 10.6 | Time synchronization mechanisms | 🟡 Partial | NTP configured; not consistent across all CDE systems | 🟠 High |
| 10.7 | Failures of security controls detected and addressed | ❌ Not In Place | No automated detection of security control failures | 🔴 RoC Blocker |

**Remediation Priority: CRITICAL — Requirement 10 is the most significant gap. A SIEM must be deployed before RoC can be achieved.**

---

## Requirement 11 — Test Security of Systems and Networks Regularly

| Sub-Req | Description | Status | Gap | Priority |
|---------|-------------|--------|-----|----------|
| 11.1 | Processes and mechanisms for testing defined | 🟡 Partial | Pen test conducted annually; no formal testing policy | 🟠 High |
| 11.2 | Wireless access points managed and tested | ✅ In Place | No wireless in CDE; quarterly rogue AP scans performed | — |
| 11.3 | External and internal vulnerabilities managed | 🟡 Partial | Quarterly ASV scans conducted; internal scans ad hoc | 🟠 High |
| 11.4 | External and internal penetration testing | 🟡 Partial | Annual pen test completed; remediation tracking informal | 🟠 High |
| 11.5 | Network intrusion detection/prevention deployed | ❌ Not In Place | No IDS/IPS on CDE network segments | 🔴 RoC Blocker |
| 11.6 | Unauthorised changes to payment pages detected | 🟡 Partial | No change detection mechanism on payment pages | 🟠 High |

---

## Requirement 12 — Support Information Security with Organizational Policies and Programs

| Sub-Req | Description | Status | Gap | Priority |
|---------|-------------|--------|-----|----------|
| 12.1 | Comprehensive information security policy | 🟡 Partial | Policy exists; not reviewed in 18 months | 🔴 RoC Blocker |
| 12.2 | Acceptable use policies for end-user technologies | ✅ In Place | AUP signed by all staff | — |
| 12.3 | Risks to the CDE formally identified and managed | 🟡 Partial | Risk register exists; not formally tied to PCI DSS scope | 🟠 High |
| 12.4 | PCI DSS compliance managed | 🟡 Partial | No formal compliance officer assigned to PCI program | 🟠 High |
| 12.5 | PCI DSS scope documented and validated | 🟡 Partial | Scope defined; not formally reviewed annually | 🔴 RoC Blocker |
| 12.6 | Security awareness education program | 🟡 Partial | Annual training; no PCI-specific training module | 🟠 High |
| 12.7 | Personnel screened before access to CDE | ✅ In Place | Background checks run for all CDE-access staff | — |
| 12.8 | Risk from third-party service providers managed | ❌ Not In Place | No formal TPRM; no PCI DSS compliance confirmation from vendors | 🔴 RoC Blocker |
| 12.9 | Third-party service providers acknowledge responsibility | ❌ Not In Place | No acknowledgment agreements with payment vendors | 🔴 RoC Blocker |
| 12.10 | Suspected and confirmed incidents responded to | 🟡 Partial | IRP exists; no PCI-specific incident response procedure | 🟠 High |

---

## PCI DSS Compliance Scorecard

| Requirement | Total Sub-Reqs | ✅ In Place | 🟡 Partial | ❌ Not In Place |
|-------------|---------------|-----------|-----------|----------------|
| 1 — Network Security | 5 | 1 | 4 | 0 |
| 2 — Secure Config | 6 | 2 | 3 | 1 |
| 3 — Stored Data | 7 | 2 | 4 | 1 |
| 4 — Data in Transit | 3 | 3 | 0 | 0 |
| 5 — Malware | 4 | 3 | 1 | 0 |
| 6 — Secure Dev | 5 | 0 | 3 | 2 |
| 7 — Access Control | 3 | 3 | 0 | 0 |
| 8 — Authentication | 6 | 0 | 4 | 2 |
| 9 — Physical Access | 5 | 5 | 0 | 0 |
| 10 — Logging | 7 | 0 | 1 | 6 |
| 11 — Testing | 6 | 1 | 4 | 1 |
| 12 — Policy | 10 | 2 | 6 | 2 |
| **Total** | **67** | **22 (33%)** | **30 (45%)** | **15 (22%)** |

---

## Top 5 Remediation Priorities Before QSA Engagement

| # | Action | Requirement | Timeline |
|---|--------|------------|----------|
| 1 | Deploy SIEM with 12-month log retention | Req 10 | 90 days |
| 2 | Implement network segmentation for CDE | Req 1, 1.3 | 60 days |
| 3 | Eliminate shared accounts; enforce MFA on all CDE access | Req 8 | 45 days |
| 4 | Tokenize remaining legacy PAN storage | Req 3 | 90 days |
| 5 | Build third-party PCI DSS acknowledgment program | Req 12.8, 12.9 | 60 days |
