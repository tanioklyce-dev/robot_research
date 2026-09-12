---
title: Connectome
type: concept
created: 2026-05-08
updated: 2026-09-12
sources: 9
tags: [connectome, neuroscience, brain-mapping, biological-ai, drosophila]
---

A **connectome** is a complete wiring diagram of a nervous system — every neuron and every synaptic connection between them, mapped at synaptic resolution. The term parallels "genome" (complete sequence of an organism's DNA): a connectome is the complete circuit-level description of an animal's brain.

## Concrete instances

- ***C. elegans*** (302 neurons, ~7,000 synapses) — first complete connectome (White et al. 1986).
- ***Drosophila* hemibrain** (~25k neurons) — Janelia 2020. Half-brain at synaptic resolution.
- ***Drosophila* MANC / FANC** — male/female adult ventral nerve cord, 2024.
- ***Drosophila* whole brain** — [FlyWire](../../entities/flywire.md), October 2024. **139,255 neurons, ~50M synapses.** First complete adult-brain connectome of any organism.
- ***Drosophila* whole CNS, male** — [Berg, Beckett, Costa, Schlegel, Januszewski … Rubin, Jefferis, *Cell* 2026](../../sources/male-cns-connectome-paper.md) (HHMI Janelia FlyEM + Cambridge/MRC LMB + Google Research). **166,691 neurons, 11,691 cell types, 25.6 M-edge graph, brain *and* ventral nerve cord from one animal with an intact neck connective** — the first complete adult CNS and the first male brain. 160 teravoxels at 8 nm, flood-filling-network segmentation, **44 person-years** of proofreading; 94% pre- / 42% postsynaptic completion, 40.1% of connections proofread at both ends. Motor neurons annotated to exit nerve and muscle. Adds the isomorphic / *dimorphic* / sex-specific classes (4.8% of the male central brain differs) and the finding that the neck connective is a bottleneck *and* an integrator carrying most feedback. Preprint counts; the journal version revises them upward ([edition history](../../sources/male-cns-connectome-paper.md#edition-history)). Announced via a [Google post](../../sources/google-male-fruit-fly-brain-map-blog.md).
- ***Drosophila* whole CNS, female (BANC)** — [Bates et al., *Nature* 2026-06-08](../../sources/banc-brain-and-cord-connectome-paper.md) (Harvard/Princeton, BANC-FlyWire Consortium). Serial-section TEM at 4 × 4 × 45 nm, 7,010 sections, **~160,000 neurons**, 155 community proofreaders over ~3.5 years (~38.6 person-years); brain (~140k) and cord (~20k) joined by ~1,300 descending and ~1,800 ascending neurons. Its thesis is about control: effectors are driven mostly by sensors in the same body part (**local feedback loops**), linked by behaviour-centric AN/DN modules under light supervision — *"distributed, parallelized and embodied,"* citing Brooks 1986. With the male CNS map, both sexes now have whole-CNS connectomes from two labs and two imaging modalities.
- **Mouse and human** — current frontier targets, multiple orders of magnitude harder (~70M neurons in mouse, ~86B in human). Berkeley News' Phil Shiu names mouse as the next stop and human as the long-term ambition ([Berkeley News](../../sources/berkeley-fly-brain-news.md)).
- **Human — [H01](../../entities/h01-connectome.md)** (Lichtman Lab / Google, *Science* 2024). A **1.4-petabyte, ~1 mm³** EM reconstruction of human cortex — **tens of thousands of neurons, 183M synapses, 100 proofread cells** ([H01 release](../../sources/h01-human-cortex-reconstruction.md)). Crucially it is a **dense fragment, not a complete connectome**: it makes the human scale concrete (petabytes for a pinhead of cortex) without yet being the whole-circuit artifact the two AI pathways below require.

## Two ways to use a connectome for AI

> [!note] A third way, demonstrated (added 2026-09-12)
> [FlyGM](../../sources/flygm-connectome-graph-controller-paper.md) uses the FlyWire graph neither as a simulation substrate nor as a constraint on a neural model, but as an **architectural prior for a learned controller**: signed synaptic counts become a fixed message-passing operator, everything else is trained by imitation and PPO, and the policy drives [flybody](../../entities/flybody.md). Ablations against degree-preserving rewiring, random graphs, a larger MLP, a spiking network and five GNNs all lose (8.3° vs 13.6–125° orientation error at the hardest setting). The claim is inductive bias, not fidelity.


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
- [H01](../../entities/h01-connectome.md) — the petascale human-cortex fragment.
- [flybody](../../entities/flybody.md) — body-side complement.
- [Drosophila melanogaster](../../entities/drosophila.md) — model organism for whole-organism AI.
- [Biomechanical simulation](biomechanical-simulation.md) — companion concept.
- [Whole-organism agentic AI](../../syntheses/agents/whole-organism-agentic-ai.md) — synthesis tying connectome + body sim together.

## Mentioned in

- [Berkeley News — researchers simulate an entire fly brain on a laptop](../../sources/berkeley-fly-brain-news.md)
- [H01 — A Browsable Petascale Reconstruction of the Human Cortex](../../sources/h01-human-cortex-reconstruction.md)
- [flybody Paper](../../sources/flybody-paper.md)
- [Shiu et al. 2024 — A Drosophila computational brain model](../../sources/shiu-fly-brain-paper.md)
- [Lappalainen et al. 2024 — Connectome-constrained networks (fly visual system)](../../sources/lappalainen-flyvis-paper.md)
- [Google — male fruit fly brain map](../../sources/google-male-fruit-fly-brain-map-blog.md) — first complete adult CNS (brain + VNC), male; the dataset a brain-to-body fly simulation would need.
- [Male CNS connectome — Berg et al., Cell 2026](../../sources/male-cns-connectome-paper.md) — the primary; first complete adult CNS, neck connective intact.
- [BANC — Bates et al., Nature 2026](../../sources/banc-brain-and-cord-connectome-paper.md) — the female brain-and-cord connectome; local feedback loops and distributed control.
- [FlyGM](../../sources/flygm-connectome-graph-controller-paper.md) — a whole-brain connectome as an RL controller's architecture, with controls.
- Companions to the male CNS: [visual pathways](../../sources/male-cns-visual-pathways-paper.md), [gustatory connectome](../../sources/male-cns-gustatory-connectome-paper.md), [dimorphic social networks](../../sources/dimorphic-social-networks-paper.md) — abstract-level pages.
