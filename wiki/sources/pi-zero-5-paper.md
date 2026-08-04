---
title: "π0.5: a Vision-Language-Action Model with Open-World Generalization"
type: source
url: https://arxiv.org/abs/2504.16054
author: "Physical Intelligence (Kevin Black, Noah Brown, Danny Driess, Chelsea Finn, Karol Hausman, Brian Ichter, Sergey Levine, Suraj Nair, Karl Pertsch, Quan Vuong, et al. — 34 authors)"
affiliation: Physical Intelligence
published: 2025-04-22
ingested: 2026-08-03
venue: arXiv preprint (2504.16054, v1)
format: research paper (19 pp)
local_path: raw/2504.16054.pdf
tags: [pi-zero-5, physical-intelligence, vla, co-training, open-world, mobile-manipulation, hierarchical-inference, fast-tokenizer, flow-matching, knowledge-insulation, primary-source]
---

## Summary

**The π0.5 primary — closing the wiki's longest-standing secondhand-anchor gap.** π0.5 had become the most-cited un-ingested model in the wiki: it is the baseline in [LIBERO-PRO](libero-pro-paper.md), [CaP-X](cap-x-paper.md), [ASPIRE](aspire-paper.md), and [MolmoAct2](molmoact2-paper.md), and the substrate of [π0.5-KI](knowledge-insulation-paper.md) — all known only through other papers' tables until now.

The paper's own thesis: **open-world generalization comes from co-training on heterogeneous knowledge sources, not from scaling one data type.** Built on [π0](../entities/pi-zero.md), π0.5 trains on mobile-manipulator data (~400 hours across ~100 homes), non-mobile robot data in diverse environments (ME), laboratory cross-embodiment data (CE), **high-level semantic subtask prediction** (HL), multimodal **web data** (WD: captioning, VQA, object localization), and **verbal instructions** from human supervisors (VI). The striking statistic: **97.6% of first-phase training examples do not come from mobile manipulators doing household tasks.**

**Headline demonstration:** the first end-to-end learned system to perform **long-horizon (10–15 minute) cleaning of kitchens and bedrooms in entirely new homes** not seen in training — from prompts as broad as "put the dishes in the sink."

## Key claims

### Architecture — hierarchical inference in one model
At each inference step the model **first predicts a semantic subtask** ("pick up the cutting board"), **then predicts the low-level action chunk conditioned on it**. One model, two levels. The stated rationale: the low level benefits from cross-embodiment action data, while the high level benefits from web semantics, subtask annotations, and verbal instructions.

### Training — the discrete-pretrain → flow-matching-post-train recipe
1. **Pre-training:** standard autoregressive transformer over text, object locations, and **[FAST](../entities/fast-action-tokenization.md)-encoded discrete action tokens**, on the full heterogeneous mixture.
2. **Post-training:** attach a **300M flow-matching action expert** for continuous real-time control, specialize on mobile manipulation + verbal instructions.

> [!note] This recipe became the field's template
> Discrete-token pretraining for knowledge, continuous flow post-training for control is exactly the hybrid that [Knowledge Insulation](knowledge-insulation-paper.md) refines (π0.5-KI) and that [MolmoAct2](molmoact2-paper.md) adopts wholesale in 2026. The wiki's [per-layer KV conditioning](../concepts/learning/per-layer-kv-conditioning.md) and [knowledge-insulation](../concepts/learning/knowledge-insulation.md) threads both descend from this design.

### The scaling result — the generalization gap closes at ~100 homes
Performance on four mock-home tasks (dishes in sink, items in drawer, laundry basket, make bed) **improves with the number of training locations**, and at **104 locations** the model **matches a control trained directly on data from the test homes** (Fig. 8). That is the paper's strongest claim quantified: environment-level generalization equal to having trained in the test environment, without having done so.

### Ablations — what each data source buys (10 trials/policy/task, mock homes)
- Removing **ME or CE** (either cross-embodiment source) significantly degrades performance; removing both is worse (Fig. 10).
- Removing **web data** doesn't move mock-home task success significantly — but **significantly harms out-of-distribution object language-following** (Fig. 11): web data is where open-vocabulary semantics comes from.
- **Verbal instructions** (VI) matter for high-level inference quality (§V-E).

### Against other VLAs
π0.5 **significantly outperforms both [π0](../entities/pi-zero.md) and π0-FAST+Flow** (an enhanced π0 given the same hybrid training and the same robot data, but no HL/WD) in mock-home evaluations (Fig. 12) — isolating the co-training recipe, not the architecture, as the source of the gain.

### Stated limitations
Candid and specific: persistent trouble with unfamiliar drawer handles and physically hard cabinets; partial-observability failures (arm occluding the spill it should wipe); **the high-level inference is "easily distracted"** (opening and closing a drawer repeatedly); prompts must be simple; context is modest.

## Entities mentioned
- [Physical Intelligence](../entities/physical-intelligence.md) · [π0](../entities/pi-zero.md) · [π0.5](../entities/pi-zero-5.md) · [FAST](../entities/fast-action-tokenization.md)
- [Chelsea Finn](../entities/chelsea-finn.md) · [Sergey Levine](../entities/sergey-levine.md) · [Karol Hausman](../entities/karol-hausman.md) · [Brian Ichter](../entities/brian-ichter.md) · [Karl Pertsch](../entities/karl-pertsch.md)

## Concepts touched
- [VLA models](../concepts/learning/vla-models.md) · [Knowledge insulation](../concepts/learning/knowledge-insulation.md) · [Flow matching](../concepts/learning/flow-matching.md)
- [Imitation learning](../concepts/learning/imitation-learning.md) · [Sim-to-real transfer](../concepts/learning/sim-to-real-transfer.md) (the data-diversity route)
- [Control abstraction levels](../concepts/robotics/control-abstraction-levels.md) — hierarchical inference internalizes the System 2/System 1 split into one model

## How the 2026 record reads against this paper

> [!note] The 2026 critiques target a different axis than the paper's claim
> π0.5's demonstrated generalization is **environment- and object-level**: new homes, new object instances, OOD categories via web data. The [LIBERO-PRO](libero-pro-paper.md) collapse (π0.5 → ~0.00 under instruction paraphrase) and the [CaP-X](cap-x-paper.md)/[ASPIRE](aspire-paper.md) comparisons probe **instruction-level** robustness — paraphrase and perturbation on a benchmark-finetuned variant. Both records are real: π0.5 genuinely cleans unseen kitchens, and its language interface is genuinely brittle to rephrasing. The paper's own limitation ("relatively simple prompts," complexity "determined by the training data") anticipates the second finding.
>
> The tension worth keeping: **a model whose headline is open-world generalization fails the open-vocabulary half of it** when the vocabulary shifts at test time. The co-training recipe bought scene generalization; it did not buy instruction generalization.

## Open questions
- **n=10 per policy/task** in the ablations and mock-home comparisons — per the [audit](../syntheses/platforms/vla-success-rate-audit.md), only large gaps separate at that n; per-task orderings do not. The headline figures are figure-read, not tabulated.
- The **~400 hr / ~100 homes** mobile-manipulation corpus is proprietary; nothing here is reproducible externally.
- No latency/control-rate numbers for the hierarchical inference loop — relevant to the [control-rate ladder](../syntheses/platforms/control-rate-ladder.md) since subtask inference adds a serial step.
- Whether π0.6 / π0.6-MEM primaries exist remains open — the [π0.6 stub](../entities/pi-zero-6.md) still anchors those.

## Related sources
- [π0 paper](pi-zero-paper.md) — the base model.
- [Knowledge Insulation paper](knowledge-insulation-paper.md) — refines this paper's hybrid recipe into π0.5-KI.
- [LIBERO-PRO](libero-pro-paper.md) · [CaP-X](cap-x-paper.md) · [ASPIRE](aspire-paper.md) · [MolmoAct2](molmoact2-paper.md) — the 2026 record in which π0.5 is the standing baseline.
- [π0.7 paper](pi07-paper.md) · [π*0.6 paper](pistar06-paper.md) — the successors.
