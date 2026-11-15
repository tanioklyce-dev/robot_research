---
title: "Sparks of Weight-Space Programming: LLMs can natively read & write neural network weights"
type: source
url: https://rikiyat.github.io/blog/weight-space-programming/
local_path: raw/2026-11-02-sparks-of-weight-space-programming.md
sha256: 8270b7cfc09f538dc75df26015e3e4229bf857297c1e2a5a9c0aedc6e4cc3f89
author: Rikiya Takehi*, Jayden Teoh*, Alex Zhang, Omar Khattab (MIT CSAIL; * equal contribution)
published: 2026-11-02
ingested: 2026-11-14
format: blog post (not peer-reviewed); "Response to Comments" addendum dated 2026-11-12
logs: https://github.com/RikiyaT/lm_understand-logs
tags: [weight-space-programming, gpt-6-astra, mechanistic-interpretability, gradient-free-optimization, policy-repair, ppo, kinetix, minatar, go, qwen, gemma3, sycophancy, induction-heads, autoresearch]
---

> [!note] Edition captured
> The raw copy includes the **2026-11-12 "Response to Comments"** addendum, so the post has already changed in place once. The raw file is the text extracted from the HTML article body. Interactive figures are not preserved. The post was not given a `fetch_url`, because the sealed hash is of the extracted text rather than the HTML.

## Summary

The post argues that a frontier LLM, used as-is in natural language, can **read and write neural-network weights the way a programmer reads and edits code**. The authors call this **Weight-Space Programming**. They are explicit that it names a *concept*, "treating a network's weights as a program to be read and written," and is not a method. The programmer in every experiment is [GPT-6 Astra](../entities/gpt-6-astra.md). It gets no gradients and no training loop, and in several experiments no tools and no forward passes. There are eight experiments, each with a stated budget. Three **read** weights: identifying the game, the diffusion shape, the training language, and induction heads. Two **fix** them: a stuck PPO car policy, and Qwen3.5-0.8B's reasoning loops. Two **write** them from zero: MinAtar agents and a 1.5M-parameter Go network. The eighth experiment, identifying a sycophantic fine-tune, **fails from the weights alone**. The headline results are a zero-shot Breakout network that scores 20× a 500M-step PPO agent, and a 0.016% weight edit that takes Qwen3.5-0.8B on MATH-500 from 7.9% to 48.1%. A null result on Gemma 3 270M gives the post's most important caveat: *editing removes an obstacle that hid an ability; it did not add one.*

## Key claims

**Reading weights (no forward passes)**
- **Exp 1: which game.** There are four PPO policies (1B steps each) on the authors' own 10×10 grid versions of Breakout, Pong, Pac-Man and Freeway. All four use the same MLP, 500→32→32→5 with 17,253 weights. Given only the raw weights as text, with no tools and no list of games to choose from, Astra names **all four** correctly. It does this from where each input channel's first-layer weights concentrate. For example, the Breakout agent's weights lie along the bottom row, where the paddle is.
- **Exp 2: what a DDPM draws.** There are three 12×12 DDPMs (circle, square, triangle; 23,824 weights each). Astra identifies all three from the output layer, but draws each shape as an **outline**, although the models generate filled shapes. The authors read this error as evidence that Astra reads the weight geometry rather than simulating the forward pass.
- **Exp 3: language from the middle layers only.** There are three 7.16M-parameter character-level transformers (4 layers × 6 heads), trained on Python, romaji and English. The embedding and unembedding are removed, Python analysis is allowed (≤100 runs), and running any layer on any input is forbidden. Astra names the right language **in all 6 attempts**, though its confidence is only 0.48–0.62. It finds **exactly** the measured copying (induction) heads, with no false positives, using QK/OV matrix composition. The authors note this is the Elhage et al. method, which they never mentioned to Astra. It distinguishes romaji because the last block writes in fewer distinct directions, which fits romaji never using q, l, v or x.
- **Exp 7: which model is sycophantic. A failure.** Two Gemma 3 270M copies were fine-tuned identically, one honest and one that follows the user's suggested answer, with the embeddings and output layer frozen. **From the weights alone, Astra could not tell them apart in 4 of 4 attempts.** It found many weight differences but could not map them to behaviour. When it was allowed attention patterns, but not outputs, on texts it wrote itself, it identified the sycophant in **3 of 3** pairs: middle-layer head 10.2 attends to the user's answer (85.7% vs 0.75%).

**Fixing weights**
- **Exp 4: a stuck control policy.** The official Kinetix PPO actor (171,664 weights, 1B steps) has fallen into a local minimum on a car-over-ramp level. The car drives straight at the ramp and stalls (0/256), when it should back up first to gain run-up. Astra gets the weights, a scene description and one recorded episode. With **no tools and one reply**, it edits **3.5% of the weights** and reaches **1,024/1,024 successes**. Its edit adds a small side path of a few units per layer. The path reads the car's position and speed, drives the reversing manoeuvre, and switches off once the wheel is past the strip, leaving the trained network to do the rest.
- **Exp 8: Qwen3.5-0.8B math.** Astra works in a CPU Python kernel over the weights. It may use practice problems from GSM8K and MATH training sets and 10, 25 or 50 forward passes (≤512 problems each). No gradients are allowed. It traced the model's thinking loops to a **single direction written by the MLPs of layers 15 and 19**. It subtracted that direction from 64 output columns in each, which is **131,072 weights (0.016%)**. With 50 passes, MATH-500 went from **7.9 to 48.1**, GSM8K from **13.8 to 67.1**, and IFEval from **21.0 to 62.3**. Token-limit hits fell from **93% to 33%**. With 10 or 25 passes the loops barely moved (87%, 86%). The extra passes are what made the difference.
- **Gemma 3 270M null result.** This model rarely loops (8.5% token-limit hits). Astra found only ordinary reasoning errors, with "no single component behind them to switch off." No edit moved MATH-500 by more than about a point (6.8 → 7.6 at best), and Astra itself called the gain not established.

**Writing weights from zero**
- **Exp 5: MinAtar, one shot.** Astra writes all weights for a 600→32→32→6 network as text in one reply. It has no data, no tools and no rollouts. The networks score Breakout **517.4** (PPO-100M 15.8, PPO-500M 25.3), Asterix **53.2** (25.8 / 55.2) and Seaquest **53.1** (5.6 / 88.9), over 1,000 episodes with sticky actions. In Breakout, layer 1 computes where the ball will land and layer 2 moves the paddle there.
- **Exp 6: 9×9 Go, 1.48M weights.** The network is 243→512×6→82 and starts at zero. Astra builds it in a Python sandbox with no Go library and no search, as a hand-written Go program. It marks stones and liberties, propagates along chains to find groups in danger, and scores captures, saves, atari avoidance and eye-filling. With **0 forward passes** (a single 336-line Python run), it wins more than half its games against two small PPO networks. With **50 passes** (each ≤128 practice games), it beats an equal-sized PPO network trained on 20M games.

**Framing (from the 2026-11-12 addendum)**
- The authors say they are claiming a *capability*, not a method, and compare it to GPT-3's in-context learning: weak, but new. They argue the baselines are not meant as fair competitions. PPO is there to "put a price, in experience" on what Astra achieves with none.
- Gradients are not ruled out by the concept. The authors excluded them here only to isolate what the model gets from reasoning alone. "Natively" means no training loop and no network trained specifically to read weights. Python is "a tool for that reasoning, not for optimization."
- They have not compared Astra with human interpretability researchers. They expect the field to advance by composing known interpretability techniques at scale.
- They report more than 100 follow-ups. The ones named include replications (Hugging Face, Simon Willison, others), **robot policies (SII, SJTU, HKU)**, quantum circuits (Penn State), IWIBench, and clinical and genomics applications. Full experiment logs are public, and the edited Qwen is on Hugging Face.

**Proposed futures (speculative, the authors' own list)**
- Auditing without evaluation, for example finding backdoors directly in the weights.
- One-shot initialisation instead of training.
- Zero-data capability steering and unlearning without catastrophic forgetting.
- A "richer, more native" path to recursive self-improvement.
- Grafting circuits across *different* architectures.
- The authors are building a WSP benchmark and harness.

## Entities mentioned
- [GPT-6 Astra](../entities/gpt-6-astra.md) is the weight programmer in all experiments.
- [OpenAI](../entities/openai.md) makes Astra.
- [Qwen](../entities/qwen.md) is the edited model in Exp 8 (Qwen3.5-0.8B).
- [Gemma3](../entities/gemma3.md) is the sycophancy testbed and the null result (270M).
- [Hugging Face](../entities/hugging-face.md) rebuilt the Qwen edit from the logs and hosts a demo.
- [Andrej Karpathy](../entities/andrej-karpathy.md): his *Software 2.0* essay is cited. Weights as the program is that essay's premise, taken literally.
- People with no wiki page: Omar Khattab (DSPy; prompt and program optimisation, the "LLMs optimise text artifacts" lineage the post extends), Alex Zhang, Rikiya Takehi, Jayden Teoh.

## Concepts touched
- [Weight-space programming](../concepts/learning/weight-space-programming.md) is the concept this post names.
- [Mechanistic interpretability](../concepts/safety/mechanistic-interpretability.md): reading and editing weights with a general model instead of purpose-built tools; independent rediscovery of the induction-head QK/OV method; direction ablation.
- [Code as policy](../concepts/agents/code-as-policy.md): Exp 5 and 6 are code-as-policy compiled into weights. The model writes a program and then expresses it as a network.
- [Control abstraction levels](../concepts/robotics/control-abstraction-levels.md): a new rung, where the LLM writes the policy's parameters rather than its actions or its code.
- [LLM-agent architecture](../concepts/agents/llm-agent-architecture.md): the harness design (a Python kernel, a forward-pass budget, an audited tool log) is the experimental variable.

## Assessment

> [!warning] Single-lab, single-model, self-reported, mostly n = 1
> This is a blog post, and almost every result is **one model and one setting**. Exp 3 and Exp 7 have more than one attempt, but none has more than 6. The logs are public, and replications are reported, which counts in the post's favour. But none of the replications is ingested here, so this page cannot judge them.

Four points matter in judging the results.

- **The Qwen number is mostly an un-looping number.** The authors say so in effect. 93% of base answers hit the 32k-token limit under the chosen sampling, so the base model fails by never finishing rather than by reasoning badly. The authors defend the setting: thinking-off would raise the base score, but it avoids the broken mode instead of repairing it. The Gemma null result is the control that shows the limit. Read the 7.9 → 48.1 jump as **repairing a single-component failure**, which is notable, and not as gaining math ability.
- **PPO baselines say little about relative strength.** Breakout 517 against PPO-500M's 25 points to a poorly converged PPO, not to a 20× better policy. The authors' framing, that PPO here measures the cost in experience of getting there, is the honest reading.
- **"No tools" still allows vast amounts of in-context reasoning.** "No forward passes" in Exp 3 still allows unlimited matrix algebra on the weights, which can approximate running layers on synthetic inputs. The authors audited every run for actual forward passes.
- **The capability is uneven, and the one failure is the one safety cares about.** Structural features (input geometry, induction heads, a loop direction) are readable from the weights. A behavioural disposition installed by fine-tuning (sycophancy) was not, until activation-level evidence was allowed. The "auditing without evaluation" future depends on exactly the case that failed.

## Why this matters for this wiki

- **Policy repair without retraining.** Exp 4 is a robotics result in all but name. An RL controller is stuck in a local minimum, and it is fixed by a minimal, interpretable weight edit that bolts on a behaviour and then hands control back. The post links an extension to a real VLA: SII, SJTU and HKU had Claude Opus 5.5 edit **π0.5**'s weights on a YAM arm. It is now ingested as [Editing π0.5's weights](robotics-weight-editing-pi05.md). It claims a RoPE-based action-timing edit fitted into Q/K weights, a repair of a prefix bug in the official Training-Time RTC implementation encoded in the time-modulation weights, and a −12% task time at 40 Hz with 100% success in both arms of the comparison, at 3 runs per condition.
- **A rung above code-as-policy.** This wiki already has frontier LLMs as direct policies and as controller writers ([GPT-6 Astra](../entities/gpt-6-astra.md), RoboDojo and RoboPianist). Here the same model writes the policy's **parameters**, with the result still in a fast, deployable network form. That answers the latency and cost objection raised by [Praxis-1](../entities/praxis-1.md) (15.6× slower, 51× costlier per task). The LLM does its expensive thinking once, offline, and the artifact runs at network speed.
- **The proposed interpretability experiment gains an instrument.** [Latent inspection vs policy collapse](../syntheses/projects/latent-inspection-policy-collapse.md) asks whether internals predict failure under perturbation. A general LLM reading a policy's weights is a new candidate reader. The sycophancy failure says to expect it to see structure more readily than dispositions.

## Open questions
- Do the results survive multiple seeds and other frontier models? Is this a GPT-6 Astra capability or a general one? (Compare Astra's model-specific jump on RoboDojo, where GPT-5.5 is near zero.)
- How much of each success comes from the harness: the forward-pass budget, Python, and task description quality? The Qwen 10/25/50-pass gradient suggests the budget is decisive.
- Can a fine-tuned *disposition* (sycophancy, a backdoor, a reward hack) ever be read from weights alone, or is activation access the floor?
- For robot policies: does the π0.5 extension hold beyond its 3-run bottle task? (Its own block-stacking showed no speedup.) Is an edit like Exp 4's side path safe out of distribution, or does it add a hidden mode switch no one tested?
- Candidates to ingest: IWIBench (arXiv 2611.08647) and Simon Willison's replication. The π0.5 post is now ingested as [robotics-weight-editing-pi05](robotics-weight-editing-pi05.md).
