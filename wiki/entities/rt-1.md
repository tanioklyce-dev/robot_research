---
title: RT-1
type: entity
subtype: model
created: 2026-08-04
updated: 2026-08-04
sources: 3
tags: [rt-1, robotics-transformer, imitation-learning, efficientnet, film, tokenlearner, everyday-robots, google, cross-embodiment]
---

**RT-1 (Robotics Transformer 1)** — the **35M-parameter** policy that made a single large multi-task robot model credible (Brohan et al., Robotics at Google + [Everyday Robots](everyday-robots.md), 2022). **~130,000 demonstrations, 700+ tasks, 17 months, a fleet of 13 mobile manipulators**, running at **3 Hz** ([paper](../sources/rt-1-paper.md)).

## Architecture — designed backwards from the control rate

**FiLM-conditioned EfficientNet-B3** (ImageNet-pretrained, 16M params, 6 images → 81 vision-language tokens) → **TokenLearner** (81 → 8 tokens) → Transformer → **discrete action tokens**. Total 35M at 3 Hz.

Two details worth keeping: **identity-initialized FiLM** — the affine dense layers start at zero so the layer is initially an identity and doesn't disrupt the pretrained backbone (it also helps when training EfficientNet from scratch) — and TokenLearner's 10× token compression, which is what buys the control rate. Inference speed was a design constraint, not an afterthought.

## Results (3,000 real-world trials)

| Model | Seen | Unseen | Distractors | Backgrounds |
|---|---:|---:|---:|---:|
| **RT-1** | **97** | **76** | **83** | **59** |
| Gato (37M, retrained on this data) | 65 | 52 | 43 | 35 |
| BC-Z | 72 | 19 | 47 | 41 |
| BC-Z XL (RT-1-sized) | 56 | 43 | 23 | 35 |

Baselines were **retrained on RT-1's data**, not quoted from their own papers. Note **BC-Z XL is worse than BC-Z** — naively scaling the baseline architecture *hurts*. The claim is "this architecture absorbs data," not "bigger is better."

## Heterogeneous data absorption

- **Simulation data** containing objects never seen in the real world: added at **no cost** to real-world performance.
- **Cross-embodiment:** adding **Kuka IIWA** bin-picking data (from QT-Opt) lifts performance on new bin-picking tasks **22% → 39%**, with minimal degradation elsewhere.

> [!note] The cross-embodiment thread starts here
> A **+17 pp gain from another robot's data in 2022**, achieved by *just mixing the data* — no shared latent space, no retargeting, no tokenizer. That naive approach is exactly what [UniT](unit.md) later argues breaks down at humanoid scale (*"forces the model to fit fundamentally different action distributions simultaneously"*). See [latent action tokens](../concepts/learning/latent-action-tokens.md).

## Position in this wiki

The ancestor of the whole [VLA](../concepts/learning/vla-models.md) lineage: [RT-2](rt-2.md) reuses its discrete-action-token interface, [RT-H](rt-h.md) trains on its Kitchen dataset (70K demos, 6 task categories) and beats it, and [OpenVLA](openvla.md) descends from RT-2. It is also the low-level policy inside [SayCan](saycan.md) for 15 long-horizon kitchen instructions — the wiki's [LLM-agent-over-policy](../concepts/agents/llm-agent-architecture.md) pattern in its original form, and the reason the 97%/76% numbers matter, since long chains multiply per-step reliability.

## Limitations
- **No N per cell** — 3,000 trials across 200+ seen instructions means ~10–15 each; aggregate gaps hold, per-task orderings don't.
- **One action at a time, no chunking** — [ACT](act.md) is the same year; the 3 Hz is a *per-action* rate, unlike modern chunked policies.
- **[Everyday Robots](everyday-robots.md) was wound down in 2023**, so neither the platform nor the data is reproducible outside Google.
- No standard-benchmark evaluation — no [LIBERO](libero.md), no external comparison surface.

## Mentioned in
- [RT-1 paper](../sources/rt-1-paper.md)
- [RT-2 paper](../sources/rt-2-paper.md) — the baseline it becomes
