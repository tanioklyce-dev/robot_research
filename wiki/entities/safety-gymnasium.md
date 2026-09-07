---
title: Safety-Gymnasium (and SafePO)
type: entity
subtype: benchmark
created: 2026-09-07
updated: 2026-09-07
sources: 2
tags: [safety-gymnasium, safepo, safe-rl, cmdp, benchmark, mujoco, isaac-gym, gymnasium, pku-alignment, omnisafe]
---

# Safety-Gymnasium (and SafePO)

**The standard safe-RL benchmark** — an environment suite of safety-constrained continuous-control tasks built on [Gymnasium](gymnasium.md) and [MuJoCo](mujoco.md), plus **SafePO**, a companion library of **16** safe-RL algorithms. From [PKU-Alignment](pku-alignment.md); [NeurIPS 2023](../sources/safety-gymnasium-paper.md). A rebuild and extension of **OpenAI's Safety Gym**, which it credits explicitly.

`pip install safety-gymnasium`; ~100 lines to define a custom environment; docs at safety-gymnasium.com.

## What is in it

| Tier | Contents |
|---|---|
| **Gymnasium-based** | Agents `Point`, `Car`, `Doggo` (from Safety Gym) + `racecar`, `ant`. Tasks `Velocity`, `Run`, `Circle`, `Goal`, `Push`, `Button`. **40 navigation + 6 velocity** single-agent tasks. |
| **Multi-agent** | A single MuJoCo body decomposed so agents control separate segments — `2x4AntVel`, `6x1HalfCheetahVel`, `9\|8HumanoidVel`. **8 velocity tasks.** Formalized as a **Constrained Markov Game**. |
| **Vision-only** | RGB and RGB-D observation, rendered natively in MuJoCo (~2× faster on CPU than Safety Gym's `mujoco-py`/OpenGL path). |
| **Isaac-Gym** | **Safety-DexterousHands** — two hands throw and catch a ball; GPU-parallel sampling. |

**54 environments** total in the paper's own analysis.

## The constraints — all kinematic

| Constraint | Cost when |
|---|---|
| **Velocity** | `[v > v_limit]`, `v = √(vx²+vy²)` or `\|vx\|` |
| **Pillars** | contact with a cylindrical obstacle |
| **Hazards** | agent enters a risk region |
| **Sigwalls** | crossing out of the Circle task's safe area |
| **Vases** | touching or displacing a **static fragile object** |
| **Gremlins** | interaction with a moving object |
| **Safety Joint / Safety Finger** | a hand joint leaves a narrowed angle range (±10° instead of ±20°, etc.) |

> [!warning] No force, anywhere
> Speed thresholds, region entry, contact events, joint limits. **No wrench, no contact force, no pressure** — in a physics engine that computes all of them. `Vases`, *"static and fragile objects"*, is the nearest the suite comes to *how hard you hit it mattering*, and it is scored as a touch/displacement event.
>
> This is why the [contact-rich survey](../sources/safe-learning-contact-rich-survey.md) can name only three safety-specific RL benchmarks and still say **no standardized contact-force evaluation protocol exists**. It is also why nothing in the suite is [contact-rich](../concepts/robotics/contact-rich-manipulation.md): navigate, push a box, press a button, throw and catch, move fast — and catching is explicitly excluded as momentary contact.

## SafePO

16 algorithms, **one file each**, deliberately decoupled: Lagrangian-based (PPO-Lag, TRPO-Lag, **CPPO-PID**, RCPO, MAPPO-Lag), projection-based (**CPO**, PCPO, MACPO), plus FOCOPS and CUP; single- and multi-agent, first- and second-order. TensorBoard/WandB logging of 40+ quantities including the **Lagrange multiplier itself** and CPO's internal terms.

Its correctness protocol is worth copying: implement strictly from the paper, **diff line-by-line** against the acknowledged reference implementation, then **benchmark against it** — and the resulting table shows that **implementations of the same published algorithm disagree materially** (CPO on `CarButton1`: 1.75 normalized cost in SafePO, **3.65** in OpenAI's Safety-Starter-Agents).

## What the benchmark says about safe RL

- **Unconstrained RL runs 20–40× over the cost limit** (PPO: `HumanoidVel` 38.42, `DoggoCircle1` 33.14), and the fix is cheap: PPO-Lag cuts cost **98%** for a **45%** reward loss on velocity tasks.
- **Lagrangian methods oscillate** around the constraint — more time both Strongly Unsafe and Strongly Safe — where projection methods stay centered but get conservative. **A PID controller on the multiplier (CPPO-PID) fixes the oscillation at no reward cost.**
- **The velocity suite does not discriminate.** Every safe-RL algorithm meets the limit there, with *"negligible"* reward differences and tightly clustered optima; only the noisier navigation tasks separate methods. Half the benchmark reports a tie — a [saturation](../concepts/robotics/robot-policy-evaluation.md) result the authors state and don't name.

## Lineage

**OpenAI Safety Gym → Safety-Gymnasium (2023) → [Safety-CHORES](safety-chores.md) (2025)**, all sharing the CMDP framing and the co-reported reward/cost metric. The suite's own stated future work — *"transferring policy refined within the Safety-Gymnasium to physical robotic platforms"* — is what [SafeVLA](../sources/safevla-paper.md) attempts, and it is **still simulation-only**. The constraint vocabulary tracks the move: speed and regions here, collisions and fragile-object displacement there, **forces in neither**.

## Related

- [PKU-Alignment](pku-alignment.md) — the group; **OmniSafe** is their companion safe-RL infrastructure, cited but not ingested here.
- [Safety-CHORES](safety-chores.md) — the embodied successor.
- [Safe reinforcement learning](../concepts/learning/safe-reinforcement-learning.md) — the paradigm this measures.
- [Gymnasium](gymnasium.md) · [MuJoCo](mujoco.md) · [Isaac Gym](isaac-gym.md) — the substrate.

## Mentioned in

- [Safety-Gymnasium paper](../sources/safety-gymnasium-paper.md) — NeurIPS 2023; the source for this page.
