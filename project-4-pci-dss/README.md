# Project 4 — PCI DSS Compliance Program

**Scenario:** A payments technology company processing over 6 million card transactions annually engaged the GRC team to build and manage a PCI DSS v4.0 compliance program from the ground up. The organization was classified as a **Merchant Level 1** — the highest tier, requiring an annual Report on Compliance (RoC) by a Qualified Security Assessor (QSA).

**Frameworks:** PCI DSS v4.0 · NIST SP 800-53 · ISO 27001

---

## 📋 Deliverables

| File | Description |
|------|-------------|
| [`pci-dss-gap-analysis.md`](./pci-dss-gap-analysis.md) | PCI DSS v4.0 gap analysis across all 12 requirements |
| [`pci-scope-document.md`](./pci-scope-document.md) | Cardholder Data Environment (CDE) scope definition |
| [`pci-saq-d.md`](./pci-saq-d.md) | Self-Assessment Questionnaire D (SAQ-D) completion |
| [`templates/compensating-control-worksheet.md`](./templates/compensating-control-worksheet.md) | PCI DSS compensating control worksheet |
| [`templates/network-segmentation-test.md`](./templates/network-segmentation-test.md) | Network segmentation testing template |
| [`reports/pci-remediation-plan.md`](./reports/pci-remediation-plan.md) | Prioritized remediation plan |
| [`reports/roc-readiness-report.md`](./reports/roc-readiness-report.md) | QSA readiness assessment report |
| [`docs/pci-policy-index.md`](./docs/pci-policy-index.md) | Required PCI DSS policy inventory |

---

## 🎯 Objectives

1. Define and document the Cardholder Data Environment (CDE) scope
2. Assess compliance posture against all 12 PCI DSS v4.0 requirements
3. Identify gaps and build a remediation plan ahead of QSA engagement
4. Develop required policy documentation and evidence collection process

---

## PCI DSS v4.0 — 12 Requirements Overview

| Req | Domain | Assessment Result |
|-----|--------|------------------|
| 1 | Network Security Controls | 🟡 Partial |
| 2 | Secure Configurations | 🟡 Partial |
| 3 | Protect Stored Account Data | 🟡 Partial |
| 4 | Protect Data in Transmission | ✅ Met |
| 5 | Protect Against Malicious Software | ✅ Met |
| 6 | Secure Systems and Software | 🟡 Partial |
| 7 | Restrict Access by Business Need | ✅ Met |
| 8 | Identify Users and Authenticate Access | 🟡 Partial |
| 9 | Restrict Physical Access | ✅ Met |
| 10 | Log and Monitor All Access | ❌ Not Met |
| 11 | Test Security Regularly | 🟡 Partial |
| 12 | Support Information Security with Policies | 🟡 Partial |

---

## Key Findings

- **Biggest gap:** Requirement 10 — no centralized log management or audit trail for CDE systems
- **Quick win:** Requirement 4 fully met — TLS 1.2+ enforced, no PANs transmitted in clear text
- **Scope reduction opportunity:** Implement Point-to-Point Encryption (P2PE) to reduce CDE scope significantly
- **Timeline to RoC:** Estimated 9 months with current remediation velocity

---

## CDE Scope Summary

| Component | In Scope | Justification |
|-----------|----------|---------------|
| Payment processing servers (AWS) | ✅ Yes | Store, process, transmit CHD |
| Payment gateway API | ✅ Yes | Transmits PANs |
| Corporate network | ✅ Yes | Connected to CDE — not segmented |
| HR / finance systems | ❌ No | Fully isolated VLAN |
| Developer laptops | ✅ Yes | Can access CDE via VPN |

---

## Skills Demonstrated

`PCI DSS v4.0` `CDE Scoping` `SAQ-D` `Gap Analysis` `Compensating Controls` `Network Segmentation` `QSA Readiness` `Tokenization` `Encryption` `Remediation Planning`
