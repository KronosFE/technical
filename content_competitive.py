# -*- coding: utf-8 -*-
"""Competitive landscape — public-sourced, approach-level, non-disparaging.
Frames how the field is organised and where Kronos sits, without unverifiable claims
about specific private programmes."""
def register(cat, page, F):
    cat("competitive", "Competitive Landscape",
        "How the fusion field is organised — by confinement approach, by fuel, and by business "
        "model — and where the Kronos breeder–burner architecture sits. Public-sourced and factual.", 12.5)
    P = [
     ("the-competitive-landscape","The Fusion Competitive Landscape","The field splits three ways — public megaprojects, private compact ventures, and alternative concepts — and Kronos takes a distinct path through all three.",
      ["The modern fusion field organises into three broad camps: large public megaprojects proving burning-plasma physics at scale; private ventures pursuing compact, faster routes to a power plant; and programmes exploring alternative confinement concepts. Most private effort races a single deuterium–tritium machine toward net electricity.",
       "Kronos's position is structurally different: a breeder that sells fuel, neutrons and isotopes before net electricity, paired with a low-neutron burner for clean direct-conversion power — argued on the public, reproducible record rather than a single hero number."],
      [("Camps","Public · private-compact · alternative")],
      ["the-three-approaches","how-to-compare-fusion","where-kronos-fits"]),
     ("the-three-approaches","Confinement Approaches Compared","Magnetic (tokamak, stellarator, mirror), inertial, and hybrid — the main routes to fusion.",
      [('facts' if False else 'noop','')],
      None, None),  # placeholder replaced below
     ("tokamak-approach","The Tokamak Approach","The most-studied path: a toroidal magnetic bottle with a driven plasma current.",
      ["The tokamak is the most experimentally mature confinement concept, with the largest performance database, exemplified by public devices such as JET and the ITER project. Its strengths are that database and its high confinement; its challenges are disruptions, steady-state current drive, and the neutron load of D–T operation.",
       "Kronos's breeder is a compact spherical tokamak — it draws on this mature science while running at low aspect ratio for high beta."],
      [("Maturity","Highest"),("Challenge","Disruptions, D–T neutrons")],
      ["spherical-tokamak","kronos-vs-dt-tokamak","stellarator-approach"]),
     ("stellarator-approach","The Stellarator Approach","Twisting the field with external coils alone — no plasma current, no disruptions.",
      ["The stellarator (e.g. the public W7-X device) confines plasma with intricately shaped external coils, needing no driven current and avoiding disruptions, at the cost of complex magnet geometry. It is a serious alternative to the tokamak for steady-state operation.",
       "Kronos does not use a stellarator, but the concept frames why the tokamak's plasma current — which the stellarator eliminates — is a design consideration."],
      [("Strength","No disruptions"),("Cost","Coil complexity")],
      ["stellarator","tokamak-approach","the-three-approaches"]),
     ("mirror-approach","The Magnetic-Mirror Approach","A linear machine — simple geometry, direct conversion, and the plugging challenge Kronos's burner addresses.",
      [f"The magnetic mirror confines plasma in a straight field, avoiding disruptions and enabling direct energy conversion, at the cost of end losses that must be plugged. Modern tandem-mirror physics solves the historical instabilities, and high-field superconductors make the required plug fields attainable.",
       f"The Kronos burner is a modern tandem mirror, with the plug-density requirement (n_p/n_c &asymp; {F['u_np']}) as its honest open item."],
      [("Strength","Linear, direct conversion"),("Challenge","End plugging")],
      ["tandem-mirror","tandem-mirror-vs-tokamak","history-of-mirrors"]),
     ("inertial-approach","The Inertial-Confinement Approach","Compressing fuel with lasers or beams — a pulsed alternative to magnetic confinement.",
      ["Inertial confinement (e.g. the public NIF facility, which achieved target energy gain in 2022) compresses fuel pellets to fuse under their own inertia. It is a fundamentally pulsed approach with different engineering challenges — driver efficiency and repetition rate — from magnetic confinement.",
       "Kronos uses magnetic confinement, a continuous rather than pulsed route to a power plant."],
      [("Type","Pulsed"),("Milestone","NIF target gain, 2022")],
      ["inertial-confinement","the-three-approaches","magnetic-confinement"]),
     ("dt-vs-advanced-fuels","Deuterium–Tritium vs Advanced Fuels","The field's central fuel divide — and why Kronos runs both sides of it.",
      [f"Most fusion uses D–T for its unmatched reactivity, accepting a heavy neutron load ({F['b_fn']}) and a steam cycle. A minority pursue low-neutron 'advanced' fuels (D–&sup3;He, p–&sup1;&sup1;B) for cleaner operation and direct conversion, accepting much higher temperatures. The two camps rarely overlap.",
       "Kronos runs both: D–T in the breeder to make fuel and neutrons, and low-neutron D–&sup3;He in the burner to make clean electricity — capturing each fuel's advantage where it fits."],
      [("Mainstream","D–T"),("Advanced","D–&sup3;He, p–&sup1;&sup1;B"),("Kronos","Both, by purpose")],
      ["fusion-fuels-overview","the-breeder-first-strategy","d-he3-fuel"]),
     ("neutron-heavy-vs-low-neutron","Neutron-Heavy vs Low-Neutron Machines","Where the fusion energy goes shapes everything — conversion, materials, siting.",
      [f"A D–T machine puts most of its energy into 14 MeV neutrons, driving a steam cycle and heavy shielding and activation. A low-neutron machine keeps most energy in charged particles, enabling direct conversion and gentler materials demands. The choice cascades through the whole plant.",
       f"Kronos uses the neutron-heavy breeder deliberately (neutrons are its product) and the low-neutron burner ({F['u_fn']}) for clean electricity — matching the neutron budget to the job."],
      [("Neutron-heavy","Breeder — "+F["b_fn"]),("Low-neutron","Burner — "+F["u_fn"])],
      ["the-neutron-economy","steam-cycle","direct-energy-conversion"]),
     ("how-to-compare-fusion","How to Compare Fusion Programmes Honestly","Look past hero numbers to closure, plant-level gain, capital and product timing.",
      ["A fair comparison of fusion efforts asks harder questions than 'what Q did you get?': Does the design actually close on power balance, stability and the fuel cycle together? Is the quoted gain scientific (plasma Q) or plant-level (net electricity)? What is the capital path? And — often overlooked — is there a product before net electricity?",
       "Kronos argues it compares well precisely on the last questions: a reproducible closed design, an honest split of scientific and engineering gain, and a saleable product staged ahead of the hardest milestone."],
      [("Ask","Closure · gain type · capital · product timing")],
      ["fusion-gain-q","the-operating-window","where-kronos-fits"]),
     ("where-kronos-fits","Where Kronos Fits","A breeder-first, two-machine, openly-validated path — distinct from the single-D–T-tokamak mainstream.",
      ["Against the field, Kronos's distinctives are: a two-machine architecture matching fuel to purpose; a materials-and-isotopes business that does not wait on net electricity; a low-neutron, direct-conversion electricity machine; and an openly reproducible record with every caveat stated. It competes less on a single number and more on a staged, verifiable path to value.",
       "It stands on the same shared physics database as the rest of the field, and says so."],
      [("Position","Breeder-first, two-machine, open")],
      ["the-breeder-first-strategy","innovation-two-machine-architecture","how-to-compare-fusion"]),
     ("the-public-programmes","Public Fusion Programmes","The megaprojects and national labs whose science the whole field — including Kronos — builds on.",
      ["Public programmes — the ITER project, national laboratories, and major devices like JET, W7-X, NSTX and NIF — establish the physics database and validated codes the entire field relies on. They are slow and large but foundational.",
       "Kronos anchors its assumptions (confinement scaling, magnet fields, reaction rates) to this public science rather than to first-principles optimism — benefiting from it rather than dismissing it."],
      [("Role","Foundational science")],
      ["kronos-vs-iter","confinement-scaling","the-competitive-landscape"]),
    ]
    # fill the placeholder page properly
    P[1] = ("the-three-approaches","Confinement Approaches Compared","Magnetic (tokamak, stellarator, mirror), inertial, and hybrid — the main routes to fusion.",
      ["The routes to fusion divide first by how the fuel is held: magnetic confinement (tokamaks, stellarators, mirrors) holds a steady plasma in a magnetic bottle; inertial confinement compresses fuel pellets in fast pulses; hybrid and alternative concepts explore the space between. Each implies very different engineering.",
       "Kronos uses magnetic confinement in two forms — a spherical tokamak for the breeder and a tandem mirror for the burner — choosing each geometry for the job it does."],
      [("Magnetic","Tokamak · stellarator · mirror"),("Inertial","Pulsed compression")],
      ["tokamak-approach","mirror-approach","inertial-approach"])
    for slug,title,desc,paras,facts,rel in P:
        page(slug,title,"competitive",desc,desc,[('p',p) for p in paras],facts=facts,related=rel,jtype="TechArticle")
