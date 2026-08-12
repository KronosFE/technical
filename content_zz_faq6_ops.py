# -*- coding: utf-8 -*-
"""FAQ coverage batch 6 — Standards, Operations, Methodology, Diagnostics, History, Validation, Comparisons, Team, Open Science."""
def register(cat, page, F, enrich):
    Q = {
     # --- Codes & Standards ---
     "codes-overview": [
       ("Does fusion have its own regulatory code?",
        "<p>Fusion regulation is still maturing, so Kronos builds to established nuclear, pressure, structural, electrical and safety codes already used across heavy industry — a recognised basis rather than a bespoke one.</p>"),
       ("Why design to standards this early?",
        "<p>Because licensing and construction depend on it. Naming the codes each subsystem will meet is part of showing the design is buildable, not just physically sound.</p>")],
     "asme-bpvc": [
       ("Why does the ASME Boiler & Pressure Vessel Code apply?",
        "<p>The vacuum vessel, cooling loops and pressure boundaries are pressure-retaining components, so they are designed and qualified to the ASME BPVC like other nuclear and industrial pressure equipment.</p>"),
       ("Is this novel for fusion?",
        "<p>No — it is established pressure-equipment practice applied to fusion hardware, which is part of why much of the plant is classed as ready for detailed design.</p>")],
     "nqa-1": [
       ("What is ASME NQA-1?",
        "<p>The nuclear quality-assurance standard governing how safety-related work is planned, controlled and documented. Kronos references it for the rigour its safety-relevant systems require.</p>"),
       ("Why adopt a nuclear QA standard?",
        "<p>Because tritium handling and radiation protection demand nuclear-grade traceability, and NQA-1 is the recognised framework for that quality assurance.</p>")],
     "materials-standards": [
       ("Why do ASTM materials standards matter?",
        "<p>They define how the steels, copper alloys and other materials are specified, tested and certified, so that what is built matches what was analysed. Material qualification rests on them.</p>"),
       ("Do fusion materials need new standards?",
        "<p>Low-activation and irradiated-material behaviour extend existing standards, but the baseline specification and testing framework is established ASTM practice.</p>")],
     "seismic-standards": [
       ("How is the plant designed for earthquakes?",
        "<p>To ASCE seismic and structural standards, which set the ground-motion and load requirements the building and supports must withstand — the same basis used for other critical facilities.</p>"),
       ("Which components are most seismic-sensitive?",
        "<p>The heavy cold mass and its gravity supports, which must carry and restrain large masses through seismic events while limiting heat leak — a qualified structural problem.</p>")],
     "electrical-standards": [
       ("Which electrical standards apply?",
        "<p>IEEE electrical standards govern the high-power supplies, distribution and protection that feed the magnets and heating systems — established practice for large electrical installations.</p>"),
       ("Is the electrical plant unusual?",
        "<p>It is large and dynamic but conventional; Kronos's review classes power supplies and distribution as ready for detailed design.</p>")],
     "cryogenic-standards": [
       ("Why are cryogenic codes needed?",
        "<p>The helium refrigeration, transfer lines and cold vessels operate near absolute zero and must meet cryogenic safety and pressure codes — established from decades of industrial and big-science cryogenics.</p>"),
       ("Is fusion cryogenics special?",
        "<p>The scale is large but the engineering is mature; the fusion-specific part is managing nuclear heating of the cold mass, not the refrigeration itself.</p>")],
     "functional-safety-standards": [
       ("What are IEC 61508 / 61511 for?",
        "<p>They govern functional safety — how safety-instrumented systems are designed to reliably bring a plant to a safe state. Kronos's independent safety controller is built to this framework.</p>"),
       ("Why keep functional safety separate?",
        "<p>Because a safety system must be independent of the control and machine-protection systems it backs up, which is exactly what these standards require.</p>")],
     "quality-management": [
       ("Why ISO 9001 and AS9100?",
        "<p>They provide the quality-management framework — documented processes, traceability, continuous improvement — that disciplined engineering and eventual manufacturing require. AS9100 adds aerospace-grade rigour.</p>"),
       ("How does this connect to the frozen design?",
        "<p>Quality management and the frozen-canon discipline reinforce each other: both are about traceability and controlling change so nothing drifts silently.</p>")],
     "fire-protection-standards": [
       ("How is fire protection handled?",
        "<p>To NFPA standards, covering the electrical, cryogenic (oxygen-deficiency) and conventional fire hazards of a large industrial plant — established codes applied to the facility.</p>"),
       ("Are there fusion-specific fire risks?",
        "<p>The notable ones are cryogen release and high-power electrical faults, both addressed within existing NFPA and industrial-safety practice.</p>")],
     "tritium-standards": [
       ("What governs tritium handling?",
        f"<p>Radiological and tritium-specific standards set the containment, monitoring and accounting requirements. They apply mainly to the breeder, whose fuel cycle runs at ~{F['b_T']}/yr of tritium.</p>"),
       ("Is the burner subject to them?",
        f"<p>Far less — being low-neutron D–&sup3;He ({F['u_fn']}), it handles little tritium, so radiological requirements fall overwhelmingly on the breeder.</p>")],
     "iaea-framework": [
       ("How does the IAEA safety framework apply?",
        "<p>It provides internationally recognised safety principles and guidance that inform how a fusion facility is designed, operated and safeguarded, even as fusion-specific regulation develops.</p>"),
       ("Does fusion raise safeguards concerns?",
        "<p>It produces no fissile material, but neutron flux and tritium are handled responsibly within this framework — a real consideration Kronos does not dismiss.</p>")],
     # --- Operations & Commissioning ---
     "commissioning-overview": [
       ("What does commissioning a fusion machine involve?",
        "<p>Taking each system from cold, then integrating them — energising magnets, pumping down, validating interlocks — up to first plasma, with entry and exit criteria at every stage.</p>"),
       ("Can stages be skipped to save time?",
        "<p>No — nothing advances until the prior stage passes. That discipline is how a complex new machine is brought to life safely rather than quickly.</p>")],
     "cold-commissioning": [
       ("What is cold commissioning?",
        "<p>Bringing the magnets and cryogenic system down to operating temperature and verifying vacuum, cooling and instrumentation before any plasma — proving the cold plant works in isolation.</p>"),
       ("Why do it before first plasma?",
        "<p>Because faults are far easier and safer to find and fix in a cold, un-activated machine than once plasma operation begins.</p>")],
     "magnet-commissioning": [
       ("What happens during magnet commissioning?",
        "<p>The superconducting coils are energised in steps to full field, with quench detection and protection verified at each level, confirming the magnets and their protection behave as designed.</p>"),
       ("Is this where the fatigue gate is tested?",
        "<p>Commissioning proves the magnets to full field; the separate cyclic-fatigue gate — many energise cycles — is demonstrated on a dedicated powered test coil.</p>")],
     "plasma-operation": [
       ("What does running the plasma involve?",
        "<p>Holding the plasma at its operating point by continuously balancing heating, fuelling, current drive and exhaust, while the control system corrects position and shape in real time.</p>"),
       ("Is the driven plasma easy to control?",
        "<p>More controllable than an igniting one — turn the heating down and the power follows. That controllability is a direct benefit of Kronos's driven-operation choice.</p>")],
     "power-ascension": [
       ("What is power ascension?",
        "<p>A stepwise campaign that climbs from first plasma toward the design point, demonstrating performance at each level rather than assuming the full operating point from the start.</p>"),
       ("Why ascend in steps?",
        "<p>Because it lets performance be proven and problems caught gradually — the honest way to reach a design point, and how Kronos frames the road after first plasma.</p>")],
     "first-plasma-campaign": [
       ("What is the first-plasma campaign?",
        "<p>The initial period of plasma operation after commissioning, establishing reliable breakdown, current ramp and basic control — the start of physics operation, not the finished machine.</p>"),
       ("Does first plasma mean the machine works?",
        "<p>It is a major milestone but only the beginning; the power-ascension campaign that follows is what demonstrates real performance.</p>")],
     "performance-demonstration": [
       ("What is performance demonstration?",
        "<p>Showing the machine reaches its design targets — gain, confinement, steady operation — with measurements, turning modelled figures into demonstrated ones through the ascension campaign.</p>"),
       ("How does this relate to the gates?",
        "<p>It is how the later go/no-go gates are satisfied: performance is demonstrated against explicit criteria rather than claimed.</p>")],
     "fuel-cycle-operation": [
       ("What does operating the fuel cycle involve?",
        f"<p>Running the closed tritium loop on the breeder — breeding, extracting, purifying, accounting and re-injecting — while keeping inventory low and every gram tracked. It targets ~{F['b_T']}/yr.</p>"),
       ("Why is it operationally demanding?",
        "<p>Because tritium is mobile and radioactive, so accounting and containment are continuous safety-critical activities, not periodic checks.</p>")],
     "maintenance-strategy": [
       ("What is the maintenance strategy?",
        "<p>Modular components and remote handling so activated parts — first wall, blanket, divertor — can be inspected and replaced quickly. Maintainability is designed in from the start.</p>"),
       ("Why does maintenance shape the design?",
        "<p>Because how fast worn components can be swapped sets plant availability, making remote maintainability a first-order design driver rather than an afterthought.</p>")],
     "availability-operation": [
       ("What does operating for availability mean?",
        "<p>Running the plant to maximise the fraction of time it generates — which depends on component lifetimes and how quickly maintenance restores the machine.</p>"),
       ("Does Kronos claim high availability from day one?",
        "<p>No — it flags early-life availability as a leading open study, expecting it to improve with operating experience rather than starting mature. That is part of the honest commercial picture.</p>")],
     # --- Process & Methodology ---
     "design-methodology": [
       ("What is the Kronos design methodology?",
        "<p>Fix a frozen, internally consistent design point in physics-based engines, explore the space around it, apply margins, and publish the engines openly so the point can be reproduced and checked.</p>"),
       ("What makes it different?",
        "<p>Its openness and discipline — a single frozen canon, transparent reduced-order engines, and stated gates — rather than a proprietary claim taken on trust.</p>")],
     "the-operating-window": [
       ("What is the operating window?",
        "<p>The region of parameters — density, temperature, current, field — within which the machine runs stably and meets its targets. The design point sits inside it with margin.</p>"),
       ("Why design to a window, not a point?",
        "<p>Because real machines vary, so a robust design keeps margin to every limit rather than balancing on a single knife-edge combination.</p>")],
     "design-margins": [
       ("Why design with margins?",
        f"<p>Because models and materials have uncertainty, so Kronos runs below limits — for example &beta;<sub>N</sub> = {F['b_bN']} within the no-wall limit and q&#8329;&#8325; = {F['b_q95']} away from disruptive resonances — rather than at them.</p>"),
       ("Does margin mean the design is timid?",
        "<p>No — it means it is robust. Margin is what separates a buildable machine from an optimistic point estimate.</p>")],
     "the-freeze-discipline": [
       ("What is the freeze discipline?",
        "<p>Fixing the design as one canonical set of numbers so nothing drifts and every figure traces to a single source. Changes are deliberate and controlled, not silent.</p>"),
       ("Why is freezing valuable?",
        "<p>Because a frozen point can be reproduced, checked and built against — it is what makes the open deposits and the simulator agree with the papers.</p>")],
     "design-space-exploration": [
       ("What is design-space exploration?",
        "<p>Systematically varying inputs across the reduced-order engines to map how performance responds, so the chosen point is understood in context rather than found by luck.</p>"),
       ("What makes it practical here?",
        "<p>The fast reduced-order engines — running large scans is cheap, which is exactly why Kronos uses transparent engines rather than only heavy simulation.</p>")],
     "sensitivity-analysis": [
       ("What does sensitivity (tornado) analysis show?",
        "<p>Which inputs move the results most, ranked so the design's true drivers and risks are visible. It tells you where margin and further work matter, and where they do not.</p>"),
       ("How does Kronos use it?",
        "<p>To identify and name the binding items — like the magnet fatigue gate and the plug-density requirement — rather than treating all uncertainties as equal.</p>")],
     "uncertainty-quantification": [
       ("What is uncertainty quantification?",
        "<p>Carrying the uncertainty in inputs and models through to the results, so a figure comes with a credible range rather than false precision.</p>"),
       ("Why does it matter for credibility?",
        "<p>Because honest ranges and named assumptions are more trustworthy than a single confident number — consistent with Kronos's honesty framework.</p>")],
     "benchmarking": [
       ("What is benchmarking against experiment?",
        "<p>Checking the engines reproduce known results from real machines before trusting them on a new design — validation against data, not just internal consistency.</p>"),
       ("Which machines are used?",
        f"<p>Spherical-tokamak and high-field results (such as NSTX and Alcator C-Mod) anchor the breeder; mirror experiments anchor the burner. The design is built on standard scaling (H<sub>98</sub> = {F['b_H98']}), not extrapolation.</p>")],
     "model-shadow-twin": [
       ("What is the model-to-shadow-to-twin progression?",
        "<p>A design model becomes a shadow that tracks a real machine's data, and finally a digital twin kept in step with the operating plant — increasing fidelity as hardware comes online.</p>"),
       ("Where is Kronos on that path?",
        "<p>At the reproducible design-model stage, with the open engines and interactive simulator — the twin comes as real machines are built and instrumented.</p>")],
     # --- Diagnostics & Measurement ---
     "plasma-diagnostics": [
       ("What are plasma diagnostics for?",
        "<p>They measure the plasma — temperature, density, position, radiation, neutrons — both to control it in real time and to demonstrate performance against the design targets.</p>"),
       ("Which are most critical?",
        "<p>Magnetic sensors for fast position and shape control, since the control loop can only hold the plasma as well as it can see it.</p>")],
     "magnetic-diagnostics": [
       ("What do magnetic diagnostics measure?",
        "<p>The magnetic field and its rate of change around the plasma, feeding the real-time reconstruction of plasma position, shape and current the control system acts on.</p>"),
       ("Why are they the backbone?",
        "<p>Because they are fast, robust and reliable — the primary measurement underpinning equilibrium control on any tokamak.</p>")],
     "thomson-scattering": [
       ("What does Thomson scattering measure?",
        "<p>Laser light scattered off plasma electrons gives local electron temperature and density profiles — a cornerstone diagnostic for confirming the plasma's core conditions.</p>"),
       ("Why is it valuable?",
        "<p>Because it directly measures the temperature and density that set fusion power, turning modelled profiles into measured ones.</p>")],
     "interferometry": [
       ("What does interferometry measure?",
        "<p>The phase shift of a beam crossing the plasma gives the line-integrated electron density — a fast, robust density measurement used for control and fuelling.</p>"),
       ("How does it relate to density limits?",
        "<p>It monitors how close the breeder runs to the Greenwald density limit, informing fuelling and disruption avoidance.</p>")],
     "spectroscopy": [
       ("What does plasma spectroscopy reveal?",
        f"<p>The light the plasma emits identifies impurities and their concentrations, tracking plasma purity — directly relevant to keeping HYPERION near its clean Z<sub>eff</sub> of {F['b_Zeff']}.</p>"),
       ("Why does purity monitoring matter?",
        "<p>Because impurities radiate and dilute the fuel, so watching them is essential to holding the power balance, especially in the burner.</p>")],
     "bolometry": [
       ("What does bolometry measure?",
        "<p>The total radiated power from the plasma, mapping where energy is being lost as radiation — essential for verifying the divertor's high-radiated-fraction exhaust strategy.</p>"),
       ("Why is it tied to a performance gate?",
        "<p>Because HYPERION's divertor depends on radiating most of the exhaust power, and bolometry is how that radiated fraction is confirmed.</p>")],
     "neutron-diagnostics": [
       ("What do neutron diagnostics measure?",
        f"<p>The rate and energy of fusion neutrons, which directly indicate fusion power. In the neutron-rich breeder ({F['b_Pn']}) they are a primary performance measurement.</p>"),
       ("Are they useful on the burner too?",
        f"<p>Yes — the burner's small neutron signal ({F['u_fn']}) is a sensitive monitor of the D–D side reactions and thus of plasma conditions.</p>")],
     "fiber-bragg-sensing": [
       ("What is fibre-Bragg structural sensing?",
        "<p>Optical fibres whose reflected wavelength shifts with strain and temperature, giving distributed structural monitoring of components like magnets — even in electrically noisy, high-field environments.</p>"),
       ("Why use optical sensing here?",
        "<p>Because fibre sensors are immune to the strong electromagnetic fields around the magnets and can be embedded to watch the structure whose fatigue is the binding gate.</p>")],
     # --- History & Context ---
     "history-of-fusion": [
       ("How long has fusion been pursued?",
        "<p>Since the mid-20th century — decades of steady progress in confinement, heating and materials that built the experimental database today's designs rely on.</p>"),
       ("What changed to make commercial fusion plausible now?",
        "<p>High-temperature superconductors enabling compact high-field machines, a mature physics database, and business models like Kronos's that earn before net-electric power is solved.</p>")],
     "history-of-mirrors": [
       ("Why did magnetic mirrors fade, then return?",
        f"<p>Early mirrors leaked through the loss cone and the tandem fixes needed stronger magnets than existed. Modern REBCO reaching {F['u_Bplug']} is what gives the concept its second life in the burner.</p>"),
       ("Was the mirror physics wrong?",
        "<p>No — the tandem-plug and ambipolar physics were understood; the enabling magnets simply were not available until now.</p>")],
     "history-of-superconducting-magnets": [
       ("How did high-field superconductors change fusion?",
        f"<p>REBCO tape carries current and field older superconductors could not, letting compact machines reach {F['b_Bpeak']} — shrinking machine size and cost, since both fall steeply with field.</p>"),
       ("Why is this the pivotal enabler?",
        "<p>Because both Kronos machines depend on high field: the compact breeder and the mirror-plugging burner alike only work with REBCO-class magnets.</p>")],
     "the-fusion-landscape": [
       ("What does the modern fusion landscape look like?",
        "<p>A mix of large public programmes proving physics at scale and private companies racing toward products, most aiming at net-electric power from a single machine.</p>"),
       ("Where does Kronos sit?",
        "<p>On a distinct wedge — selling the breeder's neutrons and isotopes first, so its business does not wait on net-electric gain.</p>")],
     # --- Validation & Reproducibility ---
     "validation-suite-breeder": [
       ("What is the breeder validation suite?",
        f"<p>The set of open engines, inputs and expected outputs that reproduce HYPERION's design point (DOI {F['doi_b']}, v2 {F['doi_b2']}) — so its Q = {F['b_Q']} and {F['b_Pfus']} can be re-derived.</p>"),
       ("What does reproducing it prove?",
        "<p>That the numbers follow from the stated model and inputs — not that the unbuilt machine will match them, which is why physical gates remain on the path to build.</p>")],
     "validation-suite-burner": [
       ("What is the burner validation suite?",
        f"<p>The open engines and cases that reproduce the burner's design point (DOI {F['doi_u']}) — its Q<sub>E</sub> = {F['u_QE']}, neutron fraction {F['u_fn']}, and the three product housings.</p>"),
       ("Does it include the honest caveat?",
        f"<p>Yes — the suite reproduces the requirement-class net power contingent on the ~{F['u_np']} plug-density ratio, not an unconditional claim.</p>")],
     "tier-1-tier-2": [
       ("What are Tier-1 and Tier-2 reproduction?",
        "<p>Tier-1 is byte-exact reproduction of deterministic results; Tier-2 is agreement within a stated tolerance where results are not bit-for-bit deterministic. Both are defined so 'reproduces' has a precise meaning.</p>"),
       ("Why distinguish them?",
        "<p>Because honesty about what 'reproduces' means matters — some computations match exactly, others within tolerance, and Kronos states which is which.</p>")],
     # --- Comparisons & Context ---
     "why-now": [
       ("Why is now the right time for fusion?",
        "<p>High-temperature superconductors make compact high-field machines possible, the physics database is mature, and business models that earn before net-electric power lower the barrier to a first product.</p>"),
       ("Why is Kronos's timing different?",
        "<p>Because it does not wait for net-electric gain — the breeder's neutrons and isotopes give it a route to revenue now, with breeder construction slated for Q2 2027.</p>")],
     "fusion-vs-solar-wind": [
       ("Does fusion compete with solar and wind?",
        "<p>No — it complements them. Renewables provide cheap intermittent energy; fusion provides the firm, dispatchable power that fully decarbonising a grid still needs.</p>"),
       ("So where does fusion win?",
        "<p>On firmness and footprint — round-the-clock power at high density near the load, covering the hardest last part of decarbonisation rather than the easy part renewables already serve.</p>")],
     "fusion-vs-gas": [
       ("How does fusion compare with natural gas?",
        "<p>It targets the same firm, dispatchable role gas plays today — but without carbon emissions or fuel-price exposure, since its fuel is effectively unlimited hydrogen isotopes.</p>"),
       ("Can it really replace gas peaking?",
        "<p>A driven fusion machine is dispatchable in principle, combining baseload firmness with load-following — the combination that makes it a candidate to displace gas over time.</p>")],
     # --- Team & Heritage ---
     "the-scientific-approach": [
       ("What is the Kronos scientific approach?",
        "<p>Physics-based, frozen, reproducible design: fix a consistent point, publish the engines, state the gates, and let others check the work rather than trust claims.</p>"),
       ("How is it different from typical startup messaging?",
        "<p>It leads with what is not yet demonstrated — gates and caveats — because credibility built on reproducibility outlasts credibility built on hype.</p>")],
     "the-honesty-framework-in-practice": [
       ("What does honesty as an engineering principle mean?",
        f"<p>Stating limits plainly — low-neutron not aneutronic, requirement-class net power, not-yet-built, standard confinement not optimistic — so every strong claim (like Q = {F['b_Q']}) is believable.</p>"),
       ("Is this just marketing?",
        "<p>No — it is enforced in the work: a frozen canon, open deposits anyone can re-run, and named gates. The discipline is checkable, not a slogan.</p>")],
     # --- Open Science & Publications ---
     "open-science-in-fusion": [
       ("What does open science mean at Kronos?",
        "<p>Publishing the actual engines, inputs and expected outputs — not just conclusions — as open Zenodo deposits under CC BY 4.0, so anyone can reproduce the results.</p>"),
       ("Why is that unusual in fusion?",
        "<p>Because much of the field shares results but not the means to check them. Letting skeptics re-run your numbers is a deliberate, durable credibility strategy.</p>")],
     "how-to-cite": [
       ("How do I cite Kronos's work?",
        f"<p>Cite the relevant Zenodo deposit by DOI — breeder {F['doi_b']} (v2 {F['doi_b2']}), burner {F['doi_u']}, REBCO magnets {F['doi_rebco']}, direct conversion {F['doi_dec']}, and the AI/quantum record {F['doi_ai']} — each under CC BY 4.0.</p>"),
       ("Can I reuse the figures and engines?",
        "<p>Yes — CC BY 4.0 permits reuse with attribution, which is the point of publishing them openly.</p>")],
    }
    for slug, faq in Q.items():
        if faq and faq[0][0] != "x":
            enrich(slug, faq=faq)
