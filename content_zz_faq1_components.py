# -*- coding: utf-8 -*-
"""FAQ coverage batch 1 — Components & Hardware. Two page-specific Q&A each."""
def register(cat, page, F, enrich):
    Q = {
     "tf-coil": [
       ("Which machine uses the toroidal-field coils?",
        f"<p>The breeder, HYPERION. They are its main confining magnet, D-shaped REBCO windings reaching {F['b_Bpeak']} at the conductor. The linear burner has no toroidal field — it confines its plasma in a straight solenoid instead.</p>"),
       ("Are these coils a standard or a first-of-a-kind component?",
        f"<p>The geometry is conventional tokamak practice, but the REBCO high-temperature-superconductor construction at {F['b_Bpeak']} is at the field frontier. Kronos maps the conductor, joints and structure in its open REBCO study (DOI {F['doi_rebco']}).</p>")],
     "pf-coil-set": [
       ("What do the poloidal-field coils actually do?",
        "<p>They are the real-time actuators for plasma position and shape — elongation, triangularity and vertical stability — driven continuously by the control system. They shape the field; the plasma current makes most of the poloidal field itself.</p>"),
       ("Is this hardware novel?",
        "<p>No. Ring shaping coils are standard tokamak equipment; the engineering task is fitting and powering them around a compact spherical machine rather than inventing them.</p>")],
     "central-solenoid-component": [
       ("What is the central solenoid for?",
        f"<p>It acts as a transformer primary, inducing and ramping HYPERION's {F['b_Ip']} plasma current. Its available flux swing (volt-seconds) is one reason the breeder also relies on non-inductive current drive and bootstrap current for steady state.</p>"),
       ("Why is it a hard component in a spherical tokamak?",
        "<p>Because the machine's central column is deliberately slim, there is very little room for the solenoid. That tight flux budget is a defining trade of the compact, low-aspect-ratio design.</p>")],
     "central-cell-solenoid": [
       ("Which machine has a central-cell solenoid?",
        f"<p>The burner (AEGIS and MetroVolt). It is a long string of solenoid coils producing a uniform axial field of about {F['u_Bm']} class along the machine, and it is the simplest part of the magnet system.</p>"),
       ("How does it change between products?",
        f"<p>Only in length. The same coil string is extended from {F['u_ref_len']} to {F['u_aeg_len']} (AEGIS) to {F['u_mv_len']} (MetroVolt) to reach different power classes — the physics per metre is unchanged.</p>")],
     "mirror-throat-coil": [
       ("What does the mirror-throat coil do?",
        f"<p>At each end of the burner's central cell it raises the field to about {F['u_Bm']}, reflecting particles back toward the centre. With the plug it sets the mirror ratio and the end confinement.</p>"),
       ("Is it the burner's highest-field magnet?",
        f"<p>No — the high-field plug coil is, reaching {F['u_Bplug']}. The throat coil operates at the lower central-cell-to-throat field and is a less demanding magnet.</p>")],
     "plug-coil": [
       ("Why is the plug coil the burner's most critical magnet?",
        f"<p>It reaches the burner's peak field, {F['u_Bplug']}, to build the ambipolar potential that confines the central plasma. Its cyclic fatigue at full field is the burner's single binding magnet gate.</p>"),
       ("How is that fatigue gate closed?",
        "<p>By a powered REBCO test coil taken through many energise cycles at full field. A single cycle is well within limits; it is the repeated cycling that must be demonstrated, and Kronos names it openly rather than assuming it.</p>")],
     "hts-current-lead": [
       ("What is an HTS current lead?",
        "<p>A high-temperature-superconductor feedthrough that carries the magnets' large currents from room-temperature power supplies into the cold mass while minimising heat leaking into the cryogenic system.</p>"),
       ("Is it off-the-shelf?",
        "<p>It is a specialised, long-lead item, but one demonstrated on existing superconducting machines rather than a novel invention — solid engineering, not an open physics question.</p>")],
     "superconducting-joint": [
       ("Why do the magnets need superconducting joints?",
        f"<p>Superconducting tape comes in finite lengths, so long coils are spliced from many pieces. Joint resistance affects both efficiency and how a coil behaves in a quench, which is why it is a focus of the REBCO study (DOI {F['doi_rebco']}).</p>"),
       ("Is joint quality a risk?",
        "<p>It is a fabrication-qualification item, not an open physics unknown — the goal is a repeatable low-resistance splice, demonstrated and quality-controlled at production scale.</p>")],
     "coil-case": [
       ("What does the coil case do?",
        "<p>Each superconducting coil sits in a high-strength steel case, and intercoil structure ties the coils together. This structure carries the hoop and overturning Lorentz loads the winding pack alone could not.</p>"),
       ("Is the structural case a solved problem?",
        "<p>Static loads analyse as sound with margin. The open question is cyclic fatigue of the structure under repeated operation, which is part of the named magnet gate rather than the static case.</p>")],
     "quench-dump-resistor": [
       ("What is the quench dump resistor for?",
        "<p>If a magnet quenches, its stored energy is switched into the dump resistor and dissipated as heat safely outside the coil, preventing a damaging hot spot. Its size follows directly from the coil's stored magnetic energy.</p>"),
       ("Is quench protection proven for these magnets?",
        "<p>Kronos's adiabatic hot-spot analysis reports the magnet self-protecting within its design basis; REBCO's slow quench propagation makes fast, reliable detection — not the dump itself — the harder half of the job.</p>")],
     "dump-switch": [
       ("What is the quench dump switch?",
        "<p>A fast breaker that opens on a quench signal to divert the coil current into the dump resistor within milliseconds. Its speed and reliability are central to magnet protection.</p>"),
       ("Is it a novel component?",
        "<p>No — high-current DC breakers are established technology. The engineering task is specifying and qualifying one to the magnets' current and reliability requirements.</p>")],
     "vacuum-vessel-sector": [
       ("What is a vacuum-vessel sector?",
        "<p>A forged-and-rolled steel segment of the breeder's chamber, joined to its neighbours by automated field welds to form the sealed, ported vessel that holds ultra-high vacuum and provides the first structural boundary.</p>"),
       ("Why is it a schedule driver?",
        "<p>The large sector forgings are a long-lead procurement item (of order two years), so they sit on the critical path and are ordered early in the build.</p>")],
     "vessel-port": [
       ("What are vessel ports for?",
        "<p>They penetrate the vessel and blanket to admit heating beams, diagnostics and remote-handling tools, sealed by port plugs. Their number and size trade access against shielding and structural strength.</p>"),
       ("Are ports a weak point?",
        "<p>They are a deliberate design trade, not a flaw — every penetration is a hole in the shield, so ports are sized and shielded to preserve magnet protection and vessel integrity.</p>")],
     "blanket-module-component": [
       ("What does the breeding blanket module do?",
        f"<p>It surrounds the breeder plasma, slows the fusion neutrons to breed tritium (toward breeding ratio {F['b_TBR']}, ~{F['b_T']}/yr) and recovers their energy as heat. It is the component that turns HYPERION's neutrons into product.</p>"),
       ("Why is the blanket built in modules?",
        "<p>So worn units can be replaced remotely without rebuilding the machine — modularity is central to plant availability, and the blanket is a component that will be serviced over the plant's life.</p>")],
     "first-wall-panel-component": [
       ("What load does the first-wall panel take?",
        f"<p>It faces the plasma directly and carries the breeder's neutron and heat load, rated for a wall loading of {F['b_wall']}. Tungsten armour is bonded to an actively-cooled copper-alloy heat sink.</p>"),
       ("Is the first wall replaceable?",
        "<p>Yes — panels are designed as modular, remotely-replaceable units, because in a neutron-rich machine the first wall is a consumable that is inspected and swapped, not a permanent structure.</p>")],
     "divertor-cassette-component": [
       ("Which machine uses the divertor cassette?",
        "<p>The breeder. It carries the high-heat-flux target plates where the exhaust field lines land, and is swapped by remote handling as it wears. The linear burner exhausts to end tanks instead of a divertor.</p>"),
       ("How is the divertor heat load kept survivable?",
        "<p>By radiating most of the exhaust power before it reaches the targets (detachment / high radiated fraction). Achieving that while keeping the core clean is one of HYPERION's named performance gates.</p>")],
     "neutron-shield-block": [
       ("What does the neutron shield block protect?",
        "<p>It sits between the plasma and the magnets, slowing and capturing neutrons to protect the superconductors' lifetime. It is heaviest on the neutron-rich breeder, where space in the central column is scarce.</p>"),
       ("Is shielding a formality?",
        "<p>No — fitting adequate magnet shielding into a compact machine is a genuine neutronics constraint that trades directly against the size of the central column.</p>")],
     "reflector-liner-component": [
       ("Which machine has a reflector liner?",
        "<p>The burner. Its reflective liner returns radiation to the plasma, improving the power balance that closes the machine — it is a deciding component, not a detail.</p>"),
       ("What is the trade on the liner?",
        "<p>Higher reflectivity helps the power balance but the liner material also activates under the burner's residual neutrons. Kronos flags that reflectivity-vs-activation tension explicitly rather than assuming an ideal mirror.</p>")],
     "expander-tank-component": [
       ("What is the expander / end tank?",
        "<p>At each end of the burner, the field fans out into an expander tank where the escaping plasma is spread over a large area and its energy handled — the linear machine's equivalent of a divertor.</p>"),
       ("Does the direct converter sit here?",
        f"<p>Yes — the expander is where the escaping charged particles are decelerated and their energy recovered by the direct-energy converter at about {F['u_dec']}, the step that lets the burner skip a steam cycle.</p>")],
     "dec-collector-ring": [
       ("What does the DEC collector ring do?",
        f"<p>Its angled, biased 'venetian-blind' rings decelerate the burner's escaping ions and collect their energy as electricity at about {F['u_dec']}. It is the heart of direct energy conversion.</p>"),
       ("Why does direct conversion matter?",
        f"<p>Because D–&sup3;He releases its energy as charged particles, they can be turned into electricity directly instead of via heat. That is the single biggest reason the burner's plant-level efficiency (Q<sub>E</sub> = {F['u_QE']}) can exceed a thermal plant's.</p>")],
     "tritium-extraction-unit": [
       ("What does the tritium extraction unit do?",
        f"<p>It removes and purifies the tritium bred in the breeder's blanket so it can be accounted for and re-injected as fuel — the recovery step of the closed D–T fuel cycle that yields ~{F['b_T']}/yr.</p>"),
       ("Is it a licensing-relevant component?",
        f"<p>Yes. Tritium is the breeder's one genuinely radioactive material, so its extraction, inventory ({F['b_startup']} startup) and accounting are handled with permeation barriers, containment and continuous monitoring, and named as a licensing gate.</p>")],
     "nbi-injector": [
       ("What does the neutral-beam injector do?",
        f"<p>It accelerates ions, neutralises them, and fires fast atoms across the confining field to heat the plasma and drive current, within HYPERION's {F['b_Paux']} auxiliary budget.</p>"),
       ("Is it standard equipment?",
        "<p>High-energy beams use negative-ion sources and are specialised, long-lead components, but they are demonstrated technology on existing machines rather than an open research question.</p>")],
     "gyrotron": [
       ("What is the gyrotron used for?",
        "<p>It generates high-power microwaves for electron-cyclotron heating and current drive, enabling precise, steerable power deposition — useful both for heating and for suppressing specific tearing modes.</p>"),
       ("Is it a long-lead item?",
        "<p>Yes. Megawatt-class gyrotrons are specialised sources with multi-year lead times, delivered to the plasma through diamond windows and low-loss transmission lines.</p>")],
     "rf-antenna": [
       ("What does the RF antenna / launcher do?",
        "<p>It couples radio-frequency power into the plasma for heating and current drive, matched to the plasma edge so the power crosses into the plasma rather than reflecting back.</p>"),
       ("Is RF heating novel?",
        "<p>No — ion- and electron-cyclotron launchers are established heating technology; the design work is the antenna's coupling, cooling and survivability at the plasma edge.</p>")],
     "pellet-injector-component": [
       ("What is the pellet injector for?",
        "<p>It fires frozen fuel pellets deep into the plasma to fuel the core efficiently, reaching further in than gas puffing and giving control over the density profile.</p>"),
       ("Is pellet fuelling proven?",
        "<p>Yes — cryogenic pellet injection is routine on today's tokamaks. It is conventional fuelling hardware adapted to the machine, not an open question.</p>")],
     "cryostat-component": [
       ("What does the cryostat do?",
        "<p>It is the large vacuum enclosure around the entire cold mass, providing the insulating vacuum that stops room-temperature heat from reaching the magnets so the cryoplant only handles residual leaks.</p>"),
       ("Is it a novel structure?",
        "<p>No — it is a large but conventional vacuum vessel. The engineering is scale and penetrations, not new physics.</p>")],
     "thermal-shield-component": [
       ("What is the thermal shield?",
        "<p>An actively-cooled shield inside the cryostat, with multi-layer insulation, that intercepts thermal radiation before it reaches the cold magnets — cutting the heat load the cryoplant must remove.</p>"),
       ("Why does intercepting heat matter so much?",
        "<p>Because heat removed at cryogenic temperature is expensive. Every watt the thermal shield stops at an intermediate temperature is a watt the costly cold refrigerator does not have to lift.</p>")],
     "cryopump-component": [
       ("What does the cryopump do?",
        "<p>It freezes exhaust gas onto very cold surfaces to achieve the high pumping speeds a fusion vessel needs to control density and remove helium ash. It fills up and is periodically regenerated.</p>"),
       ("Does it handle tritium?",
        "<p>On the breeder, yes — the exhaust it captures is tritium-bearing, so cryopump regeneration is part of the tritium-handling loop, not just vacuum housekeeping.</p>")],
     "cold-box": [
       ("What is the cryoplant cold box?",
        "<p>It is the heart of the helium refrigerator — the insulated vessel holding the heat exchangers and turbines that produce the cold helium circulated to the magnets and shields.</p>"),
       ("Is the cryoplant novel?",
        "<p>No. Large helium refrigeration is mature big-science and industrial-gas engineering; Kronos's construction-readiness review classes it as ready for detailed design.</p>")],
     "cryoline": [
       ("What is the cryogenic distribution line?",
        "<p>Vacuum-insulated piping that carries cold helium from the cryoplant to the magnets, current leads and thermal shields, and returns it — the plumbing of the cold system.</p>"),
       ("Is it a standard component?",
        "<p>Yes — cryogenic transfer lines are established technology. The design work is routing, heat-leak budgeting and reliability, not invention.</p>")],
     "heat-exchanger-component": [
       ("What does the heat exchanger do?",
        "<p>On the breeder it transfers the blanket's captured neutron heat from the primary coolant to the power-conversion loop. It is conventional thermal-plant equipment sized to the machine's heat load.</p>"),
       ("Is this the breeder's route to electricity?",
        "<p>Yes — the breeder recovers energy as heat through a thermal cycle, unlike the burner's direct conversion. But the breeder's commercial case rests on neutrons, tritium and helium-3, not on that electricity.</p>")],
     "primary-coolant-pump": [
       ("What does the primary coolant pump do?",
        "<p>It circulates coolant through the breeder's blanket and first wall to carry away the neutron and surface heat, feeding it to the heat exchanger. It is standard high-reliability power-plant equipment.</p>"),
       ("Is coolant technology a fusion unknown?",
        "<p>No — the pumps and loops are conventional; the fusion-specific requirement is compatibility with the neutron environment and, on the breeder, with tritium permeation.</p>")],
     "power-supply-converter": [
       ("What do the power supplies and converters do?",
        "<p>They condition grid power into the precise, controllable currents the magnets, heating systems and coils need, and absorb energy during ramps and faults. They are the machine's electrical backbone.</p>"),
       ("Is this novel hardware?",
        "<p>No — high-power converters are mature industrial technology. The task is specification and integration to the machine's dynamic requirements, classed as ready for detailed design.</p>")],
     "gravity-support-component": [
       ("What are the gravity supports?",
        "<p>The structural feet that carry the entire cold mass and vessel weight down to the building foundation while accommodating thermal contraction and seismic loads, and limiting heat leak into the cold mass.</p>"),
       ("Are they routine?",
        "<p>They are careful but conventional structural engineering, combining load-bearing, low thermal conductance and seismic qualification — well within established practice.</p>")],
     "magnetic-pickup-coil": [
       ("What does the magnetic pickup coil measure?",
        "<p>It senses the local magnetic field and its rate of change, feeding the real-time reconstruction of plasma position, shape and current that the control system acts on.</p>"),
       ("Why are these diagnostics critical?",
        "<p>Because the control loop can only hold the plasma as well as it can see it — magnetic sensors are the primary, fast, robust measurement underpinning position and shape control.</p>")],
     "diagnostic-port-plug": [
       ("What is a diagnostic port plug?",
        "<p>An instrumented plug that fills a vessel port, carrying diagnostic sensors while maintaining vacuum and neutron shielding. It packages measurement hardware into the machine's access openings.</p>"),
       ("Why integrate diagnostics into a shielded plug?",
        "<p>Because every opening is a gap in the shield. Building diagnostics into a shielding plug lets the machine see inside without compromising magnet protection or vacuum integrity.</p>")],
     "sis-controller": [
       ("What does the safety-instrumented controller do?",
        "<p>It is the independent safety system that monitors for hazardous conditions and drives the plant to a safe state, kept separate from the machine-protection and normal control systems by design.</p>"),
       ("How does it differ from machine protection?",
        "<p>Machine protection guards the hardware; the safety-instrumented system protects people and the environment. Keeping them independent is standard safety-engineering practice, applied here to a fusion plant.</p>")],
    }
    for slug, faq in Q.items():
        enrich(slug, faq=faq)
