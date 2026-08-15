# -*- coding: utf-8 -*-
"""Motion Library — a gallery of ALL Kronos clips (hosted on R2), grouped by topic.
Self-contained page; intersection-observer lazy autoplay keeps 500+ videos performant.
Regenerate: python3 build_motion.py"""
import os, re, json, collections, html

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = "https://kronosfusionenergy.com"
CLIPS_BASE = "https://pub-6f4141e515994eaf98b678a16ccbf603.r2.dev/"

NAV = ('<nav class="sitebar"><a class="sb-home" href="%s/">KRONOS &middot; FUSION ENERGY</a>'
  '<span class="sb-links">'
  '<a href="%s/">Home</a><a href="%s/learn/">Learn</a><a href="%s/technical/">Technical</a>'
  '<a href="%s/technical/motion.html">Motion</a>'
  '<a href="%s/whitepapers">Whitepapers</a><a href="%s/publications">Publications</a>'
  '<a href="%s/3D_Model">3D&nbsp;Model</a><a href="%s/Physics_Validation_Simulation">Live&nbsp;Sim</a>'
  '</span></nav>') % ((SITE,)*9)
FOOTER = ('<footer class="mfoot">&copy; 2026 Kronos Fusion Energy, Inc. &middot; Los Angeles, California &middot; '
  '<a href="%s">kronosfusionenergy.com</a> &middot; '
  '<a href="https://zenodo.org/communities/kronos_fusion_energy">Zenodo community</a> &middot; '
  'Correspondence: p.ford@kronosfusionenergy.com</footer>') % SITE

GT = {"A":"Why Fusion & the Company","AA":"Design Parameters & Scans","AB":"Analogies & Intuition",
 "AC":"Operations & Disruptions","AD":"Confinement & Control","AE":"Start-Up & Milestones",
 "B":"The Breeder — Hyperion","BC":"Breeder Core","BDC":"Breeder — Comparisons","BHT":"Breeder Heating",
 "BMH":"Breeder MHD & Stability","BMR":"Breeder Materials","BNU":"Breeder Neutronics",
 "BTR":"Breeder Tritium & Fuel","BUC":"Breeder Under the Hood","C":"Strategic Isotopes","CTL":"Real-Time Control",
 "D":"The Burner — Aegis & MetroVolt","DT":"The Digital Twin","E":"The Digital Twin","F":"AI & Quantum",
 "G":"The Fleet & Open Science","H":"Brand & Website","HPC":"HPC & Compute","I":"Fusion Science 101",
 "J":"Breeder Subsystems","K":"Burner Subsystems","L":"Isotope Applications","M":"AI · Twin · Quantum (Deep)",
 "MAG":"Magnets","ML":"Machine Learning","N":"Comparisons & Competitive","O":"Strategy & Business",
 "P":"Company, Team & Vision","PRD":"Products","Q":"Safety & Environment","QA":"Quantum Algorithms",
 "QC":"Quantum Computing","R":"Applications & Use-Cases","S":"Website UI & Motion","SUR":"Surrogate Models",
 "T":"Social & Short-Form","U":"Extended Series U","UQ":"Uncertainty Quantification","V":"Extended Series V",
 "W":"Extended Series W","X":"Extended Series X","Y":"Extended Series Y","Z":"Extended Series Z"}

STYLE = """
*{box-sizing:border-box}
body{margin:0;background:#1c2430;color:#e7ebf2;
  font-family:'Space Grotesk',-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif}
a{color:#d4ad5c}
.sitebar{background:#232c39;display:flex;flex-wrap:wrap;gap:10px 20px;align-items:center;justify-content:space-between;
  padding:11px 22px;font-size:13.5px;position:sticky;top:0;z-index:10}
.sitebar a{color:#e8ebef;text-decoration:none}
.sitebar .sb-home{font-weight:700;letter-spacing:.1em;color:#fff;font-size:12.5px}
.sitebar .sb-links{display:flex;flex-wrap:wrap;gap:16px}
.sitebar a:hover{color:#d4ad5c}
.mwrap{max-width:1220px;margin:0 auto;padding:0 22px}
.mhero{padding:40px 0 8px;border-bottom:1px solid #2e3b4c;margin-bottom:8px}
.mkick{font-size:12px;letter-spacing:.18em;text-transform:uppercase;color:#d4ad5c;font-weight:600}
.mhero h1{font-family:'Newsreader',Georgia,serif;font-weight:500;font-size:34px;line-height:1.14;margin:10px 0 12px;color:#fff}
.mhero p{color:#a7b3c4;max-width:70ch;margin:0;font-size:15.5px;line-height:1.6}
.mjump{font-size:12.5px;line-height:2.1;color:#8fa0b8;margin:18px 0 6px}
.mjump a{color:#b9c6d8;text-decoration:none;white-space:nowrap;margin-right:4px}
.mjump a:hover{color:#d4ad5c}.mjump .ct{color:#6c7a8c;font-size:11px}
.mgroup{margin:32px 0 6px;scroll-margin-top:64px}
.mgroup h2{font-size:14px;letter-spacing:.07em;text-transform:uppercase;color:#fff;
  border-bottom:2px solid #d4ad5c;padding-bottom:7px;margin:0 0 14px}
.mgroup h2 .ct{color:#7d8aa0;font-size:12px;font-weight:400}
.mgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(232px,1fr));gap:16px}
.mclip{margin:0}
.mclip video{width:100%;aspect-ratio:16/9;object-fit:cover;background:#0e1420;border:1px solid #33425a;
  border-radius:9px;box-shadow:0 3px 12px rgba(0,0,0,.28);display:block}
.mclip figcaption{font-size:12.5px;color:#9aa8bd;margin-top:7px}
.mfoot{margin:44px 0 0;padding:22px;background:#232c39;font-size:13px;color:#8fa0b8;text-align:center}
.mfoot a{color:#d4ad5c;text-decoration:none}
@media(max-width:560px){.mhero h1{font-size:26px}.mgrid{grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:11px}}
"""

SCRIPT = ("<script>document.addEventListener('DOMContentLoaded',function(){"
  "var io=new IntersectionObserver(function(es){es.forEach(function(e){var v=e.target;"
  "if(e.isIntersecting){"
  "if(!v.src){v.src=v.dataset.src;v.addEventListener('canplay',function(){v.play().catch(function(){});},{once:true});}"
  "v.play().catch(function(){});"
  "}else{v.pause();}});},"
  "{rootMargin:'300px 0px',threshold:0.1});"
  "document.querySelectorAll('.mclip video').forEach(function(v){io.observe(v);});});</script>")

def gcode(s):
    m = re.match(r"^([a-z]+)[0-9]", s)
    return m.group(1).upper() if m else "HERO"

def caption(s):
    s = re.sub(r"\.mp4$","",s); s = re.sub(r"^[a-z]+[0-9]*-","",s); s = s.replace("-"," ").strip()
    return (s[:1].upper()+s[1:]) if s else "Kronos motion"

def build():
    smp = os.path.join(HERE, "..", "_clip_slug_map.json")
    if not os.path.exists(smp): smp = os.path.join(HERE, "_clip_slug_map.json")
    slugs = sorted(set(json.load(open(smp)).values()))
    groups = collections.defaultdict(list)
    for s in slugs: groups[gcode(s)].append(s)
    order = [g for g in ["HERO"] + list(GT.keys()) if g in groups]
    order += sorted(g for g in groups if g not in order)
    total = len(slugs)

    def gtitle(g): return "Original Hero Set" if g == "HERO" else GT.get(g, "Series " + g)
    jump = " ".join(f'<a href="#g-{g}">{gtitle(g)} <span class="ct">{len(groups[g])}</span></a>' for g in order)
    secs = []
    for g in order:
        cards = "".join(
          '<figure class="mclip"><video autoplay muted loop playsinline preload="none" '
          f'data-src="{CLIPS_BASE}{c}"></video><figcaption>{html.escape(caption(c))}</figcaption></figure>'
          for c in groups[g])
        secs.append(f'<section id="g-{g}" class="mgroup"><h2>{gtitle(g)} '
                    f'<span class="ct">&middot; {len(groups[g])} clips</span></h2><div class="mgrid">{cards}</div></section>')

    page = (f'<!doctype html><html lang="en"><head><meta charset="utf-8">'
      f'<meta name="viewport" content="width=device-width,initial-scale=1">'
      f'<title>Motion Library · Kronos Fusion Energy</title>'
      f'<meta name="description" content="The Kronos Fusion Energy motion library — {total} in-brand, '
      f'freeze-compliant, silent animation clips of the physics, machines, isotopes, control and company, produced in-house.">'
      f'<meta name="robots" content="index,follow,max-image-preview:large">'
      f'<link rel="canonical" href="{SITE}/technical/motion.html">'
      f'<meta property="og:title" content="Kronos Fusion Energy — Motion Library"><meta property="og:type" content="website">'
      f'<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
      f'<link href="https://fonts.googleapis.com/css2?family=Newsreader:opsz,wght@6..72,400;6..72,500&family=Space+Grotesk:wght@400;500;600&display=swap" rel="stylesheet">'
      f'<style>{STYLE}</style></head><body>'
      f'{NAV}'
      f'<div class="mwrap"><header class="mhero"><div class="mkick">Motion Library</div>'
      f'<h1>{total} clips of the machine, the physics, and the mission.</h1>'
      f'<p>Every animation in the Kronos motion library — {total} in-brand, freeze-compliant, silent loops '
      'produced in-house, spanning the breeder and burner, the strategic isotopes, the digital twin, AI and '
      'quantum control, safety, applications, and the company. Each is a computed, on-brand visual of the same '
      'design record documented across this technical library.</p></header>'
      f'<div class="mjump">{jump}</div>{"".join(secs)}</div>'
      f'{FOOTER}{SCRIPT}</body></html>')
    open(os.path.join(HERE, "motion.html"), "w", encoding="utf-8").write(page)
    print(f"Motion Library: {total} clips in {len(groups)} groups -> motion.html")

if __name__ == "__main__":
    build()
