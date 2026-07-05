---
title: Connectome
type: concept
created: 2026-05-08
updated: 2026-07-04
sources: 3
tags: [connectome, neuroscience, brain-mapping, biological-ai, drosophila]
---

A **connectome** is a complete wiring diagram of a nervous system — every neuron and every synaptic connection between them, mapped at synaptic resolution. The term parallels "genome" (complete sequence of an organism's DNA): a connectome is the complete circuit-level description of an animal's brain.

## Concrete instances

- ***C. elegans*** (302 neurons, ~7,000 synapses) — first complete connectome (White et al. 1986).
- ***Drosophila* hemibrain** (~25k neurons) — Janelia 2020. Half-brain at synaptic resolution.
- ***Drosophila* MANC / FANC** — male/female adult ventral nerve cord, 2024.
- ***Drosophila* whole brain** — [FlyWire](../../entities/flywire.md), October 2024. **139,255 neurons, ~50M synapses.** First complete adult-brain connectome of any organism.
- **Mouse and human** — current frontier targets, multiple orders of magnitude harder (~70M neurons in mouse, ~86B in human). Berkeley News' Phil Shiu names mouse as the next stop and human as the long-term ambition ([Berkeley News](../../sources/berkeley-fly-brain-news.md)).

## Two ways to use a connectome for AI

### 1. Connectome → simulation ([Shiu et al. 2024](../../sources/shiu-fly-brain-paper.md))

Take the wiring + a neuron-dynamics model (e.g., leaky integrate-and-fire) and run a physical simulation of the brain. Shiu et al. did this for the entire FlyWire connectome (127k neurons) using the Brian 2 simulator, with a single free parameter `Wsyn = 0.275 mV`. The model matched ~91% of 164 empirical predictions across feeding (taste → proboscis extension) and grooming (antennal mechanosensory) circuits — and discovered that Ir94e GRNs are aversive (a novel prediction confirmed in vivo).

**Concrete artifact:** [Drosophila brain model](../../entities/drosophila-brain-model.md) (`philshiu/Drosophila_brain_model`, MIT).

**Strengths:** mechanistic; predicts neuron-level activity; no training required; runs on a laptop CPU.
**Weaknesses:** dynamics model is heuristic (LIF); doesn't incorporate gap junctions, neuromodulators, glia, plasticity, or non-spiking neurons; absolute firing rates not expected to match recordings.

### 2. Connectome-constrained deep learning ([Lappalainen et al. 2024](../../sources/lappalainen-flyvis-paper.md), Mi et al. 2022)

Build a deep neural network whose connectivity *signs and counts* are fixed by the biological wiring, then learn the remaining parameters (resting potentials, time constants, per-type unitary synapse scales) by gradient descent under a task objective.

- **[Lappalainen et al. 2024](../../sources/lappalainen-flyvis-paper.md)** (*Nature* 634:1132–1140) — 64 cell types / 45,669 neurons / 1.5M synapses across the fly optic lobe. Trained on optic-flow estimation from naturalistic video; predicts ON/OFF channel separation, T4/T5 motion selectivity, and matches recordings from 26 prior studies — *without ever being shown neural activity during training*.
- **Mi et al. 2022** (ICLR) — connectome-constrained latent-variable model of whole-brain neural activity.

**Concrete artifact:** [flyvis](../../entities/flyvis.md) (`TuragaLab/flyvis`, MIT, actively maintained — v1.1.3 in March 2026).

**Strengths:** scales to deep-learning training pipelines; generalizes across stimuli; predicts neural activity from a behavioural objective alone.
**Weaknesses:** abstracts away biophysical detail (no spikes, no synaptic dynamics); success depends on connectivity sparsity.

## Why it matters here

Connectomes are the **brain side** of the whole-organism agentic-AI program (the [flybody](../../entities/flybody.md) family is the body side). The Vaxenburg et al. flybody paper explicitly names the combination as the long-term target: *"combining our whole-body model with a complete nervous system connectome … could enable the development of whole-animal models of the entire body and nervous system of the adult fruit fly."*

## Related

- [FlyWire](../../entities/flywire.md) — the *Drosophila* connectome dataset.
- [flybody](../../entities/flybody.md) — body-side complement.
- [Drosophila melanogaster](../../entities/drosophila.md) — model organism for whole-organism AI.
- [Biomechanical simulation](biomechanical-simulation.md) — companion concept.
- [Whole-organism agentic AI](../../syntheses/agents/whole-organism-agentic-ai.md) — synthesis tying connectome + body sim together.

## Mentioned in

- [Berkeley News — researchers simulate an entire fly brain on a laptop](../../sources/berkeley-fly-brain-news.md)
- [flybody Paper](../../sources/flybody-paper.md)
- [Shiu et al. 2024 — A Drosophila computational brain model](../../sources/shiu-fly-brain-paper.md)
- [Lappalainen et al. 2024 — Connectome-constrained networks (fly visual system)](../../sources/lappalainen-flyvis-paper.md)
