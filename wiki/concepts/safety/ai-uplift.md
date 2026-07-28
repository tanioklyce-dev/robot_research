---
title: AI uplift studies
type: concept
created: 2026-07-27
updated: 2026-07-27
sources: 3
tags: [ai-safety, uplift-study, evaluation, methodology, rct, responsible-scaling, frontier-red-team, robotics, autonomy]
---

**An uplift study** measures how much an AI system raises a *human's* performance on a task, by randomizing participants into a treatment arm (AI access) and a control arm (no AI), holding the task fixed, and comparing outcomes. "Uplift" is the differential. It is a straightforward RCT design, imported into AI safety from **biological-risk evaluation**, where the question — *does this model make it meaningfully easier for a non-expert to do something dangerous?* — is more decision-relevant than any benchmark score.

It answers a question benchmarks structurally cannot: **capability benchmarks score the model alone; uplift studies score the human-plus-model system.** For any domain where the risk is mediated by a person, the second number is the one that matters.

## Why safety teams run them: uplift as a leading indicator of autonomy

The load-bearing inference, argued explicitly in [Project Fetch](../../sources/anthropic-project-fetch-robot-dog.md):

> In AI, the ability to **help a human** do X reliably shows up **before** the ability to do X **unassisted**.

Their cited precedent is code: assistants that could help you *debug* code preceded assistants that could *write* it. If that ordering holds, then measuring uplift on a task the model can't yet do alone is **forecasting**, not productivity measurement — you are reading the leading edge of a capability before it becomes autonomous. That is why [Anthropic's Frontier Red Team](../../entities/frontier-red-team.md) treats a robotics uplift result as a signal about the **autonomous AI R&D** threshold in the Responsible Scaling Policy, rather than as a robotics finding.

### The hypothesis got tested — on the same task ladder, ten months later

Uplift-as-leading-indicator is normally unfalsifiable in practice, because nobody re-runs the study. This one was re-run. [Project Fetch: Phase Two](../../sources/anthropic-project-fetch-phase-two.md) put **Claude Opus 4.7 alone** on the same robot and the same tasks:

| | Time on the shared task subset |
|---|---|
| 4 humans, no AI (Aug 2025) | **361 min** |
| 4 humans + Claude (Aug 2025) | **181 min** — the 2× uplift |
| **Opus 4.7, alone (Jun 2026)** | **9 min 35 s** — 18.9× / 37.7× |

The ordering held, and the interval was **ten months**. Two qualifications keep this from being a clean confirmation: the model still failed the **closed-loop retrieval** step — the same wall the human+Claude team hit — and Phase Two is **three trials** with humans still approving commands. So what was demonstrated is *supervised* near-autonomy on the parts of the ladder that were already the model's strong suit, not the crossing of a threshold.

> [!note] The most interesting number is the code volume
> Team Claude wrote **10,309** lines; the unassisted humans **1,136**; **Opus 4.7 alone, 1,045** — *fewer than either human team*, for equal or better results. Phase One read the AI arm's 9× output as "arguably distracting side quests." Removing the humans removed the bloat. **The pathology belonged to the collaboration, not to the model** — which is a finding about human-AI workflow design, not about capability, and it is the one result in this cluster that generalizes straight to everyday practice.

## What the design measures well, and what it doesn't

**Measures well:**
- Task completion counts and wall-clock time under a fixed deadline.
- *Where in a workflow* the advantage concentrates. Project Fetch's most useful result is not "2× faster" but **which sub-task** the gap lived in: connecting to unfamiliar hardware and extracting sensor data — not writing control logic, where the control arm was actually **faster**.
- Behavioral and affective side-effects, via transcript analysis. Project Fetch used LIWC-style dictionary counts (Pennebaker & Francis 1996; Tausczik & Pennebaker 2010) with Mann-Whitney U tests, finding a large negative-emotion effect (d = 2.16) in the no-AI arm, and a **work-style divergence**: the AI arm fragmented into individuals each pairing with their own model instance, rather than collaborating.

**Doesn't measure:**
- **Autonomy.** An uplift study says nothing about what the model does alone. Project Fetch states this outright.
- **Understanding.** The AI arm wrote ~9× more code and finished faster; participants speculated the *control* arm would score higher on a post-hoc quiz about the libraries involved. Speed and comprehension can move in opposite directions and only one is instrumented.
- **Whether volume is progress.** Much of that 9× was self-described "side quests" parallel to the objective.

## The control-arm problem

The sharpest methodological weakness, and Project Fetch concedes it: when the control arm consists of **habituated daily users of the tool being withheld**, you are not measuring "no-AI baseline performance." You are measuring **withdrawal**. Participants described going without Claude as "strange" and some felt their coding skills had degraded — six months after Claude Code shipped.

This cuts both ways on the affect result. A large negative-emotion effect in the control arm is consistent with "robotics without AI help is frustrating" *and* with "having your daily tool removed is frustrating," and the design cannot separate them. A control arm of genuine AI non-users would plausibly show a much smaller effect; a treatment arm of AI novices would need acclimation time it wasn't given.

Generally: **an uplift study's external validity is capped by how representative its control arm's baseline is.** Convenience samples of employees at the lab building the tool are the hardest case.

## Instances in this wiki

- **[Project Fetch](../../sources/anthropic-project-fetch-robot-dog.md)** (Anthropic Frontier Red Team, experiment Aug 2025 / pub. 2025-11-12) — the only ingested uplift study proper. Robotics domain: 8 non-roboticists, 2 arms of 4, one day, program a quadruped to fetch a beach ball. Treatment arm: 7/8 tasks vs 6/8, 181 vs 361 min, only arm to reach partial autonomy, ~9× more code. Biological-risk uplift studies are referenced as the method's origin but are not ingested.
- **[Project Fetch: Phase Two](../../sources/anthropic-project-fetch-phase-two.md)** (2026-06-18) — the autonomy follow-through on the same ladder; see above.
- **[How Claude Performs on Robotics Tasks](../../sources/anthropic-how-claude-performs-on-robotics-tasks.md)** (2026-07-09) — the other end of the axis: not uplift at all, but a direct capability profile across [control abstraction levels](../robotics/control-abstraction-levels.md). Useful here because it explains *why* the retrieval step survives both Fetch runs — closed-loop low-level control is exactly where frontier models are weakest, and models are far stronger when they **write** the controller than when they **are** the controller.

> [!note] A gap worth naming
> The wiki is thick with **capability benchmarks** (LIBERO, DROID, Meta-World, RoboCasa, real-robot success rates) and has exactly **one** human-in-the-loop uplift measurement. For robotics specifically — a field where nearly all deployment is currently human-supervised — the "how much faster does a person get" axis is almost entirely unmeasured in the sources here. The closest adjacent artifacts are the **FRC AI-first dev-loop** reports ([Team 254](../../sources/team-254-ai-in-frc-presentation.md), [Team 4414](../../sources/team-4414-hightide-2026-binder.md)), which claim large workflow uplift from agentic coding on real robots but with **no control arm** — testimony, not measurement.

## Related concepts
- [Control abstraction levels](../robotics/control-abstraction-levels.md) — *where* the model is allowed to act, and why that changes its measured capability by orders of magnitude. An uplift number without an abstraction level is under-specified.
- [AI red-teaming](ai-red-teaming.md) — the adversarial sibling: *can I make the model misbehave?* vs uplift's *what can the model make people able to do?* Both published under "red team" labels.
- [AI safety and alignment](ai-safety-alignment.md) — Responsible Scaling Policy capability thresholds are what uplift results feed into.
- [AI guardrails](ai-guardrails.md) — the deployment-time pole; uplift studies are an evaluation-time instrument.
- [LLM-agent architecture](../agents/llm-agent-architecture.md) — the autonomy end of the same axis. Uplift = model writes the code, human runs the loop; agents = model is *in* the loop.

## Mentioned in
- [Project Fetch: Can Claude train a robot dog?](../../sources/anthropic-project-fetch-robot-dog.md)
- [Project Fetch: Phase Two](../../sources/anthropic-project-fetch-phase-two.md)
- [How Claude Performs on Robotics Tasks](../../sources/anthropic-how-claude-performs-on-robotics-tasks.md)
