---
title: OmniVLA — An Omni-Modal Vision-Language-Action Model for Robot Navigation (Hirose, Glossop, Shah, Levine; 2025)
type: source
url: https://arxiv.org/abs/2509.19480
fetch_url: https://arxiv.org/pdf/2509.19480v1
author: Noriaki Hirose, Catherine Glossop, Dhruv Shah, Sergey Levine
published: 2025-09-23
ingested: 2026-09-11
venue: arXiv v1 (9 pp., 7 figures, 6 tables)
local_path: raw/2509.19480v1.pdf
sha256: f6744c6c6b5ef1d23fc0db3345a287d91f0c1269c17b056236f760245a509ee9
format: pdf
tags: [omnivla, navigation, visual-navigation, vla, openvla, language-conditioned, goal-pose, image-goal, modality-dropout, frodobots, bdd-v, mbra, cross-embodiment, unitree-go1, lora, berkeley, rail, hirose, shah, levine]
---

## Summary

The RAIL navigation line's arrival at a **VLA**: [OpenVLA](../entities/openvla.md) (7B; Llama 2 + SigLIP/DINOv2) fine-tuned with LoRA (~5% of parameters) to accept a goal as **language, a 2-D pose, an egocentric goal image, or any combination**, with a **modality-dropout** attention mask so every dataset contributes whatever labels it has. The headline data claim — **~9,500 hours across 10 platforms, "the largest pre-training dataset for an end-to-end navigation policy"** — deserves a footnote the wiki supplies below: 8,680 of those hours are **BDD-V car dashcam video** with actions synthesized by a custom [MBRA](mbra-paper.md) relabeler, and the FrodoBots 700 h are MBRA-relabeled too. Real-world results are strong: it beats every single-modality specialist (language 0.73 vs LeLaN 0.43; 2-D pose 0.95 vs MBRA-pose 0.86; image goals 1.00, tied with MBRA-image), follows **out-of-distribution "how" instructions** while reaching a "where" pose (0.80 on the composed task no baseline can attempt), adapts to a new **satellite-image** goal modality by swapping one encoder (0.19 → 0.62), and transfers to a Vizbot and a [Unitree Go1](../entities/unitree-go1.md). A 50M **OmniVLA-edge** on the ViNT architecture matches it on pose and image goals and trails on language.

## Key claims

### Data (Table I)

| Mixture | Platforms | Hours used | Action labels | Modalities |
|---|---|---:|---|---|
| GNM mixture (7 sets) | 6 robots | 62 | raw | pose, ego image |
| LeLaN mixture (5 sets) | 3 | 128.7 | NoMaD-generated | language*, ego image |
| FrodoBots-2K | Earth Rover Zero | 700 | MBRA | pose, ego image (+ satellite, eval only) |
| **BDD-V** | car (20 m/s) | **8,680** | custom MBRA variant | pose, ego image |

*synthetic. Batch sampling ratio LeLaN : GNM : FrodoBots : BDD-V = **4 : 1 : 1 : 1**, so the dashcam corpus is 91% of hours but 1/7 of samples. Including BDD-V "enables the policy to succeed in roughly half of the failed cases" of a model trained without it.

### Model (§III)

- OpenVLA-7B; goal image through the same SigLIP+DINOv2 visual backbone with a projector, 2-D pose through a tokenizer/projector, language as prompt; unused modalities filled with random values and masked out in attention. Linear action head (OpenVLA-OFT style) emits **N = 8 actions at 3 Hz (2.4 s)**. LoRA ≈ 5% trainable; 8× H100, effective batch 224. Objective: MSE to reference actions, plus LeLaN's object-reaching term on LeLaN samples.
- **OmniVLA-edge:** ViNT + a pose projector + ResNet/CLIP with FiLM for language, early fusion, M = 5 frame history, ~50M params — "a very compelling choice for resource-constrained deployment."
- Inference for the big model runs on a **local RTX 4090** sending velocities to the robot over the internet.

### Results (Table II; language over 40 environments, pose 7 × 3, image 8 routes)

| Method | Language SR | OOD-behavior | Pose SR / progress | Image SR / progress |
|---|---:|---:|---:|---:|
| CoW (OWL-ViT + planner) | 0.30 | 0.05 | — | — |
| LeLaN | 0.43 | 0.15 | — | — |
| CounterfactualVLA | 0.33 | 0.45 | — | — |
| MBRA-pose / MBRA-image | — | — | 0.86 / 0.92 | 1.00 / 1.00 |
| NoMaD | — | — | 0.33 / 0.47 | 0.63 / 0.77 |
| ViNT | — | — | — | 0.50 / 0.68 |
| SmolVLA (omni-modal) | 0.10 | 0.15 | 0.38 / 0.70 | 0.38 / 0.45 |
| MiniVLA (omni-modal) | 0.23 | 0.15 | 0.43 / 0.75 | 0.25 / 0.36 |
| **OmniVLA-edge** (50M) | 0.60 | 0.25 | 0.91 / 0.95 | 1.00 / 1.00 |
| **OmniVLA** (7B) | **0.73** | **0.65** | **0.95 / 0.98** | **1.00 / 1.00** |

- Language success splits 1.00 in simple scenes vs **0.65 with obstacles**; the OOD-behavior column ("move along the wall," "between A and B") is where the 7B LLM prior shows: 0.65 vs 0.25 for the 50M edge model with the same data. NaVILA scored **0.0** — it needs step-by-step prompts, a prompt-style domain gap.
- **Composed goals (Table IV, 10 environments, pose 25–100 m + OOD behavioral prompt):** OmniVLA **0.80** success / 0.60 behavior; MBRA-pose 0.70 (cannot read the prompt); NoMaD 0.40; edge 0.30; MiniVLA 0.30; SmolVLA 0.10.
- **Ablation (Table III, edge model):** single-modality training vs omni-modal — language 0.43 → 0.60, pose 0.86 → 0.91, image 1.00 → 1.00, satellite 0.19 → 0.57.
- **Adaptation:** new satellite modality by swapping one frozen-model encoder 0.19 → 0.62; 1.2 h of data from unseen environments lifts satellite 0.57 → 0.83 and pose 0.81 → 0.86; fine-tuning on the CounterfactualVLA dataset 0.725 → 0.825 SR.
- SmolVLA and MiniVLA "perform quite poorly" — attributed to manipulation-only pretraining and limited capacity.

## Reading it against the wiki

> [!note] 9,500 hours, of which 8,680 are a car
> The "largest navigation pretraining set" is 91% BDD-V dashcam footage at 20 m/s with synthesized actions, trained at a 1/7 sampling weight. The genuinely robot-collected, human-labeled core is GNM's 62 h; the next 830 h are FrodoBots and LeLaN with relabeled or generated actions. This is the [MBRA](mbra-paper.md) thesis taken to its conclusion — **observations from anywhere, actions from a model** — and the ablation says it works (BDD-V halves failures). But quote the hour count with its composition, as the wiki's [success-rate audit](../syntheses/platforms/vla-success-rate-audit.md) discipline would for any headline number.

- **Modality dropout is NoMaD's goal mask generalized** ([NoMaD](nomad-paper.md)), and the same device Octo and π-series manipulation VLAs use for missing inputs; OmniVLA cites the manipulation precedent explicitly.
- **The edge/VLA gap is language, not control.** A 50M ViNT-style model equals the 7B VLA on pose and image goals and loses only on out-of-distribution language — the cleanest evidence in the wiki for *where* a VLM backbone earns its cost in a navigation policy: semantics, not affordances. See the backbone question on [VLA models](../concepts/learning/vla-models.md).
- **Backbone choice matters and is not just size:** MiniVLA (1B) and SmolVLA (500M) with the same omni-modal recipe are far below the 50M edge model — manipulation pretraining did not transfer to navigation.
- The FrodoBots Earth Rover Zero remains the evaluation platform; OmniVLA thanks FrodoBots for hardware — the [network's](../entities/bitrobot.md) evaluation-fleet loop, informally.

## Entities mentioned

- [Noriaki Hirose](../entities/noriaki-hirose.md), [Dhruv Shah](../entities/dhruv-shah.md), [Sergey Levine](../entities/sergey-levine.md); Catherine Glossop.
- [OpenVLA](../entities/openvla.md) — the base; [SmolVLA](../entities/smolvla.md) — a baseline; [FrodoBots](../entities/frodobots.md) — data and platform; [Unitree Go1](../entities/unitree-go1.md), Vizbot.

## Concepts touched

- [Visual navigation policies](../concepts/robotics/visual-navigation-policies.md), [VLA models](../concepts/learning/vla-models.md), [crowdsourced robot training data](../concepts/learning/crowdsourced-robot-training-data.md), [robot policy evaluation](../concepts/robotics/robot-policy-evaluation.md).

## Open questions

- What the BDD-V reannotation model is (Appendix B; not transcribed) and how its actions were validated for a 20 m/s car mapped onto a 1 m/s rover.
- Checkpoints "will be released" — release status not verified.
- Latency of a 7B policy at 3 Hz over the internet is not reported.
