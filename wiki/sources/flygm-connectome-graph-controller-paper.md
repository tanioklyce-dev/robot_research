---
title: "Whole-Brain Connectomic Graph Model Enables Whole-Body Locomotion Control in Fruit Fly — FlyGM (Jin, Zhu, Zhang & Sui, 2026)"
type: source
url: https://arxiv.org/abs/2602.17997
local_path: raw/2602.17997.pdf
sha256: ebdeb8cc94490cdcc2967565f06bcd7f9ab2706cd606cf4dbb74b0f22b688e0e
author: "Zehao Jin, Yaoye Zhu, Chen Zhang, Yanan Sui†"
affiliations: "Tsinghua University"
published: 2026-02-20
revised: 2026-06-14 (v3)
venue: "arXiv preprint v3, cs.LG; no peer-reviewed venue as of ingest"
format: paper (18 pp; 9 pp body + references + appendices)
arxiv: 2602.17997
project_page: https://lnsgroup.cc/research/FlyGM
tags: [connectome, flywire, flybody, graph-neural-network, reinforcement-learning, PPO, imitation-learning, locomotion, drosophila, mujoco, structural-prior, whole-organism, brain-body]
ingested: 2026-09-12
---

# Whole-Brain Connectomic Graph Model Enables Whole-Body Locomotion Control in Fruit Fly (FlyGM)

## Summary

**The brain-to-body bridge the wiki said nobody had built.** FlyGM takes the [FlyWire](../entities/flywire.md) whole-brain connectome (FAFB v783) as a directed graph, signs each edge by presynaptic neurotransmitter (net excitatory minus inhibitory synapse count), partitions neurons into afferent / intrinsic / efferent by FlyWire's flow labels, and uses the synaptic weight matrix **W as a fixed message-passing operator** in a recurrent graph network: observations are encoded into the afferent neurons, one step of W·H propagates, a shared MLP conditioned on a per-neuron trainable descriptor updates every state, and the efferent states are decoded into motor actions for [flybody](../entities/flybody.md), the MuJoCo fly. Trained by imitation of flybody's released MLP experts, then fine-tuned with PPO, it walks (gait initiation, straight walking, turning at 3 cm/s and 10 rad/s) and flies (20 cm/s, as a residual over the wing-pattern generator).

The result that matters is the control: against a **degree-preserving rewiring** of the same graph, an **Erdős–Rényi** graph with matched nodes and edges, an over-parameterised **MLP**, a **spiking** baseline and five standard **GNNs**, the biological wiring converges faster in imitation and has the lowest orientation error in every speed/yaw condition — **8.29° vs 13.55° (rewired) and 13.90° (MLP)** at the hardest setting, where the random graph collapses to 125°. Even an *unweighted* connectome beats every non-connectome baseline. Trained dynamics show sensory / central / motor populations differentiating by superclass, and the random-graph control does not.

> [!note] What is and is not claimed
> The connectome supplies the *wiring*; everything else — the encoder, decoder, per-neuron descriptors, update MLP — is learned, and the graph runs at the flybody control rate, not at biological timescales. The claim is that connectome topology is a **useful inductive bias for control**, evidenced by ablation, not that the model is a simulation of a fly's nervous system. Observations include 1,253 features (with 16 × 16 binocular vision) for walking, injected into all afferent neurons via one gate; the flybody proprioceptor mapping is not modelled. Four tasks, one body simulator, no real-world component.

## Key claims

### Method (Sec. 3)

- Signed weights: W_vu = N_exc(u, v) − N_inh(u, v), with ACh, glutamate, aspartate, histamine as excitatory and GABA, glycine as inhibitory (following the *effectome* linear-dynamics view).
- Per step: encode x_t (to 32-D) → gate into afferent states → M = W·H → H' [v] = f_ψ([M[v]; η_v]) with a trainable descriptor η_v per neuron → decode efferent states to actions. 32 channels, 4 message-passing layers.
- Training: imitation of flybody's expert MLP (KL between Gaussian action distributions plus an annealed MSE), then PPO with an MLP value head; distributed on A100s.

### Ablation of the wiring (Tab. 1, 3, 4; App. F–H)

| Controller | Angle error at v = 3, ψ = 7 |
|---|---|
| **FlyGM (signed weights, per-neuron descriptors)** | **8.29 ± 0.21°** |
| FlyGM unweighted | 11.00 |
| FlyGM, shared descriptors per superclass | 9.10 |
| Degree-preserving rewiring | 13.55 |
| MLP (4 × 512, more parameters) | 13.90 |
| Erdős–Rényi random graph | 125.36 |
| Spiking network (LIF, same MLP layout) | ~126; never a stable gait |

- *"The structural advantage of the connectome grows with task complexity."*
- Against GCN, EdgeCNN, GAT, GraphSAGE and PNA on the same node partition and pipeline: FlyGM's imitation KL 2.34 vs 2.89 (PNA, next best); average RL reward **334 vs 145** (PNA). *"The advantage… does not stem solely from graph-structured computation or parameter budget, but specifically from the biological connectivity structure."*
- Signed weights help most at high yaw (8.29 vs 11.00); descriptors help less than topology.

### Behaviour and representation (Sec. 4.2–4.3)

- Gait initiation in ~80 ms; tripod gait with anti-phase leg groups; turning via asymmetric stride modulation *"without requiring task-specific tuning"*; flight as WPG-frequency and wing-torque residuals.
- Recording neuron states during a walk–decelerate–pause–turn sequence and reducing to one intensity per neuron: superclasses (sensory, ascending, descending, motor, central, optic…) show distinct, phase-locked patterns; the same analysis on the random-graph policy yields *"nearly homogeneous activation patterns across superclasses."*

### Limitations (authors')

Newer synapse detections and sex-specific annotations not used; longer per-step compute and memory than an MLP; locomotion only.

## Why it matters in this wiki

- **The [whole-organism agentic AI](../syntheses/agents/whole-organism-agentic-ai.md) synthesis described this experiment as the missing integration** — FlyWire brain + flybody body. It has now been run, from a control-engineering angle (the connectome as an architecture prior) rather than a neuroscience one (the connectome as a model of the fly).
- **A structural-prior result with the right controls.** Rewired and random graphs, a bigger MLP, five GNNs: the ablation ladder is what the wiki's [ablation](../glossary.md#ablation) entry asks for, and the comparison with standard GNNs answers the obvious objection.
- **The next dataset is obvious.** FlyWire stops at the brain; the [BANC](banc-brain-and-cord-connectome-paper.md) and [male CNS](male-cns-connectome-paper.md) maps reach the motor neurons, so the efferent set could be the real motor-neuron population and the decoder could shrink to a muscle map.
- **Contrast with [Shiu et al.](shiu-fly-brain-paper.md)**: same graph, opposite philosophy — Shiu keeps the connectome's weights and adds *no* learning; FlyGM keeps the topology and learns everything else. Neither is closed-loop with a body except FlyGM.

## Entities mentioned

- [FlyWire](../entities/flywire.md) — the graph (FAFB v783), flow-type partition, neurotransmitter predictions.
- [flybody](../entities/flybody.md) — the body, tasks, expert policies and datasets.
- [NeuroMechFly](../entities/neuromechfly.md) — cited as the alternative body simulator.
- Yanan Sui (Tsinghua) — no entity page; the group's musculoskeletal-control line (DynSyn, hierarchical model-based planning) is cited.

## Concepts touched

- [Connectome](../concepts/bio/connectome.md) — a third way to use one: as an architectural prior for a learned controller.
- [Biomechanical simulation](../concepts/bio/biomechanical-simulation.md) — flybody closed-loop.
- [Imitation learning](../concepts/learning/imitation-learning.md) — KL-to-expert distillation before RL.

## Open questions

- **Brain + cord.** Run on BANC or the male CNS with real motor neurons as the efferent set.
- **Timescale.** One graph step per control step; whether multiple propagation steps per action (closer to neural dynamics) help or hurt is untested.
- **Beyond locomotion.** Manipulation-like tasks (grooming, feeding) would test the claim that the prior is general.
- **Is the advantage from the fly's wiring specifically, or from any evolved small-world graph?** The rewiring control preserves degree, not community structure.
