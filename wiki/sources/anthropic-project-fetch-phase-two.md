---
title: "Project Fetch: Phase Two"
type: source
url: https://www.anthropic.com/research/project-fetch-phase-two
author: Michael Ilie, C. Daniel Freeman, Kevin K. Troy
affiliations: Anthropic Frontier Red Team
published: 2026-06-18
ingested: 2026-07-27
venue: anthropic.com — Frontier Red Team
format: web article (evaluation report)
tags: [anthropic, claude, frontier-red-team, uplift-study, autonomy, quadruped, unitree-go2, claude-code, ai-safety, responsible-scaling]
---

## Summary

Seven months after [Project Fetch](anthropic-project-fetch-robot-dog.md), Anthropic re-ran the experiment with **no human team at all**: **Claude Opus 4.7**, in Claude Code, with adaptive thinking at maximum effort, driving the same quadruped through the same task ladder. On the four tasks every participant completed, the two human teams took **361 minutes** (no AI) and **181 minutes** (with Claude). Opus 4.7 took **9 minutes 35 seconds** — **37.7× faster** than the unassisted humans and **18.9× faster** than the Claude-assisted humans.

This is the paper that turns Fetch's *uplift-precedes-autonomy* hypothesis from an argument into a measurement, and it does so inside a single calendar year: **the same task ladder went from "humans get 2× uplift" to "the model does it essentially alone, 19× faster than the assisted humans."** The one thing Claude still could not do is the thing Phase One's Claude team also could not do — **precise, closed-loop retrieval of the ball**.

## Setup

- **Baseline** — the original experiment (run **August 2025**, published November 2025): human teams operated a quadruped via its manufacturer controller, connected to its sensors (video + lidar), wrote control programs, monitored movement, detected a beach ball, and attempted autonomous retrieval.
- **Change for Phase Two** — the **physical-controller task was removed** (a model has no hands for a handheld remote; Phase One's controller task was already flagged as a hardware-luck confound).
- **Subject** — **Claude Opus 4.7**, adaptive thinking at **maximum effort**, operating **in Claude Code**.
- **Human involvement** — deliberately minimal: connect the laptop, supply initial prompts, approve commands, authorize advancement between tasks. No debugging, no strategy.
- **Trials** — **three**, with elapsed time measured and success assessed qualitatively.

## Key claims

### Speed

On the **four tasks completed by all participants**:

| Participant | Time |
|---|---|
| Team Claude-less (4 humans, no AI) | **361 min** |
| Team Claude (4 humans + Claude) | **181 min** |
| **Claude Opus 4.7 (alone)** | **9 min 35 s** |

- **37.7×** faster than Team Claude-less.
- **18.9×** faster than Team Claude.

The 361 vs 181 figures also retroactively **pin down Phase One's "about half the time"** claim, which the original post gave only qualitatively.

### Code volume — the Phase One pathology disappears

| Participant | Lines of code |
|---|---|
| Team Claude | **10,309** |
| Team Claude-less | **1,136** |
| **Claude Opus 4.7** | **1,045** |

Two things fall out of this table:

1. It **confirms and quantifies** Phase One's "~9× more code" observation (10,309 / 1,136 ≈ **9.1×**).
2. **Opus 4.7 alone wrote *less* code than either human team** — slightly under the unassisted humans, and roughly **a tenth** of what the human+Claude team produced — for equal or better results. Phase One characterized the Claude team's 9× output as including "arguably distracting" side quests. Running without humans **removed the side quests**, not just the humans. Whatever generated that bloat was a property of the *collaboration*, not of the model.

> [!note] A caution on the comparison
> Team Claude's 10,309 lines were produced by four people each pairing with their own Claude instance on **parallel** objectives, over a full day, with exploration explicitly encouraged. Opus 4.7's 1,045 lines came from a **narrower, controller-free task list** in three trials. The ratio is real but the two numbers were not produced under matched conditions, and the source does not claim they were.

### What Claude still cannot do

**Precise closed-loop beach-ball retrieval — the actual "fetch."** The task requiring continuous feedback-based adjustment is where the model stops and, per the source, where humans remain better. This is the same wall Phase One's Team Claude hit (it could locate, navigate to, and nudge the ball but lacked the dexterity to retrieve it), and it is consistent with the [companion evaluation](anthropic-how-claude-performs-on-robotics-tasks.md)'s finding that **placing** is the bottleneck subgoal in manipulation and that low-level closed-loop control is where frontier models are weakest.

## Why this matters for the wiki

The [Frontier Red Team](../entities/frontier-red-team.md)'s stated premise in Phase One was that **uplift precedes autonomy** — that measuring how much a model helps humans is a leading indicator of what it will soon do alone. Phase Two is the follow-through, and the interval is the story: **roughly ten months from experiment to re-run** (Aug 2025 → Jun 2026), across which the same task ladder went from a 2× human uplift to near-autonomous execution at 19× the assisted-human speed.

That does *not* mean the threshold was crossed. The task is a beach ball in a warehouse; the retrieval step still fails; and Phase Two is **three trials**. But it is the wiki's only source where an uplift result and its autonomy follow-up are measured on **the same task ladder with the same hardware**, which is exactly what the uplift-as-leading-indicator argument requires and almost never gets.

## Limitations

- **Three trials.** No error bars, no distribution.
- **Not a matched comparison.** The controller task was removed, so "the four tasks completed by all participants" is a subset chosen post-hoc; and the humans were working a full day under different incentives.
- **Human-in-the-loop remains** — laptop connection, prompts, command approval, task advancement. This is *supervised* near-autonomy, not unattended operation. How much the approval step contributed is not isolated.
- **The retrieval failure is unquantified** — described qualitatively, with no success rate.
- **Single model.** No comparison to other frontier models on the same ladder (unlike the [companion evaluation](anthropic-how-claude-performs-on-robotics-tasks.md), which runs eleven).

## Open questions

- **What exactly did the human approvals authorize?** If command approval filtered dangerous or wrong actions, the 9m35s is a human-supervised number and the unattended figure would be worse — Phase One's opening anecdote (a robot commanded 1 m/s for 5 s toward a table under 5 m away) is the reason this matters.
- **Would a Phase Three drop the approval gate?** The stated trajectory points there.
- **Does the retrieval wall move with the [control abstraction level](../concepts/robotics/control-abstraction-levels.md)?** The companion evaluation shows models are far better supervising a pretrained policy than emitting low-level actions. Nobody has run Fetch with a pretrained grasping policy underneath Claude, which is the obvious next configuration.

## Entities mentioned

- [Anthropic Frontier Red Team](../entities/frontier-red-team.md) — authors.
- [Anthropic](../entities/anthropic.md).
- [Unitree Go2](../entities/unitree-go2.md) — the quadruped (identified by name in the [companion evaluation](anthropic-how-claude-performs-on-robotics-tasks.md), which links back to this page).

## Concepts touched

- [AI uplift studies](../concepts/safety/ai-uplift.md) — this is the uplift→autonomy follow-through.
- [Control abstraction levels](../concepts/robotics/control-abstraction-levels.md) — Claude Code writing controllers is *programmatic control* in the companion evaluation's taxonomy.
- [AI safety and alignment](../concepts/safety/ai-safety-alignment.md) — Responsible Scaling Policy thresholds.
