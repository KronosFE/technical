# -*- coding: utf-8 -*-
"""Open science, publications, deposits, IP."""

def register(cat, page, F):
    cat("openscience", "Open Science & Publications",
        "The open record behind Kronos — five Zenodo deposits, the peer-review track, how to "
        "cite the work, and the granted and pending patents.", 7)

    page("the-open-deposits","The Five Open Deposits","openscience",
         "Kronos deposits its physics openly on Zenodo under CC BY 4.0: breeder, burner, REBCO magnets, direct energy conversion, and the AI/quantum record.",
         "The Kronos design record is not a brochure — it is five downloadable deposits anyone can re-run.",
         [('p',"Kronos publishes its reduced-order engines, inputs and expected outputs as open Zenodo deposits, licensed CC&nbsp;BY&nbsp;4.0. Each is independently reproducible and citable."),
          ('facts',[("Breeder — HYPERION","DOI "+F["doi_b"]+" (v2 "+F["doi_b2"]+")"),
                    ("Burner — D–&sup3;He tandem mirror","DOI "+F["doi_u"]),
                    ("REBCO magnets & tape","DOI "+F["doi_rebco"]),
                    ("Direct energy conversion","DOI "+F["doi_dec"]),
                    ("AI + ML + quantum","DOI "+F["doi_ai"])]),
          ('gap',("Open by design","Publishing the engines, not just the conclusions, is what lets a reviewer check Kronos rather than trust it."))],
         related=["how-to-cite","how-to-reproduce","reproducibility-overview","peer-review-track"],
         jtype="TechArticle")

    page("how-to-cite","How to Cite Kronos","openscience",
         "The correct DOIs and attribution for citing the Kronos deposits in academic or technical work.",
         "The deposits are CC BY 4.0 — cite them freely, with attribution.",
         [('p',"Each Kronos deposit carries a persistent DOI. Cite the specific deposit relevant to your claim, with attribution to Kronos Fusion Energy, under CC&nbsp;BY&nbsp;4.0."),
          ('facts',[("Breeder",F["doi_b"]),("Breeder v2",F["doi_b2"]),("Burner",F["doi_u"]),
                    ("REBCO",F["doi_rebco"]),("DEC",F["doi_dec"]),("AI/Quantum",F["doi_ai"])]),
          ('gap',("One retired identifier","An earlier reserved DOI was never published and should not be cited; only the identifiers above are live."))],
         related=["the-open-deposits","how-to-reproduce","peer-review-track"],
         jtype="TechArticle")

    page("peer-review-track","The Peer-Review Track","openscience",
         "Open deposits are the first step; Kronos is pursuing the conventional peer-review path in parallel through arXiv and journal or IAEA venues.",
         "Reproducibility and peer review are complementary. Kronos pursues both.",
         [('p',"The open deposits let anyone reproduce the numbers today. In parallel, Kronos is preparing the conventional peer-review path — preprints and journal or IAEA submissions — so the work is scrutinised through both mechanisms."),
          ('gap',("Status","Peer-review submissions are in preparation; status updates are published as they progress, and the deposits remain the reproducible record in the meantime."))],
         related=["the-open-deposits","reproducibility-overview","how-to-cite"],
         jtype="TechArticle")

    page("intellectual-property","Intellectual Property","openscience",
         f"Kronos separates open science from proprietary implementation: the design record is open, while the build IP is protected — one patent granted ({F['patent_granted']}) and more pending.",
         "Open where it builds trust, protected where it builds a company. Kronos is deliberate about the line.",
         [('p',f"The Kronos model is to publish the physics openly — so it can be checked — while protecting the proprietary engineering that turns a design into a manufacturable machine. Kronos holds a granted patent, {F['patent_granted']}, with additional applications pending ({F['patent_pending']})."),
          ('p',"The genuinely proprietary build detail lives in the patent filings, not in the open deposits or the public engineering drawings — which are representative, not fabrication-grade."),
          ('gap',("The boundary","Open: the reproducible physics record. Protected: the build implementation. The two are kept cleanly separate."))],
         facts=[("Granted",F["patent_granted"]),("Pending",F["patent_pending"])],
         related=["the-open-deposits","the-path-to-build","reproducibility-overview"],
         jtype="TechArticle")
