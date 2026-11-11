"""Shared engagement context. Every project is one workstream of the same fictional program."""

PERSON = {
    "name": "Emmanuel Balogun",
    "title": "GRC Analyst",
    "focus": "Cybersecurity risk, compliance and IT audit",
    "github": "https://github.com/ebalogunGRC",
    "linkedin": "https://www.linkedin.com/in/emmanuel-balogun-616a0137a",  # leave blank to hide
    "email": "",             # e.g. "you@example.com" — leave blank to hide
    "resume": "",            # e.g. "assets/Emmanuel-Balogun-Resume.pdf" — leave blank to hide
    "location": "Washington State · open to remote",
    "headshot": "https://avatars.githubusercontent.com/u/281046980?v=4",
    "credentials": [
        ("CompTIA Security+", "Certified"),
        ("ISACA CISA", "In progress"),
        ("M.S. Management Information Systems", "Texas Southern University"),
    ],
}

COMPANY = {
    "name": "NovaCare Health Technologies",
    "short": "NovaCare",
    "summary": (
        "A fictional Seattle-based healthcare technology company with about 900 employees. "
        "It runs a patient portal and telehealth app, an EHR integration hub that exchanges HL7 and FHIR "
        "messages with 45 partner clinics, and a claims-processing service. Production runs on AWS; the "
        "workforce uses Microsoft 365 and Entra ID on roughly 1,050 managed endpoints."
    ),
    "facts": [
        ("Workforce", "~900 employees, 1,050 managed endpoints"),
        ("Platform", "AWS (6 accounts, us-west-2), Microsoft 365, Entra ID"),
        ("Data", "PHI for ~1.4M patients across 45 partner clinics"),
        ("Obligations", "HIPAA Security Rule (business associate), SOC 2 Type II commitments to clinics"),
        ("Vendors", "62 active third parties, 14 with PHI access"),
    ],
    "program": "FY2026 Security Assurance Program",
    "as_of": "October 31, 2026",
    "as_of_iso": "2026-10-31",
}

# Owners are roles, used consistently across all eight workstreams.
OWNERS = [
    "CISO", "IAM Manager", "Cloud Platform Lead", "SOC Manager", "IT Operations Manager",
    "AppSec Lead", "Vendor Risk Manager", "Privacy Officer", "BCDR Manager", "Engineering Director",
    "Compliance Director", "CTO", "CMIO", "HR Director",
]
