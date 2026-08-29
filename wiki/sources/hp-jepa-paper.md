---
title: "HP-JEPA: Hierarchical Partitioning for Multi-Resolution Graph Joint-Embedding Predictive Learning"
type: source
url: https://arxiv.org/abs/2608.00491
local_path: raw/hp-jepa_2608.00491.pdf
sha256: b1a56e94fa050fa6be75d3efca8db8eaf54793574d26c8c312642b542e8ea3fb
author: Ruichen Xu, Jingxiang Qu, Wenhan Gao, Jiaxing Zhang, Linsey Pang, Ravid Shwartz-Ziv, Yann LeCun, Yuefan Deng
published: 2026-08-01
ingested: 2026-08-26
venue: arXiv (cs.LG)
format: paper (15 pp)
tags: [jepa, graph-neural-network, self-supervised-learning, hierarchical, multi-resolution, lecun]
---

# HP-JEPA: Hierarchical Partitioning for Multi-Resolution Graph Joint-Embedding Predictive Learning

> [!note] Filed for completeness — the most peripheral of this batch for this wiki
> Graph self-supervised learning, no dynamics, no actions, no control, no world model in the predictive-of-consequences sense. It is a [JEPA](../concepts/world-models/jepa.md) in the architectural sense only: latent-space prediction of masked targets. Recorded so the LeCun publication record here is complete, and because its **hierarchy-of-resolutions** argument rhymes with a live thread in the wiki.

## Summary

**Graph-JEPA** tokenizes a graph by partitioning it into regions, encoding visible context regions with an online encoder, targets with an EMA target encoder, and predicting target latents from context — JEPA transplanted to graphs. Its limitation: **a single predefined partition resolution**, which biases representations toward one structural granularity. HP-JEPA organizes each graph into an **ordered bank of coarse-to-fine partition resolutions**, runs context-target latent prediction separately at each, and fuses the resolution-specific representations by concatenation or task-specific weighting.

The motivating claim: *fine partitions preserve local motifs but fragment regional organization and long-range dependencies; coarse partitions capture topology but blur discriminative local patterns; and the most informative granularity varies across graphs.*

## Key claims

- Outperforms the fixed-resolution **Graph-JEPA** baseline on **6 of 8 tasks** — seven graph-classification benchmarks and one graph-regression benchmark.
- **Size-stratified analysis**: higher accuracy than Graph-JEPA in most graph-size quartiles on three representative datasets. This is the more interesting evidence, since it tests the actual hypothesis (that a fixed resolution mis-serves graphs of differing size) rather than just the aggregate.

> [!note] 6 of 8, not 8 of 8
> The paper reports the two losses without hiding them, and the abstract's phrasing ("improving upon Graph-JEPA on most evaluated benchmarks") is appropriately hedged. Worth noting because multi-resolution methods are usually presented as strictly dominant.

## The one idea that connects to the rest of the wiki

The wiki tracks **[hierarchical JEPA (H-JEPA)](../concepts/world-models/jepa.md#hierarchical-jepa-h-jepa--long-horizon-planning)** as LeCun's proposed answer to long-horizon planning, and holds [HWM](../entities/hwm.md) as its instantiation — a two-level planner that takes Push-T from 17% → 61%. HP-JEPA is hierarchy along a **different axis**: not temporal abstraction for planning, but **structural resolution for representation**. Same instinct (one granularity is never right), different quantity being coarsened.

Whether that transfers is an open question and this paper does not ask it. But it is a reminder that "hierarchical JEPA" names at least two distinct programs, and the wiki should not conflate them.

## Entities mentioned

- [Yann LeCun](../entities/yann-lecun.md); **Ravid Shwartz-Ziv** (NYU); Yuefan Deng (Stony Brook); Jiaxing Zhang (contributions made independently of TikTok, per the paper's own footnote).
- **Graph-JEPA** — the baseline. No page.

## Concepts touched

- [JEPA](../concepts/world-models/jepa.md) — architecture family; the hierarchy axis.

## Open questions

- **No robotics, control, or dynamics content** — nothing to carry into the wiki's world-model pages beyond the hierarchy observation.
- **No comparison to non-JEPA graph SSL** in what was extracted (contrastive or generative graph SSL are described in related work but the headline comparison is Graph-JEPA only).
- **Cost of the resolution bank is unaddressed** — running context-target prediction at every resolution multiplies pretraining work, and no compute accounting was found.
