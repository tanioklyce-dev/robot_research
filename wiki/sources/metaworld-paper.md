---
title: Meta-World — A Benchmark for Multi-Task and Meta-RL (paper)
type: source
url: https://arxiv.org/abs/1910.10897
author: Tianhe Yu, Deirdre Quillen, Zhanpeng He, Ryan Julian, Avnish Narayan, Hayden Shively, Adithya Bellathur, Karol Hausman, Chelsea Finn, Sergey Levine
published: 2019-10 (CoRL 2019)
ingested: 2026-05-16
tags: [metaworld, benchmark, meta-rl, multi-task, manipulation, sawyer, mujoco]
---

## Summary
The original [Meta-World](../entities/metaworld.md) paper — proposes a **50-task** simulated robot manipulation benchmark for **meta-RL and multi-task RL** evaluation, designed as a deliberate response to prior meta-RL benchmarks that used "narrow" task distributions (e.g. running velocities). 10 authors from Stanford + UC Berkeley + Google Brain, led by Tianhe Yu with [Chelsea Finn](../entities/chelsea-finn.md) and [Sergey Levine](../entities/sergey-levine.md) senior. CoRL 2019. The most striking finding: **even with as few as 10 distinct training tasks, state-of-the-art meta-RL and multi-task RL algorithms struggle to learn them simultaneously** — a result that has aged into a structural critique of meta-RL itself.

## Key claims

### Abstract (verbatim)
"Meta-reinforcement learning algorithms can enable robots to acquire new skills much more quickly, by leveraging prior experience to learn how to learn. However, much of the current research on meta-reinforcement learning focuses on task distributions that are very narrow. For example, a commonly used meta-reinforcement learning benchmark uses different running velocities for a simulated robot as different tasks. When policies are meta-trained on such narrow task distributions, they cannot possibly generalize to more quickly acquire entirely new tasks. Therefore, if the aim of these methods is to enable faster acquisition of entirely new behaviors, we must evaluate them on task distributions that are sufficiently broad to enable generalization to new behaviors. In this paper, we propose an open-source simulated benchmark for meta-reinforcement learning and multi-task learning consisting of 50 distinct robotic manipulation tasks. Our aim is to make it possible to develop algorithms that generalize to accelerate the acquisition of entirely new, held-out tasks. We evaluate 7 state-of-the-art meta-reinforcement learning and multi-task learning algorithms on these tasks. Surprisingly, while each task and its variations (e.g., with different object positions) can be learned with reasonable success, these algorithms struggle to learn with multiple tasks at the same time, even with as few as ten distinct training tasks. Our analysis and open-source environments pave the way for future research in multi-task learning and meta-learning that can enable meaningful generalization, thereby unlocking the full potential of these methods."

### Headline result
- **7 SOTA meta-RL / multi-task RL algorithms evaluated**. Each task is individually learnable. **Multi-task learning across just 10 tasks** is where the algorithms struggle — even with low task counts.

### Benchmark structure (per project page / entity, not surfaced from abstract)
The benchmark exposes four splits: **ML10, ML45** (meta-learning, 10 / 45 training tasks held out from disjoint held-out tasks) and **MT10, MT50** (multi-task, all-tasks-seen training).

## Entities mentioned
- [Metaworld](../entities/metaworld.md)
- [MuJoCo](../entities/mujoco.md) — physics engine.
- [Chelsea Finn](../entities/chelsea-finn.md), [Sergey Levine](../entities/sergey-levine.md) — senior authors.
- Downstream users in the wiki: [MuJoCo Playground](../sources/mujoco-playground-paper.md), [JEPA-WMs](../sources/jepa-wms-paper.md) (42 Metaworld tasks).

## Concepts touched
- None directly — Meta-World is a benchmark substrate that surfaces multi-task / meta-RL failure modes.

## Open questions
- Robot platform and physics engine confirmed via the entity page (Sawyer + MuJoCo) but not surfaced from the abstract. Pull from §3 of the paper body if those details become load-bearing.
- The "50 tasks" choice itself is unexplained in the abstract — design rationale (vs 30, vs 100) is presumably in the methods section.
- Whether the 2019 multi-task-failure result has been overturned by post-2020 work (RT-2 / VLAs / scaling) is the most interesting follow-up question.
