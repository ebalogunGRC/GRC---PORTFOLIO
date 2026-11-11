# Emmanuel Balogun — GRC Portfolio

**Live site:** https://ebalogungrc.github.io/GRC---PORTFOLIO/

A complete security assurance program for one fictional healthcare company, **NovaCare Health Technologies**. Eight connected assessments cover risk, compliance, audit, vulnerability management, vendors, cloud and identity, resilience, and AI. Every finding links to a risk ID, an owner and a due date, and every register downloads as CSV.

| # | Assessment | Frameworks | Records |
|---|---|---|---|
| 01 | [Enterprise Cybersecurity Risk Assessment](https://ebalogungrc.github.io/GRC---PORTFOLIO/projects/risk-assessment/) | NIST SP 800-30, SP 800-53, ISO 27001, HIPAA | 25 risks |
| 02 | [NIST CSF 2.0 Gap Assessment](https://ebalogungrc.github.io/GRC---PORTFOLIO/projects/gap-assessment/) | NIST CSF 2.0, SP 800-53, ISO 27001 | 36 outcomes |
| 03 | [IT General Controls Audit](https://ebalogungrc.github.io/GRC---PORTFOLIO/projects/it-audit/) | COSO, SP 800-53, SOC 2 TSC, IIA Standards | 14 controls |
| 04 | [Vulnerability Management & POA&M](https://ebalogungrc.github.io/GRC---PORTFOLIO/projects/vulnerability-management/) | NIST SP 800-40, CVSS v3.1 | 16 items |
| 05 | [Third-Party Risk Management Review](https://ebalogungrc.github.io/GRC---PORTFOLIO/projects/third-party-risk/) | CSF GV.SC, SP 800-161, SOC 2, SIG, HIPAA | 12 vendors |
| 06 | [Cloud Security & Identity Assessment](https://ebalogungrc.github.io/GRC---PORTFOLIO/projects/cloud-iam/) | CIS AWS v3.0.0, CISA SCuBA, SP 800-53 | 15 controls |
| 07 | [Business Impact Analysis & Recovery Readiness](https://ebalogungrc.github.io/GRC---PORTFOLIO/projects/business-continuity/) | NIST SP 800-34, ISO 22301, HIPAA | 10 services |
| 08 | [AI Governance & Use-Case Risk Review](https://ebalogungrc.github.io/GRC---PORTFOLIO/projects/ai-governance/) | NIST AI RMF, ISO/IEC 42001 | 10 use cases |

Each assessment page includes the scope and criteria, an overall rating, key findings, analysis charts, a searchable register with full records (audit findings use condition, criteria, cause and effect), and the method used.

## Repository layout

```
index.html                 Home page
projects/<name>/index.html One page per assessment
downloads/*.csv            Register exports
assets/site.css, site.js   Shared design and register interactions
src/                       Data and generator (Python 3.12+)
404.html                   Not-found page for GitHub Pages
```

## Editing

The HTML is generated from the data files in `src/`. To change a finding, contact details or wording, edit the matching `src/data_*.py` file (contact links are in `src/data_company.py`), then run:

```
python3 src/build.py
```

No packages are required. Commit the regenerated files.

## Disclosure

NovaCare Health Technologies is fictional. All records were written for this portfolio to demonstrate assessment methods and deliverables. They do not describe a real organization, client or audit. Vendor names other than AWS and Microsoft are fictional.
