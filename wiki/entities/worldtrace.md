---
title: WorldTrace
type: entity
subtype: method
created: 2026-09-02
updated: 2026-09-02
sources: 2
tags: [worldtrace, video-world-model, memory, kv-cache, rope, attention, drift, nvidia, training-free, long-horizon]
---

**WorldTrace** — a **training-free memory framework for interactive video world models**, from Xindi Wu, Sven Elflein, James Lucas and colleagues at [NVIDIA](nvidia.md). Presented at [Day 2 of the Chicago Booth world-modeling workshop](../sources/chicago-booth-world-modeling-workshop-2026-day2.md) as *"Addressable Memory for Video World Models"* by Aljoša Ošep.

## The failure it names

The demo nobody runs: navigate from A to B in a generated world and then **navigate back**. The returned-to frame does not match the starting frame, and over long rollouts the model drifts and forgets what it has seen.

Two **coupled** failure modes, and separating them is the contribution:

1. **Addressability.** Video world models use rotary position embeddings; learned key-query offsets are bounded by the training context. At inference the agent keeps wandering, so offsets keep growing. *"You may still have earlier frames in your KV cache but the model can't address them anymore because positional offsets are out of distribution."* The memory is present and unreachable.
2. **Content fidelity.** Compressing history by averaging *rotated* embeddings makes different phases cancel, destroying the visual information.

## The mechanism

Split the cache into a fixed-size **summary cache** (compressed distant memory) and a **recent window** (verbatim recent frames). The key move:

> Summary slots do **not** keep their original absolute positions. Each is assigned a **fixed virtual position relative to the current query** — so it stays inside the model's training context *regardless of how long the rollout becomes*.

Framed generally, this makes memory compression a question of **designing a structured sparse approximation to full attention over history**, with two instantiations: **WorldTrace-Field** (recent frames verbatim, summary slots average earlier frames — coarse global information) and **WorldTrace-Landmark** (one-hot rows at detected scene boundaries — episodic scene memory). The baseline it replaces is the sliding window most methods use, which simply evicts everything past a horizon.

Reported qualitatively: recovers garage geometry a sliding-window baseline loses, keeps appearance consistent where the baseline preserves structure but not looks, and navigates past a landmark on a long rollout where the baseline accumulates error.

## Why it matters here

> [!note] Blackwell's problem, met in engineering rather than in theory
> The wiki's [belief-states page](../concepts/world-models/belief-states-and-mixed-states.md) records Blackwell's result that the sufficient statistic for a nonunifilar process is generically **infinite-dimensional**, so any fixed-width latent is lossy by construction. WorldTrace does not escape that — it is still a fixed-size cache. What it shows is that **a large part of observed "forgetting" in video world models is not compression loss at all, but an addressing failure**: the information survives and the model cannot reach it. That is a repairable bug sitting on top of an unrepairable limit, and the two had not been distinguished.

## Related
- [World model](../concepts/world-models/world-model.md) / [generative video vs JEPA world models](../syntheses/world-models/generative-video-vs-jepa-world-models.md).
- [Belief states and mixed states](../concepts/world-models/belief-states-and-mixed-states.md).
- [Genie 3](genie-3.md), [Ctrl-World](ctrl-world.md) — the interactive-video family with the same drift problem.

## Mentioned in
- [Third World Modeling Workshop — Day 2](../sources/chicago-booth-world-modeling-workshop-2026-day2.md) — lightning talk, session 2.

> [!note] Thin entity
> Five-minute talk, no paper ingested. The poster is linked from the workshop programme.
