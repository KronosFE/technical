# -*- coding: utf-8 -*-
"""Process & methodology — how Kronos designs, simulates, freezes and gates."""

def register(cat, page, F):
    cat("methodology", "Process & Methodology",
        "How Kronos actually works: the design method, the simulation stack, the freeze "
        "discipline, the gate reviews, and the honesty framework that runs through all of it.", 3)

    P = [
     ("design-methodology","The Kronos Design Methodology","How a design point is chosen, scanned, and frozen — from parameter scans to a single reproducible operating point.",
      "Kronos designs from the physics outward and freezes to a single, reproducible point — then defends that point in the open.",
      [('p',"The design method starts with the fuel and the mission, not a platform. For each machine, a reduced-order model sweeps the parameter space — thousands of configurations — to find operating points that close on power balance, stability and the fuel cycle simultaneously."),
       ('p',f"A single configuration is then selected as the frozen design point (breeder config 22021, Q = {F['b_Q']}; burner Mode M, Q<sub>E</sub> = {F['u_QE']}). Freezing means every downstream artefact — papers, figures, the 3D model, this library — reproduces the same numbers from the same source."),
       ('gap',("Why freeze","A frozen point makes the whole record self-consistent and auditable. When the design changes, the freeze changes deliberately and visibly, not silently."))],
      [("Breeder point","config 22021, Q "+F["b_Q"]),("Burner point","Mode M, Q_E "+F["u_QE"])],
      ["design-space-exploration","the-freeze-discipline","gate-reviews"]),
     ("design-space-exploration","Design-Space Exploration","Kronos scans tens of thousands of configurations to find where a machine genuinely closes, not just where it looks good.",
      "A single hero number can hide a fragile design. Kronos maps the whole neighbourhood around its operating point.",
      [('p',"Rather than tune a single case, Kronos runs large parameter scans — the breeder design-space scan alone spans over 25,000 configurations — and reports the operating window, not just the peak. This shows how sensitive the design is and where the closure boundaries lie."),
       ('p',"Publishing the window, including the regions where the machine does <i>not</i> close, is a deliberate credibility choice."),
       ('gap',("Closure boundaries","The burner scans show closure crossing a specific fuel-fraction boundary; the deposit reports both sides of it."))],
      [("Breeder scan","25,000+ configurations")],
      ["design-methodology","uncertainty-quantification","the-operating-window"]),
     ("uncertainty-quantification","Uncertainty Quantification","Kronos runs Monte-Carlo uncertainty studies so a design point comes with error bars, not false precision.",
      "A number without an uncertainty is a guess in a lab coat. Kronos quantifies its own.",
      [('p',"Kronos propagates input uncertainties through its models with Monte-Carlo sampling, producing distributions and feasibility fractions rather than single deterministic values. Sensitivity (Sobol) and tornado analyses rank which assumptions the result actually depends on."),
       ('gap',("Honest error bars","Reporting a feasibility fraction — the share of sampled cases that still close — is more honest than a single point, and it is deposited alongside the point estimate."))],
      None,
      ["design-space-exploration","design-methodology","reproducibility-overview"]),
     ("the-freeze-discipline","The Freeze Discipline","A 'frozen' design point is the single source of truth every Kronos artefact must reproduce.",
      "One number, everywhere. That is the freeze discipline.",
      [('p',"When Kronos freezes a design, that operating point becomes canonical: papers, figures, the interactive 3D model, the live simulator and this library all draw from it. No artefact is allowed to quietly carry a different number."),
       ('p',f"The current freeze fixes the breeder at Q = {F['b_Q']} / {F['b_Pfus']} and the burner at Q<sub>E</sub> = {F['u_QE']} / f<sub>n</sub> = {F['u_fn']}."),
       ('gap',("Change control","When the design evolves, the freeze is updated deliberately and the change is recorded — never silently overwritten."))],
      None,
      ["design-methodology","reproducibility-overview","gate-reviews"]),
     ("gate-reviews","Gate Reviews (G1–G4)","Kronos advances through evidence-based go/no-go gates rather than declaring success.",
      "Progress at Kronos is gated on evidence, not enthusiasm. G1 through G4 are the checkpoints.",
      [('p',"The programme is structured around gate reviews: G1 (physics design freeze), then successive gates for component demonstration, an integrated prototype, and a first product. Each gate has explicit criteria that must be met before the next phase begins."),
       ('p',"The binding gate criteria are the design's largest open items — confinement assumptions on the breeder side, and the plug-density requirement on the burner side. Naming them as gates keeps the roadmap honest."),
       ('gap',("Where we are","G1, the physics design freeze, is complete. The gates ahead are demonstration-driven and are described as targets, not achievements."))],
      [("G1","Physics design freeze — done"),("Binding gates","Confinement; plug density")],
      ["the-freeze-discipline","plug-density-requirement","the-path-to-build"]),
     ("model-shadow-twin","From Model to Shadow to Digital Twin","How the public interactive model is designed to evolve into a live digital twin once hardware exists.",
      "Today's model is a design instrument; tomorrow's is a mirror of a running machine. Kronos is explicit about the difference.",
      [('p',"Kronos frames three stages of fidelity. The <b>model</b> is today's interactive, physics-grounded design instrument. A <b>shadow</b> would run alongside early hardware, fed by test data. A <b>digital twin</b> would mirror an operating machine in real time. The public 3D model is honest that it is stage one."),
       ('gap',("Not yet a twin","The interactive model is a schematic design tool. Calling it a 'digital twin' before hardware exists would overstate it — so Kronos does not."))],
      None,
      ["design-methodology","the-3d-model","the-path-to-build"]),
     ("honesty-framework","The Honesty Framework","Kronos states its open questions on the same page as its results — as a design principle.",
      "The most unusual thing about the Kronos record is what it refuses to hide.",
      [('p',"Every Kronos surface carries its caveats with its claims: low-neutron is never called aneutronic; net burner power is labelled requirement-class; the machines are stated to be unbuilt; economics are kept off public technical pages. This is a deliberate framework, not a disclaimer bolted on at the end."),
       ('p',"The bet is that in a field with a long history of over-promising, verifiable honesty is a competitive advantage with the serious audiences — national labs, technical investors, and reviewers."),
       ('gap',("Why it helps",'Honesty is framed as rigor: stating a gate is how you show you understand — and can close — the problem.'))],
      None,
      ["gate-reviews","reproducibility-overview","the-open-deposits"]),
    ]
    for slug,title,desc,lede,body,facts,rel in P:
        page(slug,title,"methodology",desc,lede,body,facts=facts,related=rel,jtype="TechArticle")
