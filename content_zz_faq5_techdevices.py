# -*- coding: utf-8 -*-
"""FAQ coverage batch 5 — Technical deep-dives and Reference Devices."""
def register(cat, page, F, enrich):
    Q = {
     # --- Technical ---
     "reduced-order-modeling": [
       ("What is a reduced-order model?",
        "<p>A fast, transparent, physics-based calculator that captures the essential balances of a system without the cost of full simulation. Kronos's deposited engines are reduced-order models.</p>"),
       ("When is a reduced-order model not enough?",
        "<p>Where a claim needs full structural FEA, thermal-hydraulic CFD or Monte-Carlo neutronics. Kronos names those as detailed-design work rather than presenting scoping estimates as high-fidelity results.</p>")],
     "high-fidelity-analysis": [
       ("What is high-fidelity analysis?",
        "<p>The detailed-design work beyond the scoping engines — full FEA for structure and fatigue, CFD for cooling, and MCNP-class neutronics — that replaces estimates with engineered results.</p>"),
       ("Has Kronos completed it?",
        "<p>No — it is placed on the path to build as scheduled work. The honest distinction between a design study and an engineered machine is exactly this analysis.</p>")],
     "charged-particle-heating": [
       ("What is charged-particle self-heating?",
        "<p>Confined fusion products (like the D–T helium nucleus) deposit their energy back into the plasma, helping sustain its temperature. Strong self-heating is what makes ignition possible.</p>"),
       ("Do Kronos machines rely on it?",
        "<p>Not dominantly — both are driven designs whose power tracks the external heating, a deliberately conservative posture that keeps them controllable rather than depending on self-heating running away.</p>")],
     "plasma-wall-interaction": [
       ("What is plasma–wall interaction?",
        "<p>The exchange of particles and heat between the plasma edge and the wall — erosion, redeposition, fuel retention and recycling — which governs wall lifetime and plasma purity.</p>"),
       ("Why does it matter for the design?",
        "<p>Because it sets how long plasma-facing components last and how clean the core stays, driving the choice of tungsten armour and the divertor's radiated-fraction strategy.</p>")],
     "systems-integration": [
       ("What does systems integration mean here?",
        "<p>Making dozens of subsystems — magnets, vessel, heating, cryogenics, fuel cycle, controls — fit and function together within a compact machine, where most risk lives at the interfaces.</p>"),
       ("Why is it emphasised for a compact machine?",
        "<p>Because space is scarce and everything competes for the central column, integration is a first-order design driver, not an afterthought.</p>")],
     "staged-commercialization": [
       ("What is Kronos's staged-commercialisation idea?",
        "<p>Earn from the breeder's neutrons and isotopes first, then firm power from the burner — so revenue starts before net-electric fusion is solved, funding the harder later stages.</p>"),
       ("How is it gated?",
        "<p>Through evidence-based go/no-go gates — physics freeze (done), component demonstration, integrated prototype, first product — each with explicit criteria rather than fixed promises.</p>")],
     "the-product-family": [
       ("What is the Kronos product family?",
        f"<p>The breeder (HYPERION) for neutrons, tritium and isotopes, and the burner in two housings — AEGIS ({F['u_aeg_net']}) and MetroVolt ({F['u_mv_net']}) — for firm power. Two machines, distinct jobs.</p>"),
       ("Why not one machine for everything?",
        "<p>Because fuel follows purpose: neutron-rich D–T to make fuel, low-neutron D–&sup3;He to make firm power. Matching each machine to what it sells is the core of the strategy.</p>")],
     "the-magnet-system": [("x","x")],
     "magnet-system": [
       ("What makes up the magnet system?",
        f"<p>REBCO high-temperature-superconducting coils, their structural cases, current leads, joints, cryogenics and quench protection — reaching {F['b_Bpeak']} in the breeder and {F['u_Bplug']} in the burner plug.</p>"),
       ("What is its binding open item?",
        f"<p>Cyclic fatigue of the high-field structure, mapped in the open REBCO study (DOI {F['doi_rebco']}) and closed by a powered test coil cycled at full field.</p>")],
     "winding-pack": [
       ("What is the winding pack?",
        "<p>The bundle of superconducting tape, insulation and cooling that actually carries a coil's current. It sits inside a structural case that contains the forces it cannot hold alone.</p>"),
       ("Why is it studied so closely?",
        f"<p>Because current density, joints, insulation and quench behaviour all live in the winding pack — the details that decide whether a high-field REBCO coil is buildable (DOI {F['doi_rebco']}).</p>")],
     "radial-build": [
       ("What is the radial build?",
        "<p>The sequence of layers from plasma outward — first wall, blanket, shield, vacuum vessel, magnet — each competing for radial space, especially in the breeder's tight central column.</p>"),
       ("Why is it a defining constraint?",
        "<p>Because every layer must fit while still breeding tritium and protecting the magnets. The radial build is where the compact machine's hardest trades are settled.</p>")],
     "general-arrangement": [
       ("What is the general arrangement?",
        "<p>The overall layout of the machine and plant — how the core, heating, cryogenics, fuel cycle and balance of plant are positioned and connected — the top-level engineering picture.</p>"),
       ("Where can I see it?",
        "<p>The public 3D model and headline blueprint sheets show the arrangement; the full detailed CAD is kept in a private, access-controlled build.</p>")],
     "the-radial-build-x": [("x","x")],
     "critical-current-envelope": [
       ("What is the critical-current envelope?",
        "<p>The surface, falling with field and temperature, above which a superconductor quenches to normal resistance. Magnets operate safely inside it with margin.</p>"),
       ("Why map it explicitly?",
        f"<p>Because reaching the breeder's and burner's fields means working near the REBCO high-field frontier, so Kronos maps the envelope openly (DOI {F['doi_rebco']}) rather than assuming comfortable margin.</p>")],
     "the-loss-cone": [
       ("What is the loss cone?",
        "<p>The range of particle velocities that can escape out the ends of a magnetic mirror. Particles whose motion falls in it are not reflected and are lost — the mirror's fundamental leak.</p>"),
       ("How does the burner deal with it?",
        f"<p>With high-field plugs and an ambipolar potential that reflect escaping ions — effective only if the plug reaches the ~{F['u_np']} density ratio, the burner's binding condition.</p>")],
     "the-magnet-materials-suite": [
       ("What is in the magnet materials suite?",
        "<p>REBCO superconducting tape, copper stabiliser, cryogenic structural steels and insulation — the material set that makes a high-field, mechanically-loaded coil work at cryogenic temperature.</p>"),
       ("Which material choice is most critical?",
        "<p>The structural alloy carrying cyclic Lorentz loads, since magnet fatigue is the binding gate — the superconductor enables the field, but the steel survives the forces.</p>")],
     "the-plasma-facing-suite": [
       ("What is in the plasma-facing materials suite?",
        f"<p>Tungsten armour on precipitation-strengthened copper-alloy heat sinks, rated for the breeder's {F['b_wall']} first-wall load — chosen for heat tolerance, low erosion and low fuel retention.</p>"),
       ("Are these permanent?",
        "<p>No — they are consumables designed for remote inspection and replacement, because they live in the machine's harshest environment.</p>")],
     "the-structural-materials-suite": [
       ("What is in the structural materials suite?",
        "<p>Low-activation ferritic-martensitic steels for the neutron-facing structure and high-strength cryogenic alloys for the magnets — chosen so activation is short-lived and strength holds cold.</p>"),
       ("Why low-activation steel specifically?",
        "<p>Because it decays to hands-on levels in decades rather than millennia, which is what keeps the neutron-rich breeder's waste bounded and manageable.</p>")],
     "verification-and-validation": [
       ("What is verification and validation?",
        "<p>Verification checks that a model solves its equations correctly; validation checks that those equations match reality. Both are needed before a computed number can be trusted for design.</p>"),
       ("How does Kronos approach it?",
        "<p>By anchoring to the experimental database, benchmarking engines against known results, and publishing the engines openly so others can verify them — reproducibility plus benchmarking, not assertion.</p>")],
     "what-reproducibility-proves": [
       ("What does reproducibility actually prove?",
        "<p>That a published number follows correctly from the stated model and inputs — that Kronos did the calculation it says it did. Anyone can re-run the open engines and get the same result.</p>"),
       ("What does it not prove?",
        "<p>That an unbuilt machine will behave exactly as modelled. That is why every figure is a computed design target, and why physical gates and high-fidelity analysis remain on the path to build.</p>")],
     "the-provenance-record": [
       ("What is the provenance record?",
        "<p>The documented chain from each published number back to the engine, inputs and version that produced it — so every figure can be traced to its source rather than taken on faith.</p>"),
       ("Why does provenance matter?",
        "<p>Because in a frozen, reproducible design, traceability is what lets a reviewer confirm that the papers, simulator and deposits all rest on the same canonical numbers.</p>")],
     "the-ai-quantum-record": [
       ("What is the AI, ML and quantum record?",
        f"<p>An open deposit (DOI {F['doi_ai']}) documenting the AI/ML methods and quantum-related work Kronos uses to accelerate design and analysis — published alongside the physics engines.</p>"),
       ("Does AI drive the design point?",
        "<p>No — the design rests on transparent physics engines; AI accelerates exploration and cross-checks. The record exists so those methods are as reproducible as the physics.</p>")],
     "the-dec-record": [
       ("What is the direct-energy-conversion record?",
        f"<p>An open deposit documenting the burner's direct-conversion engine — how escaping ions are decelerated and collected at about {F['u_dec']} — so the Q<sub>E</sub> = {F['u_QE']} figure can be reproduced.</p>"),
       ("Why publish it separately?",
        "<p>Because direct conversion is the burner's decisive efficiency step, worth its own reproducible record rather than being buried in a summary.</p>")],
     "the-rebco-record": [
       ("What is the REBCO magnet record?",
        f"<p>An open deposit (DOI {F['doi_rebco']}) mapping the high-temperature-superconducting magnets — critical current, stress, quench — against demonstrated coils, so the magnet claims can be checked.</p>"),
       ("What does it say about the magnet gate?",
        "<p>That the static case is sound with margin and cyclic fatigue is the binding open item — stated openly rather than assumed closed.</p>")],
     # --- Reference Devices ---
     "device-iter": [
       ("What is ITER and why does Kronos cite it?",
        "<p>ITER is the large international tokamak under construction to demonstrate fusion at scale. Kronos cites it as a source of the confinement and engineering database its design draws on.</p>"),
       ("Does Kronos compete with ITER?",
        "<p>Not directly — ITER is public science proving physics at scale; Kronos commercialises focused products. Its breeder's case does not depend on ITER's outcome.</p>")],
     "device-jet": [
       ("What was JET's significance?",
        "<p>The Joint European Torus held records for fusion power from D–T plasmas and validated much of the confinement physics later machines rely on. It is a cornerstone of the empirical database.</p>"),
       ("Why does Kronos reference it?",
        "<p>Because JET's D–T results are part of the experimental basis for the standard confinement scaling Kronos designs to, rather than optimistic extrapolation.</p>")],
     "device-nstx": [
       ("What is NSTX and why is it relevant to Kronos?",
        f"<p>NSTX (and its upgrade) is a spherical tokamak that demonstrated high beta at low aspect ratio — exactly the regime HYPERION uses. Its results underpin the breeder's &beta;<sub>N</sub> = {F['b_bN']} choice.</p>"),
       ("How closely does Kronos follow it?",
        f"<p>HYPERION runs comfortably within the no-wall beta limits observed on machines like NSTX, a deliberately conservative posture for a spherical tokamak at A = {F['b_A']}.</p>")],
     "device-diii-d": [
       ("What is DIII-D's contribution?",
        "<p>DIII-D is a versatile tokamak that produced much of the shaping, stability and negative-triangularity physics Kronos draws on — including the edge behaviour behind HYPERION's shape choice.</p>"),
       ("Why cite it for negative triangularity?",
        "<p>Because experiments there and on similar machines demonstrated that negative triangularity can suppress edge modes while keeping good confinement, grounding Kronos's design choice in data.</p>")],
     "device-alcator": [
       ("What did Alcator C-Mod demonstrate?",
        f"<p>The Alcator C-Mod tokamak reached high plasma pressure using very high magnetic field in a compact machine — direct evidence for the high-field, compact approach the breeder takes.</p>"),
       ("Why is that relevant to Kronos?",
        "<p>Because it validates the core premise that high field lets a small machine perform, which REBCO now makes achievable steadily rather than in short pulses.</p>")],
     "device-tftr": [
       ("What was TFTR?",
        "<p>The Tokamak Fusion Test Reactor was among the first to run D–T fuel and produce significant fusion power, part of the foundational D–T experimental record.</p>"),
       ("Why does Kronos reference it?",
        "<p>As part of the demonstrated basis for D–T operation the breeder relies on — real machines have run this fuel, not just models.</p>")],
     "device-jt60": [
       ("What is JT-60SA?",
        "<p>A large superconducting tokamak supporting ITER and advanced-scenario research, contributing to the steady-state and high-beta physics database.</p>"),
       ("How does it inform Kronos?",
        "<p>Its steady-state and advanced-regime results are part of the basis for the breeder's non-inductive, high-bootstrap operation.</p>")],
     "device-east-kstar": [
       ("What do EAST and KSTAR demonstrate?",
        "<p>These superconducting tokamaks have achieved long-pulse, high-performance plasmas — key evidence that steady-state operation with superconducting magnets is achievable.</p>"),
       ("Why cite them?",
        "<p>Because the breeder must run in true steady state, and these machines are part of the demonstrated basis that long-pulse superconducting operation works.</p>")],
     "device-nif": [
       ("What is the National Ignition Facility?",
        "<p>NIF is the inertial-confinement facility that achieved target energy gain in 2022 by laser-compressing fuel pellets — a landmark, but a very different approach from Kronos's magnetic confinement.</p>"),
       ("Why does Kronos reference it?",
        "<p>As context for the field's progress and to distinguish its own continuous, magnetically-confined approach from pulsed inertial fusion.</p>")],
     "device-w7x": [
       ("What is Wendelstein 7-X?",
        "<p>W7-X is the leading stellarator, demonstrating that intricately shaped coils can confine plasma steadily without a plasma current — and so without disruptions.</p>"),
       ("How does it relate to Kronos?",
        "<p>It is the main alternative disruption-free route; Kronos achieves disruption-free operation instead through its linear burner, avoiding the stellarator's coil complexity.</p>")],
     "device-tmx": [
       ("What were TMX and the historical tandem mirrors?",
        "<p>TMX and its successors were the experiments that developed tandem-mirror physics — end plugs and ambipolar potentials — the direct ancestors of the Kronos burner concept.</p>"),
       ("What did they show, and what limited them?",
        f"<p>They demonstrated the plugging physics but were limited by the magnet fields then available. Modern REBCO reaching {F['u_Bplug']} is what revives the concept for the burner.</p>")],
     "device-gdt": [
       ("What is the Gas-Dynamic Trap?",
        "<p>The GDT is a modern mirror experiment that has achieved high beta and hot ions in an open, linear configuration — recent evidence that mirror confinement can reach reactor-relevant parameters.</p>"),
       ("Why is it important to the burner's case?",
        "<p>Because it provides contemporary experimental support for the linear-mirror approach the burner uses, beyond the historical tandem-mirror record.</p>")],
    }
    for slug, faq in Q.items():
        if faq and faq[0][0] != "x":
            enrich(slug, faq=faq)