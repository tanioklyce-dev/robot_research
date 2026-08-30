---
title: Gato
type: entity
subtype: model
created: 2026-08-30
updated: 2026-08-30
sources: 0
tags: [gato, deepmind, generalist-agent, multi-embodiment, action-tokenization, mu-law, control-rate, decoder-only]
---

**Gato** — DeepMind, TMLR 2022 ([paper](../sources/gato-paper.md)). A **1.2B-parameter decoder-only transformer** trained on **604 distinct tasks** with one set of weights, which "can play Atari, caption images, chat, stack blocks with a real robot arm and much more, deciding based on its context whether to output text, joint torques, button presses, or other tokens."

**The direct ancestor of every [VLA](../concepts/learning/vla-models.md) in this wiki**: tokenize everything into one sequence, train a decoder-only transformer to predict the next token.

## The two things to remember

**1. The model size was chosen by the control rate.** *"We focus our training at the operating point of model scale that allows real-time control of real-world robots, currently around 1.2B parameters."* Every "why is this VLA only 3B" question in the wiki traces to this constraint — stated here as a deliberate design choice, four years before the wiki's [control-rate ladder](../syntheses/platforms/control-rate-ladder.md) and [Jetson compute comparisons](../syntheses/platforms/jetson-onboard-compute-xlerobot.md) made the same argument from hardware.

**2. Its action tokenization is where discrete action bins come from.** Continuous values — proprioception, joint torques — are **mu-law encoded** to `[−1, 1]`, **discretized to 1024 uniform bins**, and shifted into their own vocabulary slice `[32000, 33024)`. Mu-law is a telephony compander, borrowed because torques, like speech amplitudes, cluster near zero; uniform binning on raw torque wastes resolution where nothing happens. [FAST](fast-action-tokenization.md), [VQ-BeT](vq-bet.md)'s codebook and [latent action tokens](../concepts/learning/latent-action-tokens.md) are later answers to the same allocation problem.

Also notable: **prompt conditioning instead of one-hot task IDs** — 25% of training sequences get a demonstration prepended, and at evaluation the agent is prompted with a successful demonstration by default. In-context imitation, in 2022.

## Numbers

**Over 450 of 604 tasks above a 50% expert-score threshold** (100% = per-task expert, 0% = random, 50 rollouts each). 24 layers, embedding 2048, FFN 8196, context 1024 tokens; 16×16 TPUv3 slice, 1M steps, ~4 days. Trained **offline and purely supervised**.

> [!warning] 50% of expert is a low bar
> The famous sentence is "same weights, Atari and a real robot arm." The measurement is 450/604 above *half* of expert — recognizably attempting the task, not performing it. Read Gato as an existence proof that one set of weights can span modalities and embodiments, not as evidence that 2022 generalists were competitive with specialists.

## Mentioned in

- [Gato paper](../sources/gato-paper.md)

## Open questions / TBD

- **Nobody re-ran Gato at the modern operating point**, which its own framing invites — a [Jetson Thor](jetson-thor.md) is not a 2022 robot computer.
- **The demonstration-in-context assist is never ablated** against no-prompt control performance.
- **Mu-law binning vs learned action tokenization** has never been compared head-to-head on a shared benchmark.
