# -*- coding: utf-8 -*-
"""Physics & fusion science pages."""

def register(cat, page, F):
    cat("physics", "Physics & Fusion Science",
        "The physics behind the Kronos breeder–burner architecture — confinement, stability, "
        "transport, heating, and the fuel cycles — grounded in decades of experimental fusion science.", 1)

    page("fusion-basics", "What Fusion Is, and Why It Is Hard", "physics",
         "Fusion releases energy by merging light nuclei. Confining a hot enough, dense enough plasma for long enough is the engineering challenge Kronos is built to solve.",
         "Fusion powers the stars. On Earth the challenge is not whether it works — it does — but whether a machine can hold a plasma hot enough, dense enough, and long enough to produce more energy than it consumes, and do it economically.",
         [('p', "Nuclear fusion merges light atomic nuclei into heavier ones, converting a sliver of their mass into energy according to E = mc&sup2;. A deuterium–tritium reaction releases 17.6&nbsp;MeV — millions of times more energy per reaction than burning a chemical bond. The catch is that nuclei are positively charged and repel one another; only at temperatures of tens to hundreds of millions of degrees do they move fast enough to fuse."),
          ('h2', "The three levers"),
          ('p', "Every fusion concept trades off the same three quantities, combined in the <a href=\"./lawson-criterion.html\">Lawson triple product</a>: plasma temperature, density, and energy confinement time. Raise all three high enough and the plasma produces net power."),
          ('ul', ["<b>Temperature</b> — the fuel must be hot enough for nuclei to tunnel through their mutual repulsion; D–T peaks near 10–20&nbsp;keV (100–230&nbsp;million&nbsp;K).",
                  "<b>Density</b> — more nuclei per cubic metre means more reactions per second.",
                  "<b>Confinement time</b> — the plasma's heat must be held long enough to sustain the reactions rather than leaking away."]),
          ('h2', "How Kronos approaches it"),
          ('p', "Kronos runs a two-machine strategy. The <a href=\"./spherical-tokamak.html\">HYPERION breeder</a> is a compact spherical tokamak that produces neutrons and breeds tritium; the <a href=\"./tandem-mirror.html\">D–&sup3;He tandem-mirror burner</a> converts a fuel that is far cleaner in neutrons directly into electricity. Neither machine claims ignition — both are honestly described as <a href=\"./ignition-vs-driven.html\">driven systems</a>."),
          ('gap', ("Honest framing", "Kronos publishes computed design targets, not measured results — the integrated machines are not yet built, though construction of the HYPERION breeder is scheduled to begin in Q2 2027. Every number on this page traces to an open, reproducible deposit.")),
          ],
         facts=[("Breeder gain Q", F["b_Q"]), ("Breeder fusion power", F["b_Pfus"]),
                ("Burner neutron fraction", F["u_fn"]+" (low-neutron)"), ("Status", "Design & simulation study")],
         related=["lawson-criterion","spherical-tokamak","tandem-mirror","ignition-vs-driven","fusion-gain-q"],
         jtype="TechArticle")

    page("lawson-criterion", "The Lawson Criterion and the Triple Product", "physics",
         "The Lawson criterion sets the minimum density-confinement product for net fusion power. The triple product adds temperature and is the field's standard figure of merit.",
         "One inequality governs whether a fusion plasma can pay for itself. Kronos designs to it explicitly, and reports where each machine sits against it.",
         [('p', "John Lawson's 1955 criterion states that for a plasma to release more fusion energy than it takes to heat it, the product of density <i>n</i> and energy confinement time &tau;<sub>E</sub> must exceed a threshold that depends on temperature. The modern form multiplies in temperature <i>T</i> to give the <b>triple product</b> <i>n&middot;T&middot;&tau;<sub>E</sub></i>, measured in keV&middot;s&middot;m<sup>-3</sup>."),
          ('h2', "Why it is the right yardstick"),
          ('p', "The triple product captures the essential tension: fusion power scales with density squared and with reactivity (a strong function of temperature), while losses scale with how quickly the plasma cools. A machine can reach the same triple product with a hot, diffuse plasma or a cooler, denser one — which is exactly the design freedom Kronos exploits across its two machines."),
          ('h2', "Where Kronos sits"),
          ('p', f"The HYPERION breeder is designed for an energy confinement time of {F['b_tauE']} at a confinement quality of H<sub>98</sub>&nbsp;=&nbsp;{F['b_H98']}, an ion temperature near {F['b_Ti']}, giving a fusion gain of Q&nbsp;=&nbsp;{F['b_Q']}. The D–&sup3;He burner operates far hotter — around {F['u_Ti']} — because its fuel requires it."),
          ('gap', ("Open gate", f"The breeder's confinement target assumes H<sub>98</sub>&nbsp;=&nbsp;{F['b_H98']} — solidly within the experimental database but not yet demonstrated at this exact configuration. It is one of the design's named gates.")),
          ],
         facts=[("Break-even", "Q = 1"), ("Confinement time (breeder)", F["b_tauE"]),
                ("Confinement quality", "H98 = "+F["b_H98"]), ("Ion temperature (breeder)", F["b_Ti"])],
         related=["fusion-gain-q","energy-confinement-time","ignition-vs-driven","fusion-basics"],
         jtype="TechArticle")

    page("fusion-gain-q", "Fusion Gain (Q) and Engineering Gain", "physics",
         "Q is fusion power divided by heating power. Engineering gain counts net electricity against all plant power. Kronos reports both, honestly.",
         "Q is the number everyone quotes — but it is not the number that keeps the lights on. Kronos is careful to distinguish scientific gain from the plant-level gain that matters commercially.",
         [('p', f"<b>Fusion gain</b> Q is the ratio of fusion power produced to external heating power supplied. Q&nbsp;=&nbsp;1 is scientific break-even; Q&nbsp;&rarr;&nbsp;&infin; is ignition. The HYPERION breeder is designed for Q&nbsp;=&nbsp;{F['b_Q']} — its {F['b_Pfus']} of fusion power against {F['b_Paux']} of auxiliary heating."),
          ('h2', "Scientific vs engineering gain"),
          ('p', "Q measures the plasma. The plant-level <b>engineering gain</b> counts net electricity delivered to the grid against every watt the facility consumes — magnets, cryogenics, heating, pumps, controls. A machine can have an impressive Q and still not be a net electricity producer. Kronos reports the plant-level ledger separately for each product housing rather than letting a high plasma Q stand in for commercial viability."),
          ('h2', "The burner's direct advantage"),
          ('p', f"The D–&sup3;He burner is quoted at an engineering gain Q<sub>E</sub>&nbsp;=&nbsp;{F['u_QE']} because it converts charged-particle energy straight to electricity via <a href=\"./direct-energy-conversion.html\">direct energy conversion</a> at about {F['u_dec']} efficiency, skipping the thermal cycle's losses."),
          ('gap', ("Requirement-class result", f"The burner's net-positive engineering gain is a <i>requirement</i>: it depends on achieving a plug-to-central density ratio of about {F['u_np']}. Until a plug demonstration reaches it, net power is a target, not a measured outcome.")),
          ],
         facts=[("Breeder Q", F["b_Q"]), ("Breeder P_fus", F["b_Pfus"]), ("Breeder P_aux", F["b_Paux"]),
                ("Burner Q_E", F["u_QE"]), ("DEC efficiency", F["u_dec"])],
         related=["direct-energy-conversion","ignition-vs-driven","lawson-criterion","plug-density-requirement"],
         jtype="TechArticle")

    page("ignition-vs-driven", "Ignition vs Driven Operation", "physics",
         "An igniting plasma sustains itself; a driven plasma is continuously heated. Kronos designs driven systems on purpose — they are controllable and honest.",
         "Much of fusion's mystique attaches to ignition. Kronos deliberately does not chase it, and explains why a driven machine is the more controllable, more honest engineering choice.",
         [('p', "In an <b>igniting</b> plasma, fusion self-heating alone keeps the fuel hot with no external input — Q&nbsp;&rarr;&nbsp;&infin;. In a <b>driven</b> plasma, external heating runs continuously and the machine produces a steady multiple of that input. Both can be net-energy-positive; they differ in control and risk."),
          ('h2', "Why Kronos chooses driven"),
          ('ul', ["<b>Control.</b> A driven plasma is steered by its heating systems — turn the input down and the plasma responds. An igniting burn must be controlled by other means.",
                  "<b>Honesty.</b> Quoting a finite Q with its heating power stated is a complete, checkable claim; 'ignition' invites over-reading.",
                  f"<b>Fit to the fuel.</b> The D–&sup3;He burner runs hot ({F['u_Ti']}) and is inherently a driven system; the breeder's Q&nbsp;=&nbsp;{F['b_Q']} is comfortably net-positive without needing self-sustainment."]),
          ('gap', ("What this costs", "A driven machine must supply auxiliary heating for its whole operating life, which the engineering-gain ledger accounts for explicitly.")),
          ],
         facts=[("Breeder", "Driven, Q = "+F["b_Q"]), ("Burner", "Driven, Q_E = "+F["u_QE"]),
                ("Ignition claimed?", "No — by design")],
         related=["fusion-gain-q","lawson-criterion","fusion-basics"],
         jtype="TechArticle")

    # --- fuels ---
    fuels = [
        ("dt-fuel","Deuterium–Tritium (D–T) Fuel","D–T is the most reactive fusion fuel and the breeder's choice. It is neutron-rich, which Kronos uses deliberately to breed tritium and drive the burner economy.",
         "D–T is where practical fusion starts: the highest reactivity at the lowest temperature. Kronos embraces its neutrons rather than apologising for them.",
         [('p', f"Deuterium and tritium fuse to helium-4 plus a 14.1&nbsp;MeV neutron, releasing 17.6&nbsp;MeV total. It has the highest reactivity of any candidate fuel and peaks at a comparatively low {F['b_Ti']}, which is why the HYPERION breeder uses it."),
          ('p', f"About {F['b_fn']} of D–T energy leaves as neutrons. Kronos treats that as a feature: the neutrons breed tritium in the blanket (target breeding ratio {F['b_TBR']}) and co-produce helium-3, feeding the burner side of the architecture."),
          ('gap',("Tritium is bred, not mined","Tritium does not occur naturally in useful quantities. The breeder must make its own — the blanket's job — targeting "+F['b_T']+" per year."))],
         [("Reaction","D + T &rarr; &sup4;He + n"),("Energy","17.6 MeV"),("Neutron fraction",F["b_fn"]),("Peak temperature","~"+F["b_Ti"])],
         ["tritium-breeding","catalyzed-dd","d-he3-fuel","the-neutron-economy"]),
        ("d-he3-fuel","Deuterium–Helium-3 (D–&sup3;He) Fuel","D–&sup3;He is the burner's fuel — low in neutrons and ideal for direct energy conversion, at the cost of much higher temperature.",
         "D–&sup3;He is the reason the burner can convert energy directly to electricity. It trades a far cleaner neutron budget for a much hotter, harder-to-confine plasma.",
         [('p', f"Deuterium and helium-3 fuse to helium-4 and a proton, releasing 18.3&nbsp;MeV as charged particles — which can be converted to electricity directly. The Kronos burner runs this reaction at about {F['u_Ti']} with a neutron fraction of only {F['u_fn']}."),
          ('p', "Because most of the energy is in charged particles, the burner uses <a href=\"./direct-energy-conversion.html\">direct energy conversion</a> rather than a steam cycle. That is the architectural payoff of choosing this fuel."),
          ('gap',("Low-neutron, not aneutronic",f"Side D–D reactions still produce neutrons, so the burner's neutron fraction is {F['u_fn']} — low, but not zero. Kronos never describes it as aneutronic."))],
         [("Reaction","D + &sup3;He &rarr; &sup4;He + p"),("Energy","18.3 MeV"),("Neutron fraction",F["u_fn"]),("Temperature","~"+F["u_Ti"])],
         ["direct-energy-conversion","helium-3-supply","tandem-mirror","the-neutron-economy"]),
        ("catalyzed-dd","Catalysed Deuterium–Deuterium (D–D)","Pure-deuterium operation removes the tritium supply problem but demands even higher performance. Kronos studies it as a fuel-flexibility endpoint.",
         "D–D fusion needs only deuterium — abundant in seawater — but asks more of the machine. Kronos treats it as a strategic option, not a baseline.",
         [('p', "Deuterium fuses with itself along two branches of nearly equal probability, one yielding tritium and a proton, the other helium-3 and a neutron. 'Catalysed' D–D burns the tritium and helium-3 in situ. The appeal is fuel that needs no breeding; the cost is a lower reactivity that demands higher temperature and confinement."),
          ('gap',("Where it fits","Kronos maps D–D as a fuel-flexibility endpoint rather than the commercial baseline — the deposits report where a pure-D burner point does and does not close."))],
         [("Fuel","Deuterium only"),("Source","Seawater (abundant)"),("Trade","Higher temperature required")],
         ["dt-fuel","d-he3-fuel","fusion-fuels-overview"]),
    ]
    for slug,title,desc,lede,body,facts,rel in fuels:
        page(slug,title,"physics",desc,lede,body,facts=facts,related=rel,jtype="TechArticle")

    page("fusion-fuels-overview","Fusion Fuel Cycles Compared","physics",
         "A side-by-side of D–T, D–&sup3;He and D–D: reactivity, temperature, neutron budget, and where each fits in the Kronos breeder–burner strategy.",
         "There is no single best fusion fuel — only the right fuel for the job. Kronos runs two of them, on purpose.",
         [('p',"The Kronos thesis is that fuel should follow purpose. The breeder uses neutron-rich D–T to make tritium and neutrons; the burner uses low-neutron D–&sup3;He to make electricity cleanly and directly."),
          ('facts',[("D–T","Highest reactivity; "+F["b_fn"]+" neutrons; breeds tritium"),
                    ("D–&sup3;He","Low-neutron ("+F["u_fn"]+"); direct conversion; needs "+F["u_Ti"]),
                    ("D–D","Deuterium-only; no breeding; highest performance demand")]),
          ('gap',("The strategy","'Fuel follows purpose, not platform' — the breeder and burner are optimised for different fuels because they do different jobs."))],
         related=["dt-fuel","d-he3-fuel","catalyzed-dd","the-breeder-first-strategy"],
         jtype="TechArticle")
