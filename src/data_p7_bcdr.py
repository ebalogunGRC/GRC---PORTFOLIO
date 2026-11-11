"""Project 07 — Business impact analysis and recovery readiness (NIST SP 800-34 Rev. 1, ISO 22301).
Times in hours. Tested values come from the most recent timed exercise; None = never tested."""

# id, service, business owner, tier, MTD, RTO, RPO, tested RTO, tested RPO, last test, dependencies, impact if down, gap / action, owner, due, links
B = [
 ("BIA-01","Patient portal and telehealth","CMIO",1,24,4,1,3.5,0.25,"2026-09-18",
  "AWS us-west-2, Entra ID B2C, Calendra widget, CloudFront",
  "Patients cannot book or attend virtual visits; clinics fall back to phone scheduling.",
  "Met RTO and RPO in the September exercise. Single-region dependency accepted under R-16.","BCDR Manager","—","R-16"),
 ("BIA-02","EHR integration hub","CTO",1,8,4,0.25,31,2,"2026-08-22",
  "RDS (PostgreSQL), Amazon MQ, Clinilink VPN, Terraform state",
  "Lab results and referrals stop flowing to 45 clinics; patient-safety risk after about 8 hours.",
  "Missed RTO by 27 hours. Message-queue rebuild was manual and undocumented. Codify in Terraform and retest quarterly.","BCDR Manager","2027-04-30","R-13, ITGC-09"),
 ("BIA-03","Claims processing","Compliance Director",1,72,24,4,None,None,"",
  "claims-db (RDS), Windows batch scheduler (2012 R2), clearinghouse SFTP",
  "Clinic reimbursements delayed; contractual penalties after 3 days.",
  "Never tested. Backups share the production account with no object lock. Isolate backups and run first timed restore.","BCDR Manager","2027-01-31","R-02, VM-05"),
 ("BIA-04","Identity (Entra ID and AD)","IAM Manager",1,4,2,0.5,1.5,0,"2026-06-11",
  "Microsoft cloud, 2 on-prem domain controllers",
  "No staff can sign in to any system.",
  "Met RTO. AD forest recovery procedure not rehearsed since 2024; add to the 2027 exercise plan.","IAM Manager","2027-06-30",""),
 ("BIA-05","Clinical scheduling (internal)","CMIO",2,48,12,4,None,None,"",
  "SaaS scheduling platform, Entra SSO",
  "Clinicians lose visibility of daily schedules; manual workarounds possible for 2 days.",
  "Never tested. No exported offline schedule. Add a nightly PDF export to SharePoint.","BCDR Manager","2027-02-28",""),
 ("BIA-06","Email and collaboration","IT Operations Manager",2,48,24,4,6,0,"2026-05-07",
  "Microsoft 365",
  "Internal communication degraded; Teams and SMS fallback available.",
  "Met. Communication tree tested in May.","IT Operations Manager","—",""),
 ("BIA-07","File shares (on-prem)","IT Operations Manager",3,120,48,24,40,24,"2026-03-26",
  "fs-01/02, Vaultline Backup",
  "Departmental documents unavailable; low clinical impact.",
  "Met, with 8 hours to spare. Vendor key custody issue tracked under TPR-04.","IT Operations Manager","—","TPR-04"),
 ("BIA-08","Security monitoring (SIEM/SOC)","SOC Manager",2,24,8,1,None,None,"",
  "SIEM SaaS, Brightwire MSSP, log forwarders",
  "Attacks go undetected during an outage; no direct patient impact.",
  "Never tested. No documented fallback if the SIEM is down. Agree a manual EDR-console procedure with Brightwire.","SOC Manager","2027-03-31","TPR-08"),
 ("BIA-09","Payroll","HR Director",3,168,72,24,None,None,"",
  "Paylane Payroll (SaaS)",
  "Payroll can run one cycle late by manual file; legal deadline sets the MTD.",
  "Vendor-hosted. Confirm Paylane's own DR test results annually instead of testing internally.","HR Director","2027-03-31","TPR-05"),
 ("BIA-10","Corporate website","Compliance Director",4,168,72,24,2,0,"2026-04-15",
  "CloudFront, S3 static hosting",
  "Brand impact only; patients use the portal directly.",
  "Met. Static site redeploys from Git in minutes.","Cloud Platform Lead","—",""),
]

def readiness(rto, trto):
    if trto is None: return "Not tested"
    return "Meets RTO" if trto <= rto else "Misses RTO"

SERVICES = []
for b in B:
    (bid,svc,bo,tier,mtd,rto,rpo,trto,trpo,last,deps,impact,gap,owner,due,links)=b
    SERVICES.append(dict(id=bid,service=svc,bowner=bo,tier=tier,mtd=mtd,rto=rto,rpo=rpo,trto=trto,trpo=trpo,last=last,
        deps=deps,impact=impact,gap=gap,owner=owner,due=due,links=links,ready=readiness(rto,trto)))
