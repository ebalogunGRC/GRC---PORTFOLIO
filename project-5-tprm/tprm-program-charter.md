# Third-Party Risk Management (TPRM) Program Charter
**Organization:** FinServ Co. | **Version:** 1.0 | **Effective Date:** Q3 2025  
**Owner:** GRC Team | **Executive Sponsor:** Chief Risk Officer

---

## 1. Purpose

This charter establishes the Third-Party Risk Management (TPRM) program for FinServ Co. The program provides a structured, risk-based approach to identifying, assessing, managing, and monitoring risks arising from the use of third-party vendors, suppliers, and service providers.

---

## 2. Scope

This program applies to all third parties that:
- Store, process, or transmit company or customer data
- Provide services that support critical business functions
- Have logical or physical access to company systems or facilities
- Are subject to regulatory requirements (e.g., DORA, PCI DSS, GDPR)

This includes but is not limited to: SaaS providers, cloud vendors, IT outsourcers, professional services firms, payment processors, and data processors.

---

## 3. Regulatory and Framework Alignment

| Regulation / Framework | Relevant Requirements |
|----------------------|----------------------|
| ISO 27001:2022 | Controls 5.19, 5.20, 5.21, 5.22 — Supplier relationships |
| NIST SP 800-161 | Supply chain risk management practices |
| SOC 2 CC9.2 | Vendor and partner risk assessment |
| DORA (EU 2022/2554) | ICT third-party risk management, critical provider oversight |
| GDPR Article 28 | Data processor agreements and due diligence |
| FSB Principles | Third-party and outsourcing risk in financial services |

---

## 4. TPRM Governance Structure

| Role | Responsibility |
|------|---------------|
| Chief Risk Officer | Program executive sponsor; escalation point |
| GRC Manager | Program ownership; policy maintenance |
| GRC Analyst | Day-to-day assessments, questionnaires, tracking |
| Legal / Procurement | Contract security clauses, DPA negotiation |
| Business Unit Owners | Identify new vendors; participate in risk decisions |
| CISO | Technical risk review for Tier 1 vendors |
| Vendor Risk Committee | Quarterly governance meeting; approve high-risk exceptions |

---

## 5. TPRM Lifecycle

### 5.1 Vendor Identification and Intake
- All new vendor engagements must be submitted to GRC before contract signing
- Business owner completes a **Vendor Intake Form** identifying data types, access level, and business criticality
- GRC assigns initial tier classification

### 5.2 Due Diligence Assessment
- **Tier 1:** Full security questionnaire (DDQ) + review of SOC 2 / ISO 27001 report + security interview if required
- **Tier 2:** Abbreviated DDQ + SOC 2 report review (or equivalent)
- **Tier 3:** Self-attestation questionnaire
- **Tier 4:** Standard contract terms only

### 5.3 Contract Requirements
All vendor contracts must include (tiered by risk):

| Clause | Tier 1 | Tier 2 | Tier 3 | Tier 4 |
|--------|--------|--------|--------|--------|
| Data Processing Agreement (DPA) | ✅ Required | ✅ Required | ✅ If processing PD | ❌ |
| Security obligations | ✅ Detailed | ✅ Standard | ✅ Basic | ✅ Basic |
| Breach notification (72 hours) | ✅ Required | ✅ Required | ✅ Required | ❌ |
| Right to audit | ✅ Required | ✅ Required | ❌ | ❌ |
| Sub-processor approval | ✅ Required | ✅ Required | ❌ | ❌ |
| Business continuity requirements | ✅ Required | ✅ Required | ❌ | ❌ |
| Data deletion on termination | ✅ Required | ✅ Required | ✅ Required | ❌ |

### 5.4 Risk Assessment and Scoring
Each vendor receives a **Vendor Risk Score (VRS)** based on:
- Inherent risk (data sensitivity × access level × business criticality)
- Control effectiveness (from DDQ responses and evidence)
- Residual risk = Inherent risk adjusted for controls

### 5.5 Ongoing Monitoring
| Tier | Monitoring Activity |
|------|-------------------|
| Tier 1 | Annual re-assessment + quarterly check-in + event-triggered review |
| Tier 2 | Annual re-assessment |
| Tier 3 | Biennial re-assessment |
| Tier 4 | Triennial re-assessment |

**Event triggers for out-of-cycle review:**
- Vendor data breach or security incident
- Significant change in vendor ownership or structure
- Expansion of services or data access
- Adverse news or regulatory action against vendor
- Contract renewal

### 5.6 Issue Management
- Vendor assessment findings are tracked in the Vendor Risk Register
- Critical issues require remediation plan within 30 days
- Unresolved critical issues escalate to Vendor Risk Committee
- GRC may recommend vendor termination for persistent high-risk findings

### 5.7 Vendor Offboarding
All vendor terminations must follow the documented offboarding process:
- Confirm data deletion/return per contractual requirements
- Revoke all access within 24 hours of termination
- Obtain written data destruction confirmation
- Archive vendor assessment records for minimum 5 years

---

## 6. Key Performance Indicators

| KPI | Target |
|-----|--------|
| Tier 1 vendor assessment completion rate | 100% annually |
| New vendor intake SLA (assessment within X days) | 15 business days |
| Vendors with valid SOC 2 / ISO cert on file | 100% of Tier 1 |
| Contracts with security obligations | 100% of Tier 1 & 2 |
| Critical vendor issues remediated within 30 days | >90% |
| Vendor risk register accuracy | Updated within 30 days of changes |

---

## 7. Escalation Matrix

| Scenario | Escalation To | Timeframe |
|----------|--------------|-----------|
| Vendor data breach affecting company data | CISO + CRO + Legal | Immediate |
| Critical risk finding — vendor refuses to remediate | Vendor Risk Committee | 5 business days |
| Vendor financial distress or acquisition | CRO + Legal | 5 business days |
| New critical vendor onboarding | CISO review required | Before contract |

---

## 8. Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | Q3 2025 | GRC Analyst | Initial program charter |

*Review annually or following significant regulatory changes.*
