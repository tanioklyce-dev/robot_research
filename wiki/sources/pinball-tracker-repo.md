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

## Update (2026-07-22) — the third machine

The `pokemon_cooltoy` test split (empty at ingest, and the subject of this
page's first open question) is now **labeled**: 1,556 rows, source frames
32700–33299, three balls in multiball (600/418/538), all `tracked`. The
decorative **Pokéball toy** was excluded as a hard negative on the same logic as
the Foo Fighters captive ball; all three labeled tracks roam ~470×980 px at
3–11 px/frame median speed, confirming none of them is the stationary sphere.

The project's `best.pt` (the epoch-28 checkpoint behind the 0.878/0.920 figures
above) was then scored on **both** held-out machines with one recipe
(`pbt-predict` → greedy match in image space at 30 px tolerance):

| source (split) | P | R | F1 | loc |
|---|---|---|---|---|
| `foofighters_deadflip` (val) | 0.903 | 0.927 | **0.914** | 6.9 px |
| `pokemon_cooltoy` (test) | 0.572 | 0.540 | **0.555** | 8.8 px |

> [!warning] Corrected 2026-07-22
> This row first read **0.232 F1 / 16.9 px**, computed against labels that were
> **5 frames out of alignment** with the video: the task clip starts at source
> frame 32700, not the 32705 in its filename, and the import trusted the
> filename. The "collapse" reading, and the claim that it reproduced V1's
> tennis→badminton failure, are withdrawn. The bug was invisible to every
> aggregate metric and was caught by a human watching an overlay video and
> noticing the labels trailed the ball.

Foo Fighters reproduces the previously reported baseline (0.914 vs 0.920),
confirming the recipe. **A second venue costs ~0.36 F1** — substantial, but the
model still tracks the ball most of the time (localization ~8.8 px, inside a ball
radius). Residual failures concentrate where the playfield is densest with
**round, shiny, ball-like decorations** (Pokéball toy, Pikachu figurines) and in
the pop-bumper scrum.

The project's original triage of this gap ruled out spatial offset, scale
mismatch, decode threshold, and per-ball/per-segment artifacts — but **not
temporal alignment**, which was the actual cause. A constant frame lag is
invisible to all of those checks; notably the "recall is identical across decode
thresholds, so the model emits no heat at the ball" argument was an artifact of
comparing against ground truth in the wrong place.

> [!note] Magnitude: cross-*court*, not cross-*sport*
> An earlier version of this page claimed the result matched V1's zero-shot
> tennis→badminton **35.2 F1 / 22.9% recall**. With corrected labels it does
> not — 0.555 is a different regime, and the resemblance was produced by the
> alignment bug. The honest comparison is V1's 10-fold cross-validation, where
> recall drops **97.3 → 75.7** across courts and lighting *within* one sport.
> A per-venue penalty is real; a collapse is not.

**Methodology correction with teeth.** The project's own eval recipe silently
depends on `--max-peaks` matching the clip's ball count. At the default of 4,
the *val* clip (one ball in play) scores **0.537 F1 at precision 0.376** —
manufactured peaks, not a real regression. Any TrackNet-family evaluation that
caps peaks above the true object count will understate precision the same way;
this is the practical face of the multi-ball formulation question in
[fast-ball-tracking §8](../syntheses/projects/fast-ball-tracking-for-robots.md).

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

- ~~**Val is one ball flight** ... labeling the third machine is what would
  upgrade it to a trend.~~ **Answered 2026-07-22 — and the answer is negative.**
  The third machine was labeled and the same checkpoint scores **0.555 F1** on
  it (after correcting a 5-frame label misalignment that first made it read
  0.232). The 0.878/0.920 val figure was one generalization *point*, not a
  trend; see the Update section above. Val remains one ball flight and still both
  selects the checkpoint and reports its own result, so that methodological
  caveat stands independently.
- ~~**What actually fixes the domain gap here is untested.**~~ **Partly answered
  2026-07-22:** training on **two** machines (Godzilla + Foo Fighters, Pokémon
  still held out) lifts the held-out score **0.555 → 0.638**, and a fixed-volume
  control attributes **+0.043 to diversity** and **+0.040 to the extra data**.
  Real, at roughly +0.04 F1 per cabinet labeled. **Update 2026-07-23:** two
  *clutter-matched* machines (Avengers IQ + Elvira HoH, both dense with round
  decorations) added to training lift the val-selected Pokémon score to **0.606**
  and push **precision to 0.735** (the highest recorded; precision was the
  failure) with best-yet localization 6.9 px — but they do **not** beat plain
  diversity on aggregate F1 (0.639 vs Godzilla+FF's 0.638 on `last.pt`). Labeling
  for the failure mode improved the error *profile*, not the headline number. See
  [fast-ball-tracking §9](../syntheses/projects/fast-ball-tracking-for-robots.md). [Background
  estimation](../sources/tracknetv3-repo.md) and [motion
  attention](../concepts/robotics/motion-attention.md) remain untried. See
  [fast-ball-tracking §9](../syntheses/projects/fast-ball-tracking-for-robots.md).
- ~~**Does augmentation substitute for domain diversity?**~~ **Answered
  2026-07-22: no.** Directional photometric jitter on the same single train
  machine moved Pokémon **0.555 → 0.566** (small enough to be single-run noise)
  while *improving* Foo Fighters 0.914 → 0.928 on precision. Augmentation hardens what the model already sees;
  it cannot supply an object class absent from training. See
  [fast-ball-tracking §9](../syntheses/projects/fast-ball-tracking-for-robots.md).
- **Zero negative examples.** All 2,400 labeled rows are `tracked` — no drained
  playfield, no occlusion. The model has never been shown what "no ball" looks
  like.
- Does the ~1.95M U-Net hold up against a VGG-16-scale backbone on the *same*
  data? No controlled ablation exists — the parameter reduction is evidence, not
  proof.
- No Jetson/edge benchmark yet; the ~50 FPS figure is desktop.
