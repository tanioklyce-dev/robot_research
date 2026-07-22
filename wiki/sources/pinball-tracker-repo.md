---
title: pinball_tracker GitHub (tanioklyce-dev)
type: source
url: https://github.com/tanioklyce-dev/pinball_tracker
author: tanioklyce-dev (first-party)
published: 2026-07-17 (created)
ingested: 2026-07-21
local_path: ../pinball-tracker (sibling working copy)
format: github-repo
license: MIT
tags: [pinball, object-tracking, heatmap, tracknet, u-net, cvat, labeling, first-party, computer-vision, project]
---

# pinball_tracker GitHub (tanioklyce-dev)

## Summary

First-party implementation of the **fast-ball tracker** scoped in
[pinball-playing-robot](../syntheses/projects/pinball-playing-robot.md): a
heatmap-regression CNN that locates the pinball in gameplay video, with a full
`register → label → train → predict/track` pipeline. Built independently of, and
a few days before, the wiki's [TrackNet ingest](tracknet-huang-2019.md) — and it
independently converged on the same core decision (**[heatmap output over
bounding boxes](../concepts/robotics/heatmap-object-localization.md)**, stacked
frames for motion), for the same stated reason: a pinball is tiny, fast,
motion-blurred and mirror-finished, so single-frame appearance is a poor cue.

Its value to the wiki is as **field evidence** — it is the only source here that
actually built a TrackNet-class tracker and measured it, and it **contradicts two
recommendations** in
[fast-ball-tracking-for-robots](../syntheses/projects/fast-ball-tracking-for-robots.md).
MIT, Python, ~4.6k LOC, 56 commits as of ingest.

## Key facts

- **Model is not literally TrackNet.** A 3-stage **U-Net, ~1.95M params**:
  encoder 32→64→128 + 256 bottleneck, bilinear-interpolate decoder with skip
  connections, 9-channel input (3 stacked RGB frames), single-channel logits at
  full input resolution, pixelwise **weighted BCE** (`pos_weight=50`). No VGG-16
  backbone, no DeconvNet, no per-pixel 256-way softmax — heatmap *regression*
  rather than [V1's classification formulation](tracknet-huang-2019.md).
  Roughly **1/8th the parameters** of a VGG-16-based TrackNet.
- **Playfield homography normalization.** Four clicked corners → canonical
  top-down mm warp, so camera angle is removed before the model sees anything.
  Input size is set entirely by `px_per_mm` (0.5 → ball ≈ 13.5 px).
- **Held-out-by-machine evaluation.** Train `godzilla_sdtm` (Godzilla, 1080p30),
  val `foofighters_deadflip` (Foo Fighters, 1080p60) — different machine *and*
  framerate. No frame-level leakage is structurally possible; the split is by
  whole source.
- **Result:** val **F1 0.878 ± 0.020** steady-state, 0.920 best epoch, 3.4 px
  localization, precision 0.929 on the unseen machine. Train-set F1 was 0.96, so
  the generalization gap is small.
- **Trained on 600 frames.** One 20-second train clip (1,800 rows across 3
  balls) and one 10-second val clip (600 rows, 1 ball).
- **Throughput** ~50 FPS at `px_per_mm=0.5` on a desktop GPU (commit `362abfa`)
  — past real-time for 30fps sources. **Not a Jetson number.**
- **CVAT round-trip labeling** (`labeling/cvat.py`) with a classical
  frame-diff + Kalman **bootstrap** label-proposal engine.
- Tooling posture: 193 tests, `ruff`-clean, pre-commit hook running lint + full
  suite.

## Key claims

- **Classical-CV bootstrap labeling fails on lamp-heavy footage.** The best
  bootstrap configuration tracked **24 of 300 frames (~8%)**; the repo's own
  guidance (`STATUS.md`) is *"for lamp-heavy competitive footage, skip bootstrap
  — hand-label."* On a pinball playfield the roundest, brightest blob is
  frequently a **lit insert**, not the ball, and once the tracker locks onto a
  blinking insert it satisfies the physics gate indefinitely.
- **Halving the warp resolution improved accuracy *and* speed.** Commit
  `362abfa` dropped `px_per_mm` 1.0 → 0.5 expecting a trade-off and got neither:
  F1 0.75 → 0.96 (train-set), localization 7.2 → 4.5 px, throughput ~19 → ~50
  FPS. Attributed to reduced insert confusion at smaller apparent scale.
- **A stationary shiny sphere makes a good hard negative.** The Foo Fighters
  captive ball was deliberately left unlabeled rather than annotated as a
  positive — it is stationary in 90% of frames, so labeling it would both
  contradict the balls-in-play policy and inflate recall with a trivially
  "tracked" target. Val precision of 0.929 indicates the model is not firing on
  it.
- **Measured pinball kinematics** (2,400 labeled rows, playfield mm):
  median **6.8–8.7 mm/frame**, p95 42–59, max **162.5 mm/frame**, peak speed
  **4.87 m/s**. The wiki's only measured ball-speed data.

## Entities mentioned

- [TrackNet](../entities/tracknet.md) — the model family this implements a
  variant of.

## Concepts touched

- [Heatmap-based object localization](../concepts/robotics/heatmap-object-localization.md)
  — independently arrived at, and the project's central design decision.
- [Motion attention](../concepts/robotics/motion-attention.md) — **not**
  implemented; motion is purely implicit via frame stacking, matching TrackNet
  V1/V2. The remaining cheap accuracy lever.

## Related

- [Fast-ball tracking for robots](../syntheses/projects/fast-ball-tracking-for-robots.md)
  — the analysis this project provides field evidence for and against; see its
  **Field evidence** section.
- [Pinball-playing robot](../syntheses/projects/pinball-playing-robot.md) — the
  parent project scoping; this is its fast-loop perception component.
- `docs/REVIEW-2026-07-21.md` in the repo — full code review (findings only, no
  code modified), including a glossary of the tracking vocabulary.

## Open questions

- **Val is one ball flight.** 600 consecutive frames of a single trajectory,
  only 201 human keyframes (the rest CVAT interpolation), and the same set both
  selects the checkpoint and reports the result. The **test split is empty**
  (`pokemon_cooltoy` registered but unlabeled), so there is no unconsumed
  held-out set. `0.878 ± 0.020` is promising but weakly evidenced; labeling the
  third machine is what would upgrade it to a trend.
- **Zero negative examples.** All 2,400 labeled rows are `tracked` — no drained
  playfield, no occlusion. The model has never been shown what "no ball" looks
  like.
- Does the ~1.95M U-Net hold up against a VGG-16-scale backbone on the *same*
  data? No controlled ablation exists — the parameter reduction is evidence, not
  proof.
- No Jetson/edge benchmark yet; the ~50 FPS figure is desktop.
