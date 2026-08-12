# -*- coding: utf-8 -*-
"""History & context — how the field arrived here, and where Kronos sits in it."""

def register(cat, page, F):
    cat("history", "History & Context",
        "How fusion research arrived at the compact, high-field, open-science moment — and "
        "where the Kronos breeder–burner architecture sits in that story.", 13)

    P = [
     ("history-of-fusion","A Short History of Fusion Energy","From 1950s tokamaks and mirrors to today's compact, high-field machines.",
      ["Fusion research began in earnest in the 1950s, splitting early into toroidal devices (the Soviet tokamak, stellarators) and open-ended magnetic mirrors. Tokamaks came to dominate after demonstrating superior confinement, and the field spent decades building ever-larger machines that steadily climbed the performance ladder.",
       "Two developments reopened the compact path: high-temperature superconductors that reach fields once impossible, and cheap computation for design and validation. Kronos's architecture draws on both lineages — the tokamak for its breeder, the mirror for its burner."],
      ["why-now","history-of-mirrors","the-breeder-first-strategy"]),
     ("history-of-mirrors","The Magnetic Mirror's Second Life","Why an old idea, reworked with modern magnets and physics, is compelling again.",
      ["Magnetic mirrors were among the earliest fusion concepts but fell behind tokamaks when simple mirrors proved leaky and unstable. Decades of physics — minimum-B stabilisation, the tandem-mirror plug, thermal barriers — solved the core problems, and modern high-field superconductors make the required plug fields attainable.",
       f"The Kronos burner is a modern tandem mirror: low-neutron D–&sup3;He, direct conversion, no disruptions — with the plug-density requirement (n_p/n_c &asymp; {F['u_np']}) as its honest open item."],
      ["tandem-mirror","minimum-b-configuration","history-of-fusion"]),
     ("history-of-superconducting-magnets","The Rise of High-Field Superconductors","How REBCO tape changed what a compact fusion machine can be.",
      [f"For decades, fusion magnets used low-temperature superconductors capped near modest fields. The maturing of REBCO high-temperature tape — carrying huge currents at very high field — lifted that cap, enabling the {F['b_Bpeak']} breeder and {F['u_Bplug']} burner fields that make a compact machine credible.",
       "High-field magnets are the single technology most responsible for the compact-fusion moment Kronos is built for."],
      ["rebco-tape","high-field-magnets","why-now"]),
     ("open-science-in-fusion","Open Science Comes to Fusion","Why publishing reproducible engines, not just results, is a shift for the field.",
      ["Fusion has historically communicated through papers and press. Depositing the actual reduced-order engines, inputs and expected outputs — so anyone can reproduce the numbers — is a cultural shift. Kronos leans into it: five open Zenodo deposits under CC BY 4.0, plus a public interactive model and live simulator.",
       "The wager is that in a field with a history of over-promising, radical reproducibility is a durable form of credibility."],
      ["reproducibility-overview","the-open-deposits","honesty-framework"]),
     ("the-fusion-landscape","The Modern Fusion Landscape","Public megaprojects, private compact ventures, and where Kronos's strategy differs.",
      ["Today's field spans public megaprojects proving burning-plasma physics at scale and a wave of private ventures pursuing compact, faster paths — most racing a single D–T machine toward net electricity. Kronos's differentiator is structural: a breeder that sells fuel and isotopes first, and a low-neutron burner for clean electricity, backed by an open, reproducible record.",
       "It competes less on a single hero number and more on a staged, verifiable path to value."],
      ["kronos-vs-dt-tokamak","kronos-vs-iter","the-breeder-first-strategy"]),
    ]
    for slug,title,desc,paras,rel in P:
        page(slug,title,"history",desc,desc,[('p',p) for p in paras],related=rel,jtype="TechArticle")
