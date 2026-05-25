# NIST Cybersecurity Framework 2.0 — Maturity Assessment

**Organization:** SaaS Co. | **Assessment Date:** Q2 2025  
**Framework:** NIST CSF 2.0 | **Assessor:** GRC Analyst

---

## Maturity Tier Definitions

| Tier | Label | Description |
|------|-------|-------------|
| Tier 1 | Partial | Ad hoc, reactive; no formal processes |
| Tier 2 | Risk Informed | Practices exist but not organisation-wide; some risk awareness |
| Tier 3 | Repeatable | Formally approved, consistently implemented, risk-informed |
| Tier 4 | Adaptive | Organisation-wide, continuously improved, informed by lessons learned |

**Current Overall Maturity: Tier 2 (Risk Informed)**  
**Target Maturity: Tier 3 (Repeatable) by Q2 2026**

---

## GV — Govern (New in CSF 2.0)

| Subcategory | Description | Current | Target | Gap |
|-------------|-------------|---------|--------|-----|
| GV.OC | Organizational context understood | Tier 2 | Tier 3 | Risk appetite not formally documented |
| GV.RM | Risk management strategy established | Tier 2 | Tier 3 | No board-approved risk strategy |
| GV.RR | Roles and responsibilities defined | Tier 2 | Tier 3 | CISO role defined; others informal |
| GV.PO | Policy established and communicated | Tier 2 | Tier 3 | Policies exist; review cadence inconsistent |
| GV.OV | Oversight of cybersecurity strategy | Tier 1 | Tier 3 | No board/exec security governance committee |
| GV.SC | Cybersecurity supply chain risk managed | Tier 1 | Tier 2 | No TPRM program |

**Section Maturity: Tier 1–2 | Priority: 🔴 High**

---

## ID — Identify

| Subcategory | Description | Current | Target | Gap |
|-------------|-------------|---------|--------|-----|
| ID.AM | Asset management | Tier 2 | Tier 3 | Cloud assets not fully inventoried |
| ID.RA | Risk assessment | Tier 2 | Tier 3 | Risk register exists; not fully formalised |
| ID.IM | Improvement (lessons learned) | Tier 1 | Tier 3 | No formal post-incident review process |

**Section Maturity: Tier 2 | Priority: 🟠 Medium**

---

## PR — Protect

| Subcategory | Description | Current | Target | Gap |
|-------------|-------------|---------|--------|-----|
| PR.AA | Identity management and access control | Tier 3 | Tier 3 | ✅ MFA, SSO, RBAC all in place |
| PR.AT | Awareness and training | Tier 2 | Tier 3 | Annual training; no role-based or phishing sim program |
| PR.DS | Data security | Tier 2 | Tier 3 | Encryption at rest/transit; no data classification |
| PR.PS | Platform security | Tier 2 | Tier 3 | Patch management informal; no config baseline |
| PR.IR | Technology and process resilience | Tier 2 | Tier 3 | BCP exists; not tested in 18 months |

**Section Maturity: Tier 2–3 | Priority: 🟠 Medium**

---

## DE — Detect

| Subcategory | Description | Current | Target | Gap |
|-------------|-------------|---------|--------|-----|
| DE.CM | Continuous monitoring | Tier 1 | Tier 3 | No SIEM; no continuous monitoring capability |
| DE.AE | Adverse event analysis | Tier 1 | Tier 3 | No real-time alerting or event correlation |

**Section Maturity: Tier 1 | Priority: 🔴 High — WEAKEST AREA**

---

## RS — Respond

| Subcategory | Description | Current | Target | Gap |
|-------------|-------------|---------|--------|-----|
| RS.MA | Incident management | Tier 2 | Tier 3 | IRP exists; untested; no runbooks |
| RS.AN | Incident analysis | Tier 1 | Tier 3 | No forensic capability or structured analysis process |
| RS.CO | Incident response reporting | Tier 2 | Tier 3 | Internal reporting; no external comms plan for breaches |
| RS.MI | Incident mitigation | Tier 2 | Tier 3 | Mitigation done ad hoc; no defined playbooks |

**Section Maturity: Tier 1–2 | Priority: 🔴 High**

---

## RC — Recover

| Subcategory | Description | Current | Target | Gap |
|-------------|-------------|---------|--------|-----|
| RC.RP | Incident recovery plan | Tier 2 | Tier 3 | BCP exists; DR plan absent |
| RC.CO | Recovery communication | Tier 1 | Tier 2 | No communication plan for recovery status to stakeholders |

**Section Maturity: Tier 1–2 | Priority: 🟠 Medium**

---

## NIST CSF Maturity Summary

| CSF Function | Current Tier | Target Tier | Priority |
|-------------|-------------|------------|----------|
| GV — Govern | 1.5 | 3 | 🔴 High |
| ID — Identify | 2.0 | 3 | 🟠 Medium |
| PR — Protect | 2.4 | 3 | 🟠 Medium |
| DE — Detect | 1.0 | 3 | 🔴 High |
| RS — Respond | 1.5 | 3 | 🔴 High |
| RC — Recover | 1.5 | 2 | 🟠 Medium |
| **Overall** | **1.8** | **3.0** | |

---

## Recommended Improvement Roadmap

### Immediate (0–3 months) — Tier 1 → Tier 2
- Deploy SIEM with baseline alerting rules (DE.CM, DE.AE)
- Establish security governance committee with exec sponsorship (GV.OV)
- Complete DR plan with RTO/RPO targets (RC.RP)
- Create incident response runbooks for top 5 scenarios (RS.MI)

### Short-term (3–6 months) — Tier 2 → Tier 3
- Formalise risk management strategy with board approval (GV.RM)
- Complete data classification and labelling (PR.DS)
- Launch TPRM program with vendor tiering (GV.SC)
- Begin phishing simulation program (PR.AT)
- Define patch SLAs and implement automated patching (PR.PS)

### Medium-term (6–12 months) — Sustain Tier 3
- Conduct annual tabletop exercises (RS.MA, RC.RP)
- Implement lessons-learned process from incidents (ID.IM)
- Achieve consistent Tier 3 across all functions
- Begin planning for Tier 4 in highest-priority areas (PR.AA, PR.PS)
