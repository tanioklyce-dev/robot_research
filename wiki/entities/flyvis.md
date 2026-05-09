---
title: flyvis (TuragaLab/flyvis)
type: entity
subtype: code-repository
created: 2026-05-08
updated: 2026-05-08
sources: 1
license: MIT
url: https://github.com/TuragaLab/flyvis
docs: https://turagalab.github.io/flyvis/
tags: [fly-visual-system, connectome-constrained, deep-learning, pytorch, hexagonal-cnn, drosophila, hhmi-janelia, open-source, mit-license]
---

**`TuragaLab/flyvis`** — Open-source PyTorch library accompanying [Lappalainen et al. 2024 *Nature*](../sources/lappalainen-flyvis-paper.md). Implements a **connectome-constrained deep mechanistic network (DMN)** of the *Drosophila* visual system: 64 cell types, 45,669 neurons, ~1.5M synaptic connections, arranged on a hexagonal lattice covering the central visual field. **MIT-licensed.** Maintained by the **Turaga lab** at HHMI Janelia — the same lab that produced [flybody](flybody.md).

Repo description: *"A connectome-constrained deep mechanistic network (DMN) model of the fruit fly visual system in PyTorch."*

## What it is

- A deep neural network whose **connectivity is fixed by the EM connectome** (FIB-25 + FIB-19 reconstructions of the optic lobe). Signs and per-type synapse counts are non-trainable.
- 734 free parameters are learned by gradient descent: 65 resting potentials, 65 membrane time constants, 604 unitary synapse scaling factors.
- Training task: **optic-flow estimation on naturalistic video** (Sintel film), via a 2-layer convolutional decoder reading off medulla activity.
- No neural recordings used during training. The model nevertheless predicts ON/OFF channel separation, T4/T5 motion-direction selectivity, and matches recordings from 26 prior experimental studies.

## Repository contents

- **Seven numbered tutorial notebooks** covering: connectome exploration, optic-flow task training, flash and moving-edge responses, ensemble clustering and analysis, maximally excitatory stimuli generation, custom stimulus provision. Available as both rendered docs and **Google Colab** notebooks.
- **Pretrained models** distributed for "try pretrained models on your data" usage — a meaningful difference from many connectome papers where the released code requires retraining from scratch.
- Ensemble-of-models machinery — many models trained from random inits, analyses operate on the distribution.
- Documentation site: [turagalab.github.io/flyvis](https://turagalab.github.io/flyvis/).

## Activity / health (as of 2026-05-08)

- **Latest release: v1.1.3 (2026-03-07).** Actively maintained ~16 months after the *Nature* publication.
- ~65% Python / ~35% Jupyter.

## Architectural shape

- **Hexagonal CNN** layer matches the optic lobe's hexagonal columnar structure (721 columns covering the central visual field).
- One electrical compartment per neuron, except CT1 (per-column compartments — wide-field morphology).
- Threshold-linear leaky integrator dynamics; graded-release chemical synapses approximated by a threshold-linear function of presynaptic voltage.
- Brain region scope: **retina → lamina → medulla → lobula + lobula plate**. Visual system only — no central brain, no motor output.

## Why it matters here

- **The brain-side controller template** for whole-organism agentic AI. If you wanted to put a connectome-constrained controller inside [flybody](flybody.md), flyvis is the existing engineering pattern: deep net + connectome mask + task objective + ensemble.
- **Same lab as flybody.** Srinivas Turaga is senior on both flyvis (brain side, 2024) and flybody (body side, 2025). The integration the [whole-organism synthesis](../syntheses/whole-organism-agentic-ai.md) identifies as "open" sits inside one PI's research program — not across institutions.
- **One of two paradigms** for using a connectome computationally — the *connectome-constrained deep learning* path. Companion is mechanistic LIF ([Drosophila brain model](drosophila-brain-model.md)). See [Connectome](../concepts/connectome.md).
- **Visual system only.** A whole-brain version (using the FlyWire connectome) is the obvious next step but is not done in this codebase.

## Related

- [Lappalainen et al. 2024 — Connectome-constrained networks (fly visual system)](../sources/lappalainen-flyvis-paper.md) — the paper.
- [HHMI Janelia](hhmi-janelia.md) — host institution (Turaga lab).
- [flybody](flybody.md) — sister project from the same lab; body-side complement.
- [Drosophila brain model (philshiu)](drosophila-brain-model.md) — sister project from a different group; mechanistic-LIF paradigm.
- [FlyWire](flywire.md) — *not* the connectome flyvis trains on (it predates whole-brain FlyWire and uses optic-lobe FIB-25/FIB-19); the architectural template generalizes.
- [Connectome](../concepts/connectome.md) — concept.
- [Whole-organism agentic AI](../syntheses/whole-organism-agentic-ai.md) — synthesis.

## Mentioned in

- [Lappalainen et al. 2024 — Connectome-constrained networks (fly visual system)](../sources/lappalainen-flyvis-paper.md)
