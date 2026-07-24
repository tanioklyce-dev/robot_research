---
title: Drosophila melanogaster
type: entity
subtype: model-organism
created: 2026-05-08
updated: 2026-05-10
sources: 6
tags: [drosophila, fruit-fly, model-organism, neuroscience, biomechanics]
---

***Drosophila melanogaster*** — the common fruit fly. The dominant invertebrate model organism in modern neuroscience and the substrate for both the [FlyWire connectome](flywire.md) (~139k neurons, ~50M synapses) and the [flybody](flybody.md) whole-body physics simulator. Adult body: ~3 mm long, six legs, two wings, two compound eyes.

## Why it's the canonical "whole-organism AI" target

- **Tractable scale.** Brain is small enough to map at synaptic resolution (FlyWire, October 2024) — orders of magnitude smaller than mouse (~70M neurons) or human (~86B), yet capable of vision, learning, foraging, courtship, navigation.
- **Rich behavioural repertoire.** Walking, flight (saccades, evasion, hovering, looming-response), grooming, courtship, feeding — all in a body small enough to simulate in real time on a laptop.
- **Genetic toolkit.** Decades of GAL4/UAS, optogenetics, and trans-Tango lines for circuit dissection.
- **Aerodynamic interest.** Wing-beat frequency ~218 Hz, naturalistic high-G saccades — non-trivial fluid dynamics as part of the body simulation problem.

## Position in this wiki

The wiki cares about *Drosophila* not as biology per se but as **the smallest organism for which both a connectome and a whole-body physics sim now exist** — i.e., the smallest viable target for "whole-organism agentic AI." See [Whole-organism agentic AI](../syntheses/agents/whole-organism-agentic-ai.md).

## Related

- [FlyWire](flywire.md) — adult brain connectome.
- [flybody](flybody.md) — whole-body physics simulator.
- [NeuroMechFly](neuromechfly.md) — earlier walking-focused body sim.
- [Connectome](../concepts/bio/connectome.md) — concept page.

## Mentioned in

- [Berkeley News — researchers simulate an entire fly brain on a laptop](../sources/berkeley-fly-brain-news.md)
- [flybody Paper](../sources/flybody-paper.md)
- [flybody GitHub](../sources/flybody-github.md)
- [Shiu et al. 2024 — A Drosophila computational brain model](../sources/shiu-fly-brain-paper.md)
- [Lappalainen et al. 2024 — Connectome-constrained networks (fly visual system)](../sources/lappalainen-flyvis-paper.md)
- [flygym GitHub (NeLy-EPFL/flygym)](../sources/flygym-github.md)
- [neuromechfly.org website](../sources/neuromechfly-website.md)
