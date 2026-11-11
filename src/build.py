"""Builds the static site into ./site. Run: python3 build.py"""
from collections import Counter
from lib import e, page, topbar, footer, write, DISCLOSURE
from data_company import PERSON, COMPANY
from projects import build_projects, TITLES, ORDER
from data_p1_risk import RISKS
from data_p2_csf import OUTCOMES
from data_p3_audit import CONTROLS
from data_p4_vuln import FINDINGS
from data_p5_tprm import VENDORS
from data_p6_cloud import CHECKS
from data_p7_bcdr import SERVICES
from data_p8_ai import USECASES

specs = build_projects()
by = {s["slug"]: s for s in specs}

# Two headline numbers per project, all computed from the data.
HEAD = {
 "risk-assessment": [(len(RISKS), "risks scored"), (sum(r["inh_band"] == "Critical" for r in RISKS), "Critical before treatment")],
 "gap-assessment": [(len(OUTCOMES), "CSF outcomes"), (sum(o["prio"] == "High" for o in OUTCOMES), "High-priority gaps")],
 "it-audit": [(len(CONTROLS), "ITGCs tested"), (sum(c["result"] != "Effective" for c in CONTROLS), "deficiencies")],
 "vulnerability-management": [(len(FINDINGS), "POA&M items"), (sum(f["sla_state"] == "Overdue" for f in FINDINGS), "past SLA")],
 "third-party-risk": [(len(VENDORS), "vendors reviewed"), (sum(v["residual"] == "High" for v in VENDORS), "High residual risk")],
 "cloud-iam": [(len(CHECKS), "controls tested"), (sum(c["result"] == "Fail" for c in CHECKS), "failed")],
 "business-continuity": [(len(SERVICES), "services in BIA"), (sum(s["ready"] != "Meets RTO" for s in SERVICES), "untested or missed RTO")],
 "ai-governance": [(len(USECASES), "AI use cases"), (sum(u["tier"] == "High" for u in USECASES), "High-risk")],
}
ONE_LINE = {
 "risk-assessment": "25 risks scored on a 5×5 scale with treatment decisions, owners, NIST 800-53 and ISO 27001 mapping, and documented executive risk acceptance.",
 "gap-assessment": "36 CSF 2.0 outcomes rated for status and maturity against a target profile, producing a prioritized roadmap.",
 "it-audit": "14 IT general controls tested with defined samples. Exceptions written as condition, criteria, cause and effect, with management responses.",
 "vulnerability-management": "A POA&M that adjusts CVSS for exposure and asset criticality, tracks SLAs, and records compensating controls and risk acceptances.",
 "third-party-risk": "Vendor tiering, SOC 2 report review (opinions, exceptions, CUECs), BAA checks and conditional approval decisions.",
 "cloud-iam": "15 Entra ID, Microsoft 365 and AWS controls tested against CIS and CISA SCuBA baselines from configuration evidence.",
 "business-continuity": "MTD, RTO and RPO agreed with business owners for 10 services, compared with results of timed recovery tests.",
 "ai-governance": "An AI use-case inventory, risk tiering, NIST AI RMF gap review and AI Review Board decisions, including shadow AI.",
}

nav = [("Work", "#work"), ("Method", "#method"), ("About", "#about"), ("Contact", "#contact")]

score_rows = "".join(
    f'<li><a href="projects/{s}/"><span class="n">{i+1:02d}</span><span class="t">{e(TITLES[s])}'
    f'<small>{HEAD[s][0][0]} {e(HEAD[s][0][1])} · {HEAD[s][1][0]} {e(HEAD[s][1][1])}</small></span><span aria-hidden="true">→</span></a></li>'
    for i, s in enumerate(ORDER))

creds = "".join(f"<div><b>{e(a)}</b><span>{e(b)}</span></div>" for a, b in PERSON["credentials"])
facts = "".join(f"<dt>{e(k)}</dt><dd>{e(v)}</dd>" for k, v in COMPANY["facts"])

def plinks(slugs):
    return "".join(f'<li><a href="projects/{s}/">{ORDER.index(s)+1:02d} · {e(TITLES[s])}</a></li>' for s in slugs)

plist = []
for i, s in enumerate(ORDER):
    sp = by[s]
    fw = "".join(f'<span class="chip">{e(f)}</span>' for f in sp["frameworks"][:3])
    stats = "".join(f'<div><b>{n}</b><span>{e(l)}</span></div>' for n, l in HEAD[s])
    plist.append(f"""<li><span class="pn">{i+1:02d}</span>
<div class="pbody"><span class="label">{e(sp["kicker"])}</span><h3><a href="projects/{s}/">{e(TITLES[s])}</a></h3><p>{e(ONE_LINE[s])}</p><div class="chips">{fw}</div></div>
<div class="pstats">{stats}</div>
<div class="open"><a href="projects/{s}/">Open the assessment →</a></div></li>""")

contact_items = [f'<a class="btn" href="{e(PERSON["github"])}" target="_blank" rel="noopener">GitHub</a>']
if PERSON["linkedin"]: contact_items.insert(0, f'<a class="btn" href="{e(PERSON["linkedin"])}" target="_blank" rel="noopener">LinkedIn</a>')
if PERSON["resume"]: contact_items.append(f'<a class="btn" href="{e(PERSON["resume"])}" target="_blank" rel="noopener">Resume (PDF)</a>')
email_line = (f'<p>Email: <span class="copy">{e(PERSON["email"])}</span></p>' if PERSON["email"] else "")

li_btn = (f'<a class="btn ghost" href="{e(PERSON["linkedin"])}" target="_blank" rel="noopener">LinkedIn</a>' if PERSON["linkedin"] else "")
total_records = len(RISKS)+len(OUTCOMES)+len(CONTROLS)+len(FINDINGS)+len(VENDORS)+len(CHECKS)+len(SERVICES)+len(USECASES)

body = f"""{topbar(0, nav)}
<main id="main">
<section class="hero"><div class="wrap">
<div class="hero-copy">
<span class="label">{e(PERSON["title"])} · {e(PERSON["focus"])}</span>
<h1>I turn security gaps into decisions leaders can act on.</h1>
<p class="lead">I'm {e(PERSON["name"])}. I came to GRC from enterprise IT support and access management, where I saw firsthand how controls work, and fail, in daily operations. This portfolio is a complete security assurance program for one fictional healthcare company: eight connected assessments, {total_records} documented records, every finding tied to a risk, an owner and a date.</p>
<div class="hero-actions"><a class="btn" href="#work">View the assessments</a>{li_btn}<a class="btn ghost" href="{e(PERSON["github"])}" target="_blank" rel="noopener">GitHub profile</a></div>
<div class="creds">{creds}</div>
</div>
<aside class="scorecard" aria-label="Program scorecard">
<header><b>{e(COMPANY["program"])}</b><span class="label">Status as of {e(COMPANY["as_of"])}</span></header>
<ol>{score_rows}</ol>
<footer>{e(COMPANY["name"])} is fictional. Every record was written for this portfolio.</footer>
</aside>
</div></section>

<section class="band" id="engagement" aria-labelledby="h-eng"><div class="wrap">
<div class="section-head"><span class="label">The engagement</span><h2 id="h-eng">One company, one program, eight workstreams</h2>
<p>Instead of eight unrelated exercises, every project assesses the same organization. Findings reference each other the way they would in a real program, and they all roll up to one enterprise risk register.</p></div>
<div class="engage">
<div style="display:grid;gap:14px"><h3>{e(COMPANY["name"])}</h3><p>{e(COMPANY["summary"])}</p></div>
<dl class="facts">{facts}</dl>
</div>
<div class="flow" role="list">
<div role="listitem"><span class="arrow">Assess</span><h3>Control posture</h3><ul>{plinks(["gap-assessment","it-audit","cloud-iam"])}</ul></div>
<div role="listitem"><span class="arrow">Extend</span><h3>Beyond the perimeter</h3><ul>{plinks(["third-party-risk","business-continuity","ai-governance"])}</ul></div>
<div role="listitem"><span class="arrow">Track</span><h3>Remediation</h3><ul>{plinks(["vulnerability-management"])}</ul></div>
<div role="listitem"><span class="arrow">Decide →</span><h3>Enterprise risk register</h3><ul>{plinks(["risk-assessment"])}</ul><p style="font-size:0.9rem" class="muted">Every finding traces to a risk ID with an owner, a treatment and a target residual score.</p></div>
</div>
</div></section>

<section id="work" aria-labelledby="h-work"><div class="wrap">
<div class="section-head"><span class="label">Assessments</span><h2 id="h-work">The work</h2>
<p>Each assessment opens as a full report: scope, conclusion, key findings, analysis, a searchable register with complete records, and the method and criteria used. Every register downloads as CSV.</p></div>
<ol class="plist">{"".join(plist)}</ol>
</div></section>

<section class="band" id="method" aria-labelledby="h-method"><div class="wrap">
<div class="section-head"><span class="label">Method</span><h2 id="h-method">How I work</h2>
<p>The same discipline runs through every assessment, whatever the framework.</p></div>
<ol class="steps">
<li><span class="k">1 · Scope</span><h3>Agree what matters</h3><p>Define systems, data and criteria with the people who own them.</p></li>
<li><span class="k">2 · Evidence</span><h3>Test, don't ask</h3><p>Inspect configurations, logs and samples rather than relying on interviews alone.</p></li>
<li><span class="k">3 · Rate</span><h3>Score consistently</h3><p>Use published scales so every rating can be explained and repeated.</p></li>
<li><span class="k">4 · Recommend</span><h3>Make it actionable</h3><p>Specific fixes with an owner, a due date and a link to the risk they reduce.</p></li>
<li><span class="k">5 · Verify</span><h3>Close with proof</h3><p>Retest before closing, and record formal acceptance when risk stays above appetite.</p></li>
</ol>
<div class="finding-format">
<div><span class="label">Condition</span><h3>What I found</h3><p>“3 of 25 leavers stayed enabled 6 to 14 business days after termination.”</p></div>
<div><span class="label">Criteria</span><h3>What should happen</h3><p>“Access Management Standard §4.2: disable within 1 business day.”</p></div>
<div><span class="label">Cause</span><h3>Why it happened</h3><p>“Late HR entries do not trigger the IT ticket.”</p></div>
<div><span class="label">Effect</span><h3>Why it matters</h3><p>“Former staff could reach email and SaaS apps holding PHI.”</p></div>
</div>
</div></section>

<section id="skills" aria-labelledby="h-skills"><div class="wrap">
<div class="section-head"><span class="label">Capabilities</span><h2 id="h-skills">Frameworks and skills</h2></div>
<div class="skills">
<div><h3>Risk management</h3><ul>
<li>Risk assessment <span>· NIST SP 800-30, 5×5 scoring</span></li><li>Risk treatment and acceptance</li><li>Third-party risk <span>· SOC 2 report review, SIG, BAAs</span></li>
<li>Business impact analysis <span>· MTD, RTO, RPO</span></li><li>AI risk <span>· NIST AI RMF, ISO/IEC 42001</span></li></ul></div>
<div><h3>Compliance and audit</h3><ul>
<li>NIST CSF 2.0 and SP 800-53 Rev. 5</li><li>ISO/IEC 27001:2022 Annex A</li><li>HIPAA Security Rule</li><li>SOC 2 Trust Services Criteria</li>
<li>ITGC testing <span>· sampling, workpapers, findings</span></li><li>POA&amp;M and remediation tracking</li></ul></div>
<div><h3>Technical foundation</h3><ul>
<li>Entra ID and Active Directory <span>· access lifecycle, MFA, PIM</span></li><li>AWS security <span>· IAM, CloudTrail, CIS benchmark</span></li>
<li>Microsoft 365 and Intune</li><li>Vulnerability management <span>· CVSS, SLAs</span></li><li>Enterprise IT support <span>· ~4 years</span></li></ul></div>
</div>
</div></section>

<section class="band" id="about" aria-labelledby="h-about"><div class="wrap">
<div class="about">
<div class="photo"><img src="{e(PERSON["headshot"])}" alt="Portrait of {e(PERSON["name"])}" width="200" height="250" loading="lazy" data-fallback="EB"></div>
<div class="about-copy"><span class="label">About</span><h2 id="h-about">{e(PERSON["name"])}</h2>
<p>I've spent about four years in enterprise IT, most recently as a help desk analyst handling access requests, account lifecycle and endpoint issues. That work showed me where controls break down in practice: the leaver account nobody disabled, the admin role nobody reviewed, the backup nobody tested.</p>
<p>I hold an M.S. in Management Information Systems from Texas Southern University and CompTIA Security+, and I'm preparing for ISACA's CISA. I'm looking for roles in GRC, IT risk, compliance and IT audit, especially where identity and access management meet governance.</p>
<p class="muted">{e(PERSON["location"])}</p></div>
</div>
</div></section>

<section class="contact" id="contact" aria-labelledby="h-contact"><div class="wrap">
<span class="label" style="color:inherit;opacity:.75">Contact</span>
<h2 id="h-contact">Let's talk about your GRC team.</h2>
<p>I'm open to GRC analyst, IT risk, compliance and IT audit roles, remote or in the Pacific Northwest. LinkedIn is the fastest way to reach me.</p>
{email_line}
<div class="contact-links">{"".join(contact_items)}</div>
</div></section>
</main>
{footer()}"""

write("index.html", page(f"{PERSON['name']} | GRC Portfolio",
      f"{PERSON['name']}, GRC analyst. Eight connected security assessments for a fictional healthcare company: risk, NIST CSF 2.0, ITGC audit, vulnerability POA&M, vendor risk, cloud and identity, BIA, and AI governance.",
      body, depth=0))

# 404 page for GitHub Pages
write("404.html", page("Page not found | " + PERSON["name"], "Page not found.",
      f"""{topbar(0, [("Home", "/GRC---PORTFOLIO/")])}<main id="main"><section><div class="wrap" style="display:grid;gap:16px">
<span class="label">404</span><h1>That page isn't here.</h1><p class="muted">The portfolio was reorganized. Every assessment is listed on the home page.</p>
<p><a class="btn" href="/GRC---PORTFOLIO/">Go to the portfolio</a></p></div></section></main>{footer()}""".replace('href="./"', 'href="/GRC---PORTFOLIO/"').replace('href="assets/', 'href="/GRC---PORTFOLIO/assets/'), depth=0)
      .replace('href="assets/site.css"', 'href="/GRC---PORTFOLIO/assets/site.css"').replace('src="assets/site.js"', 'src="/GRC---PORTFOLIO/assets/site.js"'))
print("built", len(specs), "projects")
