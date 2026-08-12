# -*- coding: utf-8 -*-
"""FAQ coverage batch 4 — Competitive, Innovations, Safety & Environment, Applications, Technology."""
def register(cat, page, F, enrich):
    Q = {
     # --- Competitive Landscape ---
     "the-competitive-landscape": [
       ("How does Kronos compare with other fusion companies?",
        "<p>Most of the field is racing toward net-electric power from a single machine. Kronos instead sells the breeder's neutrons and isotopes first, so its business does not wait on solving net-electric gain — a different wedge, not a faster horse.</p>"),
       ("Are the comparisons fair to competitors?",
        "<p>Every comparison Kronos publishes is drawn from public sources and is non-disparaging — the aim is to place its own strategy honestly, on the same ruler, not to attack anyone.</p>")],
     "tokamak-approach": [
       ("What is the tokamak approach?",
        f"<p>A toroidal magnetic bottle where a plasma current helps confine the plasma — the most developed fusion concept. Kronos's breeder is a compact, spherical tokamak at Q = {F['b_Q']}.</p>"),
       ("What is the tokamak's main drawback?",
        "<p>The plasma current can disrupt, dumping energy and forces suddenly. Kronos manages that in the breeder and sidesteps it entirely in the linear burner, which has no plasma current.</p>")],
     "the-public-programmes": [
       ("How does Kronos relate to public programmes like ITER?",
        "<p>Public programmes prove the physics at large scale and generate the database Kronos designs to. Kronos aims to commercialise focused products quickly, complementing rather than duplicating that public science.</p>"),
       ("Does Kronos depend on ITER succeeding?",
        f"<p>No. Its designs use standard confinement scaling (H<sub>98</sub> = {F['b_H98']}) already in today's database, so the breeder's case does not hinge on any single future experiment.</p>")],
     "stellarator-approach": [
       ("What is the stellarator approach?",
        "<p>A toroidal machine that uses intricately shaped external coils, instead of a plasma current, to twist the field — which avoids disruptions at the cost of very complex magnets.</p>"),
       ("Why doesn't Kronos use one?",
        "<p>Kronos gets disruption-free operation from its linear burner and compactness from its spherical breeder, without the stellarator's coil-manufacturing complexity — a different route to similar advantages.</p>")],
     "inertial-approach": [
       ("What is inertial confinement?",
        "<p>Instead of holding a diffuse plasma steadily, it compresses a tiny fuel pellet so fast that it fuses before flying apart — the approach NIF used for its 2022 target gain.</p>"),
       ("Why does Kronos use magnetic confinement instead?",
        "<p>Because driver efficiency and repetition rate make inertial fusion a very different power-plant problem. Kronos's continuous magnetic machines produce steady output, which suits firm power and isotope production.</p>")],
     "mirror-approach": [
       ("What is the magnetic-mirror approach?",
        f"<p>A straight, open-ended magnetic bottle stronger at its ends. Kronos's burner is a tandem mirror, gaining a disruption-free machine that converts energy directly and scales by length.</p>"),
       ("Didn't mirrors fail decades ago?",
        f"<p>Simple mirrors leaked, but the physics fixes (tandem plugs, thermal barriers) were understood; what was missing were magnets strong enough. Modern REBCO reaching {F['u_Bplug']} is what makes the concept viable now.</p>")],
     "neutron-heavy-vs-low-neutron": [
       ("What is the difference between neutron-heavy and low-neutron machines?",
        f"<p>Neutron-heavy D–T machines like the breeder ({F['b_fn']}) put most energy into neutrons — ideal for breeding and isotopes. Low-neutron D–&sup3;He machines like the burner ({F['u_fn']}) put it into charged particles — ideal for direct conversion and cleaner siting.</p>"),
       ("Which does Kronos use?",
        "<p>Both, deliberately — one for each product. The breeder sells neutrons; the burner sells firm power. Fuel follows purpose rather than one fuel being forced to do every job.</p>")],
     "dt-vs-advanced-fuels": [
       ("Is D–T or an advanced fuel better?",
        f"<p>D–T is easiest but neutron-heavy; advanced fuels like D–&sup3;He are cleaner but far harder and need scarce helium-3. Kronos uses each where it wins: D–T to breed, D–&sup3;He to burn.</p>"),
       ("Are 'aneutronic' fuel claims trustworthy?",
        f"<p>Be careful with them — even D–&sup3;He produces some neutrons via side reactions ({F['u_fn']} in the burner). Kronos never calls its burner aneutronic, only low-neutron.</p>")],
     # --- Innovations & Distinctives ---
     "innovation-neutron-economy": [
       ("What is the neutron-economy idea?",
        f"<p>Reframing the breeder's {F['b_Pn']} of neutron power from a shielding burden into a product line — tritium, helium-3 and isotopes. It is the innovation that lets fusion earn before net-electric power is solved.</p>"),
       ("Why is that a competitive advantage?",
        "<p>Because it decouples revenue from the hardest unsolved problem in fusion. Kronos can build a business on neutrons today while the field races toward grid electricity.</p>")],
     "innovation-low-neutron-burner": [
       ("What makes the low-neutron burner distinctive?",
        f"<p>It runs D–&sup3;He in a linear tandem mirror, so it is disruption-free, converts energy directly at ~{F['u_dec']}, and scales by length into three product housings from one physics core.</p>"),
       ("What is the honest caveat?",
        f"<p>Its net power is requirement-class: it depends on the plug reaching a density ratio near {F['u_np']}. Kronos labels it as such rather than quoting net power unconditionally.</p>")],
     "innovation-high-field-compact": [
       ("Why is the high-field compact core an innovation?",
        f"<p>Machine size and cost fall steeply as magnetic field rises, and REBCO high-temperature superconductors let the breeder reach {F['b_Bpeak']} at the conductor — a small machine doing a large machine's job.</p>"),
       ("What is the trade?",
        "<p>Higher field means larger forces and tighter fatigue margins on the magnets — which is exactly why the magnet's cyclic fatigue is named as a binding gate.</p>")],
     "innovation-negative-triangularity": [
       ("What does negative triangularity buy?",
        f"<p>HYPERION's negative-triangularity shape (&delta; = {F['b_delta']}) can suppress edge-localised modes while keeping good confinement — taming the plasma edge without violent bursts, a deliberate stability choice.</p>"),
       ("Is it unproven?",
        "<p>Negative triangularity is an active, promising area demonstrated on several tokamaks. Kronos adopts it as a design choice grounded in that experimental work, not as a novel bet.</p>")],
     "innovation-modular-housings": [
       ("What are the modular product housings?",
        f"<p>One burner physics core packaged at three lengths — {F['u_ref_len']}, {F['u_aeg_len']} (AEGIS) and {F['u_mv_len']} (MetroVolt) — to hit different power classes without redesigning the physics.</p>"),
       ("Why does this help commercialisation?",
        "<p>Because gain and neutron fraction are length-independent, so one qualified design serves several markets, spreading engineering effort across products instead of starting over each time.</p>")],
     "innovation-isotope-platform": [
       ("What is the isotope and helium-3 platform?",
        f"<p>The breeder's neutron flux used to co-produce tritium, helium-3 (~{F['b_He3']}/yr) and medical and industrial isotopes — a portfolio of high-value products from one neutron source.</p>"),
       ("Is helium-3 the money-maker?",
        "<p>Kronos frames helium-3's value as strategic, not near-term revenue. The bankable base is tritium; helium-3 is a strategic position in a genuinely scarce material.</p>")],
     "innovation-frozen-design": [
       ("What is the frozen-design discipline?",
        "<p>The design point is fixed as a single frozen set of numbers (the canon), so nothing quietly drifts and every published figure traces to one source of truth. It is a discipline, not a marketing claim.</p>"),
       ("Why freeze the design?",
        "<p>Because a frozen, internally consistent point can be checked, reproduced and built against. It is what makes the open deposits meaningful — reviewers check the same numbers Kronos designs to.</p>")],
     "innovation-open-record": [
       ("What is radical reproducibility?",
        f"<p>Publishing the actual engines, inputs and expected outputs as open Zenodo deposits under CC BY 4.0, so anyone can re-run Kronos's calculations rather than trust its conclusions.</p>"),
       ("Why make it a strategy?",
        "<p>Because in a field prone to hype, letting skeptics reproduce your numbers is a durable form of credibility — a moat built from openness rather than secrecy.</p>")],
     "innovation-honesty-framework": [
       ("How is honesty a moat?",
        "<p>By stating gates, caveats and open items plainly — low-neutron not aneutronic, requirement-class net power, not-yet-built — Kronos builds trust that overclaiming competitors erode. Credibility compounds; hype decays.</p>"),
       ("Does that mean the design is weak?",
        f"<p>No — it means the strong parts are believable. HYPERION's Q = {F['b_Q']} and the open deposits stand precisely because Kronos is candid about what is not yet demonstrated.</p>")],
     # --- Safety & Environment ---
     "radiation-protection": [
       ("What are the radiation hazards at a fusion plant?",
        "<p>Mainly neutrons during operation and activated structure afterwards, concentrated in the breeder. There is no chain reaction and no spent fuel; the hazards are handled by conventional shielding and access control.</p>"),
       ("Is the burner different?",
        f"<p>Yes — being low-neutron ({F['u_fn']}), it produces far less activation than the breeder, which is one reason it could in principle be sited closer to where its power is used.</p>")],
     "fusion-waste": [("x","x")],
     "decommissioning": [
       ("What is left to decommission at a fusion plant?",
        "<p>Structural metal made mildly radioactive by neutrons — no spent fuel and no long-lived high-level waste. Low-activation materials are chosen so that much of it decays to hands-on levels within decades.</p>"),
       ("How does that compare with fission?",
        "<p>There is no fissile inventory and no long-lived high-level waste stream, so the decommissioning problem is bounded and shorter-lived — though Kronos still screens waste class and volume per component rather than assuming it away.</p>")],
     "radiation-protection-x": [("x","x")],
     "can-fusion-be-used-for-weapons": [
       ("Can a fusion plant make weapons material?",
        "<p>It produces no plutonium and needs no enriched uranium, so fission's proliferation route does not exist. Its fuels are hydrogen isotopes and helium-3.</p>"),
       ("Are there any proliferation-relevant aspects?",
        "<p>A high neutron flux and tritium handling are safeguards-and-siting considerations managed by design and oversight — which Kronos treats as real responsibilities rather than dismissing.</p>")],
     "fusion-carbon-footprint": [
       ("Does fusion emit carbon?",
        "<p>Not in operation — the reaction produces helium, not carbon dioxide. The footprint is in construction materials (steel, concrete, magnets), like any large clean-energy plant.</p>"),
       ("How does it compare with other clean sources?",
        "<p>Its lifecycle emissions are dominated by one-time construction, spread over decades of firm output — in the same low range as other low-carbon generation, which Kronos assesses rather than asserts.</p>")],
     "lifecycle-assessment": [
       ("What does a lifecycle assessment cover?",
        "<p>All the environmental inputs and outputs across a plant's life — construction materials, water and land use, operation and decommissioning — not just what comes out of the stack during operation.</p>"),
       ("Has Kronos finished one?",
        "<p>Kronos screens lifecycle impacts by product and flags what remains to be computed rather than publishing a finished, polished number it cannot yet defend.</p>")],
     "water-use": [
       ("Does fusion use a lot of water?",
        "<p>The breeder rejects heat through a thermal cycle, so it has cooling-water needs like other thermal plants; the burner's direct conversion reduces that heat-rejection load. Kronos screens water use per product.</p>"),
       ("Can it be sited in dry regions?",
        "<p>Cooling method (wet, dry or hybrid) is a siting choice that trades water against efficiency and cost — the same engineering trade any thermal plant faces, assessed per deployment.</p>")],
     "land-use": [
       ("How much land does a fusion plant need?",
        "<p>Very little for its energy output — the power density is high, so a plant's footprint is small compared with the equivalent capacity of intermittent renewables plus storage.</p>"),
       ("Why does compact land use matter?",
        "<p>Because firm power at a small footprint suits point-of-use siting near cities, industry and data centres, where land is scarce and transmission is costly.</p>")],
     # --- Applications & Markets ---
     "fusion-for-industry": [
       ("How can fusion serve industry?",
        "<p>By providing firm, clean power and high-grade heat for processes that are hard to electrify or decarbonise — exactly the demand renewables struggle to cover reliably.</p>"),
       ("Which Kronos product fits industry?",
        f"<p>The burner, sold as firm dispatchable power (up to {F['u_mv_net']} net in MetroVolt), and the breeder's process heat and isotopes for industrial users.</p>")],
     "industrial-heat-hydrogen": [
       ("Can fusion make industrial heat and hydrogen?",
        "<p>Yes — its high-grade heat can drive industrial processes and efficient (including high-temperature) hydrogen production, reaching emissions that electrification alone cannot.</p>"),
       ("Is this a near-term product?",
        "<p>It is an application of the same firm-power and heat output, framed as a market direction rather than a separate near-term product line.</p>")],
     "helium-3-for-quantum": [
       ("Why is helium-3 valuable for quantum and medicine?",
        "<p>It is essential for the dilution refrigerators that cool quantum computers, for neutron detection, and for certain medical imaging — a genuinely scarce isotope with no easy substitute.</p>"),
       ("How does Kronos supply it?",
        f"<p>The breeder co-produces about {F['b_He3']}/yr as part of its neutron economy, giving a terrestrial source. Kronos frames this as strategic value rather than near-term revenue.</p>")],
     "desalination-context": [
       ("Can fusion power desalination?",
        "<p>Yes — its firm power and waste heat suit large-scale desalination, which needs steady, round-the-clock energy. It is an application of the burner's firm output, not a bespoke machine.</p>"),
       ("Is this a Kronos product?",
        "<p>It is a market context for firm fusion power, illustrating where reliable clean energy and heat are valuable — not a separate product line.</p>")],
     "space-power-context": [
       ("Is fusion relevant to space power?",
        "<p>Its high energy density and helium-3 link make it a long-horizon topic for space, and lunar helium-3 is part of the wider strategic picture. Kronos's products, though, are firmly terrestrial.</p>"),
       ("Does Kronos build space reactors?",
        "<p>No. Space power is discussed as strategic context — especially around helium-3 — not as a current Kronos product.</p>")],
     # --- The Technology Stack ---
     "hts-magnet-technology": [
       ("What is HTS magnet technology?",
        f"<p>Magnets wound from REBCO high-temperature superconductor, which carries current and field that older superconductors cannot — enabling the breeder's {F['b_Bpeak']} and the burner's {F['u_Bplug']} fields.</p>"),
       ("What is the open engineering item?",
        f"<p>Cyclic fatigue of the high-field magnet structure, and reliable quench detection in REBCO — both mapped in Kronos's open magnet study (DOI {F['doi_rebco']}).</p>")],
     "plasma-technology": [
       ("What does the plasma technology stack include?",
        f"<p>Heating and current drive (beams and RF, {F['b_Paux']} in the breeder), real-time control, fuelling and exhaust — the systems that create, hold and steer the plasma.</p>"),
       ("Is any of it novel physics?",
        "<p>The individual technologies are demonstrated on today's machines; the work is integrating them to the frozen design, not inventing new plasma tools.</p>")],
     "fuel-cycle-technology": [
       ("What is fuel-cycle technology?",
        f"<p>The systems that breed, extract, purify, account for and re-inject tritium in the breeder — a closed loop running at breeding ratio {F['b_TBR']}. It is unique to the D–T machine.</p>"),
       ("Why is it singled out?",
        "<p>Because tritium is the breeder's one genuinely radioactive material, its handling is both a product enabler and a licensing-relevant safety system.</p>")],
     "materials-technology": [
       ("What does the materials technology stack cover?",
        f"<p>Plasma-facing armour (tungsten on copper alloys), low-activation structural steels, and the neutron-damage engineering that sets component lifetimes under the breeder's {F['b_wall']} load.</p>"),
       ("What is the hardest materials problem?",
        "<p>Surviving neutron damage over life while keeping activation short-lived — handled by material choice and by making the most-loaded components replaceable.</p>")],
     "manufacturing-technology": [
       ("What is in the manufacturing and assembly stack?",
        "<p>Coil winding, large-forging fabrication, automated welding of vessel sectors, and the assembly sequence — much of it drawn from established heavy-industry and big-science practice.</p>"),
       ("Is manufacturing a bottleneck?",
        "<p>Long-lead items like sector forgings and magnets drive the schedule, which is why the breeder's build sequence and procurement start early, ahead of the Q2 2027 construction start.</p>")],
     "the-ai-ml-stack": [
       ("What is the AI and ML stack used for?",
        f"<p>To accelerate design scans, surrogate modelling and analysis of the frozen design. Its methods and records are published openly (DOI {F['doi_ai']}) alongside the physics deposits.</p>"),
       ("Does AI replace the physics engines?",
        "<p>No — it augments them. The design point rests on transparent, reproducible physics engines; AI speeds exploration and cross-checks rather than substituting for the underlying calculation.</p>")],
     "the-live-simulator": [
       ("What is the live in-browser simulator?",
        "<p>A public tool that runs Kronos's reduced-order physics engines directly in the browser, so anyone can change inputs and see the design point respond — reproducibility you can click.</p>"),
       ("Are its numbers the same as the papers?",
        "<p>Yes — it runs the same frozen-canon engines that back the deposits, so the simulator and the published figures agree by construction.</p>")],
     "the-digital-model-technology": [
       ("What is the interactive 3D model?",
        "<p>A public, explorable 3D representation of the machine where components can be inspected with real design context — the geometry side of Kronos's open record.</p>"),
       ("Is the full engineering model public?",
        "<p>No. A public build shows the machine and headline blueprint sheets; the detailed CAD and full sheet set are kept in a private, access-controlled build.</p>")],
    }
    for slug, faq in Q.items():
        if faq and faq[0][0] != "x":
            enrich(slug, faq=faq)
