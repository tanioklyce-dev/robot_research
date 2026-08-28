---
title: The LIBERO tie cluster — CogVLA, VLA-Adapter, MemoryVLA, FLOWER, BAKU
type: entity
subtype: model
created: 2026-08-13
updated: 2026-08-13
sources: 2
tags: [libero, benchmark, cogvla, vla-adapter, memoryvla, flower, baku, statistical-tie, baseline]
---

A holding page for five models this wiki **quotes numbers from without describing** — four of which sit inside the [LIBERO](libero.md) statistical tie the wiki reasons about, and one which appears as a dataset baseline. Filed so the tables that cite them are interpretable; **none has a primary source ingested.**

> [!warning] Everything here is secondhand
> Numbers come from the baseline tables of [X-VLA](../sources/xvla-paper.md), [TurboVLA](../sources/turbovla-paper.md), [MolmoAct2](../sources/molmoact2-paper.md), and [RoboMIND](../sources/robomind-paper.md). No architecture claim below is verified against a primary paper.

## Inside the LIBERO tie

Per the [success-rate audit](../syntheses/platforms/vla-success-rate-audit.md), separating two policies at ~97% needs **>1.8 pp** (n=500/suite) or **>1.0 pp** (n=2,000 four-suite average). The cluster now holds **ten models within 1.2 pp** — so membership is meaningful and *ordering inside it is not*.

| Model | LIBERO avg | What is known |
|---|---:|---|
| **CogVLA** | 97.4 | Named in the tie; nothing else established here. |
| **VLA-Adapter** | 97.3 | Name implies a PEFT/adapter approach to VLA fine-tuning — **inferred, not verified**. |
| **MemoryVLA** | 96.7 (LIBERO) | The interesting one: **held the prior best on [Simpler](simplerenv.md)-WidowX at 71.9 with 7 B params** until [X-VLA](x-vla.md) reached 95.8 at 0.9 B. Name implies explicit memory over history. |
| **FLOWER** | 95.7 | 1 B; held the **CALVIN ABC→D** best at **4.53**, the one benchmark X-VLA *lost* (4.43). |

## Not a LIBERO model

| Model | Where it appears | What is known |
|---|---|---|
| **BAKU** | [RoboMIND](robomind.md) single-task IL baseline | **Underperformed broadly** on real hardware; the authors attribute it to hyperparameters *"primarily optimized for simulation environments rather than real-world robotic platforms."* A documented sim-to-real tuning failure, at n=10. |

> [!note] Why a holding page rather than five stubs
> Each of these is currently one number and one inference. Five near-empty pages would add link targets without adding knowledge; one page makes the shared fact explicit — **the wiki cites a tie cluster it cannot characterize** — and gives each model somewhere to grow. Split them out when any gets a primary ingest.

## Related

- [LIBERO](libero.md) · [Success-rate audit](../syntheses/platforms/vla-success-rate-audit.md) — why ordering inside the cluster is unsupportable
- [X-VLA](x-vla.md) — displaced MemoryVLA on Simpler-WidowX, lost to FLOWER on CALVIN
- [SimplerEnv](simplerenv.md) · [VLA models](../concepts/learning/vla-models.md)

## Open questions

- **All five need primary ingests.** MemoryVLA and FLOWER are the highest value: MemoryVLA held a 7 B SOTA that a 0.9 B model beat by 23.9 pts, and FLOWER holds the only benchmark X-VLA lost.
- Is **VLA-Adapter** actually an adapter method? The wiki is inferring from the name, which is exactly the kind of guess that should not survive into a claim.

## Mentioned in

- [TurboVLA: Real-Time Vision-Language-Action Model at 32 Hz on an RTX 4090 with <1 GB VRAM](../sources/turbovla-paper.md)
- [X-VLA: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model (Zheng, Li et al., Oct 2025)](../sources/xvla-paper.md)
