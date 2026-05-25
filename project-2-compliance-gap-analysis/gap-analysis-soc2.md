# SOC 2 Type II — Trust Service Criteria Gap Analysis

**Organization:** SaaS Co. | **Assessment Date:** Q2 2025  
**Standard:** AICPA SOC 2 Trust Service Criteria (2017) | **Assessor:** GRC Analyst  
**In-Scope Categories:** Security (CC) · Availability (A1)

---

## Assessment Key

| Status | Symbol |
|--------|--------|
| Met | ✅ |
| Partially Met | 🟡 |
| Not Met | ❌ |

---

## CC1 — Control Environment

| Criteria | Description | Status | Gap / Evidence Notes |
|----------|-------------|--------|---------------------|
| CC1.1 | COSO Principle 1 — Commitment to integrity and ethical values | ✅ | Code of conduct signed by all; ethics hotline available |
| CC1.2 | Board oversight of internal controls | 🟡 | No formal board-level security committee; management reviews only |
| CC1.3 | Organizational structure and reporting lines | ✅ | Org chart documented; CISO reports to CEO |
| CC1.4 | Commitment to competence | 🟡 | Job descriptions exist; security skills not formally assessed for GRC roles |
| CC1.5 | Accountability for internal controls | 🟡 | Control ownership not formally assigned for all CC criteria |

---

## CC2 — Communication and Information

| Criteria | Description | Status | Gap / Evidence Notes |
|----------|-------------|--------|---------------------|
| CC2.1 | Information required for internal controls | ✅ | Policies available on intranet; annual training conducted |
| CC2.2 | Internal communication of control objectives | 🟡 | Security objectives communicated informally; not in writing to all staff |
| CC2.3 | External communication with relevant parties | 🟡 | Privacy policy and ToS published; no formal communication process for security incidents to customers |

---

## CC3 — Risk Assessment

| Criteria | Description | Status | Gap / Evidence Notes |
|----------|-------------|--------|---------------------|
| CC3.1 | Specify objectives to identify and assess risks | 🟡 | Objectives exist; not formally documented in risk management charter |
| CC3.2 | Identify and analyze risks to achieving objectives | 🟡 | Risk register exists but informal; no board-approved risk appetite statement |
| CC3.3 | Assess fraud risk | ❌ | No formal fraud risk assessment conducted |
| CC3.4 | Identify and assess changes that could impact controls | ❌ | No change management process linked to risk assessment |

**Remediation Priority:** 🔴 High — Risk assessment criteria are foundational to SOC 2

---

## CC4 — Monitoring Activities

| Criteria | Description | Status | Gap / Evidence Notes |
|----------|-------------|--------|---------------------|
| CC4.1 | Evaluate and communicate control deficiencies | 🟡 | Deficiencies tracked informally; no formal deficiency tracking register |
| CC4.2 | Perform ongoing and periodic evaluations | 🟡 | Periodic reviews done; not documented consistently; no internal audit function |

---

## CC5 — Control Activities

| Criteria | Description | Status | Gap / Evidence Notes |
|----------|-------------|--------|---------------------|
| CC5.1 | Select and develop control activities to mitigate risk | 🟡 | Controls exist but not mapped to risk register |
| CC5.2 | Select and develop technology controls | ✅ | Technical controls (MFA, EDR, RBAC) deployed and documented |
| CC5.3 | Deploy control activities through policies and procedures | 🟡 | Some policies outdated; not all controls have corresponding procedures |

---

## CC6 — Logical and Physical Access Controls

| Criteria | Description | Status | Gap / Evidence Notes |
|----------|-------------|--------|---------------------|
| CC6.1 | Logical access security measures | ✅ | SSO, MFA, RBAC implemented |
| CC6.2 | New internal users provisioned with least privilege | 🟡 | Provisioning process exists; least privilege not consistently enforced for legacy accounts |
| CC6.3 | Access removed upon termination | 🟡 | Offboarding checklist exists; average access removal time 2–3 days (target: same day) |
| CC6.4 | Physical access to data centers controlled | ✅ | AWS-managed physical security; SOC 2 report from AWS available |
| CC6.5 | Logical access to production restricted | ✅ | Production access requires VPN + MFA; limited to senior engineers |
| CC6.6 | Access over public networks encrypted | ✅ | TLS 1.2+ enforced; HSTS enabled |
| CC6.7 | Restrict access to confidential information | 🟡 | No data classification scheme; all data treated equally |
| CC6.8 | Controls to prevent unauthorized removal of assets | 🟡 | DLP not deployed; no controls on USB or cloud uploads |

---

## CC7 — System Operations

| Criteria | Description | Status | Gap / Evidence Notes |
|----------|-------------|--------|---------------------|
| CC7.1 | Detect and monitor for configuration changes | 🟡 | IaC in use; no automated drift detection |
| CC7.2 | Monitor system components for anomalous behaviour | ❌ | No SIEM; no real-time alerting on anomalous activity |
| CC7.3 | Evaluate security events | ❌ | No defined security event evaluation process |
| CC7.4 | Respond to incidents | 🟡 | IRP drafted; not tested via tabletop or simulation |
| CC7.5 | Recover from incidents | 🟡 | BCP exists; no DR test results documented |

**Remediation Priority:** 🔴 High — CC7 is heavily tested in SOC 2 Type II audits

---

## CC8 — Change Management

| Criteria | Description | Status | Gap / Evidence Notes |
|----------|-------------|--------|---------------------|
| CC8.1 | Manage changes to infrastructure and applications | 🟡 | Git-based change tracking; no formal change approval board or change tickets |

**Remediation Priority:** 🔴 High — Change management evidence is a top SOC 2 finding

---

## CC9 — Risk Mitigation

| Criteria | Description | Status | Gap / Evidence Notes |
|----------|-------------|--------|---------------------|
| CC9.1 | Identify, select, and develop risk mitigation activities | 🟡 | Risk register in place; treatment plans not all documented |
| CC9.2 | Assess and manage risks from vendors and partners | ❌ | No formal TPRM program; no vendor security questionnaires or tiering |

---

## A1 — Availability

| Criteria | Description | Status | Gap / Evidence Notes |
|----------|-------------|--------|---------------------|
| A1.1 | Availability commitments and requirements documented | 🟡 | SLA in customer contracts; no internal availability targets defined |
| A1.2 | Environmental and technical threats addressed | 🟡 | AWS multi-AZ deployment; no DR plan or tested failover |
| A1.3 | Recovery plan tested | ❌ | No DR or BCP test documented in last 12 months |

---

## SOC 2 Readiness Scorecard

| Trust Service Category | Total Criteria | ✅ Met | 🟡 Partial | ❌ Not Met |
|----------------------|---------------|--------|-----------|----------|
| CC1 — Control Environment | 5 | 2 | 3 | 0 |
| CC2 — Communication | 3 | 1 | 2 | 0 |
| CC3 — Risk Assessment | 4 | 0 | 2 | 2 |
| CC4 — Monitoring | 2 | 0 | 2 | 0 |
| CC5 — Control Activities | 3 | 1 | 2 | 0 |
| CC6 — Logical/Physical Access | 8 | 4 | 4 | 0 |
| CC7 — System Operations | 5 | 0 | 3 | 2 |
| CC8 — Change Management | 1 | 0 | 1 | 0 |
| CC9 — Risk Mitigation | 2 | 0 | 1 | 1 |
| A1 — Availability | 3 | 0 | 2 | 1 |
| **Total** | **36** | **8 (22%)** | **22 (61%)** | **6 (17%)** |

---

## Top Gaps to Close Before SOC 2 Type II Audit

| # | Gap | Criteria | Effort | Timeline |
|---|-----|----------|--------|----------|
| 1 | Deploy SIEM and anomaly alerting | CC7.2, CC7.3 | High | 3 months |
| 2 | Implement formal change management process | CC8.1 | Medium | 6 weeks |
| 3 | Build TPRM program with vendor questionnaires | CC9.2 | High | 3 months |
| 4 | Conduct tabletop incident response exercise | CC7.4 | Low | 4 weeks |
| 5 | Complete DR test and document results | A1.3, CC7.5 | Medium | 6 weeks |
| 6 | Conduct fraud risk assessment | CC3.3 | Low | 2 weeks |
| 7 | Link change management to risk triggers | CC3.4 | Medium | 6 weeks |
