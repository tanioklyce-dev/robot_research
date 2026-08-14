---
title: π0 (pi-zero)
type: entity
subtype: model
created: 2026-05-25
updated: 2026-08-13
sources: 35
tags: [pi-zero, pi0, vla, flow-matching, physical-intelligence, paligemma, action-expert, generalist-policy, cross-embodiment, lerobot, hugging-face]
---

**π0** ("pi-zero") — flagship VLA from [Physical Intelligence](physical-intelligence.md), introduced by [Black et al. (October 2024)](../sources/pi-zero-paper.md). **Architecture: PaliGemma 3 B VLM + flow-matching action expert** = 3.3 B total params. Trained on **~10,000 hours of in-house dexterous teleop** across 7 robot configurations + 68 tasks, plus OXE + DROID + Bridge. Demonstrates **single-arm + dual-arm + mobile-manipulator** cross-embodiment without per-platform retraining. Available as a [LeRobot](lerobot.md) checkpoint at [`lerobot/pi0_base`](https://huggingface.co/lerobot/pi0_base).

## Architecture

- **Base VLM**: [PaliGemma](https://arxiv.org/abs/2407.07726) 3 B — chosen for size/performance tradeoff suitable for real-time control. The framework is VLM-agnostic.
- **Action expert**: transformer module added to the VLM; emits flow-based outputs. ~0.3 B params on top of PaliGemma's 3 B.
- **Attention**: action expert uses a **full bidirectional attention mask** — all action tokens attend to each other. (Contrast with [SmolVLA](smolvla.md)'s interleaved cross-attention + causal self-attention.)
- **Inputs**: 3 RGB images + proprioceptive state + natural-language instruction.
- **Outputs**: action chunks; flow-matching head with `τ ~ Beta(...)`.

## Training data

- **~10,000 hours of dexterous manipulation** (in-house Physical Intelligence teleop).
- **7 robot configurations** (single-arm, dual-arm, mobile manipulator) × **68 tasks**.
- Augmented with **[OXE](droid.md) (Open X-Embodiment)**, **[DROID](droid.md)**, **Bridge**, etc.

## Demonstrated tasks

Laundry folding (long-horizon, dual-arm, deformable), table bussing (combinatorial — dishes + utensils + trash), dishes in microwave, eggs into carton, box assembly, grocery bagging.

## Headline results ([paper](../sources/pi-zero-paper.md), §VI)

- **Beats [OpenVLA](../concepts/learning/vla-models.md) and Octo** on bussing-task family, including cross-embodiment-fine-tuned OpenVLA baseline on UR5e.
- **Single checkpoint, multiple embodiments** — language commands from human or VLM steer the same model across single/dual-arm and mobile platforms.
- **VLM-as-planner + π0-as-controller** stack works for multi-stage tasks.

## Why it matters in this wiki

- **The canonical flow-matching VLA**. π0 popularized the **flow-matching action expert** pattern that downstream VLAs (notably [SmolVLA](smolvla.md), and now also EgoScale's DiT action expert) have adopted. Action-head taxonomy is now: **autoregressive tokens (OpenVLA)** vs **DDPM (Diffusion Policy)** vs **flow matching (π0, SmolVLA, EgoScale)** — see [VLA models concept page](../concepts/learning/vla-models.md).
- **Strongest 2024 cross-embodiment demonstration**. The "one checkpoint, 7 robot configs" claim was the first credible proof that a single generalist robot policy could span hardware tiers.
- **The default π-series reference.** Direct successors **[π0.7](pi07.md)** (5 B params; Gemma3 4B + MEM + diversified-prompt conditioning + KI training; emergent compositional generalization) and **[π*0.6](pistar06.md)** (RL-from-deployment recipe via advantage conditioning) are now filed. Intermediate π0.5 / π0.6 / π0.6-MEM remain not-separately-ingested. See [Physical Intelligence entity](physical-intelligence.md) for the full lineage table.
- **Downstream artifact in LeRobot ecosystem**. Available at `lerobot/pi0_base`; used in the [LeRobot "Robot Learning: A Tutorial"](../sources/lerobot-robot-learning-tutorial.md) as the canonical VLA code example.
- **The baseline [SmolVLA](smolvla.md) explicitly beats** on real-world SO-100 multi-task (SmolVLA 0.45 B = 78.3% vs π0 3.5 B = 61.7% avg). Smaller model + community data + interleaved cross-attention wins the comparison.

## Comparison with SmolVLA

| | π0 | [SmolVLA](smolvla.md) |
|---|---|---|
| Total params | **3.3 B** | 0.24 / 0.45 / 2.25 B |
| Base VLM | PaliGemma 3 B | SmolVLM-2 (~0.4 B) |
| Action expert attention | Full bidirectional self-attention | **Interleaved cross-attention + causal self-attention** |
| Training data | **10,000 hr** in-house teleop + OXE + DROID + Bridge | 22.9 K episodes from **481 community HF datasets** |
| Open source | Weights only (`lerobot/pi0_base`) | Full code + training recipe + data lists |
| Real-world SO-100 avg | 61.7 (multi-task) | **78.3 (multi-task)** |
| Async inference stack | not native | **yes — server/client with similarity-filtering** |

The two are the canonical contrast points in the [LeRobot tutorial](../sources/lerobot-robot-learning-tutorial.md) and the active reference points for VLA design as of mid-2026.

## As a baseline: what X-VLA reports against π0

[X-VLA](x-vla.md) ([paper](../sources/xvla-paper.md)) uses π0 as its principal comparison and is worth reading as an audit of where π0's 3 B parameters actually earn their keep:

| | π0 (3 B) | X-VLA (0.9 B) |
|---|---:|---:|
| LIBERO avg | 94.1 | **98.1** |
| Simpler-WidowX | 27.8 (55.7 finetuned on it) | **95.8** |
| [RoboTwin-2.0](robotwin.md) easy / hard | 46.4 / 16.4 | **70.0 / 39.0** |
| LIBERO under LoRA | 94.2 @ 3 B tuned | 93.0 @ **9 M** tuned |
| Cloth folding throughput | X-VLA "comparable to closed-source π0-folding" | 33 folds/hr from 1,200 episodes |

Two caveats keep this from being a clean π0 indictment. The **cloth-folding comparison is against the *public* `pi0_base` finetuned on Soft-Fold** — 150 K steps on 4×A100 — not against Physical Intelligence's internal folding model, which X-VLA only claims to be "comparable" to. And π0's own strength has always been argued on **real-world open-world breadth** (10,000 hr of in-house teleop across 7 robot configurations), which no benchmark in X-VLA's suite measures.

Still, the direction is consistent with [SmolVLA](smolvla.md)'s result from the other side: at these task scales, **π0's parameter count is not what is buying its performance**, and both a 0.45 B community-data model and a 0.9 B conditioning-focused model have now passed it on their chosen ground.

## Related

- [Physical Intelligence](physical-intelligence.md) — vendor / origin.
- [π0.7](pi07.md) — direct successor (2025); 5 B params; Gemma3 4B + diversified-prompt conditioning + KI training; first VLA with emergent compositional generalization.
- [π*0.6](pistar06.md) — RL-finetuned sibling (2025); RECAP recipe via advantage conditioning; 2× throughput / ½ failure rate on hardest tasks.
- [SmolVLA](smolvla.md) — smaller open-source contemporary; uses π0 as baseline.
- [VLA models](../concepts/learning/vla-models.md) — broader concept.
- [Diffusion Policy](diffusion-policy.md) — sibling continuous-action approach via DDPM (vs π0's flow matching).
- [LeRobot](lerobot.md) — distribution channel (`lerobot/pi0_base`); tutorial code example.
- [DROID](droid.md) — training-data component.

## Code

- Checkpoint: `lerobot/pi0_base` on Hugging Face.
- Blog: https://physicalintelligence.company/blog/pi0
- Tutorial code example: see the [LeRobot "Robot Learning: A Tutorial"](../sources/lerobot-robot-learning-tutorial.md) §"Code Example: Using π0".

## Mentioned in

- [π0 Paper](../sources/pi-zero-paper.md) — primary source (full HTML ingest).
- [Physical Intelligence entity](physical-intelligence.md)
- [SmolVLA Paper](../sources/smolvla-paper.md) — uses π0 as primary baseline; beaten on real-world SO-100 multi-task.
- [Robot Learning: A Tutorial (LeRobot)](../sources/lerobot-robot-learning-tutorial.md) — covered as canonical VLA example.
- [Stanford HAI — AI Index Report 2026](../sources/stanford-hai-ai-index-2026.md) — cited as leading Physical AI VLA.
- [LeRobot ICLR 2026 paper](../sources/lerobot-iclr-2026-paper.md) — supported reference policy at **3.5 B params** (largest in LeRobot's lineup); **13.32 GB peak mem on A100**; **fails inference within 5 s on both CPU and MPS** — confirms π0 needs GPU for onboard deployment. Distributed as `lerobot/pi0` checkpoint.
- [FAST paper](../sources/fast-paper.md) — π0 is the main backbone; **π0-FAST** (autoregressive π0 + FAST tokens) matches the π0-diffusion VLA while training up to 5× faster.
- [CaP-X paper](../sources/cap-x-paper.md) — π0 and π0.5 as LIBERO-PRO baselines against a training-free coding agent; π0 scores 0.00 everywhere, π0.5 retains position robustness (0.17–0.38) but collapses under instruction paraphrase (0.00–0.01).
- [ASPIRE paper](../sources/aspire-paper.md) — same comparison; π0.5 "largely collapses under task paraphrases."
