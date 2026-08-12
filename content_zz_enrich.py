# -*- coding: utf-8 -*-
"""Deepen cornerstone pages with extra sections + per-page FAQs. Runs LAST (enrich hook)."""

def register(cat, page, F, enrich):

    enrich("the-breeder-design-point",
      add_body=[
       ('h2',"How the numbers fit together"),
       ('p',f"HYPERION's point is internally consistent, not a wish-list. The {F['b_Pfus']} of fusion power comes from a {F['b_Ti']} plasma at density set by the operating window, confined for {F['b_tauE']} at standard H-mode quality (H<sub>98</sub> = {F['b_H98']}). That confinement, against {F['b_Paux']} of auxiliary heating, is what yields Q = {F['b_Q']}. The {F['b_Ip']} of current is split into a {F['b_fbs']} self-driven bootstrap fraction plus externally driven current — the balance that makes steady-state operation credible."),
       ('p',f"The magnetics close the loop: an {F['b_B0']} on-axis field rising to {F['b_Bpeak']} at the REBCO conductor, in an {F['b_R0']} major-radius machine at aspect ratio {F['b_A']}, elongation {F['b_kappa']} and negative triangularity {F['b_delta']}. The result is a compact, high-beta (&beta;<sub>N</sub> = {F['b_bN']}) neutron source rather than a large one."),
       ('gap',("What is assumed vs demonstrated",f"The point assumes standard H-mode confinement (H<sub>98</sub> = {F['b_H98']}) and a high divertor radiated fraction — both within the experimental database, both named as gates rather than claimed as demonstrated.")),
      ],
      faq=[
       ("What is HYPERION's fusion gain?", f"<p>Q = {F['b_Q']} — {F['b_Pfus']} of fusion power against {F['b_Paux']} of auxiliary heating. This is a driven, steady-state figure, not ignition.</p>"),
       ("Is the breeder meant to produce electricity?", "<p>No. Its products are neutrons, tritium and helium-3. Its commercial value does not depend on net-electric fusion, which is the point of building it first.</p>"),
       ("Where can I reproduce these numbers?", f"<p>The full breeder deposit is open on Zenodo (DOI {F['doi_b']}, v2 {F['doi_b2']}) under CC&nbsp;BY&nbsp;4.0 — download the engine and re-run it.</p>"),
      ])

    enrich("the-burner-design-point",
      add_body=[
       ('h2',"Why the burner scales by length"),
       ('p',f"The burner's headline figures — engineering gain Q<sub>E</sub> = {F['u_QE']} and neutron fraction {F['u_fn']} — are largely independent of the central cell's length, because they are set by the plasma's local physics, not the machine's size. That is what lets one physics core serve three products: {F['u_ref_len']} delivering {F['u_ref_net']}, {F['u_aeg_len']} delivering {F['u_aeg_net']}, and {F['u_mv_len']} delivering {F['u_mv_net']}. Longer machines simply produce proportionally more net power."),
       ('p',f"The point runs D–&sup3;He at {F['u_Ti']} ion temperature (electrons {F['u_Te']}), density {F['u_ne']}, &sup3;He fraction {F['u_x']}, central beta {F['u_beta']} and central-cell radius {F['u_ac']}. The escaping charged particles are recovered by direct energy conversion at {F['u_dec']} efficiency — no steam cycle."),
       ('gap',("The binding condition",f"Every net-power figure here is contingent on the plug reaching a plug-to-central density ratio near {F['u_np']}. Kronos labels the burner's net power requirement-class for exactly this reason.")),
      ],
      faq=[
       ("What is the burner's engineering gain?", f"<p>Q<sub>E</sub> = {F['u_QE']} at a neutron fraction of {F['u_fn']} — low-neutron, not aneutronic. It is a requirement-class figure contingent on the plug-density condition.</p>"),
       ("How does one design serve three products?", f"<p>Gain and neutron fraction are length-independent, so the same physics core is packaged at {F['u_ref_len']}, {F['u_aeg_len']} (AEGIS) and {F['u_mv_len']} (MetroVolt) to hit different power classes.</p>"),
      ])

    enrich("plug-density-requirement",
      add_body=[
       ('h2',"Why the ratio has to be so high"),
       ('p',f"The ambipolar potential that plugs a tandem mirror scales with the logarithm of the plug-to-central density ratio and with the plug electron temperature. To confine central-cell ions deeply enough for net power, the Kronos burner needs a ratio near n<sub>p</sub>/n<sub>c</sub> = {F['u_np']}. At a substantially lower ratio the potential is too shallow, ions leak, and the machine does not close — its engineering gain becomes undefined."),
       ('h2',"How it gets retired"),
       ('p',"The gate is closed by a dedicated plug demonstration: a mirror experiment that establishes the required density ratio with sloshing-ion and thermal-barrier techniques. Until that demonstration succeeds, Kronos presents the burner's net power as a target defined by the validation suite, not a measured result — and the breeder's value stands independently of it."),
      ],
      faq=[
       ("Why is the burner's net power 'requirement-class'?", f"<p>Because it depends on reaching a plug-to-central density ratio of about {F['u_np']}. That is a physics requirement to be demonstrated, so Kronos labels the result a target rather than an achievement.</p>"),
       ("What happens if the ratio can't be reached?", "<p>The burner does not close as a net-electric machine at the design point. The breeder's products — tritium, neutrons, isotopes — do not depend on it, which is why Kronos builds the breeder first.</p>"),
      ])

    enrich("fusion-gain-q",
      faq=[
       ("What is the difference between Q and Q_E?", f"<p>Q is plasma gain (fusion power ÷ heating power); HYPERION's is {F['b_Q']}. Q<sub>E</sub> is plant-level engineering gain (net electricity ÷ all plant power); the burner's is {F['u_QE']}. Kronos reports both separately and never lets a high plasma Q stand in for net electricity.</p>"),
       ("Does Kronos claim ignition?", "<p>No. Both machines are driven — continuously heated — and quote finite gain with the heating power stated. That is a complete, checkable claim.</p>"),
      ])

    enrich("the-breeder-first-strategy",
      add_body=[
       ('h2',"Why this de-risks the whole company"),
       ('p',"Most fusion ventures carry a single, binary risk: reach net electricity or fail. Kronos splits that risk. The breeder's neutron-and-isotope business can generate value on the strength of a neutron source alone — a far lower bar than net-electric fusion — while the burner's harder physics matures in parallel. Early revenue is decoupled from the field's longest-pole milestone."),
       ('gap',("The honest wedge","Kronos sells materials, not (yet) electricity — so its economics do not wait on first achieving net-electric gain. That inversion of the usual fusion risk is the core of the strategy.")),
      ],
      faq=[
       ("Why build the breeder before the burner?", "<p>The breeder has a saleable product — tritium, neutrons, isotopes, helium-3 — that does not require solving net-electric fusion. Building it first creates value and de-risks the harder burner.</p>"),
       ("What does 'fuel follows purpose' mean?", "<p>Each machine is optimised for a different fuel because it does a different job: the breeder uses neutron-rich D–T to make fuel and neutrons; the burner uses low-neutron D–&sup3;He to make clean electricity.</p>"),
      ])

    enrich("direct-energy-conversion",
      add_body=[
       ('h2',"Why it beats a steam cycle"),
       ('p',f"A thermal plant is bounded by the Carnot limit: it turns heat into electricity at an efficiency set by its temperatures, typically 30–40%. Direct conversion sidesteps that ceiling entirely by decelerating charged particles against an electric field, recovering their kinetic energy as current at about {F['u_dec']}. It only works when most of the fusion energy is in charged particles — which is precisely why the burner uses low-neutron D–&sup3;He."),
      ],
      faq=[
       ("How efficient is direct conversion?", f"<p>About {F['u_dec']} — well above a Carnot-limited steam cycle, because it never converts the energy to heat first.</p>"),
       ("Why can't a D–T machine use it?", "<p>Because ~80% of D–T energy is in neutrons, which are uncharged and cannot be decelerated electrostatically. Direct conversion needs a charged-particle-dominated fuel like D–&sup3;He.</p>"),
      ])

    enrich("superconducting-magnets",
      faq=[
       ("What field do Kronos's magnets reach?", f"<p>{F['b_Bpeak']} at the conductor in the breeder, and {F['u_Bplug']} in the burner's high-field plug — fields only high-temperature (REBCO) superconductors can sustain continuously.</p>"),
       ("What is the biggest magnet risk?", "<p>Cyclic fatigue of the high-field plug coil. It is sound under static load but cyclic fatigue at full field is a named engineering gate, closed by a powered magnet test coil.</p>"),
      ])

    enrich("the-neutron-economy",
      add_body=[
       ('h2',"Turning a shielding problem into a product"),
       ('p',f"In a conventional D–T reactor, {F['b_Pn']} of neutron power is mostly a materials and shielding burden. Kronos inverts that: the neutrons breed tritium ({F['b_T']}/yr), co-produce helium-3 ({F['b_He3']}/yr), and can make medical and industrial isotopes. The neutron flux that others engineer against is, for the breeder, the product line."),
      ],
      faq=[
       ("What does the breeder actually sell?", f"<p>Neutron-derived products: tritium ({F['b_T']}/yr), helium-3, and potentially medical/industrial isotopes — all from its {F['b_Pn']} of neutron power.</p>"),
       ("Is helium-3 a revenue source?", f"<p>Its value is framed as strategic (quantum, medical, burner fuel), distinct from near-term revenue. The bankable near-term product is tritium.</p>"),
      ])

    enrich("reproducibility-overview",
      faq=[
       ("How do I verify a Kronos number myself?", f"<p>Download the relevant Zenodo deposit (breeder {F['doi_b']}, burner {F['doi_u']}), set up the pinned environment, and re-run the engine against the provided inputs. Deterministic results reproduce byte-for-byte; others within a stated tolerance.</p>"),
       ("Does reproducibility prove the machine will work?", "<p>No. It proves the number follows rigorously from the stated model and inputs. It does not prove an unbuilt machine will match the model — which is why every figure is labelled a computed design target.</p>"),
      ])

    enrich("honesty-framework",
      faq=[
       ("Why does Kronos state its own weaknesses?", "<p>Because serious diligence finds the caveats anyway. Stating them first — requirement-class burner, named gates, low-neutron-not-aneutronic — turns candour into credibility with labs and technical investors.</p>"),
       ("Does Kronos ever call its fusion aneutronic?", f"<p>No. The burner is low-neutron ({F['u_fn']}), not aneutronic. Kronos is deliberate about that distinction on every relevant page.</p>"),
      ])

    enrich("hyperion-breeder",
      faq=[
       ("What kind of machine is HYPERION?", f"<p>A compact spherical tokamak running D–T at Q = {F['b_Q']} / {F['b_Pfus']}, built to breed tritium and produce neutrons and helium-3 rather than grid electricity.</p>"),
       ("When does it start construction?", "<p>Construction of the HYPERION breeder is scheduled to begin in Q2 2027.</p>"),
      ])

    enrich("metrovolt",
      faq=[
       ("What scale is MetroVolt?", f"<p>The {F['u_mv_len']} burner housing, delivering {F['u_mv_net']} net ({F['u_mv_gw']} class) — sized for grid and hyperscale data-centre power.</p>"),
       ("Why is it suited to data centres?", f"<p>It is firm, clean, point-of-use power at large scale, and its low neutron fraction ({F['u_fn']}) eases siting nearer to load than a neutron-heavy plant.</p>"),
      ])

    enrich("aegis",
      faq=[
       ("What is AEGIS for?", f"<p>Resilient, independent, low-signature power for fixed defence installations — the {F['u_aeg_len']} burner housing at {F['u_aeg_net']} net. It is a fixed-installation product, not naval or mobile.</p>"),
      ])

    enrich("why-kronos-matters",
      faq=[
       ("What is different about Kronos in one sentence?", "<p>It matches fuel to purpose across two machines, earns from materials before net electricity, and publishes a fully open, reproducible record with every caveat in plain sight.</p>"),
      ])

    enrich("where-kronos-fits",
      faq=[
       ("How does Kronos compare to other fusion companies?", "<p>Most race one D–T tokamak to net electricity. Kronos is breeder-first and two-machine, with a saleable product before net electricity and an openly reproducible record — competing on staged, verifiable value rather than a single hero number.</p>"),
      ])

    enrich("spherical-tokamak",
      faq=[
       ("Why a spherical tokamak for the breeder?", f"<p>Low aspect ratio (A = {F['b_A']}) lets it hold high plasma pressure (&beta;<sub>N</sub> = {F['b_bN']}) for a given field, making a compact, economical neutron source. The trade is a tight central column.</p>"),
      ])

    enrich("tandem-mirror",
      faq=[
       ("Why a linear mirror instead of a tokamak for the burner?", f"<p>A tandem mirror cannot disrupt, its exhaust flows straight into a direct converter, and it scales by length. The price is end-plugging — the plug-density requirement (~{F['u_np']}).</p>"),
      ])

    enrich("negative-triangularity",
      faq=[
       ("Why does HYPERION use negative triangularity?", f"<p>Negative triangularity (&delta; = {F['b_delta']}) can suppress edge-localised modes while keeping good confinement — protecting the divertor without an added ELM-control system.</p>"),
      ])

    enrich("helium-3-supply",
      faq=[
       ("Does Kronos depend on lunar helium-3?", f"<p>No. The breeder co-produces about {F['b_He3']}/yr terrestrially. Lunar sourcing is a long-term option, not a dependency.</p>"),
      ])

    enrich("innovation-two-machine-architecture",
      faq=[
       ("Why two machines instead of one?", "<p>Because fuel should follow purpose. A breeder optimised for neutrons and tritium, plus a burner optimised for clean electricity, is simpler and better-suited than one do-it-all reactor — and lets materials revenue precede net electricity.</p>"),
      ])

    # --- Batch 2: FAQ blocks across more high-value pages (FAQ rich results + AI answers) ---
    B = {
     "ignition-vs-driven":[("Is a driven system worse than an igniting one?","<p>No — it is more controllable. A driven plasma responds when you turn the heating down; both can be net-positive. Kronos chooses driven operation deliberately.</p>")],
     "lawson-criterion":[("What is the triple product?","<p>Density &times; temperature &times; energy confinement time — the single figure of merit for fusion performance. Exceed a threshold and the plasma produces net power.</p>")],
     "compact-vs-conventional":[("Why go compact instead of large?","<p>High-temperature superconductors reach fields that let a small machine hit useful performance, trading size and cost for a tighter, higher-field core.</p>")],
     "inherent-safety":[("Can a Kronos machine melt down?","<p>No. There is no chain reaction and only seconds of fuel; any fault makes the plasma cool and stop. There is no meltdown pathway.</p>")],
     "fusion-waste":[("Does fusion make long-lived waste?","<p>No high-level waste — only activated structure, which low-activation materials keep short-lived, decaying to hands-on levels in decades.</p>")],
     "tritium-safety":[("Is tritium a showstopper?","<p>No — it is a handled hazard managed with low inventories, permeation barriers and monitoring. The breeder breeds its own, so supply is a feature.</p>")],
     "high-field-magnets":[("Why is high field the key to compact fusion?","<p>Machine size and cost fall steeply as field rises. REBCO lets Kronos reach 16.84 T (breeder) and 26.49 T (burner plug) continuously.</p>")],
     "rebco-tape":[("What is REBCO and why does it matter?","<p>A high-temperature superconducting tape that carries huge current at very high field — the material that makes compact, high-field fusion magnets possible.</p>")],
     "the-path-to-build":[("What has to happen before construction?","<p>Close the binding gates, run high-fidelity analysis, qualify materials and fabrication drawings, and demonstrate components. Construction of the breeder is scheduled to begin in Q2 2027, with detailed design proceeding in parallel.</p>")],
     "gate-reviews":[("What are the G1–G4 gates?","<p>Evidence-based go/no-go reviews: G1 physics freeze (done), then component demonstration, integrated prototype, and first product. Each has explicit criteria.</p>")],
     "kronos-vs-dt-tokamak":[("How is Kronos different from a normal fusion tokamak?","<p>Instead of one D–T tokamak racing to net electricity, Kronos uses a D–T breeder to make fuel and neutrons, and a low-neutron D–&sup3;He burner to make electricity by direct conversion.</p>")],
     "kronos-vs-iter":[("Is Kronos a smaller ITER?","<p>No — different architecture and business model. It stands on the same shared physics database ITER helped build, but takes a compact, breeder-first, commercially-staged path.</p>")],
     "fusion-vs-fission":[("Is fusion just like fission?","<p>No. Fusion has no chain reaction, no meltdown, no long-lived high-level waste and no bomb material. It stops the instant conditions falter.</p>")],
     "the-open-deposits":[("What is in the open deposits?","<p>The reduced-order engines, inputs and expected outputs for the breeder, burner, REBCO magnets, direct conversion, and the AI/quantum record — all CC BY 4.0 on Zenodo.</p>")],
     "how-to-reproduce":[("Can I re-run the physics myself?","<p>Yes. Download a deposit, set up the pinned environment, run the engine against the inputs, and compare to the expected outputs — byte-exact or within a stated tolerance.</p>")],
     "intellectual-property":[("What is open vs proprietary?","<p>The reproducible physics record is open; the proprietary build implementation is protected (one granted patent, more pending). The two are kept cleanly separate.</p>")],
     "direct-conversion-technology":[("What efficiency does direct conversion reach?","<p>About 0.70 — well above a Carnot-limited steam cycle, because charged-particle energy is recovered as electricity without being turned into heat first.</p>")],
     "the-simulation-stack":[("What runs the live browser solver?","<p>Kronos's actual deposited reduced-order engines — the same physics behind the papers — not a mock-up.</p>")],
     "grid-scale-power":[("What grid role does the burner fill?","<p>Firm, dispatchable, zero-carbon baseload — the scarce commodity in a renewable-heavy grid — via the MetroVolt housing.</p>")],
     "data-center-power":[("Why is fusion a fit for data centres?","<p>They need large, firm, clean power near load; the low-neutron burner can site closer to demand than a neutron-heavy plant.</p>")],
     "defense-power":[("What defence role does AEGIS serve?","<p>Resilient, independent, low-signature power for fixed defence installations — not naval or mobile.</p>")],
     "tritium-supply":[("Can Kronos supply tritium to others?","<p>Yes — the breeder breeds more than it burns (breeding ratio 1.8), positioning it as a potential supplier to the wider fusion ecosystem.</p>")],
     "medical-isotopes":[("Can fusion make medical isotopes?","<p>Yes — a high-flux neutron source can produce medical isotopes, giving the breeder an additional revenue path grounded in its neutron economy.</p>")],
     "the-three-approaches":[("What are the main fusion approaches?","<p>Magnetic confinement (tokamaks, stellarators, mirrors), inertial confinement (lasers), and hybrids. Kronos uses two magnetic forms: a spherical tokamak and a tandem mirror.</p>")],
     "how-to-compare-fusion":[("How should I compare fusion programmes?","<p>Ask whether the design actually closes, whether the quoted gain is scientific or plant-level, what the capital path is, and whether there is a product before net electricity.</p>")],
     "tandem-mirror-vs-tokamak":[("Why a mirror instead of a tokamak for the burner?","<p>It cannot disrupt, enables direct conversion, and scales by length — at the cost of end-plugging, the plug-density requirement.</p>")],
     "materials-qualification":[("Are the materials proven?","<p>Representative choices are stated; fabrication-grade qualification against ASTM/ASME is scheduled work, with magnet cyclic fatigue named as the binding gate.</p>")],
     "magnet-fatigue":[("What is the magnet fatigue gate?","<p>The high-field plug coil is sound statically but cyclic fatigue at full field is infeasible on today's assumptions — the burner's binding magnet gate, closed by a powered test coil.</p>")],
     "peer-review-track":[("Is the work peer-reviewed?","<p>The deposits are openly reproducible now; conventional peer review via arXiv and journals/IAEA is in preparation. The two are complementary.</p>")],
     "the-3d-model":[("Is the 3D model a real machine?","<p>No — it is a schematic, physics-grounded design instrument (stage one of model → shadow → digital twin), labelled as such. Construction of the breeder is scheduled for Q2 2027.</p>")],
     "no-proliferation":[("Does fusion create weapons material?","<p>No plutonium, no enriched uranium. Its fuels are hydrogen isotopes and helium-3, so fission's proliferation concerns do not arise in the same way.</p>")],
     "divertor":[("Why is the divertor so hard?","<p>It must exhaust concentrated heat without failing. HYPERION spreads the load with a high radiated fraction — an effective technique with a named performance gate.</p>")],
     "blanket":[("What does the breeding blanket do?","<p>It slows fusion neutrons to breed tritium from lithium and recovers their energy as heat, targeting a breeding ratio of 1.8 for fuel self-sufficiency.</p>")],
     "the-experience-behind-kronos":[("Who builds Kronos?","<p>Scientists and engineers whose careers span the world's major fusion and large-science programmes — decades of accumulated experience anchoring conservative assumptions to real databases.</p>")],
    }
    for slug, faqs in B.items():
        enrich(slug, faq=faqs)
