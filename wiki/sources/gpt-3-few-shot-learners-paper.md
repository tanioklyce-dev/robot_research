---
title: "Language Models are Few-Shot Learners (GPT-3; Brown, Mann, Ryder, Subbiah et al., NeurIPS 2020)"
type: source
url: https://arxiv.org/abs/2005.14165
local_path: raw/2005.14165.pdf
sha256: 97fd272f1fdfc18677462d0292f5fbf26ca86b4d1b485c2dba03269b643a0e83
author: "Tom B. Brown*, Benjamin Mann*, Nick Ryder*, Melanie Subbiah*, Jared Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell … Sam McCandlish, Alec Radford, Ilya Sutskever, Dario Amodei (31 authors)"
affiliation: OpenAI
published: 2020-05-28
revised: 2020-07-22 (v4)
venue: "NeurIPS 2020; arXiv 2005.14165 v4"
format: paper (75 pp; 40 pp body + 32 pp appendices)
arxiv: 2005.14165
tags: [gpt-3, in-context-learning, few-shot, scaling, language-model, meta-learning, emergence, contamination, openai, foundational]
ingested: 2026-09-12
---

# Language Models are Few-Shot Learners (GPT-3)

## Summary

**The paper that named in-context learning and showed it grows with scale.** OpenAI trained eight autoregressive transformers from 125 M to **175 B** parameters on 300 B tokens and evaluated every one, without any gradient update, in three settings: *zero-shot* (an instruction), *one-shot* (one demonstration), *few-shot* (as many demonstrations as fit in a 2,048-token context, typically 10–100). Few-shot GPT-3 reached or approached fine-tuned state of the art on some tasks (LAMBADA 86.4%, TriviaQA 71.2%, CoQA 85.0 F1) and stayed far behind on others (ANLI, RACE, WiC at chance), and the paper's central figure is not any one number but the *shape*: **the gap between zero-, one- and few-shot widens as the model grows** — *"larger models are more proficient meta-learners."*

For this wiki the paper matters for two reasons. It is the **origin of the framing** that [Skild's S1](skild-s1-blog.md) and [Generalist's GEN-1.5](generalist-gen-1-5-blog.md) borrow — *"robotics is stuck in the BERT era"* — and it is, unlike both of them, a study that **published in-context ability against scale** across eight model sizes. And it is careful about the question those two vendors now dispute: whether the inner loop is *learned* or *recognized*. GPT-3 added **no meta-learning objective** and its authors decline to say which — footnote 1 keeps the terms *"agnostic on the question of whether the model learns new tasks from scratch at inference time or simply recognizes patterns seen during training,"* and §5 calls it *"an important unexplored direction."*

> [!note] What the analogy carries and where it strains
> GPT-3's few-shot examples are same-modality text drawn from the task's own training split; the robots' demonstrations are videos of a different body. GPT-3's scaling axis is **model size at fixed data** (eight sizes, 300 B tokens each); S1's is **data at fixed architecture** (1k → 100k hours). GPT-3 tested tasks *"unlikely to be directly contained in the training set"* (word scrambling, novel words) precisely to probe learning versus recognition; neither robot post does the equivalent. The borrowed sentence is fair as motivation and not as evidence.

## Key claims

### Definitions (§1, §2)

- **In-context learning** — *"we use the term 'in-context learning' to describe the inner loop of this process, which occurs within the forward-pass upon each sequence"* (Fig. 1.1); meta-learning is the outer loop, *"in this case just language model pre-training."*
- Few-shot: *"the model is given a few demonstrations of the task at inference time as conditioning, but no weight updates are allowed."* K typically 10–100. One-shot: one demonstration plus an instruction. Zero-shot: instruction only.
- The related-work section places the mechanism beside RL² and Hochreiter et al. 2001: *"an inner loop of adaptation takes place through computation in the model's activations across timesteps, without updating the weights, while an outer loop… updates the weights, and implicitly learns the ability to adapt to or at least recognize tasks defined at inference-time."*

### Models and data (§2, Tab. 2.1, 2.2)

| Model | Params | Layers | d_model | Batch | LR |
|---|---|---|---|---|---|
| Small | 125 M | 12 | 768 | 0.5 M | 6.0e-4 |
| Medium | 350 M | 24 | 1024 | 0.5 M | 3.0e-4 |
| Large | 760 M | 24 | 1536 | 0.5 M | 2.5e-4 |
| XL | 1.3 B | 24 | 2048 | 1 M | 2.0e-4 |
| 2.7 B | 2.7 B | 32 | 2560 | 1 M | 1.6e-4 |
| 6.7 B | 6.7 B | 32 | 4096 | 2 M | 1.2e-4 |
| 13 B | 13 B | 40 | 5140 | 2 M | 1.0e-4 |
| **GPT-3** | **175 B** | 96 | 12288 | 3.2 M | 0.6e-4 |

All trained for 300 B tokens; same architecture as GPT-2 with alternating dense and locally banded sparse attention; context 2,048. Data: filtered Common Crawl 410 B tokens (60% of the mix, seen 0.44 epochs), WebText2 19 B (22%), Books1 12 B, Books2 55 B, Wikipedia 3 B — higher-quality sets sampled 2–3×. Trained on V100s on a Microsoft cluster; *"several thousand petaflop/s-days."*

### The scaling finding (§1, §3; Fig. 1.2, 1.3, 3.8)

- Fig. 1.2 (symbol removal): *"The steeper 'in-context learning curves' for large models demonstrate improved ability to learn a task from contextual information."* Fig. 1.3 (42 benchmarks): *"While zero-shot performance improves steadily with model size, few-shot performance increases more rapidly."* Fig. 3.8 (SuperGLUE): performance rises with both size and K; fewer than eight examples per task beat a fine-tuned BERT-Large.
- *"One notable pattern is that the gap between zero-, one-, and few-shot performance often grows with model capacity, perhaps suggesting that larger models are more proficient meta-learners."*
- Arithmetic (§3.9.1): 175 B does 2-digit addition at 100%, 3-digit at 80.4%, 4-digit at 25.5%; the 13 B model does 2-digit *"only half the time"* — a jump between the two largest sizes. Only 17 of 2,000 three-digit addition problems appear in the training data; errors like a missed carry suggest computation, not lookup.
- Word scrambling (§3.9.2): zero-shot near zero, one-shot weak, few-shot 38–67% — *"the model really does appear to learn these tasks at test time."* Reversing words: 0% at every size.

### Representative results (§3)

| Task | Fine-tuned SOTA | GPT-3 zero / one / few |
|---|---|---|
| LAMBADA acc | 68.0 | 76.2 / 72.5 / **86.4** |
| TriviaQA | 68.0 (RAG) | 64.3 / 68.0 / **71.2** |
| Natural Questions | 36.6 | 14.6 / 23.0 / 29.9 |
| CoQA F1 | 90.7 | 81.5 / 84.0 / 85.0 |
| SuperGLUE avg | 89.0 | — / — / 71.8 (K = 32) |
| WiC | 76.1 | — / — / 49.4 (chance) |
| ANLI R3 | — | small models at chance; 175 B *"closes almost half the gap"* |
| Winogrande | 84.6 | 70.2 / 73.2 / 77.7 |
| Fr→En BLEU | 35.0 (sup.) | 21.2 / 33.7 / 39.2 |

Systematic weakness on *"comparison"* tasks (WiC, ANLI, RTE) — two sentences to relate — which the authors attribute to the unidirectional objective.

### Contamination (§4) and honesty

- A filtering bug left benchmark overlaps in the training data; too expensive to retrain, so every benchmark got a "clean" subset by 13-gram overlap. Most shifts negligible; **PIQA** (29% flagged, −3 pp) and **Winograd** (45% flagged, 132 schemas found in training) are asterisked; four Wikipedia LM benchmarks dropped entirely.
- News-article detection (§3.9.4): human accuracy at spotting 175 B output was **52%** (chance 50%) on ~200-word articles and 52% on ~500-word ones, versus 86–88% on a deliberately bad control.

### Limitations (§5) and impacts (§6)

- Repetition and incoherence over long passages; *"special difficulty with 'common sense physics'"* — *"If I put cheese into the fridge, will it melt?"*
- *"Large pretrained language models are not grounded in other domains of experience, such as video or real-world physical interaction, and thus lack a large amount of context about the world"* — with images and RL fine-tuning named as directions.
- Sample inefficiency versus a human lifetime of text; inference cost; uncalibrated; retains data biases (§6.2: 83% of 388 occupations male-leaning; race and religion co-occurrence analyses).
- §6.1 threat analysis: misuse *"not immediate"* from low-skill actors, APTs uninterested absent steerability.

## What robotics borrowed, precisely

| Borrowed by [S1](skild-s1-blog.md) / [GEN-1.5](generalist-gen-1-5-blog.md) | What GPT-3 says |
|---|---|
| "BERT era → GPT-3 era" as the transition robotics needs | The paper's own framing (§1): fine-tuning needs thousands of examples per task; few-shot needs none. |
| Inner loop / outer loop, learned by pre-training | Fig. 1.1 and §7: the outer loop is *"just language model pre-training"*; no meta-learning objective was added. |
| S1: the inner loop must be *designed* into episodic data | Not claimed. GPT-3 notes only that pre-training sequences *"sometimes"* contain *"repeated sub-tasks embedded within a single sequence."* |
| GEN-1.5: the inner loop *emerged* | Not claimed either. Footnote 1 and §5 explicitly leave learning-vs-recognition open. |
| In-context ability scales | **Shown**, across eight sizes, with curves (Fig. 1.2, 1.3, 3.8) — the figure the [scaling-laws page](../concepts/learning/scaling-laws-vla.md) notes neither vendor has published. |

So the paper both vendors invoke is agnostic on the exact point they disagree about, and it did the experiment neither has done.

## Entities mentioned

- [OpenAI](../entities/openai.md) · [Dario Amodei](../entities/dario-amodei.md) (last author) · Jared Kaplan (scaling laws; Johns Hopkins/OpenAI), Alec Radford, Ilya Sutskever — no pages.

## Concepts touched

- [In-context robot learning](../concepts/learning/in-context-robot-learning.md) — origin of the term and of the designed-vs-emergent ambiguity.
- [Scaling laws for VLAs](../concepts/learning/scaling-laws-vla.md) — the reference form of "capability vs scale" curves.
- [Chain of thought](../concepts/learning/chain-of-thought.md) — the few-shot prompting regime CoT later extends; GPT-3's 4–5-digit arithmetic failures are the kind of task it targeted.
- [Language model → transformer lineage](../syntheses/sequence-models/language-model-to-transformer-lineage.md) — the first post-2017 stop on that arc.

## Open questions

- **Learning or recognition** — still open in 2026 for robots as for text; GPT-3's synthetic-task probe (tasks unlikely to be in training data) is the method to copy.
- **Data vs size.** GPT-3 scaled size at fixed tokens; whether S1's data-axis crossover is the same phenomenon is untested.
- **The 13 B → 175 B jump** on arithmetic: threshold or resolution artefact of eight points?
