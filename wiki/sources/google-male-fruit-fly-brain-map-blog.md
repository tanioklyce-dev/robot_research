---
title: "5 amazing visuals show how the male fruit fly's brain map is advancing neuroscience (Google, The Keyword)"
type: source
url: https://blog.google/innovation-and-ai/technology/research/male-fruit-fly-brain-map/
local_path: raw/2026-09-03-google-male-fruit-fly-brain-map.md
sha256: 9b581c72f99695d6be3f4b5681f853f23e965d0958334c93409a86c3356de35d
author: "Michał Januszewski, Viren Jain (Research Scientists, Google Research)"
affiliations: "Google Research (Connectomics); HHMI Janelia Research Campus and collaborators"
published: 2026-09-03
venue: "Google — The Keyword (corporate blog), Google Research category"
format: web (corporate blog listicle; five visuals lost, captions kept)
tags: [connectome, drosophila, male-cns, ventral-nerve-cord, hhmi-janelia, google-research, flywire, cell-types, sexual-dimorphism, sensorimotor, secondary-source]
ingested: 2026-09-12
---

# 5 amazing visuals show how the male fruit fly's brain map is advancing neuroscience

## Summary

Google's announcement, written by two of its connectomics leads, of the **first complete synaptic-resolution map of an adult *male* fruit fly's brain *and* ventral nerve cord** — the whole central nervous system — from a years-long HHMI Janelia + Google Research + community collaboration. **More than 166,000 neurons** and **11,691 cell types**, reconstructed by AI from millions of EM section images and classified with human proofreading. It builds on the **female whole-brain map ([FlyWire](../entities/flywire.md), 2024, 139,255 neurons, brain only)**; the additions that matter are the **sex** and the **nerve cord**.

For this wiki the nerve cord is the point. The existing fly-simulation line splits cleanly into a **brain-only** computational model ([Shiu et al.](shiu-fly-brain-paper.md), built on FlyWire) and a **body-only** biomechanical model ([flybody](flybody-paper.md)), with the VNC — where the motor neurons live — sourced from separate, differently-prepared animals. A single-animal brain-plus-VNC connectome closes that gap in principle: the post's own fifth visual traces a **visual-to-motor pathway** from R1–R6 photoreceptors through the male-specific LoVP92 *"love spot"* neurons to the DNg13 motor neuron.

> [!note] Secondary source. The primaries are the papers it points at.
> This is a corporate blog listicle with AI-generated summary blocks; it names **no paper, journal, or DOI** and links to a "Neural Mapping website," a Google Research Blog post, and *"three companion studies"* on visual systems, taste, and social behaviour. Per the wiki's [primary-source rule](../../CLAUDE.md), the numbers here (166k, 11,691) should be re-sourced from the connectome paper before they are quoted in anything load-bearing. The wiki's [FlyWire](../entities/flywire.md) page went through the same step for the female map.

## Key claims

- **Scale.** *"A record-breaking more than 166,000 neurons"* across brain and VNC — versus FlyWire's 139,255 for the female brain alone. The post does not separate brain from VNC counts, so the two are not directly comparable.
- **Cell types.** **11,691** neuron types in the male CNS; *"Computing and AI helped human experts classify more than 166,000 neurons."*
- **Method, as stated.** Thin sections of brain and body, each imaged, then *"computers and AI to combine millions of 2D images to create 3D neural shapes."* No algorithm is named; the authors are the Google Connectomics group behind flood-filling networks and [H01](h01-human-cortex-reconstruction.md), so that lineage is the likely one, but the post does not say so.
- **Sexual dimorphism, three classes.** Most neurons are **isomorphic** (same in both sexes); a minority are **sex-specific**; a third class is **dimorphic** — present in both sexes but wired to different partners. Worked example: paired **AOTU012** neurons (sensory/taste processing) exist in both sexes but connect to different neighbours in males vs females.
- **A complete sensorimotor pathway in one dataset.** R1–R6 visual neurons → intermediates including the male-specific **LoVP92** (courtship-related "love spot") → **DNg13** motor neuron. *"These connect the visual neurons… to motor neurons, which help it move in response."*
- **Three companion studies** released the same day: visual systems, taste, social behaviour.
- **Positioning.** *"A foundational resource for neuroscience for years to come"*; Google frames it as AI letting connectomics *"exponentially scale"* toward full vertebrate brains.

## Why it matters in this wiki

The [connectome](../concepts/bio/connectome.md) page lists two ways to use one for AI: as a **structural prior** for a network, and as the **substrate for a whole-organism simulation**. Every whole-fly effort so far has had to stitch a female brain connectome to VNC connectomes from other animals (MANC/FANC), and the [flybody](flybody-paper.md) authors listed brain-side integration as future work. A same-animal brain + VNC map is the first dataset on which a *"stimulus → central brain → motor neuron → muscle"* loop could be closed without cross-animal registration. Whether anyone does it is a different question — the [Shiu](shiu-fly-brain-paper.md) leaky-integrate-and-fire approach would need to scale ~20% in neuron count and add descending/VNC dynamics, and the male-specific circuits mean the two sexes are now two different simulation targets.

## Entities mentioned

- [HHMI Janelia](../entities/hhmi-janelia.md) — lead institution.
- [FlyWire](../entities/flywire.md) — the female whole-brain predecessor this map *"builds on."*
- [Drosophila melanogaster](../entities/drosophila.md) — the organism.
- Google Research Connectomics (Januszewski, Jain) — also behind [H01](h01-human-cortex-reconstruction.md); no entity page.

## Concepts touched

- [Connectome](../concepts/bio/connectome.md) — new concrete instance: first complete adult CNS (brain + VNC), male.
- [Biomechanical simulation](../concepts/bio/biomechanical-simulation.md) — the brain-side dataset flybody's roadmap was waiting for.

## Open questions

- **The primary papers** — journal, DOI, authors, and the brain-vs-VNC neuron split. Ingest before quoting.
- **Is the reconstruction FFN-based** and was proofreading community-scale as with FlyWire?
- **Is the dataset public** with the same tooling as FlyWire (neuroglancer, CAVE)? The post says "explore on the Neural Mapping website."
- **Muscle targets.** A connectome ends at motor neurons; does the VNC reconstruction annotate which muscles each innervates, which is what a flybody-style integration needs?
