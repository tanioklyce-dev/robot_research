---
title: GEN-1.5
type: entity
subtype: model
created: 2026-09-07
updated: 2026-09-07
sources: 1
tags: [gen-1-5, generalist-ai, robot-foundation-model, in-context-learning, physical-prompting, one-shot, emergence, test-time-training, improvisation]
---

# GEN-1.5

[Generalist AI](generalist-ai.md)'s robot foundation model (announced **2026-08-19**), and the wiki's strongest claim of **one-shot in-context learning of physical skills** ([source](../sources/generalist-gen-1-5-blog.md)).

## What is stated about it

| | |
|---|---|
| Architecture | "a large multimodal model" — **no size, no parameter count, no compute figure given** |
| Context | **30 seconds** of video memory, plus *"other sensor, language, and proprioceptive inputs"* (unspecified) |
| Output | **100 Hz action trajectories** — a trajectory resolution; **no inference rate or latency is given** |
| Pretraining | **8+ months continuous**, three phases; **1,891,392 scenes** from homes, warehouses, factories; **no simulation data** |
| Embodiment | **not named**, anywhere |

## Reported capabilities

- **One-shot in-context** — a 3–12 s demonstration in context, no gradient updates: **59% ± 10%** across 10 tasks (zippers, jar lids, money from a wallet, marker into cup, pouring bolts, brushing, vacuum pad). Prompts recorded as **handheld-gripper human data** or robot rollouts. Generalist calls this **physical prompting**.
- **Few-step adaptation** — **83% ± 9%** after 10 gradient steps on 5 minutes (~50 demos); **66.5%** from **one** step on **one** minute. **Ten steps move the weights <0.15%** — *"reminding the model of something it nearly knows."*
- **Compositional generalization** — two independent prompts in context chain into one behavior, with bridging motions *"that appear in neither prompt."*
- **Prompt from simulation, act in reality** — despite zero simulation data in pretraining.
- **Human-to-robot** — a person demonstrates with their hands in view of the cameras; *"in some cases"* the robot reproduces it.
- **Improvisation** — banana as a makeshift brush; a dustpan used by lifting-and-dumping (a novel contact sequence); removing a paper obstacle never present in the task data; bimanual jar-opening from one-handed demos; spontaneous colour-sorting.

> [!note] The claim that would matter most if it holds
> **Improvisation strengthens as fine-tuning steps decrease** — *"lightly adapted models stay closer to their pretrained priors and can draw on a broader repertoire."* Stated as a **capability** trade-off between task-specific competence and generality, tunable by step count. If real, it is a design principle (*adapt as little as you can*) and the inverse of the field's instinct to fine-tune to convergence.

> [!warning] Evidence grade: vendor blog, no counts
> No rollout counts, no per-task breakdown, no baselines, no ablations, no released artifacts, no third-party evaluation. The ±figures are unlabelled as to what they range over. The post is candid that *"the tasks are simple and short-horizon,"* success rates are *"modest,"* and in-context skills are *"more brittle than finetuned models"* — but the numbers themselves support nothing quantitative under [this wiki's standard](../concepts/robotics/robot-policy-evaluation.md).
>
> Critically, the **emergence** claim is under-evidenced on its own terms: the post shows a model that *has* in-context learning and a validation loss that improves over eight months. It does **not** show in-context ability appearing at a scale threshold, which is the figure the claim needs.

## Related

- [Generalist AI](generalist-ai.md) — the company; GEN-0 → GEN-1 → GEN-1.5.
- [In-context robot learning](../concepts/learning/in-context-robot-learning.md) — the capability, and Generalist's **disagreement with [Skild](skild-ai.md) about whether the inner loop is built or grown**.
- [Test-time adaptation](../concepts/learning/test-time-adaptation.md) — the 1–10 step regime, which they call test-time training.
- [VLA models](../concepts/learning/vla-models.md) — the language-conditioned alternative they argue against.

## Mentioned in

- [GEN-1.5 blog post](../sources/generalist-gen-1-5-blog.md)
