---
title: "Human-in-the-loop transfer learning in collision avoidance of autonomous robots (Oriyama, Hartono & Sawada, 2025)"
type: source
url: https://doi.org/10.1016/j.birob.2025.100215
local_path: raw/human-in-the-loop-transfer-learning.pdf
sha256: 4960e8fa649c8cde74a8a2205942fee7b3f38c426a48bcf6ad0b47eeda1e7aca
author: "Minako Oriyama (Waseda), Pitoyo Hartono (Chukyo), Hideyuki Sawada (Waseda)"
published: 2025-01-28
venue: "Biomimetic Intelligence and Robotics 5 (2025) 100215 — Elsevier on behalf of Shandong University. Received 2024-11-19, accepted 2025-01-17. Open access, CC BY. 14 pp."
license: CC BY 4.0
format: peer-reviewed research article (PDF)
tags: [human-in-the-loop, transfer-learning, collision-avoidance, reinforcement-learning, weight-initialization, prior-knowledge, ultrasonic-sensors, small-networks, interpretability, waseda]
ingested: 2026-09-07
---

## Summary

**Seed a small neural network with a hand-written human rule, then let it learn online — and measure what that seeding is worth.** A 4→30→4 fully-connected network is pre-trained by supervised learning on sensor data labelled by a fixed "human common sense" algorithm; its weights initialize a 12→4 network that then does real-time reinforcement learning on a 262 g tracked robot with four ultrasonic sensors. Seven experiments (A–G) compare with and against pre-training across matched environments, a dynamic environment, sensor faults, motor faults, and continuous speed control.

The headline is the one you'd expect — pre-training helps — but **the interesting result is where it doesn't**, and the paper reports those cases honestly.

> [!note] Why a 2025 Arduino-robot paper is worth a page in this wiki
> Everything else ingested this week answers the *same question* at the opposite end of the scale axis. [GEN-1.5](generalist-gen-1-5-blog.md): eight months of pretraining over **1,891,392 scenes**, and a new task costs one 3–12 second demonstration. This paper: **100 random actions**, a four-branch `if/else`, and a new behavior costs **50 learning steps**.
>
> **Both are answers to "how do you give a robot a prior so that adaptation is cheap?"** One writes the prior by hand into the initialization; the other grows it from data and delivers it through the context window. The adaptation budgets end up in the same neighbourhood. What differs is where the prior comes from and how far it generalizes — and this paper measures the second part, which the vendor blogs do not.

## What "human common sense" actually is

Worth stating plainly, because the paper's prose is expansive about *"human intuition,"* *"human cognition and artificial intelligence,"* and *"human commonsense knowledge,"* and the artifact is **Algorithm 2**, in full:

> identify the sensor with the minimum value; if **front** → teacher signal **back**; if **back** → **forward**; if **right** → **left**; if **left** → **right**.

Four branches. The robot performs **100 random actions** from the centre of the arena, its four ultrasonic readings are recorded, that rule labels each one, and the network is trained on the result by backprop with MSE.

This is not a criticism of the experiment — it makes it *legible*. What is being transferred is a **reflex**, and the paper's real question becomes precise: **is seeding an online learner with a hand-coded reflex worth anything, and under what conditions?**

## Setup

| | |
|---|---|
| Robot | **Zumo Robot for Arduino**, tracked, 262 g, 87 × 98 × 90 mm |
| Sensing | **4 ultrasonic proximity sensors** (front/rear/right/left), 40 kHz, range 2–400 cm |
| Compute | Arduino ↔ **Bluetooth** ↔ PC; the network runs off-board |
| Actions | forward, backward, left turn, right turn (turns by stopping one motor); PWM speed 200 of ±400 |
| Pre-train net | **4 → 30 (sigmoid) → 4**, MSE, backprop |
| RL net | **12 → 4** — the 12 inputs are the same 4 sensors at **t, t−1, t−2** |
| Transfer | first-layer weights overwrite the **first four columns** of the RL net's input matrix (rest randomly initialized); hidden and output layers copied directly |

**The "RL" is a one-step reactive rule.** The evaluation `U(a(t))` compares the RMS of the two smallest sensor readings before and after an action; positive means the robot moved away from obstacles. On a good action the winning output neuron gets target 1 and the others 0; on a bad action the winner gets 0 and the others 1. The paper says so itself: *"the reinforcement learning problem is reformulated as a supervised learning task"* and *"though its implementation mimics supervised learning."* No value function, no discounting, no Q-table — *"unlike conventional Q-learning… this approach directly maps states to actions."*

That framing is why 50 steps is enough, and also why nothing here has a horizon: credit assignment spans exactly one action.

## The results, including the ones that didn't work

| Exp | Condition | Welch's t-test (no pre-train vs pre-train) |
|---|---|---|
| **A** | pre-training only, offline | — (robot reaches centre and stagnates) |
| **B** | RL only, no prior | — (collides / repeats in place / reverses into wall, from all 3 starts) |
| **C** | **pre-train + RL, matched environment** | t = 3.41 (p ≈ 9.6e-4), t = 11.8 (p ≈ 1.4e-20), t = 28.1 (p ≈ 9.9e-49) |
| **D** | **dynamic environment** (a second robot patrolling) | **t = −0.774, p = 0.441 — not significant** |
| **E** | **faulty sensor** (random ±150 added) | front p = 0.705, rear p = 0.846, right p = 0.053, **left p ≈ 4.0e-10** — *3 of 4 not significant* |
| **F** | faulty motor (one at half speed) | t = 3.82 (p ≈ 2.0e-4), t = 9.29 (p ≈ 3.0e-16) |
| **G** | continuous speed via a scaled sigmoid (k = 0.5) → stop/low/moderate/fast | t = 6.28 (p ≈ 9.2e-9) |

> [!warning] The abstract does not hedge and the results do
> Abstract: *"incorporating human knowledge **significantly improves both learning efficiency and generalization capabilities**."* But the prior is significant in the **matched** environment (C), under motor faults (F) and with continuous control (G), and **not significant** in the **dynamic** environment (D, p = 0.441) or in three of four **sensor-fault** conditions (E).
>
> The body says the right thing — the D failure is explained as *"the prior knowledge provided by humans not being designed for a dynamic environment… the relevance of the prior knowledge was limited, leaving the robot in a state similar to starting from random actions"* — and the conclusion generalizes it: the prior must be *"not merely 'adequate' but also sufficiently comprehensive and tailored to the robot's operating environment and task."*
>
> **So the finding is narrower and more useful than the abstract's**: a hand-specified prior pays exactly to the extent that the deployment environment matches the one the prior was written for, and is worth approximately nothing when it does not.

> [!note] The same shape as three other results in this wiki, from very different places
> *A prior only helps on the distribution it was built for* is this week's recurring finding. [SafeVLA](safevla-paper.md)'s elicitation ablation: an identical constrained-RL recipe in scenes without deliberately-placed hazards is **worse than the baseline it beats** — *a constrained optimizer can only constrain behaviors it observes*. [PACS](pacs-paper.md): a filter that pushes a policy off its training manifold costs it everything. [mimic-video](mimic-video-paper.md): fully denoised latents fall out of the decoder's training distribution and control degrades. Four instances, four scales, one mechanism.

## The mechanistic detail worth keeping

Under a simulated sensor fault (Experiment E), *"the weights from the hidden layer to the output layer for actions leading towards the faulty sensor **approached zero**… the network learned to ignore it."*

A small, inspectable, verifiable adaptation: the network routes around a broken input and you can *see it in the weights*. That is only possible because the network is 4→30→4, which is the paper's stated design argument:

> Models learned through deep reinforcement learning and path planning are typically treated as **black boxes**… The proposed approach suggests that using a **simpler neural network could facilitate the interpretation of the model's internal mechanisms and logic**, aligning with the HITL objective of ensuring accountability in AI decision-making.

**Interpretability by smallness** — a position the wiki's [mechanistic interpretability](../concepts/safety/mechanistic-interpretability.md) material, which is entirely about extracting structure from large models, has no other instance of. It does not scale, and it is not nothing: it is the only source here where a behavioral adaptation is read directly off the weights without an interpretability method in between.

## Where the methodology is weak

- **The t-tests are pseudoreplicated.** The comparison is *"the smallest sensor values recorded by the robot at each time step"* across conditions — 50–70 timesteps drawn from **one trajectory per condition**. Successive timesteps of a single robot run are heavily autocorrelated, so they are not independent samples. The p-values (down to 9.9e-49) are therefore far smaller than the evidence supports; the effective n is closer to *one run* than to *fifty observations*. The **direction** of the C/F/G results is well supported by the trajectory figures; the **magnitude of significance** is not.
- **n = 1 run per cell**, with no seeds and no repeats reported anywhere.
- **"Omnidirectional" is wrong.** §3 opens *"we designed and used an omnidirectional robot"*, and the platform is a **tracked** Zumo with four discrete actions that turns by pivoting on a stopped motor.
- **Six or seven experiments?** The introduction says *"seven experiments"*, §4 says *"six experiments"*, and the paper contains A through G.
- **"Transfer learning" is used idiosyncratically.** They claim *"instead of transferring parts of the neural network structure, we transfer prior knowledge"* — but they do transfer weights (first four input columns, plus hidden and output layers verbatim). It is ordinary weight transfer between two differently-shaped networks.

> [!note] And yet its statistics are better than this week's vendor blogs
> This paper reports **t and p for every comparison, including the four that fail**. [GEN-1.5](generalist-gen-1-5-blog.md) and [S1](skild-s1-blog.md) report success rates with **no trial counts at all**. The pseudoreplication is a real flaw; publishing your null results is a real virtue, and a 262 g Arduino robot managed it where two robot-foundation-model companies did not.

## Entities mentioned

- No entity pages created. The platform is a **Zumo Robot for Arduino** (Pololu) — off-the-shelf hobby hardware, not otherwise in this wiki. **Pitoyo Hartono** (Chukyo) is also an author on ref [3], *"Human-in-the-loop: infusing knowledge into neural networks"* (ICMA 2024), which is the direct predecessor of this framing.

## Concepts touched

- [Real-world robotic RL](../concepts/learning/real-world-robot-rl.md) — the same problem statement (data is expensive on hardware), attacked with a prior instead of with off-policy machinery; the low-budget counterpart to [HIL-SERL](hil-serl-paper.md).
- [In-context robot learning](../concepts/learning/in-context-robot-learning.md) — the contrast: a prior delivered through **initialization** rather than through **context**.
- [End-user robot programming](../concepts/robotics/end-user-robot-programming.md) — a non-expert specifying behavior, here by writing a four-branch rule.
- [Mechanistic interpretability](../concepts/safety/mechanistic-interpretability.md) — interpretability by smallness, and a weight-level reading of an adaptation.
- [Imitation learning](../concepts/learning/imitation-learning.md) — the pre-training stage is supervised learning from algorithmically generated labels, not human demonstrations.

## Open questions

- **Would the prior have helped in the dynamic case if it had been written for one?** Experiment D fails because the rule is static. Writing a second four-branch rule that accounts for a moving obstacle is an afternoon's work, and the paper does not try it — which would convert "the prior must match the environment" from an explanation of a null result into a tested claim.
- **How much of the benefit is the prior, and how much is just not being randomly initialized?** There is no control against a *wrong* or *arbitrary* pre-training signal. If seeding with a deliberately bad rule also beat random init, the result would be about initialization conditioning rather than about human knowledge.
- **What is the smallest prior that works?** Four branches is already close to minimal, and it recovers most of the gap in the matched environment. That is a data point on the question the foundation-model line answers with 1.89M scenes, and the interpolation between them is unexplored.
- **Does the ignore-the-broken-sensor result survive at scale?** Weights going to zero for a faulty input is exactly the behavior you would want from a large policy and could not observe in one. Whether the same adaptation happens inside a VLA — and whether anyone could tell — is the general form of this paper's interpretability argument.
