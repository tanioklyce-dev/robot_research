---
title: "VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models"
type: source
url: https://arxiv.org/abs/2307.05973
author: "Wenlong Huang, Chen Wang, Ruohan Zhang, Yunzhu Li, Jiajun Wu, Li Fei-Fei"
affiliation: Stanford University, University of Illinois Urbana-Champaign
published: 2023-07-12
ingested: 2026-08-03
venue: CoRL 2023
format: conference paper (23 pp with appendices)
local_path: raw/2307.05973.pdf
sha256: cf1cadcf7a1ee44979908c07698f87755c9b5340a79420db509a92d6d2533d42
license: arXiv preprint (v2, 2023-11-02)
tags: [voxposer, code-as-policy, value-maps, motion-planning, model-based-planning, zero-shot, manipulation, primary-source]
---

## Summary

**VoxPoser** attacks the ceiling [Code as Policies](code-as-policies-paper.md) named in its own limitations — reliance on pre-defined motion primitives, "often considered a major bottleneck of the system due to the lack of large-scale robotic data." Instead of having the LLM *parameterize primitives*, VoxPoser has it **write code that composes 3D voxel value maps** — assigning reward at the drawer handle and cost around the vase — which a model-based motion planner then optimizes into a dense 6-DoF trajectory.

The model still writes code. What changes is the **output type**: from a call sequence to an *objective function in observation space*. This buys dense trajectory synthesis without any primitive for the specific motion, plus closed-loop robustness through fast replanning.

## Key claims

### Real-world tasks, and robustness to disturbance

**5 representative tasks, 10 trials each** (n=50 per condition). Baseline is a variant of Code as Policies using pre-defined primitives:

| | CaP-style primitives | | **VoxPoser** | |
|---|---:|---:|---:|---:|
| | no disturb. | **w/ disturb.** | no disturb. | **w/ disturb.** |
| Move & Avoid | 0/10 | 0/10 | 9/10 | 8/10 |
| Set Up Table | 7/10 | 0/10 | 9/10 | 7/10 |
| Close Drawer | 0/10 | 0/10 | 10/10 | 7/10 |
| Open Bottle | 5/10 | 0/10 | 7/10 | 5/10 |
| Sweep Trash | 0/10 | 0/10 | 9/10 | 8/10 |
| **Total** | **24.0%** | **0.0%** | **88.0%** | **70.0%** |

**The primitives baseline goes to 0.0% under disturbance on every task.** Value-map composition plus replanning holds at 70%.

### Simulated generalization — 13 tasks, 2,766 unique instructions, 20 episodes/task

| Train/Test | Category | U-Net costmap | LLM + Primitives (CaP) | **VoxPoser** |
|---|---|---:|---:|---:|
| SI SA | Object Interaction | 21.0% | 41.0% | **64.0%** |
| SI SA | Spatial Composition | 53.8% | 43.8% | **77.5%** |
| SI UA | Object Interaction | 3.0% | 46.0% | **60.0%** |
| SI UA | Spatial Composition | 3.8% | 25.0% | **58.8%** |
| UI UA | Object Interaction | 0.0% | 17.5% | **65.0%** |
| UI UA | Spatial Composition | 0.0% | 25.0% | **76.7%** |

VoxPoser beats the Code-as-Policies-style baseline in **all six cells**, and — unlike both baselines — its performance is roughly *flat* across seen and unseen conditions.

### Efficient dynamics learning from online experience

Zero-shot VoxPoser trajectories used as **exploration priors** for learning an MLP dynamics model on contact-rich articulated tasks (3 seeds):

| Task | Zero-shot | No prior | **With prior** |
|---|---:|---:|---:|
| Door | 6.7% | 58.3% (**time limit exceeded**, >12 h) | **88.3%** (142 s) |
| Window | 3.3% | 36.7% (TLE) | **80.0%** (137 s) |
| Fridge | 18.3% | 70.0% (TLE) | **91.7%** (71 s) |

"Less than 3 minutes of online interactions" with priors, versus exceeding a **12-hour** limit without. The zero-shot trajectories are "meaningful but insufficient" — useful precisely as exploration seeds.

### Error attribution
An explicit component breakdown (Fig. 4) finds VoxPoser achieves the **lowest specification error** — the error of translating language into a control objective — with most remaining real-world failure coming from **perception**, chiefly a detector "sensitive to initial poses of objects and less robust when detecting object parts."

## Entities mentioned
- [Wenlong Huang](../entities/wenlong-huang.md) (first author; also on [Code as Policies](code-as-policies-paper.md) and [Inner Monologue](inner-monologue-paper.md)) · [Fei-Fei Li](../entities/fei-fei-li.md) (senior; also on [CaP-X](cap-x-paper.md))
- [VoxPoser](../entities/voxposer.md) · Stanford / UIUC

## Concepts touched
- [Code as policy](../concepts/agents/code-as-policy.md) — the "model writes intermediate structure" branch.
- [Motion planning](../concepts/robotics/motion-planning.md) · [Optimal control](../concepts/robotics/optimal-control.md) — value maps become planner objectives.
- [Control abstraction levels](../concepts/robotics/control-abstraction-levels.md) — a *different* answer to the abstraction question than CaP-X's: change the output type rather than lower the primitive level.

## Open questions
The paper's stated limitations, several of which recur through 2026:
- **Relies on external perception modules** — limiting for holistic visual reasoning or fine-grained geometry; also the dominant real-world error source.
- **A general-purpose dynamics model is still required** for contact-rich tasks at the same generality.
- **End-effector-only planning**; whole-arm planning "likely a better design choice."
- **Manual prompt engineering is required.**

Wiki additions:
- **The disturbance protocol is the paper's own design**, not a standard suite — so "0.0% under disturbance" for the CaP baseline is a result about VoxPoser's chosen perturbations. It is directionally consistent with [Inner Monologue](inner-monologue-paper.md)'s independent finding that open-loop methods collapse under disturbance.
- n=10 per real task means individual rows (e.g. Open Bottle 7/10 vs 5/10) do not separate; the 24% vs 88% aggregate does.

## Related sources
- [Code as Policies](code-as-policies-paper.md) — the baseline, and the limitation this paper targets.
- [Language to Rewards](language-to-rewards-paper.md) — the sibling "write an objective, not a call sequence" paper, published a month earlier, same conference.
- [CaP-X](cap-x-paper.md) — the 2026 framework that turns the primitive-abstraction question into a controlled axis instead of routing around it.
