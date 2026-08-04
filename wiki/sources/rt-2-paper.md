---
title: "RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control"
type: source
url: https://arxiv.org/abs/2307.15818
local_path: raw/2307.15818.pdf
author: Brohan, Brown, Carbajal, Chebotar, Chen, Choromanski, Ding, Driess, Dubey, Finn, Florence, Fu, Gonzalez Arenas, Gopalakrishnan, Han, Hausman, Herzog, Hsu, Ichter, Irpan, Joshi, Julian, Kalashnikov, Kuang, Leal, Lee, Lee, Levine, Lu, Michalewski, Mordatch, Pertsch, Rao, Reymann, Ryoo, Salazar, Sanketi, Sermanet, Singh, Singh, Soricut, Tran, Vanhoucke, Vuong, Wahid, Welker, Wohlhart, Wu, Xia, Xiao, Xu, Xu, Yu, Zitkovich
venue: arXiv 2307.15818 (CoRL 2023), 26 pp.; Google DeepMind
published: 2023-08-01
ingested: 2026-08-04
format: pdf
tags: [rt-2, vla, action-tokens, pali-x, palm-e, co-fine-tuning, emergent-capabilities, chain-of-thought, web-knowledge-transfer, google-deepmind]
---

# RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control

**Brohan, …, [Driess](../entities/physical-intelligence.md), [Finn](../entities/chelsea-finn.md), …, [Levine](../entities/sergey-levine.md), …, [Sermanet](../entities/pierre-sermanet.md), …, [Xiao](../entities/ted-xiao.md), …, Zitkovich** (54 authors) — [Google DeepMind](../entities/google-deepmind.md). CoRL 2023.

## Summary

**The paper that named the category.** *"We refer to such category of models as vision-language-action models (VLA)."* Everything the wiki files under [VLA](../concepts/learning/vla-models.md) traces its terminology here.

The recipe is deliberately minimal: take a pretrained vision-language model, **express robot actions as text tokens**, and drop them into the training set exactly like natural language. Then **co-fine-tune** on web vision-language tasks *and* robot trajectories together rather than fine-tuning on robot data alone. Two instantiations: **RT-2-PaLI-X (55B)** and **RT-2-PaLM-E (12B)**. The payoff is not in-distribution skill — that's flat versus [RT-1](rt-1-paper.md) — but **generalization and emergent semantic capability inherited from the web**.

## Key claims

### The action-as-text trick, and its tokenizer dependency

Actions are discretized into 256 bins and mapped to existing text tokens. **The mapping is backbone-specific:** PaLI-X has unique tokens for integers up to 1000, so action bins map directly onto integer tokens; PaLM-E requires overwriting the 256 least-frequently-used tokens. A small detail with a long shadow — it is the direct ancestor of [VLA-0](../entities/vla-0.md)'s "action-as-text" family and of the tokenizer work ([FAST](../entities/fast-action-tokenization.md)) that replaced naive binning.

### Co-fine-tuning is the load-bearing choice

*"Co-fine-tuning leads to more generalizable policies"* than naive fine-tuning on robot data alone, because the model keeps seeing web data and so retains its original vocabulary of concepts rather than collapsing onto the robot distribution. This is the direct precursor of [π0.5](../entities/pi-zero-5.md)'s co-training thesis (97.6% of its pretraining is *not* mobile-manipulation data) and of [Knowledge Insulation](../concepts/learning/knowledge-insulation.md)'s stop-gradient answer to the same corruption problem.

### Results — 6,000 evaluation trials

Generalization (over 280 tasks, split easy/hard):

| Model | Seen | Unseen objects (E/H) | Unseen backgrounds (E/H) | Unseen environments (E/H) | **Unseen avg** |
|---|---:|---:|---:|---:|---:|
| R3M | 45 | 32 / 14 | 13 / 9 | 0 / 2 | 12 |
| VC-1 | 63 | 34 / 10 | 13 / 3 | 0 / 0 | 10 |
| [RT-1](rt-1-paper.md) | 92 | 31 / 43 | 71 / 9 | 26 / 14 | 32 |
| MOO | 75 | 58 / 48 | 38 / 41 | 19 / 3 | 35 |
| **RT-2-PaLI-X-55B** | 91 | 70 / 62 | 96 / 48 | 63 / 35 | **62** |
| **RT-2-PaLM-E-12B** | 93 | 84 / 76 | 75 / 71 | 36 / 33 | **62** |

**Seen-task performance is flat (91–93 vs RT-1's 92). The entire gain is in generalization: 62 vs 32, ~2× over the next two baselines and ~6× over R3M/VC-1.** The two RT-2 variants tie on average, with PaLM-E better on *hard* splits and PaLI-X better on easy ones.

> [!warning] Contradiction — the blog says 3×, the paper says ~2×
> [DeepMind's announcement blog](rt-2-deepmind-blog.md) claims *"3x improvement in generalization versus prior baselines."* The paper's own Figure 4 / Table 4 report **"∼2x improvement over the next two baselines, RT-1 and MOO"** (62 vs 32/35), reserving the 3× figure for the separate **emergent-capability** evaluation (*"more than 3x average success rate over the next best baseline"*). The blog appears to have promoted the emergent-eval number into the generalization headline. **Cite 2× for generalization and 3× for emergent skills.**

**Emergent capabilities** — evaluated in three families, none present in robot training data:
- **Symbol understanding** — *"move coke can near 3," "push coke can on top of heart"*
- **Reasoning** — math (*"move banana near the sum of two plus one"*), logos (*"move cup to google"*), nutrition (*"pick a healthy drink"*), color
- **Human recognition** — *"move the coke can to the person with glasses"*

RT-2-PaLI-X leads on symbols, reasoning, and person recognition; the smaller **PaLM-E has an edge on math reasoning**, which the authors attribute to backbone differences rather than scale.

**Chain-of-thought**, added via a short fine-tune, enables multi-stage semantic inference — picking *a rock* as an improvised hammer, *an energy drink* for someone tired. The first embodied-CoT result in this wiki's lineage, later formalized by [MolmoAct](../entities/molmoact.md)'s depth/trace tokens and [adaptive-depth reasoning](../concepts/learning/adaptive-depth-reasoning.md).

**Language-Table** (open-source sim, PaLI-3B): RT-2 **90** vs LAVA 77, RT-1 74, BC-Zero 72 — a comparison surface outside Google's own suite, on a different robot.

### The inference-cost disclosure that founded off-board serving

> *"It is infeasible to run [these models] on standard desktop machines… we deploy them in a multi-TPU cloud service and query this service over the network."*

- **RT-2-PaLI-X-55B: 1–3 Hz.**
- **5B version: ~5 Hz.**

> [!note] The original network-served policy
> This is the earliest instance in the wiki of the pattern that [SmolVLA](../entities/smolvla.md)'s async client/server, [MolmoAct2](../entities/molmoact2.md)'s FastAPI deployment, and every "local AI server" argument in [where the compute lives](../syntheses/agents/on-device-and-on-robot-agents.md) are still working around. It also sets the baseline that [TurboVLA](turbovla-paper.md) inverts three years later: **55B at 1–3 Hz over a network, versus 0.2 B at 32 Hz in 0.9 GB on a desktop GPU** — with the [control-rate ladder](../syntheses/platforms/control-rate-ladder.md) showing the architectural change bought more than the hardware ever did.

## Open questions

- **Physical skills do not improve.** The authors are explicit that emergent capability is *semantic*: the model's dexterity remains bounded by the robot data. Three years on, this is still the field's shape — [Gemini Robotics 2](rt-2-deepmind-blog.md) lifted gripper dexterity but not finger dexterity.
- **No N per emergent category** — 6,000 trials total across many categories; per-category orderings (PaLI-X vs PaLM-E on math) are not statistically supported and shouldn't be repeated as rankings.
- **Nothing is released** — no weights, no data, no code. The reproduction burden fell to [OpenVLA](../entities/openvla.md) a year later.
- **Everyday Robots was wound down** shortly after publication, making the platform unavailable.

## Entities mentioned
- [RT-2](../entities/rt-2.md) · [RT-1](../entities/rt-1.md) · [PaLI-X](../entities/pali-x.md) · [Everyday Robots](../entities/everyday-robots.md) · [Google DeepMind](../entities/google-deepmind.md)
- [Chelsea Finn](../entities/chelsea-finn.md) · [Sergey Levine](../entities/sergey-levine.md) · [Pierre Sermanet](../entities/pierre-sermanet.md) · [Ted Xiao](../entities/ted-xiao.md)
- Descendants: [OpenVLA](../entities/openvla.md) · [VLA-0](../entities/vla-0.md) · [FAST](../entities/fast-action-tokenization.md) · [RT-H](../entities/rt-h.md)

## Concepts touched
- [VLA models](../concepts/learning/vla-models.md) — the paper that coined the term
- [Chain-of-thought](../concepts/learning/chain-of-thought.md) — first embodied CoT in this lineage
- [Action representation languages](../syntheses/agents/action-representation-languages.md) — action-as-text, the readable-but-not-meaningful rung
- [Control abstraction levels](../concepts/robotics/control-abstraction-levels.md) — level 1 at 1–3 Hz over a network
