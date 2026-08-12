# -*- coding: utf-8 -*-
"""Diagnostics & measurement — how a plasma's state is measured."""

def register(cat, page, F):
    cat("diagnostics", "Diagnostics & Measurement",
        "How you measure a plasma hotter than the Sun's core without touching it — the "
        "instruments that turn a fusion machine into a scientific one.", 5.5)

    D = [
     ("plasma-diagnostics","Plasma Diagnostics Overview","You cannot put a thermometer in a 100-million-degree plasma; you measure it with light, waves and particles instead.",
      ["A fusion plasma is far too hot for any probe to touch, so its temperature, density, current and impurity content are inferred remotely — from the light it emits, the way it bends waves passed through it, and the particles and neutrons that escape. A modern machine carries dozens of such diagnostics, and Kronos's control and validation both lean on them."],
      ["thomson-scattering","interferometry","neutron-diagnostics"]),
     ("thomson-scattering","Thomson Scattering","Firing a laser through the plasma and reading the scattered light to measure temperature and density.",
      ["Thomson scattering shines a laser through the plasma; electrons scatter the light, and the Doppler broadening of the scattered spectrum gives the electron temperature while its intensity gives the density. It is the gold-standard local measurement of both."],
      ["plasma-diagnostics","electron-temperature","interferometry"]),
     ("interferometry","Interferometry","Measuring plasma density from how much it delays a probing beam.",
      ["A plasma slows electromagnetic waves in proportion to its density. By interfering a beam that has passed through the plasma with a reference beam, interferometry measures the line-integrated density continuously — a workhorse density diagnostic."],
      ["plasma-diagnostics","plasma-density","thomson-scattering"]),
     ("magnetic-diagnostics","Magnetic Diagnostics","Coils around the plasma that measure its current, position and shape.",
      ["Simple pickup coils and flux loops around the vessel sense the plasma's magnetic field, from which its current, position and shape are reconstructed in real time. They are the backbone of plasma control."],
      ["plasma-current","instrumentation-control","plasma-shaping"]),
     ("neutron-diagnostics","Neutron Diagnostics","Counting fusion neutrons to measure the fusion power directly.",
      [f"The rate of fusion neutrons is a direct measure of fusion power. Neutron detectors and cameras count and image them, giving an independent check on performance — especially meaningful on the neutron-rich breeder ({F['b_Pn']} of neutron power)."],
      ["the-neutron-economy","plasma-diagnostics","dt-fuel"]),
     ("spectroscopy","Plasma Spectroscopy","Reading the plasma's emitted light to find its impurities and temperature.",
      ["Every ion emits characteristic spectral lines. Spectroscopy reads that light to identify impurities, measure their density and infer ion temperature and rotation from line shapes — key to controlling impurities and Z_eff."],
      ["zeff","impurity-seeding","plasma-diagnostics"]),
     ("fiber-bragg-sensing","Fibre-Bragg Structural Sensing","Optical fibres that measure strain and temperature deep inside the magnet structure.",
      ["Fibre-Bragg gratings embedded in structure reflect a wavelength that shifts with strain and temperature, giving distributed structural and thermal telemetry from places no conventional sensor survives — relevant to magnet health monitoring."],
      ["magnet-fatigue","instrumentation-control","superconducting-magnets"]),
     ("bolometry","Bolometry","Mapping where the plasma radiates its power away.",
      ["Bolometers measure the total radiated power and its spatial distribution, essential for understanding the power balance and for divertor-protecting radiative scenarios."],
      ["radiated-power-fraction","bremsstrahlung","plasma-diagnostics"]),
    ]
    for slug,title,desc,paras,rel in D:
        page(slug,title,"diagnostics",desc,desc,[('p',p) for p in paras],related=rel,jtype="TechArticle")
