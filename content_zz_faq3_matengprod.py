# -*- coding: utf-8 -*-
"""FAQ coverage batch 3 — Materials & Magnets, Engineering & Subsystems, Products."""
def register(cat, page, F, enrich):
    Q = {
     # --- Materials & Magnets ---
     "plasma-facing-materials": [
       ("What are plasma-facing materials chosen for?",
        f"<p>Heat tolerance, low erosion and low tritium retention rather than strength. Tungsten armour on copper-alloy heat sinks is the reference pairing, rated for HYPERION's {F['b_wall']} first-wall load.</p>"),
       ("Are they permanent?",
        "<p>No — plasma-facing components are consumables designed to be inspected and replaced remotely, because they live in the harshest environment in the machine.</p>")],
     "tungsten-armor": [
       ("Why tungsten for the plasma-facing armour?",
        "<p>It has the highest melting point of any metal, low erosion and low fuel retention, which is why it is the international reference armour for the highest-heat-flux surfaces.</p>"),
       ("What is tungsten's drawback?",
        "<p>It is brittle and, as a high-Z metal, radiates strongly if it reaches the core — so it is used as a thin armour on a tougher heat sink and kept out of the confined plasma.</p>")],
     "copper-alloys": [
       ("Why copper alloys under the armour?",
        "<p>Precipitation-strengthened copper alloys combine high thermal conductivity with useful strength, so they pull heat out of the plasma-facing armour fast enough to survive the flux. They are the heat-sink material beneath the tungsten.</p>"),
       ("What limits them?",
        "<p>Neutron irradiation degrades copper's conductivity and toughness, which is why the copper-alloy heat sinks sit in the replaceable first-wall and divertor components rather than in permanent structure.</p>")],
     "structural-alloys": [
       ("What are cryogenic structural alloys used for?",
        "<p>They form the magnet cases and cold structure that must stay strong and tough at liquid-helium temperatures while containing enormous Lorentz forces. Strength actually rises at cryogenic temperature, which helps.</p>"),
       ("Is fatigue the concern?",
        "<p>Yes — a single load is well within limits, but cyclic fatigue of the cold structure under repeated operation is part of the burner's named magnet gate.</p>")],
     "magnet-structure": [
       ("Why is a magnet fundamentally a structure problem?",
        "<p>The Lorentz forces try to blow the coil apart, and the winding pack alone cannot hold them, so a high-strength case and intercoil structure carry the hoop and overturning loads. The magnet is as much steel as superconductor.</p>"),
       ("Is the structure proven?",
        f"<p>Bore-resolved analysis shows the static case is sound with margin; cyclic fatigue is the binding open item, mapped in the open REBCO study (DOI {F['doi_rebco']}).</p>")],
     "neutron-damage-materials": [
       ("How do fusion neutrons damage materials?",
        f"<p>They displace atoms from the lattice (measured in dpa) and transmute them into gas and radioactive isotopes, degrading materials and setting component lifetimes. The neutron-rich breeder ({F['b_fn']}) carries almost all of this load.</p>"),
       ("How is the damage bounded?",
        "<p>By low-activation steels chosen so their decay products are short-lived, and by designing damaged components — first wall, blanket — to be replaceable rather than permanent.</p>")],
     "neutron-multiplier-materials": [
       ("What is a neutron multiplier for?",
        f"<p>Materials like beryllium or lead multiply neutrons in the blanket so that more than one tritium atom can be bred per fusion neutron, helping reach a breeding ratio above one (HYPERION targets {F['b_TBR']}).</p>"),
       ("Why is multiplication needed at all?",
        "<p>Because some neutrons are lost to structure and leakage, so bare lithium cannot quite breed enough tritium to sustain the fuel cycle without a multiplier.</p>")],
     "reflector-liner": [
       ("What is the burner's reflector liner?",
        "<p>A reflective inner surface that returns radiation to the plasma, improving the power balance that closes the machine. In the low-neutron burner it is a deciding component, not a detail.</p>"),
       ("What is the design tension?",
        "<p>Higher reflectivity helps the power balance, but the liner material also activates under residual neutrons. Kronos states that reflectivity-versus-activation trade explicitly rather than assuming an ideal reflector.</p>")],
     "quench-protection-detail": [
       ("How does quench protection work in practice?",
        "<p>Detect the resistive voltage as a coil goes normal, then switch its stored energy into a dump resistor before a hot spot forms. Detection is the harder half, because REBCO quenches propagate slowly.</p>"),
       ("Are these magnets self-protecting?",
        "<p>Kronos's adiabatic hot-spot analysis reports the magnet protecting itself within its design basis — but reliable, fast quench detection in REBCO is named as an engineering focus, not assumed solved.</p>")],
     # --- Engineering & Subsystems ---
     "heating-systems": [
       ("How is the plasma heated?",
        f"<p>By neutral beams and radio-frequency systems (ion- and electron-cyclotron), which also drive current. HYPERION's auxiliary heating budget is {F['b_Paux']}, and these systems are how a driven machine is steered.</p>"),
       ("Is heating technology mature?",
        "<p>Beams and RF launchers are demonstrated on today's machines; they are specialised, long-lead components rather than open research questions.</p>")],
     "power-conversion": [
       ("How does each machine convert its energy?",
        f"<p>The breeder recovers heat through a conventional thermal cycle; the burner recovers charged-particle energy directly at about {F['u_dec']}, skipping the Carnot-limited steam cycle. Conversion follows the fuel.</p>"),
       ("Why does direct conversion matter commercially?",
        f"<p>It lifts plant-level efficiency above a thermal plant's, underpinning the burner's Q<sub>E</sub> = {F['u_QE']}. Kronos reports net electricity after the plant's own draw, not gross.</p>")],
     "cryogenic-system": [
       ("What does the cryogenic system do?",
        "<p>A helium refrigerator removes the residual heat leaking into the cold magnets through supports, leads, radiation and nuclear heating, keeping the superconductor at operating temperature.</p>"),
       ("Is the cryoplant novel?",
        "<p>No — large helium refrigeration is mature big-science and industrial engineering, classed in Kronos's review as ready for detailed design.</p>")],
     "vacuum-system": [
       ("Why does the plasma need ultra-high vacuum?",
        "<p>So stray gas cannot cool or contaminate the plasma. Reaching a very low base pressure is a cold-commissioning milestone, and cryopumps provide the high pumping speeds to hold density and exhaust ash.</p>"),
       ("Does the vacuum system handle tritium?",
        "<p>On the breeder, yes — it manages the tritium-bearing exhaust, so vacuum and tritium handling are linked systems there.</p>")],
     "fuel-cycle": [
       ("What is the tritium fuel cycle?",
        f"<p>A closed loop unique to the D–T breeder: breed tritium in the blanket, extract and purify it, account for every gram, and re-inject it. HYPERION runs it at breeding ratio {F['b_TBR']} for ~{F['b_T']}/yr.</p>"),
       ("Why is the fuel cycle licensing-relevant?",
        "<p>Because tritium is mobile and radioactive, its inventory, containment and accounting are core safety systems — one reason the breeder carries most of Kronos's radiological engineering.</p>")],
     "heat-flux": [
       ("What is the heat-flux handling problem?",
        "<p>Concentrated exhaust power can exceed what any surface survives, so the divertor and first wall must be actively cooled and, where possible, shielded by radiating the power away before it lands.</p>"),
       ("What sets the limit?",
        "<p>Material and cooling limits on the plasma-facing components. Managing peak heat flux — largely by raising the radiated fraction — is one of HYPERION's named performance gates.</p>")],
     "the-central-cell": [
       ("What is the burner's central cell?",
        f"<p>The long, straight solenoid section where the D–&sup3;He plasma is confined and fusion happens. Its length sets the product: {F['u_ref_len']}, {F['u_aeg_len']} (AEGIS) or {F['u_mv_len']} (MetroVolt).</p>"),
       ("Why is length the main product variable?",
        f"<p>Because gain and neutron fraction are set by local plasma physics, not machine size, so extending the central cell scales net power while the physics per metre stays the same.</p>")],
     "the-end-cell": [
       ("What is the burner's end cell?",
        f"<p>The high-field plug and mirror-throat region at each end that confines the central plasma, plus the expander where escaping particles are spread out and their energy recovered. It is where the plug physics lives.</p>"),
       ("Why is the end cell critical?",
        f"<p>Because the ambipolar plug it creates is what holds the plasma in — and its effectiveness depends on the ~{F['u_np']} plug-density ratio, the burner's binding condition.</p>")],
     "heating-systems-x": [("x","x")],
     "instrumentation-control": [
       ("What does instrumentation, control and safety cover?",
        "<p>The sensors, real-time control system, machine-protection system and the independent safety-instrumented system — the layers that measure the plasma, hold it at its operating point and keep the plant safe.</p>"),
       ("Why keep safety separate from control?",
        "<p>So that the system protecting people and the environment is independent of the systems running and protecting the machine — standard safety-engineering practice applied to a fusion plant.</p>")],
     "assembly-sequence": [
       ("What does the assembly sequence describe?",
        "<p>The order in which the machine is built — foundations, cryostat, magnets, vessel, internals — respecting the long-lead items and the tolerances that later commissioning depends on.</p>"),
       ("Why does it matter for schedule?",
        "<p>Because long-lead forgings and magnets sit on the critical path; the breeder's build begins in Q2 2027, and the sequence is what keeps procurement and integration from colliding.</p>")],
     "balance-of-plant": [
       ("What is the balance of plant?",
        "<p>Everything beyond the fusion core — heat rejection, electrical distribution, power supplies, cooling and controls — much of it conventional power-plant and big-science engineering.</p>"),
       ("Is it a source of risk?",
        "<p>Largely not — Kronos's construction-readiness review classes most balance-of-plant as ready for detailed design, which separates the genuinely novel systems from the well-understood ones.</p>")],
     "interface-control": [
       ("What is interface control?",
        "<p>The discipline of managing the boundaries where subsystems meet — mechanical, electrical, thermal, vacuum — so that independently designed components actually fit and function together.</p>"),
       ("Why is it emphasised?",
        "<p>Because in a tightly packed machine most integration risk lives at the interfaces, not within components. Controlling them rigorously is how a frozen design stays buildable.</p>")],
     # --- Products & Applications ---
     "neutron-source-product": [
       ("What is the neutron-source product?",
        f"<p>The breeder sold for what its {F['b_Pn']} of neutron power can do — breeding tritium and helium-3 and producing medical and industrial isotopes — rather than for electricity.</p>"),
       ("Why lead with neutrons?",
        "<p>Because that value exists today, independent of grid-scale net-electric fusion. Reframing neutrons from a shielding burden into a product is the commercial heart of building the breeder first.</p>")],
     "firm-clean-power-product": [
       ("What is the firm clean power product?",
        f"<p>The burner sold as firm, dispatchable, carbon-free power for grids and large loads — up to {F['u_mv_net']} net in the MetroVolt housing — targeting the scarce commodity in a renewable-heavy grid.</p>"),
       ("How is it different from renewables?",
        "<p>It is firm and steerable rather than intermittent, complementing cheap renewables by covering the hardest, last part of decarbonisation instead of competing for the easy part.</p>")],
     "isotope-platform": [
       ("What is the isotope platform?",
        f"<p>The breeder's neutron flux used to co-produce valuable isotopes — tritium, helium-3 (~{F['b_He3']}/yr) and medical and industrial isotopes — as a portfolio of products from one neutron source.</p>"),
       ("Is helium-3 the revenue base?",
        "<p>No. Kronos treats helium-3's value as strategic rather than near-term revenue; the more clearly bankable base is tritium, which the breeder can supply steadily.</p>")],
     "neutron-source-product-x": [("x","x")],
     "can-fusion-power-a-data-center": [
       ("Can fusion power a data centre?",
        f"<p>That is exactly the burner's target — firm, clean, point-of-use power for hyperscale load. The MetroVolt housing is sized in the {F['u_mv_gw']} class, matching large data-centre demand.</p>"),
       ("Why is fusion attractive for data centres?",
        "<p>Because they need firm, round-the-clock power that renewables alone struggle to guarantee, and the burner's low neutron fraction could in principle allow siting nearer to load than a neutron-heavy plant.</p>")],
    }
    for slug, faq in Q.items():
        if faq and faq[0][0] != "x":
            enrich(slug, faq=faq)
