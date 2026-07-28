---
title: Anthropic Frontier Red Team
type: entity
subtype: lab
created: 2026-07-27
updated: 2026-07-27
sources: 3
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

A three-part robotics arc on the same hardware ([Unitree Go2](unitree-go2.md)), all ingested 2026-07-27:

1. **[Project Fetch: Can Claude train a robot dog?](../sources/anthropic-project-fetch-robot-dog.md)** (experiment Aug 2025, pub. 2025-11-12) — the **uplift** study. 8 staff, 2 arms of 4, one day; Claude arm 7/8 tasks vs 6/8, **181 min vs 361 min** on the shared subset.
2. **[Project Fetch: Phase Two](../sources/anthropic-project-fetch-phase-two.md)** (2026-06-18; Michael Ilie, C. Daniel Freeman, Kevin K. Troy) — the **autonomy** follow-through. Claude Opus 4.7 alone in Claude Code: **9 min 35 s** — 18.9× the assisted humans, 37.7× the unassisted. Closed-loop ball retrieval still fails.
3. **[How Claude Performs on Robotics Tasks](../sources/anthropic-how-claude-performs-on-robotics-tasks.md)** (2026-07-09; Shmuel Berman, Michael Ilie, Jia Deng, C. Daniel Freeman) — the **capability profile**. Eleven models × four [control abstraction levels](../concepts/robotics/control-abstraction-levels.md) × quadruped/humanoid/manipulation. Harness released as `github.com/safety-research/embody`.

The arc is unusually well-designed as evidence: **the same task ladder, the same robot, ten months apart**, measuring uplift and then autonomy. That is precisely what the *uplift-precedes-autonomy* premise needs and almost never gets.

Also referenced but **not ingested**: an earlier quadruped evaluation in the **Claude 4 System Card, p. 114** (Claude training a locomotion policy in simulation; not yet autonomously capable).

## Related
- [Anthropic](anthropic.md) — parent.
- [AI uplift studies](../concepts/safety/ai-uplift.md) — the methodology.
- [AI red-teaming](../concepts/safety/ai-red-teaming.md) — the adversarial-probing sibling genre. Note the difference in kind: red-teaming asks *can I make the model misbehave?*; the Frontier Red Team's uplift work asks *what can the model now make people able to do?* Both live under the "red team" label; only the first is about attacks.
- [Apollo Research](apollo-research.md) — the *external* evaluation counterpart Anthropic commissions.

## People (bylined on the robotics line)
- **Michael Ilie** — on both Phase Two and the robotics evaluation; the connective author across the arc.
- **C. Daniel Freeman** — likewise on both.
- **Kevin K. Troy** — Phase Two.
- **Shmuel Berman**, **Jia Deng** — the robotics evaluation.

No entity pages filed for any of them yet; see the backlog.

## Mentioned in
- [Project Fetch: Can Claude train a robot dog?](../sources/anthropic-project-fetch-robot-dog.md)
- [Project Fetch: Phase Two](../sources/anthropic-project-fetch-phase-two.md)
- [How Claude Performs on Robotics Tasks](../sources/anthropic-how-claude-performs-on-robotics-tasks.md)
