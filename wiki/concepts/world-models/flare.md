---
title: FLARE (Future Latent Representation Alignment)
type: concept
created: 2026-07-04
updated: 2026-07-04
sources: 5
tags: [flare, implicit-world-model, latent-alignment, jepa-adjacent, auxiliary-loss, vla, repa]
---

**FLARE (Future LAtent REpresentation Alignment)** — a lightweight **auxiliary loss that adds implicit latent world modeling to a flow-matching robot policy**. Instead of reconstructing future pixels or VAE latents, FLARE makes a policy's internal representation *predict a compact future latent* while it predicts actions: dedicated learnable "future tokens" inside the policy's DiT are aligned (cosine similarity) to the embedding of a future observation. Introduced by NVIDIA GEAR ([FLARE Paper](../../sources/flare-paper.md), May 2025) and adopted as the auxiliary objective in [GR00T N1.5](../../sources/groot-n1_5.md) at coefficient **λ=0.2**.

## How it works
- Total loss `L = L_fm + λ·L_align`: the flow-matching action loss `L_fm` is unchanged; `L_align` is negative cosine similarity between the policy's projected future-token features and a target encoder's embedding of the *future* observation `φ_{t+H}`.
- **Target encoder**: an action-aware SigLIP-2 + Q-former (M=32 tokens), updated by **EMA** (ρ≈0.995) — the same teacher pattern as [JEPA](jepa.md).
- **REPA lineage**: derived from Representation Alignment (used in text-to-image diffusion) but (1) aligns to *future* rather than current embeddings, and (2) uses separate future-token streams that interact with the action stream via self-attention.

## Why it's JEPA-adjacent
FLARE is an **implicit / latent world model** — it predicts future representations, not future pixels — which is the defining commitment of [JEPA](jepa.md). It sits alongside the wiki's other "JEPA-as-auxiliary-inside-a-policy" instance, [VLA-JEPA](../../sources/vla-jepa-paper.md), and contrasts with **reconstruction-based** joint world-model+policy methods (UWM, UVA, [DINO-WM](../../entities/dino-wm.md)) that pay the compute/latency cost of high-fidelity generation and risk action-modeling capacity competing with pixel reconstruction. The practical payoff FLARE emphasizes: because the alignment target needs no action labels, **action-less human egocentric video** can train it (human-video co-training roughly doubles novel-object success — [paper](../../sources/flare-paper.md) §4.3).

## Related concepts
- [JEPA](jepa.md) — the joint-embedding-predictive-architecture family; FLARE is a JEPA-adjacent auxiliary loss with an EMA teacher.
- [World model](world-model.md) — FLARE is the *implicit* (non-reconstructive) corner, applied as a policy co-training signal.
- [Flow matching](../learning/flow-matching.md) — the base action-prediction objective FLARE augments.
- [VLA models](../learning/vla-models.md) — FLARE is compatible with any diffusion/flow-matching VLA; its highest-profile deployment is [GR00T N1.5](../../sources/groot-n1_5.md).

## Mentioned in
- [FLARE Paper](../../sources/flare-paper.md) — primary source.
- [GR00T N1.5 research page](../../sources/groot-n1_5.md) — adopts FLARE at λ=0.2.
