---
title: Physical Intelligence
type: entity
subtype: organization
created: 2026-05-09
updated: 2026-08-03
sources: 15
tags: [physical-intelligence, vla, pi-zero, pi-zero-7, pi-star-zero-6, generalist-policy, robotics, flow-matching, recap]
---

**Physical Intelligence** (also written as π) — San Francisco AI robotics company; develops cross-platform generalist robot policies. The wiki now tracks **four primary π-series models** (π0, **π0.5**, π0.7, π*0.6) with π0.6 / π0.6-MEM still referenced only via downstream papers.

## Founding team — the code-as-policy crossing

The founders include **[Karol Hausman](karol-hausman.md)** (CEO) and **[Brian Ichter](brian-ichter.md)**, with **[Chelsea Finn](chelsea-finn.md)** and **[Sergey Levine](sergey-levine.md)** among the founding researchers — i.e. the core of the Google cohort that built **[SayCan](saycan.md)**, **[Inner Monologue](inner-monologue.md)**, and **[Code as Policies](../sources/code-as-policies-paper.md)**. The people who established *LLM-plans-over-skills* then founded the flagship *end-to-end VLA* lab.

This matters for reading the wiki's 2026 architectural argument: when [CaP-X](../sources/cap-x-paper.md) and [ASPIRE](../sources/aspire-paper.md) show code-writing agents degrading gracefully where π0/π0.5 collapse under paraphrase, that is a **within-community comparison between two bets made by overlapping people**, not a rivalry between camps. See [code as policy](../concepts/agents/code-as-policy.md).

## The π series

```
π0  →  π0.5  →  π0.6  →  π0.6-MEM  →  π0.7    (2024 → late 2025)
                                  ↘   π*0.6   (RL variant)
```

| Model | Year | Architecture | Headline contribution | Primary source |
|---|---|---|---|---|
| **[π0](pi-zero.md)** | Oct 2024 | PaliGemma 3 B VLM + 0.3 B flow-matching action expert (3.3 B total); **full bidirectional SA** in action expert | First cross-embodiment flow-matching VLA; 10,000 hr in-house teleop + OXE/DROID/Bridge; beat OpenVLA + Octo on bussing | [paper](../sources/pi-zero-paper.md) ✓ |
| **[π0.5](pi-zero-5.md)** | Apr 2025 | π0 + hierarchical inference (predict subtask, then actions); discrete-FAST pretrain → 300M flow-matching post-train | **Open-world generalization via co-training**: cleans kitchens/bedrooms in **entirely unseen homes**, 10–15 min tasks; 97.6% of pre-training is *not* mobile-manipulation data; at 104 training locations matches a model trained on the test homes | [paper](../sources/pi-zero-5-paper.md) ✓ |
| **[π0.6](pi-zero-6.md)** | — | Larger backbone + more diverse conditioning | (intermediate; documented via [pi-zero-6.md](pi-zero-6.md) anchor) | — |
| **[π0.6-MEM](pi-zero-6.md)** | — | Adds MEM video history / memory encoder | (intermediate; documented via [pi-zero-6.md](pi-zero-6.md) anchor) | — |
| **[π0.7](pi07.md)** | 2025 | **Gemma3 4B + 860M flow-matching action expert** (5 B total); MEM video encoder; **Knowledge Insulation (KI)** training; **stop-gradient** to VLM | **First "emergent capabilities" VLA**: out-of-the-box espresso machine + laundry + box folding + sweet-potato-into-air-fryer compositional generalization via **diversified prompt** (subgoal images from BAGEL 14B world model + episode metadata + control mode) | [paper](../sources/pi07-paper.md) ✓ |
| **[π*0.6](pistar06.md)** | 2025 | π0.6 + advantage-indicator conditioning (CFGRL-style) | **RECAP recipe** — RL from deployment via advantage-conditioned policy extraction; **2× throughput, ½ failure rate** on hardest tasks; 13-hr continuous espresso operation | [paper](../sources/pistar06-paper.md) ✓ |

## Design themes across the π series

- **Flow matching is the canonical action head** — adopted across all π models. The wiki's first ingest of this design choice and the lineage other VLAs ([SmolVLA](smolvla.md), [EgoScale](../sources/egoscale-paper.md)) have since followed.
- **Knowledge Insulation (KI) training** — VLM backbone trained via next-token prediction with FAST tokens; flow-matching action expert with **stop-gradient** so the VLM stays stable. Used in both π0.7 and π*0.6.
- **Sibling complementary directions in 2025**: π0.7 = "more diverse data + diversified prompts," π*0.6 = "iterate on the model with deployment experience." Both run the same Gemma3-class VLM + flow-matching action expert + KI training.
- The action-head choice — **flow matching** — is the canonical contrast point against [Diffusion Policy](diffusion-policy.md)'s DDPM and OpenVLA's autoregressive action tokens.

## π0.5 as the standing 2026 baseline

Since mid-2026, **π0.5 is the model the field's evaluation record is measured against** — and the record is two-sided. Its [paper](../sources/pi-zero-5-paper.md) demonstrates real scene-level generalization (unseen homes); [LIBERO-PRO](../sources/libero-pro-paper.md), [CaP-X](../sources/cap-x-paper.md), and [ASPIRE](../sources/aspire-paper.md) show it is the most position-robust of the tested VLAs **and** that it collapses to ~0.00 under instruction paraphrase; [MolmoAct2](../sources/molmoact2-paper.md) beats it by +3.8 on RoboEval. The one-line reconciliation on the [π0.5 page](pi-zero-5.md): **the co-training recipe bought scene generalization but not instruction generalization.**

## Significance

Physical Intelligence and [NVIDIA GR00T](../entities/nvidia-groot.md) / Gemini Robotics represent the main non-academic demonstration that VLA-style generalist policies can work across real robot platforms. The [Stanford HAI AI Index 2026](../sources/stanford-hai-ai-index-2026.md) cites π0/π0.6 as the leading examples of Physical AI / foundation models for robotics.

## Related
- [π0](pi-zero.md), [π0.7](pi07.md), [π*0.6](pistar06.md) — model entities.
- [VLA models](../concepts/learning/vla-models.md) — π-series sits at the center of this paradigm.
- [SmolVLA](smolvla.md) — Hugging Face's smaller open contemporary; uses π0 as baseline.
- [NVIDIA GR00T](../entities/nvidia-groot.md) — parallel generalist-policy effort.

## Mentioned in
- [π0 Paper](../sources/pi-zero-paper.md) — primary source for π0.
- [π0.7 Paper](../sources/pi07-paper.md) — primary source for π0.7.
- [π*0.6 Paper](../sources/pistar06-paper.md) — primary source for π*0.6 + RECAP.
- [Knowledge Insulation Paper](../sources/knowledge-insulation-paper.md) — the KI training recipe (π0.5-KI) behind π0.7 / π*0.6.
- [FAST Paper](../sources/fast-paper.md) — the DCT action tokenizer + π0-FAST; the discrete-token half of the π-series toolkit.
- [SmolVLA Paper](../sources/smolvla-paper.md) — uses π0 as primary baseline.
- [Stanford HAI — AI Index Report 2026](../sources/stanford-hai-ai-index-2026.md)
- [π0.5 paper](../sources/pi-zero-5-paper.md) — primary source for π0.5; **ingested 2026-08-03**, closing the wiki's most-cited secondhand-anchor gap.
