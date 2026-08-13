---
title: RT-H
type: entity
subtype: model
created: 2026-08-04
updated: 2026-08-04
sources: 2
tags: [rt-h, action-hierarchy, language-motions, action-representation, corrections, interactive-imitation-learning, rt-2, pali-x, google-deepmind, stanford]
---

**RT-H (Robot Transformer with Action Hierarchies)** — a [Google DeepMind](google-deepmind.md) + Stanford policy that predicts a **language motion** (*"move arm forward," "rotate arm right"*) as an intermediate layer between the task description and the low-level action, using one [PaLI-X](pali-x.md) 55B VLM for both queries ([paper](../sources/rt-h-paper.md), 2024). The wiki's **primary reference for a human-readable intermediate action representation**.

## The mechanism

| | |
|---|---|
| **Hierarchy** | `π_h: (obs, task) → language motion`, then `π_l: (obs, task, motion) → action` |
| **Backbone** | Single [PaLI-X](pali-x.md) 55B VLM, co-trained on the [RT-2](rt-2.md) internet-scale mixture; ViT frozen |
| **Motion vocabulary** | **2,500+ phrases, zero human annotation** — mechanically extracted from proprioception |
| **Actions** | RT-2-style: 9 dims (3 delta position, 3 delta rotation, 2 base, 1 gripper) discretized to 256 bins |
| **Inference** | Two sequential queries doubles latency; solved by **asynchronous querying** (motion predicted one step ahead, batched) |
| **Data** | Diverse+Kitchen: 100K demos (70K RT-1/RT-2 Kitchen + 30K new Diverse) |

**How the vocabulary is built** — map each of the 9 action dimensions to a spatial word, threshold out small dimensions, compose the survivors in magnitude order. *"Move arm forward and close gripper."* The combinatorics do the rest.

> [!note] RT-H's "language" is a labeled discretization of its own action space
> Not learned semantics, not hand-authored per task: a **fixed generative grammar** (axis words × sign × composition order) applied to a thresholded partition of the robot's 9-D action space. That makes it a genuine **controlled natural language** with a specified grammar and an induced lexicon — and it makes the embodiment coupling exact. The 9 dimensions are *this* robot's (arm deltas + mobile base + parallel gripper); a suction cup or a five-finger hand requires redefining the extraction, hence the whole vocabulary. **The grammar might port; the lexicon cannot.** See [action representation languages](../syntheses/agents/action-representation-languages.md).

## Why it matters

**The words carry value beyond the partition.** RT-H-OneHot relabels the *same* language motions as integers and performs **much worse**: *"while action hierarchy itself gets us part of the way, the structure of language greatly improves language motion and action prediction."* This is the same measurement as [TurboVLA](turbovla.md)'s task-ID ablation (95.4 vs 97.7 semantic English, p = 0.0001) — two years apart, 55B vs 0.2B, VLM-centric vs [LLM-free](../concepts/learning/llm-free-vla.md), same conclusion.

**Data sharing at the motion layer.** *"Pour a cup"* and *"pick up a coke can"* share no task-level semantics but **entirely overlap at the language motion level** until the object is picked. This is a data-efficiency argument for the readable layer, not an ergonomics one — the strongest reason to want it.

**Corrections in language, learned cheaply.** A human types or speaks a replacement phrase mid-episode; only the *motion query* is retrained afterward, since the action query already executes the corrected phrase. **40% → 63% with 30 correction episodes per task**, versus teleop-corrected RT-2-IWR at 13%.

**Motion prediction is the bottleneck, not action decoding.** Offline MSE with ground-truth motions is **40% lower** than end-to-end — which is why intervening at the motion layer pays.

## Measured results (n = 80: 8 tasks × 10 trials; 95% Wilson CIs reported)

| Claim | Verdict |
|---|---|
| +15 pp over [RT-2](rt-2.md) (~40 vs ~25%) | **survives, marginally** (p = 0.043) |
| Corrections 40 → 63% | **survives** (p = 0.0036) |
| 63% vs RT-2-IWR 13% | **survives** (p < 0.0001) |
| Object generalization 65 vs 55% (n=50) | **TIE** (p = 0.31) |

## Limitations

- Absolute success stays at **63%** after corrections on the hard eight.
- Hierarchy introduces failure modes a flat model lacks — oscillation, getting stuck re-predicting *"close gripper."*
- Correction quality is capped by the action query; when a phrase overshoots, the operator's only recourse is more phrases.
- **Its own cross-embodiment proposal was never executed** — Future Work suggests bridging [OXE](open-x-embodiment.md) embodiments and human video via language motions; the 2026 field went to unified latent tokens instead.
- No LIBERO or standard-benchmark numbers, so it cannot be placed in the wiki's [LIBERO table](libero.md).

## Related
- [Action representation languages](../syntheses/agents/action-representation-languages.md) — the synthesis RT-H anchors
- [RT-2](rt-2.md) — the flat baseline and the backbone recipe
- [TurboVLA](turbovla.md) — the independent confirmation of the language-over-labels result
- [MolmoAct](molmoact.md) — the *visual* readable intermediate; its trace editing was found more reliable than language correction
- [π0.5](pi-zero-5.md) — semantic-subtask hierarchy, one level of abstraction above RT-H's motions

## Mentioned in
- [RT-H paper](../sources/rt-h-paper.md)
