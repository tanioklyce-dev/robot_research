---
title: JEPA project ladder for ROSOrin Pro
type: synthesis
created: 2026-05-08
updated: 2026-05-08
tags: [jepa, leworldmodel, lewm, rosorin-pro, education, projects, research-projects]
---

# JEPA project ladder for ROSOrin Pro

Companion to [LeWM on ROSOrin Pro — feasibility analysis](lewm-on-rosorin-pro-feasibility.md) and [JEPA task capabilities](jepa-task-capabilities.md). The feasibility doc concludes that LeWM-on-ROSOrin-Pro is research-grade-not-plug-and-play; this page turns that conclusion into a **project ladder** for an amateur / educational researcher to climb one rung at a time.

## What LeWM is good at (educational framing)

Scoped to LeWM specifically (the lightest single-GPU JEPA — see [JEPA task capabilities](jepa-task-capabilities.md) for the full seven-paper picture):

1. **Image-goal planning (latent-space MPC).** Hand it a goal observation, it plans an action sequence by minimizing latent prediction cost. Up to 48× faster than foundation-model-based world models ([LeWorldModel Paper](../sources/leworldmodel-paper.md)).
2. **Action-conditioned latent dynamics.** Encoder + predictor co-trained end-to-end on raw pixels — distinct from [DINO-WM](../entities/dino-wm.md)'s frozen-feature design.
3. **Surprise / anomaly detection.** Prediction error reliably flags physically implausible events ([LeWorldModel Paper](../sources/leworldmodel-paper.md)).
4. **Latent probing / interpretability.** Physical structure decodable from embeddings via linear probes ([LeWorldModel Paper](../sources/leworldmodel-paper.md)).
5. **Sample-efficient training.** ~15M params, single GPU, hours of wall time on PushT/cube/tworooms/reacher ([howto](leworldmodel-howto.md)).

**What LeWM is *not* good at** — long-horizon hierarchical tasks, multi-task generalization in one model, direct policy emission (no `policy.act(obs)` interface), real-robot deployment (the [LeWM paper](../sources/leworldmodel-paper.md) flags this as an open question; a credible result here would be a small but genuine contribution).

## The ladder

Each project is sized for a single learner with a desktop GPU + [ROSOrin Pro](../entities/rosorin-pro.md) kit. Earlier projects de-risk later ones, but the ladder also serves as menu.

### Tier A — software-only warmups (no robot needed)

#### Project 1 · LeWM hello world
Reproduce PushT planning end-to-end on the desktop GPU. Install → load `quentinll/lewm-pusht` → run `eval.py` → watch the planner solve 2D pushing. Hits the four real install gotchas documented in [LeWM howto](leworldmodel-howto.md) (gym 0.21 metadata, swig, `datasets` pin, HF→ckpt conversion bug).
- **Outcome**: working JEPA install + intuition for the planner-as-cost-model pattern.
- **Effort**: ~1 weekend.
- **Risk**: low. Mostly tooling friction; all gotchas pre-documented.

#### Project 2 · Latent-space probing study
Take pretrained LeWM, freeze it, train linear probes on the embeddings to recover ground-truth state (block xy in PushT, joint angles in reacher). Vary number of trajectories, probe depth, layer choice. Compare to a [DINOv2](../entities/dinov2.md)-feature baseline.
- **Outcome**: small empirical writeup on *what* JEPA latents encode. Echoes [LeWM Paper](../sources/leworldmodel-paper.md)'s probing-interpretability claim with your own evidence.
- **Effort**: ~1–2 weeks.
- **Risk**: low. Pure software.

### Tier B — robot-passive, no learned control

#### Project 3 · Surprise detector on the ROSOrin Pro camera
Stream the Aurora930 RGB feed through a frozen LeWM PushT encoder + predictor. Plot per-frame prediction MSE during normal teleop vs deliberately-staged anomalies (person walks in, gripper drops block, lighting change). The pretrained model is out-of-distribution for this scene, so absolute scores are noisy — the question is whether *relative* surprise still tracks anomalies.
- **Outcome**: cheapest "JEPA touched my robot" milestone. No training, no closed-loop control. Real data going through a JEPA.
- **Effort**: ~1 week.
- **Risk**: low. Pretrained-OOD might be unusable — fallback is to fine-tune briefly on benign ROSOrin footage first.

### Tier C — sim-only deployment

#### Project 4 · ROSOrin-Pro PushT clone in Gazebo
Build a tabletop scene with the [6-DOF arm](../entities/rosorin-pro-arm.md) pushing a single block to a target pose. Write a `stable-worldmodel`-compatible env wrapper around the Gazebo + ROS 2 stack — [stable-worldmodel](../entities/stable-worldmodel.md) doesn't yet ship a Gazebo wrapper, so this is a contributable deliverable. Collect ~thousands of sim trajectories with a scripted controller. Retrain LeWM with the 8-D action space (6 arm + 2 base).
- **Outcome**: a custom-trained LeWM that plans pushing in the ROSOrin sim. The heart of the feasibility doc's recommended path (steps 2–4).
- **Effort**: ~3–6 weeks.
- **Risk**: medium. Action-space retraining is novel; Gazebo env wrapper effort is bounded but real.

### Tier D — sim-to-real on hardware

#### Project 5 · Plan-and-execute on the real arm
Take the LeWM from Project 4. Run image-goal MPC on the physical [ROSOrin Pro](../entities/rosorin-pro.md). Tightly-scoped task: push a single colored block to a target square on a non-reflective mat, fixed camera angle. Measure success rate, sensitivity to starting position, common failure modes.
- **Outcome**: the **first published-class LeWM-on-real-robot result, on educational hardware**. The [LeWM paper](../sources/leworldmodel-paper.md)'s own open question (*"does LeWM scale to real-robot deployment?"*) is unanswered as of 2026-05; even a qualified positive on a $1k–2k kit would be a genuine contribution.
- **Effort**: ~4–8 weeks after Project 4.
- **Risk**: medium-high. HX-12H bus servos are educational-grade — lower repeatability than [Franka](../entities/franka-panda.md). Sim-to-real gap on contact-rich pushing in Gazebo is the dominant uncertainty (see [sim-to-real concept page](../concepts/sim-to-real-transfer.md)).

> [!warning] Hardware-tier tax
> Educational-grade servos introduce noise that small training sets may not cover. Plan for more data and looser success thresholds than research-tier benchmarks would suggest.

### Tier E — research extensions (pick one)

#### Project 6a · OpenClaw + LeWM integration
Use [OpenClaw](../entities/openclaw.md)'s LLM agent to decompose natural-language tasks ("push the red block to the corner") into image goals; LeWM plans the low-level actions. Architectural fit: high-level LLM tool calls + low-level latent MPC. Neither project documents this combination — it's plausible but unproven.
- **Effort**: ~1–2 months on top of Project 5.
- **Risk**: medium. Goal-image generation from language is the bottleneck — may need a small generative-image module to fill the gap.

#### Project 6b · Multi-task LeWM
Train one LeWM across 3–5 ROSOrin tasks. Multi-task generalization in a single LeWM is not yet demonstrated in the literature ([JEPA task capabilities](jepa-task-capabilities.md) flags this as a gap).
- **Effort**: ~2 months on top of Project 4.
- **Risk**: medium. Open research; may genuinely not work without architectural changes.

#### Project 6c · Real-robot teleop dataset
Build a cheap teleop rig (controller → ROS topic → trajectory recorder) and collect real [ROSOrin Pro](../entities/rosorin-pro.md) demos. Compare LeWM trained on real data to the sim-trained version from Project 4. The [DROID](../entities/droid.md)-on-Franka path, scaled down for educational hardware.
- **Effort**: ~2–3 months on top of Project 5.
- **Risk**: medium. The teleop rig is the engineering risk, not the JEPA part — the [RUM](../entities/robot-utility-models.md)-on-[Stretch](../entities/stretch.md) precedent shows the deployment shape works.

## How to pick

| Goal | Path |
|---|---|
| **Learn JEPA deeply, low time commitment** | Projects 1 → 2 → 3. Builds planning + probing + surprise intuition without robot dependencies dominating the timeline. |
| **Real research project worth writing up** | Projects 4 → 5. Months, not weeks. Addresses an open question on accessible hardware. |
| **Reliable downstream automation on ROSOrin Pro** | *Don't start with JEPA* — do behavior-cloning-class methods first (RUM-style). Return to JEPA only when BC ceilings. The [feasibility analysis](lewm-on-rosorin-pro-feasibility.md) is blunt about this. |

## Sources used

- [JEPA task capabilities](jepa-task-capabilities.md) — capability taxonomy.
- [LeWM on ROSOrin Pro — feasibility analysis](lewm-on-rosorin-pro-feasibility.md) — gap analysis + recommended deployment path.
- [LeWorldModel — train and run howto](leworldmodel-howto.md) — install / train / eval recipe + gotchas.
- [LeWorldModel entity](../entities/leworldmodel.md), [LeWorldModel Paper](../sources/leworldmodel-paper.md) — model claims and open questions.
- [ROSOrin Pro](../entities/rosorin-pro.md) + [6-DOF arm](../entities/rosorin-pro-arm.md) — hardware spec.
- [stable-worldmodel](../entities/stable-worldmodel.md) — env zoo coverage and Gazebo gap.
- [OpenClaw](../entities/openclaw.md) — LLM-agent framework on the kit.
- [Robot Utility Models](../entities/robot-utility-models.md) — closest deployment-shape precedent (educational-tier real-robot learned policy).

## Related

- [Joint-Embedding Predictive Architecture](../concepts/jepa.md)
- [Generative-video vs JEPA world models](generative-video-vs-jepa-world-models.md)
- [LeWM on Stretch — feasibility analysis](lewm-on-stretch-feasibility.md) — companion if the platform is reconsidered.
- [Sim-heavy vs real-data paths to generalist policies](sim-heavy-vs-real-data-paths.md)
