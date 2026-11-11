"""Project 04 — Vulnerability management and POA&M.
Priority = CVSS v3.1 base severity, raised one level for internet-facing Tier 1 assets,
lowered one level for internal Tier 3 assets. SLA (days): Critical 15, High 30, Moderate 90, Low 180."""
from datetime import date, timedelta

AS_OF = date(2026,10,31)
SLA = {"Critical":15,"High":30,"Moderate":90,"Low":180}
LEVELS = ["Low","Moderate","High","Critical"]

def sev(cvss):
    return "Critical" if cvss>=9 else "High" if cvss>=7 else "Moderate" if cvss>=4 else "Low"

# id, finding, cve, cvss, asset, tier, exposure, discovered, status, owner, milestone, closed, links
V = [
 ("VM-01","Log4j 2.14 remote code execution in fax-to-EHR gateway","CVE-2021-44228",10.0,"fax-gw-01 (legacy gateway)",1,"Internet","2026-08-19","Open – mitigated",
  "IT Operations Manager","WAF rule and egress block applied 2026-08-21; gateway replacement go-live 2026-12-15.","","R-04"),
 ("VM-02","OpenSSH signal handler race condition on bastion hosts","CVE-2024-6387",8.1,"bastion-01/02",1,"Internet","2026-10-08","In remediation",
  "Cloud Platform Lead","Rebuild bastions from patched AMI; then retire in favour of SSM Session Manager.","","R-04"),
 ("VM-03","Broken object-level authorization on /appointments API","Pen test PT-2026-04",8.6,"Patient portal API",1,"Internet","2026-09-02","Closed – verified",
  "AppSec Lead","Ownership check added to API middleware; retest passed 2026-09-16.","2026-09-16","R-17"),
 ("VM-04","TLS 1.0/1.1 enabled on clinic file-transfer endpoint","Config",5.9,"sftp.clinic-exchange",2,"Internet","2026-07-14","Closed – verified",
  "Cloud Platform Lead","TLS 1.2+ policy applied to the load balancer.","2026-08-05",""),
 ("VM-05","Windows Server 2012 R2 out of support","EOL",9.8,"Claims batch scheduler (7 hosts)",2,"Internal","2026-02-10","Risk accepted",
  "IT Operations Manager","Exception RA-2026-03 until migration completes 2027-03-31; hosts isolated on a restricted VLAN.","","R-12"),
 ("VM-06","RDS master password committed to source repository","Secrets scan",9.1,"claims-db (PHI)",1,"Internal","2026-10-02","In remediation",
  "AppSec Lead","Credential rotated 2026-10-03; 10 remaining secrets rotating by 2026-11-30.","","R-11"),
 ("VM-07","S3 bucket allows public listing (marketing assets)","Config",5.3,"novacare-web-assets",3,"Internet","2026-09-21","Closed – verified",
  "Cloud Platform Lead","Block Public Access enabled; CloudFront origin access control added.","2026-09-24","R-09"),
 ("VM-08","Outdated jQuery 1.12 in clinic admin portal (XSS)","Library",6.1,"Clinic admin portal",2,"Internet","2026-08-04","Open",
  "AppSec Lead","Upgrade bundled in the December release.","",""),
 ("VM-09","EDR agent missing on clinic kiosks","Coverage",7.5,"74 kiosk and lab endpoints",3,"Internal","2026-06-30","In remediation",
  "IT Operations Manager","38 of 74 enrolled; remainder moved to kiosk VLAN by 2026-12-31.","","R-18"),
 ("VM-10","SMB signing not required on file servers","Config",5.3,"fs-01, fs-02",2,"Internal","2026-05-12","Open",
  "IT Operations Manager","GPO change scheduled for the November maintenance window.","",""),
 ("VM-11","Container base image with 23 high CVEs","Image scan",7.8,"telehealth-api image",1,"Internal","2026-10-12","In remediation",
  "Engineering Director","Move to distroless base image; rebuild pipeline weekly.","",""),
 ("VM-12","Default SNMP community string on core switch","Config",7.5,"core-sw-01",2,"Internal","2026-09-28","Open",
  "IT Operations Manager","Move to SNMPv3 with unique credentials.","",""),
 ("VM-13","Stale vendor VPN account with standing access","Access",6.5,"Clinilink VPN tunnel",1,"Internet","2026-09-05","Closed – verified",
  "Vendor Risk Manager","Account disabled; vendor access now via time-bound approval.","2026-09-09","TPR-02"),
 ("VM-14","Missing HTTP security headers on patient portal","Config",4.3,"Patient portal",1,"Internet","2026-09-15","Open",
  "AppSec Lead","Add CSP, HSTS preload and frame-ancestors in CloudFront response policy.","",""),
 ("VM-15","Unquoted service path in print management agent","Local",5.5,"~400 workstations",3,"Internal","2026-06-02","Open",
  "IT Operations Manager","Vendor fix in agent v8.2; deploy through Intune.","",""),
 ("VM-16","Weak cipher suites on internal LDAP","Config",3.7,"dc-01, dc-02",2,"Internal","2026-04-20","Open",
  "IAM Manager","Enforce LDAPS with TLS 1.2 during the January DC upgrade.","",""),
]

FINDINGS = []
for v in V:
    (vid,title,ref,cvss,asset,tier,exp,disc,status,owner,ms,closed,links)=v
    base = sev(cvss); i = LEVELS.index(base)
    if exp=="Internet" and tier==1: i=min(i+1,3)
    if exp=="Internal" and tier==3: i=max(i-1,0)
    prio = LEVELS[i]
    d = date.fromisoformat(disc)
    due = d + timedelta(days=SLA[prio])
    end = date.fromisoformat(closed) if closed else AS_OF
    age = (end - d).days
    closed_flag = status.startswith("Closed")
    if status == "Risk accepted":
        sla_state = "Exception"
    elif closed_flag:
        sla_state = "Met" if end <= due else "Missed"
    else:
        sla_state = "Overdue" if AS_OF > due else "Within SLA"
    FINDINGS.append(dict(id=vid,title=title,ref=ref,cvss=cvss,asset=asset,tier=tier,exposure=exp,discovered=disc,
        status=status,owner=owner,milestone=ms,closed=closed,links=links,base=base,prio=prio,sla=SLA[prio],
        due=due.isoformat(),age=age,sla_state=sla_state,is_open=not closed_flag))
