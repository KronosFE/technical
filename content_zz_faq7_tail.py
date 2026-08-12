# -*- coding: utf-8 -*-
"""FAQ coverage batch 7 — remaining Technical narrative pages."""
def register(cat, page, F, enrich):
    Q = {
     "the-safety-case": [
       ("What is fusion's basic safety case?",
        "<p>Safety is physics, not a bolted-on system: the plasma holds only seconds of fuel and depends on precisely maintained conditions, so any fault makes it cool and stop. There is no chain reaction, critical mass or stored energy to drive a runaway.</p>"),
       ("What are the real hazards Kronos manages?",
        f"<p>Tritium and activated structure, concentrated in the breeder — handled with low inventories, containment, monitoring and low-activation materials. The low-neutron burner ({F['u_fn']}) carries far less, and additionally has no disruptions.</p>")],
     "the-environmental-case": [
       ("What is fusion's environmental case?",
        "<p>No carbon emissions in operation, no long-lived high-level waste and no spent fuel — only structural metal made mildly radioactive by neutrons, kept short-lived by low-activation materials.</p>"),
       ("Does Kronos claim a finished environmental assessment?",
        "<p>No — it screens water, land, waste and carbon impacts by product and flags what remains to be computed, rather than publishing a polished number it cannot yet defend.</p>")],
     "spherical-tokamak-history": [
       ("How did the spherical tokamak develop?",
        f"<p>Experiments like NSTX and MAST showed that squeezing the aspect ratio down raises achievable beta and stability — the physics HYPERION uses at A = {F['b_A']} and &beta;<sub>N</sub> = {F['b_bN']}.</p>"),
       ("What held spherical tokamaks back?",
        "<p>The tight central column limits solenoid and magnet space, and high field was hard to reach there. High-temperature superconductors are what now make a compact, high-field spherical breeder practical.</p>")],
     "direct-conversion-history": [
       ("How old is the direct-conversion idea?",
        f"<p>Direct energy conversion — collecting charged-particle energy as electricity instead of heat — dates to mid-20th-century mirror research. The burner revives it, recovering energy at about {F['u_dec']}.</p>"),
       ("Why is it practical now?",
        f"<p>Because modern high-field magnets make the low-neutron D–&sup3;He burner viable, and its charged-particle energy is exactly what direct conversion captures — lifting plant efficiency to Q<sub>E</sub> = {F['u_QE']}.</p>")],
    }
    for slug, faq in Q.items():
        enrich(slug, faq=faq)
