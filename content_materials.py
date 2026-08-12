# -*- coding: utf-8 -*-
"""Materials & magnets."""

def register(cat, page, F):
    cat("materials", "Materials & Magnets",
        "The materials that make a compact, high-field fusion machine possible — superconductors, "
        "structure, plasma-facing components — and the honest limits on each.", 5)

    page("superconducting-magnets","Superconducting Magnets for Fusion","materials",
         "High-temperature superconducting magnets are what make a compact, high-field fusion machine possible. Kronos's magnet study is deposited openly.",
         "The magnet is the machine. Everything about a compact fusion device follows from how much field its coils can hold.",
         [('p',f"Fusion needs strong magnetic fields to confine a hot plasma; the stronger the field, the smaller and cheaper the machine can be for the same performance. High-temperature superconductors — chiefly <a href='./rebco-tape.html'>REBCO</a> — carry enormous currents at high field with no resistive loss, enabling fields that copper coils could never sustain continuously."),
          ('facts',[("Breeder peak field",F["b_Bpeak"]),("Burner plug field",F["u_Bplug"]),
                    ("Conductor","REBCO HTS tape"),("Study","DOI "+F["doi_rebco"])]),
          ('gap',("Cyclic fatigue is a gate","The highest-field plug magnet is sound under static load, but cyclic fatigue at full field is a named engineering gate — one of the design's honest open items."))],
         related=["rebco-tape","high-field-magnets","quench-protection-detail","magnet-structure"],
         jtype="TechArticle")

    mats = [
     ("rebco-tape","REBCO HTS Tape","The rare-earth barium copper oxide conductor at the heart of Kronos's magnets.",
      [f"REBCO tape is a layered composite: a thin superconducting REBCO film on a strong metal substrate, stabilised with copper. It sustains very high current density in fields well beyond what low-temperature superconductors reach, which is why it enables the {F['b_Bpeak']} breeder field and the {F['u_Bplug']} burner plug.",
       "Kronos's REBCO study — deposited openly — maps the critical-current envelope, the winding-pack stack, bore-resolved stress, quench behaviour, neutron lifetime and fatigue, benchmarked against demonstrated coils."],
      [("Type","High-temperature superconductor"),("Role","Magnet conductor"),("Deposit","DOI "+F["doi_rebco"])],
      ["superconducting-magnets","high-field-magnets","magnet-structure"]),
     ("magnet-structure","Magnet Structural Materials","The high-strength alloys that hold a magnet together against its own field.",
      ["A high-field magnet generates immense Lorentz forces that try to blow it apart; the winding pack must be reinforced with high-strength, cryogenically-tough structural alloys and a robust case. The REBCO study resolves the stress through the winding-pack stack.",
       "Kronos analyses bore-resolved stress against material limits; the static case is sound, with cyclic fatigue flagged as the binding magnet gate."],
      [("Loads","Lorentz hoop forces"),("Analysis","Bore-resolved stress")],
      ["superconducting-magnets","rebco-tape","quench-protection-detail"]),
     ("plasma-facing-materials","Plasma-Facing Materials","The refractory materials that survive direct exposure to the plasma edge.",
      [f"Plasma-facing components — the first wall and divertor targets — must tolerate intense heat and particle flux. Refractory metals such as tungsten are standard for the highest-flux surfaces. HYPERION's first wall is designed for {F['b_wall']}; the burner's loading is far gentler.",
       "Material choice trades heat tolerance, erosion, and activation. Kronos reports the loadings and the qualification path rather than assuming survival."],
      [("First-wall load (breeder)",F["b_wall"]),("High-flux material","Refractory metals")],
      ["first-wall","divertor","neutron-damage-materials"]),
     ("neutron-damage-materials","Neutron Damage and Activation","How fusion neutrons degrade materials over time, and how Kronos accounts for it.",
      [f"Fusion neutrons displace atoms in structural materials (measured in displacements-per-atom) and can transmute them into radioactive isotopes. This sets component lifetimes and the plant's waste profile. The breeder, being neutron-rich ({F['b_fn']}), carries most of this load; the burner far less ({F['u_fn']}).",
       "Kronos screens activation and waste class per component rather than assuming low-activation materials solve the problem for free."],
      [("Breeder neutron fraction",F["b_fn"]),("Burner neutron fraction",F["u_fn"])],
      ["plasma-facing-materials","blanket","the-neutron-economy"]),
     ("reflector-liner","The Burner Reflector Liner","A reflective liner that returns escaping radiation, central to the burner's power balance.",
      ["The D–&sup3;He burner lines its central cell with a reflective material to return radiation to the plasma, improving the power balance. The liner's reflectivity is a deciding parameter for net power, and its material must balance that against neutron activation.",
       "Kronos flags the copper-versus-activation tension in the liner choice explicitly rather than assuming an ideal reflector."],
      [("Role","Radiation return"),("Trade","Reflectivity vs activation")],
      ["neutron-damage-materials","tandem-mirror","the-burner-design-point"]),
     ("quench-protection-detail","Quench Protection in Practice","The detection and energy-dump systems that keep a quenching magnet safe.",
      ["If a superconducting coil loses superconductivity, its stored energy must be removed before a local hot spot forms. Protection combines fast detection with a dump circuit that extracts the magnetic energy. Kronos analyses peak hot-spot temperature with an adiabatic method and reports the magnet as self-protecting within its design basis.",
       "Quench protection is one of the validation items that is confirmed in-model rather than left open."],
      [("Method","Adiabatic hot-spot"),("Result","Self-protecting (design basis)")],
      ["superconducting-magnets","rebco-tape","validation-suite-breeder"]),
    ]
    for slug,title,desc,paras,facts,rel in mats:
        page(slug,title,"materials",desc,desc,[('p',p) for p in paras],facts=facts,related=rel,jtype="TechArticle")
