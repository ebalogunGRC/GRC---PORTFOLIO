# PCI DSS v4.0 — Remediation Plan
**Organization:** PayTech Co. | **Period:** Q3 2025 – Q1 2026  
**Goal:** Achieve PCI DSS v4.0 RoC readiness | **Owner:** GRC Team | **Sponsor:** CISO

---

## Executive Summary

The PCI DSS v4.0 gap analysis identified **15 sub-requirements not in place** and **30 partially met** across the 12 requirements. The most critical gaps are in Requirement 10 (Logging & Monitoring) and network segmentation. This remediation plan prioritizes actions by compliance risk and effort, targeting QSA engagement in Q1 2026.

---

## Remediation Phases

### Phase 1 — Critical Fixes (Q3 2025: Jul–Sep)
*Requirement 10 and network segmentation — RoC blockers*

| # | Action | Requirement | Owner | Due | Est. Cost |
|---|--------|------------|-------|-----|-----------|
| 1.1 | Deploy SIEM (Microsoft Sentinel or Splunk) with CDE log ingestion | Req 10.1, 10.2 | Head of Engineering | Aug 31 | $40,000/yr |
| 1.2 | Configure immutable log storage (S3 with WORM policy, 12-month retention) | Req 10.3, 10.5 | Cloud Engineer | Aug 15 | $2,000/yr |
| 1.3 | Configure SIEM alerts for all required event types (auth failures, privilege use, CHD access) | Req 10.4, 10.7 | Security Engineer | Sep 15 | Included |
| 1.4 | Implement network segmentation — isolate CDE from corporate network | Req 1.3 | Head of Engineering | Sep 30 | $15,000 |
| 1.5 | Deploy IDS/IPS on all CDE network segments | Req 11.5 | Cloud Engineer | Sep 30 | $20,000/yr |
| 1.6 | Eliminate all shared accounts in CDE systems | Req 8.1 | IT Manager | Jul 31 | Internal |
| 1.7 | Enforce MFA on all CDE access including legacy jump server | Req 8.3, 8.4 | IT Manager | Aug 31 | Internal |

---

### Phase 2 — High Priority Controls (Q4 2025: Oct–Dec)
*Authentication, data protection, change management*

| # | Action | Requirement | Owner | Due | Est. Cost |
|---|--------|------------|-------|-----|-----------|
| 2.1 | Complete tokenization of legacy PAN storage (db-legacy-pan-01 migration) | Req 3.4, 3.5 | Engineering Lead | Nov 30 | $30,000 |
| 2.2 | Deploy PAM tool for privileged CDE access with session recording | Req 8.6 | IT Manager | Oct 31 | $25,000/yr |
| 2.3 | Implement formal key management policy and rotation schedule | Req 3.7 | CISO | Oct 15 | Internal |
| 2.4 | Deploy WAF on all payment-facing endpoints | Req 6.4 | Cloud Engineer | Oct 31 | $10,000/yr |
| 2.5 | Implement formal change management process for CDE | Req 6.5 | IT Manager | Oct 31 | Internal |
| 2.6 | Implement configuration baselines for all CDE systems | Req 2.2 | Cloud Engineer | Nov 30 | Internal |
| 2.7 | Complete formal CDE asset inventory | Req 2.4 | GRC Analyst | Oct 15 | Internal |
| 2.8 | Formalise patch management SLA for CDE (Critical: 7 days, High: 30 days) | Req 6.1, 6.3 | IT Ops | Oct 31 | Internal |

---

### Phase 3 — Policy, Third-Party & Testing (Q4 2025–Q1 2026)
*Documentation, vendor program, penetration testing*

| # | Action | Requirement | Owner | Due | Est. Cost |
|---|--------|------------|-------|-----|-----------|
| 3.1 | Update information security policy — annual review | Req 12.1 | GRC Analyst | Oct 31 | Internal |
| 3.2 | Build third-party PCI DSS acknowledgment program — collect AOCs from all Tier 1 vendors | Req 12.8, 12.9 | GRC Analyst | Nov 30 | Internal |
| 3.3 | Develop PCI-specific incident response procedure | Req 12.10 | CISO | Nov 30 | Internal |
| 3.4 | Implement PCI-specific security awareness training module | Req 12.6 | HR / CISO | Nov 30 | $5,000 |
| 3.5 | Conduct post-segmentation penetration test to validate CDE isolation | Req 11.4 | External Pen Tester | Dec 15 | $20,000 |
| 3.6 | Conduct quarterly internal vulnerability scans (formalise schedule) | Req 11.3 | IT Ops | Ongoing | Internal |
| 3.7 | Configure NTP consistently across all CDE systems | Req 10.6 | Cloud Engineer | Oct 15 | Internal |
| 3.8 | Implement change detection on payment pages | Req 11.6 | Engineering Lead | Dec 31 | $5,000 |
| 3.9 | Assign formal PCI DSS Compliance Officer role | Req 12.4 | CISO | Oct 1 | Internal |

---

### Phase 4 — QSA Readiness & RoC (Q1 2026)

| # | Action | Owner | Due |
|---|--------|-------|-----|
| 4.1 | Conduct internal PCI DSS readiness assessment | GRC Analyst | Jan 15, 2026 |
| 4.2 | Remediate any remaining gaps from readiness assessment | GRC Team | Feb 28, 2026 |
| 4.3 | Engage QSA — submit evidence packages | GRC Analyst | Mar 1, 2026 |
| 4.4 | QSA on-site assessment | QSA | Mar 2026 |
| 4.5 | **RoC issued** 🎯 | QSA | Apr 2026 |

---

## Budget Summary

| Category | Estimated Cost |
|----------|---------------|
| SIEM (annual) | $40,000 |
| IDS/IPS (annual) | $20,000 |
| PAM Tool (annual) | $25,000 |
| WAF (annual) | $10,000 |
| Network segmentation (one-time) | $15,000 |
| Legacy PAN migration (one-time) | $30,000 |
| Penetration testing | $20,000 |
| QSA fees (RoC) | $40,000–$80,000 |
| Training and miscellaneous | $10,000 |
| **Total Estimated** | **$210,000–$250,000** |

---

## Risk of Non-Compliance

| Risk | Impact |
|------|--------|
| Card brand fines | $5,000–$100,000 per month |
| Loss of ability to process cards | Business-ending |
| Mandatory forensic investigation cost (post-breach) | $100,000–$500,000 |
| Reputational damage and customer loss | Severe |

*The cost of compliance is significantly less than the cost of non-compliance.*
