---
title: RT-2
type: entity
subtype: model
created: 2026-08-04
updated: 2026-08-04
sources: 2
tags: [rt-2, vla, action-tokens, pali-x, palm-e, co-fine-tuning, emergent-capabilities, chain-of-thought, google-deepmind, web-knowledge-transfer]
---

**RT-2** — [Google DeepMind](google-deepmind.md)'s 2023 VLA, and **the paper that named the category**: *"We refer to such category of models as vision-language-action models (VLA)"* ([paper](../sources/rt-2-paper.md), CoRL 2023; [announcement blog](../sources/rt-2-deepmind-blog.md)). Everything this wiki files under [VLA](../concepts/learning/vla-models.md) inherits its terminology here.

> [!note] Promoted from secondhand stub to primary, 2026-08-04
> This page was created hours earlier from [RT-H](../sources/rt-h-paper.md)'s description of RT-2, with a warning that the primary was un-ingested. Both the paper and the blog are now ingested and the secondhand framing is retired.

## The recipe

Take a pretrained VLM, **express robot actions as text tokens**, and drop them into the training mixture exactly like natural language. Then **co-fine-tune** on web vision-language tasks *and* robot trajectories together rather than fine-tuning on robot data alone.

- **Backbones:** RT-2-**[PaLI-X](pali-x.md) (55B)** and RT-2-**PaLM-E (12B)**.
- **Actions:** 256 bins per dimension mapped onto existing text tokens. The mapping is **backbone-specific** — PaLI-X has unique tokens for integers up to 1000 so bins map directly; PaLM-E requires overwriting the 256 least-frequently-used tokens.
- **Data:** [RT-1](rt-1.md)'s Kitchen corpus on the [Everyday Robots](everyday-robots.md) mobile manipulator.

**Co-fine-tuning is the load-bearing choice** — it keeps the model seeing web data so it retains its concept vocabulary instead of collapsing onto the robot distribution. The direct precursor of [π0.5](pi-zero-5.md)'s co-training thesis and of [Knowledge Insulation](../concepts/learning/knowledge-insulation.md)'s stop-gradient answer to the same corruption problem.

## Results (6,000 evaluation trials)

| Model | Seen | **Unseen avg** |
|---|---:|---:|
| [RT-1](rt-1.md) | 92 | 32 |
| MOO | 75 | 35 |
| **RT-2-PaLI-X-55B** | 91 | **62** |
| **RT-2-PaLM-E-12B** | 93 | **62** |
| R3M / VC-1 | 45 / 63 | 12 / 10 |

**Seen-task performance is flat versus RT-1. The entire gain is generalization** — ~2× over the next two baselines, ~6× over R3M/VC-1. The two variants tie on average; PaLM-E is better on *hard* splits, PaLI-X on easy ones.

**Emergent capabilities** (none present in robot training data): symbol understanding (*"push coke can on top of heart"*), reasoning (math, logos, nutrition, color), and human recognition (*"move the coke can to the person with glasses"*) — **3× the next best baseline** on average. **Chain-of-thought** fine-tuning adds multi-stage inference: a rock as an improvised hammer, an energy drink for someone tired. The first embodied-CoT result in this lineage, later formalized by [MolmoAct](molmoact.md)'s depth/trace tokens.

**Language-Table** (open-source sim, PaLI-3B): **90** vs LAVA 77, RT-1 74, BC-Zero 72 — a comparison surface outside Google's own suite.

> [!warning] Contradiction — 3× vs 2×
> The [DeepMind blog](../sources/rt-2-deepmind-blog.md) headlines *"3x improvement in generalization."* The paper reports **~2×** for generalization (62 vs 32/35) and reserves **3×** for the separate emergent-capability evaluation. **Cite 2× for generalization, 3× for emergent skills.**

## Inference cost — the original network-served policy

> *"It is infeasible to run [these models] on standard desktop machines… we deploy them in a multi-TPU cloud service and query this service over the network."*

**55B → 1–3 Hz. 5B → ~5 Hz.** The earliest instance in this wiki of the off-board serving pattern that [SmolVLA](smolvla.md)'s async stack and [MolmoAct2](molmoact2.md)'s FastAPI deployment still work around — and the baseline [TurboVLA](turbovla.md) inverts three years later at **0.2 B / 32 Hz / 0.9 GB on a desktop GPU**. See the [control-rate ladder](../syntheses/platforms/control-rate-ladder.md).

## Limitations
- **Physical skills do not improve.** The authors are explicit that emergent capability is *semantic*; dexterity stays bounded by the robot data. Still the field's shape three years on.
- **No N per emergent category** — per-category orderings (PaLI-X vs PaLM-E on math) are not statistically supported.
- **Nothing released** — no weights, data, or code. The reproduction burden fell to [OpenVLA](openvla.md) a year later.
- [Everyday Robots](everyday-robots.md) was wound down shortly after publication.

## Descendants
[OpenVLA](openvla.md) (open reimplementation) · [RT-H](rt-h.md) (adds a language-motion layer, +15 pp over RT-2) · [VLA-0](vla-0.md) (action-as-text taken further) · [FAST](fast-action-tokenization.md) (replaces naive binning)

## Mentioned in
- [RT-2 paper](../sources/rt-2-paper.md)
- [RT-2 DeepMind blog](../sources/rt-2-deepmind-blog.md)
- [RT-H paper](../sources/rt-h-paper.md) — the flat baseline RT-H's hierarchy beats
