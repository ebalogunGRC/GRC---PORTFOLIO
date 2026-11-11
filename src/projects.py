"""Project page specs and rendering."""
from collections import Counter
from math import log10
from lib import e, fmt_date, pill, register, hbars, legend, page, topbar, footer, write, write_csv, SEV
from data_company import COMPANY, PERSON
from data_p1_risk import RISKS
from data_p2_csf import OUTCOMES, FUNCS
from data_p3_audit import CONTROLS
from data_p4_vuln import FINDINGS, SLA
from data_p5_tprm import VENDORS
from data_p6_cloud import CHECKS
from data_p7_bcdr import SERVICES
from data_p8_ai import USECASES

RATINGS = {1: "Ineffective", 2: "Needs major improvement", 3: "Needs improvement", 4: "Effective"}

# Map record-ID prefixes to project slugs so cross-references become links.
PREFIX = {"R-": "risk-assessment", "CSF ": "gap-assessment", "ITGC-": "it-audit", "VM-": "vulnerability-management",
          "TPR-": "third-party-risk", "CIA-": "cloud-iam", "BIA-": "business-continuity", "AI-": "ai-governance"}
PROGRAM = {"R program": "risk-assessment", "VM program": "vulnerability-management", "ITGC program": "it-audit",
           "TPR program": "third-party-risk", "CIA program": "cloud-iam", "BIA program": "business-continuity",
           "AI program": "ai-governance"}

def xref(s, here):
    """Turn 'R-01, CIA-02' into links to the owning project pages."""
    if not s: return "—"
    parts = []
    for tok in [t.strip() for t in s.split(",") if t.strip()]:
        slug = PROGRAM.get(tok)
        label = tok
        if not slug:
            for pre, sl in PREFIX.items():
                if tok.startswith(pre): slug = sl; break
        if tok in PROGRAM: label = TITLES[PROGRAM[tok]]
        if slug and slug != here:
            parts.append(f'<a href="../{slug}/">{e(label)}</a>')
        else:
            parts.append(e(label))
    return ", ".join(parts)

def linked_slugs(records, field, here):
    out = []
    for r in records:
        for tok in [t.strip() for t in (r.get(field) or "").split(",") if t.strip()]:
            slug = PROGRAM.get(tok)
            if not slug:
                for pre, sl in PREFIX.items():
                    if tok.startswith(pre): slug = sl; break
            if slug and slug != here and slug not in out: out.append(slug)
    return out

ORDER = ["risk-assessment", "gap-assessment", "it-audit", "vulnerability-management",
         "third-party-risk", "cloud-iam", "business-continuity", "ai-governance"]
TITLES = {
    "risk-assessment": "Enterprise Cybersecurity Risk Assessment",
    "gap-assessment": "NIST CSF 2.0 Gap Assessment",
    "it-audit": "IT General Controls Audit",
    "vulnerability-management": "Vulnerability Management & POA&M",
    "third-party-risk": "Third-Party Risk Management Review",
    "cloud-iam": "Cloud Security & Identity Assessment",
    "business-continuity": "Business Impact Analysis & Recovery Readiness",
    "ai-governance": "AI Governance & Use-Case Risk Review",
}

def kv(label, value): return (label, value)

# ---------------------------------------------------------------- charts
def heatmap(risks, which="inh"):
    counts = Counter((r["il"], r["ii"]) if which == "inh" else (r["rl"], r["ri"]) for r in risks)
    def band(s): return "crit" if s >= 20 else "high" if s >= 10 else "mod" if s >= 5 else "low"
    cells = []
    for l in range(5, 0, -1):
        cells.append(f'<span class="ax">{l}</span>')
        for i in range(1, 6):
            n = counts.get((l, i), 0)
            b = band(l * i)
            if n:
                cells.append(f'<button type="button" class="cell b-{b} has" data-set-filter="cell:{l}x{i}" '
                             f'aria-label="Likelihood {l}, impact {i}: {n} risks. Show in register">{n}</button>')
            else:
                cells.append(f'<span class="cell b-{b}" aria-hidden="true"><span class="z">{l*i}</span></span>')
    cells.append('<span></span>' + "".join(f'<span class="ax">{i}</span>' for i in range(1, 6)))
    return (f'<div class="heatwrap"><span class="heat-y">Likelihood →</span><div class="heat">{"".join(cells)}</div></div>'
            f'<div class="heat-x">Impact →</div>')

def rto_chart(services):
    # Log-scale horizontal chart: target RTO bar, tested result dot, MTD tick; values in a fixed right column.
    W, left, right, rowh, top = 1080, 290, 120, 34, 26
    ticks = [1, 4, 8, 24, 72, 168]
    lo, hi = log10(0.5), log10(200)
    def x(h): return left + (log10(max(h, 0.5)) - lo) / (hi - lo) * (W - left - right)
    H = top + rowh * len(services) + 30
    g = [f'<svg class="chart" viewBox="0 0 {W} {H}" role="img" aria-label="Target recovery time versus tested recovery time for each service">']
    g.append(f'<text x="{W-right+20}" y="{top-10}" style="font-weight:600">Tested</text>')
    for t in ticks:
        g.append(f'<line class="grid" x1="{x(t):.1f}" y1="{top-8}" x2="{x(t):.1f}" y2="{H-26}"/>')
        g.append(f'<text x="{x(t):.1f}" y="{H-10}" text-anchor="middle">{t}h</text>')
    for k, s in enumerate(services):
        y = top + k * rowh
        g.append(f'<text x="0" y="{y+14}" style="font-family:var(--body);font-size:13px;fill:var(--ink)"><tspan style="font-family:var(--mono);font-size:11px;fill:var(--muted)">{e(s["id"])}</tspan>  {e(s["service"])}</text>')
        g.append(f'<rect x="{left}" y="{y+3}" width="{x(s["rto"])-left:.1f}" height="14" rx="2" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="1"/>')
        g.append(f'<line x1="{x(s["mtd"]):.1f}" y1="{y}" x2="{x(s["mtd"]):.1f}" y2="{y+20}" stroke="var(--ink)" stroke-width="2.5"/>')
        if s["trto"] is None:
            g.append(f'<text x="{W-right+20}" y="{y+14}" style="fill:var(--muted)">not tested</text>')
        else:
            ok = s["trto"] <= s["rto"]
            col = "var(--low)" if ok else "var(--crit)"
            g.append(f'<circle cx="{x(s["trto"]):.1f}" cy="{y+10}" r="6.5" fill="{col}" stroke="var(--surface)" stroke-width="2"/>')
            g.append(f'<text x="{W-right+20}" y="{y+14}" style="fill:{col};font-weight:600">{s["trto"]:g}h</text>')
    g.append("</svg>")
    return '<div class="chartscroll">' + "".join(g) + "</div>"

def age_chart(findings):
    open_f = sorted([f for f in findings if f["is_open"]], key=lambda f: -f["age"])
    W, left, right, rowh, top = 560, 60, 60, 26, 10
    mx = max(max(f["age"] for f in open_f), max(f["sla"] for f in open_f)) * 1.02
    def x(d): return left + d / mx * (W - left - right)
    H = top + rowh * len(open_f) + 30
    g = [f'<svg class="chart" viewBox="0 0 {W} {H}" role="img" aria-label="Age of each open finding compared with its remediation SLA">']
    for t in range(0, int(mx) + 1, 60):
        g.append(f'<line class="grid" x1="{x(t):.1f}" y1="{top-6}" x2="{x(t):.1f}" y2="{H-26}"/><text x="{x(t):.1f}" y="{H-10}" text-anchor="middle">{t}d</text>')
    colors = {"Critical": "var(--crit)", "High": "var(--high)", "Moderate": "var(--mod)", "Low": "var(--low)"}
    for k, f in enumerate(open_f):
        y = top + k * rowh
        over = f["sla_state"] == "Overdue"
        g.append(f'<text x="0" y="{y+12}" style="fill:var(--ink)">{e(f["id"])}</text>')
        g.append(f'<rect x="{left}" y="{y+2}" width="{x(f["age"])-left:.1f}" height="12" rx="2" fill="{colors[f["prio"]]}" opacity="{1 if over else 0.4}"/>')
        g.append(f'<line x1="{x(f["sla"]):.1f}" y1="{y-1}" x2="{x(f["sla"]):.1f}" y2="{y+17}" stroke="var(--ink)" stroke-width="2.5"/>')
        g.append(f'<text x="{W-right+10}" y="{y+12}" style="fill:{"var(--crit)" if over else "var(--muted)"};font-weight:{600 if over else 400}">{f["age"]}d</text>')
    g.append("</svg>")
    return '<div class="chartscroll">' + "".join(g) + "</div>"

def maturity_chart(outcomes):
    W, H, left, bottom, top = 560, 230, 30, 30, 12
    funcs = FUNCS
    bw = (W - left - 10) / len(funcs)
    def y(v): return top + (4 - v) / 4 * (H - top - bottom)
    g = [f'<svg class="chart" viewBox="0 0 {W} {H}" role="img" aria-label="Average current and target maturity by CSF function">']
    for v in range(0, 5):
        g.append(f'<line class="grid" x1="{left}" y1="{y(v):.1f}" x2="{W-10}" y2="{y(v):.1f}"/><text x="{left-8}" y="{y(v)+4:.1f}" text-anchor="end">{v}</text>')
    for k, (code, name) in enumerate(funcs):
        rows = [o for o in outcomes if o["fcode"] == code]
        cur = sum(o["cur"] for o in rows) / len(rows)
        tgt = sum(o["target"] for o in rows) / len(rows)
        cx = left + k * bw + bw / 2
        g.append(f'<rect x="{cx-16:.1f}" y="{y(cur):.1f}" width="32" height="{y(0)-y(cur):.1f}" rx="2" fill="var(--accent)"/>')
        g.append(f'<line x1="{cx-24:.1f}" y1="{y(tgt):.1f}" x2="{cx+24:.1f}" y2="{y(tgt):.1f}" stroke="var(--ink)" stroke-width="2" stroke-dasharray="4 3"/>')
        g.append(f'<text x="{cx:.1f}" y="{y(cur)-6:.1f}" text-anchor="middle" style="fill:var(--ink);font-weight:600">{cur:.1f}</text>')
        g.append(f'<text x="{cx:.1f}" y="{H-10}" text-anchor="middle">{code}</text>')
    g.append("</svg>")
    return "".join(g)

def matrix(rows_lbl, cols_lbl, count_fn, cls_fn, filt_fn, corner=""):
    head = f'<tr><th>{e(corner)}</th>' + "".join(f'<th scope="col">{e(c)}</th>' for c in cols_lbl) + "</tr>"
    body = []
    for r in rows_lbl:
        tds = []
        for c in cols_lbl:
            n = count_fn(r, c)
            cls = cls_fn(r, c)
            if n:
                tds.append(f'<td><button type="button" class="cell b-{cls} has" data-set-filter="{e(filt_fn(r, c))}" aria-label="{e(r)}, {e(c)}: {n}">{n}</button></td>')
            else:
                tds.append(f'<td><span class="cell b-{cls}" aria-hidden="true"><span class="z">0</span></span></td>')
        body.append(f'<tr><th scope="row">{e(r)}</th>{"".join(tds)}</tr>')
    return f'<div class="chartscroll"><table class="matrix">{head}{"".join(body)}</table></div>'

# ---------------------------------------------------------------- specs
def spec_risk():
    rs = RISKS
    inh = Counter(r["inh_band"] for r in rs); res = Counter(r["res_band"] for r in rs)
    above = [r for r in rs if r["res"] >= 10]
    domains = sorted(Counter(r["domain"] for r in rs).items(), key=lambda kv: -kv[1])
    bands = ["Critical", "High", "Moderate", "Low"]
    segc = {"Critical": "seg-crit", "High": "seg-high", "Moderate": "seg-mod", "Low": "seg-low"}
    shift = hbars([
        ("Inherent", [(inh[b], segc[b], b) for b in bands], f'{sum(r["inh"] for r in rs)} pts', None),
        ("Target residual", [(res[b], segc[b], b) for b in bands], f'{sum(r["res"] for r in rs)} pts', None),
    ], total=len(rs))
    reduction = 1 - sum(r["res"] for r in rs) / sum(r["inh"] for r in rs)
    dom = hbars([(d, [(sum(1 for r in rs if r["domain"] == d and r["inh_band"] == b), segc[b], b) for b in bands],
                  str(n), f"domain:{d}") for d, n in domains])
    charts = f"""<div class="charts">
<div class="panel"><h3>Inherent risk heat map</h3><p class="sub">Count of risks per likelihood × impact cell. Select a cell to filter the register.</p>{heatmap(rs)}
{legend([("Low 1–4","seg-low"),("Moderate 5–9","seg-mod"),("High 10–16","seg-high"),("Critical 20–25","seg-crit")])}</div>
<div class="panel"><h3>Inherent versus target residual</h3><p class="sub">Number of risks in each band before and after the approved treatment plans. Aggregate risk points fall {reduction:.0%}.</p>{shift}
<h3 style="margin-top:14px">Risks by domain</h3><p class="sub">Coloured by inherent band. Select a domain to filter.</p>{dom}</div>
</div>"""
    cols = [
        dict(key="id", label="ID", html=lambda r: e(r["id"]), cls="id"),
        dict(key="title", label="Risk", html=lambda r: f'<b>{e(r["title"])}</b><br><span class="muted">{e(r["domain"])}</span>'),
        dict(key="inh", label="Inherent", html=lambda r: f'{pill(r["inh_band"])} <span class="mono">{r["il"]}×{r["ii"]}={r["inh"]}</span>',
             sort=lambda r: f'{r["inh"]:02d}', numeric=True, cls="n"),
        dict(key="ttype", label="Treatment", html=lambda r: e(r["ttype"])),
        dict(key="res", label="Target residual", html=lambda r: f'{pill(r["res_band"])} <span class="mono">{r["res"]}</span>',
             sort=lambda r: f'{r["res"]:02d}', numeric=True, cls="n"),
        dict(key="owner", label="Owner", html=lambda r: e(r["owner"])),
        dict(key="status", label="Status", html=lambda r: e(r["status"])),
        dict(key="due", label="Due", html=lambda r: e(fmt_date(r["due"])), sort=lambda r: r["due"], cls="n"),
    ]
    detail = [
        ("Threat event", lambda r: e(r["threat"]), False),
        ("Vulnerability / condition", lambda r: e(r["vuln"]), False),
        ("Existing controls", lambda r: e(r["existing"]), False),
        ("Scoring", lambda r: f'Inherent L{r["il"]} × I{r["ii"]} = {r["inh"]} ({r["inh_band"]}); target residual L{r["rl"]} × I{r["ri"]} = {r["res"]} ({r["res_band"]})', False),
        ("Treatment plan", lambda r: e(r["plan"]), True),
        ("NIST SP 800-53 Rev. 5", lambda r: e(r["nist"]), False),
        ("ISO/IEC 27001:2022", lambda r: e(r["iso"]), False),
        ("Related records", lambda r: xref(r["links"], "risk-assessment"), False),
        ("Owner and due date", lambda r: f'{e(r["owner"])} · {e(fmt_date(r["due"]))}', False),
    ]
    filters = [
        ("band", "Inherent band", bands[:3], lambda r: r["inh_band"]),
        ("domain", "Domain", [d for d, _ in sorted(domains)], lambda r: r["domain"]),
        ("status", "Status", sorted(set(r["status"] for r in rs)), lambda r: r["status"]),
        ("cell", "Heat-map cell", sorted(set(f'{r["il"]}x{r["ii"]}' for r in rs), reverse=True), lambda r: f'{r["il"]}x{r["ii"]}'),
    ]
    csv = (["ID","Risk","Domain","Threat event","Vulnerability","Existing controls","Inherent L","Inherent I","Inherent score","Inherent band",
            "Treatment","Treatment plan","Residual L","Residual I","Residual score","Residual band","Owner","Due","Status","NIST 800-53","ISO 27001 Annex A","Related"],
           [[r["id"],r["title"],r["domain"],r["threat"],r["vuln"],r["existing"],r["il"],r["ii"],r["inh"],r["inh_band"],r["ttype"],r["plan"],
             r["rl"],r["ri"],r["res"],r["res_band"],r["owner"],r["due"],r["status"],r["nist"],r["iso"],r["links"]] for r in rs])
    return dict(
        slug="risk-assessment", kicker="Risk management",
        lede=f"A FY2026 enterprise risk assessment for {COMPANY['name']}: 25 cybersecurity risks scored on a 5×5 likelihood-and-impact scale, each with a treatment decision, accountable owner, control mapping and target residual score. It also serves as the company's HIPAA risk analysis of record.",
        frameworks=["NIST SP 800-30 Rev. 1", "NIST SP 800-53 Rev. 5", "ISO/IEC 27001:2022", "HIPAA §164.308(a)(1)"],
        period="Feb – Apr 2026; status as of Oct 31, 2026",
        glance=[("Objective","Identify and prioritize the cybersecurity risks that could disrupt patient services or expose PHI, and agree treatment with owners."),
                ("Scope","All production systems, the corporate Microsoft 365 tenant, endpoints, and the 14 vendors with PHI access."),
                ("Approach","Asset and threat workshops with 9 risk owners, review of prior audit and pen-test results, scoring per NIST SP 800-30 Appendix G–I."),
                ("Criteria","Risk appetite: target residual ≤ 9 (Moderate). Any High residual needs written acceptance by an executive.")],
        kpis=[(str(len(rs)),"risks assessed across " + str(len(domains)) + " domains",False),
              (str(inh["Critical"]),"rated Critical before treatment",True),
              (f"{reduction:.0%}","reduction in aggregate risk points once treatments are complete",False),
              (str(len(above)),"High residual risks formally accepted by executives",False)],
        rating=(2, "Exposure is concentrated in identity, backups and internet-facing systems. Every risk has an owner and a treatment decision: 3 are complete, 17 in progress and 3 not yet started."),
        findings=[("R-01","Privileged identities are the single largest exposure","All 38 administrator roles are permanent and 14 rely on push MFA. One phished admin could reach every PHI system. Phishing-resistant MFA and just-in-time elevation reduce the score from 20 to 8."),
                  ("R-02, R-13","NovaCare cannot yet prove it can recover from ransomware","Backups sit in the production AWS account without immutability, and the last EHR hub restore took 31 hours against a 4-hour objective."),
                  ("R-04, R-11","Known, exploitable weaknesses are reachable today","A Log4j-vulnerable gateway is internet-facing and 11 live credentials were found in code. Both have containment in place and fixes due by year end."),
                  ("R-05, R-16","Two High residual risks were accepted, on the record","The EHR partner's qualified SOC 2 and the single-region AWS design remain above appetite. The COO and CTO signed time-bound acceptances with review dates.")],
        charts=charts,
        reg=register(rs, cols, detail, filters, "../../downloads/01-risk-register.csv", "Search risks, owners, controls…", noun="risks"),
        csv=("downloads/01-risk-register.csv",) + csv,
        method_steps=["Confirm scope, assets and data flows with system owners.","Identify threat events and the specific vulnerabilities or conditions that enable them.",
                      "Record existing controls and rate likelihood (1–5) and impact (1–5) using the criteria table.","Agree a treatment (mitigate, transfer, avoid, accept) and a target residual score with each owner.",
                      "Map treatments to NIST SP 800-53 and ISO 27001 Annex A controls; log acceptances above appetite.","Track status monthly and re-score when a treatment is verified."],
        criteria=("Score bands", ["Band","Score","Required response"],
                  [["Critical","20–25","Escalate to executive team; treatment plan within 15 days"],["High","10–16","Treatment plan within 30 days, or executive acceptance"],
                   ["Moderate","5–9","Owner-managed treatment; within appetite"],["Low","1–4","Monitor during annual review"]]),
    )

def spec_csf():
    os_ = OUTCOMES
    st = Counter(o["status"] for o in os_)
    order = ["Implemented", "Partially implemented", "Not implemented"]
    segc = {"Implemented": "seg-low", "Partially implemented": "seg-mod", "Not implemented": "seg-crit"}
    byf = hbars([(f"{name} ({code})", [(sum(1 for o in os_ if o["fcode"] == code and o["status"] == s), segc[s], s) for s in order],
                  f'{sum(1 for o in os_ if o["fcode"]==code and o["status"]=="Implemented")}/{sum(1 for o in os_ if o["fcode"]==code)}',
                  f"func:{name}") for code, name in FUNCS], total=6)
    avg_cur = sum(o["cur"] for o in os_) / len(os_)
    avg_tgt = sum(o["target"] for o in os_) / len(os_)
    high = [o for o in os_ if o["prio"] == "High"]
    charts = f"""<div class="charts">
<div class="panel"><h3>Implementation status by function</h3><p class="sub">Six outcomes per function. The figure on the right is outcomes fully implemented. Select a function to filter.</p>{byf}
{legend([("Implemented","seg-low"),("Partially implemented","seg-mod"),("Not implemented","seg-crit")])}</div>
<div class="panel"><h3>Average maturity: current versus target</h3><p class="sub">Bars show average current maturity (0–4). Dashed lines show the target profile.</p>{maturity_chart(os_)}
{legend([("Current","seg-acc"),("Target (dashed)","seg-none")])}</div>
</div>"""
    pc = {"High": "high", "Medium": "mod", "Low": "low"}
    sc = {"Implemented": "low", "Partially implemented": "mod", "Not implemented": "crit"}
    cols = [
        dict(key="id", label="Outcome", html=lambda o: e(o["id"]), cls="id"),
        dict(key="name", label="Description", html=lambda o: f'<b>{e(o["name"])}</b><br><span class="muted">{e(o["func"])}</span>'),
        dict(key="status", label="Status", html=lambda o: pill(o["status"], sc[o["status"]]),
             sort=lambda o: order.index(o["status"])),
        dict(key="cur", label="Current → target", html=lambda o: f'<span class="mono">{o["cur"]} → {o["target"]}</span>', sort=lambda o: o["cur"], numeric=True, cls="n"),
        dict(key="prio", label="Priority", html=lambda o: pill(o["prio"], pc[o["prio"]]), sort=lambda o: ["High","Medium","Low"].index(o["prio"])),
        dict(key="owner", label="Owner", html=lambda o: e(o["owner"])),
    ]
    detail = [
        ("Current state observed", lambda o: e(o["current"]), True),
        ("Recommendation", lambda o: e(o["rec"]), True),
        ("Maturity", lambda o: f'Current {o["cur"]}, target {o["target"]} (gap {o["gap"]})', False),
        ("Mapping (NIST SP 800-53 · ISO 27001)", lambda o: e(o["mapping"]), False),
        ("Related records", lambda o: xref(o["links"], "gap-assessment"), False),
        ("Owner", lambda o: e(o["owner"]), False),
    ]
    filters = [
        ("func", "Function", [n for _, n in FUNCS], lambda o: o["func"]),
        ("status", "Status", order, lambda o: o["status"]),
        ("prio", "Priority", ["High", "Medium", "Low"], lambda o: o["prio"]),
    ]
    csv = (["Outcome","Description","Function","Status","Current maturity","Target maturity","Gap","Priority","Owner","Current state","Recommendation","Mapping","Related"],
           [[o["id"],o["name"],o["func"],o["status"],o["cur"],o["target"],o["gap"],o["prio"],o["owner"],o["current"],o["rec"],o["mapping"],o["links"]] for o in os_])
    return dict(
        slug="gap-assessment", kicker="Compliance assessment",
        lede="A scoped NIST Cybersecurity Framework 2.0 assessment of 36 outcomes, six from each function. Each outcome has an observed current state, a maturity score against a target profile, a prioritized recommendation and an owner.",
        frameworks=["NIST CSF 2.0", "NIST SP 800-53 Rev. 5", "ISO/IEC 27001:2022"],
        period="Mar – May 2026; status as of Oct 31, 2026",
        glance=[("Objective","Measure NovaCare's program against a CSF 2.0 target profile and produce a prioritized roadmap."),
                ("Scope","36 of the 106 CSF 2.0 subcategories, chosen for relevance to PHI protection and SOC 2 commitments."),
                ("Approach","Document review, 12 stakeholder interviews and inspection of system configurations and reports."),
                ("Criteria","Maturity 0–4 (Not performed, Initial, Repeatable, Defined, Managed). Target is 3 unless the outcome warrants otherwise.")],
        kpis=[(str(len(os_)),"outcomes assessed, 6 per function",False),
              (f"{st['Implemented']}","fully implemented",False),
              (f"{avg_cur:.1f} / {avg_tgt:.1f}","average current versus target maturity",False),
              (str(len(high)),"High-priority gaps on the roadmap",True)],
        rating=(3, "Govern, Identify and Protect have working foundations. Detect and Recover are the weakest functions and drive most High-priority gaps."),
        findings=[("DE.CM-03, DE.CM-06","Activity by insiders and vendors is not monitored","Record access in the support console and vendor VPN sessions are logged nowhere a person reviews. Neither would surface misuse of PHI."),
                  ("DE.AE-03","The SIEM sees 62% of the log sources it needs","Cloud data events and identity risk signals are missing, so detections rely almost entirely on endpoint alerts."),
                  ("RC.RP-01 to RC.RP-04","Recovery has never been exercised end to end","There is no agreed restore order, no backup integrity check and no criteria for declaring recovery complete."),
                  ("PR.AA-03, PR.AA-05","Strong basics with privileged gaps","MFA covers all users and Entra access is reviewed quarterly, but privileged MFA is phishable and AWS roles are never reviewed.")],
        charts=charts,
        reg=register(os_, cols, detail, filters, "../../downloads/02-csf-gap-assessment.csv", "Search outcomes, findings, owners…", noun="outcomes"),
        csv=("downloads/02-csf-gap-assessment.csv",) + csv,
        method_steps=["Select outcomes with stakeholders and set the target maturity for each.","Interview control owners and request evidence for each outcome.",
                      "Inspect configurations and reports to confirm what is actually in place.","Rate status and current maturity; record the gap to target.",
                      "Prioritize gaps by risk (linked to the enterprise register) and assign owners.","Publish a roadmap and re-assess outcomes as remediation closes."],
        criteria=("Maturity scale", ["Level","Name","Meaning"],
                  [["0","Not performed","No process or control in place"],["1","Initial","Ad hoc; depends on individuals"],["2","Repeatable","Done consistently but not documented or measured"],
                   ["3","Defined","Documented, owned and followed across the organization"],["4","Managed","Measured, reported and improved"]]),
    )

def spec_audit():
    cs = CONTROLS
    res = Counter(c["result"] for c in cs)
    order = ["Effective", "Deficiency", "Significant deficiency"]
    segc = {"Effective": "seg-low", "Deficiency": "seg-mod", "Significant deficiency": "seg-crit"}
    areas = ["Access management", "Change management", "IT operations", "Governance"]
    bya = hbars([(a, [(sum(1 for c in cs if c["area"] == a and c["result"] == s), segc[s], s) for s in order],
                  f'{sum(1 for c in cs if c["area"]==a and c["result"]=="Effective")}/{sum(1 for c in cs if c["area"]==a)}', f"area:{a}") for a in areas])
    tested = sum(c["sample"] for c in cs); exc = sum(c["exc"] for c in cs)
    rate = [(c["id"], c["exc"], c["sample"]) for c in cs if c["exc"]]
    exch = hbars([(f'{i}', [(x / n * 100, "seg-crit", "Exception rate %"), (100 - x / n * 100, "seg-none", "No exception %")], f"{x}/{n}", None) for i, x, n in rate], total=100)
    charts = f"""<div class="charts">
<div class="panel"><h3>Results by control area</h3><p class="sub">The figure on the right is controls operating effectively. Select an area to filter.</p>{bya}
{legend([("Effective","seg-low"),("Deficiency","seg-mod"),("Significant deficiency","seg-crit")])}</div>
<div class="panel"><h3>Exceptions found in sample</h3><p class="sub">Controls with at least one exception. Each bar is that control’s full sample; red is the share that failed.</p>{exch}</div>
</div>"""
    rc = {"Effective": "low", "Deficiency": "mod", "Significant deficiency": "crit"}
    cols = [
        dict(key="id", label="ID", html=lambda c: e(c["id"]), cls="id"),
        dict(key="control", label="Control", html=lambda c: f'<b>{e(c["control"])}</b><br><span class="muted">{e(c["area"])} · {e(c["freq"])}</span>'),
        dict(key="sample", label="Sample", html=lambda c: f'<span class="mono">{c["sample"]} of {c["pop"]}</span>', sort=lambda c: c["sample"], numeric=True, cls="n"),
        dict(key="exc", label="Exceptions", html=lambda c: f'<span class="mono">{c["exc"]}</span>', sort=lambda c: c["exc"], numeric=True, cls="n"),
        dict(key="result", label="Result", html=lambda c: pill(c["result"], rc[c["result"]]), sort=lambda c: order.index(c["result"])),
        dict(key="owner", label="Owner", html=lambda c: e(c["owner"])),
    ]
    detail = [
        ("Test procedure", lambda c: e(c["proc"]), True),
        ("Condition", lambda c: e(c["condition"]), False),
        ("Criteria", lambda c: e(c["criteria"]), False),
        ("Cause", lambda c: e(c["cause"]), False),
        ("Effect", lambda c: e(c["effect"]), False),
        ("Recommendation", lambda c: e(c["rec"]), False),
        ("Management response", lambda c: e(c["resp"]), False),
        ("NIST SP 800-53 Rev. 5", lambda c: e(c["nist"]), False),
        ("Related records · due date", lambda c: f'{xref(c["links"], "it-audit")} · {e(fmt_date(c["due"]))}', False),
    ]
    filters = [("area", "Area", areas, lambda c: c["area"]), ("result", "Result", order, lambda c: c["result"])]
    csv = (["ID","Area","Control","Frequency","Test procedure","Population","Sample","Exceptions","Result","Condition","Criteria","Cause","Effect","Recommendation","Management response","Owner","Due","NIST 800-53","Related"],
           [[c["id"],c["area"],c["control"],c["freq"],c["proc"],c["pop"],c["sample"],c["exc"],c["result"],c["condition"],c["criteria"],c["cause"],c["effect"],c["rec"],c["resp"],c["owner"],c["due"],c["nist"],c["links"]] for c in cs])
    return dict(
        slug="it-audit", kicker="IT audit",
        lede="An internal audit of 14 IT general controls over access, change management, IT operations and governance. Each control was tested for design and operating effectiveness with a defined sample, and every exception is written up as condition, criteria, cause and effect with a management response.",
        frameworks=["COSO 2013", "NIST SP 800-53 Rev. 5", "AICPA TSC (SOC 2)", "IIA Global Internal Audit Standards"],
        period="Fieldwork Jun – Sep 2026 (period under review Jan 1 – Aug 31, 2026)",
        glance=[("Objective","Give the audit committee assurance that ITGCs supporting PHI systems and the SOC 2 report operate effectively."),
                ("Scope","Entra ID, AWS production accounts, GitHub deployment pipeline, AWS Backup, SIEM, and the policy library."),
                ("Approach","Inquiry, inspection and reperformance. Samples drawn at random from system-generated populations."),
                ("Criteria","NovaCare policies and standards, mapped to NIST SP 800-53 and the SOC 2 common criteria.")],
        kpis=[(str(len(cs)),"controls tested",False),(str(res["Effective"]),"operating effectively",False),
              (str(res["Deficiency"] + res["Significant deficiency"]),f'deficiencies, {res["Significant deficiency"]} of them significant',True),
              (f"{tested}",f"items inspected, {exc} exceptions",False)],
        rating=(2, "Change management and training controls work. Two significant deficiencies, in privileged access review and restore testing, need correction before the next SOC 2 period."),
        findings=[("ITGC-02","Privileged access reviews skip AWS entirely","Reperforming the Q2 review found 4 engineers who had changed roles but kept AdministratorAccess in production. Management removed them on Sep 12."),
                  ("ITGC-09","Tier 1 restore tests were not performed","No tests in Q1 or Q2. The Q3 EHR hub restore took 31 hours against a 4-hour RTO."),
                  ("ITGC-01, ITGC-12","Account lifecycle depends on manual steps","12% of sampled leavers stayed active for 6–14 days, and 27% of service accounts have no owner."),
                  ("ITGC-05","Admins could bypass deployment controls","2 of 25 deployments had no change ticket. The bypass was removed during fieldwork.")],
        charts=charts,
        reg=register(cs, cols, detail, filters, "../../downloads/03-itgc-testing.csv", "Search controls, findings, owners…", noun="controls"),
        csv=("downloads/03-itgc-testing.csv",) + csv,
        method_steps=["Walk through each control with its owner to confirm design.","Obtain a complete, system-generated population and confirm its completeness.",
                      "Select a random sample sized to the control frequency.","Inspect or reperform each sample item and document exceptions.",
                      "Write findings in condition, criteria, cause, effect form and agree management responses.","Retest remediated controls before closing findings."],
        criteria=("Sample sizes and ratings", ["Frequency","Sample","Rating used"],
                  [["Annual","1","Effective: no exceptions"],["Quarterly","2","Deficiency: exception or design gap, limited impact"],["Monthly","2","Significant deficiency: control not operating; PHI or report at risk"],
                   ["Weekly","5",""],["Daily / per event","25",""]]),
    )

def spec_vuln():
    fs = FINDINGS
    openf = [f for f in fs if f["is_open"]]
    overdue = [f for f in fs if f["sla_state"] == "Overdue"]
    closed = [f for f in fs if not f["is_open"]]
    prios = ["Critical", "High", "Moderate", "Low"]
    states = ["Met", "Within SLA", "Overdue", "Exception"]
    segc = {"Met": "seg-low", "Within SLA": "seg-acc", "Overdue": "seg-crit", "Exception": "seg-none"}
    byp = hbars([(f"{p} · {SLA[p]}-day SLA", [(sum(1 for f in fs if f["prio"] == p and f["sla_state"] == s), segc[s], s) for s in states],
                  str(sum(1 for f in fs if f["prio"] == p)), f"prio:{p}") for p in prios])
    mean_age = sum(f["age"] for f in openf) / len(openf)
    charts = f"""<div class="charts">
<div class="panel"><h3>SLA performance by priority</h3><p class="sub">All 16 POA&amp;M items. Select a priority to filter.</p>{byp}
{legend([("Closed within SLA","seg-low"),("Open, within SLA","seg-acc"),("Overdue","seg-crit"),("Risk-accepted exception","seg-none")])}</div>
<div class="panel"><h3>Age of open findings against SLA</h3><p class="sub">Bar length is days open on Oct 31, 2026, coloured by priority; the tick is the SLA. Solid bars and red figures are overdue.</p>{age_chart(fs)}</div>
</div>"""
    sc = {"Met": "low", "Within SLA": "plain", "Overdue": "crit", "Exception": "plain"}
    cols = [
        dict(key="id", label="ID", html=lambda f: e(f["id"]), cls="id"),
        dict(key="title", label="Finding", html=lambda f: f'<b>{e(f["title"])}</b><br><span class="muted">{e(f["asset"])}</span>'),
        dict(key="cvss", label="CVSS", html=lambda f: f'<span class="mono">{f["cvss"]:.1f}</span>', sort=lambda f: f["cvss"], numeric=True, cls="n"),
        dict(key="prio", label="Priority", html=lambda f: pill(f["prio"]), sort=lambda f: 3 - prios.index(f["prio"]), numeric=True),
        dict(key="due", label="SLA due", html=lambda f: e(fmt_date(f["due"])), sort=lambda f: f["due"], cls="n"),
        dict(key="age", label="Age", html=lambda f: f'<span class="mono">{f["age"]}d</span>', sort=lambda f: f["age"], numeric=True, cls="n"),
        dict(key="status", label="Status", html=lambda f: f'{e(f["status"])}<br>{pill(f["sla_state"], sc[f["sla_state"]])}', sort=lambda f: f["status"]),
    ]
    detail = [
        ("Reference", lambda f: e(f["ref"]), False),
        ("Asset · tier · exposure", lambda f: f'{e(f["asset"])} · Tier {f["tier"]} · {e(f["exposure"])}', False),
        ("Prioritization", lambda f: f'CVSS {f["cvss"]:.1f} ({e(f["base"])}) adjusted for exposure and asset tier → {e(f["prio"])}, {f["sla"]}-day SLA', True),
        ("Milestone / action", lambda f: e(f["milestone"]), True),
        ("Discovered · due · closed", lambda f: f'{e(fmt_date(f["discovered"]))} · {e(fmt_date(f["due"]))} · {e(fmt_date(f["closed"]) if f["closed"] else "open")}', False),
        ("Owner · related", lambda f: f'{e(f["owner"])} · {xref(f["links"], "vulnerability-management")}', False),
    ]
    filters = [("prio", "Priority", prios, lambda f: f["prio"]), ("sla", "SLA status", states, lambda f: f["sla_state"]),
               ("exposure", "Exposure", ["Internet", "Internal"], lambda f: f["exposure"])]
    csv = (["ID","Finding","Reference","CVSS v3.1","Base severity","Asset","Asset tier","Exposure","Priority","SLA days","Discovered","SLA due","Closed","Age (days)","Status","SLA status","Owner","Milestone","Related"],
           [[f["id"],f["title"],f["ref"],f["cvss"],f["base"],f["asset"],f["tier"],f["exposure"],f["prio"],f["sla"],f["discovered"],f["due"],f["closed"],f["age"],f["status"],f["sla_state"],f["owner"],f["milestone"],f["links"]] for f in fs])
    return dict(
        slug="vulnerability-management", kicker="Vulnerability management",
        lede="A plan of action and milestones (POA&M) for the 16 most significant vulnerabilities from FY2026 scanning, penetration testing and configuration reviews. Priority combines CVSS with asset criticality and exposure, and every item has an SLA, owner and milestone.",
        frameworks=["NIST SP 800-40 Rev. 4", "NIST SP 800-53 RA-5, SI-2, CA-5", "CVSS v3.1", "CISA BOD 22-01 (practice)"],
        period="Findings Feb – Oct 2026; status as of Oct 31, 2026",
        glance=[("Objective","Turn raw scanner output into a prioritized, owned remediation plan that leadership can track."),
                ("Scope","16 POA&M items drawn from about 2,300 scanner results, the 2026 penetration test, and secrets and configuration scans."),
                ("Approach","De-duplicate, validate exploitability, adjust CVSS for exposure and asset tier, assign owners, track to verified closure."),
                ("Criteria","Remediation SLAs: Critical 15 days, High 30, Moderate 90, Low 180. Exceptions need a signed risk acceptance.")],
        kpis=[(str(len(fs)),"POA&M items tracked",False),(str(len(overdue)),"open items past SLA",True),
              (f"{len(closed)}",f"closed and verified by retest",False),(f"{mean_age:.0f} days","average age of open items",False)],
        rating=(2, "Findings are now owned and prioritized, but 8 open items are past SLA, including three Criticals. Two of those have compensating controls in place."),
        findings=[("VM-01","Log4Shell is still present on an internet-facing gateway","The legacy fax-to-EHR gateway is 58 days past SLA. A WAF rule and egress block contain it until the replacement goes live on Dec 15."),
                  ("VM-06","A production database password sat in source code","Rotated within a day of discovery. Ten more secrets are being rotated and push protection is now on."),
                  ("VM-05","End-of-life servers handled through formal acceptance","Seven Windows Server 2012 R2 hosts run under exception RA-2026-03, isolated on a restricted VLAN until migration in March 2027."),
                  ("Program","Ownership was the root cause of delay","31% of findings had no owner at the start of the year (R-19). Ownership by asset tag and CISO escalation at day 10 are now in the standard.")],
        charts=charts,
        reg=register(fs, cols, detail, filters, "../../downloads/04-poam.csv", "Search findings, assets, owners…", noun="items"),
        csv=("downloads/04-poam.csv",) + csv,
        method_steps=["Aggregate scanner, pen-test and configuration findings into one list.","Remove duplicates and false positives; confirm exploitability for Critical and High.",
                      "Adjust severity for exposure and asset tier, then set the SLA due date.","Assign an owner and a dated milestone; record compensating controls.",
                      "Escalate overdue Criticals to the CISO; require signed acceptance for exceptions.","Close only after a rescan or retest confirms the fix."],
        criteria=("Prioritization rule", ["Adjustment","Effect"],
                  [["Internet-facing and Tier 1 asset","Raise one level"],["Internal and Tier 3 asset","Lower one level"],["All others","Keep CVSS v3.1 base severity"],
                   ["Known exploited (KEV) or public exploit","Treat as Critical regardless"]]),
    )

def spec_tprm():
    vs = VENDORS
    tiers = [1, 2, 3, 4]
    resid = ["High", "Moderate", "Low"]
    def cls(r, c): return {"High": "crit", "Moderate": "mod", "Low": "low"}[c]
    mtx = matrix([f"Tier {t}" for t in tiers], resid,
                 lambda r, c: sum(1 for v in vs if f'Tier {v["tier"]}' == r and v["residual"] == c),
                 cls, lambda r, c: f"residual:{c}", corner="Tier \\ residual")
    dec = Counter(v["decision"] for v in vs)
    decs = ["Approve", "Approve with conditions", "Remediate before renewal"]
    segd = {"Approve": "seg-low", "Approve with conditions": "seg-mod", "Remediate before renewal": "seg-crit"}
    decb = hbars([(d, [(dec[d], segd[d], d)], str(dec[d]), f"decision:{d}") for d in decs], total=len(vs))
    phi = [v for v in vs if "PHI" in v["data"]]
    nobaa = [v for v in vs if "PHI" in v["data"] and v["baa"] == "No"]
    charts = f"""<div class="charts">
<div class="panel"><h3>Inherent tier against residual risk</h3><p class="sub">Tier reflects what the vendor can reach; residual reflects what the review found. Select a cell to filter.</p>{mtx}</div>
<div class="panel"><h3>Review decisions</h3><p class="sub">Outcome of each review. Select a decision to filter.</p>{decb}
<p class="sub" style="margin-top:8px">{len(phi)} of {len(vs)} vendors handle PHI. {len(nobaa)} of those had no business associate agreement at review.</p></div>
</div>"""
    rc = {"High": "crit", "Moderate": "mod", "Low": "low"}
    dc = {"Approve": "low", "Approve with conditions": "mod", "Remediate before renewal": "crit"}
    cols = [
        dict(key="id", label="ID", html=lambda v: e(v["id"]), cls="id"),
        dict(key="name", label="Vendor", html=lambda v: f'<b>{e(v["name"])}</b><br><span class="muted">{e(v["service"])}</span>'),
        dict(key="tier", label="Tier", html=lambda v: e(v["tier_label"]), sort=lambda v: v["tier"], numeric=True),
        dict(key="data", label="Data", html=lambda v: e(v["data"])),
        dict(key="residual", label="Residual", html=lambda v: pill(v["residual"], rc[v["residual"]]), sort=lambda v: resid.index(v["residual"])),
        dict(key="decision", label="Decision", html=lambda v: pill(v["decision"], dc[v["decision"]]), sort=lambda v: decs.index(v["decision"])),
        dict(key="next", label="Next review", html=lambda v: e(fmt_date(v["next"])), sort=lambda v: v["next"], cls="n"),
    ]
    detail = [
        ("Access", lambda v: e(v["access"]), False),
        ("Business associate agreement", lambda v: e(v["baa"]), False),
        ("Assurance reviewed", lambda v: e(v["assurance"]), True),
        ("Key findings", lambda v: e(v["findings"]), True),
        ("Conditions / required actions", lambda v: e(v["conditions"]), True),
        ("Owner · related", lambda v: f'{e(v["owner"])} · {xref(v["links"], "third-party-risk")}', False),
    ]
    filters = [("tier", "Tier", ["Tier 1", "Tier 2", "Tier 3", "Tier 4"], lambda v: f'Tier {v["tier"]}'),
               ("residual", "Residual", resid, lambda v: v["residual"]), ("decision", "Decision", decs, lambda v: v["decision"])]
    csv = (["ID","Vendor","Service","Data","Access","Tier","Assurance reviewed","BAA","Key findings","Residual risk","Decision","Conditions","Owner","Next review","Related"],
           [[v["id"],v["name"],v["service"],v["data"],v["access"],v["tier_label"],v["assurance"],v["baa"],v["findings"],v["residual"],v["decision"],v["conditions"],v["owner"],v["next"],v["links"]] for v in vs])
    return dict(
        slug="third-party-risk", kicker="Third-party risk",
        lede="A risk-based review of 12 of NovaCare's 62 vendors, including every Tier 1 supplier. Vendors are tiered by what they can reach, assessed against their SOC 2, ISO and questionnaire evidence, and given a documented decision with conditions.",
        frameworks=["NIST CSF 2.0 GV.SC", "NIST SP 800-161 Rev. 1", "AICPA SOC 2", "Shared Assessments SIG", "HIPAA §164.308(b)"],
        period="Jul – Sep 2026; status as of Oct 31, 2026",
        glance=[("Objective","Establish a repeatable tiering and review process and clear the backlog of unreviewed critical vendors."),
                ("Scope","12 vendors: all Tier 1 vendors, every vendor with PHI access, and a sample of lower tiers."),
                ("Approach","Inherent-risk questionnaire for tiering, review of SOC reports (opinion, exceptions, CUECs, bridge letters), contract and BAA checks."),
                ("Criteria","Tier 1 reassessed annually, Tier 2 every 2 years, Tier 3–4 at renewal. PHI access requires a signed BAA.")],
        kpis=[(str(len(vs)),"vendors reviewed",False),(str(sum(1 for v in vs if v["tier"]==1)),"Tier 1 critical vendors",False),
              (str(sum(1 for v in vs if v["residual"]=="High")),"with High residual risk",True),(str(len(nobaa)),"PHI vendor without a BAA",True)],
        rating=(3, "Half the vendors reviewed are well controlled. Six need conditions or remediation, and one handles PHI without a business associate agreement."),
        findings=[("TPR-02","The EHR partner's SOC 2 opinion is qualified","Shared admin accounts at Clinilink, plus an any-to-any VPN tunnel into NovaCare's hub. Approved only with a corrective action plan and network restriction."),
                  ("TPR-06","PHI is in a support tool with no BAA","Agents attach patient documents in Helpdesko. Renewal is blocked until a BAA is signed and retention is limited."),
                  ("TPR-07","The AI transcription contract allowed model training","An amendment to prohibit training and require US-only processing is a condition of approval (see AI-04)."),
                  ("TPR-11","Contractor technicians share accounts","Two generic remote-support accounts with no session recording. Access suspended until named accounts with MFA are issued.")],
        charts=charts,
        reg=register(vs, cols, detail, filters, "../../downloads/05-vendor-reviews.csv", "Search vendors, findings, conditions…", noun="vendors"),
        csv=("downloads/05-vendor-reviews.csv",) + csv,
        method_steps=["Classify each vendor with the inherent-risk questionnaire to set its tier.","Collect assurance: SOC 2 Type II, ISO certificates, SIG responses, pen-test summaries.",
                      "Review SOC reports for opinion, exceptions, period coverage, bridge letters and CUECs.","Check contracts for BAA, breach notice, audit rights and data location terms.",
                      "Rate residual risk and record a decision with conditions and an owner.","Schedule the next review by tier and track conditions to closure."],
        criteria=("Tiering", ["Tier","Profile","Reassessment"],
                  [["1 · Critical","PHI at scale or production access; hard to replace","Annual"],["2 · High","PHI or employee PII, limited access","Every 2 years"],
                   ["3 · Moderate","Limited personal data, low integration","At renewal"],["4 · Low","No sensitive data","At renewal"]]),
    )

def spec_cloud():
    cs = CHECKS
    res = Counter(c["result"] for c in cs)
    order = ["Pass", "Partial", "Fail"]
    segc = {"Pass": "seg-low", "Partial": "seg-mod", "Fail": "seg-crit"}
    plats = ["Entra ID", "Entra ID / AD", "Microsoft 365", "AWS"]
    plats = [p for p in plats if any(c["platform"] == p for c in cs)]
    byp = hbars([(p, [(sum(1 for c in cs if c["platform"] == p and c["result"] == s), segc[s], s) for s in order],
                  f'{sum(1 for c in cs if c["platform"]==p and c["result"]=="Pass")}/{sum(1 for c in cs if c["platform"]==p)}', f"platform:{p}") for p in plats])
    ident = [c for c in cs if c["platform"].startswith("Entra")]
    charts = f"""<div class="charts one">
<div class="panel"><h3>Results by platform</h3><p class="sub">The figure on the right is controls that passed. Select a platform to filter.</p>{byp}
{legend([("Pass","seg-low"),("Partial","seg-mod"),("Fail","seg-crit")])}</div>
</div>"""
    rc = {"Pass": "low", "Partial": "mod", "Fail": "crit"}
    cols = [
        dict(key="id", label="ID", html=lambda c: e(c["id"]), cls="id"),
        dict(key="control", label="Control", html=lambda c: f'<b>{e(c["control"])}</b><br><span class="muted">{e(c["platform"])}</span>'),
        dict(key="bench", label="Benchmark", html=lambda c: f'<span class="mono">{e(c["bench"])}</span>'),
        dict(key="result", label="Result", html=lambda c: pill(c["result"], rc[c["result"]]), sort=lambda c: order.index(c["result"])),
        dict(key="owner", label="Owner", html=lambda c: e(c["owner"])),
        dict(key="due", label="Due", html=lambda c: e(fmt_date(c["due"])), sort=lambda c: c["due"], cls="n"),
    ]
    detail = [
        ("Test performed", lambda c: e(c["test"]), False),
        ("Evidence observed", lambda c: e(c["evidence"]), False),
        ("Recommendation", lambda c: e(c["rec"]), True),
        ("NIST SP 800-53 Rev. 5", lambda c: e(c["nist"]), False),
        ("Related records", lambda c: xref(c["links"], "cloud-iam"), False),
    ]
    filters = [("platform", "Platform", plats, lambda c: c["platform"]), ("result", "Result", order, lambda c: c["result"])]
    csv = (["ID","Platform","Control","Benchmark","NIST 800-53","Test performed","Result","Evidence observed","Recommendation","Owner","Due","Related"],
           [[c["id"],c["platform"],c["control"],c["bench"],c["nist"],c["test"],c["result"],c["evidence"],c["rec"],c["owner"],c["due"],c["links"]] for c in cs])
    return dict(
        slug="cloud-iam", kicker="Cloud & identity",
        lede="A technical control assessment of NovaCare's identity platform and AWS environment. Fifteen controls were tested against CIS and CISA SCuBA baselines using configuration exports and logs, with the evidence observed recorded for each.",
        frameworks=["CIS AWS Foundations v3.0.0", "CISA SCuBA (Entra ID, M365)", "NIST SP 800-53 Rev. 5", "Zero Trust (NIST SP 800-207)"],
        period="Aug – Sep 2026; status as of Oct 31, 2026",
        glance=[("Objective","Verify that identity and cloud controls the risk register depends on are configured as intended."),
                ("Scope","Entra ID tenant, on-prem AD service accounts, Microsoft 365 sharing, and all 6 AWS accounts."),
                ("Approach","Read-only configuration exports, Access Analyzer and sign-in log review; no changes made during testing."),
                ("Criteria","CIS AWS Foundations v3.0.0, CISA SCuBA secure configuration baselines, NovaCare access standards.")],
        kpis=[(str(len(cs)),"controls tested",False),(str(res["Pass"]),"passed",False),(str(res["Fail"]),"failed",True),
              (f'{sum(1 for c in ident if c["result"]=="Fail")} of {len(ident)}',"identity controls failed",True)],
        rating=(2, "AWS foundations (root, logging, encryption) are solid. Identity is the weak point: privileged access, lifecycle automation and service accounts all failed."),
        findings=[("CIA-01, CIA-02","Every privileged role is permanent","38 standing admin assignments, 9 Global Administrators, and 14 admins on push MFA. Moving to PIM with phishing-resistant MFA addresses R-01."),
                  ("CIA-08","Wildcard permissions on PHI data stores","Six roles hold rds:* and s3:* on PHI resources; Access Analyzer flags 112 unused permissions."),
                  ("CIA-06, CIA-07","Identity lifecycle is manual","No HR-driven provisioning, 9 apps outside SSO, and 23 ownerless service accounts, 4 with Domain Admin."),
                  ("CIA-09, CIA-11, CIA-13","Cloud foundations pass","Organization-wide CloudTrail, hardware MFA on all root users and customer-managed KMS encryption on every PHI store.")],
        charts=charts,
        reg=register(cs, cols, detail, filters, "../../downloads/06-cloud-iam-tests.csv", "Search controls, evidence, owners…", noun="controls"),
        csv=("downloads/06-cloud-iam-tests.csv",) + csv,
        method_steps=["Select controls from CIS and SCuBA baselines that support risks in the register.","Obtain read-only access and export configurations and logs.",
                      "Test each control and record the evidence observed, with counts.","Rate Pass, Partial or Fail against the baseline requirement.",
                      "Recommend the specific configuration change and owner.","Retest after remediation and update the linked risks."],
        criteria=("Result definitions", ["Result","Meaning"],
                  [["Pass","Meets the baseline in all accounts or tenants tested"],["Partial","Configured but with exclusions, gaps in coverage or no monitoring"],
                   ["Fail","Not configured, or configured in a way that defeats the control"]]),
    )

def spec_bcdr():
    ss = SERVICES
    ready = Counter(s["ready"] for s in ss)
    t1 = [s for s in ss if s["tier"] == 1]
    charts = f"""<div class="charts one">
<div class="panel"><h3>Recovery time: target versus tested</h3><p class="sub">Log scale, hours. Shaded bar is the RTO, the dot is the most recent timed test (green met, red missed), the black tick is the maximum tolerable downtime.</p>{rto_chart(ss)}
{legend([("Target RTO","seg-acc"),("Tested, met RTO","seg-low"),("Tested, missed RTO","seg-crit"),("Maximum tolerable downtime (tick)","seg-ink")])}</div>
</div>"""
    rc = {"Meets RTO": "low", "Misses RTO": "crit", "Not tested": "plain"}
    cols = [
        dict(key="id", label="ID", html=lambda s: e(s["id"]), cls="id"),
        dict(key="service", label="Service", html=lambda s: f'<b>{e(s["service"])}</b><br><span class="muted">Business owner: {e(s["bowner"])}</span>'),
        dict(key="tier", label="Tier", html=lambda s: f'<span class="mono">{s["tier"]}</span>', sort=lambda s: s["tier"], numeric=True, cls="n"),
        dict(key="rto", label="RTO / RPO", html=lambda s: f'<span class="mono">{s["rto"]:g}h / {s["rpo"]:g}h</span>', sort=lambda s: s["rto"], numeric=True, cls="n"),
        dict(key="mtd", label="MTD", html=lambda s: f'<span class="mono">{s["mtd"]:g}h</span>', sort=lambda s: s["mtd"], numeric=True, cls="n"),
        dict(key="trto", label="Tested RTO", html=lambda s: f'<span class="mono">{"—" if s["trto"] is None else f"{s["trto"]:g}h"}</span>', sort=lambda s: -1 if s["trto"] is None else s["trto"], numeric=True, cls="n"),
        dict(key="ready", label="Readiness", html=lambda s: pill(s["ready"], rc[s["ready"]])),
    ]
    detail = [
        ("Impact if unavailable", lambda s: e(s["impact"]), False),
        ("Dependencies", lambda s: e(s["deps"]), False),
        ("Last timed test", lambda s: e(fmt_date(s["last"]) if s["last"] else "Never tested") + (f' · tested RPO {s["trpo"]:g}h' if s["trpo"] is not None else ""), False),
        ("Recovery owner · due", lambda s: f'{e(s["owner"])} · {e(fmt_date(s["due"]))}', False),
        ("Gap and action", lambda s: e(s["gap"]), True),
        ("Related records", lambda s: xref(s["links"], "business-continuity"), False),
    ]
    filters = [("tier", "Tier", ["1", "2", "3", "4"], lambda s: str(s["tier"])), ("ready", "Readiness", ["Meets RTO", "Misses RTO", "Not tested"], lambda s: s["ready"])]
    csv = (["ID","Service","Business owner","Tier","MTD (h)","RTO (h)","RPO (h)","Tested RTO (h)","Tested RPO (h)","Last test","Readiness","Dependencies","Impact","Gap and action","Owner","Due","Related"],
           [[s["id"],s["service"],s["bowner"],s["tier"],s["mtd"],s["rto"],s["rpo"],s["trto"] if s["trto"] is not None else "",s["trpo"] if s["trpo"] is not None else "",s["last"],s["ready"],s["deps"],s["impact"],s["gap"],s["owner"],s["due"],s["links"]] for s in ss])
    return dict(
        slug="business-continuity", kicker="Resilience",
        lede="A business impact analysis of 10 services that sets maximum tolerable downtime, RTO and RPO with each business owner, then compares those targets with the results of real timed recovery tests.",
        frameworks=["NIST SP 800-34 Rev. 1", "ISO 22301:2019", "HIPAA §164.308(a)(7)", "NIST CSF 2.0 RC"],
        period="May – Sep 2026; status as of Oct 31, 2026",
        glance=[("Objective","Agree recovery targets with the business and find where technical recovery capability falls short."),
                ("Scope","10 business services, from the patient portal (Tier 1) to the corporate website (Tier 4)."),
                ("Approach","BIA interviews with business owners, dependency mapping, review of timed restore and failover exercise records."),
                ("Criteria","Tested RTO must be within target; target RTO must sit well inside MTD. Tier 1 services tested quarterly.")],
        kpis=[(str(len(ss)),"services analysed",False),(str(len(t1)),"Tier 1 services",False),
              (str(ready["Not tested"]),"services never recovery-tested",True),(str(ready["Misses RTO"]),"tested service missed its RTO",True)],
        rating=(2, "Five services met their targets in testing. The EHR integration hub took 31 hours against a 4-hour RTO, and one Tier 1 service has never been tested."),
        findings=[("BIA-02","The EHR hub's last recovery took longer than clinics can tolerate","31 hours, against a 4-hour RTO and an 8-hour MTD set by the CTO and CMIO. Manual queue rebuild was the bottleneck."),
                  ("BIA-03","Claims processing has never been restored","Its backups share the production account with no object lock, so ransomware could take both (see R-02)."),
                  ("BIA-08","No fallback when security monitoring is down","If the SIEM is unavailable there is no agreed way to keep watching for attacks."),
                  ("BIA-01, BIA-04","Portal and identity recover within target","Both met RTO in 2026 exercises, which shows the testing approach works and can be extended.")],
        charts=charts,
        reg=register(ss, cols, detail, filters, "../../downloads/07-bia-recovery.csv", "Search services, dependencies, gaps…", noun="services"),
        csv=("downloads/07-bia-recovery.csv",) + csv,
        method_steps=["Interview business owners to describe impact over time if each service stops.","Set MTD from the point impact becomes unacceptable; derive RTO and RPO inside it.",
                      "Map technology and vendor dependencies for each service.","Collect results of the most recent timed recovery for each service.",
                      "Compare tested results with targets and record gaps with owners.","Schedule tests by tier and feed gaps into the risk register."],
        criteria=("Service tiers", ["Tier","Typical RTO","Test frequency"],
                  [["1","≤ 4 hours","Quarterly"],["2","≤ 24 hours","Semi-annually"],["3","≤ 72 hours","Annually"],["4","Best effort","Annually"]]),
    )

def spec_ai():
    us = USECASES
    tiers = ["High", "Medium", "Low"]
    stats = ["Approved", "Approved with conditions", "Under review", "Paused", "Prohibited"]
    def cls(r, c): return {"High": "crit", "Medium": "mod", "Low": "low"}[r]
    mtx = matrix(tiers, stats, lambda r, c: sum(1 for u in us if u["tier"] == r and u["status"] == c), cls,
                 lambda r, c: f"status:{c}", corner="Tier \\ status")
    funcs = ["GOVERN", "MAP", "MEASURE", "MANAGE"]
    gapc = {f: sum(1 for u in us if f + ":" in u["gaps"]) for f in funcs}
    gb = hbars([(f.title(), [(gapc[f], "seg-acc", f)], f"{gapc[f]} use cases", f"gap:{f.title()}") for f in funcs], total=len(us))
    charts = f"""<div class="charts">
<div class="panel"><h3>Risk tier against decision</h3><p class="sub">Select a cell to filter the inventory.</p>{mtx}</div>
<div class="panel"><h3>Gaps by NIST AI RMF function</h3><p class="sub">Number of use cases with at least one gap in each function. Measure gaps are the most common: few models have been tested for accuracy or bias.</p>{gb}</div>
</div>"""
    tc = {"High": "crit", "Medium": "mod", "Low": "low"}
    sc = {"Approved": "low", "Approved with conditions": "mod", "Under review": "plain", "Paused": "high", "Prohibited": "crit"}
    cols = [
        dict(key="id", label="ID", html=lambda u: e(u["id"]), cls="id"),
        dict(key="name", label="Use case", html=lambda u: f'<b>{e(u["name"])}</b><br><span class="muted">{e(u["vendor"])}</span>'),
        dict(key="data", label="Data", html=lambda u: e(u["data"])),
        dict(key="tier", label="Risk tier", html=lambda u: pill(u["tier"], tc[u["tier"]]), sort=lambda u: tiers.index(u["tier"])),
        dict(key="status", label="Decision", html=lambda u: pill(u["status"], sc[u["status"]]), sort=lambda u: stats.index(u["status"])),
        dict(key="owner", label="Owner", html=lambda u: e(u["owner"])),
    ]
    detail = [
        ("Purpose", lambda u: e(u["purpose"]), False),
        ("Decision impact", lambda u: e(u["impact"]), False),
        ("Human oversight", lambda u: e(u["human"]), False),
        ("Business owner · next review", lambda u: f'{e(u["bowner"])} · {e(fmt_date(u["review"]))}', False),
        ("Gaps by AI RMF function", lambda u: e(u["gaps"]), True),
        ("Conditions and next steps", lambda u: e(u["conditions"]), True),
        ("Related records", lambda u: xref(u["links"], "ai-governance"), False),
    ]
    filters = [("tier", "Risk tier", tiers, lambda u: u["tier"]), ("status", "Decision", stats, lambda u: u["status"]),
               ("gap", "Gap area", [f.title() for f in funcs], lambda u: [f.title() for f in funcs if f + ":" in u["gaps"]])]
    csv = (["ID","Use case","Business owner","Purpose","Data","Decision impact","Human oversight","Vendor / model","Risk tier","Decision","Gaps","Conditions","Owner","Next review","Related"],
           [[u["id"],u["name"],u["bowner"],u["purpose"],u["data"],u["impact"],u["human"],u["vendor"],u["tier"],u["status"],u["gaps"],u["conditions"],u["owner"],u["review"],u["links"]] for u in us])
    return dict(
        slug="ai-governance", kicker="AI governance",
        lede="An inventory and risk review of 10 AI use cases at NovaCare, from a patient-facing symptom checker to unapproved public chatbots. Each use case is tiered, assessed against the four NIST AI RMF functions, and given a decision by the AI Review Board.",
        frameworks=["NIST AI RMF 1.0", "NIST AI 600-1 (GenAI profile)", "ISO/IEC 42001:2023", "HIPAA Privacy & Security Rules"],
        period="Aug – Oct 2026; status as of Oct 31, 2026",
        glance=[("Objective","Give leadership a complete view of where AI is used and a consistent way to approve, condition or stop it."),
                ("Scope","10 use cases found through a staff survey, procurement records and proxy logs, including shadow AI."),
                ("Approach","Use-case intake form, data-flow review, vendor contract review, and gap assessment against AI RMF Govern, Map, Measure and Manage."),
                ("Criteria","High tier: affects clinical, hiring or financial decisions about people, or handles PHI with limited human review.")],
        kpis=[(str(len(us)),"AI use cases inventoried",False),(str(sum(1 for u in us if u["tier"]=="High")),"High-risk use cases",True),
              (str(sum(1 for u in us if u["status"] in ("Paused","Prohibited","Under review"))),"paused, prohibited or on hold",False),
              (str(gapc["MEASURE"]),"use cases with untested accuracy, bias or drift",True)],
        rating=(3, "Low-risk internal uses are well governed. The program now needs testing evidence for High-risk use cases and a policy that stops PHI from reaching public AI tools."),
        findings=[("AI-01","Patient symptom checker paused","It gave care-level advice with no clinical validation and no red-flag escalation. Restart requires a validation study and CMIO sign-off."),
                  ("AI-09","340 staff used 11 unapproved AI services in one month","No AI acceptable-use policy exists. An approved enterprise assistant and a block for PHI users are the fix (R-21)."),
                  ("AI-05","Resume screening on hold pending a bias audit","The tool decides who gets an interview and has never been tested for adverse impact."),
                  ("AI-04","Transcription approved with contract conditions","Model-training rights removed, US-only processing required, and medication-name accuracy to be measured on 200 notes.")],
        charts=charts,
        reg=register(us, cols, detail, filters, "../../downloads/08-ai-use-cases.csv", "Search use cases, gaps, owners…", noun="use cases"),
        csv=("downloads/08-ai-use-cases.csv",) + csv,
        method_steps=["Build the inventory from a survey, procurement records and network logs.","Complete an intake form for each use case: purpose, data, decisions affected, human oversight.",
                      "Assign a risk tier using the criteria table.","Assess gaps against AI RMF Govern, Map, Measure and Manage.",
                      "Present to the AI Review Board for a decision and conditions.","Re-review High-tier use cases every 6 months and after model changes."],
        criteria=("Risk tiers", ["Tier","Criteria","Review"],
                  [["High","Clinical, hiring or financial decisions about people; or PHI with limited human review","Board decision; 6-month review"],
                   ["Medium","PHI or personal data with a human reviewing every output","Board decision; annual review"],["Low","No personal data; low-impact internal use","Owner approval; annual review"]]),
    )

SPECS = [spec_risk, spec_csf, spec_audit, spec_vuln, spec_tprm, spec_cloud, spec_bcdr, spec_ai]

# ---------------------------------------------------------------- render
def render_project(p, idx, all_specs):
    slug = p["slug"]; num = f"{idx+1:02d}"; title = TITLES[slug]
    prev_s = all_specs[idx-1] if idx > 0 else None
    next_s = all_specs[idx+1] if idx < len(all_specs)-1 else None
    level, rtext = p["rating"]
    scale = "".join(f'<i class="{"on" if k < level else ""}"></i>' for k in range(4))
    kpis = "".join(f'<div class="kpi{" warn" if w else ""}"><b>{e(v)}</b><span>{e(l)}</span></div>' for v, l, w in p["kpis"])
    glance = "".join(f'<div><span class="label">{e(k)}</span><p>{e(v)}</p></div>' for k, v in p["glance"])
    finds = "".join(f'<article><span class="ref">{e(r)}</span><div><h3>{e(t)}</h3><p>{e(x)}</p></div></article>' for r, t, x in p["findings"])
    steps = "".join(f"<li>{e(s)}</li>" for s in p["method_steps"])
    ctitle, chead, crows = p["criteria"]
    ctable = "<table><thead><tr>" + "".join(f"<th>{e(h)}</th>" for h in chead) + "</tr></thead><tbody>" + \
             "".join("<tr>" + "".join(f"<td>{e(c)}</td>" for c in r) + "</tr>" for r in crows) + "</tbody></table>"
    rel = p.get("related") or []
    related = "".join(f'<a href="../{s}/"><b>{e(TITLES[s])}</b><span>Project {ORDER.index(s)+1:02d}</span></a>' for s in rel[:3])
    nav = [("Summary", "#summary"), ("Register", "#register"), ("Method", "#method"), ("All projects", "../../#work")]
    pager = ""
    if prev_s: pager += f'<a href="../{prev_s["slug"]}/"><span>← Previous · {idx:02d}</span>{e(TITLES[prev_s["slug"]])}</a>'
    if next_s: pager += f'<a class="next" href="../{next_s["slug"]}/"><span>Next · {idx+2:02d} →</span>{e(TITLES[next_s["slug"]])}</a>'
    fw = "".join(f'<span class="chip">{e(f)}</span>' for f in p["frameworks"])
    body = f"""{topbar(2, nav)}
<main id="main">
<header class="p-head"><div class="wrap">
<nav class="crumbs" aria-label="Breadcrumb"><a href="../../">Portfolio</a><span aria-hidden="true">/</span><a href="../../#work">Assessments</a><span aria-hidden="true">/</span><span>Project {num}</span></nav>
<span class="label">Project {num} · {e(p["kicker"])}</span>
<h1>{e(title)}</h1>
<p class="lede">{e(p["lede"])}</p>
<div class="chips">{fw}</div>
<div class="p-meta"><div><span>Organization</span>{e(COMPANY["name"])} (fictional)</div><div><span>Period</span>{e(p["period"])}</div><div><span>Prepared by</span>{e(PERSON["name"])}</div></div>
</div></header>

<section class="p-section" id="summary" aria-labelledby="h-summary"><div class="wrap">
<h2 id="h-summary">Engagement summary</h2>
<div class="glance">{glance}</div>
<div class="kpis">{kpis}</div>
</div></section>

<section class="p-section" aria-labelledby="h-concl"><div class="wrap">
<h2 id="h-concl">Conclusion and key findings</h2>
<div class="conclusion">
<div class="rating"><span class="label">Overall rating</span><div class="scale r{level}">{scale}</div><strong>{e(RATINGS[level])}</strong><p>{e(rtext)}</p></div>
<div class="keyfindings">{finds}</div>
</div>
</div></section>

<section class="p-section" aria-labelledby="h-analysis"><div class="wrap">
<h2 id="h-analysis">Analysis</h2>
{p["charts"]}
</div></section>

<section class="p-section" id="register" aria-labelledby="h-reg"><div class="wrap">
<h2 id="h-reg">Register</h2>
<p class="sub">The full working register. Search, filter or sort, and open any row for the complete record. IDs in the related-records field link to the other workstreams.</p>
{p["reg"]}
</div></section>

<section class="p-section" id="method" aria-labelledby="h-method"><div class="wrap">
<h2 id="h-method">Method and criteria</h2>
<div class="method"><div><h3>How the assessment was performed</h3><ol>{steps}</ol></div><div><h3>{e(ctitle)}</h3><div class="chartscroll">{ctable}</div></div></div>
</div></section>

<section class="p-section" aria-labelledby="h-rel"><div class="wrap">
<h2 id="h-rel">Connected workstreams</h2>
<p class="sub">Findings here feed, or draw on, these other parts of the same program.</p>
<div class="related">{related}</div>
<div style="margin-top:36px" class="pager">{pager}</div>
</div></section>
</main>
{footer()}"""
    desc = f"{title}: {p['lede'][:150]}"
    write(f"projects/{slug}/index.html", page(f"{title} | {PERSON['name']}", desc, body, depth=2, canonical_path=f"projects/{slug}/"))
    rel_path, header, rows = p["csv"]
    write_csv(rel_path, header, rows)

RECORDS = {"risk-assessment": (RISKS, "links"), "gap-assessment": (OUTCOMES, "links"), "it-audit": (CONTROLS, "links"),
           "vulnerability-management": (FINDINGS, "links"), "third-party-risk": (VENDORS, "links"), "cloud-iam": (CHECKS, "links"),
           "business-continuity": (SERVICES, "links"), "ai-governance": (USECASES, "links")}

def build_projects():
    specs = [f() for f in SPECS]
    for s in specs:
        recs, fld = RECORDS[s["slug"]]
        out = linked_slugs(recs, fld, s["slug"])
        if s["slug"] != "risk-assessment" and "risk-assessment" in out:
            out.remove("risk-assessment"); out.insert(0, "risk-assessment")
        s["related"] = out
    for i, s in enumerate(specs):
        render_project(s, i, specs)
    return specs
