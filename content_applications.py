# -*- coding: utf-8 -*-
"""Applications — where the two machines' output creates value."""

def register(cat, page, F):
    cat("applications", "Applications & Markets",
        "Where Kronos's output is used: firm grid and data-centre power, resilient defence "
        "installations, tritium and isotopes, helium-3 for quantum and medicine, and industrial heat.", 6.5)

    P = [
     ("grid-scale-power","Fusion for the Grid","Firm, dispatchable, zero-carbon power to anchor a decarbonised grid — the MetroVolt burner's core market.",
      "A decarbonised grid still needs firm power underneath the renewables. That is the burner's job.",
      [('p',f"As grids fill with intermittent solar and wind, the scarce, valuable commodity becomes firm, dispatchable, clean generation. The MetroVolt burner housing ({F['u_mv_len']}, {F['u_mv_net']} net, {F['u_mv_gw']} class) is aimed squarely at that role: steady baseload that can also follow load, with no operational carbon and secure fuel."),
       ('gap',("Cost is the gate","Whether fusion wins this market depends on capital cost and availability — Kronos's central commercial studies, not a settled result."))],
      [("Product","MetroVolt burner"),("Role","Firm, dispatchable baseload"),("Class",F["u_mv_gw"])],
      ["metrovolt","baseload-power","dispatchable-power"]),
     ("data-center-power","Fusion for Data Centres","Large, firm, clean power sited close to hyperscale load — a fast-growing demand fusion suits.",
      "AI and cloud growth are creating firm-power demand faster than grids can build it. Fusion is a natural answer.",
      [('p',f"Hyperscale data centres need very large, always-on, clean power — increasingly faster than local grids can supply. The low-neutron burner can, in principle, site nearer to load than a neutron-heavy plant, delivering firm point-of-use power. MetroVolt targets this at {F['u_mv_gw']} class."),
       ('gap',("Design-stage","Siting and delivery figures are design-stage targets for an unbuilt machine."))],
      [("Demand","Hyperscale, firm, clean"),("Fit","Low-neutron, point-of-use")],
      ["can-fusion-power-a-data-center","metrovolt","grid-scale-power"]),
     ("defense-power","Fusion for Defence Installations","Resilient, independent, low-signature power for fixed defence sites — the AEGIS housing.",
      "Critical defence installations need power that does not depend on a vulnerable grid. AEGIS is built for that.",
      [('p',f"Fixed defence installations value energy resilience and independence above almost all else. The AEGIS burner housing ({F['u_aeg_len']}, {F['u_aeg_net']} net) provides firm, self-contained, low-signature power for such fixed sites. It is a fixed-installation product — not a mobile or naval one."),
       ('gap',("Fixed installations only","Kronos scopes AEGIS to fixed defence installations; it does not claim mobile or shipboard deployment."))],
      [("Product","AEGIS burner"),("Use","Fixed defence installations"),("Net power",F["u_aeg_net"])],
      ["aegis","tandem-mirror","grid-scale-power"]),
     ("tritium-supply","Fusion as a Tritium Source","The breeder's blanket makes tritium the whole fusion industry needs — a product before net electricity.",
      "Tritium is scarce and the fusion industry needs more of it. The breeder makes it.",
      [('p',f"Tritium is scarce, expensive, and needed by every D–T fusion effort. HYPERION's blanket breeds {F['b_T']} at a breeding ratio of {F['b_TBR']} — more than it consumes — positioning Kronos as a potential supplier to the wider fusion ecosystem, independent of solving net electricity."),
       ('gap',("The bankable base","Of the breeder's outputs, tritium is the most clearly bankable near-term product; helium-3's value is framed as strategic, not immediate revenue."))],
      [("Output",F["b_T"]),("Breeding ratio",F["b_TBR"])],
      ["tritium-breeding","the-breeder-first-strategy","helium-3-for-quantum"]),
     ("medical-isotopes","Fusion for Medical Isotopes","A high-flux neutron source can produce medical isotopes — another breeder revenue path.",
      "Neutrons make medicine. The breeder's flux is a platform for isotopes hospitals need.",
      [('p',"Many medical isotopes are made by neutron irradiation, and supply is often fragile. The breeder's high neutron flux is a natural production platform, giving Kronos an isotope-supply optionality grounded in the machine's core output rather than a speculative new capability."),
       ('gap',("Optionality, grounded","This is framed as an option on the breeder's neutron economy, not a standalone claim."))],
      [("Basis","High-flux neutron source"),("Output","Medical isotopes")],
      ["isotope-platform","the-neutron-economy","tritium-supply"]),
     ("helium-3-for-quantum","Helium-3 for Quantum and Medicine","Breeder-produced helium-3 serves quantum computing and medical imaging — a strategic, scarce material.",
      "Helium-3 is scarce and strategically valuable well beyond fusion. The breeder makes its own.",
      [('p',f"Helium-3 is used in quantum-computing dilution refrigerators, neutron detection, and medical imaging — and is genuinely scarce. HYPERION co-produces about {F['b_He3']} as part of its fuel cycle, giving Kronos an internal supply and a strategic position in a constrained material."),
       ('gap',("Strategic value &ne; revenue","Kronos frames helium-3's value as strategic and enabling, distinct from near-term revenue, which rests on tritium."))],
      [("Breeder output",F["b_He3"]),("Uses","Quantum, detection, medical")],
      ["helium-3","helium-3-supply","medical-isotopes"]),
     ("industrial-heat-hydrogen","Fusion for Industrial Heat and Hydrogen","Firm high-grade heat and clean electricity can decarbonise industry and make hydrogen.",
      "Not all energy demand is electricity. Firm clean heat is just as hard to decarbonise — and fusion makes it.",
      [('p',"Heavy industry needs firm, high-grade heat, and clean hydrogen needs abundant clean power. A fusion plant's steady output can serve both — process heat and electrolytic hydrogen — extending its value beyond the electricity market."),
       ('gap',("Downstream of the core","These are applications of firm output; they inherit the same design-stage status as the generators themselves."))],
      [("Outputs","Process heat, hydrogen")],
      ["grid-scale-power","baseload-power","fusion-carbon-footprint"]),
    ]
    for slug,title,desc,lede,body,facts,rel in P:
        page(slug,title,"applications",desc,lede,body,facts=facts,related=rel,jtype="TechArticle")
