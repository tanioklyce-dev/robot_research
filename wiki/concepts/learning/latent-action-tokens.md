---
title: Latent action tokens
type: concept
created: 2026-08-04
updated: 2026-08-30
sources: 5
tags: [latent-action-tokens, cross-embodiment, rq-vae, codebook, unit, univla, visual-anchoring, action-representation, humanoid]
---

# Latent action tokens

**Latent action tokens** are discrete codes from a learned codebook that stand in for actions, shared across embodiments. A policy predicts *tokens* rather than joint values; a per-embodiment decoder turns tokens into that robot's controls. The codebook is the interface — and it is **unreadable by construction**.

This is the field's dominant 2026 answer to cross-embodiment transfer, and the direct competitor to a human-readable action vocabulary. See [action representation languages](../../syntheses/agents/action-representation-languages.md).

## Why the field went here

Human video is abundant; humanoid data is scarce. But kinematics don't match — different DoF counts, control modes, action parameterizations. Two older answers both break down:

- **Motion retargeting** (IK solvers mapping human motion onto a specific robot) is *"labor-intensive, unscalable, and often physically inconsistent,"* and case-by-case per morphology.
- **Naive co-training on mixed embodiments** *"forces the model to fit fundamentally different action distributions simultaneously, often leading to embodiment-specific shortcuts rather than shared representations"* ([UniT](../../sources/unit-paper.md)).

The wiki's earliest datapoint on the naive approach is [RT-1](../../sources/rt-1-paper.md), which simply mixed Kuka IIWA bin-picking data into Everyday Robots data and gained **22% → 39%** on new bin-picking tasks. That worked at 2022 scale and two similar arms; UniT's argument is that it stops working at humanoid scale.

## The design space

[UniT](../../sources/unit-paper.md)'s taxonomy of latent-action architectures, which is the clearest available:

| Design | Failure mode |
|---|---|
| **Action-only** — reconstruct proprioception | severe human/robot distribution shift; no external grounding |
| **Vision-only** — infer intent from pixels ([UniVLA](../../entities/univla.md)) | entangles appearance confounders (texture, lighting); misses fine physical detail |
| **Decoupled vision + action** — independent tokenizers | **disjoint vocabularies**; no representational unification |
| **Cross-reconstruction** ([UniT](../../entities/unit.md)) | — |

**Visual anchoring** is UniT's mechanism and its thesis: *"while human and humanoid kinematics differ in structural DoFs, the physical outcomes of their intents share a consistent visual representation."* Three branches (visual, action, fusion) are quantized by a **shared RQ-VAE codebook**, and every token must decode **both** the visual transition and the action chunk. Forcing actions to predict vision anchors kinematics to consequences; forcing vision to predict actions strips appearance confounders. What survives is the intersection — embodiment-agnostic physical intent.

## What the tokens buy

From [UniT](../../sources/unit-paper.md), the wiki's only primary source here:

- **A measurable objective effect** — VLA-UniT 66.7% vs an architecturally identical GR00T baseline at 47.8% on RoboCasa GR1 (n=1,200). **+18.9 pp from the prediction target alone.**
- **~10× data efficiency** — 45.5% on 10% of the data, matching the baseline's full-data 47.8%.
- **Zero-shot task transfer from human video** — an unseen stacking task: baseline **0%**, VLA-UniT with human co-training **60%**, with emergent waist rotation and head turning mirroring the human demonstrations.
- **Denoising.** At σ=0.2 injected noise, [FAST](../../entities/fast-action-tokenization.md) degrades **10.7×**, an action-only RQ-VAE **2.7×**, UniT **1.7×**. Visual grounding discards kinematic variation with no visual correspondence — useful for messy human motion capture.
- **Representation alignment that propagates** — t-SNE shows human/humanoid clusters separate under raw-action conditioning and **overlapping** under UniT, not just at the token layer but inside the downstream VLA and world model.

And a clarifying negative: as a world-model conditioning interface, UniT ≈ raw actions on **single-embodiment** DROID (PSNR 21.32 vs 21.02), and only pulls away under **human-humanoid co-training** (EgoDex 28.06 vs 24.84). **The unified interface pays only when embodiments are actually mixed.**

## The cost

A codebook index is not inspectable, not loggable in human terms, and **not correctable by a human operator mid-episode** — the three things [RT-H](../../entities/rt-h.md)'s language motions buy, where a typed phrase took a policy from 40% to 63%.

> [!warning] The comparison nobody has run
> No work in this wiki evaluates a **readable** and a **latent** action interface on the same robot and the same tasks. UniT doesn't cite RT-H; RT-H's own proposal to bridge [OXE](../../entities/open-x-embodiment.md) embodiments *with language motions* was never executed. The two traditions are answering the same question and not talking to each other — the single clearest open question on the [action representation languages](../../syntheses/agents/action-representation-languages.md) page.
>
> A [behavior tree](../robotics/behavior-trees.md) is the obvious way to have both — latent tokens at the leaves, readable structure above — and nobody has built it either.

## Limits

- **Visual anchoring assumes visible consequences.** Force-dominant, occluded, or in-hand manipulation has intent a shared visual decoder cannot see.
- **The evidence is pick-and-place-shaped** — EgoDex `basic_pick_place` and `pour` carry the transfer results.
- **One primary source.** UniVLA and universal-action-tokenization work are known here only secondhand.

## Related
- [UniT](../../entities/unit.md) · [UniVLA](../../entities/univla.md) — the instances
- [Action representation languages](../../syntheses/agents/action-representation-languages.md) — the readable/latent tradeoff in full
- [VLA models](vla-models.md) — where the tokens are predicted
- [FAST](../../entities/fast-action-tokenization.md) — an action tokenizer that is *not* cross-embodiment, and degrades 10.7× under noise
- [World-action model](../world-models/world-action-model.md) — WM-UniT conditions video generation on these tokens

## Mentioned in
- [UniT paper](../../sources/unit-paper.md)
- [Bengio et al. 2003 — A Neural Probabilistic Language Model](../../sources/bengio2003-neural-probabilistic-language-model.md) — the ancestor: a learned lookup table over a discrete alphabet, trained jointly with the task. The readability complaint here is a restatement of its central property — the geometry is learned, so nobody specified what the axes mean. See [distributed representations](distributed-representations.md).
- [Introducing Index (Figure AI)](../../sources/figure-index-announcement.md) — Named as one of the published approaches to the human→robot action-label gap that [Figure's Index](../../entities/figure-index.md) leaves entirely unaddressed while claiming *"the world's largest robot training dataset."*
