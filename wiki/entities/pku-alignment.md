---
title: PKU-Alignment (Peking University)
type: entity
subtype: lab
created: 2026-09-07
updated: 2026-09-07
sources: 2
tags: [pku-alignment, peking-university, yaodong-yang, safe-rl, cmdp, safe-rlhf, safety-gymnasium, safevla, alignment, china]
---

# PKU-Alignment

Alignment research group at the **Institute for Artificial Intelligence, Peking University**, led by **Yaodong Yang**, with the **State Key Laboratory of General Artificial Intelligence**, the **PKU-PsiBot Joint Lab**, and the **Zhongguancun Academy** appearing as co-affiliations. The wiki's entry point is [SafeVLA](../sources/safevla-paper.md) (NeurIPS 2025 Spotlight).

## Why it has a page

Because the same group produced three artifacts that this wiki keeps arriving at from different directions, and they form one line rather than three projects:

| Work | What it is |
|---|---|
| **Safe-RLHF** (Dai, Yang et al.) | separating *helpfulness* from *harmlessness* into a reward model and a **cost** model, then optimizing under a constraint rather than a blended reward |
| **[Safety-Gymnasium](safety-gymnasium.md)** (Ji, Zhang, Zhou, … Yang; NeurIPS 2023) | the standard safe-RL benchmark — **one of only three safety-specific RL environments** the [contact-rich survey](../sources/safe-learning-contact-rich-survey.md) names in its whole Table 3 — plus **SafePO**, 16 algorithms one file each |
| **[SafeVLA / ISA](../sources/safevla-paper.md)** (2025) | the same CMDP-plus-Lagrangian machinery applied to a **vision-language-action policy**, with [Safety-CHORES](safety-chores.md) as the embodied analogue of Safety Gymnasium |

The through-line is a single methodological commitment: **safety is a constraint, not a term in the objective.** Blending a safety penalty into a reward gives you a policy that will trade harm for reward at whatever exchange rate the coefficient implies; a constrained formulation gives you a policy that satisfies the constraint and then optimizes. SafeVLA's FLaRe-RS comparison is that argument finally measured on a robot policy — the shaped variant loses on **both** axes.

The group's other named alignment work (Ji et al. on lightweight alignment and language feedback, PKU-Alignment collaborations) is cited in SafeVLA but not ingested.

> [!note] Still partly thin
> **Safety-Gymnasium is now ingested.** Safe-RLHF, **OmniSafe** (their safe-RL infrastructure) and the group's LLM-alignment work are known here only through citations in the two papers that are.

> [!warning] The line is internally consistent except in one place
> Safety-Gymnasium (2023) criticizes OpenAI's Safety Gym for **binary indicator costs** — *"this representation method loses some information… when the robot collides with a vase and causes the vase to move at different velocities, there should be different cost values."* [SafeVLA](../sources/safevla-paper.md) (2025) then uses **binary unweighted costs** and defends the choice on the grounds that severity is context-dependent. Both defensible, neither measured against the other. See the [SafeVLA page](../sources/safevla-paper.md).

## Related

- [SafeVLA](../sources/safevla-paper.md) · [Safety-CHORES](safety-chores.md) · [Safety-Gymnasium](safety-gymnasium.md)
- [Safe reinforcement learning](../concepts/learning/safe-reinforcement-learning.md) — the paradigm this group works in.
- [Arash Ajoudani](arash-ajoudani.md) / [IIT](istituto-italiano-di-tecnologia.md) — the interaction-control tradition approaching robot safety from forces rather than from constrained optimization; the [contact-rich survey](../sources/safe-learning-contact-rich-survey.md) cites this group heavily and works in a different regime.
- [Allen Institute for AI](ai2.md) — whose embodied stack SafeVLA is built on.

## Mentioned in

- [SafeVLA paper](../sources/safevla-paper.md)
- [Safety-Gymnasium paper](../sources/safety-gymnasium-paper.md)
