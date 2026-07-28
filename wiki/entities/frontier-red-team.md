---
title: Anthropic Frontier Red Team
type: entity
subtype: lab
created: 2026-07-27
updated: 2026-07-27
sources: 1
tags: [anthropic, ai-safety, red-teaming, uplift-study, policy, responsible-scaling, frontier-red-team]
---

**Anthropic Frontier Red Team** — the internal [Anthropic](anthropic.md) team that measures what frontier models are becoming *newly capable of* in domains with national-security or catastrophic-risk relevance, and feeds those measurements into the **Responsible Scaling Policy**'s capability thresholds. Its output is published under **Policy > Frontier Red Team** on anthropic.com. Distinct from the model-safety/alignment research org: the Frontier Red Team's unit of work is a **capability evaluation**, not a training intervention.

## Method: the uplift study

The team's signature instrument is the **randomized [uplift study](../concepts/safety/ai-uplift.md)** — split participants into an AI-access arm and a no-AI arm, hold the task fixed, and measure the performance differential. Originally applied to **biological risk**; ported to robotics in [Project Fetch](../sources/anthropic-project-fetch-robot-dog.md) (November 2025), which measured how much faster non-roboticist staff could program a quadruped with Claude in the loop.

The team's stated interpretive frame is that **uplift is an early indicator of autonomy**: the capability to help a human do X shows up before the capability to do X unassisted (their cited precedent — code debugging assistance preceded code generation). So measuring uplift on a task the model *cannot yet do alone* is treated as forecasting, not just productivity measurement.

## Why robotics

Robotics is not tracked for its own sake. [Project Fetch](../sources/anthropic-project-fetch-robot-dog.md)'s reflection ties it to the **autonomous AI R&D** threshold in the Responsible Scaling Policy: a model that can interact competently with **previously unknown physical hardware** is closer to a model that can run its own experimental loop, and autonomous AI R&D is flagged as a path to "rapid, unpredictable advances" outpacing risk evaluation. As of that post, models were assessed as **below** the threshold.

The team distinguishes two horizons explicitly: **controlling existing hardware** (nearer) vs **designing and building new hardware** (further).

## Published work in this wiki

- [Project Fetch: Can Claude train a robot dog?](../sources/anthropic-project-fetch-robot-dog.md) (2025-11-12) — the quadruped uplift study. 8 staff, 2 teams, one day; Team Claude 7/8 tasks vs 6/8 and ≈half the wall-clock on shared tasks.
- *How Claude Performs on Robotics Tasks* (anthropic.com/research/claude-plays-robotics) — **not yet ingested**; the apparent autonomy-side companion to Project Fetch.
- Earlier quadruped evaluation summarized in the **Claude 4 System Card, p. 114** (Claude training a locomotion policy in simulation; not yet autonomously capable). Not ingested.

## Related
- [Anthropic](anthropic.md) — parent.
- [AI uplift studies](../concepts/safety/ai-uplift.md) — the methodology.
- [AI red-teaming](../concepts/safety/ai-red-teaming.md) — the adversarial-probing sibling genre. Note the difference in kind: red-teaming asks *can I make the model misbehave?*; the Frontier Red Team's uplift work asks *what can the model now make people able to do?* Both live under the "red team" label; only the first is about attacks.
- [Apollo Research](apollo-research.md) — the *external* evaluation counterpart Anthropic commissions.

## Mentioned in
- [Project Fetch: Can Claude train a robot dog?](../sources/anthropic-project-fetch-robot-dog.md)
