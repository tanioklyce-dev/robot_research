---
title: EgoDex dataset
type: entity
subtype: dataset
created: 2026-05-15
updated: 2026-05-15
sources: 2
tags: [dataset, egocentric, apple-vision-pro, hand-tracking, manipulation, pretraining]
---

**EgoDex** — a **829-hour** dataset of egocentric human manipulation video captured with **Apple Vision Pro**, providing accurate wrist and hand tracking across **194 tabletop manipulation tasks** with everyday objects. Released by Apple (cited as `[8]` in EgoScale). Functions in the [EgoScale](../sources/egoscale-paper.md) pretraining pipeline as the *high-precision* complement to ~20k hours of noisier in-the-wild egocentric data.

## What it is
- **829 hours** of egocentric video at unspecified framerate.
- **194 tabletop manipulation tasks** with everyday objects.
- **Captured on Apple Vision Pro** — uses the headset's native hand-tracking + camera-pose estimation pipelines, which are substantially cleaner than off-the-shelf SLAM + hand-pose pipelines applied to in-the-wild video.
- Provides **wrist pose and finger keypoints** as native data products.

## Role in [EgoScale](../sources/egoscale-paper.md)
EgoScale's pretraining mixes ~20k hours of in-the-wild egocentric video (noisy, large) with EgoDex's 829 hours (clean, small). The framing: in-the-wild data provides diversity and scale; EgoDex provides higher-precision kinematic signals that "anchor pretraining while preserving scalability."

## Role in [DreamDojo](../sources/dreamdojo-paper.md)
One of three pretraining datasets in DreamDojo's mixture (In-lab : EgoDex : DreamDojo-HV = 1 : 2 : 10 sampling ratio). DreamDojo also constructs a dedicated **EgoDex Eval** out-of-distribution benchmark on the Fourier GR-1 humanoid, replicating EgoDex's objects and tasks in-lab — the *headline OOD-generalization claim* of DreamDojo is partly proved on EgoDex-derived evals.

The Apple-published primary paper for EgoDex is cited as **Hoque et al. 2025** in DreamDojo (vs `[8]` reference in EgoScale).

## Why it matters in this wiki
- **The first cleanly-tracked egocentric dataset in the wiki's coverage.** Most egocentric corpora (Ego4D, EPIC-KITCHENS) rely on post-hoc SLAM + hand-pose estimation, which is the noise source EgoDex is designed to bypass.
- **Apple's most concrete contribution to the embodied-AI data ecosystem to date.** The dataset itself is the artifact; Apple has not (publicly) shipped a VLA built on it.
- **Reference target for sim-to-real and human-to-robot transfer.** The 21-keypoint hand-pose representation EgoDex provides is the *clean* version of what every other paper has been approximating.

## Related
- [EgoScale Paper](../sources/egoscale-paper.md) — only wiki source citing this dataset.
- [NVIDIA GR00T](nvidia-groot.md) — VLA family pretrained on the same combined corpus (20k hr in-the-wild + EgoDex).
- [Imitation learning](../concepts/learning/imitation-learning.md) — pretraining-from-human-data paradigm.

## Mentioned in
- [EgoScale Paper](../sources/egoscale-paper.md)
- [DreamDojo Paper](../sources/dreamdojo-paper.md)

## Open questions
- **License and access**: EgoScale doesn't transcribe EgoDex's license. Apple's typical research-dataset terms are restrictive; unclear if EgoDex is openly downloadable.
- **Capture details**: framerate, scene count, distinct subjects. DreamDojo's Table 1 lists 30k trajectories across 5 scenes.
- **Original paper**: **Hoque et al. 2025** (per DreamDojo citation). Candidate primary-source ingest.
- **Comparison to Ego4D / EPIC-KITCHENS**: how does the 829-hour Apple-clean corpus compare to the 4000+ hours of unclean in-the-wild egocentric data?
