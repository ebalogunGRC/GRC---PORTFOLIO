# Risk Assessment Methodology

**Version:** 1.0 | **Framework References:** NIST RMF (SP 800-37), ISO 31000:2018, FAIR

---

## 1. Purpose

This document defines the methodology used to identify, assess, score, and treat risks in the Enterprise Risk Register. It ensures consistency and repeatability across all risk assessments.

---

## 2. Risk Identification

Risks are identified through:
- **Interviews** with department heads and system owners
- **Review of prior audit findings** and open remediation items
- **Threat intelligence** — industry-specific threat reports (FS-ISAC, CISA alerts)
- **Control gap analysis** from compliance assessments
- **Incident history** — past near-misses and confirmed incidents

---

## 3. Risk Scoring

We use a **qualitative 5×5 matrix** combining Likelihood and Impact.

### 3.1 Likelihood Scale
| Score | Label | Definition |
|-------|-------|-----------|
| 5 | Almost Certain | Expected to occur within 12 months (>90%) |
| 4 | Likely | Will probably occur within 12 months (60–90%) |
| 3 | Possible | May occur within 12 months (30–60%) |
| 2 | Unlikely | Not expected but possible (10–30%) |
| 1 | Rare | Highly unlikely to occur (<10%) |

### 3.2 Impact Scale
| Score | Label | Business Impact |
|-------|-------|----------------|
| 5 | Catastrophic | Existential threat — regulatory shutdown, >$10M loss, major breach |
| 4 | Major | Severe — significant regulatory fines, >$1M loss, extended outage |
| 3 | Moderate | Notable — operational disruption, <$1M loss, short outage |
| 2 | Minor | Limited — small financial loss, brief disruption |
| 1 | Negligible | Minimal impact — easily absorbed |

### 3.3 Risk Score Calculation
```
Risk Score = Likelihood Score × Impact Score

Critical:  15–25
High:       9–14
Medium:     4–8
Low:        1–3
```

---

## 4. Risk Treatment Options

| Option | When to Use |
|--------|------------|
| **Mitigate** | Deploy controls to reduce likelihood or impact |
| **Transfer** | Shift risk via insurance, contracts, or third parties |
| **Accept** | Residual risk within appetite; document and monitor |
| **Avoid** | Discontinue the activity generating the risk |

---

## 5. Risk Ownership

Every risk must have a named **Risk Owner** — the senior person accountable for ensuring treatment is implemented. Risk owners are accountable to the Risk Committee.

---

## 6. Review Cadence

| Risk Level | Review Frequency |
|-----------|-----------------|
| Critical | Monthly |
| High | Quarterly |
| Medium | Semi-annually |
| Low | Annually |

---

## 7. Risk Appetite Statement

The organization maintains a **low risk appetite** for:
- Regulatory non-compliance
- Customer data exposure
- Payment processing fraud

The organization maintains a **moderate risk appetite** for:
- Operational process inefficiency
- Technology modernization investments

---

## References

- NIST SP 800-30 Rev. 1 — Guide for Conducting Risk Assessments
- NIST SP 800-37 Rev. 2 — Risk Management Framework
- ISO 31000:2018 — Risk Management Guidelines
- FAIR (Factor Analysis of Information Risk) — quantitative risk model reference
