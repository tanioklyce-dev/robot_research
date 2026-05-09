---
title: Connectome
type: concept
created: 2026-05-08
updated: 2026-05-08
sources: 1
tags: [connectome, neuroscience, brain-mapping, biological-ai, drosophila]
---

A **connectome** is a complete wiring diagram of a nervous system — every neuron and every synaptic connection between them, mapped at synaptic resolution. The term parallels "genome" (complete sequence of an organism's DNA): a connectome is the complete circuit-level description of an animal's brain.

## Concrete instances

- ***C. elegans*** (302 neurons, ~7,000 synapses) — first complete connectome (White et al. 1986).
- ***Drosophila* hemibrain** (~25k neurons) — Janelia 2020. Half-brain at synaptic resolution.
- ***Drosophila* MANC / FANC** — male/female adult ventral nerve cord, 2024.
- ***Drosophila* whole brain** — [FlyWire](../entities/flywire.md), October 2024. **139,255 neurons, ~50M synapses.** First complete adult-brain connectome of any organism.
- **Mouse and human** — current frontier targets, multiple orders of magnitude harder (~70M neurons in mouse, ~86B in human). Berkeley News' Phil Shiu names mouse as the next stop and human as the long-term ambition ([Berkeley News](../sources/berkeley-fly-brain-news.md)).

## Two ways to use a connectome for AI

### 1. Connectome → simulation (Shiu et al. 2024)

Take the wiring + a neuron-dynamics model (e.g., leaky integrate-and-fire) and run a physical simulation of the brain. The Berkeley team did this for the fly brain on a laptop and matched real fly behavioural responses (proboscis extension on taste-neuron stimulation).

**Strengths:** mechanistic; predicts neuron-level activity.
**Weaknesses:** dynamics model is heuristic (LIF); doesn't yet incorporate neuromodulators, glia, plasticity.

### 2. Connectome-constrained deep learning (Lappalainen et al. 2024, Mi et al. 2022)

Train a deep neural network whose connectivity matrix is *masked* by the biological wiring — the connectome constrains which weights can be non-zero. Then fit the unmasked weights to neural activity recordings.

- **Lappalainen et al. 2024** (*Nature* 634:1132–1140) — predicts fly visual-system neural activity at single-neuron resolution, using a connectome-constrained deep net.
- **Mi et al. 2022** (ICLR) — connectome-constrained latent-variable model of whole-brain neural activity.

**Strengths:** scales to deep-learning training pipelines; generalizes across stimuli.
**Weaknesses:** abstracts away biophysical detail (no spikes, no synaptic dynamics).

## Why it matters here

Connectomes are the **brain side** of the whole-organism agentic-AI program (the [flybody](../entities/flybody.md) family is the body side). The Vaxenburg et al. flybody paper explicitly names the combination as the long-term target: *"combining our whole-body model with a complete nervous system connectome … could enable the development of whole-animal models of the entire body and nervous system of the adult fruit fly."*

## Related

- [FlyWire](../entities/flywire.md) — the *Drosophila* connectome dataset.
- [flybody](../entities/flybody.md) — body-side complement.
- [Drosophila melanogaster](../entities/drosophila.md) — model organism for whole-organism AI.
- [Biomechanical simulation](biomechanical-simulation.md) — companion concept.
- [Whole-organism agentic AI](../syntheses/whole-organism-agentic-ai.md) — synthesis tying connectome + body sim together.

## Mentioned in

- [Berkeley News — researchers simulate an entire fly brain on a laptop](../sources/berkeley-fly-brain-news.md)
- [flybody Paper](../sources/flybody-paper.md)
