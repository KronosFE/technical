# -*- coding: utf-8 -*-
"""FAQ & honest explainers — one question per page, FAQPage schema."""

def register(cat, page, F):
    cat("faq", "Questions & Honest Answers",
        "Direct answers to the questions serious reviewers ask — about the physics, the "
        "claims, the risks, and what is and is not yet proven.", 9)

    # (slug, question, one-line, answer-paragraphs, related)
    Q = [
     ("is-kronos-fusion-aneutronic","Is Kronos fusion aneutronic?",
      "No. The burner is low-neutron, not aneutronic — a distinction Kronos always makes.",
      [f"No. The D–&sup3;He burner is <b>low-neutron</b>, with a neutron fraction of about {F['u_fn']} — far below D–T's {F['b_fn']}, but not zero. Side D–D reactions produce neutrons, so 'aneutronic' would be an overstatement, and Kronos never uses the word for it.",
       f"The breeder is deliberately neutron-rich; its neutrons are the product. Only the far-future proton–boron endpoint approaches truly aneutronic operation, and Kronos frames that as a research destination, not its commercial baseline."],
      ["d-he3-fuel","the-neutron-economy","dt-fuel"]),
     ("has-kronos-built-a-reactor","Has Kronos built a reactor?",
      "No. Kronos is a design-and-simulation study; the integrated machines are not yet built.",
      ["No. Kronos is at the physics-design and simulation stage. Every figure it publishes is a computed design target, reproducible from open deposits, and the interactive model is a design instrument — not a mirror of operating hardware.",
       "Kronos states this plainly on every technical surface rather than letting an impressive model imply otherwise. The roadmap to hardware runs through explicit gate reviews."],
      ["gate-reviews","the-path-to-build","reproducibility-overview"]),
     ("how-do-we-know-the-numbers-are-real","How do we know the Kronos numbers are real?",
      "Because you can download the engines and reproduce them yourself.",
      [f"You do not have to trust them. The reduced-order engines, inputs and expected outputs are deposited openly on Zenodo (CC&nbsp;BY&nbsp;4.0). An independent reviewer can re-run them and reproduce the published figures — byte-exact for deterministic results, within tolerance otherwise.",
       f"The breeder's Q = {F['b_Q']} is backed by a {F['b_checks']}-check validation suite; the burner's Q<sub>E</sub> = {F['u_QE']} by a {F['u_checks']}-check suite."],
      ["reproducibility-overview","how-to-reproduce","the-open-deposits"]),
     ("whats-the-catch-with-the-burner","What is the catch with the burner?",
      "Net power is requirement-class: it depends on reaching a plug-density ratio near "+F["u_np"]+".",
      [f"The honest catch is the plug-density requirement. The burner's net-positive engineering gain depends on the end plugs reaching a density about {F['u_np']}&times; the central cell to build a deep enough confining potential. Until a plug demonstration reaches that ratio, net power is a target, not a measured result.",
       "Kronos labels this <b>requirement-class</b> and puts it front and centre rather than burying it."],
      ["plug-density-requirement","tandem-mirror","validation-suite-burner"]),
     ("why-two-machines","Why does Kronos build two different machines?",
      "Because fuel should follow purpose: one machine breeds fuel, the other burns it for electricity.",
      ["The breeder and burner do different jobs, so they use different fuels and geometries. The spherical-tokamak breeder makes neutrons, tritium and helium-3; the tandem-mirror burner converts D–&sup3;He directly to electricity. 'Fuel follows purpose, not platform.'",
       "Building the breeder first gives Kronos a saleable product — isotopes and neutrons — before the hardest net-electric milestone is reached."],
      ["the-breeder-first-strategy","spherical-tokamak","tandem-mirror"]),
     ("can-a-fusion-plant-melt-down","Can a Kronos machine melt down?",
      "No. A fusion plasma has no chain reaction and holds only seconds of fuel; loss of control simply stops it.",
      ["No. Fusion has no chain reaction and no critical mass. The plasma holds only a tiny, continuously-supplied amount of fuel; anything that disturbs it — a fault, a power loss — makes the plasma cool and stop, rather than run away. There is no meltdown pathway.",
       "The burner, being a linear mirror, also avoids the tokamak disruption failure mode entirely."],
      ["disruptions","fusion-basics","the-path-to-build"]),
     ("what-are-the-open-questions","What are Kronos's biggest open questions?",
      "The plug-density requirement, plug-magnet cyclic fatigue, and breeder confinement and divertor assumptions.",
      [f"Kronos names its binding gates openly: the burner's plug-density requirement (n<sub>p</sub>/n<sub>c</sub> &asymp; {F['u_np']}); cyclic fatigue of the high-field plug magnet; and, on the breeder, the confinement quality assumption (H<sub>98</sub> = {F['b_H98']}) and the divertor's high radiated-fraction requirement.",
       "Stating these as gates is the point: it shows the problems are understood and have defined closure paths."],
      ["plug-density-requirement","gate-reviews","superconducting-magnets"]),
     ("does-kronos-claim-net-electricity","Does Kronos claim net electricity today?",
      "No. Net electricity is a computed design target with stated gates, not a demonstrated result.",
      ["No. The engineering-gain figures are computed design targets, and the burner's are explicitly requirement-class. Kronos separates plasma gain from plant-level net electricity and never conflates a high plasma Q with proven grid power.",
       "This care is deliberate in a field with a history of over-claiming."],
      ["fusion-gain-q","plug-density-requirement","does-kronos-claim-net-electricity"][:2]),
    ]
    for slug,q,oneliner,ans,rel in Q:
        page(slug,q,"faq",oneliner,oneliner,[('qa',[(q," ".join(f"<p>{a}</p>" for a in ans))])],
             related=rel,jtype="FAQPage",kicker="Question")
