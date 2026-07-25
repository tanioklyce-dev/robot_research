---
title: Adaptive depth reasoning
type: concept
created: 2026-07-25
updated: 2026-07-25
tags: [adaptive-depth-reasoning, embodied-cot, depth-tokens, vq-vae, temporal-redundancy, inference-latency, molmoact2, molmoact-think, chain-of-thought]
sources: 1
---

# Adaptive depth reasoning

**Adaptive depth reasoning** is the latency-saving mechanism behind **MolmoAct2-Think**, the reasoning variant of [MolmoAct2](../../entities/molmoact2.md) ([Fang, Duan et al. 2026](../../sources/molmoact2-paper.md), §5). It is a way to keep a geometrically-grounded intermediate reasoning step (predicting depth before acting) **inside the control loop** without paying its full cost at every timestep.

## Definition

**The problem.** Reasoning-augmented VLAs improve action quality by generating dense intermediate representations — depth maps, goal images, point trajectories, world-model rollouts — before emitting an action. But this reasoning **dominates inference latency**: hundreds of tokens must be produced before a single action, making the very mechanism intended to make policies reliable too slow for closed-loop control. [MolmoAct](../../entities/molmoact.md) added depth-token prediction as a reasoning step but re-predicts every depth code at every step.

**The insight — trajectory-level temporal redundancy.** Across consecutive control steps, most of a scene's depth structure is unchanged; only the region the robot is manipulating moves. So re-computing the entire depth grid each step is wasted work.

**The mechanism.** Each observation's depth map (from **Depth Anything V2**) is quantized by a depth **VQ-VAE** into a **10×10 grid of 100 spatial codes**, each one of **128 learned depth-code values** — ordinary autoregressive tokens compatible with the next-token interface. At inference, MolmoAct2-Think:
1. compares the current image to the cached previous image on the same **10×10 grid of 32×32 RGB patches** by cosine similarity;
2. marks a cell **updated** when similarity **< 0.996**;
3. **re-predicts (argmax-decodes) only the updated cells**, and **replays cached codes** for unchanged cells (consumed as known depth-token inputs);
4. conditions the action expert on the filled depth prefix via [per-layer KV conditioning](per-layer-kv-conditioning.md), then generates the continuous action.

The result: **geometric-reasoning cost scales with the fraction of the scene that changes**, not the full 100-token grid.

**Training regularization** (needed because inference conditions on *predicted*, not oracle, depth): 10% of depth-code input tokens are randomly corrupted during fine-tuning, and a learned **per-layer depth gate** (sigmoid, bias init −4) lets each expert layer decide how strongly to use the depth prefix.

## Key references

- [MolmoAct2 paper (Fang, Duan et al. 2026)](../../sources/molmoact2-paper.md), §5 — the defining source.
- [MolmoAct](../../entities/molmoact.md) (Lee et al. 2025) — the non-adaptive depth-token predecessor.
- Related "embodied CoT" lineage: goal-image prediction (CoT-VLA), point trajectories, world-model rollouts — see [chain-of-thought](chain-of-thought.md).

## Related concepts

- [Chain-of-thought](chain-of-thought.md) — depth tokens are a **non-textual "embodied CoT"** reasoning step.
- [Per-layer KV conditioning](per-layer-kv-conditioning.md) — how the depth prefix conditions the action expert.
- [Variational autoencoder](variational-autoencoder.md) — the VQ-VAE family the depth quantizer belongs to.
- [World model](../world-models/world-model.md) — the heavyweight alternative (per-step rollouts) adaptive depth is positioned against.

## Current state

Single-source concept as of this ingest. On [LIBERO](../../entities/libero.md), MolmoAct2-Think edges MolmoAct2 (**98.1** vs 97.2 avg), with the largest gain (+2.2) on the hardest suite (Long) — evidence the depth pathway is a real, non-incidental gain rather than saturation noise. The **latency claim is viewpoint-dependent**: the paper notes the biggest savings come in third-person setups where the background is largely static; egocentric/mobile views (where the whole scene moves) offer fewer replayable cells. Even so, MolmoAct2-Think runs at only **12.71 Hz** vs. plain MolmoAct2's **55.79 Hz** — adaptive depth reduces but does not eliminate the reasoning tax, leaving open whether the accuracy/interpretability gain justifies ~4× the latency for a given deployment.

## Mentioned in

- [MolmoAct2 paper (Fang, Duan et al. 2026)](../../sources/molmoact2-paper.md) — introduces the mechanism.
- [MolmoAct2](../../entities/molmoact2.md) — the model (MolmoAct2-Think variant).
