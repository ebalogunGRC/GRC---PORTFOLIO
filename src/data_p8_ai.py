"""Project 08 — AI governance: use-case inventory and risk review (NIST AI RMF 1.0, ISO/IEC 42001:2023).
Risk tier: High = affects clinical, employment or financial decisions about people, or processes PHI with
limited human review; Medium = PHI or personal data with a human in the loop; Low = no personal data."""

# id, use case, business owner, purpose, data, decision impact, human oversight, vendor/model, tier, status,
# gaps (by AI RMF function), conditions / next steps, owner, review, links
A = [
 ("AI-01","Patient symptom checker chatbot","CMIO","Suggests care level (self-care, visit, urgent) to portal users.",
  "PHI (symptoms, history)","Influences whether patients seek care","None before advice is shown","Vendor LLM via API","High","Paused",
  "MEASURE: no clinical accuracy testing against triage protocols. MANAGE: no escalation for red-flag symptoms. GOVERN: no clinical safety sign-off.",
  "Paused 2026-09-01 by the AI Review Board. Restart requires a clinical validation study, hard-coded red-flag escalation and CMIO sign-off.","CMIO","2027-03-31","R-21"),
 ("AI-02","Internal document summarization","CTO","Summarizes policies and meeting notes in the approved enterprise assistant.",
  "Internal business data; PHI blocked by DLP","None","User reviews every output","Enterprise AI assistant (tenant-isolated)","Low","Approved",
  "No material gaps. Usage logged; prompts not used for vendor training.",
  "Annual review; confirm DLP block on PHI patterns stays in place.","CTO","2027-09-30",""),
 ("AI-03","Service desk ticket routing","IT Operations Manager","Classifies IT tickets and routes them to the right queue.",
  "Employee names, device data","Low (internal workflow)","Agents can reroute","ITSM platform built-in model","Low","Approved",
  "No material gaps. Misrouting rate is already measured monthly (6%).",
  "None beyond monthly accuracy reporting.","IT Operations Manager","2027-09-30",""),
 ("AI-04","Ambient clinical note transcription","CMIO","Drafts visit notes from telehealth audio for clinician review.",
  "PHI (audio, transcripts)","Draft enters the medical record after clinician sign-off","Clinician edits and signs every note","Scribewell AI","High","Approved with conditions",
  "MAP: vendor contract allowed training on de-identified data. MEASURE: error rate for medication names not measured. GOVERN: patient notice not in telehealth consent.",
  "Contract amendment (no training, US-only processing); measure medication-name error rate on 200 notes; add AI disclosure to consent form.","Privacy Officer","2027-01-31","TPR-07"),
 ("AI-05","Resume screening","HR Director","Ranks applicants for high-volume support roles.",
  "Applicant PII","Decides who gets an interview","Recruiter sees ranked list only","HR platform add-on","High","Under review",
  "MEASURE: no adverse-impact testing across protected groups. MAP: features used by the model are undisclosed. GOVERN: no notice to applicants.",
  "Do not use until the vendor supplies a bias audit and recruiters review every application, not only the top-ranked.","HR Director","2026-12-31",""),
 ("AI-06","SOC alert triage assistant","SOC Manager","Summarizes alerts and suggests severity for analysts.",
  "Security logs (may contain PHI)","Influences response priority","Analyst confirms severity","Brightwire MSSP tooling","Medium","Approved with conditions",
  "MEASURE: false-negative rate on suppressed alerts unknown. MANAGE: no audit of auto-closed alerts.",
  "Weekly sample of 25 auto-closed alerts reviewed by a senior analyst for 3 months.","SOC Manager","2027-02-28","TPR-08"),
 ("AI-07","Marketing copy generation","Compliance Director","Drafts website and email copy.",
  "None","None","Marketing review before publishing","Enterprise AI assistant","Low","Approved",
  "No material gaps. Health claims already pass the existing compliance review.",
  "None.","Compliance Director","2027-09-30",""),
 ("AI-08","Claims anomaly detection","Compliance Director","Flags claims for fraud and coding review.",
  "PHI, billing codes","Flags claims for manual review; no auto-denial","Reviewer decides every flag","In-house model","Medium","Approved with conditions",
  "MEASURE: model not revalidated since 2024 code-set update. MANAGE: no drift monitoring.",
  "Revalidate on 2026 claims data and add quarterly drift reporting.","Engineering Director","2027-03-31",""),
 ("AI-09","Unapproved public chatbots","Compliance Director","Staff using free AI services for drafting and lookup.",
  "Unknown; PHI exposure likely","Unknown","None","11 public services (proxy logs)","High","Prohibited",
  "GOVERN: no AI acceptable-use policy. MAP: no inventory of shadow AI use. MANAGE: no technical block.",
  "Publish AI acceptable-use policy, offer the enterprise assistant as the approved option, block unapproved services for PHI users.","Compliance Director","2027-01-31","R-21"),
 ("AI-10","Code assistant for engineers","Engineering Director","Suggests code in the IDE.",
  "Source code; secrets possible","Code changes go through review","Peer review on every pull request","Enterprise code assistant","Medium","Approved with conditions",
  "MAP: assistant could suggest code containing secrets or vulnerable patterns. MEASURE: no tracking of AI-suggested code defects.",
  "Keep secrets push protection and SAST on all repositories (see R-11, R-24).","Engineering Director","2027-06-30","R-11, R-24"),
]

USECASES = []
for a in A:
    (aid,name,bo,purpose,data,impact,human,vendor,tier,status,gaps,cond,owner,rev,links)=a
    USECASES.append(dict(id=aid,name=name,bowner=bo,purpose=purpose,data=data,impact=impact,human=human,vendor=vendor,
        tier=tier,status=status,gaps=gaps,conditions=cond,owner=owner,review=rev,links=links))
