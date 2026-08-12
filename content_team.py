# -*- coding: utf-8 -*-
"""Team & heritage — deliberately conservative: aggregate and public-facing only.
No sensitive individual affiliations, no internal legal tier."""

def register(cat, page, F):
    cat("team", "Team & Heritage",
        "The experience behind Kronos — decades of work across the world's fusion and "
        "large-science programmes, described at the level the public record already reflects.", 10)

    page("the-experience-behind-kronos","The Experience Behind Kronos","team",
         "Kronos is built by scientists and engineers whose careers span the world's major fusion and large-science programmes — six decades of accumulated fusion experience.",
         "Kronos is not a first attempt at fusion. It is the work of people who have spent their careers on it.",
         [('p',"The Kronos technical bench brings together experience from across the international fusion and large-science community — tokamak and mirror physics, superconducting magnets, cryogenics, materials, and direct energy conversion — accumulated over decades of hands-on programme work."),
          ('p',"The design record reflects that depth: conservative assumptions anchored to real experimental databases, honest gates where experience says the hard problems are, and an open, reproducible presentation."),
          ('gap',("How we describe the team","Kronos describes its people at the level already reflected in the public record, and keeps individual affiliations and internal matters appropriately private."))],
         related=["the-scientific-approach","the-honesty-framework-in-practice","design-methodology"],
         jtype="TechArticle")

    page("the-scientific-approach","The Kronos Scientific Approach","team",
         "Conservative assumptions, open data, and explicit gates — the scientific posture that runs through the whole Kronos programme.",
         "The Kronos posture is deliberately unglamorous: assume less, show more, and name the hard parts.",
         [('p',"Rather than optimistic first-principles projections, Kronos anchors its performance assumptions to established experimental databases — standard H-mode confinement, demonstrated magnet fields, measured reaction rates — and then reports where the design still has to be proven."),
          ('p',"That posture is a fit to the audience: national labs, technical investors and reviewers reward verifiable conservatism over hero numbers."),
          ('gap',("Why it matters","In a field with a long history of over-promising, a conservative, reproducible presentation is itself a differentiator."))],
         related=["the-experience-behind-kronos","design-methodology","honesty-framework"],
         jtype="TechArticle")

    page("the-honesty-framework-in-practice","Honesty as an Engineering Principle","team",
         "How the honesty framework shows up in day-to-day engineering decisions, not just messaging.",
         "For Kronos, honesty is not a communications style — it is an engineering discipline.",
         [('p',"The same discipline that labels the burner requirement-class and calls the neutron budget low-neutron-not-aneutronic also drives internal decisions: assumptions are graded, uncertainties are propagated, and design points are frozen so nothing drifts. Honesty and rigour are the same habit."),
          ('gap',("The payoff","Serious diligence tends to find the caveats anyway — so stating them first builds credibility instead of costing it."))],
         related=["honesty-framework","the-scientific-approach","reproducibility-overview"],
         jtype="TechArticle")
