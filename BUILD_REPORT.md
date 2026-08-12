# Kronos Technical Library — build report

**Built:** 2026-08-11 · **Depth pass:** 2026-08-12 · **Pages:** 1005 (+ index) · **Categories:** 22 · **Verification: CLEAN**

A self-contained, on-brand, SEO- and AI-optimized technical knowledge base for
`kronosfusionenergy.com/technical/`. Every page is grounded in the frozen design canon
and standard fusion science — nothing invented, nothing padded.

## Depth pass (2026-08-12) — added before final push
- **FAQ blocks on every substantive article page.** 268 pages now carry a "Common questions"
  section (2 page-specific Q&A each), up from 54 — every non-glossary, non-FAQ page across all
  22 categories. This is the single highest-value AI/SEO addition: each renders a **FAQPage**
  JSON-LD node (311 total on the site) for answer-engine extraction and rich results.
- **Glossary depth.** ~130 cornerstone glossary terms deepened with a third body paragraph
  (batches A–F); every glossary term already shipped with two full paragraphs by construction.
- **Cornerstones deepened** with extra sections + assumptions-vs-demonstrated callouts.
- All additions hold the frozen canon and honest gates; `verify()` re-checked CLEAN after each batch.

## What's in the folder
- `index.html` — master directory (all categories, all pages, page counts)
- `<slug>.html` — 1005 content pages
- `sitemap.xml` — 1,006 URLs for search engines
- `llms.txt` — AI-crawler index (every page + one-line description), like your `learn/llms_learn.txt`
- `_style.css` — shared stylesheet (1:1 with your `learn/` brand)
- `build_library.py` — the generator (regenerate any time: `python3 build_library.py`)
- `content_*.py` — content modules (auto-discovered by the generator)

## Pages by category
| Category | Pages |
|---|---|
| Glossary of Fusion & Plasma Terms | 699 |
| Questions & Honest Answers | 43 |
| Components & Hardware | 37 |
| Physics & Fusion Science | 31 |
| Engineering & Subsystems | 22 |
| Materials & Magnets | 18 |
| Process & Methodology | 17 |
| Safety & Environment | 13 |
| Reference Devices | 12 |
| Products & Applications | 12 |
| Codes & Standards | 12 |
| Competitive Landscape | 11 |
| Applications & Markets | 10 |
| Innovations & Distinctives | 10 |
| Operations & Commissioning | 10 |
| The Technology Stack | 10 |
| Diagnostics & Measurement | 8 |
| Open Science & Publications | 7 |
| Comparisons & Context | 7 |
| History & Context | 7 |
| Validation & Reproducibility | 6 |
| Team & Heritage | 3 |

## Guardrails — verified on the generated HTML
- **Frozen canon only.** Every number comes from one `F{}` block (Q 3.424 · 88.7 MW · 9.86 MA · burner Q_E 1.31 / f_n 5.44% · plug ratio 16). Nothing drifts, nothing invented.
- **DOIs:** only the 5 live ones (breeder 21746157 / v2 21795620, burner 21746479, REBCO 21842514, DEC 21842864, AI 21842371). **Dead DOI 21248916: 0 occurrences.**
- **Economics:** 0 — no $, LCOE, EBITDA, valuation or cap-table tokens anywhere (public-safe).
- **Honest gates carried throughout:** low-neutron *not* aneutronic · burner net power requirement-class · H₉₈ / divertor caveats · "not yet built · computed design targets."
- **Positive-for-Kronos tone:** honesty framed as rigor and strength; nothing self-critical.
- **SEO + AI on every page:** canonical, OG, Twitter card, `robots: index,follow,max-snippet:-1`, JSON-LD (TechArticle / DefinedTerm / FAQPage) + BreadcrumbList, dense internal linking, sitemap, llms.txt.

## How to extend toward 1000 pages
The generator auto-discovers any `content_*.py` module that defines `register(cat, page, F)`.
To add more pages, drop in another module (more glossary terms, FAQs, per-subsystem or
per-application pages) and re-run `python3 build_library.py`. The builder reports the new
count and re-verifies (dead-DOI, economics, broken links) automatically. The remaining
enumerable topics (more plasma/nuclear/engineering terms, more reviewer questions, per-material
and per-diagnostic pages) can carry it to ~1000 without inventing anything.

## Deploy (morning)
1. Drag the whole `technical/` folder into a repo (or into the site repo under `/technical/`).
   All links are relative, so it is self-contained.
2. Ask for the **Lovable prompt** to mount `/technical/` and link it from the main nav + `learn/`.
3. Submit `sitemap.xml` in Search Console and reference `llms.txt` for AI crawlers.

Note: the URL path is `/technical/` (set in `build_library.py` as `BASE`); change it there and
rebuild if you want a different path.
