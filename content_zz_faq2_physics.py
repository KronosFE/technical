# -*- coding: utf-8 -*-
"""FAQ coverage batch 2 — Physics & Fusion Science."""
def register(cat, page, F, enrich):
    Q = {
     "fusion-basics": [
       ("Why is fusion so hard to achieve?",
        "<p>Two positively charged nuclei repel, so they must be heated to tens or hundreds of millions of degrees and held together long enough to fuse. Doing that while getting more energy out than you put in is the whole challenge.</p>"),
       ("How does Kronos make fusion pay before that is solved?",
        f"<p>By selling the breeder's neutrons, tritium and helium-3 rather than waiting on net-electric power. HYPERION runs at plasma gain Q = {F['b_Q']} — net-positive plasma, driven and steady — with a business that does not depend on grid electricity.</p>")],
     "the-dt-reaction": [
       ("How is D–T's energy split?",
        "<p>Momentum conservation gives the light neutron 14.1 MeV and the helium nucleus 3.5 MeV. The neutron carries its energy out to breed tritium and deposit heat; the confined helium heats the plasma.</p>"),
       ("Why does Kronos embrace D–T's neutrons?",
        f"<p>Because in the breeder those neutrons are the product — they breed tritium and helium-3 and enable isotope production. Its {F['b_fn']} neutron fraction is a feature of a machine built to make fuel, not electricity.</p>")],
     "the-dhe3-reaction": [
       ("Why can D–&sup3;He energy be converted directly?",
        f"<p>Its 18.3 MeV is released almost entirely as charged particles, which can be decelerated and collected as electricity instead of boiling water. That is the basis of the burner's Q<sub>E</sub> = {F['u_QE']}.</p>"),
       ("Is D–&sup3;He aneutronic?",
        f"<p>No — side D–D reactions still emit some neutrons, giving a neutron fraction of {F['u_fn']}. Kronos calls the burner low-neutron, never aneutronic, which is a deliberate honesty choice.</p>")],
     "catalyzed-dd": [
       ("What is catalysed D–D?",
        "<p>Deuterium fusing with itself produces tritium and helium-3, which can then react further — a fuel cycle needing only deuterium. It avoids external tritium supply but demands even higher temperatures than D–&sup3;He.</p>"),
       ("Does Kronos use catalysed D–D?",
        "<p>It is relevant background physics, not a Kronos product fuel. The breeder runs D–T and the burner runs D–&sup3;He; catalysed D–D is discussed for completeness of the fuel-cycle picture.</p>")],
     "dt-fuel": [
       ("Why is D–T the easiest fusion fuel?",
        f"<p>It has the highest reactivity at the lowest temperature of any candidate fuel, which is why the breeder runs comparatively cool at {F['b_Ti']}. The trade is a high neutron yield and the need to breed tritium.</p>"),
       ("Where does the tritium come from?",
        f"<p>The breeder makes its own in the blanket at breeding ratio {F['b_TBR']}, about {F['b_T']} per year — turning the tritium-supply problem into a product line.</p>")],
     "d-he3-fuel": [
       ("Why does D–&sup3;He run so much hotter?",
        f"<p>Its reaction peaks at a higher energy than D–T, so the burner operates at about {F['u_Ti']} — far hotter and harder to confine. The payoff is charged-particle energy that direct conversion can capture.</p>"),
       ("Where does the helium-3 come from?",
        f"<p>The breeder co-produces about {F['b_He3']}/yr, giving Kronos an internal terrestrial supply of a genuinely scarce isotope rather than depending on lunar mining or reactor by-product.</p>")],
     "fusion-fuels-overview": [
       ("Why does Kronos use two different fuels?",
        f"<p>Fuel follows purpose. The breeder uses neutron-rich D–T to make fuel and isotopes; the burner uses low-neutron D–&sup3;He to make firm power via direct conversion. Each fuel is matched to what the machine sells.</p>"),
       ("Which fuel is 'best'?",
        "<p>There is no universal best — D–T is easiest but neutron-heavy; D–&sup3;He is cleaner but far harder to ignite and needs scarce helium-3. Kronos treats the choice as application-specific, not ideological.</p>")],
     "power-balance": [
       ("What is a plasma power balance?",
        "<p>It is the accounting of heating in versus losses out — conduction, radiation and particle loss — that determines whether a plasma sustains its temperature. Closing it is what defines a working operating point.</p>"),
       ("Does Kronos report net or gross power?",
        f"<p>Net. The burner's headline figures are net electricity after the plant's own consumption, and it labels net power requirement-class because it depends on the plug reaching a density ratio near {F['u_np']}.</p>")],
     "radiation-balance": [
       ("Why does radiation matter to the power balance?",
        "<p>Bremsstrahlung and line radiation drain energy from the plasma, setting a floor on the temperature a given fuel needs to stay net-positive. It matters most for the hot, purity-sensitive D–&sup3;He burner.</p>"),
       ("How does the burner manage radiation loss?",
        "<p>With a clean plasma and a reflective liner that returns radiation to the plasma, improving the balance. The liner's reflectivity trades against its neutron activation, which Kronos flags openly.</p>")],
     "plasma-pressure": [
       ("What sets a plasma's power density?",
        f"<p>Pressure — the product of density and temperature. Fusion power scales roughly with pressure squared, and how much pressure a magnet can hold is measured by beta. HYPERION runs at &beta;<sub>N</sub> = {F['b_bN']}.</p>"),
       ("Why is high beta valuable?",
        "<p>More plasma pressure per tesla of field means a cheaper machine for a given output. Kronos's low-aspect-ratio breeder is chosen partly because spherical tokamaks naturally reach high beta.</p>")],
     "plasma-equilibrium": [
       ("What is plasma equilibrium?",
        "<p>It is the balance where the plasma's outward pressure is held by the magnetic field's inward force, giving a stable shape and position. The control system holds this equilibrium continuously.</p>"),
       ("How is equilibrium held in real time?",
        "<p>Magnetic sensors reconstruct the plasma's position and shape, and the poloidal-field coils are driven to correct it within milliseconds — the core of vertical and shape control.</p>")],
     "plasma-edge-physics": [("x","x")],
     "edge-physics": [
       ("Why is the plasma edge so important?",
        "<p>The narrow edge region sets how much heat concentrates on the divertor and, through the H-mode pedestal, strongly influences the whole plasma's performance. Small edge changes have large global effects.</p>"),
       ("How does negative triangularity help the edge?",
        f"<p>HYPERION's negative triangularity (&delta; = {F['b_delta']}) can suppress edge-localised modes while keeping good confinement — a deliberate choice to tame the edge without violent ELM bursts.</p>")],
     "power-exhaust": [
       ("Why is power exhaust one of fusion's hardest problems?",
        "<p>All the exhaust power funnels toward a small divertor area, where it can exceed what any material survives. Getting the power out without destroying the components it flows through is a genuine engineering limit.</p>"),
       ("How does HYPERION handle it?",
        "<p>By radiating most of the exhaust power before it reaches the targets, spreading it over the whole wall. Achieving that high radiated fraction while keeping the core clean is a named performance gate.</p>")],
     "power-exhaust-x": [("x","x")],
     "neutronics": [
       ("What is neutronics?",
        f"<p>The study of how fusion neutrons travel, breed tritium, deposit heat and damage materials. It is the breeder's central discipline, driving the blanket, shielding and the {F['b_wall']} first-wall load.</p>"),
       ("Are these neutronics results high-fidelity?",
        "<p>Kronos's public figures come from reduced-order engines; full Monte-Carlo (MCNP-class) neutronics is named as detailed-design work on the path to build, not claimed as already complete.</p>")],
     "impurity-transport": [
       ("Why does impurity transport matter?",
        f"<p>Heavy impurities radiate strongly and dilute the fuel, so where they accumulate decides how clean the core stays. HYPERION is designed to a clean Z<sub>eff</sub> of {F['b_Zeff']}.</p>"),
       ("How are impurities controlled?",
        "<p>Through wall conditioning, controlled edge seeding for divertor protection, and good exhaust — balancing enough edge radiation against core contamination as an active control problem.</p>")],
     "helium-transport": [
       ("Why must helium ash be removed?",
        "<p>The helium produced by fusion dilutes the fuel and cools the plasma if it builds up, so it must be transported to the edge and pumped out. Ash removal efficiency sets a practical ceiling on sustainable fusion power.</p>"),
       ("What removes the ash?",
        "<p>The divertor and cryopumps on the breeder, and the end tanks on the burner — which is why those exhaust systems are performance-critical, not merely protective.</p>")],
     "startup-physics": [
       ("What happens during plasma start-up?",
        "<p>A discharge goes from gas breakdown through current ramp-up to the steady flat-top where fusion conditions are held, all while keeping the current and density profiles stable within the flux budget.</p>"),
       ("Is start-up harder in a compact machine?",
        "<p>Yes — the slim central column leaves little room for the solenoid, so robust, partly non-inductive start-up is a real design requirement Kronos treats as part of proving operability.</p>")],
     "current-diffusion": [
       ("What is current diffusion?",
        "<p>The plasma current profile relaxes resistively over time, reshaping the safety-factor profile that governs stability. Because it evolves slowly, current-profile control must be applied across the whole discharge.</p>"),
       ("Why does the current profile matter?",
        "<p>It sets where dangerous tearing modes can grow and enables advanced regimes. Tailoring it with heating and current drive is a primary tool for stability and steady-state performance.</p>")],
     "steady-state-operation": [
       ("What does steady-state operation require?",
        f"<p>Sustaining the plasma indefinitely rather than in pulses. For the breeder that means holding {F['b_Ip']} of current by combining the {F['b_fbs']} bootstrap fraction with efficient external drive.</p>"),
       ("Is the burner steady-state?",
        "<p>Yes, naturally — being continuously driven by its heating, it runs steadily by design, one of the linear architecture's simplifications over a pulsed tokamak.</p>")],
     "disruption-physics": [
       ("What is a disruption?",
        "<p>A sudden loss of confinement in a tokamak that dumps the plasma's energy and current, producing intense heat loads, mechanical forces and possible runaway electrons. It is a defining tokamak failure mode.</p>"),
       ("Does the burner disrupt?",
        "<p>No — the linear tandem-mirror burner has no plasma current to disrupt, so it avoids this failure mode entirely. That is one of its architectural safety advantages over the breeder.</p>")],
     "mirror-confinement-physics": [
       ("How does a magnetic mirror confine plasma?",
        "<p>A straight field that is stronger at its ends reflects particles back toward the centre. Simple mirrors leak through a loss cone; the tandem configuration adds end plugs and an electrostatic barrier to plug that leak.</p>"),
       ("Why revive mirrors now?",
        f"<p>Modern high-field REBCO magnets make the required plug fields ({F['u_Bplug']}) attainable, and direct conversion suits the linear geometry — reviving a concept whose physics was well understood but whose magnets were not previously available.</p>")],
     "ambipolar-physics": [
       ("What is ambipolar confinement?",
        f"<p>An electrostatic potential, set up by the plasma's own tendency to stay quasineutral, holds the ions in the burner's central cell. Building a deep enough potential is what plugs the mirror's ends.</p>"),
       ("What is the catch?",
        f"<p>The potential depth depends on the plug reaching a density about {F['u_np']} times the central cell. That plug-density requirement is the burner's single most important open condition, which Kronos names openly.</p>")],
     "end-loss-and-plugging": [
       ("What is end loss in a mirror?",
        "<p>Particles whose velocity falls in the loss cone escape out the ends of a mirror, the fundamental leak of the simple configuration. Controlling it is the central problem of mirror confinement.</p>"),
       ("How does the burner plug the ends?",
        f"<p>With high-field plug coils and an ambipolar electrostatic potential that reflects escaping ions. The plugging effectiveness hinges on the ~{F['u_np']} plug-density ratio, the burner's binding physics condition.</p>")],
     "centre-column-challenge": [
       ("What is the centre-column challenge?",
        "<p>A spherical tokamak squeezes the doughnut's hole nearly shut, leaving very little room in the central column for the solenoid, conductor and shielding — all of which compete for the same scarce space.</p>"),
       ("Why accept it?",
        f"<p>Because low aspect ratio (A = {F['b_A']}) buys high beta and compactness. The tight, highly-loaded centre column is the defining engineering trade Kronos accepts to get a small, high-performance breeder.</p>")],
    }
    for slug, faq in Q.items():
        if faq and faq[0][0] != "x":
            enrich(slug, faq=faq)
