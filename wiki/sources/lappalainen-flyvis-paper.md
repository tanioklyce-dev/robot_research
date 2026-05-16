---
title: "Connectome-constrained networks predict neural activity across the fly visual system (Lappalainen et al. 2024)"
type: source
subtype: paper
created: 2026-05-08
updated: 2026-05-08
url: https://doi.org/10.1038/s41586-024-07939-3
pmcid: PMC11525180
author: Lappalainen, Tschopp, Prakhya, McGill, Nern, Shinomiya, Takemura, Gruntman, Macke, Turaga
published: 2024-09-11
ingested: 2026-05-08
journal: "Nature 634(8036):1132–1140"
code: https://github.com/TuragaLab/flyvis
tags: [drosophila, connectome, fly-visual-system, deep-learning, pytorch, motion-detection, optic-flow, hexagonal-cnn, connectome-constrained, biological-ai]
---

## Summary

*Nature* paper (published 11 September 2024) showing that a deep neural network whose **connectivity is fixed by the *Drosophila* optic-lobe connectome** — but whose neuron and synapse parameters are learned by gradient descent — accurately predicts single-neuron activity across the fly visual system, including ON/OFF channel separation and direction selectivity in the canonical T4/T5 motion detectors. Trained only to estimate optic flow on naturalistic video, with no neural-activity supervision, the model's predictions match recordings from **26 prior experimental studies**. Released as the open-source [TuragaLab/flyvis](https://github.com/TuragaLab/flyvis) library. Lead author **Janne K. Lappalainen** (Tübingen); senior author **Srinivas C. Turaga** (HHMI Janelia, also senior on [flybody](flybody-paper.md)).

## Thesis

Connectome data tells you *which* neurons connect, but not *how strongly* or with *what dynamics*. Train a neural network with the connectome's connectivity mask in place — fixing 604 synaptic signs and 2,355 synapse counts — and let backprop discover the remaining 734 free parameters (resting potentials, time constants, per-type unitary synapse scales) under a behaviourally meaningful task objective (motion detection). The result both performs the task and predicts real neural activity, **without ever being shown neural recordings during training**.

## Key claims

### Network construction
- **Scale.** 45,669 neurons, 64 cell types, 1,513,231 synaptic connections, 721 hexagonal columns covering the central visual field.
- **Brain region.** Retina → lamina → medulla → lobula + lobula plate. Visual system only — no central brain, no motor output.
- **Connectivity source.** Two EM connectome reconstructions (FIB-25 and FIB-19), with cell-type repetition tile-extended across the hexagonal lattice.
- **Dynamics.** Threshold-linear leaky integrator per neuron; graded-release chemical synapses approximated by a threshold-linear function of presynaptic voltage. One electrical compartment per neuron except CT1 (one per column, since CT1 has wide-field morphology).
- **What's fixed vs free:**
  - Fixed: 604 synaptic signs (from EM-predicted neurotransmitter), 2,355 type-to-type synapse counts.
  - Learned: 65 resting potentials, 65 membrane time constants, 604 unitary synapse scaling factors → **734 free parameters total**.

### Software & training
- **PyTorch** with custom hexagonal CNN architecture matching the optic lobe's hexagonal lattice. Backprop through time over 19 frames (792 ms at 50 Hz).
- **Task.** Optic-flow estimation on 23 sequences from the open-source *Sintel* animated film. A 2-layer convolutional decoder maps medulla/downstream activity to a per-frame 2D velocity field.
- **Optimizer.** Adam with adaptive learning rate (5×10⁻⁵ → 5×10⁻⁶); 150,000 iterations.
- **Ensemble.** Many models trained from random initializations; analyses look at the distribution.
- **Validation data.** Comparison against responses to circular-flash, moving-edge, single-ommatidium-flash, and naturalistic-video stimuli reported across 26 prior studies.

### Predictive results
- **ON/OFF channel separation** correctly predicted for all 32 characterized cell types.
- **T4 = ON-motion-selective, T5 = OFF-motion-selective**, with the four cardinal-direction subtypes recovered.
- **Mechanistic predictions.** Mi4 → T4 inhibitory timing; CT1 → T5 inhibitory timing; lateral T4-to-T4 connectivity effects — all consistent with the experimental literature.
- **Spatial receptive fields.** Tm3, Tm4 → broad (two-column radius, 11.6°); Mi1/Mi4/Mi9/Tm1/Tm2/Tm9/CT1 → narrow. Matches measurements.
- **Quantitative.** Contrast preference correctly predicted in 30 of 32 characterized cell types; better-task-performing models correlate more strongly with experimentally measured direction selectivity (r = −0.60, p = 2.6×10⁻⁶ across the ensemble).
- **Novel prediction.** TmY3 proposed as a parallel motion pathway independent of T4/T5; consistency varies across ensemble clusters, so flagged tentative.

## Reproducibility status

- **Code:** [github.com/TuragaLab/flyvis](https://github.com/TuragaLab/flyvis) — **MIT-licensed**, actively maintained (v1.1.3, 2026-03-07). Documentation site at [turagalab.github.io/flyvis](https://turagalab.github.io/flyvis/). See [flyvis entity page](../entities/flyvis.md).
- **Pretrained models** distributed with the codebase ("try pretrained models on your data" path), so reproducing predictions does not require retraining from scratch.
- **Seven tutorial notebooks** including Google Colab versions cover connectome exploration, optic-flow training, flash and moving-edge responses, ensemble clustering, maximally-excitatory-stimuli generation, and custom-stimulus provision.
- **Data:** Sintel video is openly downloadable; the connectome data is bundled with the codebase per the paper's "code and data availability" statement.
- **Stack:** Standard PyTorch + a custom hexagonal CNN layer; GPU-trainable on commodity hardware (paper does not state training cost).

## Entities mentioned

- [FlyWire](../entities/flywire.md) — *not* used here. flyvis predates whole-brain FlyWire and uses the older optic-lobe-specific FIB-25 / FIB-19 reconstructions. The conceptual approach (deep net with connectome-masked connectivity) is what generalizes to FlyWire scale.
- [Drosophila melanogaster](../entities/drosophila.md) — model organism.
- [HHMI Janelia](../entities/hhmi-janelia.md) — Turaga lab; Aljoscha Nern, Kazunori Shinomiya, Shin-ya Takemura, Eyal Gruntman.
- [flyvis](../entities/flyvis.md) — the released codebase (MIT, PyTorch, v1.1.3 March 2026).
- Janne K. Lappalainen — lead author (Tübingen).
- Srinivas C. Turaga — senior author (HHMI Janelia). Also senior on [flybody](flybody-paper.md).
- Jakob H. Macke — co-senior (Tübingen).

## Concepts touched

- [Connectome](../concepts/bio/connectome.md) — substrate. Together with [Shiu et al. 2024](shiu-fly-brain-paper.md), this defines the two main ways to *use* a connectome computationally (mechanistic LIF vs. connectome-constrained deep learning).
- [Imitation learning](../concepts/learning/imitation-learning.md) — *not* used here; training is task-supervised on optic flow, not imitation.

## Open questions

- **Visual system only.** No motor output, no central brain, no behaviour. The "decoder" is a CNN reading optic flow off medulla activity, not a behavioural readout. Scaling the same approach to the **full FlyWire connectome** is the obvious next step but is not done in this paper.
- **Single computation.** Trained only for motion detection. Other visual computations (looming, colour, visual learning) would need separate task objectives.
- **Connectome incompleteness.** FIB-25/FIB-19 are local reconstructions stitched together. Some cell types lack experimental neurotransmitter data and required educated guesses.
- **Sparsity caveat.** The authors attribute success in part to the *sparse* structure of the visual-system connectome. They note that for non-sparse circuits, predictions degrade unless connection strengths (not just counts) are also known.
- **No body, no closed loop.** Same gap as Shiu et al. — a connectome-constrained controller producing motor commands inside [flybody](../entities/flybody.md) is the integration target identified in [Whole-organism agentic AI](../syntheses/agents/whole-organism-agentic-ai.md), and flyvis is the existing template that integration would build on.

## Why it matters here

- **Closes a wiki gap.** Previously referenced only via the [Connectome](../concepts/bio/connectome.md) concept page and the [whole-organism synthesis](../syntheses/agents/whole-organism-agentic-ai.md). Now ingested as a primary source.
- **The brain-side controller template.** flyvis is the closest existing analogue to what a "fly agent" controller inside flybody would look like: a deep net whose architecture is anatomically constrained, trained end-to-end on a task, predictive of real neural activity. The synthesis's "Lappalainen-style controller" framing now has a primary source.
- **Same lab as flybody.** Turaga is senior on both papers — flyvis (brain side, 2024) and [flybody](flybody-paper.md) (body side, 2025). The integration the synthesis identifies as "open" sits inside one PI's research program.
