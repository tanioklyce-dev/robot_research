---
title: "Berkeley News — researchers simulate an entire fly brain on a laptop"
type: source
subtype: news-article
created: 2026-05-08
updated: 2026-05-08
url: https://news.berkeley.edu/2024/10/02/researchers-simulate-an-entire-fly-brain-on-a-laptop-is-a-human-brain-next/
author: UC Berkeley News
published: 2024-10-02
ingested: 2026-05-08
tags: [drosophila, connectome, fly-brain, flywire, leaky-integrate-and-fire, biological-ai]
---

## Summary

UC Berkeley News article (2024-10-02) reporting that Phil Shiu (then UC Berkeley postdoc, now at Eon) and collaborators built **a computer simulation of the entire adult fruit fly brain** — 139,255 neurons and ~50 million synaptic connections — by combining the [FlyWire](../entities/flywire.md) connectome with a leaky-integrate-and-fire dynamics model. The simulation predicted neural responses (e.g., proboscis extension when taste neurons are stimulated) that were then validated against real fly behaviour. The article frames the work as a stepping stone toward mouse and eventually human connectomes.

## Key claims

- **Scale.** 139,255 neurons, ~50M connections. Runs on a laptop.
- **Method.** "Leaky integrate-and-fire computational model" — neurons fire if they receive more positive than negative input. The Berkeley article does not name a specific software framework.
- **Validation.** The model "proved amazingly good at predicting how the real fly brain responds to stimuli" — including specific behaviours such as proboscis extension on taste-neuron activation.
- **Source data.** [FlyWire](../entities/flywire.md) connectome (FlyWire.ai) — output of an international consortium led by MRC Laboratory of Molecular Biology (Cambridge, UK), Princeton University, University of Vermont, University of Cambridge.
- **Funding.** NIH BRAIN Initiative, Wellcome, Medical Research Council, Princeton, NSF.
- **Roadmap.** Shiu: *"This really suggests that getting a mouse connectome, and eventually a human connectome, will be incredibly valuable."*
- **AI framing.** Article notes the model "may be useful in the field of AI and machine learning, which involve so-called neural networks" and discusses an *"alternate way of getting to really good AI."*

## Companion papers (mentioned but not directly linked in article)

- Shiu et al. *Nature* (2024) — *"A Drosophila computational brain model reveals sensorimotor processing"*
- Dorkenwald et al. *Nature* (2024) — *"Neuronal wiring diagram of an adult brain"* (the FlyWire connectome itself)
- Schlegel et al. *Nature* (2024) — *"Whole-brain annotation and multi-connectome cell typing of Drosophila"*

## Entities mentioned

- [FlyWire](../entities/flywire.md) — connectome consortium and dataset.
- [Drosophila melanogaster](../entities/drosophila.md) — model organism.
- [Phil Shiu](../entities/phil-shiu.md) — lead author; UC Berkeley → Eon Systems.
- [Drosophila brain model](../entities/drosophila-brain-model.md) — open-source code (the artifact behind the "fly brain on a laptop" framing).
- Gabriella Sterne (University of Rochester)
- Kristin Scott (UC Berkeley, professor emerita)

## Concepts touched

- [Connectome](../concepts/connectome.md) — complete wiring diagram of a nervous system.
- [Biomechanical simulation](../concepts/biomechanical-simulation.md) — companion thread (this work models the brain only, not the body).

## Open questions

- The Berkeley article doesn't name the simulation software or any code release. The Shiu et al. *Nature* paper itself would be the primary source for those details — TBD as a follow-up ingest.
- How accurate is "leaky integrate-and-fire" against real fly neural recordings? The article reports qualitative behavioural validation, not neuron-level RMSE.
- The article frames the work as brain-only. Pairing it with a body simulator like [flybody](../entities/flybody.md) is the natural whole-organism follow-up — see [Whole-organism agentic AI](../syntheses/whole-organism-agentic-ai.md).
