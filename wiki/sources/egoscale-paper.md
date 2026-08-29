---
title: EgoScale — Scaling Dexterous Manipulation with Diverse Egocentric Human Data
type: source
url: https://arxiv.org/abs/2602.16710
arxiv_id: 2602.16710v1
local_path: raw/2602.16710v1.pdf
sha256: 39c691baf374a154e26ffc0098b97037875909495013d4017d97761716ff2735
project_page: https://research.nvidia.com/labs/gear/egoscale/
doi: https://doi.org/10.48550/arXiv.2602.16710
license: CC BY 4.0
author: Ruijie Zheng, Dantong Niu, Yuqi Xie, Jing Wang, Mengda Xu, Yunfan Jiang, Fernando Castañeda, Fengyuan Hu, You Liang Tan, Letian Fu, Trevor Darrell, Furong Huang, Yuke Zhu, Danfei Xu, Linxi (Jim) Fan
affiliations: NVIDIA; UC Berkeley; University of Maryland
published: 2026-02-18 (arXiv v1; cover date 2026-02-19)
ingested: 2026-05-15
tags: [egoscale, nvidia-gear, vla, dexterous-manipulation, scaling-laws, human-data, egocentric, gr00t, flow-matching, dit, sharpa, galaxea, unitree-g1]
---

> [!note] Project leads
> Yuke Zhu, Danfei Xu, and Linxi (Jim) Fan are flagged as project leads (†) on the author list. Trevor Darrell (UC Berkeley) and Furong Huang (UMD) are the external academic co-authors; everyone else is at NVIDIA.

## Summary

**EgoScale** is the first explicit *scaling-law* analysis for Vision–Language–Action (VLA) pretraining on egocentric human video. The paper pretrains a [flow-matching](../concepts/learning/flow-matching.md) VLA on **20,854 hours of egocentric human video** — the same corpus [GR00T N1.7](../entities/nvidia-groot.md) is built on — and uncovers a clean log-linear relationship between validation loss and data scale:

```
L = 0.024 − 0.003 · ln(D)         R² = 0.9983
```

where `D` = hours of human pretraining data (measured in the 1k–20k hr range). This validation loss **strongly tracks downstream real-robot performance**, establishing large-scale human video as a *predictable* supervision source for VLAs. Beyond the scaling law, the paper introduces a two-stage transfer recipe (large-scale human pretrain → small-scale aligned human-robot mid-training → task-specific post-training) that yields **+54% average success** on five dexterous tasks over a no-pretraining baseline using a 22-DoF dexterous hand, **88% one-shot shirt folding** from a single robot demonstration, and **+30% absolute improvement** on the Unitree G1 with a tri-finger hand — evidence that the human-pretrained motor prior is **embodiment-agnostic**.

This is the public scaling-law paper for the [NVIDIA GR00T](../entities/nvidia-groot.md) pretraining pipeline, written by the [NVIDIA GEAR](../entities/nvidia-gear.md) team. The "EgoScale pretraining" referred to in earlier GR00T documentation now has its primary source.

## Key claims

### Scaling phenomenon (the headline)
- Pretrained on **20,854 hours of egocentric human manipulation video** — >20× larger than prior human-to-robot transfer datasets — across 9,869 scenes, 6,015 tasks, 43,237 objects, 30 FPS RGB. Augmented by 829 hr of **[EgoDex](../entities/egodex.md)** (Apple Vision Pro–captured) for higher-precision wrist + hand kinematics.
- **Log-linear scaling law**: `L = 0.024 − 0.003 · ln(D)` with **R² = 0.9983** in the 1k–20k hr range (Figure 5, center). No saturation observed.
- **Validation loss tracks real-robot performance**: across the five data-scale checkpoints (1k / 2k / 4k / 10k / 20k hr), average task completion rises monotonically 0.30 → 0.45 → 0.48 → 0.57 → 0.71 (§3.3).
- **Small datasets overfit, large datasets don't**: 1k–2k hr runs plateau or degrade after ~20K steps; 10k–20k hr runs improve stably through 100K steps (§3.3, Figure 5 left).

### Two-stage transfer recipe
- **Stage I — large-scale human pretrain** (§2.4): 20K hr human data, 100K steps, **256 GB200 GPUs**, global batch size 8,192, lr 5×10⁻⁵, all params unfrozen.
- **Stage II — aligned human-robot mid-training**: small dataset (50 hr human + 4 hr robot, 344 tabletop tasks) where humans and the robot perform similar tasks in matched scenes with matched cameras. 50K steps, batch 2,048, lr 3×10⁻⁵; VL backbone frozen, only vision encoder + DiT action expert updated.
- **Stage III — task-specific post-training**: 10K steps, batch 512, lr 3×10⁻⁵. Vision encoder frozen if mid-training was used.

### Action representation (the ablation that justifies "joint-space" over "wrist-only" or "fingertip")
- Action space: **relative wrist motion** (SE(3) between consecutive timesteps) + **retargeted 22-DoF dexterous hand joint actions** (target hand: [Sharpa Wave](../entities/sharpa-wave.md)).
- Ablation (§3.6, Figure 8) on Card / Tongs / Bottle tasks compares three pretraining action representations:
  - **Wrist-only** (no finger supervision): task-completion ≈ 0.56 / 0.24 / 0.26.
  - **Fingertip-SE(3)**: ≈ 0.17 (Card) / 0.76 / 0.55.
  - **Full retargeted joint angles** (default): ≈ 0.74 / 0.79 / 0.61.
- Joint-space hand actions win across the board. Wrist-only is too coarse for contact-rich tasks; fingertip-SE(3) frequently produces implausible joint configurations after IK mapping.

### Model architecture
- **Flow-based VLA architecture similar to GR00T N1** (§2.3): pretrained VLM backbone (vision-language encoder, text encoder) + **DiT action expert** with flow-matching objective.
- Action chunk prediction conditioned on `o_t = (image, language instruction)` + (for robot data only) proprioceptive state `q_t`. For human data, `q_t` is replaced by a learnable placeholder token.
- **Embodiment-conditioned MLP adapters** at input (proprioceptive state) and output (hand actions) — only the adapters differ across embodiments; vision-language backbone, DiT action expert, and wrist-motion prediction are fully shared.

### Main results (§3.2, Figure 4)
Five dexterous manipulation tasks on Galaxea R1Pro humanoid with 22-DoF Sharpa Wave hands, comparing 4 checkpoints: No-Pretrain / Midtrain-Only / Human-Pretrain / **Human-Pretrain + Midtrain**.

| Task | No-Pretrain | Midtrain Only | Human Pretrain | **Pretrain + Midtrain** |
|---|---:|---:|---:|---:|
| Shirt Rolling (completion / success) | 0.40 / 0.05 | 0.55 / 0.20 | 0.83 / 0.40 | **0.90 / 0.50** |
| Card Sorting | 0.14 / 0.00 | 0.54 / 0.50 | 0.74 / 0.70 | **0.87 / 0.65** |
| Tongs Fruit Transfer | 0.35 / 0.05 | 0.85 / 0.60 | 0.79 / 0.45 | **0.87 / 0.65** |
| Bottle Cap Unscrew | 0.18 / 0.00 | 0.51 / 0.10 | 0.63 / 0.21 | **0.82 / 0.59** |
| Syringe Liquid Transfer | 0.16 / 0.00 | 0.23 / 0.00 | 0.53 / 0.17 | **0.70 / 0.42** |
| **Average** | **0.24 / 0.02** | **0.53 / 0.28** | **0.71 / 0.38** | **0.83 / 0.56** |

Headline: +54% absolute success-rate improvement over no-pretraining (0.02 → 0.56).

### Emergent one-shot transfer (§3.4)
With *only one robot demonstration* + 100 aligned human demonstrations, the Pretrain+Midtrain model achieves:
- **0.88 success** on Fold Shirt (not in mid-training data).
- **0.55 success** on Unscrew Water Bottles (three novel bottle geometries).

Models without either large-scale human pretraining *or* aligned mid-training fail in this one-shot setting — the two stages are complementary.

### Cross-embodiment transfer to Unitree G1 (§3.5)
On the Unitree G1 with a tri-finger hand (fewer DoF than the Sharpa Wave 22-DoF training target):
- Two tasks: Pen-in-Bin and Dish Handover in Rack.
- Pretraining + G1-augmented mid-training yields **+30% absolute success** improvement over the G1-only baseline.
- The lower-body balance and locomotion are handled by a separately trained Homie policy; EgoScale only emits upper-body commands.

This is evidence that human-pretrained representations generalize across **kinematically different hands** (22-DoF → tri-finger), not just across different VLA fine-tuning targets — i.e. the human data is a *reusable motor prior*, not a corpus-specific bias.

## Position in the wiki

### Closes the GR00T-pretraining-source question
The wiki had already noted that [NVIDIA GR00T](../entities/nvidia-groot.md) N1.7 EA is "pretrained on 20,854 hours of egocentric human video" without a primary source. **EgoScale is that primary source.** The exact 20,854-hour figure matches; the EgoScale paper is the public scaling-law analysis for the corpus GR00T is built on.

### Establishes a "VLA scaling laws" thread
The wiki's [VLA models](../concepts/learning/vla-models.md) concept page tracks ~10 VLAs but has nothing on training-data-vs-performance scaling laws. EgoScale is the first to publish a clean one. Seeded as the new [scaling laws — VLAs and human data](../concepts/learning/scaling-laws-vla.md) concept page.

### Architectural placement
EgoScale's **flow-matching action head** sits in the action-head taxonomy already in [VLA models](../concepts/learning/vla-models.md):
- π0 — flow-matching action head ✓
- EgoScale — flow-matching action head (DiT + flow matching, similar to GR00T N1) ✓
- Diffusion Policy — DDPM
- Helix S1 — continuous regression
- OpenVLA — autoregressive action tokens

### Adjacent to but distinct from sim-to-real
EgoScale takes **the opposite path** from the [sim-to-real](../concepts/learning/sim-to-real-transfer.md) literature: instead of generating synthetic data in simulation and bridging to real robots, it pretrains directly on *real* human video. The 20,854-hour figure shifts the comparison from "how much sim do you need?" to "how much human video do you need?" Cosmos / World-Foundation-Model line and EgoScale are two parallel responses to the same VLA-data-bottleneck.

## Entities mentioned

**Already in wiki:**
- [NVIDIA GEAR](../entities/nvidia-gear.md) — paper origin lab.
- [Jim Fan (Linxi Fan)](../entities/jim-fan.md) — project lead.
- [Yuke Zhu](../entities/yuke-zhu.md) — project lead.
- [NVIDIA](../entities/nvidia.md) — parent organization.
- [NVIDIA GR00T](../entities/nvidia-groot.md) — the VLA family this paper's pretraining feeds.

**New entity stubs created with this ingest:**
- [Sharpa Wave hand](../entities/sharpa-wave.md) — 22-DoF dexterous hand used as the primary post-training target.
- [EgoDex dataset](../entities/egodex.md) — 829 hr Apple Vision Pro–captured egocentric dataset used as the high-precision supplement to in-the-wild data.

**Mentioned in the paper but not (yet) entitied:**
- Galaxea R1Pro — humanoid robot platform for all primary experiments. Dual 7-DoF arms, base+torso fixed.
- Unitree G1 — humanoid platform for cross-embodiment experiments (tri-finger hand).
- Homie — separately trained lower-body locomotion policy paired with EgoScale's upper-body commands for the G1 dish-handover task.
- Vive trackers / Manus gloves — mocap hardware for the aligned mid-training collection.
- Trevor Darrell (Berkeley), Furong Huang (UMD), Danfei Xu (GA Tech / NVIDIA) — co-authors.

## Concepts touched
- [VLA models](../concepts/learning/vla-models.md) — EgoScale is the flow-matching-VLA scaling-law paper.
- [Scaling laws — VLAs and human data](../concepts/learning/scaling-laws-vla.md) — new hub seeded by this paper.
- [Imitation learning](../concepts/learning/imitation-learning.md) — large-scale human video imitation as the pretraining objective.
- [Sim-to-real transfer](../concepts/learning/sim-to-real-transfer.md) — adjacent paradigm; EgoScale is the *real-data-pretrain* alternative.

## Open questions

- **Does the scaling law continue beyond 20k hr?** The paper explicitly does not extrapolate but notes "substantial headroom for further gains as both human data scale and model capacity continue to increase." A follow-up at 100k hr or with a larger model would test whether the log-linear continues or saturates.
- **What's the model size?** The paper compares to "GR00T N1 [19]" and uses a DiT action expert but does not state EgoScale's total parameter count. Probably similar to GR00T N1.6/N1.7 (3B params) but not confirmed in the body.
- **What is the in-the-wild egocentric dataset?** ~20k hr "in-the-wild" + 829 hr EgoDex. The in-the-wild portion is described as "egocentric activity datasets totaling 20,854 hours across 9,869 scenes, 6,015 tasks, 43,237 objects" but the constituent dataset names aren't given in the main body. Likely Ego4D + EPIC-KITCHENS + others — a follow-up read of the appendix would confirm.
- **Mid-training dataset reuse**: the 50-hour aligned human-robot dataset is presented as a small mid-training piece. Will NVIDIA release it? If so, it's a critical reproducible artifact.
- **Inference compute**: not reported. A 3B-param flow-matching VLA running at humanoid-control rates is a nontrivial deployment question.
- **License of the human data**: EgoDex is Apple-published (license TBD); the in-the-wild ~20k hr is unspecified. Reusability for downstream open-source work depends on this.
- **Scaling law constants vs. NLP**: the LLM scaling-law literature reports specific power-law exponents (Hoffmann et al. 2022 / Chinchilla). EgoScale reports a log-linear loss-vs-data law — a different functional form. Would be worth a comparative synthesis.

## Why this is a significant ingest

1. **Closes a primary-source gap.** GR00T pretraining was the largest unsourced number in the wiki ("20,854 hours of egocentric human video" cited without citation). This is that citation.
2. **First VLA scaling-law paper.** The wiki tracks ~13 VLAs but has no scaling-law treatment. EgoScale is the canonical reference for "how much human data do you need" — the question every VLA team has but no one had published a clean answer to.
3. **Public benchmark for the "human video instead of sim" thesis.** [NVIDIA Cosmos](../entities/nvidia-cosmos.md) and the World Foundation Model line bet on synthetic data; EgoScale shows the real-data path also scales predictably. Same parent company, two parallel responses to the VLA data bottleneck.
4. **Embodiment-agnostic motor prior evidence.** The G1 tri-finger result (+30% with no G1-specific pretraining changes) is one of the cleanest demonstrations to date that a VLA's pretraining can generalize across kinematically different end-effectors.
