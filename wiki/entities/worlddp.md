---
title: WorldDP
type: entity
subtype: model
created: 2026-07-26
updated: 2026-09-07
sources: 1
tags: [worlddp, world-model, jepa, object-centric, diffusion-policy, hierarchical-planning, mpc, particle-filter, multi-stage-manipulation, dinov2, sam2, ogbench, lecun, ami-labs, nyu]
---

# WorldDP

**WorldDP** ([Goswami, Krishnamurthy, LeCun, Khorrami 2026](../sources/worlddp-paper.md), arXiv 2606.08775) is a **hierarchical framework for multi-stage robotic manipulation** that unifies an **object-centric [JEPA](../concepts/world-models/jepa.md) world model** (high-level subgoal planner) with a **[Diffusion Policy](diffusion-policy.md)** (low-level subgoal tracker). It is a [Yann LeCun](yann-lecun.md)-coauthored NYU paper and the **first paper in this wiki to carry an [AMI Labs](ami-labs.md) affiliation** on his byline.

## Why it matters in this wiki

WorldDP is the wiki's first model to **bridge the two rival control paradigms it otherwise tracks separately** — LeCun's JEPA-world-model-as-planner line ([DINO-WM](dino-wm.md), [LeWorldModel](leworldmodel.md), [HWM](hwm.md), [V-JEPA 2](v-jepa-2.md)) and the imitation-learning [Diffusion Policy](diffusion-policy.md) / [VLA](../concepts/learning/vla-models.md) line. Its argument is that neither alone handles **multi-stage** tasks: latent world models plan but stall on long horizons; diffusion policies execute but don't plan. WorldDP makes the world model a **subgoal generator** and the diffusion policy a **subgoal executor** — and empirically that combination more than doubles the next-best success rate on 3-object rearrangement. It also sharpens the contrast with **[HWM](hwm.md)** (the wiki's other hierarchical latent planner), which uses a *second world model* at the low level rather than a diffusion policy.

## Architecture

- **Object-Centric Encoder (OCE):** frozen **DINOv2** patch features → **slot attention** (N slots for robot/objects/background) refined by a GRU "Slot Corrector"; trained with reconstruction + a **Tversky mask loss** against **SAM2**-generated segmentation masks (privileged training-time guidance). Learns object representations *on top of* DINOv2 patches, not raw pixels.
- **Dynamics model:** a **Conditional Diffusion Transformer (CDiT)** (12 layers, 4 heads) over object-centric states, conditioned on a 32-D latent action embedding; autoregressive at planning time.
- **Upper tier (planning):** the world model is the transition function in an **MPC** loop optimized by a **Particle Filter** (multi-modal, unlike CEM's single Gaussian). Cost = object-embedding MSE + a **contact-prediction** term (an MLP flags robot-object contact → pushes subgoals to pivotal frames like "handle gripped").
- **Lower tier (execution):** a **goal-conditioned 40-step Diffusion Policy** tracks each subgoal; multi-object tasks plan/execute per object in an MPC loop.

## Reading notes — what the names hide (close read, 2026-09-07)

A section-by-section read of the primary ([source page](../sources/worlddp-paper.md)) turned up four points where the paper's terminology would mislead someone trying to reuse a component. None changes the reported results; all change what the results demonstrate.

- **The "Conditional Diffusion Transformer" does not diffuse.** §3.2 and Appendix A.2 describe a deterministic regressor: teacher-forced **MSE** in slot space, one forward pass per rollout step, and no noise schedule, diffusion timestep, or denoising loop anywhere in the text. "Diffusion" is inherited from the block architecture (CDiT from Navigation World Models, Bar et al. 2025 — un-ingested — via Goswami et al. 2025), where it *was* used for denoising. Consequence: the world model is the one component that **cannot** represent the multi-modal futures the paper's own argument turns on. Multi-modality is handled *around* it — the particle filter keeps several hypotheses, and the low-level [Diffusion Policy](diffusion-policy.md) is genuinely stochastic. Whether a truly stochastic predictor would help or hurt planning is an experiment the paper does not run.
- **The "particle filter" is a multi-elite sampler, not a Bayesian filter.** No importance weights, no likelihood, no proportional resampling, no per-step belief propagation. Algorithm 1: sample Q=600 latent action sequences at fixed σ around M=10 elite means, roll each out through the world model, score, keep the top 10 as the next means, repeat L=10–20 times, return the best. Structurally it is a **mixture-of-Gaussians CEM with fixed σ and no covariance fitting**, i.e. truncation-selection evolutionary search. The CEM contrast (single Gaussian collapses to one mode; ten elites keep ten) is real — but the paper's *"use of particle filters is new for planning using world models"* is new mainly in name.
- **The CEM ablation may not be optimizer-vs-optimizer.** The PF is seeded with straight-line end-effector trajectories to workspace keypoints (§3.3) — a strong Cartesian reachability prior. The text does not say whether the "w/o PF" CEM variant received the same seeds. Some of the PF's margin may be the initialization.
- **SAM2 supervision does a second job the paper doesn't name: it fixes slot order.** Unsupervised slot attention is permutation-ambiguous; an MSE between slot matrices across frames would be ill-posed if slot 3 were the red cube in one frame and the gripper in the next. Pinning each slot to a named entity via the Tversky mask loss (α=0.99, β=0.01, inverse-size weighting — every knob says *do not lose the cube*) is what makes the dynamics loss well-defined at all. Remove the privileged masks and the dynamics model needs a matching step, not just a worse encoder.

Smaller things worth knowing before reuse:

- **The clock lives in the action embedding.** Training samples 5 frames at random increasing offsets within a 100-frame window; the 3-layer transformer action encoder compresses the *variable-length* chunk between frames into 32-D. There is no fixed step duration — the world model predicts "the state after this chunk," and the planner samples in that 32-D space, trusting it to be smooth enough to perturb at σ. Untested.
- **Slot count N is a hard prior**: 3 / 5 / 7 slots, matching the true entity count per environment; slot dim jumps 64 → 128 → **1024** for the scene tasks without explanation. This is assignment of known entities, not object discovery.
- **Contact predictor input is inconsistent between main text and appendix.** §3.3 says it maps the state `s_k` to per-object contact probabilities; Appendix A.4 says it takes *the mean of the DINOv2 patch features*. If A.4 is right, the contact signal bypasses the object-centric state entirely.
- Planner hyperparameters (Appendix C): horizon **T = 2–3** world-model steps; **Q = 600** particles; **σ = 1.0 / 0.5 / 0.1**; **M = 10** elites; **L = 20 / 10** iterations; **λ_plan = 0.05–0.1**.

## Reported numbers (from ingested sources)

OGBench manipulation (UR5e, [LeWM](leworldmodel.md)-variant envs; 50 held-out trials):

- **Cube-Triple, all 3 cubes: 30%** — >2× the next best (HECRL* 12, DP100 4, [DINO-WM](dino-wm.md)/[LeWM](leworldmodel.md) 0).
- **Scene-Single-Composite, full task: 20%** (HECRL* 18, DP100 14, others 0).
- **Cube-Single + Scene-Single-Direct "both-task" avg: 74.5%** (HECRL* 63, DP100 63, DP40 32).
- Ablations confirm the hierarchy, the object-centric encoding, the 40-step (vs 100-step) DP, and the particle filter (vs CEM) each help.

## Related

- [Yann LeCun](yann-lecun.md) — co-author; his AMI-Labs-affiliated paper.
- [Diffusion Policy](diffusion-policy.md) — the low-level tracker WorldDP wraps.
- [HWM](hwm.md) — the other hierarchical latent-world-model planner; uses a world model (not a diffusion policy) at the low level.
- [DINO-WM](dino-wm.md) / [LeWorldModel](leworldmodel.md) / [V-JEPA 2](v-jepa-2.md) — single-stage JEPA-world-model baselines it beats.
- [JEPA](../concepts/world-models/jepa.md) — the paradigm it extends with object-centric states.
- [VLA models](../concepts/learning/vla-models.md) — the end-to-end alternative it positions against.

## Open questions

- Per-environment training (no cross-task/embodiment transfer shown); **simulation-only** (OGBench), unlike the LeCun program's real-Franka V-JEPA 2 / HWM results; SAM2 guidance is privileged supervision.
- Would a genuinely stochastic (diffusion or flow) predictor in slot space help the planner, or make the MSE-based subgoal cost ill-posed? (See reading notes — the current CDiT is deterministic.)
- Did the "w/o PF" CEM ablation get the keypoint-trajectory seeds? If not, the optimizer comparison is confounded by initialization.
- If SAM2 masks are trusted, why distill into slots at all rather than mask-pool DINOv2 features per object at inference? The slot route buys a fixed-size state and a cheaper forward pass at the cost of a hard-coded N.

## Mentioned in

- [WorldDP paper (Goswami et al. 2026)](../sources/worlddp-paper.md) — the primary source.
