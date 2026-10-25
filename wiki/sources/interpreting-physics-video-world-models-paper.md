---
title: "Interpreting Physics in Video World Models (Joseph, Garrido, Balestriero, …, Richards, Rabbat, 2026)"
type: source
url: https://arxiv.org/abs/2602.07050
fetch_url: https://arxiv.org/pdf/2602.07050v1
local_path: raw/2602.07050v1.pdf
sha256: 4d67a8c153154f3b854a6f1a4aeac5b874809c603bcd43e1c840564343105c8b
author: Sonia Joseph, Quentin Garrido, Randall Balestriero, Matthew Kowal, Thomas Fel, Shahab Bakhtiari, Blake Richards, Mike Rabbat
published: 2026-02-04
ingested: 2026-10-24
venue: arXiv (cs.CV), v1
format: "paper, 33 pp (9 main + appendices A–C). Affiliations: FAIR / Meta Superintelligence Labs, Mila & McGill, FAR.AI, Kempner Institute (Harvard), Université de Montréal. Richards and Rabbat are joint last authors."
tags: [interpretability, v-jepa-2, videomae-v2, intuitive-physics, intphys, probing, physics-emergence-zone, population-code, steering, attention-heads, kubric, clevrer, world-model, representation-geometry]
---

# Interpreting Physics in Video World Models (2026-02-04)

## Summary

This is a mechanistic-interpretability study of **how** frozen video encoders represent physics: [V-JEPA 2](../entities/v-jepa-2.md) L/H/G and VideoMAE-v2 G. It uses layer-wise probes, subspace geometry, attention ablations and steering.
- **Physics Emergence Zone.** Across all scales, possible-vs-impossible discrimination (IntPhys) jumps from chance to ~85–95% at **about one-third depth**, peaks mid-network, and **degrades toward the output**.
- **Speed is easy, direction is hard.** Speed and acceleration magnitude are decodable from early layers. **Motion direction appears only at the emergence zone**, as a ring-shaped, high-dimensional population code: about 40–50 features, steerable only by coordinated interventions across dozens of dimensions.
- **Not a physics engine.** Direction and possible/impossible judgments occupy **nearly orthogonal subspaces**. They share a computational substrate (unusually *local* spatiotemporal attention heads in the zone) but no latent variables.

The paper's verdict: **distributed, task-specific representations**, not a factorised physics engine.

## Key claims
- **Emergence (§4, Fig. 1):** a sharp, scale-invariant transition at ~⅓ depth for V-JEPA 2 L/H/G and VideoMAE-v2 G. Smaller VideoMAE-v2 models show no reliable emergence. The pattern holds across violation types: object permanence, shape constancy, spatiotemporal continuity.
- **Intermediate beats final (§4.2):** *"final-layer features do not necessarily preserve the most informative physical structure."* Intermediate layers give better downstream intuitive-physics performance (App. C.1.4).
- **Motion variables (§5; Kubric toy-ball videos):**
  - Cartesian velocity and acceleration both transition at the zone, and **acceleration is decodable without a velocity intermediate**.
  - In polar form, **speed and |a| are available early, while direction emerges only at the zone**. The authors compare this to biological motion processing (motion energy early, direction selectivity later).
  - It replicates per object on CLEVRER.
- **Task specificity (§6.1):** CLEVRER counting and SSv2 classification show no ⅓-depth signature; shuffled-video detection does. The zone tracks **global spatiotemporal coherence**, not depth in general.
- **No shared variables (§6.2):** principal angles between motion and IntPhys subspaces are 69°–83°. Only **7–13%** of the IntPhys subspace projects onto direction (< 3% onto speed), indistinguishable from random.
- **Shared mechanism (§6.3, Table 2):** suppressing *local* attention only inside the zone drops direction R² from 0.97 to **0.14** and IntPhys from 78.3% to **51.9–62.2%**. ImageNet stays at ~33%.
- **Geometry and steering (§7):**
  - MLP units tile 360° with sinusoidal tuning, forming a circular population code.
  - Possible/impossible needs ~20 features and direction 40–50, rising to ~80 near the output.
  - Steering along one probe axis leaves > 80° error; steering across **all** probe directions at layer 8 leaves **< 0.5°**.
  - This contrasts with LLMs, where concepts such as refusal steer along a single direction.
- **Limitations (§9):** encoder-only masked-objective models; coarse spatiotemporal tasks; **no contact dynamics or force inference**; synthetic single-ball data may not reflect natural video.

## Reading notes (wiki inference)
- **Direction is the hard half, again.** [LeHami](lehami-symplectic-latent-dynamics-paper.md) found that a *tied* temporal window recovers speed but not the **sign** of velocity, and that untied windows or explicit structure are needed for direction. Here, in a frozen video encoder, speed is linearly available from the first layers while direction needs a third of the network. Two independent results point the same way: **signed motion direction is what costs representation**, and magnitude comes nearly free.
- **Layer choice for frozen-encoder world models.** [DINO-WM](../entities/dino-wm.md)-style and V-JEPA-2-AC-style world models read a frozen encoder's **output** features. If physics-relevant structure peaks mid-depth and degrades toward the output, readout depth is an untuned hyperparameter in those pipelines. The [Toso et al. result](preserving-unstable-modes-inverse-dynamics-paper.md), where frozen DINOv2 never stabilises CartPole but iBOT does, is consistent with *which features the backbone exposes* being load-bearing.
- **Probing caveat.** "Decodable at layer *k*" is accessibility to a probe, not use by the model. The ablation and steering results are what make this more than a probing study.

## Entities mentioned
- [V-JEPA 2](../entities/v-jepa-2.md) · [Randall Balestriero](../entities/randall-balestriero.md) · [AMI Labs](../entities/ami-labs.md) (Rabbat is a listed co-founder per a [third-party tracker](ami-labs-intelligence-hub-research.md); this paper's affiliation is FAIR)

## Concepts touched
- [Physical reasoning benchmarks](../concepts/world-models/physical-reasoning-benchmarks.md): IntPhys as a probe target, not just a behavioural score.
- [JEPA](../concepts/world-models/jepa.md): the internal geometry of a JEPA video encoder against a pixel-reconstruction one.
- [World-model evaluation](../concepts/world-models/world-model-evaluation.md): intermediate-layer readout; probes plus causal ablation.

## Open questions
- Does the emergence zone exist in **action-conditioned** predictors (V-JEPA 2-AC), or only in the encoder?
- Would reading frozen features from the emergence zone rather than the output improve DINO-WM / V-JEPA-2-AC planning on dynamic tasks?
- Contact and force: the paper explicitly does not test them, and they are the manipulation-relevant physics.
