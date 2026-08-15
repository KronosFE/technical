# Kronos Fusion Energy — Technical Library

A 1,005-page public technical knowledge base for the Kronos compact fusion platform: the physics,
engineering, materials, components, methodology, validation, and honest open gates behind the
**HYPERION** spherical-tokamak D–T breeder and the **D–³He tandem-mirror generator** (AEGIS /
MetroVolt). SEO- and AI-optimized, on-brand, and grounded entirely in the frozen 2026 design canon
— nothing invented.

**Live:** [kronosfusionenergy.com/technical](https://www.kronosfusionenergy.com/technical)

## Structure
- `index.html` — master directory (22 categories)
- `<slug>.html` — 1,005 content pages (physics, components, materials, engineering, methodology,
  validation, innovations, competitive, devices, standards, safety, applications, glossary, FAQ, …)
- `sitemap.xml`, `llms.txt`, `robots.txt` — search-engine + AI-crawler discovery
- `_style.css` — shared brand stylesheet
- `build_library.py` + `content_*.py` — static generator (auto-discovers content modules);
  regenerate with `python3 build_library.py`
- `BUILD_REPORT.md` — full build report and guardrail summary

## Principles
Every number traces to one frozen canon block (single source of truth). Honest gates are carried
throughout: low-neutron **not** aneutronic; burner net power is requirement-class; breeder
construction is scheduled to begin **Q2 2027** (not yet built); figures are computed design targets.
No economics or financial information anywhere. Only live Zenodo DOIs are referenced. The generator
self-verifies (dead-DOI, economics, broken-link checks) on every build.

## Related
Formal papers + open data: [Publications](https://www.kronosfusionenergy.com/publications) ·
Explainer series: [Whitepapers](https://www.kronosfusionenergy.com/whitepapers) ·
Run it: [Live simulator](https://www.kronosfusionenergy.com/Physics_Validation_Simulation) ·
Deposits: [Zenodo community](https://zenodo.org/communities/kronos_fusion_energy)

© 2026 Kronos Fusion Energy, Inc. · Los Angeles, California.
