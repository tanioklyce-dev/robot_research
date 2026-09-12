---
title: Cross-embodiment transfer
type: concept
created: 2026-09-11
updated: 2026-09-12
sources: 25
tags: [cross-embodiment, embodiment-gap, action-space, normalized-actions, soft-prompts, latent-action-tokens, embodiment-conditioning, retargeting, whole-body-control, navigation, manipulation, humanoid, scaling]
---

# Cross-embodiment transfer

**Cross-embodiment transfer** is getting one policy, model, or dataset to work across robots with different bodies — different kinematics, actuators, sensors, mounting, speeds, and end effectors. The phrase is on over a hundred pages of this wiki. This page exists to say what it has meant in each of them, because it has meant at least four different things, and the answer to whether transfer is "solved" depends entirely on which.

## Four scopes that share one name

| Scope | What differs across bodies | Example | Status in the wiki |
|---|---|---|---|
| **1. Ground navigation** | wheelbase, speed, camera height; even legs vs wheels vs rotors | [GNM](../../sources/gnm-paper.md) drives a Tello quadrotor with no aerial data; [ViNT](../../sources/vint-paper.md) and [MBRA](../../sources/mbra-paper.md) drive a [Go1](../../entities/unitree-go1.md) unchanged | **effectively solved** — because the action space is a normalized 2-D waypoint |
| **2. Parallel-gripper arms, 6–7 DoF** | base frame, reach, camera rig, control rate, dataset conventions | [X-VLA](../../sources/xvla-paper.md), [π0](../../sources/pi-zero-paper.md), [GR00T](../../entities/nvidia-groot.md), [Demo-JEPA](../../sources/demo-jepa-paper.md) | **works with a recipe**; this is what "cross-embodiment" means in 2026 VLA papers |
| **3. Legged locomotion** | morphology, mass, DoF count, missing limbs | [LocoFormer](../../sources/locoformer-paper.md): ten commercial platforms at 0.96 | **solved for locomotion**, by training on bodies that do not exist |
| **4. Radically different bodies** | hands vs grippers; humans vs humanoids; a 5-DoF arm vs a 7-DoF one | [UniT](../../sources/unit-paper.md), [EgoScale](../../sources/egoscale-paper.md), the [RoboMIND](../../sources/robomind-paper.md) exclusion | **open** — and the actual subject of [open question #10](../../syntheses/world-models/open-questions-and-research-direction.md) |

The [Demo-JEPA](../../sources/demo-jepa-paper.md) page says it plainly: its "cross-embodiment" is Sawyer → Franka and UR5e → Franka, "three 6–7 DoF arms with parallel grippers, no human, no hand, no mobile base." [Franka](../../entities/franka-panda.md) is 39.1% of X-VLA's pretraining episodes. When a 2026 VLA says "cross-embodiment," read scope 2.

## Why navigation is free and manipulation is not

The whole difference is whether a **shared low-dimensional action abstraction** exists. [GNM](../../sources/gnm-paper.md)'s ablation is the cleanest statement: normalized waypoints (scaled by each robot's top speed) score **1.0 / 0.95** where raw velocities score 0.73 / 0.54 and unnormalized waypoints 0.42 / 0.26. A TurtleBot and a 10 m/s ATV share that space; the legs, wheels or rotors are the robot's own controller's problem. The same holds for Figure's [Go-Big](../../sources/figure-project-go-big.md), whose SE(2) velocity commands are recoverable from a human's own camera motion. Manipulation has no equivalent: the closest, `xyz + Rot6D + binary gripper`, is exactly the representation that **structurally excludes** [Tien Kung](../../entities/tien-kung.md)'s 15,187 dexterous-hand trajectories from [RoboMIND](../../sources/robomind-paper.md), and that [RoboTwin](../../entities/robotwin.md) 1.0 could only serve to a 6-DoF Piper at 2.4% success. The [research-direction](../../syntheses/world-models/open-questions-and-research-direction.md) page reworded #10 accordingly: not "transfer across radically different bodies" but *transfer where no shared action abstraction exists*.

A second axis is usually conflated with the first ([six-DoF grasp generation](../robotics/six-dof-grasp-generation.md)): *policy-side* heterogeneity (action space, camera rig, control rate) versus *gripper-side* heterogeneity (morphology, closing kinematics). [GraspGen-X](../../sources/graspgenx-paper.md) calls grasp generation "the least transferable component in cross-embodiment settings" — a new gripper cost its predecessor a week of an 8-GPU node — while planning, depth and segmentation port for a config file.

## The mechanisms the wiki has seen

Nineteen distinct answers appear across the sources. Grouped by what they change:

**Change the action representation**

- **Normalize it** — GNM's top-speed scaling; the reason scope 1 is solved.
- **Align it geometrically** — X-VLA's `xyz + Rot6D + gripper`, GR00T's relative-EEF spaces, [Cosmos 3](../../sources/cosmos-3-technical-report.md)'s relative-transform pseudo-actions (9-D AV, 10-D single-arm, 20-D dual-arm, 29-D humanoid, 57-D egocentric, all built from ego pose + effector pose + grasp state), [RDT](../../entities/rdt.md)'s "physically interpretable unified action space," [UMI](../../sources/umi-paper.md)'s wrist-relative trajectories. Cosmos 3's mid-training on this space gives a new embodiment **24.6% vs 0.0%** at 500 iterations.
- **Replace it with a learned codebook** — [latent action tokens](latent-action-tokens.md): UniT's visually anchored RQ-VAE (+18.9 pp over an identical GR00T baseline; 60% zero-shot from human video vs 0%), UniVLA's vision-only codes, [DreamDojo](../../sources/dreamdojo-paper.md)'s continuous latents, [UnifoLM](../../sources/unifolm-wla-1-project-page.md)'s per-body-part RVQ, [SONIC](../../sources/sonic-paper.md)'s FSQ token space as the VLA-to-controller interface. UniT's own negative: the codebook ≈ raw actions on single-embodiment data and **pays only when embodiments are actually mixed**.
- **Emit a controller command instead** — the [WBC interface](../robotics/whole-body-control.md): [HIW-500](../../entities/hiw-500.md)'s 23-D base-velocity + EE-pose + gripper action inherits the vendor's whole-body controller as a fixed layer; [HOVER](../../sources/hover-paper.md) unifies *interfaces* (mode masks over one oracle) rather than bodies.

**Tell the model which body it is**

- **Discrete tags** — GR00T's `LIBERO_PANDA` / `UNITREE_G1_SONIC` / `NEW_EMBODIMENT`; [OXE](../../entities/open-x-embodiment.md)'s tagged trajectories. GR00T N1.7's 29 → 132 state/action expansion is README-only, no ablation ([Isaac-GR00T](../../sources/isaac-gr00t-github.md)).
- **Learned embeddings** — [soft prompts](soft-prompt-cross-embodiment.md): 0.04% of parameters worth +9.2 pts in X-VLA, clustering by hardware configuration, with prompt retrieval proposed and never run; UnifoLM's embodiment embedding; EgoScale's per-embodiment MLP adapters. [ViNT](../../sources/vint-paper.md) did the same for goal *modality* two years earlier.
- **Continuous descriptors** — GraspGen-X's 12-D swept-volume vector; adding a one-hot on top *hurts*, because partitioning the conditioning space blocks sharing across gripper families.
- **Per-embodiment heads** — the default X-VLA argues against, because it acts only at the last layer.

**Let the model infer the body**

- **From recent observations** — GNM's k = 5-frame embodiment context (0.7 vs 0.36 on hard environments); [RMA](../../sources/rma-paper.md)'s extrinsics vector from 0.5 s of proprioception.
- **From its own failures, in context** — [LocoFormer](../../sources/locoformer-paper.md): a biped fails trial 1 and walks by trial 3 with frozen weights; second-layer activations start identical across four humanoid variants and **separate into body-specific clusters within ~5 s**. Trained on **procedurally generated robots that do not exist** ([locomotion lineage](../../syntheses/rl/locomotion-adaptation-lineage.md)).

**Change the data instead of the model**

- **Naive mixing** — [RT-1](../../sources/rt-1-paper.md) lifted new bin-picking 22% → 39% by pooling Kuka data; X-VLA found that adding 290K mixed-robot episodes **dropped** Simpler-WidowX 39.6 → 25.0 until the conditioning recipe was in place. [π0.5](../../sources/pi-zero-5-paper.md): 97.6% of its first-phase data is not the target embodiment, and removing either cross-embodiment source degrades it. [DROID](../../entities/droid.md): scene diversity at fixed embodiment beat embodiment diversity. The [scaling-laws page](scaling-laws-vla.md)'s resolution: cross-embodiment data scales *conditional on the conditioning mechanism*.
- **Retarget it** — human motion → robot via SMPL and feasibility filtering ([H2O](../../sources/h2o-paper.md), [ASAP](../../sources/asap-paper.md), [EgoScale](../../sources/egoscale-paper.md): +30% on a G1 tri-finger hand from 22-DoF training data).
- **Normalize at collection** — [RoboMIND](../../sources/robomind-paper.md)'s one platform, one protocol; [UMI](../../sources/umi-paper.md) and [RUM](../../sources/robot-utility-models-paper.md)'s fixed-viewpoint rig (Stretch → xArm 7 at a ~10-point cost).
- **Move the abstraction above the body** — PDDL, behavior trees, code-as-policy primitives ([action representation languages](../../syntheses/agents/action-representation-languages.md)); [ASPIRE](../../sources/aspire-paper.md)'s sim-discovered skills guide a real YAM (drawer 0/20 → 11/20). Embodiment-specificity **relocates** into the primitive set rather than disappearing ([code as policy](../agents/code-as-policy.md)).
- **Pick the nearest checkpoint** — [MolmoAct2](../../sources/molmoact2-github-repo.md)'s guidance: fine-tune from the nearest embodiment's checkpoint, not the generalist. The practitioner's version of prompt retrieval.

## The three results to hold onto

1. **Latents are not automatically embodiment-invariant.** Demo-JEPA: planning toward a source robot's own V-JEPA 2.1 future latent "fails across all tasks" — a translator is required even between two similar arms. UniT shows human and humanoid distributions *overlapping* under its codebook; LocoFormer shows representations *diverging* by body within seconds and calls that the goal. Three signs on one question, and no experiment relates them. The [backlog](../../backlog.md)'s "which robot is this?" linear probe on V-JEPA latents is the cheapest way to start.
2. **Transfer weakens with the gap, measurably.** Gemini Robotics 1.5's Motion Transfer: zero-shot ALOHA 0.43 / Franka 0.58 / humanoid 0.40 vs near-zero baselines, and the report itself says the benefit "weakens as the embodiment gap grows" ([GR 1.5](../../sources/gemini-robotics-1-5-report.md)). The credible commercial version is DeepMind's "a few hours, typically under 200 examples" for a new bi-arm ([model page](../../sources/deepmind-gemini-robotics-model-page.md)) — adaptation, not zero-shot.
3. **"Omni-bodied" and "any robot" claims outrun their evidence.** [Skild](../../entities/skild-ai.md)'s S1 names no embodiment; the claim rests on LocoFormer, for locomotion. Waddle's "any arms, grippers, cameras" is contradicted by CaP-X and ASPIRE, which report the primitive API must be extended per body ([code as policy](../agents/code-as-policy.md)).

## Open questions

- **The dexterous-hand hole.** What action space admits multi-fingered hands into a cross-embodiment VLA? Candidates exist (per-body-part RVQ, SONIC's hand tokens, EgoScale's retargeting); none has been compared ([backlog](../../backlog.md)).
- **The language route.** [RT-H](../../entities/rt-h.md) proposed bridging OXE embodiments with human-readable motion language in 2024; the field went to unreadable codebooks and never recorded whether the readable route failed ([action representation languages](../../syntheses/agents/action-representation-languages.md)).
- **Condition the model or normalize the data?** X-VLA and RoboMIND are opposite strategies for the same disease; nobody has run both on one corpus.
- **Bottom of the range.** 5-DoF arms are untested by every cross-embodiment paper in the wiki ([five-DoF analysis](../../syntheses/projects/five-dof-arms-in-robotwin.md)).

## Related concepts

- [Soft prompts](soft-prompt-cross-embodiment.md), [latent action tokens](latent-action-tokens.md), [scaling laws for VLAs](scaling-laws-vla.md), [visual navigation policies](../robotics/visual-navigation-policies.md), [whole-body control](../robotics/whole-body-control.md), [control abstraction levels](../robotics/control-abstraction-levels.md), [six-DoF grasp generation](../robotics/six-dof-grasp-generation.md), [in-context robot learning](in-context-robot-learning.md), [crowdsourced robot training data](crowdsourced-robot-training-data.md).
- [Action representation languages](../../syntheses/agents/action-representation-languages.md), [the abstraction tax](../../syntheses/world-models/abstraction-tax.md), [locomotion adaptation lineage](../../syntheses/rl/locomotion-adaptation-lineage.md), [Ten open questions](../../syntheses/world-models/open-questions-and-research-direction.md) (#10).

## Mentioned in

> [!note] Curated list — the term appears on 100+ pages; the ones below supplied this page's claims.

- Navigation: [GNM](../../sources/gnm-paper.md), [ViNT](../../sources/vint-paper.md), [MBRA](../../sources/mbra-paper.md), [Go-Big](../../sources/figure-project-go-big.md).
- Conditioning: [X-VLA](../../sources/xvla-paper.md), [GraspGen-X](../../sources/graspgenx-paper.md), [Isaac-GR00T](../../sources/isaac-gr00t-github.md), [Gemini Robotics model page](../../sources/deepmind-gemini-robotics-model-page.md).
- Codebooks and interfaces: [UniT](../../sources/unit-paper.md), [DreamDojo](../../sources/dreamdojo-paper.md), [UnifoLM-WLA-1.0](../../sources/unifolm-wla-1-project-page.md), [SONIC](../../sources/sonic-paper.md), [HOVER](../../sources/hover-paper.md), [HIW-500](../../sources/bitrobot-hiw-500-dataset-page.md).
- Mixtures: [RT-1](../../sources/rt-1-paper.md), [π0](../../sources/pi-zero-paper.md), [π0.5](../../sources/pi-zero-5-paper.md), [Cosmos 3](../../sources/cosmos-3-technical-report.md), [Gemini Robotics 1.5](../../sources/gemini-robotics-1-5-report.md), [RoboMIND](../../sources/robomind-paper.md).
- Bodies and humans: [LocoFormer](../../sources/locoformer-paper.md), [RMA](../../sources/rma-paper.md), [H2O](../../sources/h2o-paper.md), [ASAP](../../sources/asap-paper.md), [EgoScale](../../sources/egoscale-paper.md).
- Negatives: [Demo-JEPA](../../sources/demo-jepa-paper.md), [UMI](../../sources/umi-paper.md), [RUM](../../sources/robot-utility-models-paper.md), [ASPIRE](../../sources/aspire-paper.md), [MolmoAct2 repo](../../sources/molmoact2-github-repo.md).
- [Robot Self-Improvement via Human-Video Dynamics Models](../../sources/robot-self-improvement-human-video-dynamics-paper.md) — a *manipulation* instance of the shared-abstraction argument: 6-DoF wrist pose + hand closure, learned from human video, carries policy, dynamics and value models from a Stretch 3 to a Franka Panda (36.7% → 70.0% on the Franka). Two single parallel-jaw arms, so the scope is narrow.
