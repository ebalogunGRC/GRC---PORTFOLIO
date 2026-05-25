# IT General Controls (ITGC) Matrix

**Organization:** HealthTech Co. | **Framework:** COSO 2013 · COBIT 2019 · SOC 2

---

## Control Matrix

| Control ID | Domain | Control Description | Type | Frequency | Owner | SOC 2 | COBIT | Design | Operating | Finding |
|-----------|--------|--------------------|----|-----------|-------|-------|-------|--------|-----------|---------|
| ITGC-01 | Access Management | New user accounts provisioned via formal request and approval | Preventive | Per event | IT Manager | CC6.2 | DSS06.03 | ✅ | 🟡 | FIND-002 |
| ITGC-02 | Access Management | User access revoked within 1 business day of termination | Preventive | Per event | IT Manager | CC6.3 | DSS06.03 | 🟡 | ❌ | FIND-002, FIND-004 |
| ITGC-03 | Access Management | Quarterly user access reviews conducted and documented | Detective | Quarterly | IT Manager | CC6.2 | APO09.03 | 🟡 | ❌ | FIND-002 |
| ITGC-04 | Access Management | Privileged accounts reviewed semi-annually | Detective | Semi-annual | CISO | CC6.3 | DSS06.03 | ❌ | ❌ | FIND-004 |
| ITGC-05 | Access Management | MFA enforced on all production system access | Preventive | Continuous | IT Manager | CC6.1 | DSS05.04 | ✅ | ✅ | — |
| ITGC-06 | Access Management | Production access restricted to authorized personnel only | Preventive | Continuous | Head of Eng. | CC6.5 | DSS05.04 | ✅ | ✅ | — |
| ITGC-07 | Change Management | All production changes require documented ticket and approval | Preventive | Per event | IT Manager | CC8.1 | BAI06.01 | ❌ | ❌ | FIND-001 |
| ITGC-08 | Change Management | Changes tested in non-production environment before deployment | Preventive | Per event | Head of Eng. | CC8.1 | BAI06.02 | 🟡 | 🟡 | — |
| ITGC-09 | Change Management | Emergency changes documented and reviewed post-implementation | Detective | Per event | IT Manager | CC8.1 | BAI06.03 | ❌ | ❌ | FIND-001 |
| ITGC-10 | Change Management | Code deployments require peer review (GitHub PR) | Preventive | Per event | Head of Eng. | CC8.1 | BAI06.01 | ✅ | 🟡 | — |
| ITGC-11 | Incident Management | Security incidents logged in ticketing system | Detective | Per event | CISO | CC7.3 | DSS02.01 | 🟡 | 🟡 | FIND-003 |
| ITGC-12 | Incident Management | Incidents classified by severity with defined SLA | Detective | Per event | CISO | CC7.4 | DSS02.02 | ❌ | ❌ | FIND-003 |
| ITGC-13 | Incident Management | Post-incident reviews conducted for Severity 1/2 incidents | Corrective | Per event | CISO | CC4.2 | MEA02.06 | ❌ | ❌ | — |
| ITGC-14 | Monitoring | Centralized log management (SIEM) in place | Detective | Continuous | CISO | CC7.2 | DSS05.07 | ❌ | ❌ | FIND-003 |
| ITGC-15 | Monitoring | Automated alerts configured for security events | Detective | Continuous | CISO | CC7.2 | DSS05.07 | ❌ | ❌ | FIND-003 |
| ITGC-16 | Monitoring | Logs retained for minimum 12 months | Preventive | Continuous | IT Manager | CC7.2 | BAI09.05 | 🟡 | 🟡 | — |
| ITGC-17 | Backup & Recovery | Automated daily backups of production data | Preventive | Daily | Cloud Eng. | A1.2 | DSS04.07 | ✅ | ✅ | — |
| ITGC-18 | Backup & Recovery | Backup restoration tested quarterly | Detective | Quarterly | CTO | A1.3 | DSS04.07 | 🟡 | ❌ | FIND-005 |
| ITGC-19 | Backup & Recovery | RTO and RPO targets defined and documented | Preventive | Annual | CTO | A1.2 | DSS04.02 | ❌ | ❌ | FIND-005 |
| ITGC-20 | Vulnerability Mgmt | Vulnerability scans conducted monthly | Detective | Monthly | IT Ops | CC7.1 | APO12.01 | ✅ | ✅ | — |
| ITGC-21 | Vulnerability Mgmt | Critical vulnerabilities patched within 15 days | Corrective | Per finding | IT Ops | CC7.1 | APO12.06 | ❌ | ❌ | FIND-006 |
| ITGC-22 | Vulnerability Mgmt | Patch compliance tracked and reported | Detective | Monthly | IT Ops | CC4.1 | APO12.06 | ❌ | ❌ | FIND-006 |
| ITGC-23 | Vendor Management | Annual vendor security review conducted for Tier 1 vendors | Detective | Annual | GRC Analyst | CC9.2 | APO10.03 | ❌ | ❌ | FIND-007 |
| ITGC-24 | Security Awareness | All employees complete annual security training | Preventive | Annual | HR / CISO | CC1.4 | APO07.03 | ✅ | 🟡 | FIND-008 (Remediated) |

---

## Control Effectiveness Summary

| Domain | Total Controls | ✅ Effective | 🟡 Partial | ❌ Deficient |
|--------|--------------|------------|-----------|------------|
| Access Management | 6 | 2 | 1 | 3 |
| Change Management | 4 | 0 | 2 | 2 |
| Incident Management | 3 | 0 | 1 | 2 |
| Monitoring | 3 | 0 | 1 | 2 |
| Backup & Recovery | 3 | 1 | 0 | 2 |
| Vulnerability Management | 3 | 1 | 0 | 2 |
| Security Awareness | 1 | 0 | 1 | 0 |
| **Total** | **24** | **4 (17%)** | **6 (25%)** | **14 (58%)** |

---

## Control Type Distribution

| Type | Count |
|------|-------|
| Preventive | 14 |
| Detective | 8 |
| Corrective | 2 |

*Note: Over-reliance on preventive controls with weak detective capability (no SIEM) amplifies risk, as failures may go undetected.*
