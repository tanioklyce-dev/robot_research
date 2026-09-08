---
title: "τ: Learning Touch-Augmented Vision-Language-Action Models from Future Visual Supervision (Cheng et al., 2026)"
type: source
url: https://arxiv.org/abs/2607.24485
fetch_url: https://arxiv.org/pdf/2607.24485v3
local_path: raw/2607.24485v3.pdf
sha256: 6a6dcb2ac33072a865875433c1a2e1aa0dfe4fde292c5492b5282970bac94ae6
author: "Ning Cheng, Jinan Xu, Wanlin Li, Yangzhi Chen, Jing Gao, Yiqun Wang, Kelan Peng, Wenjuan Han"
published: 2026-07-27
venue: "arXiv preprint (v1 2026-07-27 → **v3 2026-08-07**, the version read here), cs.RO. 10 pp."
format: paper (PDF)
tags: [tactile-sensing, vla, vtla, contact-rich, insertion, jepa, pi-zero-5, tacaura, gelsight, flow-matching, real-robot, force-vs-vision]
ingested: 2026-09-07
---

## Summary

**The wiki's first measured answer to the question it has been carrying all week — and it points against the vendor claim.** τ bolts a **vision-based tactile** encoder onto a pretrained **[π0.5](../entities/pi-zero-5.md)** VLA and trains it with a JEPA-style auxiliary objective that is discarded at deployment. On four contact-rich real-robot tasks it takes the *same backbone* from **28.75% to 71.25%** average full-task success.

The single most important number is the ablation, because it is a controlled comparison the vendor literature does not have: **remove the tactile module and performance returns to 28.75% — exactly π0.5's vision-only score.** The authors' own reading of the stage breakdown is the sentence this wiki has been looking for:

> **Grasping and picking success rates remain at 100%, indicating that coarse object interaction can still be achieved without touch, whereas precise contact reasoning and execution cannot.**

Top pick from [the awesome-jepa triage](awesome-jepa-github.md), filed one turn earlier as landing on the force-vs-vision seam. It does.

## Why it settles something

The wiki has been holding an open tension since this morning:

- [The contact-rich survey](safe-learning-contact-rich-survey.md): force/torque dominates the literature (~60 works vs ~30 vision, 4 language), and *"high-fidelity contact forces… cannot be obtained from the web."*
- [FLUX-mimic](flux-3-launch.md): ECU insertion into tight-fitting fixtures and seal/cable handling **at Audi**, from a video backbone, **with no force or tactile sensing mentioned**.
- [mimic-video](mimic-video-paper.md): the architecture's paper confirms vision + proprioception only — but **never runs a contact-rich task**, so it settled the sensing question and not the capability one.

τ runs the capability experiment. Its tasks are the ones in dispute: **plug insertion** and **USB insertion** (tight-tolerance geometric alignment — the survey's most-studied class), **stamp press** and **whiteboard erasing** (*"contact-force sensing and modulation under less restrictive geometric constraints"* — the survey's surface-interaction family).

| Model | Plug (Grasp/Align/Insert) | USB | Stamp Press | Whiteboard | **Avg** |
|---|---|---|---|---|---|
| π0 | 100 / 25 / 0 | 100 / 25 / 15 | 100 / 65 / 30 | 100 / 100 / 35 | 20.00 |
| **π0.5** (vision-only base) | 100 / 50 / **20** | 100 / 35 / **20** | 100 / 70 / **35** | 100 / 100 / **40** | **28.75** |
| ForceVLA† | 100 / 85 / **0** | 100 / 45 / 5 | 100 / 100 / 70 | 100 / 100 / 45 | 30.00 |
| ForceFlow† | 90 / 40 / 0 | 85 / 30 / 0 | 90 / 60 / 45 | 95 / 95 / 50 | 23.75 |
| T-Rex† | 100 / 30 / 30 | 95 / 30 / 30 | 100 / 70 / 35 | 100 / 100 / 30 | 31.25 |
| **τ-WristSup.** | 100 / 75 / **60** | 100 / 50 / **40** | 100 / 100 / **90** | 100 / 100 / **95** | **71.25** |
| τ-FrontSup. | 100 / 80 / 65 | 100 / 70 / 50 | 100 / 100 / 75 | 100 / 100 / 85 | 68.75 |
| τ-DualViewSup. | 100 / 70 / 55 | 100 / 50 / 35 | 100 / 100 / 65 | 100 / 100 / 75 | 57.50 |

(† = adapted by the authors to their tactile setup, framework preserved. 20 trials per cell.)

> [!warning] The failure is entirely at the terminal, contact-dependent stage
> **Every model reaches 100% on grasp/pick.** The spread is in completion. The two starkest cases are baselines that all but arrive and then cannot finish:
>
> - **ForceVLA† aligns the plug 85% of the time and inserts it 0%.**
> - **ForceFlow† establishes contact on the whiteboard 95% of the time and completes the wipe 50%.**
>
> That is a precise instrument reading on where vision runs out: not at reaching, not at grasping, not even at making contact — **at the moment the task becomes about what is happening inside the contact**, which is exactly where [the survey says occlusion is maximal and force decides](../concepts/robotics/contact-rich-manipulation.md).

## How it works

Three parts on top of a frozen-ish **π0.5** backbone (flow-matching action expert, language instruction concatenated with proprioceptive state, action chunk `â_{t:t+H}`):

**1. Tactile encoding and adaptation.** Two vision-based tactile sensors on the gripper fingers, each producing a **1-channel normal map plus 2-channel shear map**, separately normalized. A **touch encoder initialized from π0.5's own vision encoder** (shared L/R) embeds them; a **learnable linear adapter** projects into the VLA's latent space. Tokens are concatenated `Z = [Z_vision ; Z_language ; Z_touch]` and consumed by the LLM and action expert like any other modality.

**2. The JEPA-style branch — and its twist.** Their own statement of the difference is the interesting part:

> Distinct from JEPA, which predicts target representations from contextual observations for general representation learning, **our branch predicts future visual feature *changes* from the action-conditioned tactile representation**.

So: given the current tactile tokens *and the actions about to be taken*, a small MLP predictor forecasts **how the visual features will change**. The target is `Δz_future = sg(z_{t+Δ} − z_t)` — a **detached** difference of features from the VLA's own vision encoder. Loss is a **weighted cosine alignment**, and the weights are the sharp detail: each future step is weighted by **the magnitude of tactile variation** (clipped to [0.2, 5.0]), *"to emphasize future task processes with significant contact transitions."* Total loss `L = L_IL + 0.3·L_SSL`.

**3. It is training-only.** *"The predictive branch is used only during training, thereby improving representation quality without increasing inference complexity."* Tactile is still an input at deployment; **the visual supervision is not**.

> [!note] What the design actually claims, stated carefully
> This is **not** "vision can replace touch." It is *"future vision can **teach** touch"* — the video signal supplies a free, dense, action-conditioned training target that turns a tactile encoder from a contact-state detector into a **dynamics predictor**, without any tactile labels and without a tactile world model's inference cost.
>
> That is a genuine third position between the wiki's two poles, and it is orthogonal to the [JE-vs-reconstruction crossover](joint-embedding-vs-reconstruction-paper.md): the prediction is in **latent space**, on **feature differences**, weighted by **tactile change**.

## The ablations, which carry the argument

| Removed | Avg | Δ |
|---|---|---|
| — (full τ-WristSup.) | **71.25** | — |
| Action-sequence conditioning | 58.75 | −12.5 |
| Predictive SSL branch | ~51 (drops of 10/15/20/35 pp by task) | — |
| **Tactile encoding + adaptation** | **28.75** | **−42.5** |

Two readings the paper draws, both worth keeping:

- **Removing the SSL branch leaves intermediate stages unchanged** and costs only final completion — *"the predictive objective helps the model capture the temporal evolution for tactile representations **during sustained contact**."* Sustained contact is precisely the survey's definition of contact-rich.
- **Removing tactile degrades the intermediate stages too** — alignment on insertion, contact establishment on stamp press — while grasping stays at 100%. Hence the conclusion quoted at the top.

## Data infrastructure: TacAura

Genuinely useful, and stated as open-source-to-come (teleoperation tools, synchronization/conversion utilities, dataset).

| | |
|---|---|
| Robot | **Franka Research 3** + Franka Hand |
| Tactile | **DM-Tac WS** vision-based sensors replacing the gripper fingers, **320×240 @ ~40 FPS**, custom 3D-printed adapter |
| Cameras | 2× RealSense **D435i** third-person (640×480, 15 FPS) + 1× wrist **D405** |
| Teleop | **exoskeleton arm kinematically isomorphic to the FR3**, joint-position mapping, **with visualized tactile feedback to the operator** |
| Data | streams timestamp-aligned, downsampled to **10 Hz**, **100 demonstrations per task**, 4 tasks |
| Training | 30,000 steps |

> [!note] The teleoperation detail is the one to steal
> Demonstrations are collected with **tactile feedback visualized to the human operator**. If the demonstrator cannot perceive contact, the demonstrations will not contain contact-appropriate behavior to imitate — a data-collection version of the same argument the paper makes about policies. The wiki's [crowdsourced robot training data](../concepts/learning/crowdsourced-robot-training-data.md) coverage has nothing on tactile-in-the-loop teleoperation.

## Generalization, and where it is thin

Zero-shot on two unseen objects and two unseen distractor sets, for two tasks:

- **Whiteboard erasing is robust**: 95% seen → 90/90% unseen objects → **95/95% under visual clutter**, no degradation.
- **USB insertion is not**: 40% → 25/35% unseen objects (avg 30%), and 40% → 20/25% under distractors (avg 22.5%, **−17.5 pp**). Their reading: *"visual clutter poses a substantial challenge to **target localization and precise alignment**."*

The asymmetry is informative. Clutter hurts the task whose difficulty is *finding and aligning to a small hole* and does not touch the task whose difficulty is *modulating force on a surface* — which is a second, independent signal that the two contact-rich families the survey names really do fail differently.

## Where to hold it at arm's length

- **20 trials per cell.** By the [wiki's standard](../concepts/robotics/robot-policy-evaluation.md) that is roughly ±20 pp — so the **42.5-point** tactile ablation and the **40-point** margin over the best baseline survive comfortably, and the ordering *among* τ's three variants (71.25 / 68.75 / 57.50) does not.
- **Baselines are the authors' adaptations** (†) of ForceVLA, ForceFlow and T-Rex to their sensor setup. Necessary — those methods assume different sensing — and it means the numbers are not those methods' published results.
- **One robot, one gripper, one tactile sensor model, 100 demos/task, four tasks.** The authors name the limits themselves: *"cross-task, cross-embodiment, and cross-sensor transferability remains unexplored."*
- **No comparison against tactile-aware world models**, omitted for *"computational resource constraints"* — which is the most relevant missing baseline given the wiki's [world-action model](../concepts/world-models/world-action-model.md) coverage.
- **Vision-based tactile, not force/torque.** The signal is a high-resolution deformation image, not a wrench. That matters for how the result transfers to the wrist-F/T setups that dominate the classical literature.

## What it does to the wiki's open question

> [!warning] First measurement, and it runs against the vendor claim
> On tight-tolerance insertion, a pretrained VLA with vision and proprioception scores **20%**; the same backbone with tactile scores **60%**. [FLUX-mimic](flux-3-launch.md) claims ECU insertion into tight-fitting fixtures at Audi from a **video backbone with no tactile**, with **no published success rate**.
>
> These are not strictly comparable — different backbone, different data scale, different robot, and one of them has no numbers at all. **But the wiki now has one controlled measurement on the question and zero on the other side**, and the measurement says the terminal contact stage is where the vision-only policy fails.
>
> The honest state: *"force is not recoverable from pixels"* is looking stronger than it did this morning, and the burden has moved. **FLUX-mimic's claim is the one that now needs numbers.**

## Entities mentioned

- [π0.5](../entities/pi-zero-5.md) / [π0](../entities/pi-zero.md) ([Physical Intelligence](../entities/physical-intelligence.md)) — the backbone and the baselines.
- **DM-Tac WS**, **TacAura**, **ForceVLA**, **ForceFlow**, **T-Rex** — no pages. **Franka Research 3** — see [Franka Panda](../entities/franka-panda.md).

## Concepts touched

- [Tactile sensing](../concepts/robotics/tactile-sensing.md) — the strongest measured case for touch in this wiki.
- [Contact-rich manipulation](../concepts/robotics/contact-rich-manipulation.md) — the task families, and where vision runs out.
- [VLA models](../concepts/learning/vla-models.md) — tactile as a fourth token stream into a pretrained VLA.
- [JEPA](../concepts/world-models/jepa.md) — latent prediction repurposed as an auxiliary trainer for a *different* modality.
- [Crowdsourced robot training data](../concepts/learning/crowdsourced-robot-training-data.md) — tactile-in-the-loop teleoperation.
- [Robot policy evaluation](../concepts/robotics/robot-policy-evaluation.md) — 20 trials per cell.

## Open questions

- **Does the future-visual trick work for force/torque instead of vision-based touch?** The supervision needs only *a signal whose dynamics correlate with visual change*. A wrist wrench qualifies, is far cheaper than a GelSight-class sensor, and is what most of the classical literature already has.
- **Would it survive [FLUX-mimic](flux-3-launch.md)'s tasks?** Seals and cables are deformable; every task here is rigid. The survey calls deformable manipulation under-explored, and nothing here touches it.
- **Is the 100% grasp / low-completion signature a general diagnostic?** Every model in Table 1 grasps perfectly and diverges only at completion. If that pattern is reliable, **stage-wise reporting is a cheap detector for "this policy lacks contact sensing"** — and almost no VLA benchmark reports stages.
- **What happens with an actual tactile world model?** The paper skips that baseline for compute reasons, and it is the comparison that would separate *"predictive tactile representation"* from *"tactile representation."*
