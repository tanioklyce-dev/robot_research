---
title: "DINOv3 (Siméoni et al., Meta AI Research, 2025)"
type: source
url: https://arxiv.org/abs/2508.10104
local_path: raw/2508.10104v1.pdf
sha256: c68dc50b1f73e1641a592f777984fc360759e84b7fe65ac4f6e1377927f20b2e
author: Oriane Siméoni, Huy V. Vo, Maximilian Seitzer, Federico Baldassarre, Maxime Oquab, et al.
affiliation: Meta AI Research (+ WRI, Inria for two co-authors)
published: 2025-08-13 (v1)
ingested: 2026-05-11
tags: [dinov3, dino, ssl, foundation-model, vit, meta-fair, gram-anchoring, dense-features, distillation, baldassarre]
---

> [!note] Ingest depth
> Read from the **full PDF** (`raw/2508.10104v1.pdf`, 67 pages — a technical report, not a conference paper). Sections 1 (intro), 2 (related work), 3 (training at scale: data + architecture), 4 (Gram anchoring), 5 (post-training: high-res / distillation / text alignment), 6 (benchmarks summary) read in full; appendix on satellite-imagery DINOv3 (Sec. 8) skimmed. Sections 7 (evaluation deep-dive) and 9 (broader impact / model card) skimmed. **This is the SSL foundation-model release; depth focuses on the technical contributions, not the long evaluation tables.**

## Summary

**DINOv3** — the third major release in Meta FAIR's DINO self-supervised-learning line (DINO → DINOv2 → DINOv3), a 7B-parameter ViT-based **foundation vision encoder trained with no annotations**. The paper's headline claim: a **single frozen SSL backbone** can match or beat weakly-supervised (CLIP-family) and supervised state-of-the-art models across both global (classification, OOD) and dense (segmentation, depth, 3D matching) tasks — with substantial gains on dense tasks specifically.

Four technical contributions:

1. **Data scaling** via automatic curation (Vo et al. 2024 lineage): a "background" web-scale image pool, mixed with a smaller specialized set (ImageNet-1k). No metadata, no labels.
2. **7B-parameter ViT** with **axial RoPE positional embeddings + RoPE-box jittering** (random rescaling of patch coordinates to improve resolution/aspect-ratio robustness). Trained for **1M iterations with constant-LR / constant-WD / constant-EMA schedules** — no cosine schedule, no need to know the optimization horizon a priori.
3. **Gram anchoring** — a new regularization that **fixes the long-training dense-feature degradation** observed in DINOv2. The training loss is augmented with a term that pushes the student's *Gram matrix* (pairwise patch similarities) toward that of an earlier-iteration "Gram teacher," which still has clean dense features. **Local features are free to move; only the structure of similarities is anchored.** This is the central methodological contribution.
4. **Single-teacher multi-student distillation** producing a model family (ViT-S/14, ViT-B/14, ViT-L/14, ViT-H/14+, ViT-7B/16, plus ConvNeXt distillations) of varying sizes — making the 7B's representations available at deployment-friendly footprints.

**Headline empirical results (frozen 7B backbone, no fine-tuning):**

- **COCO detection: mAP 66.1** (with frozen backbone — beats specialized fine-tuned pipelines).
- **ADE20k segmentation: mIoU 63.0**.
- ADE20k linear probe: mIoU 55.9 (vs. DINOv2 49.5, AM-RADIOv2.5 53.0, Web-DINO 42.7).
- Cityscapes linear: mIoU 81.1 (DINOv2: 75.6).
- NYUv2 depth RMSE: 0.309 (DINOv2: 0.372).
- KITTI depth RMSE: 2.346 (DINOv2: 2.624).

The 7B + distillation family is positioned as a **drop-in replacement for the DINOv2 family** with substantially better dense features and the same frozen-backbone usage pattern.

## Abstract (verbatim, condensed)

> "Self-supervised learning holds the promise of eliminating the need for manual data annotation, enabling models to scale effortlessly to massive datasets and larger architectures... This technical report introduces DINOv3, a major milestone toward realizing this vision by leveraging simple yet effective strategies. First, we leverage the benefit of scaling both dataset and model size by careful data preparation, design, and optimization. Second, we introduce a new method called **Gram anchoring**, which effectively addresses the known yet unsolved issue of dense feature maps degrading during long training schedules. Finally, we apply post-hoc strategies that further enhance our models' flexibility with respect to resolution, model size, and alignment with text. As a result, we present a versatile vision foundation model that outperforms the specialized state of the art across a broad range of settings, without fine-tuning."

## The dense-feature degradation problem (Section 4.1)

DINOv2 (and SSL ViT training generally above ~300M params) suffers a well-known but unresolved pathology in extended training:

- **Global metrics (ImageNet linear probe, classification) keep improving** through 1M+ iterations.
- **Dense metrics (segmentation mIoU, depth, patch-level cosine maps) degrade** after ~200k iterations, sometimes falling below their early levels.
- **Visual signature**: patch-level cosine similarity maps become noisy — features lose locality. The CLS-to-patch cosine similarity rises during training, and *high CLS-patch similarity correlates with degraded dense performance* (Figure 5a).

The paper's diagnosis: the DINO global loss + iBOT local loss combination starts addressing this but becomes unstable as training progresses — the global representation comes to dominate, and patch features lose their independent structure.

## Gram anchoring (Section 4.2, the central contribution)

**Idea**: don't constrain the patch features themselves — constrain the *Gram matrix* (the matrix of all pairwise dot products of L2-normalized patch features in an image).

**Loss**:
```
L_Gram = || X_S · X_Sᵀ  −  X_G · X_Gᵀ ||²_F
```
where `X_S` is the P×d matrix of L2-normalized patch features from the student, `X_G` is the same from a **Gram teacher** (an earlier iteration of the teacher network that still has clean dense features), and the norm is the Frobenius norm.

**Why it works**:
- The Gram matrix encodes only the *structure of pairwise similarities* between patches. Two feature maps that differ by an isometry have the same Gram matrix.
- The student's individual features are free to drift, evolve, and improve on global tasks — only the *patch-to-patch consistency structure* is held fixed.
- This decouples the dense-consistency objective from the global-representation objective.

**Practical details**:
- The Gram teacher is selected as an early iteration of the teacher network — explicitly chosen for its strong dense properties.
- The Gram loss is added as a *refinement step* `L_Ref` partway through training; impact is "almost immediate" — significant dense-task improvements within the first 10k iterations of refinement (Figure 8).
- **High-resolution Gram variant `L_HRef`** (Section 4.3): feed the Gram teacher images at 2× resolution, then bicubic-downsample its features to match student output. The high-resolution features produce smoother Gram matrices that transfer through downsampling. This variant gives an additional bump (ADE20k 55.7 vs. 53.6 at 1× resolution, ablation Figure 9b).

> [!note] Why this matters beyond DINOv3
> Gram anchoring is the **first clean fix for the long-training dense-feature degradation in SSL ViTs**. The paper specifically frames this as "the known yet unsolved issue." Any future SSL training run that wants to scale training time past 200k iterations on a model > 300M params is now expected to use something like this.

## Training recipe (Section 3)

### Loss composition (pre-Gram, Section 3.2)
```
L_Pre = L_DINO + L_iBOT + 0.1 · L_DKoleo
```

- `L_DINO`: original DINO loss — student-teacher cross-entropy on CLS-token output distributions, with two views (global crops).
- `L_iBOT`: image-BERT-style masked-modeling loss on patch tokens (Zhou et al. 2021).
- `L_DKoleo`: **distributed Koleo regularizer** — encourages uniform spread of CLS embeddings; computed in batches of 16 samples, possibly across GPUs (the "D" is for distributed).

After Gram anchoring is added, the full training loss becomes `L_Pre + L_Gram`.

### Architecture details (Section 3.2)
- **7B-parameter ViT** with custom hyperparameters (Table 2 in paper).
- **Axial RoPE** (Rotary Positional Embeddings) — applied separately per axis; each patch is assigned a coordinate in a normalized `[-1, 1]` box.
- **RoPE-box jittering**: at each iteration, the coordinate box is randomly rescaled to `[-s, s]` with `s ∈ [0.5, 2]`. Improves robustness to test-time resolution / aspect-ratio shifts.
- **Patch size 16** (the prior DINOv2 used patch size 14).

### Training schedule
- **Constant** learning rate, weight decay, EMA momentum, teacher temperature — no cosine schedule.
- **1M iterations** (DINOv2 was ~625k).
- Specifically designed to enable indefinite continuation of training without needing to predict the optimization horizon.

## Post-training (Section 5)

After the main 1M-iteration training + Gram refinement:

1. **High-resolution adaptation (Section 5.1)** — 10k additional iterations with mixed-resolution crops: global crops from `{512, 768}`, local crops from `{112, 168, 224, 336}`. Gram anchoring (with 7B as Gram teacher) is essential during this phase — without it, dense-task performance degrades.
2. **Distillation (Section 5.2)** — a novel **single-teacher multi-student** procedure that distills the 7B teacher into a family of smaller models in one pass:
   - ViT-S/14, ViT-B/14, ViT-L/14, ViT-H/14+ (the "+" indicates distilled-from-7B size variant), plus a 7B/16 student.
   - ConvNeXt-Tiny, -Small, -Base, -Large distillations also produced — making the representation available outside ViT.
3. **Text alignment (Section 5.3)** — adds zero-shot capabilities (text-image retrieval, zero-shot classification) without compromising the dense backbone.

## Benchmark snapshot (Section 6, Tables 3+)

DINOv3 is the new SSL state-of-the-art on dense tasks and competitive on global tasks. Selected results, frozen backbone, linear probing:

| Task | Dataset | Metric | DINOv3 7B/16 | DINOv2 g/14 | AM-RADIOv2.5 g/14 | SigLIP 2 g/16 |
|---|---|---|---|---|---|---|
| Segmentation | ADE20k | mIoU ↑ | **55.9** | 49.5 | 53.0 | 42.7 |
| Segmentation | Cityscapes | mIoU ↑ | **81.1** | 75.6 | 78.4 | 64.8 |
| Segmentation | VOC | mIoU ↑ | **86.6** | 83.1 | 85.4 | 72.7 |
| Depth | NYUv2 | RMSE ↓ | **0.309** | 0.372 | 0.340 | 0.494 |
| Depth | KITTI | RMSE ↓ | **2.346** | 2.624 | 2.918 | 3.273 |
| OOD classif. | ObjectNet | Acc ↑ | best in class | — | — | — |
| 3D keypoint match | NAVI | Recall ↑ | best in class | — | — | — |
| Detection (frozen) | COCO | mAP ↑ | **66.1** | — | — | — |

DINOv3 closes the historical "WSL-beats-SSL on global, SSL-beats-WSL on dense" gap by **also matching CLIP-family models on global tasks** while extending the dense-task lead substantially (33–34% relative on depth/tracking/segmentation vs. best-in-class WSL, per Figure 1b).

## Cross-domain generalization (Section 8 — satellite imagery)

A separate experiment trains DINOv3 from scratch on **satellite imagery** (the Vo et al. 2024 curation method generalized to non-natural images). The resulting model surpasses all prior approaches on canonical remote-sensing benchmarks. The PCA visualizations on aerial imagery (Figure 1d) cleanly separate roads, houses, and greenery without any supervision — the paper uses this to argue that **the DINOv3 recipe is domain-agnostic**, applicable to medical imaging, biology, astronomy, particle physics, and any setting where labeled data is scarce but unlabeled data is abundant.

## Entities mentioned

- **[DINOv3](../entities/dinov3.md)** — the subject of this source.
- **[Meta FAIR](../entities/meta-fair.md)** — primary institutional affiliation; all corresponding authors. (The paper uses "Meta AI Research" rather than "FAIR" — the rebranding is recent but the lab is the same.)
- **Federico Baldassarre** — co-corresponding author; also senior author on [DINO-world](dino-world-paper.md). Same person bridges the DINO-foundation and DINO-world-model lines.
- WRI (World Resources Institute) and Inria — affiliations for two co-authors (Tolan / Mairal).

## Concepts touched

- **[DINOv2](../entities/dinov2.md)** — direct predecessor; DINOv3 is the architectural and training-recipe successor.
- **Self-supervised learning** — the central research program; DINOv3 is the latest data point on the SSL-vs-supervised / SSL-vs-WSL trend lines.
- **Frozen-backbone foundation models** — DINOv3 makes the frozen-backbone story stronger across both global and dense tasks.
- **Gram anchoring** — *concept page worth creating*; this paper is the canonical reference.

## Relationship to JEPA / world-model literature

DINOv3 is the **foundation-encoder layer** that downstream JEPA / world-model papers depend on:

- **[DINO-WM](dino-wm-paper.md)** (Zhou et al., NYU + FAIR, Nov 2024) uses **DINOv2** as frozen encoder. The natural next step is a DINOv3-WM variant — open question whether anyone has published one yet.
- **[DINO-world](dino-world-paper.md)** (Baldassarre et al., FAIR, July 2025) uses DINOv2 features for video world models. Baldassarre is co-corresponding on this DINOv3 paper — same author, both lines.
- **[JEPA-WMs](jepa-wms-paper.md)** (Terver et al., FAIR, Dec 2025) — uses DINOv2-class features; predates DINOv3's public release by 4 months.
- **[V-JEPA 2](v-jepa-2-paper.md)** uses a separate video-pretrained ViT — but the SSL methodology DINOv3 advances (Gram anchoring, constant-schedule training) is directly relevant to future video-SSL work.

DINOv3 is also methodologically adjacent to **[LeJEPA](lejepa-paper.md)** (Balestriero & LeCun, Nov 2025) — both target the stability of long SSL training:
- DINOv3 uses **Gram anchoring** (regularize the patch-similarity structure) on top of the DINO/iBOT loss.
- LeJEPA uses **SIGReg** (enforce isotropic-Gaussian embeddings via Epps-Pulley characteristic-function tests) instead of DINO/iBOT.

Both are anti-collapse / anti-degradation regularizers, but they operate on different structures. **LeJEPA argues "drop the heuristics, one regularizer is enough"; DINOv3 stays inside the DINOv2 heuristics-heavy paradigm but adds Gram anchoring to fix the last known failure mode at scale.** Open question whether the two approaches will merge in future Meta-FAIR / NYU work.

## Open questions / TBD

1. **Has DINOv3 been used as the encoder in a JEPA world model yet?** This is the obvious next-step paper given the [DINO-WM](dino-wm-paper.md) → DINOv2 lineage; worth checking.
2. **Gram anchoring vs. SIGReg empirical comparison.** Both target SSL training stability; would a clean head-to-head benchmark exist? Not in this paper.
3. **Does DINOv3 ship publicly as a model release, or only as a research paper?** The DINOv2 release pattern was open weights + code; same expected here but not verified at ingest time.
4. **Robotics adoption.** This wiki has many papers using DINOv2 features for robotics (DINO-WM, et al.). Open question how fast the robotics community has adopted DINOv3 — at the time of this paper (Aug 2025), most ingested robotics-side papers (Mar–Dec 2025) were already using DINOv2 and would need to be re-evaluated against DINOv3.
