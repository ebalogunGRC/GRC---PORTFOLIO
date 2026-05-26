# 📋 Project 2 — Compliance Gap Analysis

**Organization:** SaaS Co. | **Frameworks:** ISO 27001:2022 · SOC 2 Type II · NIST CSF 2.0  
**Role:** GRC Analyst | **Period:** Q3–Q4 2020  
**Status:** ✅ Complete

---

## 📌 Project Overview

A growing SaaS company preparing for ISO 27001 certification and SOC 2 Type II audit engaged the GRC team to conduct a formal gap analysis across three major frameworks. The company also needed to understand its current cybersecurity maturity level using the NIST CSF 2.0 to prioritize improvements and build a realistic compliance roadmap.

---

## 🎯 Objectives

1. Assess compliance posture against ISO 27001:2022 Annex A controls
2. Evaluate readiness against SOC 2 Trust Service Criteria (CC1–CC9 + Availability)
3. Determine NIST CSF 2.0 maturity tier across all 6 functions
4. Identify and prioritize control gaps by severity and compliance impact
5. Produce a 12-month compliance roadmap targeting certification and SOC 2 report

---

## 🔍 Scope

| Item | Detail |
|------|--------|
| **ISO 27001 Controls** | All 93 Annex A controls across 4 domains |
| **SOC 2 Criteria** | CC1–CC9 (Common Criteria) + A1 (Availability) — 36 criteria |
| **NIST CSF Functions** | GV, ID, PR, DE, RS, RC — all 6 functions |
| **Frameworks Applied** | ISO 27001:2022, AICPA SOC 2, NIST CSF 2.0 |
| **Assessment Method** | Document review, interviews, technical walkthroughs |
| **Target Outcome** | ISO 27001 certification + SOC 2 Type II report |

---

## 🛠️ Methodology

### Step 1 — Document Review
Reviewed existing policies, procedures, and controls against framework requirements to establish baseline compliance posture.

### Step 2 — Stakeholder Interviews
Conducted structured interviews with IT, security, HR, legal, and operations teams to validate document findings and identify undocumented practices.

### Step 3 — Control Assessment
Each control was rated using a 3-tier scale:
- ✅ **Implemented** — Control fully in place and operating effectively
- 🟡 **Partial** — Control exists but has gaps or is inconsistently applied
- ❌ **Not Implemented** — Control absent or entirely ineffective

### Step 4 — Gap Prioritization
Gaps were prioritized by certification impact (blockers vs. non-blockers), risk level, and remediation effort.

### Step 5 — Roadmap Development
A phased 12-month remediation roadmap was developed with milestones, owners, timelines, and budget estimates.

---

## 📋 Key Findings

### ISO 27001:2022 Results

| Domain | Total Controls | ✅ Implemented | 🟡 Partial | ❌ Not Implemented |
|--------|---------------|--------------|-----------|------------------|
| 5. Organizational | 37 | 11 (30%) | 17 (46%) | 9 (24%) |
| 6. People | 8 | 4 (50%) | 4 (50%) | 0 |
| 7. Physical | 14 | 9 (64%) | 5 (36%) | 0 |
| 8. Technological | 34 | 14 (41%) | 12 (35%) | 8 (24%) |
| **Total** | **93** | **38 (41%)** | **38 (41%)** | **17 (18%)** |

**Top Certification Blockers:**
- No data classification policy or labelling scheme (Controls 5.12, 5.13)
- No SIEM or centralised logging (Controls 8.15, 8.16)
- No formal supplier security program (Controls 5.19–5.22)
- Incident response plan not tested or approved (Controls 5.24, 5.26)

### SOC 2 Type II Results

| Category | Total | ✅ Met | 🟡 Partial | ❌ Not Met |
|----------|-------|--------|-----------|----------|
| All Criteria | 36 | 8 (22%) | 22 (61%) | 6 (17%) |

**Top SOC 2 Gaps:**
- No SIEM — anomalous behaviour not monitored (CC7.2, CC7.3)
- No formal change management process (CC8.1)
- No TPRM program for vendor risk (CC9.2)
- DR plan not tested (A1.3)

### NIST CSF 2.0 Maturity

| Function | Current Tier | Target Tier |
|----------|-------------|------------|
| GV — Govern | 1.5 | 3 |
| ID — Identify | 2.0 | 3 |
| PR — Protect | 2.4 | 3 |
| DE — Detect | **1.0** | 3 |
| RS — Respond | 1.5 | 3 |
| RC — Recover | 1.5 | 2 |
| **Overall** | **1.8** | **3.0** |

**Weakest area:** Detect function — no SIEM, no real-time monitoring capability.

---

## 📁 Project Deliverables

| File | Description |
|------|-------------|
| [`gap-analysis-iso27001.md`](./gap-analysis-iso27001.md) | Full ISO 27001 Annex A gap analysis — all 93 controls |
| [`gap-analysis-soc2.md`](./gap-analysis-soc2.md) | SOC 2 Trust Service Criteria gap analysis |
| [`nist-csf-maturity.md`](./nist-csf-maturity.md) | NIST CSF 2.0 maturity assessment |
| [`reports/compliance-roadmap.md`](./reports/compliance-roadmap.md) | 12-month compliance roadmap with milestones and budget |
| [`templates/gap-analysis-template.md`](./templates/) | Reusable gap analysis template |
| [`docs/framework-crosswalk.md`](./docs/) | ISO 27001 / SOC 2 / NIST CSF control crosswalk |

---

## 💡 Skills Demonstrated

`ISO 27001:2022` `SOC 2 Type II` `NIST CSF 2.0` `Gap Analysis` `Maturity Assessment` `Control Mapping` `Framework Crosswalks` `Compliance Roadmapping` `Stakeholder Interviews` `Executive Reporting`

---

## 📌 Key Takeaways

- Running three frameworks simultaneously reveals significant control overlap — a single remediation effort can close gaps across all three
- The Detect function (NIST CSF) is most commonly underdeveloped — no SIEM means no visibility
- SOC 2 Type II requires 6–12 months of evidence — starting the clock early is critical
- A phased roadmap with budget estimates is essential for securing executive buy-in
