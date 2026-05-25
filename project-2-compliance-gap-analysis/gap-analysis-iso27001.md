# ISO 27001:2022 — Annex A Controls Gap Analysis

**Organization:** SaaS Co. | **Assessment Date:** Q2 2025  
**Standard:** ISO/IEC 27001:2022 | **Assessor:** GRC Analyst

---

## Assessment Key

| Status | Symbol | Meaning |
|--------|--------|---------|
| Implemented | ✅ | Control fully in place and effective |
| Partial | 🟡 | Control exists but has gaps or is inconsistently applied |
| Not Implemented | ❌ | Control absent or entirely ineffective |

**Priority:** 🔴 High (cert blocker) | 🟠 Medium | 🟢 Low

---

## 5. Organizational Controls

| # | Control | Status | Gap Description | Priority |
|---|---------|--------|----------------|----------|
| 5.1 | Policies for information security | 🟡 Partial | Policy exists but not reviewed in 2 years; missing BYOD and data classification policies | 🔴 High |
| 5.2 | Information security roles and responsibilities | 🟡 Partial | CISO assigned; no documented security responsibilities for non-IT roles | 🟠 Medium |
| 5.3 | Segregation of duties | ✅ Implemented | Developer/admin roles separated; reviewed quarterly | — |
| 5.4 | Management responsibilities | 🟡 Partial | Verbal commitment from leadership; no formal management review documented | 🟠 Medium |
| 5.5 | Contact with authorities | ❌ Not Implemented | No process for contacting law enforcement or regulators during incidents | 🔴 High |
| 5.6 | Contact with special interest groups | ❌ Not Implemented | Not subscribed to threat intel feeds or ISACs | 🟠 Medium |
| 5.7 | Threat intelligence | ❌ Not Implemented | No formal threat intelligence program | 🟠 Medium |
| 5.8 | Information security in project management | 🟡 Partial | Security review not consistently included in project lifecycle | 🔴 High |
| 5.9 | Inventory of information and other assets | 🟡 Partial | Asset inventory exists but incomplete; cloud assets not catalogued | 🔴 High |
| 5.10 | Acceptable use of assets | ✅ Implemented | AUP in place, signed by all employees at onboarding | — |
| 5.11 | Return of assets | 🟡 Partial | Offboarding checklist exists; device return not always verified | 🟠 Medium |
| 5.12 | Classification of information | ❌ Not Implemented | No data classification policy or labelling scheme | 🔴 High |
| 5.13 | Labelling of information | ❌ Not Implemented | No labelling standards or tooling | 🔴 High |
| 5.14 | Information transfer | 🟡 Partial | Encryption in transit; no formal data transfer agreements with partners | 🟠 Medium |
| 5.15 | Access control | ✅ Implemented | RBAC enforced; access reviews quarterly | — |
| 5.16 | Identity management | ✅ Implemented | SSO + MFA deployed; centralized IAM | — |
| 5.17 | Authentication information | ✅ Implemented | Password policy enforced via IdP; no shared credentials | — |
| 5.18 | Access rights | 🟡 Partial | Access provisioning process documented; de-provisioning timing inconsistent | 🟠 Medium |
| 5.19 | Information security in supplier relationships | ❌ Not Implemented | No formal supplier security policy; no standardized vendor questionnaire | 🔴 High |
| 5.20 | Addressing security within supplier agreements | 🟡 Partial | Basic DPAs in place; no security SLAs or right-to-audit clauses | 🔴 High |
| 5.21 | Managing security in the ICT supply chain | ❌ Not Implemented | No software supply chain risk process | 🔴 High |
| 5.22 | Monitoring and review of supplier services | ❌ Not Implemented | No annual supplier review process or performance tracking | 🔴 High |
| 5.23 | Security for use of cloud services | 🟡 Partial | Cloud used widely; no formal cloud security policy or CASB | 🟠 Medium |
| 5.24 | Information security incident management planning | 🟡 Partial | Incident response plan drafted but not tested or approved | 🔴 High |
| 5.25 | Assessment and decision on events | 🟡 Partial | Informal triage; no documented classification criteria | 🟠 Medium |
| 5.26 | Response to incidents | 🟡 Partial | IRP exists; runbooks absent for key scenarios | 🔴 High |
| 5.27 | Learning from incidents | ❌ Not Implemented | No post-incident review process | 🟠 Medium |
| 5.28 | Collection of evidence | ❌ Not Implemented | No forensic evidence handling procedure | 🟠 Medium |
| 5.29 | Business continuity | 🟡 Partial | BCP exists; not tested in 18 months | 🔴 High |
| 5.30 | ICT readiness for business continuity | ❌ Not Implemented | No DR plan; RTO/RPO targets undefined | 🔴 High |

---

## 6. People Controls

| # | Control | Status | Gap Description | Priority |
|---|---------|--------|----------------|----------|
| 6.1 | Screening | ✅ Implemented | Background checks run for all employees | — |
| 6.2 | Terms and conditions of employment | ✅ Implemented | Confidentiality agreements and AUP signed at hire | — |
| 6.3 | Information security awareness, training | 🟡 Partial | Annual training in place; no role-based training for privileged users | 🟠 Medium |
| 6.4 | Disciplinary process | ✅ Implemented | HR policy covers security violations | — |
| 6.5 | Responsibilities after termination | 🟡 Partial | Offboarding checklist; access revocation timing inconsistent | 🟠 Medium |
| 6.6 | Confidentiality agreements | ✅ Implemented | NDAs signed by all staff and contractors | — |
| 6.7 | Remote working | 🟡 Partial | Remote work allowed; no formal remote work security policy | 🟠 Medium |
| 6.8 | Information security event reporting | 🟡 Partial | Reporting channel exists; not well-communicated to staff | 🟠 Medium |

---

## 7. Physical Controls

| # | Control | Status | Gap Description | Priority |
|---|---------|--------|----------------|----------|
| 7.1 | Physical security perimeters | ✅ Implemented | Office access badge controlled | — |
| 7.2 | Physical entry | ✅ Implemented | Visitor log maintained | — |
| 7.3 | Securing offices, rooms, facilities | ✅ Implemented | Server room locked; badge access controlled | — |
| 7.4 | Physical security monitoring | 🟡 Partial | CCTV at entry points; no coverage of server room | 🟠 Medium |
| 7.5 | Protection against physical threats | ✅ Implemented | Fire suppression and UPS in place | — |
| 7.6 | Working in secure areas | ✅ Implemented | Clean desk policy enforced | — |
| 7.7 | Clear desk and screen | ✅ Implemented | Policy in place; compliance spot-checked | — |
| 7.8 | Equipment siting and protection | ✅ Implemented | Equipment in rack cabinets; no consumer-grade equipment in prod | — |
| 7.9 | Security of assets off-premises | 🟡 Partial | Laptop encryption enforced; no MDM for mobile devices | 🟠 Medium |
| 7.10 | Storage media | 🟡 Partial | No formal media disposal or sanitisation procedure | 🟠 Medium |
| 7.11 | Supporting utilities | ✅ Implemented | UPS and generator in place for server room | — |
| 7.12 | Cabling security | ✅ Implemented | Structured cabling documented | — |
| 7.13 | Equipment maintenance | 🟡 Partial | Ad hoc maintenance; no formal schedule | 🟢 Low |
| 7.14 | Secure disposal of equipment | 🟡 Partial | Devices wiped before disposal; no certificate of destruction | 🟠 Medium |

---

## 8. Technological Controls (Sample)

| # | Control | Status | Gap Description | Priority |
|---|---------|--------|----------------|----------|
| 8.1 | User endpoint devices | ✅ Implemented | MDM on laptops; mobile policy gap | — |
| 8.2 | Privileged access rights | 🟡 Partial | PAM not deployed; admin accounts not regularly reviewed | 🔴 High |
| 8.3 | Information access restriction | ✅ Implemented | RBAC in production systems | — |
| 8.4 | Access to source code | ✅ Implemented | Source code access restricted by role in GitHub | — |
| 8.5 | Secure authentication | ✅ Implemented | MFA enforced on all critical systems | — |
| 8.6 | Capacity management | 🟡 Partial | Cloud auto-scaling in place; no formal capacity review process | 🟢 Low |
| 8.7 | Protection against malware | ✅ Implemented | EDR deployed on all endpoints | — |
| 8.8 | Management of technical vulnerabilities | 🟡 Partial | Vulnerability scanner deployed; no formal patch SLA | 🔴 High |
| 8.9 | Configuration management | 🟡 Partial | IaC used; no configuration baseline documentation | 🟠 Medium |
| 8.15 | Logging | ❌ Not Implemented | No SIEM; application logs not centralised | 🔴 High |
| 8.16 | Monitoring activities | ❌ Not Implemented | No real-time monitoring or alerting | 🔴 High |
| 8.20 | Networks security | ✅ Implemented | Firewalls, VPN, network segmentation in place | — |
| 8.25 | Secure development lifecycle | 🟡 Partial | SAST tool in CI/CD; no formal SDLC security policy | 🔴 High |
| 8.28 | Secure coding | 🟡 Partial | Internal guidelines exist; not formally documented or trained | 🟠 Medium |

---

## Summary Scorecard

| Annex A Section | Total Controls | ✅ Implemented | 🟡 Partial | ❌ Not Implemented |
|----------------|---------------|--------------|-----------|------------------|
| 5. Organizational | 37 | 11 (30%) | 17 (46%) | 9 (24%) |
| 6. People | 8 | 4 (50%) | 4 (50%) | 0 |
| 7. Physical | 14 | 9 (64%) | 5 (36%) | 0 |
| 8. Technological | 34 | 14 (41%) | 12 (35%) | 8 (24%) |
| **Total** | **93** | **38 (41%)** | **38 (41%)** | **17 (18%)** |

---

## Priority Remediation Items (Cert Blockers)

1. **Data classification policy + labelling** (5.12, 5.13) — Required for ISMS scope definition
2. **SIEM / centralised logging** (8.15, 8.16) — Fundamental detection capability
3. **Supplier security program** (5.19–5.22) — Common audit finding
4. **Incident management plan — test + approve** (5.24, 5.26)
5. **DR plan with defined RTO/RPO** (5.30)
