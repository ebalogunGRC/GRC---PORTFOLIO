# Vendor Risk Register
**Organization:** FinServ Co. | **Version:** 1.0 | **Last Updated:** Q2 2025  
**Owner:** GRC Team | **Review Cycle:** Quarterly

---

## Tier 1 — Critical Vendors

### VENDOR-001 — Salesforce (CRM Platform)
| Field | Detail |
|-------|--------|
| **Service** | Customer Relationship Management (CRM) |
| **Data Processed** | Customer PII, financial data, sales data |
| **Access Level** | High — stores customer records |
| **Inherent Risk** | Critical |
| **Assessment Date** | March 2025 |
| **SOC 2 Report** | ✅ SOC 2 Type II obtained (valid to Dec 2025) |
| **ISO 27001** | ✅ Certified |
| **DDQ Completed** | ✅ Yes |
| **DPA in Place** | ✅ Yes |
| **Breach Notification Clause** | ✅ 72-hour requirement |
| **Right to Audit** | ✅ Yes |
| **Control Effectiveness** | Strong |
| **Residual Risk** | 🟡 Medium |
| **Risk Owner** | VP of Sales |
| **Next Review** | March 2026 |
| **Open Issues** | None |

---

### VENDOR-002 — AWS (Cloud Infrastructure)
| Field | Detail |
|-------|--------|
| **Service** | Cloud hosting — compute, storage, database |
| **Data Processed** | All company and customer data (infrastructure layer) |
| **Access Level** | Critical — hosts all production systems |
| **Inherent Risk** | Critical |
| **Assessment Date** | January 2025 |
| **SOC 2 Report** | ✅ SOC 2 Type II obtained |
| **ISO 27001** | ✅ Certified |
| **PCI DSS AOC** | ✅ Obtained |
| **DDQ Completed** | ✅ Reviewed AWS Shared Responsibility Model |
| **DPA in Place** | ✅ AWS DPA signed |
| **Breach Notification Clause** | ✅ Per AWS Security Agreement |
| **Control Effectiveness** | Strong |
| **Residual Risk** | 🟡 Medium |
| **Risk Owner** | CTO |
| **Next Review** | January 2026 |
| **Open Issues** | Ensure shared responsibility matrix is documented for each AWS service in use |

---

### VENDOR-003 — Okta (Identity Provider)
| Field | Detail |
|-------|--------|
| **Service** | Identity and Access Management (SSO, MFA) |
| **Data Processed** | Employee credentials, authentication logs |
| **Access Level** | Critical — controls access to all systems |
| **Inherent Risk** | Critical |
| **Assessment Date** | February 2025 |
| **SOC 2 Report** | ✅ SOC 2 Type II obtained |
| **DDQ Completed** | ✅ Yes |
| **DPA in Place** | ✅ Yes |
| **Breach Notification Clause** | ✅ Yes |
| **Control Effectiveness** | Strong |
| **Residual Risk** | 🟡 Medium |
| **Risk Owner** | CISO |
| **Next Review** | February 2026 |
| **Open Issues** | Review Okta's 2023 breach response documentation; confirm current controls enhanced |

---

### VENDOR-004 — Stripe (Payment Processing)
| Field | Detail |
|-------|--------|
| **Service** | Payment gateway and card processing |
| **Data Processed** | Cardholder data, transaction data |
| **Access Level** | Critical — processes payment card data |
| **Inherent Risk** | Critical |
| **Assessment Date** | January 2025 |
| **PCI DSS** | ✅ Level 1 Service Provider — AOC obtained |
| **SOC 2 Report** | ✅ SOC 2 Type II obtained |
| **DDQ Completed** | ✅ Yes |
| **DPA in Place** | ✅ Yes |
| **Breach Notification Clause** | ✅ 24-hour notification for payment data |
| **Control Effectiveness** | Strong |
| **Residual Risk** | 🟢 Low |
| **Risk Owner** | CFO |
| **Next Review** | January 2026 |
| **Open Issues** | None |

---

### VENDOR-005 — DataVendor Ltd (Data Analytics)
| Field | Detail |
|-------|--------|
| **Service** | Customer behaviour analytics and reporting |
| **Data Processed** | Customer PII, transaction history, usage patterns |
| **Access Level** | High — receives bulk customer data exports |
| **Inherent Risk** | Critical |
| **Assessment Date** | Not yet assessed — **GAP** |
| **SOC 2 Report** | ❌ Not obtained |
| **ISO 27001** | ❌ Not certified |
| **DDQ Completed** | ❌ No — outstanding |
| **DPA in Place** | ❌ No — processing customer PII without DPA |
| **Breach Notification Clause** | ❌ Not in contract |
| **Control Effectiveness** | Unknown |
| **Residual Risk** | 🔴 Critical |
| **Risk Owner** | Head of Analytics |
| **Next Review** | Immediate — escalated |
| **Open Issues** | 🔴 CRITICAL: Customer PII being processed with no DPA, no security assessment, no breach notification clause. Immediate action required: suspend data transfers pending assessment or terminate relationship. |

---

### VENDOR-006 — CyberSec Tools Inc (Vulnerability Scanner)
| Field | Detail |
|-------|--------|
| **Service** | Vulnerability scanning and penetration testing |
| **Data Processed** | Network topology, system configurations, vulnerability data |
| **Access Level** | High — network access for scanning |
| **Inherent Risk** | High |
| **Assessment Date** | April 2025 |
| **SOC 2 Report** | 🟡 SOC 2 Type I only (Type II in progress) |
| **DDQ Completed** | ✅ Yes |
| **DPA in Place** | ✅ Yes |
| **Breach Notification Clause** | ✅ Yes |
| **Control Effectiveness** | Moderate |
| **Residual Risk** | 🟡 Medium |
| **Risk Owner** | CISO |
| **Next Review** | October 2025 |
| **Open Issues** | Obtain SOC 2 Type II when available (expected Q4 2025) |

---

## Vendor Risk Register Summary

| Tier | Total Vendors | 🔴 Critical Risk | 🟠 High Risk | 🟡 Medium Risk | 🟢 Low Risk |
|------|--------------|----------------|-------------|----------------|------------|
| Tier 1 (Critical) | 18 | 1 | 3 | 12 | 2 |
| Tier 2 (High) | 45 | 0 | 8 | 30 | 7 |
| Tier 3 (Medium) | 89 | 0 | 2 | 60 | 27 |
| Tier 4 (Low) | 63 | 0 | 0 | 10 | 53 |
| **Total** | **215** | **1** | **13** | **112** | **89** |

---

## Outstanding Assessment Actions

| Priority | Vendor | Action Required | Owner | Due |
|----------|--------|----------------|-------|-----|
| 🔴 Immediate | DataVendor Ltd (VENDOR-005) | Suspend data transfers; conduct emergency assessment; negotiate DPA | GRC Analyst | Jul 15, 2025 |
| 🟠 High | 8 unassessed Tier 2 vendors | Complete DDQ and risk assessment | GRC Analyst | Sep 30, 2025 |
| 🟠 High | 15 Tier 1 vendors with expired/missing SOC 2 | Request and review updated SOC 2 reports | GRC Analyst | Aug 31, 2025 |
| 🟡 Medium | 23 vendors with no security contract clauses | Engage Legal to update at next renewal | Legal / GRC | Dec 31, 2025 |

---

## Vendor Risk Register — Metrics Dashboard

| Metric | Current | Target |
|--------|---------|--------|
| Tier 1 vendors assessed | 6/18 (33%) | 100% by Q4 2025 |
| Valid SOC 2 on file (Tier 1) | 9/18 (50%) | 100% by Q4 2025 |
| Contracts with security clauses (Tier 1) | 12/18 (67%) | 100% by Q1 2026 |
| DPAs in place (Tier 1 + 2 processing PD) | 38/52 (73%) | 100% by Q3 2025 |
| Vendors with open critical issues | 1 | 0 |
