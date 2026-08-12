#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kronos Technical Library — static page generator.
Builds a large, on-brand, SEO + AI-optimized technical knowledge base for
kronosfusionenergy.com/technical/. Every number comes from FROZEN (the frozen
design canon) so nothing can drift. No economics, no cap table, honest gates,
only the five live Zenodo DOIs. Regenerate any time: python3 build_library.py
"""
import os, re, html, json

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = "https://kronosfusionenergy.com"
BASE = "/technical"            # URL path segment (configurable at mount time)
BUILD_DATE = "2026-08-11"

# ---------------------------------------------------------------- FROZEN CANON
# The single source of truth. Author pages reference F[...]; never hardcode a number.
F = {
    # Breeder — HYPERION (D–T spherical tokamak), config 22021
    "b_Q": "3.424", "b_Pfus": "88.7 MW", "b_Pn": "70.7 MW", "b_fn": "79.7%",
    "b_Ip": "9.86 MA", "b_fbs": "15.2%", "b_Paux": "25.9 MW",
    "b_B0": "8 T", "b_Bpeak": "16.84 T", "b_R0": "1.2 m", "b_A": "2.5",
    "b_a": "0.48 m", "b_kappa": "2.0", "b_delta": "-0.30", "b_q95": "3.0",
    "b_Ti": "15 keV", "b_Zeff": "1.16", "b_bN": "1.532", "b_tauE": "0.374 s",
    "b_H98": "1.0", "b_wall": "1.97 MW/m2", "b_T": "4.0 kg/yr", "b_TBR": "1.8",
    "b_startup": "6.47 kg", "b_He3": "1.97 kg/yr", "b_checks": "23",
    # Burner — D–3He tandem mirror (Mode M, M-45)
    "u_QE": "1.31", "u_fn": "5.44%", "u_Ti": "90 keV", "u_Te": "89.78 keV",
    "u_ne": "2.6e20 m^-3", "u_x": "0.30", "u_Bm": "17 T", "u_Bplug": "26.49 T",
    "u_beta": "0.55", "u_ac": "0.86 m", "u_dec": "0.70", "u_aux": "28.2%",
    "u_np": "16", "u_checks": "45",
    "u_ref_len": "55 m", "u_ref_net": "+104 MWe", "u_ref_gw": "0.537 GW",
    "u_aeg_len": "440 m", "u_aeg_net": "+850 MWe", "u_aeg_gw": "4.298 GW",
    "u_mv_len": "1400 m", "u_mv_net": "+2832 MWe", "u_mv_gw": "13.678 GW",
    # Provenance
    "doi_b": "10.5281/zenodo.21746157", "doi_b2": "10.5281/zenodo.21795620",
    "doi_u": "10.5281/zenodo.21746479", "doi_rebco": "10.5281/zenodo.21842514",
    "doi_dec": "10.5281/zenodo.21842864", "doi_ai": "10.5281/zenodo.21842371",
    "patent_granted": "US 12,009,112", "patent_pending": "64/128,097",
}
LIVE_DOIS = {"21746157", "21795620", "21746479", "21842514", "21842864", "21842371"}
DEAD_DOIS = {"21248916"}

# ---------------------------------------------------------------- DESIGN (1:1 with learn/)
CSS = open(os.path.join(HERE, "_style.css"), encoding="utf-8").read() if os.path.exists(os.path.join(HERE,"_style.css")) else ""

NAV = ('<nav class="top">'
       f'<a href="{SITE}/technical/">Library</a>'
       f'<a href="{SITE}/learn/">Learn</a>'
       f'<a href="{SITE}/Physics_Validation_Simulation">Live&nbsp;Sim</a>'
       f'<a href="{SITE}/3D_Model">3D&nbsp;Model</a>'
       f'<a href="{SITE}/technology">Technology</a></nav>')

FOOTER = ('<footer><div class="wrap">'
          'Kronos Fusion Energy — compact, low-neutron fusion generators, engineered in the open. '
          'A breeder–burner architecture: HYPERION (D–T spherical tokamak) breeds the fuel; the D–&sup3;He tandem-mirror '
          'generator burns it as MetroVolt and AEGIS. Every figure is a computed design target from the 2026 '
          'pre-publication record, traceable to the open deposits '
          f'(<a href="https://doi.org/{F["doi_b"]}">breeder</a>, '
          f'<a href="https://doi.org/{F["doi_u"]}">burner</a>, CC&nbsp;BY&nbsp;4.0). '
          'The integrated machines are not yet built. '
          f'Partnerships: <a href="{SITE}/contact">kronosfusionenergy.com/contact</a>.'
          '</div></footer>')

# ---------------------------------------------------------------- PAGE MODEL
PAGES = {}   # slug -> spec
CATS = {}    # cat key -> {title, kicker, blurb, order}

def cat(key, title, blurb, order):
    CATS[key] = {"title": title, "blurb": blurb, "order": order}

def page(slug, title, catkey, desc, lede, body, facts=None, related=None,
         jtype="Article", kicker=None):
    if slug in PAGES:
        raise SystemExit("DUPLICATE SLUG: " + slug)
    PAGES[slug] = dict(slug=slug, title=title, cat=catkey, desc=desc, lede=lede,
                       body=body, facts=facts or [], related=related or [],
                       jtype=jtype, kicker=kicker or CATS.get(catkey, {}).get("title", "Technical"))

def esc(s): return html.escape(str(s), quote=False)

# ---- body element renderers. body = list of tuples:
#   ('p', text) ('h2', text) ('ul', [..]) ('ol', [..]) ('facts', [(k,v)..])
#   ('gap', (label, text))  ('qa', [(q,a)..])  ('html', raw)
def render_body(elems):
    out = []
    for e in elems:
        t = e[0]
        if t == 'p':      out.append("<p>" + e[1] + "</p>")
        elif t == 'h2':   out.append("<h2>" + esc(e[1]) + "</h2>")
        elif t == 'ul':   out.append("<ul>" + "".join("<li>"+x+"</li>" for x in e[1]) + "</ul>")
        elif t == 'ol':   out.append("<ol>" + "".join("<li>"+x+"</li>" for x in e[1]) + "</ol>")
        elif t == 'facts':
            rows = "".join(f"<tr><th>{esc(k)}</th><td>{v}</td></tr>" for k,v in e[1])
            out.append(f'<table class="facts"><tbody>{rows}</tbody></table>')
        elif t == 'gap':
            out.append(f'<div class="gap"><b>{esc(e[1][0])}</b>{e[1][1]}</div>')
        elif t == 'qa':
            out.append("".join(f'<div class="qa"><div class="q">{esc(q)}</div><div class="a">{a}</div></div>' for q,a in e[1]))
        elif t == 'html': out.append(e[1])
    return "\n".join(out)

def jsonld(spec):
    url = f"{SITE}{BASE}/{spec['slug']}.html"
    if spec["jtype"] == "DefinedTerm":
        d = {"@context":"https://schema.org","@type":"DefinedTerm","name":spec["title"],
             "description":spec["desc"],"url":url,
             "inDefinedTermSet":{"@type":"DefinedTermSet","name":"Kronos Fusion Energy Technical Library","url":f"{SITE}{BASE}/"}}
    elif spec["jtype"] == "FAQPage":
        qa = [x for el in spec["body"] if el[0]=="qa" for x in el[1]]
        d = {"@context":"https://schema.org","@type":"FAQPage","url":url,
             "mainEntity":[{"@type":"Question","name":q,
                            "acceptedAnswer":{"@type":"Answer","text":re.sub('<[^>]+>','',a)}} for q,a in qa]}
    else:
        d = {"@context":"https://schema.org","@type":"TechArticle","headline":spec["title"],
             "description":spec["desc"],"url":url,
             "datePublished":BUILD_DATE,"dateModified":BUILD_DATE,
             "publisher":{"@type":"Organization","name":"Kronos Fusion Energy","url":SITE},
             "isPartOf":{"@type":"CreativeWork","name":"Kronos Fusion Energy Technical Library","url":f"{SITE}{BASE}/"}}
    return json.dumps(d, ensure_ascii=False)

def breadcrumb_ld(spec):
    return json.dumps({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
        {"@type":"ListItem","position":1,"name":"Technical Library","item":f"{SITE}{BASE}/"},
        {"@type":"ListItem","position":2,"name":CATS.get(spec['cat'],{}).get('title','Technical'),"item":f"{SITE}{BASE}/#"+spec['cat']},
        {"@type":"ListItem","position":3,"name":spec["title"],"item":f"{SITE}{BASE}/{spec['slug']}.html"}]}, ensure_ascii=False)

def render_page(spec):
    url = f"{SITE}{BASE}/{spec['slug']}.html"
    facts = ""
    if spec["facts"]:
        rows = "".join(f'<div class="row"><dt>{esc(k)}</dt><dd>{v}</dd></div>' for k,v in spec["facts"])
        facts = f'<dl class="kf">{rows}</dl>'
    related = ""
    if spec["related"]:
        links = []
        for r in spec["related"]:
            tt = PAGES[r]["title"] if r in PAGES else r.replace("-"," ").title()
            links.append(f'<a href="./{r}.html">{esc(tt)} &rarr;</a>')
        related = f'<div class="related"><h3>Related</h3>{"".join(links)}</div>'
    catt = CATS.get(spec['cat'], {}).get('title', 'Technical')
    return f"""<!doctype html>
<html lang="en"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(spec['title'])} · Kronos Fusion Energy</title>
<meta name="description" content="{esc(spec['desc'])}">
<link rel="canonical" href="{url}">
<meta property="og:title" content="{esc(spec['title'])}">
<meta property="og:description" content="{esc(spec['desc'])}">
<meta property="og:type" content="article">
<meta property="og:url" content="{url}">
<meta property="og:site_name" content="Kronos Fusion Energy">
<meta name="twitter:card" content="summary">
<meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1">
<meta name="author" content="Kronos Fusion Energy">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;0,6..72,600;1,6..72,400;1,6..72,500&family=Space+Grotesk:wght@400;500;600&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<script type="application/ld+json">{jsonld(spec)}</script>
<script type="application/ld+json">{breadcrumb_ld(spec)}</script>
{CSS}
</head><body>
<header class="top"><div class="wrap">
<a class="brand" href="{SITE}">KRONOS<span>·</span>FUSION</a>
{NAV}
</div></header>
<main class="wrap">
<div class="crumb"><a href="{SITE}{BASE}/">Technical Library</a> &rsaquo; {esc(catt)}</div>
<div class="kicker">{esc(spec['kicker'])}</div>
<h1>{esc(spec['title'])}</h1>
<p class="lede">{spec['lede']}</p>
{facts}
{render_body(spec['body'])}
{related}
</main>
{FOOTER}
</body></html>"""

# ---------------------------------------------------------------- CONTENT
# Content modules populate CATS + PAGES. Imported below.
def build_content():
    import glob, importlib
    mods = sorted(os.path.basename(f)[:-3] for f in glob.glob(os.path.join(HERE,"content_*.py")))
    for name in mods:
        importlib.import_module(name).register(cat, page, F)

# ---------------------------------------------------------------- INDEX / SITEMAP / LLMS
def build_index():
    cats_sorted = sorted(CATS.items(), key=lambda kv: kv[1]["order"])
    sections = []
    for ck, cinfo in cats_sorted:
        items = [p for p in PAGES.values() if p["cat"] == ck]
        items.sort(key=lambda p: p["title"])
        cards = "".join(
            f'<div class="card"><div class="k">{esc(cinfo["title"])}</div>'
            f'<a href="./{p["slug"]}.html">{esc(p["title"])}</a></div>' for p in items)
        sections.append(
            f'<h2 id="{ck}">{esc(cinfo["title"])} <span class="seccount">{len(items)} pages</span></h2>'
            f'<p>{cinfo["blurb"]}</p><div class="hubgrid">{cards}</div>')
    body = "\n".join(sections)
    total = len(PAGES)
    ld = json.dumps({"@context":"https://schema.org","@type":"CollectionPage",
        "name":"Kronos Fusion Energy Technical Library","url":f"{SITE}{BASE}/",
        "description":f"A {total}-page open technical library covering the physics, validation, engineering, materials, methodology and open-science record behind Kronos Fusion Energy's breeder-burner architecture."}, ensure_ascii=False)
    htmlout = f"""<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Technical Library · Kronos Fusion Energy</title>
<meta name="description" content="The open technical library behind Kronos Fusion Energy — {total} pages on fusion physics, validation, engineering, materials, methodology and open science. Every number traceable to open deposits.">
<link rel="canonical" href="{SITE}{BASE}/">
<meta property="og:title" content="Kronos Fusion Energy — Technical Library">
<meta property="og:description" content="{total} open pages: physics, validation, engineering, materials, methodology, open science.">
<meta property="og:type" content="website"><meta property="og:url" content="{SITE}{BASE}/">
<meta name="robots" content="index,follow,max-snippet:-1">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;0,6..72,600;1,6..72,400;1,6..72,500&family=Space+Grotesk:wght@400;500;600&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<script type="application/ld+json">{ld}</script>
{CSS}
</head><body>
<header class="top"><div class="wrap">
<a class="brand" href="{SITE}">KRONOS<span>·</span>FUSION</a>
{NAV}
</div></header>
<main class="wrap">
<div class="crumb">Kronos Fusion Energy &rsaquo; Technical Library</div>
<div class="kicker">Open Technical Library</div>
<h1>The engineering and the physics, in the open.</h1>
<p class="lede">A {total}-page technical library covering the physics, validation, engineering, materials, methodology and open-science record behind Kronos Fusion Energy's breeder–burner architecture. Every figure is a computed design target traceable to our open Zenodo deposits.</p>
{body}
</main>
{FOOTER}
</body></html>"""
    open(os.path.join(HERE,"index.html"),"w",encoding="utf-8").write(htmlout)

def build_sitemap():
    urls = [f"{SITE}{BASE}/"] + [f"{SITE}{BASE}/{s}.html" for s in sorted(PAGES)]
    body = "".join(f"<url><loc>{u}</loc><lastmod>{BUILD_DATE}</lastmod><changefreq>monthly</changefreq></url>" for u in urls)
    open(os.path.join(HERE,"sitemap.xml"),"w",encoding="utf-8").write(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+body+'</urlset>')

def build_llms():
    cats_sorted = sorted(CATS.items(), key=lambda kv: kv[1]["order"])
    lines = ["# Kronos Fusion Energy — Technical Library",
             "",
             f"> Open technical knowledge base ({len(PAGES)} pages) on the physics, validation, engineering, materials, methodology and open-science record behind Kronos Fusion Energy's breeder-burner fusion architecture. Breeder = HYPERION, a D-T spherical tokamak (Q {F['b_Q']}, {F['b_Pfus']}). Burner = a D-3He tandem-mirror generator (MetroVolt, AEGIS). Every figure is a computed design target traceable to open Zenodo deposits (CC BY 4.0). The integrated machines are not yet built.",
             ""]
    for ck, cinfo in cats_sorted:
        items = [p for p in PAGES.values() if p["cat"] == ck]
        items.sort(key=lambda p: p["title"])
        lines.append(f"## {cinfo['title']}")
        for p in items:
            lines.append(f"- [{p['title']}]({SITE}{BASE}/{p['slug']}.html): {p['desc']}")
        lines.append("")
    open(os.path.join(HERE,"llms.txt"),"w",encoding="utf-8").write("\n".join(lines))

# ---------------------------------------------------------------- VERIFY
def verify():
    problems = []
    for s, spec in PAGES.items():
        blob = json.dumps(spec, ensure_ascii=False)
        for d in DEAD_DOIS:
            if d in blob: problems.append(f"DEAD DOI in {s}")
        # economics guard
        if re.search(r"\$\s?\d", blob) or re.search(r"\b(LCOE|EBITDA|valuation|cap table|\bIRR\b)\b", blob, re.I):
            problems.append(f"ECONOMICS token in {s}")
        for r in spec["related"]:
            if r not in PAGES: problems.append(f"broken related link {s} -> {r}")
    return problems

def main():
    build_content()
    n = 0
    for s, spec in PAGES.items():
        open(os.path.join(HERE, s+".html"),"w",encoding="utf-8").write(render_page(spec))
        n += 1
    build_index(); build_sitemap(); build_llms()
    probs = verify()
    print(f"Generated {n} pages across {len(CATS)} categories.")
    print("Verification:", "CLEAN" if not probs else f"{len(probs)} PROBLEMS")
    for p in probs[:40]: print("  -", p)

if __name__ == "__main__":
    main()
