---
title: Per-layer KV conditioning
type: concept
created: 2026-07-25
updated: 2026-07-25
sources: 4
tags: [per-layer-kv-conditioning, vla, action-expert, flow-matching, cross-attention, vlm-interface, molmoact2, architecture]
---

# Per-layer KV conditioning

**Per-layer KV conditioning** is the [VLA](vla-models.md) architecture design introduced by [MolmoAct2](../../entities/molmoact2.md) ([Fang, Duan et al. 2026](../../sources/molmoact2-paper.md), §4.2.1) for coupling a discrete-token VLM backbone to a continuous [flow-matching](flow-matching.md) action expert.

## Definition

The open problem it addresses: **how should a continuous action expert receive context from the VLM?** The standard approach — used by [π0](../../entities/pi-zero.md), [GR00T](../../entities/nvidia-groot.md), and most action-expert VLAs — conditions the expert on the VLM's **final hidden state** (or last-layer output), compressing the whole backbone into a single residual-stream representation.

MolmoAct2 instead conditions the expert **at every layer**. The action expert is a DiT-style transformer with **the same depth as the VLM** (L=36 layers). For each VLM layer ℓ, it collects the keys and values `(K_vlm, V_vlm)` produced by that layer's self-attention, maps them through **learned adapter projections** `P_K, P_V` into the expert's cross-attention width, and each expert block ℓ **cross-attends to the projected KV of the corresponding VLM layer ℓ**:

```
K̃_ℓ = reshape(P_K · K_vlm_ℓ),   Ṽ_ℓ = reshape(P_V · V_vlm_ℓ)
CA(Q_ℓ, K̃_ℓ, Ṽ_ℓ) = softmax(Q_ℓ K̃_ℓ^T / √d_h) Ṽ_ℓ
```

Each expert block runs action self-attention → cross-attention to the VLM KV → MLP, with the flow-time embedding producing DiT-style shift/scale/gate on all three branches.

**Why KV, not hidden states:** attending to keys and values exposes the expert to **the same attention state the VLM itself uses** at that depth — a richer, hierarchical view of visual-semantic features — rather than a single compressed vector. The adapters `P_K, P_V` are separate from the VLM's own attention projections, so the interface stays modular.

**Coupled with [knowledge insulation](knowledge-insulation.md):** during post-training the KV conditioning path is **detached** — the flow loss trains the expert and its adapters without back-propagating through the VLM's keys and values (the VLM is still updated by the discrete next-token loss). In deployment fine-tuning, MolmoAct2 **drops** the detach and lets flow gradients flow through.

## Key references

- [MolmoAct2 paper (Fang, Duan et al. 2026)](../../sources/molmoact2-paper.md), §4.2.1 + Table 11 (the defining source and ablation).
- Contrast: final-hidden-state conditioning — [π0](../../entities/pi-zero.md) / [π0.5](../../entities/pi-zero-6.md) ([Physical Intelligence](../../entities/physical-intelligence.md)), [GR00T N1](../../entities/nvidia-groot.md).

## Related concepts

- [Flow matching](flow-matching.md) — the continuous action expert this interface feeds.
- [Knowledge insulation](knowledge-insulation.md) — the detach applied to the conditioning path in post-training.
- [FAST](../../entities/fast-action-tokenization.md) — the discrete-token side the VLM is pre-trained on before the expert is attached.
- [VLA models](vla-models.md) — the action-head taxonomy.

## Current state

Per-layer KV conditioning is, as of this ingest, a **single-source concept** — MolmoAct2's architectural contribution. Its ablation (LIBERO, [Table 11](../../sources/molmoact2-paper.md)) reports **95.9%** avg vs. **94.0%** for hidden-state conditioning and **94.8%** for a per-head KV variant, a ~1.9-point gain concentrated on Object/Goal/Long. Whether the gain generalizes beyond LIBERO and beyond Molmo2-ER's specific backbone is open. Note the design requires expert depth to match backbone depth (both 36 layers), roughly doubling forward-pass compute versus a shallow-conditioning expert — the paper argues per-layer KV "preserves a similar compute profile," but the head-to-head is against final-hidden-state experts of comparable size.

## Mentioned in

- [MolmoAct2 paper (Fang, Duan et al. 2026)](../../sources/molmoact2-paper.md) — introduces the design.
- [MolmoAct2](../../entities/molmoact2.md) — the model that uses it.
