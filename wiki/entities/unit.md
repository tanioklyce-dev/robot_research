---
title: UniT
type: entity
subtype: model
created: 2026-08-04
updated: 2026-08-04
sources: 1
tags: [unit, latent-action-tokens, cross-embodiment, humanoid, rq-vae, visual-anchoring, world-model, xpeng, egodex]
---

**UniT (Unified Latent Action Tokenizer via Visual Anchoring)** — [XPENG Robotics](xpeng-robotics.md) + Tsinghua + HKU (April 2026). A **tri-branch cross-reconstruction tokenizer** that maps human and humanoid actions into one **shared RQ-VAE codebook**, creating what the paper calls a *"unified physical language"* — whose vocabulary is discrete codes, not words ([paper](../sources/unit-paper.md)).

The wiki's primary source for [latent action tokens](../concepts/learning/latent-action-tokens.md), and the strongest existing argument *against* a human-readable action representation.

## Mechanism

Three branches — **visual** (inverse dynamics over frozen [DINOv2](dinov2.md) features), **action** (state + action chunk through embodiment-specific MLPs onto a padded common width), and **fusion** — all quantized by a **shared codebook**. Every quantized token must decode **both** the visual transition (shared decoder, cosine loss) and the action chunk (embodiment-specific decoder).

**Visual anchoring** is the thesis: *"while human and humanoid kinematics differ in structural DoFs, the physical outcomes of their intents share a consistent visual representation."* Forcing actions to predict vision anchors kinematics to consequences; forcing vision to predict actions strips appearance confounders. Tokens encode **relative physical change**, not absolute configuration.

## Two uses

- **VLA-UniT** — [GR00T](nvidia-groot.md) N1.5 + [Qwen2.5-VL](qwen.md); the VLM predicts UniT token indices, a flow-matching head emits embodiment-specific actions. **The prediction target is latent; the output is joint angles.**
- **WM-UniT** — Cosmos Predict 2.5 conditioned on UniT's pre-quantization action features instead of raw actions. Does not leak future observations (the action branch sees only state and action).

## Results

| | |
|---|---|
| RoboCasa GR1, 24 tasks × 50 eps (n=1,200) | **66.7%** vs FLARE 55.0, GR00T-Qwen3 47.8, Diffusion Policy 29.5 |
| **Controlled ablation** | 66.7 vs **47.8** for the same architecture without UniT token prediction — **+18.9 pp from the objective alone** |
| Data efficiency | **45.5% on 10% of data**, ≈ the baseline's full-data 47.8% (**~10× reduction**) |
| Real humanoid (IRON-R01-1.11, 50-D action space) | Pick&Place 30 → 78%, Pouring 5 → 75% |
| OOD (5 axes, n=10–30) | Background 0 → 63.3%, Distractor 10 → 60.0%, Geometry 20 → 73.3% |
| **Zero-shot stacking** (task absent from robot data) | baseline **0%**, no-cross-recon **0%**, UniT+human **60%**, with emergent waist rotation |
| Noise robustness (σ=0.2) | [FAST](fast-action-tokenization.md) degrades **10.7×**, action-only 2.7×, **UniT 1.7×** |

Real-world N is 20–40, where the [audit](../syntheses/platforms/vla-success-rate-audit.md) says nothing under ~17–27 pp separates — but the headline gaps are **40–63 pp** and clear it easily. The **0 → 60% zero-shot** result would survive at almost any n. The 70-vs-78 contrast does not.

**A clarifying negative:** as world-model conditioning, UniT ≈ raw actions on single-embodiment DROID and only pulls ahead under human-humanoid co-training. **The unified interface pays only when embodiments are actually mixed.**

## The cost

A codebook index cannot be read, logged in human terms, or corrected by an operator mid-episode — precisely what [RT-H](rt-h.md)'s language motions buy (40% → 63% from typed corrections). **Neither paper cites the other, and no work in this wiki compares a readable and a latent interface on the same robot.** See [action representation languages](../syntheses/agents/action-representation-languages.md).

## Limitations
- Visual anchoring assumes **visible** consequences — force-dominant, occluded, and in-hand manipulation are untested.
- Transfer evidence is **pick-and-place-shaped** (EgoDex `basic_pick_place`, `pour`).
- RoboCasa GR1 numbers are not comparable to the wiki's [LIBERO](libero.md) table.

## Mentioned in
- [UniT paper](../sources/unit-paper.md)
