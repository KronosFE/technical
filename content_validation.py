# -*- coding: utf-8 -*-
"""Validation & reproducibility — the real validation system, honestly described."""

def register(cat, page, F):
    cat("validation", "Validation & Reproducibility",
        "How Kronos checks its own physics: a graded validation suite, a byte-exact "
        "reproduction protocol, and an open deposit anyone can re-run.", 2)

    page("reproducibility-overview","Reproducibility at Kronos","validation",
         "Every headline number is backed by an open deposit that anyone can download and re-run to the same result. This is the core of the Kronos credibility model.",
         "Kronos's answer to 'how do we know?' is not a claim — it is a download. The engines, inputs and expected outputs are public, and they reproduce.",
         [('p',f"The Kronos design record is deposited openly on Zenodo under CC&nbsp;BY&nbsp;4.0. Each deposit contains the reduced-order engines, the input decks, and the expected outputs, so an independent reviewer can reproduce the published numbers rather than take them on trust."),
          ('h2',"Two tiers of reproduction"),
          ('ul',["<b>Tier&nbsp;1 — byte-exact.</b> Deterministic calculations reproduce to the exact byte on a matching environment.",
                 "<b>Tier&nbsp;2 — tolerance.</b> Calculations with legitimate numerical variation reproduce within a stated tolerance."]),
          ('facts',[("Breeder validation checks",F["b_checks"]),("Burner validation checks",F["u_checks"]),
                    ("Breeder deposit","DOI "+F["doi_b"]),("Burner deposit","DOI "+F["doi_u"])]),
          ('gap',("What reproducibility does and does not prove","Reproducing a computation proves the result follows from the stated model and inputs. It does not prove the model matches a machine not yet operating (the HYPERION breeder is scheduled to begin construction in Q2 2027) — which is why Kronos labels its figures computed design targets."))],
         related=["tier-1-tier-2","validation-suite-breeder","validation-suite-burner","how-to-reproduce"],
         jtype="TechArticle")

    page("tier-1-tier-2","Tier-1 and Tier-2 Reproduction","validation",
         "Kronos grades every reproducible result as byte-exact (Tier 1) or within-tolerance (Tier 2), so reviewers know exactly what to expect.",
         "Not every correct calculation is bit-for-bit repeatable. Kronos states, per result, which standard applies.",
         [('p',"Deterministic, integer-and-float-stable calculations are graded Tier&nbsp;1: on a matching software environment they reproduce byte-for-byte. Calculations that involve legitimate sources of numerical variation — iterative solvers, sampling, platform math differences — are graded Tier&nbsp;2 and reproduce within a declared tolerance."),
          ('p',"Grading each result this way is itself an honesty mechanism: it prevents a within-tolerance match from being over-sold as exact, and it tells a reviewer immediately whether a byte difference is a real discrepancy or expected noise."),
          ('gap',("Environment matters","Tier-1 reproduction assumes the pinned software environment in the deposit; the reproduction notes specify it."))],
         related=["reproducibility-overview","how-to-reproduce","validation-suite-breeder"],
         jtype="TechArticle")

    page("validation-suite-breeder","The Breeder Validation Suite","validation",
         f"HYPERION's design point is checked by a suite of {F['b_checks']} validation tests spanning power balance, current drive, confinement, stability and the fuel cycle.",
         f"The breeder's {F['b_checks']}-check suite is the audit trail behind Q = {F['b_Q']}.",
         [('p',f"The HYPERION deposit ships a validation suite of {F['b_checks']} checks that exercise the design point end to end — the power balance that yields Q = {F['b_Q']} and {F['b_Pfus']}, the {F['b_Ip']} current split into bootstrap and driven components, the confinement assumption H<sub>98</sub> = {F['b_H98']}, the stability margins, and the tritium fuel cycle at breeding ratio {F['b_TBR']}."),
          ('p',"Each check states its inputs, its method, and its expected output, and reproduces on the deposited engine. The suite is what turns a headline number into a checkable claim."),
          ('facts',[("Checks",F["b_checks"]),("Design gain",F["b_Q"]),("Fusion power",F["b_Pfus"]),
                    ("Deposit","DOI "+F["doi_b"]+" (v2 "+F["doi_b2"]+")")]),
          ('gap',("Named gates","The suite confirms internal consistency; the design's open gates — confinement quality and divertor radiated fraction — are stated separately and honestly."))],
         related=["reproducibility-overview","tier-1-tier-2","validation-suite-burner","the-breeder-design-point"],
         jtype="TechArticle")

    page("validation-suite-burner","The Burner Validation Suite","validation",
         f"The D–&sup3;He burner's closure is checked by {F['u_checks']} validation tests covering the fuel trajectory, power ledger, and the plug-density requirement.",
         f"The burner's {F['u_checks']}-check suite is honest about the one thing that gates it.",
         [('p',f"The burner deposit ships {F['u_checks']} checks (H41–H80) that exercise the D–&sup3;He operating point — the fuel trajectory, the power ledger that yields Q<sub>E</sub> = {F['u_QE']} with neutron fraction {F['u_fn']}, and the closure conditions across the three product housings."),
          ('p',f"Crucially, the suite carries the design's central caveat rather than hiding it: net-positive operation is <b>requirement-class</b>, contingent on a plug-to-central density ratio near {F['u_np']}. At a lower ratio the machine does not close, and the suite says so."),
          ('facts',[("Checks",F["u_checks"]),("Engineering gain",F["u_QE"]),("Neutron fraction",F["u_fn"]),
                    ("Plug-density requirement","n_p/n_c &asymp; "+F["u_np"]),("Deposit","DOI "+F["doi_u"])]),
          ('gap',("Requirement, not result",f"The burner's net power depends on reaching the plug-density requirement. Until a plug demonstration achieves it, closure is a target the suite defines, not an outcome it measures."))],
         related=["plug-density-requirement","validation-suite-breeder","reproducibility-overview","the-burner-design-point"],
         jtype="TechArticle")

    page("how-to-reproduce","How to Reproduce a Kronos Result","validation",
         "A step-by-step of how an independent reviewer downloads a Kronos deposit and re-runs it to the published numbers.",
         "The whole point of an open deposit is that you do not have to believe us. Here is how to check.",
         [('ol',["Download the relevant Zenodo deposit (breeder, burner, REBCO, DEC, or AI/quantum).",
                 "Set up the pinned software environment described in the deposit's reproduction notes.",
                 "Run the deposited engine against the provided input decks.",
                 "Compare against the expected outputs — byte-exact for Tier-1 results, within the stated tolerance for Tier-2.",
                 "Consult the validation suite to see each check's inputs, method and expected value."]),
          ('facts',[("Breeder","DOI "+F["doi_b"]),("Burner","DOI "+F["doi_u"]),("REBCO","DOI "+F["doi_rebco"]),
                    ("DEC","DOI "+F["doi_dec"]),("AI / Quantum","DOI "+F["doi_ai"])]),
          ('gap',("Licence","All deposits are CC BY 4.0 — free to download, re-run, and cite, with attribution."))],
         related=["reproducibility-overview","tier-1-tier-2","the-open-deposits"],
         jtype="TechArticle")
