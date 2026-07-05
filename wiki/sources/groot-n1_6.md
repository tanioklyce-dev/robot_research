---
title: GR00T N1.6 — Research Page (NVIDIA GEAR)
type: source
url: https://research.nvidia.com/labs/gear/gr00t-n1_6/
author: NVIDIA GEAR
published: 2025-12-15
ingested: 2026-07-04
format: web (research-lab page)
tags: [groot, groot-n1-6, vla, nvidia, gear, cosmos-vlm, embodied-reasoning, state-relative-actions, locomanipulation]
---

## Summary

The GR00T **N1.6** research page. The major change vs [N1.5](groot-n1_5.md) is the VLM backbone — N1.6 swaps Eagle for an **internal NVIDIA Cosmos-2B VLM variant** trained on both general vision-language *and* embodied-reasoning tasks (e.g. next-action prediction). It doubles the DiT (16 → 32 layers), removes N1.5's post-VLM adapter in favor of **unfreezing the top 4 VLM layers**, and shifts to **state-relative action chunks**. Training data expands to bimanual YAM arms, AGIBot Genie1, simulated Galaxea R1 Pro on BEHAVIOR, and Unitree G1 whole-body loco-manipulation. Released 2025-12-15 as [`nvidia/GR00T-N1.6-3B`](https://huggingface.co/nvidia/GR00T-N1.6-3B). No headline benchmark numbers are published on the page.

## Key claims

### Architecture changes vs N1.5
- **VLM backbone → internal NVIDIA Cosmos-2B VLM variant** ([NVIDIA Cosmos](../entities/nvidia-cosmos.md) family), with flexible resolution + native aspect-ratio encoding. Its training incorporates **embodied-reasoning tasks** (next-action prediction) alongside general VL tasks — the first reasoning-integrated backbone in the GR00T line.
- **DiT doubled**: 32 layers (vs 16 in N1.5).
- **Adapter removed**; instead **top 4 layers of the VLM unfrozen** during pretraining (N1.5 kept the VLM fully frozen).
- **State-relative action chunks** for most embodiments, replacing absolute joint angles / EEF positions.

### Training data
- Adds to N1.5's mixture "several thousand hours" of teleoperated data from: **bimanual [YAM](../entities/yam.md) arms, [AGIBot](../entities/agibot.md) Genie1, simulated [Galaxea R1 Pro](../entities/galaxea-r1.md) on the [BEHAVIOR](../entities/behavior-benchmark.md) suite, and whole-body loco-manipulation with [Unitree G1](../entities/unitree-g1.md)** (via [GEAR-SONIC](../entities/gear-sonic.md)).
- Pretraining: **300K steps, global batch size 16,384**. Post-training: typically 10K–30K steps, global batch size ≤1K.

### Results
- No numeric benchmarks on the page. Stated: N1.6 "outperforms N1.5 on both simulated manipulation benchmarks and on real bimanual YAM, AgiBot Genie-1 and Unitree G1 robots."

### Limitations / takeaways
- "Multi-task language following and out-of-distribution task generalization continue to be challenging."
- **State-relative actions** enable smoother motion but exhibit **error accumulation** that impacts correction ability.
- N1.6 **converges faster than N1.5 but requires more careful tuning to prevent overfitting**; DAgger and test-time techniques recommended for real-world use.

## Entities mentioned
- [NVIDIA GR00T](../entities/nvidia-groot.md) — the N1.6 version page. [NVIDIA GEAR](../entities/nvidia-gear.md) — lab.
- [NVIDIA Cosmos](../entities/nvidia-cosmos.md) — Cosmos-2B VLM variant as the backbone (a step before N1.7's Cosmos-Reason2-2B).
- [Unitree G1](../entities/unitree-g1.md) — whole-body loco-manipulation embodiment. [AgiBot](../entities/agibot.md) — Genie1 arms.
- [YAM](../entities/yam.md) (bimanual arms), [Galaxea R1](../entities/galaxea-r1.md) (R1 Pro, sim) — now filed as entities.

## Concepts touched
- [VLA models](../concepts/learning/vla-models.md) — reasoning-integrated backbone + state-relative actions are the notable design shifts.
- [Chain of thought](../concepts/learning/chain-of-thought.md) — embodied-reasoning training in the VLM backbone is the System-2 direction.
- [Flow matching](../concepts/learning/flow-matching.md) — DiT action head (doubled depth).

## Open questions
- No published numbers — the wiki records the qualitative claims only; a follow-up paper or model card may quantify the N1.6 > N1.5 gap.
- The Cosmos-2B (N1.6) → Cosmos-Reason2-2B (N1.7) backbone progression is the clearest thread linking the GR00T policy line to the [Cosmos](../entities/nvidia-cosmos.md) reasoning line.
- YAM arms + Galaxea R1 Pro — new embodiments worth entity pages if they recur.
