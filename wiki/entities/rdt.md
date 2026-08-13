---
title: RDT-1B
type: entity
subtype: model
created: 2026-08-13
updated: 2026-08-13
sources: 4
tags: [rdt, rdt-1b, diffusion, bimanual, foundation-model, unified-action-space, tsinghua, robotwin, robomind, baseline]
---

**RDT-1B** (Robotics Diffusion Transformer) — a **1.2 B-parameter diffusion foundation model for bimanual manipulation** from Tsinghua (Liu, Wu, Li, Tan, Chen, Wang, Xu, Su, Zhu; arXiv [2410.07864](https://arxiv.org/abs/2410.07864), ICLR 2025). At publication, **the largest diffusion-based foundation model for robotic manipulation**.

Filed because RDT is one of the wiki's most-cited *undescribed* models: it appears as a baseline in [RoboTwin 2.0](robotwin.md), [RoboMIND](robomind.md), and [X-VLA](x-vla.md), and its numbers are quoted in three separate comparison tables here without the model ever being explained.

> [!note] Documented secondhand
> Everything below comes from the arXiv abstract plus the benchmark tables in [RoboTwin 2.0](../sources/robotwin2-paper.md), [RoboMIND](../sources/robomind-paper.md), and [X-VLA](../sources/xvla-paper.md). **The primary paper is not ingested.**

## Design

Two contributions, both aimed at problems this wiki tracks elsewhere:

- **Diffusion to represent multi-modality.** Bimanual manipulation has genuinely multi-modal action distributions — two arms can accomplish the same goal by different coordinated strategies. This is the same problem [X-VLA](x-vla.md) hit in cloth folding ("humans fold in a wide variety of methods… different strategies are different behavioral modes") and solved by *constraining collection*; RDT instead builds a model class that can represent the multi-modality.
- **A "Physically Interpretable Unified Action Space"** that unifies action representations across robots **while preserving the physical meaning** of the original actions. This is a third distinct answer to the heterogeneity problem, alongside [soft prompts](../concepts/learning/soft-prompt-cross-embodiment.md) (condition the model) and [RoboMIND](robomind.md)'s standardized collection (normalize the data) — and it is the one that most resembles [X-VLA](x-vla.md)'s own aligned EEF-pose space.

Pretrained on "the largest collection of multi-robot datasets to date," then fine-tuned on a self-created **6K+ episode** multi-task bimanual dataset. Claims zero-shot generalization to unseen objects and scenes, language-instruction following, and few-shot skill acquisition.

## As a baseline, where this wiki actually meets it

| Benchmark | RDT | Context |
|---|---|---|
| [RoboTwin 2.0](robotwin.md) Easy / Hard | **34.5 / 13.7** | vs π0 46.4/16.3, [ACT](act.md) 29.7/1.7, DP 28.0/0.6, DP3 55.2/5.0 |
| RoboTwin domain-randomized pretraining | 18.8 → **24.8** (+31.9% rel.) | randomized data helps; *clean* data made it **worse** (14.6) |
| RoboTwin sim-to-real | policy backbone for the **+24.4 pt** synthetic-data result on a COBOT-Magic dual-arm | |
| [RoboMIND](robomind.md) VLA finetuning | **strongest of three** (vs OpenVLA, CrossFormer), "especially notable for dual-arm" | all at **n=10** |
| [X-VLA](x-vla.md) RoboTwin table | 34.5 / 13.7 | matches the RoboTwin paper exactly |

> [!note] RDT survives domain randomization better than any non-pretrained policy
> Its −20.8 pt Easy→Hard drop is the **smallest** in RoboTwin's table — better than π0's −30.1 and far better than ACT (−28.0 to a floor of 1.7) or DP3 (−50.2). Whatever the 1 M-episode pretraining bought, robustness to appearance shift is part of it. That is the same conclusion [RoboTwin 2.0](../sources/robotwin2-paper.md) draws generally — pretraining buys robustness, not peak — with RDT as its cleanest instance.

## Position

RDT is the **diffusion** answer to bimanual generalist manipulation, contemporaneous with [π0](pi-zero.md)'s flow-matching answer and predating [X-VLA](x-vla.md)'s soft-prompt one. On the wiki's [action-head taxonomy](../concepts/learning/flow-matching.md#action-head-taxonomy-in-vlas) it sits in the **DDPM/diffusion** family with [Diffusion Policy](diffusion-policy.md), scaled to foundation-model size and made bimanual.

## Related

- [RoboTwin 2.0](robotwin.md) · [RoboMIND](robomind.md) · [X-VLA](x-vla.md) — where its numbers come from
- [π0](pi-zero.md) — the flow-matching contemporary · [Diffusion Policy](diffusion-policy.md) — the smaller-scale ancestor
- [Soft-prompt cross-embodiment conditioning](../concepts/learning/soft-prompt-cross-embodiment.md) — the rival answer to heterogeneity
- [VLA models](../concepts/learning/vla-models.md) · [Flow matching](../concepts/learning/flow-matching.md)

## Open questions

- **Primary paper un-ingested.** Everything here is abstract + baseline tables. The unified action space in particular deserves a first-hand read — it is a third distinct solution to the problem this wiki has spent a week on.
- **What exactly is "the largest collection of multi-robot datasets to date"?** Presumably OXE-scale; unverified.
- Is RDT-1B open-weights? Not established from the sources ingested here.

## Mentioned in

- [RoboTwin 2.0 paper](../sources/robotwin2-paper.md) · [RoboMIND paper](../sources/robomind-paper.md) · [X-VLA paper](../sources/xvla-paper.md) · [TurboVLA paper](../sources/turbovla-paper.md)
