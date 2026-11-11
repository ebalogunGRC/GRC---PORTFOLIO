"""Project 02 — NIST CSF 2.0 gap assessment (36 selected outcomes).
Maturity scale 0–4: 0 Not performed, 1 Initial, 2 Repeatable, 3 Defined, 4 Managed. Target is 3 unless noted."""

# id, short outcome, current state observed, status, current, target, priority, owner, recommendation, 800-53 / ISO mapping, links
O = [
 # GOVERN
 ("GV.OC-01","Mission informs cybersecurity risk management","Security strategy references patient safety and clinic uptime; approved by the CEO in March 2026.","Implemented",3,3,"Low","CISO","Keep annual review tied to the strategic plan.","PM-11 · Cl. 4.1",""),
 ("GV.RM-01","Risk management objectives agreed","Risk appetite statement drafted but not yet approved by the board's audit committee.","Partially implemented",2,3,"Medium","CISO","Present the appetite statement (residual ≤ 9 on the 5×5 scale) for audit committee approval.","PM-9 · Cl. 6.1","R-25"),
 ("GV.RR-01","Leadership accountable for cyber risk","CISO reports quarterly to the executive team; risk owners are named in the risk register.","Implemented",3,3,"Low","CISO","Add risk-owner attestations to the quarterly report.","PM-2 · Cl. 5.1",""),
 ("GV.PO-01","Cybersecurity policy established and communicated","Information security policy approved in 2024; 3 of 14 supporting standards are overdue for review and no AI policy exists.","Partially implemented",2,3,"Medium","Compliance Director","Refresh the overdue standards and publish an AI acceptable-use policy.","PL-1, PM-1 · A.5.1","R-21"),
 ("GV.OV-01","Risk strategy outcomes reviewed","No formal review of whether the strategy reduces risk; reporting is activity-based (tickets closed).","Partially implemented",1,3,"Medium","CISO","Report residual-risk trend and KRI results to the executive team each quarter.","PM-14 · Cl. 9.3",""),
 ("GV.SC-01","Supply chain risk program established","Vendor reviews happen at onboarding only; there is no tiering method and no reassessment schedule.","Partially implemented",1,3,"High","Vendor Risk Manager","Adopt the tiering model from the TPRM workstream and reassess Tier 1 vendors annually.","SR-1, SR-2 · A.5.19","TPR program"),
 # IDENTIFY
 ("ID.AM-01","Hardware inventory maintained","Intune and AWS Config cover managed endpoints and cloud resources; clinic kiosks and lab devices are tracked in a spreadsheet.","Partially implemented",2,3,"Medium","IT Operations Manager","Bring kiosks into a single CMDB fed by Intune, AWS Config and network discovery.","CM-8 · A.5.9","R-18"),
 ("ID.AM-02","Software and services inventory maintained","No inventory of SaaS applications outside SSO; 9 known apps provisioned by hand.","Partially implemented",1,3,"High","IAM Manager","Use CASB discovery to build the SaaS inventory and assign business owners.","CM-8, CM-10 · A.5.9","R-14"),
 ("ID.AM-03","Data flows documented","PHI flows for the EHR hub are diagrammed; telehealth and claims flows are not.","Partially implemented",2,3,"Medium","Privacy Officer","Document PHI flows for telehealth and claims, including third-party transfers.","AC-4, PL-8 · A.5.14",""),
 ("ID.RA-01","Vulnerabilities identified and recorded","Weekly authenticated scanning of servers and cloud; endpoints and containers scanned monthly.","Implemented",3,3,"Low","IT Operations Manager","Extend weekly scanning to container images in the registry.","RA-5 · A.8.8","VM program"),
 ("ID.RA-05","Risk used to prioritize","Enterprise risk register rebuilt in FY2026 with likelihood and impact scoring; not yet used for budget decisions.","Partially implemented",2,3,"Medium","CISO","Link the FY2027 security budget requests to register risk IDs.","RA-3, PM-9 · Cl. 6.1.2","R program"),
 ("ID.IM-01","Improvements identified from evaluations","Audit and pen-test findings tracked in separate spreadsheets with no consolidated view.","Partially implemented",1,3,"Medium","Compliance Director","Consolidate all findings into one POA&M with owners and due dates.","CA-5 · Cl. 10.1","VM program"),
 # PROTECT
 ("PR.AA-01","Identities and credentials managed","Entra ID is the identity source; 11 static secrets found in code repositories.","Partially implemented",2,3,"High","IAM Manager","Rotate exposed secrets and move non-human credentials to a vault.","IA-4, IA-5 · A.5.16, A.5.17","R-11"),
 ("PR.AA-03","Users and services authenticated","MFA for all users; 14 privileged users on push MFA; legacy auth allowed for 3 shared mailboxes.","Partially implemented",2,4,"High","IAM Manager","Require phishing-resistant MFA for privileged roles and block legacy authentication.","IA-2(1), IA-2(2) · A.8.5","R-01, R-06"),
 ("PR.AA-05","Access permissions managed and reviewed","Quarterly user access reviews completed for Entra groups; AWS IAM and the support console are never reviewed.","Partially implemented",2,3,"High","IAM Manager","Add AWS IAM roles and the support console to the quarterly review.","AC-2, AC-6 · A.5.15, A.5.18","ITGC-02, R-08"),
 ("PR.AT-01","Workforce awareness training","Annual training with 97% completion; monthly phishing simulations (click rate fell from 14% to 6%).","Implemented",3,3,"Low","Compliance Director","Add role-based modules for finance and support staff.","AT-2 · A.6.3",""),
 ("PR.DS-01","Data at rest protected","KMS encryption on all RDS and S3 PHI stores; BitLocker on 96% of laptops.","Implemented",3,3,"Low","Cloud Platform Lead","Close the BitLocker gap through Conditional Access.","SC-28 · A.8.24","R-10"),
 ("PR.PS-01","Configuration management practices applied","CIS baselines applied to Windows servers; no baseline or drift detection for Linux or AWS accounts.","Partially implemented",1,3,"High","Cloud Platform Lead","Adopt CIS AWS Foundations as the account baseline with AWS Config conformance packs.","CM-2, CM-6 · A.8.9","CIA-10, R-09"),
 # DETECT
 ("DE.CM-01","Networks monitored","VPC Flow Logs enabled but not sent to the SIEM; no network detection on the clinic VPN.","Partially implemented",1,3,"High","SOC Manager","Ingest VPC Flow Logs and VPN logs into the SIEM with baseline alerts.","SI-4, AU-12 · A.8.16","R-07"),
 ("DE.CM-03","Personnel activity monitored","Support-console record views logged but never reviewed; no UEBA.","Not implemented",0,3,"High","Privacy Officer","Run a weekly anomaly report on record access and review it.","AU-6, AC-2(12) · A.8.16","R-08"),
 ("DE.CM-06","External provider activity monitored","Vendor VPN sessions are not logged centrally; no alerts on vendor access outside contracted hours.","Not implemented",0,3,"High","SOC Manager","Log and alert on all vendor remote sessions.","SA-9, SI-4 · A.5.22","TPR-02"),
 ("DE.AE-02","Adverse events analyzed","Outsourced SOC triages EDR alerts 24/7 with a 30-minute SLA; cloud alerts handled ad hoc by engineers.","Partially implemented",2,3,"Medium","SOC Manager","Route GuardDuty and Entra ID Protection alerts to the SOC queue.","IR-4, SI-4 · A.5.25",""),
 ("DE.AE-03","Information correlated from multiple sources","SIEM receives 23 of 37 required sources; correlation rules exist for EDR only.","Partially implemented",1,3,"High","SOC Manager","Onboard the 14 missing sources and build cross-source detections.","AU-6(3), SI-4 · A.8.15","R-07"),
 ("DE.AE-06","Event information shared with the right people","SOC escalates to the on-call engineer by phone; escalation paths for privacy and legal are not defined.","Partially implemented",2,3,"Medium","SOC Manager","Define escalation criteria that bring in the Privacy Officer and legal for suspected PHI events.","IR-6 · A.6.8",""),
 # RESPOND
 ("RS.MA-01","Incident response plan executed with third parties","IR plan approved in 2025; does not include the outsourced SOC's role or vendor notification contacts.","Partially implemented",2,3,"Medium","CISO","Update the plan with SOC, cyber insurer and key vendor contacts; run a joint tabletop.","IR-8 · A.5.24",""),
 ("RS.MA-02","Incident reports triaged and validated","Triage criteria and severity matrix documented; used consistently in the 2026 incident log.","Implemented",3,3,"Low","SOC Manager","Review the severity matrix annually.","IR-5 · A.5.25",""),
 ("RS.AN-03","Incident analysis and root cause","Root-cause analysis done for 2 of 9 Severity 2+ incidents in the last 12 months.","Partially implemented",1,3,"Medium","SOC Manager","Require a post-incident review for every Severity 2+ incident within 10 business days.","IR-4, IR-5 · A.5.27",""),
 ("RS.CO-02","Stakeholders notified","HIPAA breach notification procedure exists; no template or decision log for the four-factor risk assessment.","Partially implemented",2,3,"High","Privacy Officer","Create a breach-assessment template that documents the four-factor analysis and notification decision.","IR-6, IR-7 · A.5.26",""),
 ("RS.MI-01","Incidents contained","EDR isolation is used routinely; no documented containment steps for compromised cloud identities.","Partially implemented",2,3,"Medium","SOC Manager","Write playbooks for compromised Entra accounts and AWS access keys.","IR-4 · A.5.26",""),
 ("RS.MI-02","Incidents eradicated","Eradication steps follow vendor guidance case by case; no verification step before closure.","Partially implemented",1,3,"Medium","SOC Manager","Add a verification checklist and second-person sign-off before incident closure.","IR-4 · A.5.26",""),
 # RECOVER
 ("RC.RP-01","Recovery plan executed","Recovery is part of the IR plan but has never been exercised end to end.","Partially implemented",1,3,"High","BCDR Manager","Run a full recovery exercise for one Tier 1 service in Q1 2027.","CP-10, IR-4 · A.5.29","BIA program"),
 ("RC.RP-02","Recovery actions prioritized","No agreed restore order across services; BIA tiers drafted in FY2026.","Partially implemented",1,3,"High","BCDR Manager","Approve the BIA tiers and publish a restore sequence.","CP-2 · A.5.30","BIA program"),
 ("RC.RP-03","Backup integrity verified before restore","Backups are not checked for integrity or malware before restore; no immutable copy exists.","Not implemented",0,3,"High","BCDR Manager","Enable Vault Lock, scan restore points before use, and record the result.","CP-9(1), CP-9(8) · A.8.13","R-02, BIA-03"),
 ("RC.RP-04","Post-incident operating norms established","No criteria for declaring recovery complete or for running in degraded mode.","Not implemented",0,3,"Medium","BCDR Manager","Define degraded-mode procedures and exit criteria for Tier 1 services.","CP-2 · A.5.29",""),
 ("RC.CO-03","Recovery progress communicated","The communications plan covers employees only; clinic customers are contacted ad hoc.","Partially implemented",1,3,"Medium","BCDR Manager","Add clinic-customer status updates with fixed intervals to the comms plan.","CP-2, IR-4 · A.5.29",""),
 ("RC.CO-04","Public updates shared","No pre-approved public statement templates; media handled by the CEO's office.","Not implemented",0,2,"Low","Compliance Director","Prepare holding statements approved by legal and communications.","IR-7 · A.5.26",""),
]

FUNCS = [("GV","Govern"),("ID","Identify"),("PR","Protect"),("DE","Detect"),("RS","Respond"),("RC","Recover")]

OUTCOMES = []
for o in O:
    (oid,name,cur,status,c,t,prio,owner,rec,mapping,links) = o
    fcode = oid.split(".")[0]
    OUTCOMES.append(dict(id=oid,name=name,current=cur,status=status,cur=c,target=t,gap=t-c,prio=prio,
        owner=owner,rec=rec,mapping=mapping,links=links,func=dict(FUNCS)[fcode],fcode=fcode))
