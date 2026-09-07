---
title: "Safety-Gymnasium: A Unified Safe Reinforcement Learning Benchmark (Ji et al., NeurIPS 2023)"
type: source
url: https://arxiv.org/abs/2310.12567
fetch_url: https://arxiv.org/pdf/2310.12567v3
local_path: raw/2310.12567v3.pdf
sha256: bf370401d5e3f358659f5ec15932715d00518737c48e668c44cb9a21bf3e0297
author: "Jiaming Ji, Borong Zhang, Jiayi Zhou (equal contribution), Xuehai Pan, Weidong Huang, Ruiyang Sun, Yiran Geng, Yifan Zhong, Juntao Dai, Yaodong Yang (Institute for AI, Peking University; BIGAI)"
published: 2023-10-19
venue: "NeurIPS 2023 (Datasets and Benchmarks). arXiv v1 2023-10-19 → v2 2023-11-07 → **v3 2024-10-06**, the version read here. 30 pp."
format: benchmark / software paper (PDF + arXiv HTML)
tags: [safety-gymnasium, safepo, safe-rl, cmdp, benchmark, mujoco, isaac-gym, lagrangian, cpo, pid-lagrangian, multi-agent, pku, omnisafe]
ingested: 2026-09-07
---

## Summary

**The benchmark the safe-RL literature reports against, and the reason the wiki could not previously say what "safe RL was evaluated" means.** Two artifacts: **Safety-Gymnasium**, an environment suite of safety-constrained continuous-control tasks (single-agent, multi-agent, vision-only, and an Isaac-Gym dexterous-hands tier), and **SafePO**, a single-file-per-algorithm library of **16** safe-RL algorithms. The paper's own contribution beyond the software is an analysis of **16 algorithms across 54 environments**.

It is a **rebuild of OpenAI's Safety Gym**, and unusually candid about that — a footnote goes out of its way to say *"we have no intention of attacking Safety Gym; the contribution of Safety Gym to the SafeRL community cannot be ignored, and Safety Gym also inspired this work."* The improvements are mostly engineering (native MuJoCo instead of the abandoned `mujoco-py`, `pip install safety-gymnasium`, ~2× faster CPU rendering, ~100 lines to define a custom environment) plus scope (more agents, more tasks, multi-agent, vision, GPU-parallel).

Ingested to answer three questions the wiki had been carrying on trust: **what its costs actually measure, whether any of it is force-based, and whether it saturates.** All three are answered below, and one of them creates a tension with [SafeVLA](safevla-paper.md) from the same group.

## What the environments are

**Agents** — `Point`, `Car`, `Doggo` (inherited from Safety Gym, with oscillation bugs fixed), plus `racecar` and `ant`. Multi-agent variants are built by decomposing a single MuJoCo body so separate agents control distinct segments (`2x4AntVel`, `9|8HumanoidVel`, …).

**Tasks** — `Velocity` (move forward), `Run`, `Circle` (stay on a green circle, out of a red region), `Goal` (navigate to successive goals), `Push` (push a box to goals), `Button` (touch the currently-highlighted button).

**Constraints — and this is the part that matters for this wiki:**

| Constraint | Cost incurred when |
|---|---|
| **Velocity** | speed exceeds a limit: `cost = [v(s,a) > v_limit]`, with `v = √(vx²+vy²)` in the plane or `|vx|` on a line |
| **Pillars** | contact with a large cylindrical obstacle |
| **Hazards** | the agent **enters a risk region** |
| **Sigwalls** | crossing out of the Circle task's safe area |
| **Vases** | touching or displacing a **static fragile object** |
| **Gremlins** | interaction with **moving** objects (Button tasks) |

The Isaac-Gym tier, **Safety-DexterousHands**, is different in kind and worth noting: two hands throw and catch a ball, and the *safety constraint is on the robot's own joints* — `Safety Joint` narrows the forefinger's joint ④ from ±20° to ±10°; `Safety Finger` additionally restricts joints ② and ③ from [0°, 90°] to [22.5°, 67.5°]. Cost is an indicator on being outside the permitted range.

> [!warning] Nothing here is force-based, and that is the whole answer to the backlog question
> Costs are **speed thresholds, region entry, contact events, and joint-angle limits**. There is no wrench, no contact force, no pressure, no impedance, no compliance — in a MuJoCo suite where all of those are computable. `Vases` — *"static and fragile objects"* — is the closest the suite comes to the idea that **how hard you hit something matters**, and it is scored as a touch/displacement event.
>
> So the [contact-rich survey](safe-learning-contact-rich-survey.md)'s complaint stands with a sharper edge than it stated: the field's standard safe-RL benchmark is **kinematic**, its embodied successor [Safety-CHORES](../entities/safety-chores.md) is **collision-based**, and the gap is not that nobody has built a contact-force protocol — it is that **the entire evaluation lineage was built without one**, twice, by people with a physics engine that reports contact forces.

## What the results show

Setup: `cost_limit = 25.00`, rewards normalized to PPO's performance (J̄ᴿ) and costs normalized to the cost limit (J̄ᶜ, so >1.00 is a violation).

**Unconstrained RL is not slightly unsafe — it is 20–40× over the limit.** PPO's normalized costs: `DoggoCircle1` **33.14**, `AntVel` **38.33**, `HumanoidVel` **38.42**, `HalfCheetahVel` **36.77**, `Walker2dVel` **36.11**, `CarButton1` **16.09**. Multi-agent is the same: MAPPO runs **22–39×** the limit across every velocity task.

**And the trade is cheap.** On velocity tasks, PPO-Lag against PPO: **98% cost reduction for a 45% reward decrease.** That single ratio is the strongest one-line case for constrained optimization in this wiki.

**HAPPO buys reward with cost.** It beats MAPPO on reward across all 8 velocity tasks *"accompanied by a simultaneous increase in average costs"* — an unconstrained method improving by taking more risk, which is invisible if you report reward alone.

**Three findings about the algorithm families:**

- **Lagrangian oscillates; projection does not.** Both CPO and PPO-Lag oscillate around the constraint during training, *"however, those exhibited by PPO-Lag are more conspicuous"* — a higher proportion of time in both **Strongly Unsafe** *and* **Strongly Safe** bands, while CPO stays centered. The projection-based **PCPO** gets lower average cost *and* lower reward — *"an excessively cautious policy has the potential to undermine performance."*
- **A PID controller on the multiplier fixes the oscillation.** **CPPO-PID** tracks PPO-Lag's rewards while entering the Strongly Unsafe region less often. This is the cleanest result in the paper.
- **Task stochasticity drives the spread.** On velocity tasks *every* safe-RL algorithm meets the limit, reward differences are *"negligible,"* and optimal policies are *"tightly clustered."* On the 20 navigation tasks, high stochasticity produces *"pronounced oscillations"* and visibly different rankings.

> [!note] That last finding is a saturation result, stated as an observation
> **The velocity suite does not discriminate between safe-RL algorithms.** Everything passes, at indistinguishable reward. Only the navigation tasks separate methods — and they separate them partly *because they are noisy*, which is a different property from being harder.
>
> This is the [robot policy evaluation](../concepts/robotics/robot-policy-evaluation.md) failure mode arriving in the safe-RL literature, unnamed: half of the standard benchmark reports a tie, and a paper quoting velocity-task numbers as evidence of an algorithmic advance is quoting the half that measures nothing. The authors report it plainly and do not draw the conclusion.

## The critique of Safety Gym that the same group later ignored

Appendix B.6 lists concrete defects in OpenAI's Safety Gym: a **Natural Lidar bug** that cannot detect low-lying objects; an observation space declared as `Box(-inf, +inf)` regardless of actual bounds; dependency rot (`mujoco-py`, `numpy==1.17.4`). Useful engineering criticism.

The fourth is conceptual, and it is the one worth carrying:

> **Missing cost information.** In Safety Gym, by default, there are only two possible outputs for the cost: 0 and 1… We believe that this representation method loses some information. For example, when the robot collides with a vase and causes the vase to move at different velocities, **there should be different cost values associated with it to indicate subtle differences in violating constraint behaviors.** … If the total cost generated by different obstacles is limited to only two states 0 and 1, **the learning potential for multiple constraints is lost** when multiple costs are triggered simultaneously.

That is an argument for **graded, severity-weighted costs**, made in 2023, with a worked example (how fast the vase moves) that is unmistakably about *how hard the contact was*.

> [!warning] The same group shipped binary unweighted costs two years later, and defended the choice
> [SafeVLA](safevla-paper.md) (Ji is an author of both) states: *"This analysis utilizes binary cost signals for clarity and interpretability. While severity-weighted costs are crucial for real-world deployment, we chose a binary scheme in this work to establish a clear and generalizable baseline, as the notion of severity is often highly context-dependent."*
>
> Both positions are defensible and they are in tension: **binarizing loses the information that distinguishes a nudge from a smash** (2023), and **severity is too context-dependent to fix in a benchmark** (2025). Nobody has measured which matters more, and this is now a concrete experiment: rerun a SafeVLA-style alignment with graded costs and see whether the safety behavior changes qualitatively or only in units.
>
> A qualifier in fairness to both: **Safety-Gymnasium's own documented costs are also indicator functions** — the velocity cost is literally `[v > v_limit]`, and the dexterous-hand costs are `𝕀(angle ∉ range)`. The B.6 critique is aimed at Safety Gym's *global* `constrain_indicator` flag that flattens all per-constraint costs into one bit, and this paper does not demonstrate a graded alternative in its own task definitions.

## SafePO, and why "correctness" is a stated feature

**16 algorithms**, one file each: single-agent and multi-agent, first- and second-order, **Lagrangian-based** (PPO-Lag, TRPO-Lag, CPPO-PID, RCPO, MAPPO-Lag) and **projection-based** (CPO, PCPO, MACPO), plus FOCOPS and CUP.

The correctness argument is three-step and worth copying: implement strictly from the paper (matching the gradient flow); **diff line-by-line against the acknowledged open-source implementation** where one exists; and then **benchmark against those implementations** — Table 1 compares SafePO against **Safety-Starter-Agents** (OpenAI) and **RL-Safety-Algorithms** on the same tasks under the same cost limit.

That table is the paper's least-discussed and most useful artifact: **implementations of the same published algorithm disagree**. `CarButton1` under CPO: SafePO 0.08 reward / 1.75 cost, Safety-Starter-Agents 0.34 / **3.65**, RL-Safety-Algorithms −0.06 / 3.30. Same algorithm, same task, same limit — one implementation violates the constraint twice as badly as another. Any safe-RL comparison that cites a number without its implementation is under-specified.

## Key claims

- SafeRL is framed from the start as spanning **robotics and language models**: the introduction cites work reducing LLM toxicity through SafeRL alongside autonomous vehicles and healthcare. This is a group that treats [alignment](../concepts/safety/ai-safety-alignment.md) and control as one problem, which is the through-line to [SafeVLA](safevla-paper.md) and Safe-RLHF.
- The suite is **CMDP-native** (and Constrained Markov Game for the multi-agent case), so every task ships with reward, cost, and a limit rather than a blended objective.
- **Vision-only** tasks accept RGB and RGB-D, motivated by real-world applicability — the visual tier is the intended bridge to embodied work.
- **Related environments** it positions against: OpenAI **Safety Gym**, DeepMind **AI-Safety-Gridworlds**, **safe-control-gym**, **MetaDrive**. The wiki's Table-3 list from the [contact-rich survey](safe-learning-contact-rich-survey.md) is essentially this list, two years later.
- **OmniSafe** (Ji et al., ref [8]) is the group's companion safe-RL infrastructure — cited here, not ingested.

## Limitations, in their own words

The limitations section is short and honest, and it names the exact gap the group's later work walks into:

> A limitation of this study is its inability to encompass all forms of constraints. For instance, **safety constraints related to human-centric considerations are paramount in human-AI collaboration, yet these considerations have not been fully integrated.** … This work focuses on safety tasks within a simulated environment… the transferability of the results to complex real-world safety-critical applications may be limited. **A promising work for the future involves transferring policy refined within the Safety-Gymnasium to physical robotic platforms.**

Two years on, [SafeVLA](safevla-paper.md) is that follow-up — and it is **still simulation-only**, with the same limitation restated. The human-centric constraint gap is also still open, and it is precisely the axis the [contact-rich survey](safe-learning-contact-rich-survey.md) calls *human-centered and standard-driven safety* (contact pressure, speed-and-separation, ergonomics, perceived safety).

## Entities mentioned

- [Safety-Gymnasium](../entities/safety-gymnasium.md) — **new page**: the suite and SafePO.
- [PKU-Alignment](../entities/pku-alignment.md) — the group; this is the artifact the [SafeVLA](safevla-paper.md) line is built on.
- [MuJoCo](../entities/mujoco.md) · [Isaac Gym](../entities/isaac-gym.md) · [Gymnasium](../entities/gymnasium.md) — the substrate.
- [Safety-CHORES](../entities/safety-chores.md) — the embodied successor from the same group.

## Concepts touched

- [Safe reinforcement learning](../concepts/learning/safe-reinforcement-learning.md) — **the benchmark and algorithm taxonomy this page supplies**: Lagrangian vs projection vs PID-Lagrangian, and what each costs.
- [Robot policy evaluation](../concepts/robotics/robot-policy-evaluation.md) — the saturation result, and the implementation-variance table.
- [Contact-rich manipulation](../concepts/robotics/contact-rich-manipulation.md) — what a kinematic cost function cannot express.
- [Multi-agent RL](../concepts/learning/multi-agent-rl.md) — the Constrained Markov Game half.

## Open questions

- **Does severity weighting change safety behavior, or only its units?** The 2023 critique and the 2025 defence are both from this group and nobody has run the comparison. The cheapest version: rerun a Safety-Gymnasium task with graded vase-displacement costs against the indicator version and compare the *shape* of the learned avoidance, not the cost number.
- **Why did PID-Lagrangian stay in the appendix?** This paper finds CPPO-PID fixes Lagrangian oscillation at no reward cost. [SafeVLA](safevla-paper.md) tests PID-Lagrangian in App. B.7 (Safety-ObjectNav: 0.859 SR / **1.64** cost, against the headline configuration's 0.865 / 1.854 — *lower cost*, same success) and reports only that it *"can be integrated."* Given this paper's finding, the appendix result deserved the main table.
- **Would a force-based constraint even be hard here?** MuJoCo reports contact forces. `Vases` already models fragility. A `cost = [F_contact > F_limit]` task looks like a small addition to a suite that has none — which raises the question of why two generations of this benchmark line have not added one.
- **Nothing in this suite is contact-rich.** Navigate, push a box, press a button, throw and catch a ball, move fast without exceeding a speed. By [the survey's definition](../concepts/robotics/contact-rich-manipulation.md) the *only* candidate is the dexterous-hands catch, and catching is explicitly excluded as momentary contact.
