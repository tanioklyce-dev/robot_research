---
title: "Code as Policies: Language Model Programs for Embodied Control"
type: source
url: https://arxiv.org/abs/2209.07753
author: "Jacky Liang, Wenlong Huang, Fei Xia, Peng Xu, Karol Hausman, Brian Ichter, Pete Florence, Andy Zeng"
affiliation: Robotics at Google
published: 2022-09-16
ingested: 2026-08-03
venue: ICRA 2023
format: conference paper (16 pp with appendices)
local_path: raw/2209.07753.pdf
license: arXiv preprint (v4, 2023-05-25)
tags: [code-as-policy, llm-agent, program-synthesis, robot-manipulation, generalization, humaneval, robocodegen, seminal, primary-source]
---

## Summary

**The seminal code-as-policy paper.** Liang et al. show that code-completion LLMs can be re-purposed to write **robot policy code** from natural-language commands given few-shot examples: policies that process perception outputs, parameterize control primitives, use classic control flow (if/else, for/while), and call third-party libraries (NumPy, Shapely) for spatial-geometric reasoning. They call the artifact a **language model program (LMP)**.

The paper's framing move is to identify what the *plan-a-sequence-of-skills* approaches ([SayCan](saycan-paper.md), [Inner Monologue](inner-monologue-paper.md)) cannot express. Their worked contrast, for "move the coke can a bit to the right":

> An LLM planner emits `1. Pick up coke can / 2. Move a bit right / 3. Place coke can` — which **assumes a skill exists** for "move a bit right." Code as Policies instead writes the servo loop and the offset arithmetic directly, "avoid[ing] the requirement of having predefined policies to map every step in the plan."

That is the origin of the wiki's [code-as-policy](../concepts/agents/code-as-policy.md) definition: the action vocabulary becomes arbitrary code rather than a fixed menu.

## Key claims

### The core capability set
Code-writing LLMs, few-shot prompted, can produce policies that:
- **Express feedback loops grounded in language** — `while not detect_object("apple"): robot.set_velocity(...)`.
- **Prescribe precise values to ambiguous descriptions** ("faster", "to the left") from context — what the paper calls **behavioral commonsense**.
- **Reason spatially-geometrically** by leaning on familiarity with third-party libraries, with no additional training.
- **Engage in dialogue** simply by exposing `say(text)` as a primitive.

### Hierarchical code generation
The paper's methodological contribution: prompt the LLM to **recursively define undefined functions**, letting it "accumulate their own libraries over time, and self-architect a dynamic codebase." This is the direct ancestor of every skill library in the later lineage ([Voyager](voyager-paper.md), [ASPIRE](aspire-paper.md)).

| Benchmark | Flat | Hierarchical |
|---|---|---|
| **RoboCodeGen** (new, 37 robotics function-gen problems), Codex davinci | 81% | **95%** |
| RoboCodeGen, GPT-3 175B | 68% | **84%** |
| **HumanEval** P@1 | 34.9 | **39.8** (SOTA at the time) |
| HumanEval greedy | 45.7 | **53.0** |

- **Scaling laws hold** — within each model family, larger models write better robot code (GPT-3 6.7B scores 3–5%; 175B scores 68–84%).
- Hierarchical gains appear only in the two `davinci` models, not `cushman` — "a certain level of code-generation capability needs to be reached first."

### Simulated tabletop evaluation — the generalization result

Success rates, **50 trials per task**, against CLIPort trained via imitation on **30k demonstrations** and a natural-language (non-code) LLM planner. SI/UI = seen/unseen instructions, SA/UA = seen/unseen attributes:

| Train/Test | Task family | CLIPort | NL Planner | **CaP** |
|---|---|---:|---:|---:|
| SA SI | Long-Horizon | 78.80 | 86.40 | **97.20** |
| SA SI | Spatial-Geometric | **97.33** | N/A | 89.30 |
| UA SI | Long-Horizon | 36.80 | 88.00 | **97.60** |
| UA SI | Spatial-Geometric | 0.00 | N/A | **73.33** |
| UA UI | Long-Horizon | 0.00 | 64.00 | **80.00** |
| UA UI | Spatial-Geometric | 0.01 | N/A | **62.00** |

> [!note] This 2022 table has the same shape as the 2026 LIBERO-PRO result
> **The imitation-learned policy collapses to 0.00 under unseen attributes and instructions while the code-writing agent holds at 62–80%.** Four years later, [CaP-X](cap-x-paper.md) and [ASPIRE](aspire-paper.md) reproduce exactly this shape with modern VLAs on [LIBERO-PRO](libero-pro-paper.md) — [OpenVLA](../entities/openvla.md) and [π0](../entities/pi-zero.md) at 0.00, code agents degrading gracefully.
>
> The finding is not new in 2026. What is new in 2026 is that the collapsing policies are *foundation models trained on internet-scale robot data*, not a 30k-demo CLIPort — which makes the same failure much more surprising. See [code as policy](../concepts/agents/code-as-policy.md).

Note also the one row CaP **loses**: seen-attribute spatial-geometric tasks, where CLIPort's 97.33 beats CaP's 89.30. In-distribution, the trained policy is better. The advantage is entirely a generalization advantage — which is also the 2026 story.

### Demonstrated domains
Four, three on real hardware: 2D shape drawing (UR5e, MDETR perception), tabletop pick-and-place (UR5e + suction + in-hand RealSense D435), simulated tabletop (Ravens-based, 8 inherited + 6 new tasks), and **mobile manipulation in a real kitchen** ([Everyday Robots](../entities/everyday-robots.md) mobile manipulator, ViLD perception).

## Entities mentioned
- [Robotics at Google](../entities/google-deepmind.md) · [Brian Ichter](../entities/brian-ichter.md) · [Andy Zeng](../entities/andy-zeng.md) · [Fei Xia](../entities/fei-xia.md) · [Karol Hausman](../entities/karol-hausman.md) · [Wenlong Huang](../entities/wenlong-huang.md)
- [Everyday Robots](../entities/everyday-robots.md) · [CLIPort](../entities/cliport.md) — the imitation baseline that collapses

## Concepts touched
- [Code as policy](../concepts/agents/code-as-policy.md) — this is the origin paper.
- [LLM-agent architecture](../concepts/agents/llm-agent-architecture.md) · [Control abstraction levels](../concepts/robotics/control-abstraction-levels.md)
- [Imitation learning](../concepts/learning/imitation-learning.md) — CLIPort as the contrast class.

## Open questions

> [!warning] The paper names the limitation that its successors spent four years quantifying
> CaP's own Discussion states it is "restricted by the scope of (i) what the perception APIs can describe … and (ii) **which control primitives are available**. Only a handful of named primitive parameters can be adjusted without over-saturating the prompts." And: LMPs "struggle to interpret commands that are significantly longer or more complex, **or operate at a different abstraction level than the given Examples**."
>
> This matters for how the wiki frames [CaP-X](cap-x-paper.md)'s critique. CaP-X's finding — that performance depends heavily on human-designed API scaffolding — is **not a refutation of an unaware paper**. The original authors flagged the primitive-scope ceiling explicitly. CaP-X's contribution is turning a stated caveat into a *controlled, measured axis*. [VoxPoser](voxposer-paper.md) and [Language to Rewards](language-to-rewards-paper.md) both attacked the same ceiling in 2023 by changing what the model writes.

- **Most of the paper is unquantified.** The authors say so: "quantitative evaluations of a robot system using CaP is limited to a constrained set of simulated tasks," with the three real-robot domains demonstrated "without quantitative evaluations." The famous kitchen and drawing results are **demos**.
- **RoboCodeGen has 37 problems** — small enough that the 81% → 95% hierarchical gain is roughly 5 problems.
- Assumes all instructions are feasible; "we cannot tell if a response will be correct a priori" — no self-verification, which [Voyager](voyager-paper.md) adds a year later.

## Related sources
- [CaP-X](cap-x-paper.md) — the 2026 framework named after this paper; quantifies its stated primitive-scope limitation.
- [VoxPoser](voxposer-paper.md) / [Language to Rewards](language-to-rewards-paper.md) — both benchmark *against* CaP and beat it by changing the output representation.
- [SayCan](saycan-paper.md) / [Inner Monologue](inner-monologue-paper.md) — the skill-selection alternative this paper defines itself against.
- [Voyager](voyager-paper.md) — takes hierarchical code-gen to a persistent, self-verifying skill library.
