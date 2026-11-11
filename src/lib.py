"""Rendering helpers shared by every page."""
import csv, html, io, os
from datetime import date
from data_company import PERSON, COMPANY

OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def e(s):
    return html.escape("" if s is None else str(s), quote=True)

def fmt_date(iso):
    if not iso or iso in ("—", "-"): return "—"
    d = date.fromisoformat(iso)
    return d.strftime("%b %-d, %Y")

SEV = {"Critical":"crit","High":"high","Moderate":"mod","Medium":"mod","Low":"low"}
def pill(text, cls=None):
    cls = cls if cls is not None else SEV.get(text, "")
    return f'<span class="pill {cls}">{e(text)}</span>'

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600&family=Public+Sans:ital,wght@0,400;0,550;0,600;0,650;0,700;0,750;0,800;1,400&display=swap">')

FAVICON = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='7' fill='%2314212B'/%3E"
           "%3Ctext x='16' y='21' font-family='monospace' font-size='13' font-weight='700' fill='%23F4F6F7' text-anchor='middle'%3EEB%3C/text%3E%3C/svg%3E")

def page(title, description, body, depth=0, canonical_path=""):
    root = "../" * depth
    site = "https://ebalogungrc.github.io/GRC---PORTFOLIO/"
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{e(title)}</title>
<meta name="claude:viewport-fit-sides" content="cover">
<meta name="description" content="{e(description)}">
<meta name="author" content="{e(PERSON['name'])}">
<meta property="og:type" content="website">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(description)}">
<meta property="og:url" content="{site}{canonical_path}">
<meta name="theme-color" content="#14212B">
<link rel="canonical" href="{site}{canonical_path}">
<link rel="icon" href="{FAVICON}">
{FONTS}
<link rel="stylesheet" href="{root}assets/site.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
{body}
<script src="{root}assets/site.js" defer></script>
</body>
</html>
"""

def topbar(depth=0, nav=None):
    root = "../" * depth
    nav = nav or []
    links = "".join(f'<a href="{h}">{e(t)}</a>' for t, h in nav)
    li = (f'<a class="cta" href="{e(PERSON["linkedin"])}" target="_blank" rel="noopener">LinkedIn</a>' if PERSON["linkedin"] else "")
    return f"""<header class="topbar"><div class="wrap">
<a class="brand" href="{root or './'}"><span class="mark">EB</span><span><b>{e(PERSON['name'])}</b><small>{e(PERSON['title'])} · {e(PERSON['focus'])}</small></span></a>
<nav class="topnav" aria-label="Primary">{links}{li}<a class="cta" href="{e(PERSON['github'])}" target="_blank" rel="noopener">GitHub</a></nav>
</div></header>"""

DISCLOSURE = (f"{COMPANY['name']} is a fictional company. Every record on this site was written for this portfolio to show "
              "assessment methods and deliverables. It does not describe a real organization, client or audit.")

def footer():
    return f"""<footer class="site"><div class="wrap"><p>{e(DISCLOSURE)}</p><p>© 2026 {e(PERSON['name'])}</p></div></footer>"""

def write(rel, content):
    path = os.path.join(OUT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def write_csv(rel, header, rows):
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\r\n")
    w.writerow(header)
    for r in rows: w.writerow(r)
    write(rel, "﻿" + buf.getvalue())

# ---------- Register ----------
def register(rows, cols, detail, filters, csv_href, search_ph, id_key="id", noun="records"):
    """cols: list of dict(key,label,html(row),sort(row),numeric,cls)
       detail: list of (label, fn(row), wide)
       filters: list of (key, label, options, fn(row)->value or list)"""
    sel = []
    for key, label, options, _ in filters:
        opts = "".join(f'<option value="{e(o)}">{e(o)}</option>' for o in options)
        sel.append(f'<select id="f-{key}" data-filter="{key}" aria-label="{e(label)}"><option value="">{e(label)}: all</option>{opts}</select>')
    head = "".join(
        f'<th scope="col" data-key="{c["key"]}"{" data-numeric" if c.get("numeric") else ""}>{e(c["label"])}</th>' for c in cols
    ) + '<th scope="col"><span class="sr-only">Details</span></th>'
    body = []
    ncol = len(cols) + 1
    for r in rows:
        attrs = []
        for key, _, _, fn in filters:
            v = fn(r)
            v = "|".join(v) if isinstance(v, (list, tuple)) else v
            attrs.append(f'data-{key}="{e(v)}"')
        for c in cols:
            sv = c.get("sort", lambda r, k=c["key"]: r.get(k, ""))(r)
            attrs.append(f'data-s-{c["key"]}="{e(sv)}"')
        tds = "".join(f'<td class="{c.get("cls","")}">{c["html"](r)}</td>' for c in cols)
        body.append(f'<tr class="row" {" ".join(attrs)}>{tds}<td><button type="button" class="xbtn" aria-expanded="false">Details</button></td></tr>')
        cells = "".join(
            f'<div class="{"wide" if wide else ""}"><span class="label">{e(lbl)}</span><p>{fn(r)}</p></div>'
            for lbl, fn, wide in detail
        )
        body.append(f'<tr class="detail"><td colspan="{ncol}"><div class="dgrid">{cells}</div></td></tr>')
    return f"""<div data-register>
<div class="toolbar">
<input type="search" id="reg-search" data-search placeholder="{e(search_ph)}" aria-label="Search the register">
{''.join(sel)}
<button type="button" class="btn ghost small" data-clear hidden>Clear filters</button>
<span class="count" data-count aria-live="polite">{len(rows)} {noun}</span>
</div>
<div class="tablewrap"><table class="reg"><thead><tr>{head}</tr></thead><tbody>
{''.join(body)}
</tbody></table></div>
<div class="reg-foot"><span>Select a row to open the full record. Column headers sort the table.</span><a href="{csv_href}" download>Download register (CSV)</a></div>
</div>"""

def hbars(items, total=None, unit=""):
    """items: list of (label, [(count, segclass, title)], value_text, filter_spec or None)"""
    mx = total or max(sum(s[0] for s in segs) for _, segs, _, _ in items) or 1
    out = []
    for label, segs, vtext, filt in items:
        inner = "".join(
            f'<i class="{cls}" style="width:{c / mx * 100:.2f}%" title="{e(t)}: {round(c) if isinstance(c,float) else c}"></i>' for c, cls, t in segs if c
        )
        lab = (f'<button type="button" class="l linklike" data-set-filter="{e(filt)}">{e(label)}</button>' if filt
               else f'<span class="l">{e(label)}</span>')
        out.append(f'<div class="hbar">{lab}<span class="trk">{inner}</span><span class="v">{e(vtext)}</span></div>')
    return '<div class="hbars">' + "".join(out) + "</div>"

def legend(items):
    return '<div class="legend">' + "".join(f'<span><i class="{c}"></i>{e(t)}</span>' for t, c in items) + "</div>"
