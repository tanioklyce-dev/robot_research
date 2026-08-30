---
title: "A Generalist Agent (Reed, Żołna, Parisotto et al., DeepMind, TMLR 2022) — Gato"
type: source
url: https://arxiv.org/abs/2205.06175
local_path: raw/2205.06175v3.pdf
sha256: 1d9ce8dfcac0f01296ac1dd6f1c0fbc94f7e180af2956adb5d27689407cf5332
author: "Scott Reed*, Konrad Żołna*, Emilio Parisotto*, Sergio Gómez Colmenarejo, Alexander Novikov, Gabriel Barth-Maron, Mai Giménez, Yury Sulsky, Jackie Kay, Jost Tobias Springenberg, Tom Eccles, Jake Bruce, Ali Razavi, Ashley Edwards, Nicolas Heess, Yutian Chen, Raia Hadsell, Oriol Vinyals, Mahyar Bordbar, Nando de Freitas"
affiliation: DeepMind
venue: "Transactions on Machine Learning Research (11/2022); arXiv 2205.06175"
published: 2022-05-12
ingested: 2026-08-30
tags: [gato, generalist-agent, multi-embodiment, action-tokenization, mu-law, prompt-conditioning, decoder-only, deepmind, control-rate, foundational]
---

> [!note] Ingest depth
> Read from the **full PDF** (`raw/2205.06175v3.pdf`, 42 pages). §1–5 read in full (motivation, tokenization, architecture, deployment, datasets, results, scaling); per-domain appendices skimmed. **22 wiki pages cited Gato with no page.**

## Summary

**Gato** — Reed, Żołna, Parisotto et al. (DeepMind; TMLR 2022). *"A multi-modal, multi-task, multi-embodiment generalist policy."* One decoder-only transformer, **one set of weights**, trained on **604 distinct tasks**, that *"can play Atari, caption images, chat, stack blocks with a real robot arm and much more, deciding based on its context whether to output text, joint torques, button presses, or other tokens."*

**The direct ancestor of every [VLA](../concepts/learning/vla-models.md) in this wiki**, and the paper that established the move those models are built on: **tokenize everything — pixels, text, proprioception, torques — into one sequence, and train a decoder-only transformer to predict the next token.**

## The sentence that matters most to this wiki

> "We focus our training at the operating point of model scale that allows **real-time control of real-world robots**, currently around **1.2B parameters** in the case of Gato."

**The model size was chosen by the control rate, not by the capability curve.** They say so, and then say the operating point "will naturally increase" as hardware improves, "pushing generalist models higher up the scaling law curve."

That is the wiki's [control-rate ladder](../syntheses/platforms/control-rate-ladder.md) argument stated by the authors of the paper that started the generalist-policy line — four years before the [onboard-compute comparisons](../syntheses/platforms/jetson-onboard-compute-xlerobot.md) this wiki runs on Jetson modules. Every "why is this VLA only 3B parameters" question in the wiki traces to this constraint, and Gato is where it was first made explicit as a design *choice* rather than a limitation.

## Tokenization (§2.1) — the wiki's action-tokenization ancestor

| Modality | Scheme | Range |
|---|---|---|
| **Text** | SentencePiece, 32,000 subwords | `[0, 32000)` |
| **Images** | non-overlapping **16×16 patches in raster order** ([ViT](vit-paper.md)-style), pixels normalized to `[−1, 1]` and divided by `√16` | — |
| **Discrete** (Atari buttons) | flattened row-major to integers | `[0, 1024)` |
| **Continuous** (proprioception, **joint torques**) | flattened row-major, **mu-law encoded** to `[−1, 1]`, **discretized to 1024 uniform bins**, then shifted | `[32000, 33024)` |

Then a canonical ordering: text in input order; image patches in raster order; tensors row-major; **nested structures in lexicographic order by key**; **agent timesteps as observation tokens, a separator, then action tokens**; episodes in time order.

> [!note] This is where discrete action bins come from
> The continuous-value row is the ancestor of the action-tokenization line this wiki tracks in detail — RT-2's discrete bins, [FAST](../entities/fast-action-tokenization.md), [VQ-BeT](../entities/vq-bet.md)'s codebook, [latent action tokens](../concepts/learning/latent-action-tokens.md). Gato's answer is the crudest and the most direct: **mu-law companding plus 1024 uniform bins, occupying their own slice of the vocabulary.**
>
> Mu-law is worth noticing — it is a telephony compander, borrowed because joint torques, like speech amplitudes, are non-uniformly distributed with most mass near zero. Uniform binning on raw torque would spend most of its resolution where nothing happens. Later schemes (FAST's DCT-based compression, VQ codebooks) are answers to the same problem: *a discrete action vocabulary has to allocate its resolution where the actions actually are.*

## Architecture and conditioning

**1.2B-parameter decoder-only transformer**: 24 layers, embedding size 2048, post-attention feed-forward hidden size 8196. Trained on a **16×16 TPUv3 slice for 1M steps**, batch 512, **context length L = 1024 tokens**, about **4 days**.

**Prompt conditioning instead of task IDs.** Distinct tasks can share an embodiment and action spec, so the model needs disambiguation. Rather than one-hot task identifiers, **25% of sequences in each batch get a prompt prepended** — an episode from the same source agent on the same task. Half of those prompts come from the *end* of the episode ("acting as a form of goal conditioning"), half sampled uniformly. **At evaluation the agent is prompted with a successful demonstration of the desired task**, by default in all reported control results.

> [!note] In-context imitation, in 2022
> "Show it a demonstration in the prompt, then let it act" is the mechanism the wiki now tracks as [in-context robot learning](../concepts/learning/in-context-robot-learning.md). Gato is where it was first done at scale for control. Note the honesty of the default: **every control number in the paper is obtained with a successful demonstration in the context.** That is a meaningful assist, and it should be read as part of the result rather than a detail of the eval harness.

Deployment is autoregressive rollout: tokenize the prompt, get the first observation, tokenize and append, sample the action **one token at a time**, send it to the environment, repeat.

## Results

**Over 450 of 604 tasks above a 50% expert-score threshold**, where 100% is the per-task expert and 0% a random policy, averaged over 50 rollouts per task. Real-robot results on the **RGB Stacking** benchmark (sim and real).

> [!warning] The headline does more rhetorical work than the number supports
> *"The same network with the same weights can play Atari, caption images, chat, and stack blocks with a real robot arm"* is true and is what everyone remembers. **"450 of 604 tasks above 50% of expert"** is the measurement, and 50% of an expert is a low bar — it is the level at which a policy is recognizably attempting the task, not performing it. The paper is not deceptive about this (the threshold is stated, Figure 5 shows the full distribution), but the citation-level summary of Gato consistently drops it.
>
> Read Gato as **an existence proof that one set of weights can span modalities and embodiments**, which is genuinely what it claimed, and not as evidence that generalist policies were competitive with specialists in 2022. They were not.

Trained **offline and purely supervised** — behaviour cloning over the whole corpus. The authors note "in principle, there is no reason it could not also be trained with either offline or online RL," and do not do so. Scaling analysis uses **79M / 364M / 1.18B** variants.

## Entities mentioned

- **[Google DeepMind](../entities/google-deepmind.md)** — all 20 authors.
- **Oriol Vinyals** — also a [seq2seq](sutskever2014-sequence-to-sequence-learning.md) author; Nando de Freitas, Raia Hadsell, Nicolas Heess.
- **[ViT](vit-paper.md)** — the image patch tokenization is taken directly from it.
- **[Attention Is All You Need](attention-is-all-you-need.md)** — "a transformer for simplicity and scalability."

## Concepts touched

- **[VLA models](../concepts/learning/vla-models.md)** — Gato is the architecture before the "L" was load-bearing.
- **[Latent action tokens](../concepts/learning/latent-action-tokens.md)** / **[FAST](../entities/fast-action-tokenization.md)** — descendants of the mu-law binning.
- **[In-context robot learning](../concepts/learning/in-context-robot-learning.md)** — prompt conditioning with demonstrations.
- **[Imitation learning](../concepts/learning/imitation-learning.md)** — offline, supervised, over 604 tasks.
- **[Control-rate ladder](../syntheses/platforms/control-rate-ladder.md)** — the 1.2B operating point.

## Open questions / TBD

- **Nobody re-ran Gato at modern scale.** Its own framing invites it: the operating point rises with hardware, and a [Jetson Thor](../entities/jetson-thor.md) is not a 2022 robot computer. What 604-task generalist performance looks like at the 2026 operating point is unknown.
- **The demonstration-in-context assist is never ablated** against no-prompt control performance in the main results.
- **Mu-law vs learned action tokenization** has, as far as this wiki knows, never been compared head-to-head on a shared benchmark.
