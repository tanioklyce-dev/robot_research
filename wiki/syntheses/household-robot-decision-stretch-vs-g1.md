---
title: Household robot decision — Stretch vs Unitree G1
type: synthesis
created: 2026-05-08
updated: 2026-05-08
tags: [stretch, unitree-g1, decision, household-robot, comparison, hello-robot, recommendation]
---

# Household robot decision — Stretch vs Unitree G1

A buying-decision comparison for the use case: **a research-grade robot to navigate a home, pick things off the floor, put away dishes, and open cans.** Two candidates: [[stretch|Hello Robot Stretch 3]] (research-tier mobile manipulator) and [[unitree-g1|Unitree G1]] (affordable bipedal humanoid). This page documents the comparison + recommendation so future similar decisions can reuse the analysis.

> [!note] TL;DR
> **Stretch 3 wins decisively for this use case.** G1 is exciting research hardware but the wrong tool for "useful chores around the house." Stretch has bundled software, published academic evidence on the exact tasks (RUM), and is purpose-built for unmodified home environments. G1 is research-grade humanoid hardware where you'd build the household stack from scratch.

## Open-source comparison

| | [[stretch\|Stretch]] | [[unitree-g1\|Unitree G1]] |
|---|---|---|
| Hardware | Closed (commercial product) | Closed (commercial product) |
| Low-level SDK | `stretch_body` (Python, open) | `unitree-sdk2` (open) |
| High-level stack | **[[stretch-ai\|stretch_ai]] Apache-2.0** — mapping, perception, manipulation primitives, **LLM agent for natural-language tasking** | None bundled. Locomotion examples + RL boilerplate. |
| Pre-trained policies | **[[robot-utility-models\|Robot Utility Models]]** — 5 zero-shot policies (door opening, drawer opening, tissue pickup, paper-bag pickup, object reorientation), open-source | None — academic locomotion code exists but no household-task policies |
| Documentation | Extensive ROS 2 + Python tutorials | SDK reference + a few demos |

**Both have open *software*; only Stretch has an open *application* layer.** That distinction is what matters for a non-research-team user — Stretch ships with a working LLM agent, RUM-style trained policies, and integration code. G1 ships with locomotion examples.

## Capability vs the task list

| Task | [[stretch\|Stretch]] | [[unitree-g1\|G1]] |
|---|---|---|
| **Navigate around a house** | ✅ **Designed for this.** Compact diff-drive base, ROS 2 + Nav2 stack, stable, no falls. RealSense + LiDAR onboard. | ⚠️ Bipedal locomotion in cluttered homes is *unsolved* in 2026. Falls are catastrophic; obstacle avoidance is research-grade. |
| **Pick up things off the floor** | ✅ **RUM bag/tissue/object pickup is open-source and zero-shot.** Telescoping arm reaches floor with stable base. | ❌ Bend-balance-grasp while bipedal is research-grade; no published reliable demos. |
| **Put away dishes** | ⚠️ **Partially feasible.** Single-arm ~1.5 kg payload — light items plausible, heavy plates challenging. RUM did drawer opening; cabinet/dishwasher work is DIY. | ❌ Bimanual is technically possible but no published demo of dish handling. |
| **Open cans** | ❌ Pull-tab cans need fine-tipped end-effector + sub-mm precision. Stock gripper is too coarse. | ❌ Same problem. G1's hands aren't fine-tipped enough either. |

**Reality check on tasks 3 and 4:** Putting away dishes and opening cans are **beyond both robots' 2026 out-of-the-box capability**. For Stretch, they're aspirational with significant per-home data collection. For G1, they're research projects from very little.

## Cost (approximate; verify with vendors)

| | [[stretch\|Stretch 3]] | [[unitree-g1\|G1]] |
|---|---|---|
| Starter config | ~$25,000 (base Stretch 3) | ~$16,000 (G1 EDU base) |
| Realistic "research-ready" | ~$25–30k (Stretch + optional accessories) | **~$30–45k** (G1 EDU+ with extra DOF + dexterous hands; pricing opaque) |
| Per-home setup time | Basically zero — ships ready | Significant — build the household stack |
| Software cost | Free (Apache 2.0 stack + RUM) | Free SDK; your time |

> [!note] G1 starter price is misleading
> The headline ~$16k G1 number is the EDU base, with limited DOF and basic hands. To match Stretch's manipulation capability you spec up to G1 EDU+ + arm extensions + dexterous hands, and the apparent price advantage disappears. **Configurations matter — match capability before comparing cost.**

## Published evidence (what the wiki has)

- **[[stretch|Stretch]]** + **[[stretch-ai|stretch_ai]]** + **[[robot-utility-models-paper|RUM Paper]]** — concrete published evidence that Stretch + the RUM stack hits **~90% zero-shot success** on door opening, drawer opening, tissue pickup, paper-bag pickup, and object reorientation across **2,950 robot rollouts** in NYC, NJ, and PA homes. Three of those tasks overlap directly with the floor-pickup goal.
- **[[unitree-g1|G1]]** — entity in this wiki is a stub. **No source page cites a published household-task result on G1.** The platform is academically used for **locomotion + RL research**, not household chores.

This evidence asymmetry maps directly to the decision: Stretch has a research line specifically targeting "low-cost robot doing useful tasks in unmodified homes." G1 has a research line targeting "humanoid locomotion and whole-body control."

## Recommendation: **Stretch 3**

In priority order:

1. **The exact use case is published academic research.** [[robot-utility-models-paper|RUM]] tested ~3 of the 4 task categories with 90% zero-shot success in real homes. You can run their open-source code on day one.
2. **The software stack is bundled.** [[stretch-ai|stretch_ai]] gives mapping, navigation, manipulation primitives, and an LLM agent out of the box. With G1, you build all of this.
3. **Safety + reliability.** Wheeled mobile manipulators don't fall. Bipedal humanoids do, in surprising ways, in clutter. For a home with people / pets / floors, this is decisive.
4. **Cost parity once equipped.** A fully-equipped G1 isn't dramatically cheaper than Stretch — and it gets you a less-suitable platform.

## Realistic expectations even with Stretch

- ✅ **Tasks 1–2 (navigate + floor pickup) are mostly solved** by [[stretch-ai|stretch_ai]] + [[robot-utility-models|RUM]]. Working in weeks, not years.
- ⚠️ **Task 3 (dishes)** needs DIY data collection per dish type / kitchen layout. Realistic success in the 50–70% range for forgiving cases (loading prewashed flatware, putting plates in racks). Loading a real dishwasher is research-frontier.
- ❌ **Task 4 (opening cans)** needs custom end-effector tooling. The stock gripper won't do pull-tabs reliably no matter the platform. **Don't plan on this working in 2026.**

## When G1 *would* be the right choice

- You're doing **bipedal humanoid research** as the primary goal — locomotion, whole-body control, fall recovery, RL on humanoids. G1 is the cheapest platform for that.
- You want to **track the leading edge of humanoid VLAs** — closer to where [[nvidia-groot|GR00T]] and [[figure|Figure Helix]] live.
- You're OK with **research-from-scratch** rather than off-the-shelf application.

For *household chores as the goal*, none of those reasons apply.

## Sources used in this synthesis

- [[stretch|Stretch entity]] / [[stretch-ai|stretch_ai entity]] / [[hello-robot|Hello Robot entity]]
- [[unitree-g1|Unitree G1 entity]] / [[unitree-h1|Unitree H1 entity]]
- [[robot-utility-models|Robot Utility Models entity]] + [[robot-utility-models-paper|RUM Paper]] (the empirical anchor for Stretch's task suitability)
- [[robot-utility-models-website|RUM Project Page]]
- [[hello-robot-stretch-docs|Hello Robot Stretch Documentation]]
- [[stretch-ai-llm-agent-docs|stretch_ai LLM Agent Documentation]]
- [[humanoid-platforms-survey|Humanoid platforms survey]] — landscape context for G1.
- [[robot-platforms-comparison|Robot platforms — comparison]] — non-humanoid landscape.

## Open questions / TBD

> [!note] Pricing snapshot, not sticker
> Both prices are approximate as of 2026-05 and shift with configuration. Vendor sites are authoritative; verify before purchase.

> [!note] G1's trajectory could change this answer in 1–2 years
> Unitree iterates rapidly. If a future G1 generation ships with bundled household-application stacks (or a parallel Chinese ecosystem develops) the recommendation could flip. As of 2026-05, the published evidence makes Stretch the unambiguous answer for this task list.

## Related

- [[lewm-on-rosorin-pro-feasibility|LeWM on ROSOrin Pro — feasibility analysis]] — adjacent decision document for an educational-tier alternative.
- [[robot-platforms-comparison|Robot platforms — comparison]] — broader landscape.
- [[humanoid-platforms-survey|Humanoid platforms survey]] — humanoid-specific landscape.
- [[sim-heavy-vs-real-data-paths|Sim-heavy vs real-data paths to generalist policies]] — relevant context for "where the data comes from."
