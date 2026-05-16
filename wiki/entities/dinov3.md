---
title: DINOv3
type: entity
subtype: model
created: 2026-05-11
updated: 2026-05-15
sources: 3
tags: [dinov3, vision-foundation-model, self-supervised, vit, meta-fair, dino, frozen-encoder, gram-anchoring]
---

**DINOv3** — Meta AI Research's third major DINO release ([DINOv3 paper, August 2025](../sources/dinov3-paper.md)). **7B-parameter ViT** trained with self-supervised learning at scale; positioned as a **frozen-backbone universal vision encoder** matching CLIP-family weakly-supervised models on global tasks and substantially beating them on dense tasks (segmentation, depth, 3D matching).

## Architecture & training
- **ViT-7B/16** main model. Custom variant with **axial RoPE positional embeddings** + **RoPE-box jittering** (random rescaling of patch coordinates to `[-s, s]`, `s ∈ [0.5, 2]`) for resolution / aspect-ratio robustness.
- **1M iterations** with **constant** LR / WD / EMA / teacher-temperature schedules — no cosine schedule. This is by design: enables indefinite training continuation without a priori horizon estimation.
- Loss composition: `L_DINO + L_iBOT + 0.1 · L_DKoleo`, augmented after main training with **`L_Gram`** ([Gram anchoring](../sources/dinov3-paper.md#gram-anchoring-section-42-the-central-contribution)).
- Data: automatic curation pipeline (Vo et al. 2024 lineage) producing a large "background" web-image pool mixed with a smaller ImageNet-1k specialist set. No metadata, no labels.

## Gram anchoring (central methodological contribution)
DINOv3 introduces **Gram anchoring**: a regularizer that constrains the *Gram matrix* (matrix of pairwise patch-feature similarities) of the student toward that of an earlier-iteration "Gram teacher" with clean dense features. Loss:

```
L_Gram = || X_S · X_Sᵀ  −  X_G · X_Gᵀ ||²_F
```

This decouples dense-feature consistency from global-feature improvement — local features are free to drift, only the *structure* of similarities is anchored. It is the **first clean fix for the long-training dense-feature degradation** in SSL ViTs >300M params, a problem known since DINOv2 but previously unresolved. See [DINOv3 paper §4](../sources/dinov3-paper.md) for details.

A high-resolution variant `L_HRef` (2× resolution + bicubic downsample for the Gram teacher) gives an additional ~2 mIoU on ADE20k.

## Model family (via single-teacher multi-student distillation)
- ViT-S/14, ViT-B/14, ViT-L/14, ViT-H/14+, ViT-7B/16 students distilled from the 7B teacher.
- ConvNeXt-Tiny / -Small / -Base / -Large distillations also produced — the representation is portable beyond ViT.
- Plus a high-resolution adaptation phase + a text-alignment phase (zero-shot retrieval / classification).

## Headline results (frozen 7B backbone, no fine-tuning)
| Task | Dataset | Metric | DINOv3 | DINOv2 (g/14) |
|---|---|---|---|---|
| Detection | COCO | mAP ↑ | **66.1** | — |
| Segmentation | ADE20k | mIoU ↑ | **63.0** (full) / 55.9 (linear) | 49.5 (linear) |
| Segmentation | Cityscapes | mIoU ↑ | **81.1** | 75.6 |
| Depth | NYUv2 | RMSE ↓ | **0.309** | 0.372 |
| Depth | KITTI | RMSE ↓ | **2.346** | 2.624 |

Cross-domain: trained on satellite imagery, beats all prior remote-sensing SSL baselines (DINOv3 paper §8).

## Relationship to DINOv2
DINOv3 is the **architectural and training-recipe successor** to [DINOv2](dinov2.md). Same self-distillation framework + iBOT + Koleo; same frozen-backbone usage pattern. Key changes:

- **7B params** (vs. 1.1B for DINOv2-g/14).
- **Patch size 16** (vs. 14).
- **Constant schedules** (vs. cosine).
- **Gram anchoring** (new).
- **Axial RoPE + box jittering** (vs. learned positional embeddings).
- **1M iterations** (vs. ~625k).

## Position in this wiki
DINOv3 sits one layer below the JEPA / world-model literature. Most JEPA-adjacent papers in this wiki — [DINO-WM](dino-wm.md), [DINO-world](dino-world.md), [JEPA-WMs](jepa-wms.md) — use frozen [DINOv2](dinov2.md) features. **DINOv3 is the natural drop-in upgrade** for that lineage, but no paper in this wiki has yet used it as the encoder (DINOv3 was released August 2025; JEPA-WMs Dec 2025 still used DINOv2-class features at submission time).

[Federico Baldassarre](https://scholar.google.com) is a co-corresponding author on DINOv3 *and* senior author on [DINO-world](../sources/dino-world-paper.md) — the same author bridges the DINO-foundation and DINO-world-model lines.

## Methodological cousin: LeJEPA / SIGReg
[LeJEPA](../sources/lejepa-paper.md) (Balestriero & LeCun, Nov 2025) targets the same problem — SSL training stability at scale — but takes the opposite stance:

- **DINOv3** stays inside the DINOv2 heuristics-heavy paradigm (DINO + iBOT + Koleo + EMA teacher + stop-gradient) and adds Gram anchoring to fix the last known scaling failure.
- **LeJEPA** drops the heuristics entirely; replaces them with a single SIGReg loss that proves embeddings should be isotropic Gaussian.

These are the **two competing 2025 attempts to make large-scale SSL stable**. Their authors are on different floors of the same building. Open question whether they merge in 2026 work.

## Related
- [DINOv2](dinov2.md) — direct predecessor.
- [Meta FAIR](meta-fair.md) — origin lab.
- [Learned latent space](../concepts/world-models/latent-space.md) — DINOv3 produces the embeddings downstream world models predict in.
- [DINO-WM](dino-wm.md) / [DINO-world](dino-world.md) / [JEPA-WMs](jepa-wms.md) — DINOv2 users; candidates for DINOv3 upgrade.

## Mentioned in
- [DINOv3 Paper](../sources/dinov3-paper.md)

## Open questions / TBD
- Has a DINOv3-WM or DINOv3-based world-model paper appeared yet? Worth checking — would be the natural sequel to DINO-WM.
- Public release status: DINOv2 was open-weights Apache 2.0. Same expected for DINOv3 but not verified at ingest time.
