---
title: "Do As I Can, Not As I Say: Grounding Language in Robotic Affordances (SayCan)"
type: source
url: https://arxiv.org/abs/2204.01691
author: "Michael Ahn, Anthony Brohan, Noah Brown, Yevgen Chebotar, Chelsea Finn, Karol Hausman, Brian Ichter, Sergey Levine, Fei Xia, Andy Zeng, et al. (40 authors)"
affiliation: Robotics at Google, Everyday Robots
published: 2022-04-04
ingested: 2026-08-03
venue: CoRL 2022
format: conference paper (34 pp with appendices)
local_path: raw/2204.01691.pdf
license: arXiv preprint (v2, 2022-08-16)
tags: [saycan, llm-agent, affordances, value-functions, skill-selection, mobile-manipulation, palm, grounding, primary-source]
---

## Summary

**SayCan** is the skill-selection ancestor of the [code-as-policy](../concepts/agents/code-as-policy.md) lineage — the paper that established *LLM proposes, robot's own competence disposes*. Its insight is a clean probabilistic factorization: an LLM scores **how relevant** each available skill is to the instruction (`Say` — task grounding), a learned **value function** scores **how likely that skill is to succeed from the current state** (`Can` — world grounding), and the product picks the next action.

$$p(c_i \mid i, s, \ell_\pi) \propto \underbrace{p(c_\pi \mid s, \ell_\pi)}_{\text{affordance / Can}} \cdot \underbrace{p(\ell_\pi \mid i)}_{\text{LLM / Say}}$$

The motivating failure is memorable: asked to help with a spill, an ungrounded LLM suggests "try using a vacuum cleaner" — useless if there is no vacuum and the robot cannot operate one. The robot acts as "the language model's hands and eyes."

**Its relationship to the rest of the lineage is adversarial-by-design.** [Code as Policies](code-as-policies-paper.md) defines itself explicitly against SayCan: skill selection can only reach behaviors that already exist as named skills, so "move the coke can a bit to the right" is unreachable unless someone trained that skill. SayCan is the strongest possible version of the approach code-as-policy rejects.

## Key claims

### Results — 101 instructions, 7 families, real office kitchen

Robot: [Everyday Robots](../entities/everyday-robots.md) mobile manipulator (7-DoF arm, two-finger gripper). LLM: **PaLM 540B**. 15 objects, 5 semantic locations. Metrics are **human-rated** (3 raters, 2/3 agreement) for *plan* success and *execution* success.

| Setting | Plan | Execute |
|---|---:|---:|
| **Mock kitchen** (skills trained here) | **84%** | **74%** |
| **Real kitchen** (deployment) | 81% | **60%** |

The **14-point execution drop** from mock to real kitchen — with only a 3-point plan drop — isolates where the fragility lives: the *planner* transfers, the *low-level skills* do not.

### Ablations — both halves are load-bearing

| Variant | Plan | Execute |
|---|---:|---:|
| PaLM-SayCan | **84%** | **74%** |
| No value function (max LLM score) | 67% | — |
| Generative LLM + USE projection | 74% | — |
| **BC with natural language** (no LLM grounding) | — | **0%** |
| BC with USE-projected instruction | — | 9% |

Removing affordance grounding costs 17 points of planning. Removing language grounding entirely is **catastrophic — 0% across every family** (BC NL), and BC USE manages 60% only on single primitives and 0% on everything else. Grounding "nearly doubles the performance over the non-grounded baselines."

### Where it fails
- **Long-horizon is the worst family** (73% plan / 47% execute) — "most failures were a result of early termination by the LLM," e.g. bringing one object and stopping.
- **Embodiment tasks 64% plan**, failing mostly through affordance-function misclassification.
- **Negation** ("bring me a snack that isn't an apple") and ambiguous reference ("drinks with caffeine") both break it — inherited LLM weaknesses.
- Overall error split: **65% LLM failures, 35% affordance failures.**
- Structured language planned at 93% vs. natural-language verbs at 100% — the LLM parses free-form queries *better* than templated ones.

### Improves with a better LLM
The paper's forward-looking claim: "a robot's performance can be improved simply by enhancing the underlying language model." This is the first appearance in the wiki's lineage of the argument that robot capability rides LLM progress for free — the same bet [Waddle](waddle-labs-introducing-waddle.md) makes in 2026.

## Entities mentioned
- [Everyday Robots](../entities/everyday-robots.md) · [Google DeepMind](../entities/google-deepmind.md) (Robotics at Google)
- [Chelsea Finn](../entities/chelsea-finn.md) · [Sergey Levine](../entities/sergey-levine.md) · [Brian Ichter](../entities/brian-ichter.md) · [Karol Hausman](../entities/karol-hausman.md) · [Fei Xia](../entities/fei-xia.md) · [Andy Zeng](../entities/andy-zeng.md)

## Concepts touched
- [Code as policy](../concepts/agents/code-as-policy.md) — SayCan is the "model selects skills" branch.
- [LLM-agent architecture](../concepts/agents/llm-agent-architecture.md) — the canonical early instance.
- [Control abstraction levels](../concepts/robotics/control-abstraction-levels.md) — SayCan is level 3 (policy control) in Anthropic's taxonomy.
- [Real-world robot RL](../concepts/learning/real-world-robot-rl.md) — affordances *are* value functions of sparse-reward RL tasks.

## Open questions
- **The sample sizes are small.** 101 instructions total, **11–15 per family**. A 20-point difference between families (e.g. NL Nouns 67% vs NL Verbs 100%) rests on 15 trials each. Per the wiki's [success-rate audit](../syntheses/platforms/vla-success-rate-audit.md), at n=15 nothing under ~40 pp is detectable — so the *family-level ordering* in this paper is not supported, though the headline ablations (84 vs 0) are overwhelming.
- **Human-rated success** with 2-of-3 agreement is a different measurement class from programmatic success detection; inter-rater reliability is not reported.
- **No open-loop/closed-loop distinction** — SayCan plans once and has no retry behavior, which is precisely what [Inner Monologue](inner-monologue-paper.md) adds three months later, measuring SayCan at **~0% under adversarial disturbance**.

## Related sources
- [Inner Monologue](inner-monologue-paper.md) — direct successor; uses SayCan's environment, tasks, and value functions, and takes SayCan as its baseline.
- [Code as Policies](code-as-policies-paper.md) — the branch that rejects fixed skill menus.
- [How Claude Performs on Robotics Tasks](anthropic-how-claude-performs-on-robotics-tasks.md) — the 2026 re-measurement of "LLM commands a pretrained policy," with the override decision finally quantified.
