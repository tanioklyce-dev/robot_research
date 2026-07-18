---
title: FAST (action tokenization) / π0-FAST
type: entity
subtype: method
created: 2026-07-17
updated: 2026-07-17
sources: 3
tags: [fast, action-tokenization, dct, vla, discrete-tokens, autoregressive, physical-intelligence, pi-zero]
---

# FAST (action tokenization) / π0-FAST

**FAST** (*Efficient Action Tokenization for Vision-Language-Action Models*; Pertsch, Stachowicz, Ichter, Driess, Nair, Vuong, Mees, [Finn](chelsea-finn.md), [Levine](sergey-levine.md), 2025 — arXiv 2501.09747) is a **[Physical Intelligence](physical-intelligence.md)** scheme for turning continuous robot actions into a **compact sequence of discrete tokens** using the **Discrete Cosine Transform (DCT)**. **π0-FAST** is the model that results from training [π0](pi-zero.md) to autoregressively predict FAST tokens.

## Why it matters in this wiki

FAST is the discrete-token approach that recurs on two fronts across the wiki:

1. **As a baseline model** — π0-FAST appears in nearly every 2025–2026 VLA comparison ([VLA-0](vla-0.md), [Cosmos 3](../sources/cosmos-3-technical-report.md)) as the autoregressive-discrete-token point of reference.
2. **As a component inside better VLAs** — the [Knowledge Insulation](../concepts/learning/knowledge-insulation.md) recipe used by [π0.7](pi07.md) and [π*0.6](pistar06.md) supervises the VLM backbone with **FAST tokens** (next-token prediction) while a flow-matching expert does the actual continuous control. So FAST lives on inside the current PI flagships even though π0-FAST itself is a weaker standalone policy.

The DCT idea: rather than naïvely binning each action dimension (which explodes token count or caps resolution — the discrete-token tradeoff), FAST transforms action *chunks* into the frequency domain and keeps the significant coefficients, giving a **short, high-resolution** token sequence the VLM can generate like text.

## Where it lands in the taxonomy

The [VLA-0 paper](../sources/vla-0-paper.md) classifies π0-FAST under **custom architecture** (its DCT tokenizer is a bespoke scheme), though it is functionally a **discrete-token** VLA. Either way, it's the "actions-as-discrete-tokens, done efficiently" pole — the opposite of VLA-0's "actions-as-plain-text" and the flow-matching heads of [π0](pi-zero.md)/[SmolVLA](smolvla.md).

## Reported numbers (from ingested sources)

- **LIBERO** ([VLA-0 paper](../sources/vla-0-paper.md), Table I): π0-FAST **86.0** avg with large-scale action pretraining (Spatial 90 / Object 86 / Goal 95 / Long 73); a **π0-FAST-PaliGemma** no-pretraining variant scores 71.8. Below [VLA-0](vla-0.md) (94.7) and [OpenVLA-OFT](openvla-oft.md) (97.1).
- **RoboLab-120** ([Cosmos 3 report](../sources/cosmos-3-technical-report.md), Table 19): π0-FAST **14.9%** avg success vs Cosmos3-Nano 39.7 / π0.5 28.1 / π0 3.5.

## Related

- [Knowledge Insulation](../concepts/learning/knowledge-insulation.md) — uses FAST tokens to supervise the VLM backbone; the reason FAST persists inside [π0.7](pi07.md) / [π*0.6](pistar06.md).
- [π0](pi-zero.md) — the base VLA; π0-FAST = π0 + FAST tokenization.
- [VLA-0](vla-0.md) — the action-as-text contrast; VLA-0 argues FAST-style tokenization is unnecessary complexity.
- [VLA models](../concepts/learning/vla-models.md) — action-head taxonomy.

## Open questions

- **Primary source (arXiv 2501.09747) not yet ingested** — filing it would give the exact DCT pipeline, token-count/compression figures, and the cross-embodiment results, rather than the baseline numbers relayed by [VLA-0](vla-0.md) / [Cosmos 3](../sources/cosmos-3-technical-report.md).

## Mentioned in

- [VLA-0 paper](../sources/vla-0-paper.md) — π0-FAST as a custom-architecture / discrete-token baseline.
- [Cosmos 3 technical report](../sources/cosmos-3-technical-report.md) — π0-FAST as a RoboLab-120 baseline.
- [π0.7 paper](../sources/pi07-paper.md) / [π*0.6 paper](../sources/pistar06-paper.md) — FAST tokens inside the Knowledge Insulation recipe.
