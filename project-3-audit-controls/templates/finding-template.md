# Audit Finding Write-up Template

**Instructions:** Complete one form per finding. All five components (Condition, Criteria, Cause, Effect, Recommendation) are required. This structure follows IIA and GAO audit standards.

---

## Finding Header

| Field | Input |
|-------|-------|
| **Finding ID** | FIND-[XXX] |
| **Audit Reference** | IA-[YEAR]-[XXX] |
| **Finding Title** | _(Brief, descriptive title)_ |
| **Severity** | 🔴 High / 🟠 Medium / 🟢 Low |
| **Control Domain** | _(Access Management / Change Management / etc.)_ |
| **Control ID(s)** | _(ITGC-XX)_ |
| **Status** | Open / In Progress / Remediated |
| **Control Owner** | |
| **Date Identified** | |

---

## The Five Components

### 1. Condition *(What did we find?)*

> Describe the current state — what the auditor observed, tested, or identified. Be specific: include sample sizes, error rates, dates, and system names. Avoid vague language.

*Example: "Of 50 change tickets sampled for the period January 1 – June 30, 2025, 34 (68%) had no documented approval prior to deployment to production."*

---

### 2. Criteria *(What should it be?)*

> State the standard, policy, regulation, or control objective that defines the expected state. Reference specific framework controls, policy sections, or regulatory requirements.

*Example: "SOC 2 CC8.1 requires that changes to infrastructure are authorized and approved prior to deployment. The organization's [Policy Name] requires all changes to be approved by a second party before promotion to production."*

---

### 3. Cause *(Why does the gap exist?)*

> Identify the root cause of the deficiency. Avoid blaming individuals; focus on process, resource, or design failures. Use root cause categories: lack of policy, lack of awareness, resource constraints, inadequate tooling, design flaw.

*Example: "No formal change management policy or tooling has been implemented. The organization has prioritized product delivery speed, and informal peer review practices have not been consistently applied."*

---

### 4. Effect *(What is the business impact?)*

> Describe the consequence of the condition — the risk to the business if the deficiency is not addressed. Include regulatory, financial, operational, and reputational impacts where applicable.

*Example: "Without formal change approval, unauthorized or untested code may be deployed to production, introducing vulnerabilities or service instability. This would also be noted as a control exception in an external SOC 2 audit."*

---

### 5. Recommendation *(What should be done?)*

> Provide specific, actionable recommendations. Number each action. Include a proposed timeline or urgency.

*Example:*
*1. Implement a formal change management policy within 30 days*
*2. Configure Jira for mandatory change ticket creation and approval*
*3. Establish lightweight CAB review for significant changes*

---

## Management Response

> *(To be completed by control owner within 10 business days of report issuance)*

**Agree / Disagree with finding:**

**Planned remediation actions:**

**Responsible party:**

**Target completion date:**

---

## Auditor Follow-up

| Date | Activity | Status |
|------|----------|--------|
| | Initial finding presented to management | |
| | Management response received | |
| | Remediation evidence reviewed | |
| | Finding closed | |

---

*Template version 1.0 — aligned to IIA International Standards for the Professional Practice of Internal Auditing*
