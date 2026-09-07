---
title: NVIDIA Alpamayo
type: entity
subtype: model-family
created: 2026-09-07
updated: 2026-09-07
sources: 1
tags: [alpamayo, nvidia, vla, autonomous-vehicles, reasoning, chain-of-thought, explainability, open-models, safety, level-4]
---

# NVIDIA Alpamayo

NVIDIA's **open family of reasoning vision-language-action models, simulation frameworks and datasets for autonomous vehicles**, announced 2026-01-05. Chain-of-thought [VLAs](../concepts/learning/vla-models.md) built for **Level 4** autonomy that *"reason over complex driving scenes, verbalize decision logic and support interpretable and auditable autonomy."*

> [!note] Page status: thin and partly web-researched
> This page exists because [Riccardo Mariani](riccardo-mariani.md) cites Alpamayo on the [Industrial AI Podcast](../sources/industrial-ai-podcast-nvidia-safety-strategy.md) as NVIDIA's instance of *a model designed for safety*. No Alpamayo primary — announcement, model card, or paper — has been ingested; the description above is from NVIDIA's public announcement material, verified but not read in depth. Treat the capability claims as vendor claims.

## Why it is in this wiki

Because it is the concrete artifact behind a claim the wiki has been treating as aspirational: that a **generative policy can be a safety component rather than only the thing being guarded**.

Mariani's framing is that Alpamayo-class models *"are designed for safety in that sense that they provide explainability and transparency, and then can be used as a **safety judge**."* The design bet is that **verbalized reasoning is auditable reasoning** — if the model states why it acted, a certification process has something to inspect, which is exactly what a black-box policy denies it.

Openness is presented as part of the safety argument rather than as marketing: fully open models, simulation frameworks and datasets, so that regulators and integrators can *"inspect, extend, and fine-tune the technology to meet regional safety standards."*

> [!warning] The wiki's evidence runs against the strong version of this
> "Verbalized reasoning is auditable reasoning" is a claim with counter-evidence on both sides of this wiki. [Gemini Robotics 2](../sources/gemini-robotics-2-safety-report.md): frontier models score **100%** acting on a safety signal handed to them and cannot reliably *produce* one from perception. And the [evaluation-awareness](../sources/goodfire-verbalized-eval-awareness.md) line documents stated reasoning that does not correspond to the computation behind the answer.
>
> None of that refutes Alpamayo — it is a model trained specifically for the task, and no measurement of *it* is in this wiki. It does mean the wiki should not carry "reasoning VLAs make autonomy auditable" as established, and should want the primary.

## Related

- [Riccardo Mariani](riccardo-mariani.md) — cites it as the safety-designed model.
- [NVIDIA Halos](nvidia-halos.md) — the safety programme; whether Alpamayo runs inside the certified envelope or advises it from outside is an open question.
- [VLA models](../concepts/learning/vla-models.md) · [chain-of-thought](../concepts/learning/chain-of-thought.md) — the model class and the mechanism.
- [Semantic safety](../concepts/safety/semantic-safety.md) — what "safety judge" would have to mean, and how it is measured.

## Mentioned in

- [Industrial AI Podcast #352 — NVIDIA's safety strategy](../sources/industrial-ai-podcast-nvidia-safety-strategy.md)
