---
title: DINO-WM on Stretch — concrete experiment plan
type: synthesis
created: 2026-05-09
updated: 2026-05-09
tags: [dino-wm, jepa, stretch, hello-robot, rum, experiment-plan, feasibility, mpc, image-goal]
---

Companion to [LeWM on Stretch — feasibility analysis](lewm-on-stretch-feasibility.md). Same shape — *can a JEPA-style world model run on Stretch with currently-available open assets?* — but for [DINO-WM](../../entities/dino-wm.md) instead of [LeWorldModel](../../entities/leworldmodel.md). **Verdict: DINO-WM is the JEPA-family model closest to deployable on Stretch today** because (a) the encoder is frozen pretrained DINOv2 (no representation training to redo), (b) zero-shot planning needs only goal images (not language), and (c) the Stretch + RUM dataset combination resolves the data blocker.

> [!note] TL;DR
> **DINO-WM-on-Stretch is a more conservative, more achievable variant of LeWM-on-Stretch.** Train only the dynamics predictor on RUM trajectories; reuse frozen DINOv2 patch features. Compare zero-shot image-goal MPC against RUM's BC baseline. The experiment fills a real gap — DINO-WM has no published real-robot result — and inherits all the dataset and platform infrastructure already in place.

---

## Why DINO-WM is the right JEPA-family model to try first on Stretch

Three properties separate DINO-WM from its siblings, all relevant here:

1. **Frozen pretrained encoder.** [DINO-WM](../../entities/dino-wm.md) uses DINOv2 patch features as the latent space; only the dynamics predictor is learned. LeWM trains the encoder end-to-end (with SIGReg regularization). For a real-robot first attempt, *not* having to re-train the encoder is a significant simplification — encoder training is the most data-hungry, GPU-hungry, finicky-loss part of the JEPA recipe ([LeWM howto](../world-models/leworldmodel-howto.md)).
2. **Image-goal planning, not language-conditioned action.** DINO-WM optimizes action sequences against an *observational goal* — a goal image — using the world model as a cost function ([DINO-WM Paper](../../sources/dino-wm-paper.md)). RUM's task set fits this exactly: the task "open this drawer" has a clear goal-state image. No language understanding needed, no reward engineering needed.
3. **Closer to the deployment shape than V-JEPA 2 or JEPA-WMs.** [V-JEPA 2](../../entities/v-jepa-2.md) shipped with action-conditioned post-training on DROID — but for a Franka, not a Stretch. JEPA-WMs evaluated on RoboCasa + Metaworld + DROID — also Franka-aligned. DINO-WM's six demonstrated environments (PushT, Wall, PointMaze, Rope, Granular, Reacher) are 2D/3D control benches, not robot benches; the *missing step* in DINO-WM's published evidence is exactly "show this works on a real robot." Doing that on Stretch is the natural next experiment.

---

## What's available off the shelf

| Asset | Status | Source |
|---|---|---|
| Frozen DINOv2 ViT encoder (any of S/B/L/g) | ✅ Apache-2.0; HuggingFace | [DINOv2 entity](../../entities/dinov2.md) |
| DINO-WM training code | ⚠️ Not confirmed in wiki — check `gaoyuezhou/dino_wm` on GitHub per [DINO-WM source open question](../../sources/dino-wm-paper.md) | [DINO-WM Paper](../../sources/dino-wm-paper.md) |
| Stretch hardware (Stretch 3) | ✅ $20k commercial; ROS 2 + Python; MuJoCo wrapper | [Stretch entity](../../entities/stretch.md) |
| RUM dataset (~5,500 trajectories, 5 tasks, ~40 envs/task) | ✅ Open-source; published format | [RUM Paper](../../sources/robot-utility-models-paper.md), [RUM project page](../../sources/robot-utility-models-website.md) |
| RUM task definitions + goal images | ✅ Documented per task | [RUM Paper](../../sources/robot-utility-models-paper.md) |
| Published Stretch BC baseline (RUM) | ✅ 90% with mLLM retry; 74.4% raw | [RUM Paper](../../sources/robot-utility-models-paper.md) |
| `stable-worldmodel` env zoo + planning API | ⚠️ No Stretch wrapper; Gazebo or MuJoCo bridge needed | [stable-worldmodel entity](../../entities/stable-worldmodel.md) |
| MPC implementation against frozen encoder + learned predictor | Re-implement from DINO-WM paper or `gaoyuezhou/dino_wm` | [DINO-WM Paper](../../sources/dino-wm-paper.md) |

**The unique advantage versus the LeWM-on-Stretch path:** for DINO-WM you only need to train the predictor (~M-class params) on RUM data, not the full encoder + predictor jointly. Single-GPU training is well within reach.

---

## The concrete experiment

### Phase 0 — Verify DINO-WM code exists and runs on PushT

Goal: reproduce DINO-WM's published PushT result locally before touching robot data. Catches environment / dependency / loss-curve issues independent of the Stretch question.

- Acceptance criterion: PushT zero-shot image-goal MPC success ≥ paper's reported number.

### Phase 1 — Reformat RUM trajectories into DINO-WM training format

RUM publishes (RGB observation, relative 6D action, gripper state) sequences at 3.75 Hz, 6 history frames. DINO-WM expects (encoded observation, action) pairs for the dynamics predictor. One-time engineering:

1. Read RUM HDF5 dataset.
2. Pass each RGB frame through frozen DINOv2 to get patch features (`B × N_patches × D`). Cache to disk — this is one-shot, never re-run.
3. Pair (feat_t, action_t, feat_{t+1}) into a predictor training set.

Output: ~5,500 trajectories × ~6–20 frames each = ~50–100k transitions, in DINO-WM-predictor format.

### Phase 2 — Train DINO-WM predictor on RUM data

Per task, train one predictor head. Five tasks (door, drawer, reorientation, tissue, bag) → five predictors. Single-GPU training, hours per task per the [DINO-WM paper](../../sources/dino-wm-paper.md) and [LeWM howto](../world-models/leworldmodel-howto.md) cost profile.

- Optional: train one *unified* predictor across all five tasks. Less likely to converge cleanly without task ID conditioning, but worth a single attempt to compare task-specific vs unified scaling.

### Phase 3 — Evaluate zero-shot image-goal MPC on RUM's evaluation environments

For each task:

1. Provide goal image (RUM provides one per task category).
2. Plan action sequence by optimizing latent-state distance against goal image, using the trained predictor ([DINO-WM Paper](../../sources/dino-wm-paper.md) §planning).
3. Execute on Stretch.
4. Record success rate, time-to-completion, planner cost.

Comparison: against RUM's published per-task BC numbers — Reorientation 68%, Drawer 76%, Door 76%, Tissue 80%, Bag 84% (VQ-BeT, no retry).

### Phase 4 — Ablations

- **Encoder size:** ViT-S vs ViT-B vs ViT-L. Speed–accuracy tradeoff.
- **Predictor capacity:** single layer vs deeper transformer.
- **Planning horizon:** 4 vs 8 vs 16 steps.
- **Goal-image specification:** end-state image vs sequence of subgoal images.

---

## Predicted outcomes (with hedging)

| Outcome | Likelihood | Implication |
|---|---|---|
| **DINO-WM matches or beats RUM-BC on at least one task** | Plausible. RUM tasks vary in difficulty; reorientation (68% BC) has the most room for an alternative method to win. | First published real-robot DINO-WM result. Validates frozen-feature world models for manipulation. |
| **DINO-WM trails RUM-BC on every task by ~5–15pt** | Most likely. BC fits trajectories well at full data; planning-from-cost-function gives up some sample efficiency. | Still publishable as the first real-robot DINO-WM result + concrete benchmark contribution. |
| **DINO-WM cannot solve any task above chance** | Less likely but possible. Goal-image MPC may not localize precisely enough for contact-rich tasks (bag, door). | Important negative result. Distinguishes "JEPA works on 2D control" from "JEPA generalizes to real manipulation" — the gap [JEPA task capabilities](../world-models/jepa-task-capabilities.md) flags. |
| **DINO-WM matches RUM-BC at substantially lower training cost** | Plausible because predictor is small. Worth measuring even if absolute success is below BC. | Efficiency win — predictor-only training vs full BC. |

> [!note] Expectation calibration
> DINO-WM was demonstrated on six classical 2D/3D control envs. Real Stretch tasks involve contact, occlusion, and gripper-tip-precision matters. **Treat DINO-WM-vs-BC parity as the realistic ceiling, not "DINO-WM wins."** The headline result of this experiment is more likely "DINO-WM ran on a real robot for the first time" than "DINO-WM beat BC."

---

## How this differs from LeWM on Stretch

| Property | DINO-WM on Stretch | LeWM on Stretch |
|---|---|---|
| Encoder | Frozen DINOv2 (any ViT size) | Trained end-to-end with SIGReg |
| Training cost | Predictor only — single GPU, hours per task | Encoder + predictor — single GPU, longer per task |
| Real-robot prior demonstration | None — first attempt anywhere | None — first attempt anywhere |
| Risk | Lower — fewer moving parts | Higher — encoder training is finicky |
| Speed at inference | DINO-WM's published 48× claim is LeWM's, not DINO-WM's | LeWM reports up to 48× faster than foundation-model WMs |
| Comparable to RUM-BC | Yes — same data, same robot | Yes — same data, same robot |

**Recommendation: do DINO-WM first.** It's the lower-risk proof of concept. If it works, LeWM is the natural follow-up — same engineering frame, same data, plus the encoder-training step.

---

## What this experiment doesn't answer

- **Does any JEPA model beat BC on RUM tasks at full data?** Plausibly no. BC was tuned for these tasks; JEPA is plausibly more useful for tasks BC has *less* data for, and as a substrate for transfer.
- **Does pretraining on internet video help?** DINO-WM uses DINOv2 (image-pretrained). For video pretraining, V-JEPA 2 is the relevant comparison ([V-JEPA 2](../../entities/v-jepa-2.md)) — and V-JEPA 2-AC's published Franka demonstration is closer to "real-robot zero-shot" than DINO-WM. A V-JEPA-2-AC-on-Stretch experiment is a separate, larger effort.
- **Long-horizon assistive tasks.** DINO-WM is short-horizon, image-goal. The [assistive robotics R&D landscape](../assistive/assistive-robotics-research-landscape.md) flags long-horizon multi-step ADL sequences as one of the seven blocking problems. This experiment does not address it.

---

## Why this is worth doing

1. **First published real-robot DINO-WM.** The literature has DINO-WM on PushT/Wall/PointMaze/Rope/Granular/Reacher; it has *no* real-robot result. Filling that gap is a small but real contribution.
2. **Direct empirical comparison to BC.** Same data, same robot, same task definitions, two methods. Cleaner comparison than is usually possible in robot learning.
3. **The infrastructure exists today.** Frozen DINOv2: download. RUM dataset: download. Stretch: $20k. DINO-WM training code: assumed available; if not, re-implementable from paper. No new hardware, no new dataset collection, no new platform.
4. **The result either matters as a positive signal or as a strong negative signal.** Either DINO-WM works on a real robot (validates frozen-feature world models for manipulation) or it doesn't (sharpens the JEPA-on-real-robot story by showing where the published 2D wins don't transfer).

---

## Sources used in this synthesis

- [DINO-WM Paper](../../sources/dino-wm-paper.md) — primary source for the model, training, planning recipe.
- [DINO-WM entity](../../entities/dino-wm.md) — wiki summary.
- [DINOv2 entity](../../entities/dinov2.md) — frozen encoder substrate.
- [Robot Utility Models Paper (Etukuru et al. 2024)](../../sources/robot-utility-models-paper.md) — dataset + BC baseline.
- [Stretch entity](../../entities/stretch.md), [Hello Robot entity](../../entities/hello-robot.md) — platform.
- [stable-worldmodel entity](../../entities/stable-worldmodel.md) — env zoo.
- [LeWM-on-Stretch feasibility](lewm-on-stretch-feasibility.md) — sibling synthesis whose recipe this mirrors.
- [JEPA task capabilities](../world-models/jepa-task-capabilities.md) — what JEPA models do and don't do.
- [Assistive robotics — R&D landscape](../assistive/assistive-robotics-research-landscape.md) — broader applicability context.

## Related

- [LeWM on Stretch — feasibility analysis](lewm-on-stretch-feasibility.md) — companion synthesis with the larger / riskier variant.
- [LeWM on ROSOrin Pro — feasibility analysis](lewm-on-rosorin-pro-feasibility.md) — educational-tier alternative.
- [JEPA project ladder for ROSOrin Pro](jepa-project-ladder-rosorin-pro.md) — pedagogical project ladder.
- [Stretch as the de-facto assistive-robotics platform](../assistive/stretch-as-assistive-platform.md) — why Stretch is the right substrate.
