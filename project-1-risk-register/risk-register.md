# Enterprise Risk Register
**Organization:** FinTech Co. | **Version:** 1.0 | **Last Updated:** Q2 2025  
**Owner:** GRC Team | **Review Cycle:** Quarterly

---

## Risk Register

### RISK-001 — Ransomware Attack on Production Infrastructure
| Field | Detail |
|-------|--------|
| **Domain** | Information Security |
| **Risk Statement** | A ransomware attack encrypts production databases, causing service outage and data loss |
| **Threat Source** | External threat actor (criminal group) |
| **Likelihood** | 4 — Likely |
| **Impact** | 5 — Catastrophic |
| **Inherent Risk Score** | **20 — 🔴 Critical** |
| **Existing Controls** | EDR on endpoints, daily backups, email filtering |
| **Control Effectiveness** | Partial |
| **Residual Risk Score** | **12 — 🟠 High** |
| **Risk Owner** | CISO |
| **Treatment** | Mitigate |
| **Treatment Plan** | Deploy immutable backups, implement network segmentation, conduct ransomware tabletop exercise Q3 2025 |
| **Target Residual Score** | 6 (Medium) by Q4 2025 |

---

### RISK-002 — Third-Party Vendor Data Breach
| Field | Detail |
|-------|--------|
| **Domain** | Third-Party / Supply Chain |
| **Risk Statement** | A key SaaS vendor suffers a breach exposing customer PII shared via API integration |
| **Threat Source** | External — vendor compromise |
| **Likelihood** | 3 — Possible |
| **Impact** | 5 — Catastrophic |
| **Inherent Risk Score** | **15 — 🔴 Critical** |
| **Existing Controls** | Vendor contracts with DPA, annual vendor reviews |
| **Control Effectiveness** | Weak |
| **Residual Risk Score** | **12 — 🟠 High** |
| **Risk Owner** | VP of Procurement |
| **Treatment** | Mitigate |
| **Treatment Plan** | Implement TPRM program, require SOC 2 reports from Tier 1 vendors, deploy CASB tool |
| **Target Residual Score** | 6 (Medium) by Q1 2026 |

---

### RISK-003 — Insider Threat — Privileged Data Exfiltration
| Field | Detail |
|-------|--------|
| **Domain** | Information Security |
| **Risk Statement** | A privileged employee exfiltrates customer financial data before offboarding |
| **Threat Source** | Internal — malicious or negligent employee |
| **Likelihood** | 3 — Possible |
| **Impact** | 5 — Catastrophic |
| **Inherent Risk Score** | **15 — 🔴 Critical** |
| **Existing Controls** | Role-based access control, offboarding checklist |
| **Control Effectiveness** | Partial |
| **Residual Risk Score** | **10 — 🟠 High** |
| **Risk Owner** | CISO / HR Director |
| **Treatment** | Mitigate |
| **Treatment Plan** | Deploy DLP solution, implement PAM tool, enable UEBA alerting, conduct insider threat awareness training |
| **Target Residual Score** | 5 (Medium) by Q3 2025 |

---

### RISK-004 — GDPR Violation — Unlawful Data Processing
| Field | Detail |
|-------|--------|
| **Domain** | Regulatory & Compliance |
| **Risk Statement** | Processing EU customer data without lawful basis or without required consent, resulting in regulatory fine |
| **Threat Source** | Internal process failure |
| **Likelihood** | 3 — Possible |
| **Impact** | 4 — Major |
| **Inherent Risk Score** | **12 — 🟠 High** |
| **Existing Controls** | Privacy policy, consent banners |
| **Control Effectiveness** | Partial |
| **Residual Risk Score** | **9 — 🟠 High** |
| **Risk Owner** | DPO / Legal Counsel |
| **Treatment** | Mitigate |
| **Treatment Plan** | Complete ROPA, conduct data mapping exercise, appoint formal DPO, update consent management platform |
| **Target Residual Score** | 4 (Medium) by Q4 2025 |

---

### RISK-005 — Cloud Misconfiguration Exposing Sensitive Data
| Field | Detail |
|-------|--------|
| **Domain** | Information Security |
| **Risk Statement** | Public S3 bucket or misconfigured cloud resource exposes customer or internal sensitive data |
| **Threat Source** | Internal — configuration error |
| **Likelihood** | 4 — Likely |
| **Impact** | 3 — Moderate |
| **Inherent Risk Score** | **12 — 🟠 High** |
| **Existing Controls** | Manual cloud reviews (ad hoc) |
| **Control Effectiveness** | Weak |
| **Residual Risk Score** | **10 — 🟠 High** |
| **Risk Owner** | Head of Cloud Engineering |
| **Treatment** | Mitigate |
| **Treatment Plan** | Deploy CSPM tool (e.g., Wiz, Orca), enforce SCPs in AWS Organizations, automate misconfiguration alerts |
| **Target Residual Score** | 4 (Medium) by Q3 2025 |

---

### RISK-006 — Business Continuity Failure — Key Person Dependency
| Field | Detail |
|-------|--------|
| **Domain** | Operational |
| **Risk Statement** | Sudden unavailability of a critical technical lead causes prolonged service disruption |
| **Threat Source** | Internal — personnel |
| **Likelihood** | 3 — Possible |
| **Impact** | 3 — Moderate |
| **Inherent Risk Score** | **9 — 🟠 High** |
| **Existing Controls** | None formal |
| **Control Effectiveness** | None |
| **Residual Risk Score** | **9 — 🟠 High** |
| **Risk Owner** | CTO |
| **Treatment** | Mitigate |
| **Treatment Plan** | Document runbooks, cross-train team members, update BCP with key person scenarios |
| **Target Residual Score** | 4 (Medium) by Q4 2025 |

---

### RISK-007 — Payment Processing Outage
| Field | Detail |
|-------|--------|
| **Domain** | Financial / Operational |
| **Risk Statement** | Payment processor API outage causes inability to process customer transactions |
| **Threat Source** | Third-party failure |
| **Likelihood** | 3 — Possible |
| **Impact** | 4 — Major |
| **Inherent Risk Score** | **12 — 🟠 High** |
| **Existing Controls** | SLA with payment processor |
| **Control Effectiveness** | Partial |
| **Residual Risk Score** | **8 — 🟡 Medium** |
| **Risk Owner** | VP of Engineering |
| **Treatment** | Mitigate / Transfer |
| **Treatment Plan** | Integrate secondary payment processor as fallback, test failover quarterly |
| **Target Residual Score** | 4 (Medium) by Q3 2025 |

---

### RISK-008 — Phishing Attack Resulting in Account Compromise
| Field | Detail |
|-------|--------|
| **Domain** | Information Security |
| **Risk Statement** | Employee falls for phishing email, credentials compromised, attacker pivots to internal systems |
| **Threat Source** | External — phishing campaign |
| **Likelihood** | 4 — Likely |
| **Impact** | 3 — Moderate |
| **Inherent Risk Score** | **12 — 🟠 High** |
| **Existing Controls** | Email filtering, annual security training |
| **Control Effectiveness** | Partial |
| **Residual Risk Score** | **6 — 🟡 Medium** |
| **Risk Owner** | CISO |
| **Treatment** | Mitigate |
| **Treatment Plan** | Enforce MFA on all systems, conduct quarterly phishing simulations, deploy anti-phishing awareness training |
| **Target Residual Score** | 3 (Low) by Q3 2025 |

---

### RISK-009 — PCI DSS Non-Compliance
| Field | Detail |
|-------|--------|
| **Domain** | Regulatory & Compliance |
| **Risk Statement** | Failure to meet PCI DSS requirements results in fines, card brand penalties, or loss of ability to process payments |
| **Threat Source** | Internal — compliance gap |
| **Likelihood** | 2 — Unlikely |
| **Impact** | 5 — Catastrophic |
| **Inherent Risk Score** | **10 — 🟠 High** |
| **Existing Controls** | Annual QSA engagement, tokenization of card data |
| **Control Effectiveness** | Strong |
| **Residual Risk Score** | **4 — 🟡 Medium** |
| **Risk Owner** | Compliance Manager |
| **Treatment** | Maintain / Monitor |
| **Treatment Plan** | Continue annual QSA assessment, quarterly internal scans, maintain PCI scope documentation |
| **Target Residual Score** | 4 (Medium) — ongoing |

---

### RISK-010 — Denial of Service (DDoS) Attack
| Field | Detail |
|-------|--------|
| **Domain** | Information Security / Operational |
| **Risk Statement** | Large-scale DDoS attack takes down customer-facing platform for extended period |
| **Threat Source** | External threat actor |
| **Likelihood** | 3 — Possible |
| **Impact** | 3 — Moderate |
| **Inherent Risk Score** | **9 — 🟠 High** |
| **Existing Controls** | CDN with basic DDoS protection |
| **Control Effectiveness** | Partial |
| **Residual Risk Score** | **6 — 🟡 Medium** |
| **Risk Owner** | VP of Engineering |
| **Treatment** | Mitigate / Transfer |
| **Treatment Plan** | Upgrade to enterprise DDoS protection (e.g., Cloudflare Enterprise), define runbook for DDoS response |
| **Target Residual Score** | 3 (Low) by Q4 2025 |

---

### RISK-011 — Inadequate Patch Management
| Field | Detail |
|-------|--------|
| **Domain** | Information Security |
| **Risk Statement** | Unpatched vulnerabilities exploited in production systems due to lack of formal patch cadence |
| **Threat Source** | External / Internal |
| **Likelihood** | 4 — Likely |
| **Impact** | 3 — Moderate |
| **Inherent Risk Score** | **12 — 🟠 High** |
| **Existing Controls** | Ad hoc patching, no formal policy |
| **Control Effectiveness** | Weak |
| **Residual Risk Score** | **8 — 🟡 Medium** |
| **Risk Owner** | Head of IT Operations |
| **Treatment** | Mitigate |
| **Treatment Plan** | Implement formal patch management policy, deploy automated patching tool, track via vulnerability scanner |
| **Target Residual Score** | 3 (Low) by Q3 2025 |

---

### RISK-012 — Reputational Damage from Public Data Breach
| Field | Detail |
|-------|--------|
| **Domain** | Reputational |
| **Risk Statement** | Public disclosure of a data breach causes significant customer churn and brand damage |
| **Threat Source** | Consequential — follows security incident |
| **Likelihood** | 2 — Unlikely |
| **Impact** | 5 — Catastrophic |
| **Inherent Risk Score** | **10 — 🟠 High** |
| **Existing Controls** | Incident response plan (draft), PR firm on retainer |
| **Control Effectiveness** | Partial |
| **Residual Risk Score** | **6 — 🟡 Medium** |
| **Risk Owner** | CEO / CMO |
| **Treatment** | Mitigate / Transfer |
| **Treatment Plan** | Finalize breach notification runbook, update IR plan, conduct breach simulation, review cyber insurance coverage |
| **Target Residual Score** | 4 (Medium) — ongoing |

---

### RISK-013 — Lack of Formal Access Review Process
| Field | Detail |
|-------|--------|
| **Domain** | Information Security / Audit |
| **Risk Statement** | Excessive or orphaned user accounts exist due to absence of periodic access reviews, creating unauthorized access risk |
| **Threat Source** | Internal — process gap |
| **Likelihood** | 4 — Likely |
| **Impact** | 2 — Minor |
| **Inherent Risk Score** | **8 — 🟡 Medium** |
| **Existing Controls** | None formal |
| **Control Effectiveness** | None |
| **Residual Risk Score** | **8 — 🟡 Medium** |
| **Risk Owner** | IT Manager |
| **Treatment** | Mitigate |
| **Treatment Plan** | Implement quarterly user access reviews (UAR), create access review policy, track via IGA tool |
| **Target Residual Score** | 2 (Low) by Q3 2025 |

---

### RISK-014 — Inadequate Logging and Monitoring
| Field | Detail |
|-------|--------|
| **Domain** | Information Security |
| **Risk Statement** | Insufficient logging means security incidents go undetected or cannot be investigated properly |
| **Threat Source** | Internal — control gap |
| **Likelihood** | 3 — Possible |
| **Impact** | 3 — Moderate |
| **Inherent Risk Score** | **9 — 🟠 High** |
| **Existing Controls** | Basic application logs |
| **Control Effectiveness** | Weak |
| **Residual Risk Score** | **6 — 🟡 Medium** |
| **Risk Owner** | CISO |
| **Treatment** | Mitigate |
| **Treatment Plan** | Deploy SIEM, define log retention policy (minimum 12 months), establish alert thresholds and SOC review process |
| **Target Residual Score** | 3 (Low) by Q4 2025 |

---

### RISK-015 — Failure to Complete Annual Security Awareness Training
| Field | Detail |
|-------|--------|
| **Domain** | Operational / Compliance |
| **Risk Statement** | Employees not completing mandatory security training increases susceptibility to social engineering and policy violations |
| **Threat Source** | Internal — people |
| **Likelihood** | 3 — Possible |
| **Impact** | 2 — Minor |
| **Inherent Risk Score** | **6 — 🟡 Medium** |
| **Existing Controls** | Annual training assigned in LMS |
| **Control Effectiveness** | Partial |
| **Residual Risk Score** | **4 — 🟡 Medium** |
| **Risk Owner** | HR / CISO |
| **Treatment** | Mitigate |
| **Treatment Plan** | Enforce 100% completion tracking, escalate non-completions to managers, add phishing simulation to curriculum |
| **Target Residual Score** | 2 (Low) — ongoing |

---

## Risk Summary Dashboard

| Risk Level | Count | % of Total |
|-----------|-------|-----------|
| 🔴 Critical | 3 | 20% |
| 🟠 High | 5 | 33% |
| 🟡 Medium | 7 | 47% |
| 🟢 Low | 0 | 0% |

**Top 3 Priority Actions:**
1. Deploy immutable backups + network segmentation (RISK-001)
2. Launch formal TPRM program (RISK-002)
3. Deploy DLP + PAM for insider threat mitigation (RISK-003)
