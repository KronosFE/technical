# -*- coding: utf-8 -*-
"""Inject real paper figures onto cornerstone Technical Library pages (enrich hook, runs last)."""
def register(cat, page, F, enrich):
    FIG = {
      "the-breeder-design-point": [
        ("breeder-cutaway.png", "HYPERION breeder — cutaway of the compact spherical-tokamak core."),
        ("breeder-radial-build.png", "Radial build: plasma, first wall, breeding blanket, shield, and high-field magnet.")],
      "radial-build": [
        ("breeder-radial-build.png", "The HYPERION radial build, layer by layer from plasma to magnet.")],
      "the-neutron-economy": [
        ("breeder-he3-yield.png", "Net helium-3 yield — the breeder's strategic co-product.")],
      "power-exhaust": [
        ("breeder-exhaust.png", "Divertor exhaust and the high-radiated-fraction strategy.")],
      "fuel-cycle": [
        ("breeder-fuel-cycle.png", "The closed tritium fuel cycle: breed, extract, purify, re-inject.")],
      "the-burner-design-point": [
        ("burner-axial-layout.png", "The D–&sup3;He tandem-mirror generator — axial layout, end to end."),
        ("burner-power-balance.png", "Engineering power balance of the tandem-mirror generator."),
        ("burner-synchrotron.png", "Synchrotron effective-harmonic cutoff scales with machine size.")],
      "tandem-mirror": [
        ("burner-axial-layout.png", "Tandem-mirror axial layout: central cell, high-field plugs, expanders.")],
      "power-conversion": [
        ("burner-conversion-train.png", "The direct-energy-conversion train.")],
      "the-dec-record": [
        ("dec-abstract.png", "Direct energy conversion — graphical overview."),
        ("dec-qe-closure.png", "Q<sub>E</sub> closure for the direct-conversion generator.")],
      "the-rebco-record": [
        ("rebco-field-ladder.png", "REBCO field ladder — what the conductor enables vs. what a coil realises."),
        ("rebco-bore-stress.png", "Bore-resolved structural stress in the high-field winding.")],
      "magnet-system": [
        ("rebco-field-ladder.png", "The high-field REBCO magnet system across both machines.")],
      "the-ai-quantum-record": [
        ("ai-blueprint.png", "The AI-native, certifiable real-time control blueprint.")],
    }
    def block(fn, cap):
        return ('<figure class="techfig">'
                f'<img src="./figures/{fn}" alt="{cap}" loading="lazy">'
                f'<figcaption>{cap}</figcaption></figure>')
    for slug, figs in FIG.items():
        enrich(slug, add_body=[('html', "".join(block(fn, cap) for fn, cap in figs))])
