---
title: Arash Ajoudani
type: entity
subtype: person
created: 2026-09-07
updated: 2026-09-07
sources: 1
tags: [arash-ajoudani, iit, hrii, physical-hri, impedance-control, variable-impedance, ergonomics, contact-rich, safe-learning]
---

# Arash Ajoudani

Head of the **Human-Robot Interfaces and Interaction (HRII)** lab at the [Istituto Italiano di Tecnologia](istituto-italiano-di-tecnologia.md) in Genova. Senior author of the wiki's first survey of the **physical** half of robot safety.

## Why he has a page

The wiki's safety coverage has been dominated by two traditions: **semantic safety** (DeepMind/ASIMOV — is the *goal* harmful) and **runtime filtering** (Pavone, Althoff — will this *action* leave the safe set). Ajoudani's line is the third and oldest one, and the one this wiki had no representative of: **physical human-robot interaction and interaction control** — compliance, impedance, passivity, force envelopes, ergonomics, and perceived safety as a measured quantity.

Ingested here:

- **[Safe Learning for Contact-Rich Robot Tasks: A Survey](../sources/safe-learning-contact-rich-survey.md)** (2025/2026, senior author, with Heng Zhang, Gokhan Solak, Rui Dai, Pokuang Zhou, Nikos Tsagarakis and Yu She) — ~400 works on safe exploration and safe execution in [contact-rich manipulation](../concepts/robotics/contact-rich-manipulation.md), the wiki's source for [impedance control](../concepts/robotics/impedance-control.md), [safety certificates](../concepts/robotics/safety-certificates.md), [safe RL](../concepts/learning/safe-reinforcement-learning.md) and [tactile sensing](../concepts/robotics/tactile-sensing.md).

He is also an author of *"Progress and prospects of the human–robot collaboration"* (Ajoudani, Zanchettin, Ivaldi, Albu-Schäffer, Kosuge & Khatib, *Autonomous Robots* 2018) — the survey's single most-cited reference, and the standard citation for pHRI's twin safety notions: **physical limits** (contact pressure, speed-and-separation, ergonomics) and **perceived safety** (predictability, comfort, trust). Not ingested.

## The group's research line

The survey's own most-cited empirical anchors are the group's work, and together they read as one bet stated three times, with the VLM moving progressively earlier in the stack:

| Work | Year | What it does |
|---|---|---|
| **SRL-VIC** (Zhang, Solak, Lahr, Ajoudani; RA-L) | 2024 | Variable-stiffness safe RL for contact-rich tasks — the safety comes from the *action space* being impedance |
| **OmniVIC** (Zhang, Huang, Solak, Ajoudani; arXiv 2510.17150) | 2025 | A self-improving variable impedance controller using **vision-language in-context learning** |
| **CompliantVLA-adaptor** (Zhang, Huang, Tong, Solak, P. Liu, S. Liu, Peters, Ajoudani; arXiv 2601.15541) | 2026 | **VLM-guided variable impedance action** for safe contact-rich manipulation |

Also from the group: *"A survey on imitation learning for contact-rich tasks in robotics"* (Tsuji, Kato, Solak, Zhang, Petrič, Nori, Ajoudani, 2025) — the companion survey covering the half the safe-learning survey deliberately excludes.

> [!note] Read the self-citation honestly
> These works are cited across many sections of the survey they also authored, and none of them is ingested here. That is normal for a survey written by an active group, and it is also why the survey's foundation-model claims should be treated as **the group's research programme stated as a field direction** — a defensible one, but not an independent review of it. The control-theoretic and task-taxonomy material reads as first-hand and is not affected.

## Related

- [Istituto Italiano di Tecnologia](istituto-italiano-di-tecnologia.md) — HRII's institutional home.
- [Marco Pavone](marco-pavone.md) — the runtime-filtering tradition, approaching the same problem from formal guarantees rather than interaction control.
- [Impedance and admittance control](../concepts/robotics/impedance-control.md) — the group's central mechanism.

## Mentioned in

- [Safe Learning for Contact-Rich Robot Tasks (survey)](../sources/safe-learning-contact-rich-survey.md)
