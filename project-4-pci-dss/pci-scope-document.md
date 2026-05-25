# Cardholder Data Environment (CDE) Scope Document
**Organization:** PayTech Co. | **Version:** 2.0 | **Date:** Q2 2025  
**Owner:** GRC / Security Team | **Review Cycle:** Annual (required by PCI DSS 12.5)

---

## 1. Purpose

This document defines the scope of the Cardholder Data Environment (CDE) for PCI DSS v4.0 compliance purposes. Scope definition determines which systems, people, and processes are subject to PCI DSS requirements.

---

## 2. Cardholder Data Flows

### 2.1 Data Flow Overview

```
Customer Browser
      │
      ▼ HTTPS (TLS 1.3)
Payment Gateway API ──── Token Vault (stores tokens, not PANs)
      │
      ▼ HTTPS (TLS 1.3)
Card Brand Networks (Visa / Mastercard)
      │
      ▼
Acquiring Bank
      │
      ▼
Settlement → Finance Systems (tokenized references only)
```

### 2.2 Cardholder Data Inventory

| Data Element | Stored | Protected How | In Scope |
|-------------|--------|---------------|----------|
| Primary Account Number (PAN) | Yes (legacy) | AES-256 (new), plain text (legacy — gap) | ✅ Yes |
| Cardholder Name | Yes | Encrypted at rest | ✅ Yes |
| Expiry Date | Yes | Encrypted at rest | ✅ Yes |
| CVV/CVC | No | Never stored post-auth | ✅ In scope for transit |
| PIN | No | Never stored | N/A |
| Full Magnetic Stripe | No | Never stored | N/A |

---

## 3. In-Scope Systems

### 3.1 Systems that Store, Process, or Transmit CHD

| System | Type | Location | Function |
|--------|------|----------|----------|
| payment-api-prod-01/02 | Application Server | AWS us-east-1 | Payment processing API |
| token-vault-prod | Application Server | AWS us-east-1 | Tokenization engine |
| db-payments-prod-01 | Database | AWS RDS | Stores tokenized transaction data |
| db-legacy-pan-01 | Database | AWS RDS | Stores encrypted PANs (legacy — earmarked for migration) |
| payment-gateway-lb | Load Balancer | AWS ALB | Routes payment traffic |
| hsm-01 | Hardware Security Module | AWS CloudHSM | Key management |

### 3.2 Systems Connected to CDE (Connected-to Systems)

| System | Type | Connection Reason | Risk Level |
|--------|------|------------------|-----------|
| vpn-gateway | Network | Admin access route to CDE | High |
| bastion-host-01 | Jump Server | Developer access to CDE | High |
| monitoring-siem | Security Tool | Ingests CDE logs | Medium |
| corp-network | Network | Not segmented from CDE — gap | 🔴 High |
| dev-laptops | Endpoints | Access CDE via VPN | Medium |

### 3.3 Out-of-Scope Systems (Confirmed Isolated)

| System | Isolation Method | Verification |
|--------|----------------|-------------|
| HR systems (Workday) | Separate VLAN, no CDE connection | Firewall rule review |
| Finance ERP | Separate AWS account, no CHD flows | Network diagram confirmed |
| Marketing tools | No access to cardholder data | Data flow review |
| Office WiFi | Separate VLAN, firewall-isolated | Penetration test confirmed |

---

## 4. People in Scope

| Role | CDE Access Type | Justification |
|------|----------------|---------------|
| Payment Engineering Team | Full production access | Maintain payment systems |
| DBA (2 personnel) | Database access | Manage payment databases |
| Security Operations | Log/monitoring access | Monitor CDE security events |
| GRC Analyst | Read-only audit access | Compliance reviews |
| QSA (during assessment) | Scoped read access | PCI assessment |

---

## 5. Third-Party Service Providers in Scope

| Provider | Service | PCI DSS Compliant | AOC Obtained |
|----------|---------|------------------|-------------|
| AWS | Cloud infrastructure | ✅ Yes | ✅ Yes |
| Stripe | Payment gateway (backup) | ✅ Yes | ✅ Yes |
| Visa / Mastercard | Card brand networks | ✅ Yes | Not required |
| CloudFlare | DDoS / WAF | ✅ Yes | ✅ Yes |
| Vendor A (tokenization) | Token vault software | 🟡 Unconfirmed | ❌ Not obtained |

**Gap:** AOC not obtained from Vendor A (tokenization software provider). Required by Req 12.8.

---

## 6. Scope Reduction Opportunities

| Opportunity | Description | Estimated Scope Impact |
|------------|-------------|----------------------|
| Implement P2PE | Point-to-Point Encryption removes CHD from merchant environment | High — removes 60% of in-scope systems |
| Complete legacy PAN migration | Migrate db-legacy-pan-01 to tokenized references | Medium — removes one critical in-scope system |
| Network segmentation | Isolate corporate network from CDE | High — removes connected-to systems from scope |
| Outsource payment page | Use hosted payment page (iFrame) | High — removes web tier from scope |

---

## 7. Scope Validation

PCI DSS v4.0 Requirement 12.5.1 requires the scope to be documented and confirmed at least annually and upon significant changes.

| Validation Activity | Frequency | Last Completed | Next Due |
|--------------------|-----------|---------------|----------|
| Network diagram review | Annual | Q1 2025 | Q1 2026 |
| Data flow diagram review | Annual | Q1 2025 | Q1 2026 |
| Network segmentation test | Semi-annual | Q4 2024 | Q3 2025 |
| Asset inventory review | Quarterly | Q1 2025 | Q3 2025 |
| Third-party AOC collection | Annual | Q1 2025 | Q1 2026 |

---

## 8. Sign-off

| Role | Name | Date | Signature |
|------|------|------|-----------|
| GRC Analyst (Preparer) | | | |
| CISO (Approver) | | | |
| QSA (Reviewer) | | | |

*This document must be reviewed and re-approved following any significant change to the payment environment.*
