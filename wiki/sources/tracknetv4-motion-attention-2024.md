---
title: "TrackNetV4: Enhancing Fast Sports Object Tracking with Motion Attention Maps"
type: source
url: https://arxiv.org/abs/2409.14543
author: Arjun Raj, Lei Wang (ANU), Tom Gedeon (Curtin University)
published: 2024-09-22
ingested: 2026-07-21
local_path: raw/2409.14543v1.pdf
venue: arXiv preprint (cs.CV), 2409.14543v1
license: null
format: PDF (17 pages, incl. appendix with full architecture diagrams)
tags: [object-tracking, heatmap, motion-attention, frame-differencing, attention, small-object-detection, computer-vision, sports-analytics, tennis, badminton]
---

# TrackNetV4: Enhancing Fast Sports Object Tracking with Motion Attention Maps

## Summary

A small, honest, **plug-and-play** paper from the Australian National University that adds one module to the [TrackNet](../entities/tracknet.md) family. The observation: V1–V3 are all **purely appearance-driven** — they consume stacked frames and *hope* the convolutions infer motion, but never compute motion explicitly. TrackNetV4 computes it directly, via **absolute frame-differencing maps** passed through a learnable **motion prompt layer** to produce **[motion attention maps](../concepts/robotics/motion-attention.md)**, which are then fused with the network's high-level visual features by element-wise multiplication just before the heatmap output. The module is architecture-agnostic — the authors bolt it onto both **TrackNetV2** and **TrackNetV3** and improve both, at essentially **no speed cost**. Gains are real but modest (**+0.4 to +0.6 F1**), which the paper reports without inflation, including a variant that *hurt* performance. Notably, this is an **undergraduate research project** (COMP3770) that produced a genuinely useful, widely-cited module.

## Key claims

- **The gap being filled (§I).** "Even the state-of-the-art TrackNetV3 does not explicitly leverage motion information." Prior versions rely on temporal dynamics implicitly extracted from consecutive frames, "which often contain noise and irrelevant motion." Explicit motion should suppress that noise and highlight the ball.
- **Absolute frame differencing (§II.B).** Frames are converted to grayscale, normalized to `[0,1]`, and differenced: `D_t = F'_{t+1} − F'_t`. The paper's tweak over the prior motion-prompt work is taking the **absolute value** `D⁺_t`, capturing both intensity increases *and* decreases. Signed differencing maps negative changes to 0, silently discarding half the motion evidence and causing **missed detections**.
- **Motion prompt layer (§II.B, Eq. 1).** A **Power Normalization** function `a_θ` with **learnable parameters** (slope and shift — visualized at 16.24 / 0.28) is applied to `D⁺_t`, yielding motion attention maps `A_t = a_θ(D⁺_t)`. Learnable, so the network decides what counts as salient motion rather than using a fixed threshold.
- **Motion-aware fusion (§II.B, Eq. 3).** High-level visual features `V_t` are extracted from the host TrackNet up to the last conv block (just before the sigmoid), then combined: `H_t = σ(A_t ⊚ V_t)` — element-wise multiplication followed by concatenation. Inserting the fusion at the *end* of the pipeline is deliberate, echoing why V2 added skip connections: tiny-object features decay along the processing pipeline, so the motion signal is injected where it can still steer the output.
- **Improves both hosts, at no speed cost (Table I).**

  | Dataset | Baseline | F1 | +Motion (V4) F1 | Speed (fps) |
  |---|---|---|---|---|
  | Tennis, game-level split | TrackNetV2 | 97.1 | **97.5** | 156.9 → 155.7 |
  | Tennis, clip-level split | TrackNetV2 | 96.4 | **97.0** | 160.9 → 158.6 |
  | Shuttlecock | TrackNetV2 | 90.6 | **91.4** | 163.3 → 161.1 |
  | Shuttlecock | TrackNetV3 | 97.5 | **97.9** | 15.1 → 15.1 |

  The consistent pattern is a **recall gain bought with a small precision loss** — e.g. shuttlecock V2: recall 85.3 → 88.1, precision 96.6 → 94.9. The module finds balls the baseline missed, at the cost of a few more false positives. That is the correct trade for trajectory reconstruction, where a gap is worse than an outlier.
- **Heatmap methods dominate bounding-box detectors here (Table I).** A **YOLOv7** baseline on the shuttlecock dataset scores **68.0 F1** against TrackNetV2's 90.6 and TrackNetV3's 97.5 — a ~30-point gap that empirically vindicates [V1's original decision](tracknet-huang-2019.md) to abandon bounding boxes.
- **New multi-ball dataset (Appendix).** Collected from online sources: **>23,000 training frames, >1,000 test frames**, deliberately harder than existing sets — **multiple balls in play**, **more than one court visible in frame**, **nighttime matches**, **balls camouflaged against the court colour**, mixed resolutions, mostly **amateur** singles and doubles. All balls labelled with the primary ball highlighted, to test whether the model tracks the *right* ball.
- **Reported negative result (Table II).** Two fusion variants: version 1 (Eq. 4) and version 2 (mean motion attention map multiplied into each visual feature map). Trained from scratch on their own dataset, **version 1 is worse than the baseline** (95.7 F1 vs 96.5) while version 2 improves it (97.2). Fine-tuning also proves sensitive to learning rate — at 1e-5 version 2 drops to 91.7 F1. The paper prints all of this rather than only the winning cell.
- **Weights diverge, performance doesn't (Fig. 10).** Per-layer cosine similarity between training-from-scratch and baseline-fine-tuning shows **substantial per-layer weight differences**, especially in the 2-D conv layers, "despite both models achieving very similar performance" — a small, tidy observation about solution multiplicity.

> [!note] Version numbering is not a single lab's roadmap
> V1 and V2 come from NCTU (Taiwan), V3 from a different group ([ACM MM Asia 2023](tracknetv3-repo.md)), and V4 from ANU/Curtin. "TrackNetV4" is a **community-assigned** name for a plug-in module, not the original authors' successor. See [TrackNet](../entities/tracknet.md) for the full lineage.

## Entities mentioned

- [TrackNet](../entities/tracknet.md) — the family this extends; the appendix contains the clearest published summary of V1/V2/V3 architectures.
- [Ultralytics YOLO](../entities/ultralytics-yolo.md) — YOLOv7 serves as the bounding-box baseline that the heatmap approach beats by ~30 F1.

## Concepts touched

- [Motion attention (frame differencing as a learnable prompt)](../concepts/robotics/motion-attention.md) — this paper's core contribution.
- [Heatmap-based object localization](../concepts/robotics/heatmap-object-localization.md) — the substrate the module plugs into; explicitly claimed to work with "any heatmap-based detection and tracking framework."

## Open questions

- The module is claimed to be general to any heatmap tracker, but is only demonstrated on TrackNetV2/V3. Does it help pose estimation or CenterNet-style detectors, where the moving object is large?
- Frame differencing assumes a **static camera**. Broadcast tennis is roughly fixed, but a panning/handheld camera would make the whole frame "motion." No experiment tests camera motion — a serious limitation for any robot-mounted deployment.
- Version 1 vs version 2 fusion differ substantially in outcome (95.7 vs 97.2 F1 from scratch) with no analysis of *why* the mean-attention-map variant wins. Under-explained.
- The multi-ball dataset is the paper's most reusable asset but is only evaluated against TrackNetV2 — no V3 numbers on it.
