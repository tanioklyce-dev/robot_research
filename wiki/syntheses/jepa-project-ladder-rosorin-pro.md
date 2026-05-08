---
title: JEPA project ladder for ROSOrin Pro
type: synthesis
created: 2026-05-08
updated: 2026-05-08
tags: [jepa, leworldmodel, lewm, rosorin-pro, education, projects, research-projects]
---

# JEPA project ladder for ROSOrin Pro

Companion to [[lewm-on-rosorin-pro-feasibility|LeWM on ROSOrin Pro — feasibility analysis]] and [[jepa-task-capabilities|JEPA task capabilities]]. The feasibility doc concludes that LeWM-on-ROSOrin-Pro is research-grade-not-plug-and-play; this page turns that conclusion into a **project ladder** for an amateur / educational researcher to climb one rung at a time.

## What LeWM is good at (educational framing)

Scoped to LeWM specifically (the lightest single-GPU JEPA — see [[jepa-task-capabilities|JEPA task capabilities]] for the full seven-paper picture):

1. **Image-goal planning (latent-space MPC).** Hand it a goal observation, it plans an action sequence by minimizing latent prediction cost. Up to 48× faster than foundation-model-based world models ([[leworldmodel-paper|LeWorldModel Paper]]).
2. **Action-conditioned latent dynamics.** Encoder + predictor co-trained end-to-end on raw pixels — distinct from [[dino-wm|DINO-WM]]'s frozen-feature design.
3. **Surprise / anomaly detection.** Prediction error reliably flags physically implausible events ([[leworldmodel-paper|LeWorldModel Paper]]).
4. **Latent probing / interpretability.** Physical structure decodable from embeddings via linear probes ([[leworldmodel-paper|LeWorldModel Paper]]).
5. **Sample-efficient training.** ~15M params, single GPU, hours of wall time on PushT/cube/tworooms/reacher ([[leworldmodel-howto|howto]]).

**What LeWM is *not* good at** — long-horizon hierarchical tasks, multi-task generalization in one model, direct policy emission (no `policy.act(obs)` interface), real-robot deployment (the [[leworldmodel-paper|LeWM paper]] flags this as an open question; a credible result here would be a small but genuine contribution).

## The ladder

Each project is sized for a single learner with a desktop GPU + [[rosorin-pro|ROSOrin Pro]] kit. Earlier projects de-risk later ones, but the ladder also serves as menu.

### Tier A — software-only warmups (no robot needed)

#### Project 1 · LeWM hello world
Reproduce PushT planning end-to-end on the desktop GPU. Install → load `quentinll/lewm-pusht` → run `eval.py` → watch the planner solve 2D pushing. Hits the four real install gotchas documented in [[leworldmodel-howto|LeWM howto]] (gym 0.21 metadata, swig, `datasets` pin, HF→ckpt conversion bug).
- **Outcome**: working JEPA install + intuition for the planner-as-cost-model pattern.
- **Effort**: ~1 weekend.
- **Risk**: low. Mostly tooling friction; all gotchas pre-documented.

#### Project 2 · Latent-space probing study
Take pretrained LeWM, freeze it, train linear probes on the embeddings to recover ground-truth state (block xy in PushT, joint angles in reacher). Vary number of trajectories, probe depth, layer choice. Compare to a [[dinov2|DINOv2]]-feature baseline.
- **Outcome**: small empirical writeup on *what* JEPA latents encode. Echoes [[leworldmodel-paper|LeWM Paper]]'s probing-interpretability claim with your own evidence.
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
Build a tabletop scene with the [[rosorin-pro-arm|6-DOF arm]] pushing a single block to a target pose. Write a `stable-worldmodel`-compatible env wrapper around the Gazebo + ROS 2 stack — [[stable-worldmodel|stable-worldmodel]] doesn't yet ship a Gazebo wrapper, so this is a contributable deliverable. Collect ~thousands of sim trajectories with a scripted controller. Retrain LeWM with the 8-D action space (6 arm + 2 base).
- **Outcome**: a custom-trained LeWM that plans pushing in the ROSOrin sim. The heart of the feasibility doc's recommended path (steps 2–4).
- **Effort**: ~3–6 weeks.
- **Risk**: medium. Action-space retraining is novel; Gazebo env wrapper effort is bounded but real.

### Tier D — sim-to-real on hardware

#### Project 5 · Plan-and-execute on the real arm
Take the LeWM from Project 4. Run image-goal MPC on the physical [[rosorin-pro|ROSOrin Pro]]. Tightly-scoped task: push a single colored block to a target square on a non-reflective mat, fixed camera angle. Measure success rate, sensitivity to starting position, common failure modes.
- **Outcome**: the **first published-class LeWM-on-real-robot result, on educational hardware**. The [[leworldmodel-paper|LeWM paper]]'s own open question (*"does LeWM scale to real-robot deployment?"*) is unanswered as of 2026-05; even a qualified positive on a $1k–2k kit would be a genuine contribution.
- **Effort**: ~4–8 weeks after Project 4.
- **Risk**: medium-high. HX-12H bus servos are educational-grade — lower repeatability than [[franka-panda|Franka]]. Sim-to-real gap on contact-rich pushing in Gazebo is the dominant uncertainty (see [[sim-to-real-transfer|sim-to-real concept page]]).

> [!warning] Hardware-tier tax
> Educational-grade servos introduce noise that small training sets may not cover. Plan for more data and looser success thresholds than research-tier benchmarks would suggest.

### Tier E — research extensions (pick one)

#### Project 6a · OpenClaw + LeWM integration
Use [[openclaw|OpenClaw]]'s LLM agent to decompose natural-language tasks ("push the red block to the corner") into image goals; LeWM plans the low-level actions. Architectural fit: high-level LLM tool calls + low-level latent MPC. Neither project documents this combination — it's plausible but unproven.
- **Effort**: ~1–2 months on top of Project 5.
- **Risk**: medium. Goal-image generation from language is the bottleneck — may need a small generative-image module to fill the gap.

#### Project 6b · Multi-task LeWM
Train one LeWM across 3–5 ROSOrin tasks. Multi-task generalization in a single LeWM is not yet demonstrated in the literature ([[jepa-task-capabilities|JEPA task capabilities]] flags this as a gap).
- **Effort**: ~2 months on top of Project 4.
- **Risk**: medium. Open research; may genuinely not work without architectural changes.

#### Project 6c · Real-robot teleop dataset
Build a cheap teleop rig (controller → ROS topic → trajectory recorder) and collect real [[rosorin-pro|ROSOrin Pro]] demos. Compare LeWM trained on real data to the sim-trained version from Project 4. The [[droid|DROID]]-on-Franka path, scaled down for educational hardware.
- **Effort**: ~2–3 months on top of Project 5.
- **Risk**: medium. The teleop rig is the engineering risk, not the JEPA part — the [[robot-utility-models|RUM]]-on-[[stretch|Stretch]] precedent shows the deployment shape works.

## How to pick

| Goal | Path |
|---|---|
| **Learn JEPA deeply, low time commitment** | Projects 1 → 2 → 3. Builds planning + probing + surprise intuition without robot dependencies dominating the timeline. |
| **Real research project worth writing up** | Projects 4 → 5. Months, not weeks. Addresses an open question on accessible hardware. |
| **Reliable downstream automation on ROSOrin Pro** | *Don't start with JEPA* — do behavior-cloning-class methods first (RUM-style). Return to JEPA only when BC ceilings. The [[lewm-on-rosorin-pro-feasibility|feasibility analysis]] is blunt about this. |

## Sources used

- [[jepa-task-capabilities|JEPA task capabilities]] — capability taxonomy.
- [[lewm-on-rosorin-pro-feasibility|LeWM on ROSOrin Pro — feasibility analysis]] — gap analysis + recommended deployment path.
- [[leworldmodel-howto|LeWorldModel — train and run howto]] — install / train / eval recipe + gotchas.
- [[leworldmodel|LeWorldModel entity]], [[leworldmodel-paper|LeWorldModel Paper]] — model claims and open questions.
- [[rosorin-pro|ROSOrin Pro]] + [[rosorin-pro-arm|6-DOF arm]] — hardware spec.
- [[stable-worldmodel|stable-worldmodel]] — env zoo coverage and Gazebo gap.
- [[openclaw|OpenClaw]] — LLM-agent framework on the kit.
- [[robot-utility-models|Robot Utility Models]] — closest deployment-shape precedent (educational-tier real-robot learned policy).

## Related

- [[jepa|Joint-Embedding Predictive Architecture]]
- [[generative-video-vs-jepa-world-models|Generative-video vs JEPA world models]]
- [[lewm-on-stretch-feasibility|LeWM on Stretch — feasibility analysis]] — companion if the platform is reconsidered.
- [[sim-heavy-vs-real-data-paths|Sim-heavy vs real-data paths to generalist policies]]
