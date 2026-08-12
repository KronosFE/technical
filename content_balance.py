# -*- coding: utf-8 -*-
"""Balance batch — deeper engineering, materials, methodology, validation, open-science."""

def register(cat, page, F):
    def art(slug,title,catk,desc,paras,facts=None,rel=None,gap=None):
        body=[('p',p) for p in paras]
        if gap: body.append(('gap',gap))
        page(slug,title,catk,desc,desc,body,facts=facts,related=rel or [],jtype="TechArticle")

    # --- engineering ---
    art("radial-build","The Radial Build","engineering",
        "The layer-by-layer stack from plasma to magnet — plasma, first wall, blanket, shield, vessel, coil — that every dimension follows from.",
        [f"The radial build is the ordered stack of components from the plasma outward: scrape-off layer, first wall, breeding blanket, neutron shield, vacuum vessel, thermal shield, and the superconducting coil. In a compact spherical tokamak (R&#8320; = {F['b_R0']}, A = {F['b_A']}) every millimetre is contested, especially at the centre column.",
         "Fixing the radial build is one of the first design acts: it sets the machine's size, its shielding margin, and the field the magnet must deliver."],
        [("Major radius",F["b_R0"]),("Aspect ratio",F["b_A"])],
        ["centre-column-challenge","blanket","shielding"],
        ("Tight by design","Low aspect ratio makes the radial build a genuine optimisation, not a formality — a live focus of the breeder design."))
    art("general-arrangement","The General Arrangement","engineering",
        "How the machine, its plant systems and its building fit together — the top-level layout.",
        ["The general arrangement places the reactor core within its balance of plant and building: heating and current-drive systems, cryoplant, power conversion, cooling, control room and, on the breeder, the tritium plant — all inside the shielded envelope. It is the drawing that turns a physics point into a facility.",
         "Kronos's representative engineering drawings make this legible without claiming fabrication-grade precision."],
        None,
        ["balance-of-plant","radial-build","the-path-to-build"])
    art("magnet-system","The Magnet System","engineering",
        "The full set of coils — toroidal field, poloidal field, central solenoid, and the burner's plugs — and how they work together.",
        [f"HYPERION's magnet system combines toroidal-field coils (up to {F['b_Bpeak']} at the conductor), poloidal-field coils for shape and position, and a central solenoid to drive current. The burner instead uses central-cell solenoids and high-field plug coils reaching {F['u_Bplug']}.",
         "All are wound from REBCO high-temperature superconductor — the enabling technology for both machines."],
        [("Breeder peak field",F["b_Bpeak"]),("Burner plug field",F["u_Bplug"])],
        ["superconducting-magnets","toroidal-field-coil","central-solenoid"])
    art("systems-integration","Systems Integration","engineering",
        "Managing the interfaces where subsystems meet — the discipline that keeps a complex machine coherent.",
        ["Every subsystem touches others — magnets to structure, vessel to blanket, heating to vacuum, controls to everything. Systems integration manages those interfaces so the machine works as a whole. The vacuum vessel and the control/safety system are the busiest interface hubs.",
         "Kronos maps these interfaces explicitly as part of its construction-readiness work."],
        None,
        ["balance-of-plant","instrumentation-control","the-path-to-build"])

    # --- materials ---
    art("winding-pack","The Winding Pack","materials",
        "The layered stack of superconductor, stabiliser and structure that makes up a magnet coil.",
        ["A magnet coil is built from a winding pack: REBCO tape, copper stabiliser, and structural reinforcement, insulated and impregnated. Its layered composition (the λ-stack) balances current-carrying capacity against the strength to resist Lorentz forces.",
         "The REBCO deposit resolves the winding-pack stack and the stress through it."],
        [("Conductor","REBCO tape"),("Deposit","DOI "+F["doi_rebco"])],
        ["rebco-tape","magnet-structure","cold-mass"])
    art("critical-current-envelope","The Critical-Current Envelope","materials",
        "The map of how much current REBCO carries across field and temperature — the magnet's operating boundary.",
        [f"A superconductor's critical current falls as field and temperature rise, tracing a critical surface. Magnet design keeps operation safely inside it with margin. Reaching {F['b_Bpeak']} and {F['u_Bplug']} means operating REBCO near the high-field frontier of that envelope, which the REBCO study maps explicitly."],
        [("Envelope","J_c(B,T)"),("Study","DOI "+F["doi_rebco"])],
        ["rebco-tape","critical-current","high-field-magnets"])
    art("materials-qualification","Materials Qualification","materials",
        "Proving that each material survives its service environment before it goes into a machine.",
        ["Every structural and plasma-facing material must be qualified against its real environment — heat flux, neutron damage, cyclic stress, corrosion — through testing. Kronos frames materials qualification as scheduled work on the path to build, with the honest gates (notably magnet cyclic fatigue) named.",
         "Representative material choices are stated; fabrication-grade qualification is future work, not a claimed result."],
        None,
        ["magnet-fatigue","neutron-damage-materials","the-path-to-build"])

    # --- methodology / validation / open science ---
    art("reduced-order-modeling","Reduced-Order Modelling","methodology",
        "Fast, physics-based models that scan the design space and reproduce the frozen point — the engines behind every number.",
        ["Kronos's deposited engines are reduced-order models: fast, transparent, physics-based calculators that capture the essential balances without the cost of full simulation. They are what make large design-space scans and open reproduction practical, and they run live in the public model's in-browser solver.",
         "Where a claim needs high-fidelity FEA, CFD or neutronics, Kronos says so rather than over-reading the reduced-order result."],
        None,
        ["design-space-exploration","reproducibility-overview","the-3d-model"],
        ("Honest about fidelity","Reduced-order is right for design scoping; Kronos flags where full high-fidelity analysis is still owed."))
    art("high-fidelity-analysis","High-Fidelity Analysis","methodology",
        "The full FEA, CFD and neutronics that must follow the reduced-order design before construction.",
        ["Beyond the reduced-order engines lies the detailed-design work: full structural and fatigue FEA, thermal-hydraulic CFD, and MCNP-class neutronics. Kronos places this on the path to build as scheduled work, not as a completed claim — the honest distinction between a design study and an engineered machine."],
        None,
        ["reduced-order-modeling","the-path-to-build","materials-qualification"])
    art("what-reproducibility-proves","What Reproducibility Does and Doesn't Prove","validation",
        "Reproducing a computation proves it follows from the model and inputs — not that the unbuilt machine will behave that way.",
        ["An honest account of the limits of reproducibility: re-running a Kronos deposit proves the published number follows rigorously from the stated model and inputs. It does not, by itself, prove that a machine — which does not yet exist — will match the model. Kronos states both halves of that clearly.",
         "This is why every figure is labelled a computed design target, and why the binding gates are named separately."],
        None,
        ["reproducibility-overview","tier-1-tier-2","has-kronos-built-a-reactor"],
        ("Two different claims","'The math is right' and 'the machine will work' are different claims; Kronos never lets the first stand in for the second."))
    art("the-ai-quantum-record","The AI, ML & Quantum Record","openscience",
        "An open, reproducible record of the AI/ML stack and an honest quantum resource estimate.",
        [f"Alongside the physics deposits, Kronos publishes a reproducibility record for its AI/ML methods and a quantum-computing proof-of-concept with an honest resource estimate — including the candid conclusion that quantum offers no near-term crossover for these problems. It is deposited openly (DOI {F['doi_ai']})."],
        [("Deposit","DOI "+F["doi_ai"])],
        ["the-open-deposits","reproducibility-overview","reduced-order-modeling"],
        ("Honest about limits","The quantum record's headline is a negative result stated plainly — no near-term advantage — which is itself a credibility signal."))
    art("the-dec-record","The Direct Energy Conversion Record","openscience",
        "The open deposit behind the burner's direct-conversion efficiency.",
        [f"The burner's direct energy conversion — recovering charged-particle energy as electricity at about {F['u_dec']} — is backed by its own open deposit (DOI {F['doi_dec']}), giving the {F['u_QE']} engineering-gain figure a reproducible basis."],
        [("DEC efficiency",F["u_dec"]),("Deposit","DOI "+F["doi_dec"])],
        ["direct-energy-conversion","the-open-deposits","the-burner-design-point"])
    art("the-rebco-record","The REBCO Magnet Record","openscience",
        "The open deposit behind the high-field magnet claims.",
        [f"Kronos's high-field magnet claims — {F['b_Bpeak']} in the breeder, {F['u_Bplug']} in the burner plug — rest on an open REBCO study (DOI {F['doi_rebco']}) covering the critical-current envelope, winding-pack stack, bore-resolved stress, quench, neutron lifetime and the honest fatigue gate."],
        [("Deposit","DOI "+F["doi_rebco"])],
        ["superconducting-magnets","rebco-tape","the-open-deposits"])
