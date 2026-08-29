---
title: "RT-1: Robotics Transformer for Real-World Control at Scale"
type: source
url: https://arxiv.org/abs/2212.06817
local_path: raw/2212.06817.pdf
sha256: 81efe669c8fa50ffc7097886dc78a442fa7a8f7f2451684b93069cb9fbeda767
author: Brohan, Brown, Carbajal, Chebotar, Dabis, Finn, Gopalakrishnan, Hausman, Herzog, Hsu, Ibarz, Ichter, Irpan, Jackson, Jesmonth, Joshi, Julian, Kalashnikov, Kuang, Leal, Lee, Levine, Lu, Malla, Manjunath, Mordatch, Nachum, Parada, Peralta, Perez, Pertsch, Quiambao, Rao, Ryoo, Salazar, Sanketi, Sayed, Singh, Sontakke, Stone, Tan, Tran, Vanhoucke, Vega, Vuong, Xia, Xiao, Xu, Xu, Yu, Zitkovich
venue: arXiv 2212.06817v2 (cs.RO), 31 pp.; Robotics at Google + Everyday Robots + Google Brain
published: 2023-08-11
ingested: 2026-08-04
format: pdf
tags: [rt-1, robotics-transformer, imitation-learning, efficientnet, film, tokenlearner, everyday-robots, cross-embodiment, saycan, scaling]
---

# RT-1: Robotics Transformer for Real-World Control at Scale

**Brohan, Brown, Carbajal, Chebotar, Dabis, [Finn](../entities/chelsea-finn.md), …, [Levine](../entities/sergey-levine.md), …, [Xiao](../entities/ted-xiao.md), …, Zitkovich** (50+ authors, alphabetical) — Robotics at Google, [Everyday Robots](../entities/everyday-robots.md), Google Brain.

## Summary

The paper that made "a single large multi-task robot policy" credible. RT-1 is a **35M-parameter** transformer trained on **~130,000 demonstrations spanning 700+ tasks, collected over 17 months by a fleet of 13 [Everyday Robots](../entities/everyday-robots.md) mobile manipulators.** It executes **97% of 200+ seen instructions** and **76% of never-before-seen ones**, at **3 Hz** — and the 3 Hz is architectural, not incidental.

Its thesis is deliberately unglamorous: *"one of the keys to the success of such general robotic models lies with open-ended task-agnostic training, combined with high-capacity architectures that can absorb all of the diverse robotic data."* Not a new loss, not a new representation — **scale plus an architecture that can ingest it, evaluated honestly on real hardware.** Everything in the wiki's [VLA lineage](../concepts/learning/vla-models.md) descends from this.

## Key claims

### Architecture — designed backwards from the control rate

| Stage | Detail |
|---|---|
| Image + instruction tokenization | **FiLM-conditioned EfficientNet-B3**, ImageNet-pretrained; 6 images in, 26 MBConv layers, **81 vision-language tokens**, 16M params |
| Identity-initialized FiLM | FiLM's affine dense layers (`f_c`, `h_C`) initialized to **zero**, so the layer starts as identity and does not disrupt the pretrained backbone — also helps when training EfficientNet from scratch |
| Token compression | **TokenLearner** — 81 tokens → **8** |
| Sequence model | Transformer over the compressed tokens |
| Output | **Discrete action tokens** (arm + base + mode) |
| **Total** | **35M params, 3 Hz** |

TokenLearner and the small parameter count are what buy 3 Hz; the paper is explicit that inference rate was a design constraint, not an afterthought. Compare the [control-rate ladder](../syntheses/platforms/control-rate-ladder.md) — RT-1 sits in Band C, and its successor [RT-2](rt-2-paper.md) at 55B falls to **1–3 Hz served from a TPU cloud**.

### Results (real hardware; **3,000 real-world trials**)

| Model | Seen tasks | Unseen tasks | Distractors | Backgrounds |
|---|---:|---:|---:|---:|
| **RT-1** | **97** | **76** | **83** | **59** |
| Gato (37M, retrained on this data) | 65 | 52 | 43 | 35 |
| BC-Z | 72 | 19 | 47 | 41 |
| BC-Z XL (RT-1-sized) | 56 | 43 | 23 | 35 |

Baselines were **retrained on RT-1's data** rather than quoted from their own papers — the same discipline the [TurboVLA](turbovla-paper.md) authors later applied to efficiency measurements, and still uncommon.

Note **BC-Z XL is worse than BC-Z** (56 vs 72 on seen tasks): naively scaling the baseline architecture *hurts*. The claim is not "bigger is better," it's "this architecture absorbs data; that one doesn't."

### Heterogeneous data absorption — the underrated result

Two experiments that read very differently in 2026 than in 2022:

- **Simulation data.** Adding sim demonstrations with objects never seen in the real world costs **no** real-world performance while adding capability on the sim-only objects.
- **Cross-embodiment.** Adding **Kuka IIWA** bin-picking data (from QT-Opt) to the Everyday Robots data lifts performance on new bin-picking tasks from **22% → 39%**, with only minimal degradation on the original tasks.

> [!note] The cross-embodiment thread starts here
> A **+17 pp gain from a different robot's data**, in 2022, is the earliest datapoint in this wiki for the premise that would become [Open X-Embodiment](../entities/open-x-embodiment.md), [GR00T](../entities/nvidia-groot.md)'s data pyramid, and eventually the [latent-action-token](../concepts/learning/latent-action-tokens.md) line ([UniT](unit-paper.md), [UniVLA](../entities/univla.md)). RT-1 achieves it by **just mixing the data** — no shared latent space, no retargeting, no tokenizer. That naive approach is exactly what [UniT](unit-paper.md) later argues breaks down at humanoid scale ("forces the model to fit fundamentally different action distributions simultaneously, often leading to embodiment-specific shortcuts").

### Long-horizon via SayCan

RT-1 serves as the low-level policy inside [SayCan](../entities/saycan.md) for **15 long-horizon instructions** in two real kitchens, chaining up to ~50 steps. This is the wiki's [LLM-agent-over-policy](../concepts/agents/llm-agent-architecture.md) pattern in its original form — and it is the *reason* RT-1's 97%/76% matters, since long chains multiply per-step reliability.

## Open questions

- **No N per cell.** 3,000 trials total across 200+ seen and many unseen instructions implies roughly 10–15 per instruction. Aggregate gaps (97 vs 72, 76 vs 52) are large enough to survive; **per-task orderings are not supported**, and the paper doesn't claim them.
- **Everyday Robots no longer exists** — the platform underlying RT-1, [RT-2](rt-2-paper.md), and [RT-H](rt-h-paper.md) was wound down in 2023, which is part of why this line's data is not reproducible outside Google.
- **Discrete action tokens with no chunking.** RT-1 predicts one action at a time; [ACT](../entities/act.md)'s chunking (same year) and the flow-matching heads that followed both post-date it. The 3 Hz figure is therefore a *per-action* rate, unlike modern chunked policies.
- Not evaluated on any standard benchmark — no [LIBERO](../entities/libero.md), no comparison surface outside its own suite.

## Entities mentioned
- [RT-1](../entities/rt-1.md) · [RT-2](../entities/rt-2.md) · [Everyday Robots](../entities/everyday-robots.md) · [SayCan](../entities/saycan.md)
- [Chelsea Finn](../entities/chelsea-finn.md) · [Sergey Levine](../entities/sergey-levine.md) · [Ted Xiao](../entities/ted-xiao.md)
- [Open X-Embodiment](../entities/open-x-embodiment.md) — the corpus this data later joined

## Concepts touched
- [VLA models](../concepts/learning/vla-models.md) — the ancestor of the discrete-action-token family
- [Imitation learning](../concepts/learning/imitation-learning.md) — behavior cloning at 130k demonstrations
- [Control abstraction levels](../concepts/robotics/control-abstraction-levels.md) — the pretrained policy that SayCan commands
- [Scaling laws — VLAs](../concepts/learning/scaling-laws-vla.md) — the first serious data/model/diversity ablation in real robotics
