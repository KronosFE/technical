# -*- coding: utf-8 -*-
"""Products & applications."""

def register(cat, page, F):
    cat("products", "Products & Applications",
        "One physics core, several products: the breeder's isotopes and neutrons, and the "
        "burner as MetroVolt and AEGIS across grid, data-centre, defence and space applications.", 6)

    page("the-breeder-first-strategy","The Breeder-First Strategy","products",
         "Kronos builds the neutron-and-tritium machine first because it has a product to sell before net electricity is proven — a fundamentally different commercial path.",
         "Most fusion companies must reach net electricity before they have anything to sell. Kronos does not — and that changes everything about the risk.",
         [('p',"The breeder's outputs — tritium, neutrons and helium-3 — are valuable in themselves, independent of whether grid-scale net-electric fusion is solved. That gives Kronos a materials-and-isotopes business that does not wait on the hardest physics milestone in the field."),
          ('p',"'Fuel follows purpose, not platform': the breeder is optimised to make fuel and neutrons; the burner is optimised to make electricity. Building the breeder first de-risks the whole programme."),
          ('gap',("The honest wedge","Kronos sells materials, not (yet) electricity — so its economics do not depend on first achieving net-electric gain. That is the crux of the strategy."))],
         related=["hyperion-breeder","the-neutron-economy","helium-3-supply","fusion-fuels-overview"],
         jtype="TechArticle")

    prods = [
     ("hyperion-breeder","HYPERION — The Breeder","The neutron-and-tritium machine at the base of the Kronos architecture.",
      [f"HYPERION is a compact spherical tokamak (Q = {F['b_Q']}, {F['b_Pfus']}) whose product is neutrons, tritium and helium-3 rather than grid electricity. It breeds {F['b_T']} of tritium at a breeding ratio of {F['b_TBR']} and co-produces helium-3 to feed the burner.",
       "As a neutron source and isotope producer, HYPERION has commercial value that does not depend on solving net-electric fusion first."],
      [("Type","D–T spherical tokamak"),("Product","Neutrons, tritium, He-3"),("Gain",F["b_Q"])],
      ["spherical-tokamak","the-breeder-first-strategy","the-neutron-economy"]),
     ("metrovolt","MetroVolt — Grid & Data-Centre Power","The largest burner housing, sized for utility- and data-centre-scale power.",
      [f"MetroVolt is the {F['u_mv_len']} burner housing, the largest of the three, delivering {F['u_mv_net']} net ({F['u_mv_gw']} class) from the same D–&sup3;He physics. It targets grid-scale and hyperscale data-centre power where firm, clean, point-of-use generation is valuable.",
       f"Because the burner is low-neutron ({F['u_fn']}) and directly converts to electricity, it can in principle site closer to load than a neutron-heavy plant."],
      [("Housing length",F["u_mv_len"]),("Net power",F["u_mv_net"]),("Class",F["u_mv_gw"])],
      ["tandem-mirror","can-fusion-power-a-data-center","the-burner-design-point"]),
     ("aegis","AEGIS — Defence Installations","The mid-scale burner housing for fixed defence installations.",
      [f"AEGIS is the {F['u_aeg_len']} burner housing, delivering {F['u_aeg_net']} net ({F['u_aeg_gw']} class), aimed at fixed defence installations that need resilient, independent, low-signature power. It is a fixed installation product, not a mobile or naval one.",
       "The burner's lack of disruptions and its direct conversion suit a resilience-focused deployment."],
      [("Housing length",F["u_aeg_len"]),("Net power",F["u_aeg_net"]),("Use","Fixed defence installations")],
      ["tandem-mirror","the-burner-design-point","metrovolt"]),
     ("the-neutron-economy","The Neutron Economy","How the breeder's neutrons create value — tritium, isotopes, and more.",
      [f"The breeder's {F['b_Pn']} of neutron power is not waste — it is the product. Neutrons breed tritium, can produce medical and industrial isotopes, and drive the helium-3 supply the burner needs. This 'neutron economy' is what makes the breeder a business before the burner reaches net electricity.",
       "Kronos treats neutron management as value capture, not just a shielding problem."],
      [("Neutron power (breeder)",F["b_Pn"]),("Uses","Tritium, isotopes, He-3")],
      ["the-breeder-first-strategy","helium-3-supply","tritium-breeding"]),
     ("helium-3-supply","The Helium-3 Supply Story","Why helium-3 is strategically valuable, and how the breeder produces it.",
      [f"Helium-3 is scarce and strategically valuable — for the burner's fuel, and for quantum and medical uses. The breeder co-produces about {F['b_He3']} as part of its fuel cycle, giving Kronos an internal supply path rather than depending on external markets.",
       "Kronos is careful to frame helium-3's strategic value as distinct from near-term revenue; the bankable base is tritium."],
      [("Breeder He-3 output",F["b_He3"]),("Uses","Burner fuel, quantum, medical")],
      ["the-neutron-economy","d-he3-fuel","the-breeder-first-strategy"]),
     ("isotope-platform","The Isotope Platform","Beyond fuel: the breeder as a source of medical and industrial isotopes.",
      ["A high-flux neutron source can produce isotopes used in medicine, industry and research. The breeder's neutron economy positions Kronos as a potential isotope supplier — another revenue path that does not wait on net-electric fusion.",
       "This is framed as an optionality on the breeder's core neutron output, grounded in its neutron power rather than speculative markets."],
      [("Basis","High-flux neutron source"),("Outputs","Medical / industrial isotopes")],
      ["the-neutron-economy","helium-3-supply","hyperion-breeder"]),
    ]
    for slug,title,desc,paras,facts,rel in prods:
        page(slug,title,"products",desc,desc,[('p',p) for p in paras],facts=facts,related=rel,jtype="TechArticle")
