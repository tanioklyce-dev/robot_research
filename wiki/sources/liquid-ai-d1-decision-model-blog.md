---
title: "Introducing d1: The most capable decision model, now with vision (Liquid AI blog)"
type: source
url: https://www.liquid.ai/blog/d1-decision-model
local_path: raw/2026-10-05-liquid-ai-blog-d1-decision-model.md
sha256: 63989ab6e672405fd4ca8dde95146a424bafd38ea0742193e07bb7ca187525ac
author: Liquid AI
published: 2026-10-05
ingested: 2026-10-13
venue: Liquid AI blog
format: "launch blog post, captured 2026-10-13 via curl with article-text extraction. The comparison chart is an animated SVG; its data rows were recovered from the page's inline script and appended to the capture."
tags: [liquid-ai, d1, decision-model, classification, single-forward-pass, vision, visual-inspection, routing, web-agent, context-compaction, api, cost, latency, vendor-source, primary]
---

# Introducing d1: The most capable decision model, now with vision (Liquid AI blog)

## Summary

[Liquid AI](../entities/liquid-ai.md) launched **[d1](../entities/liquid-d1.md)**, which it calls a **decision model**: a model that takes unstructured input (text, images, or both) plus one or more questions and returns **a probability for each possible answer in a single forward pass, without generating any tokens**. There are three question types: **"noul"** (yes/no → a probability), **choice** (a distribution over labels) and **score** (a probability-weighted position on a scale). One request can ask several questions about the same input. A text decision takes **200–300 ms**. Pricing is **$0.04 per million input tokens, with no output tokens**. Images are billed at 1.5 tokens per 32×32 patch, so a 1024² image costs 1,536 tokens. Against GPT-6.1 Sol and Claude Opus 5.5 on six applications, Liquid says d1 *"matches or beats GPT-6.1 Sol on four of them"* at **19×–200× lower cost**. Vision is new in this release, and open weights for later models are promised. Its robot relevance is as a **cheap, fast, calibrated classifier** for the many yes/no questions an agent loop asks: is the grasp done, is a part defective, which tool or folder, keep or drop this context.

## Key claims

- **Mechanism**: one forward pass that returns probabilities, with no decoding. No architecture, parameter count or training detail is given.
- **Latency**: 200–300 ms per text decision through the API.
- **Visual inspection, zero-shot from a short description**: **85–97% accuracy** sorting good from defective parts on four lines of the public **VisA** dataset (circuit boards, candles, cashews, chewing gum). Every model sees a known-good reference part next to the part under inspection.
- **Text applications**: Smart Filter (`WHERE d1(ticket, '…')` in SQL over 150 tickets), Code Search (folder-by-folder descent of the 6,511-file HF transformers repo), Smart Folders, a Web Agent (picks the next action on a flight-search site) and **Context Compaction** (keep, trim or drop each tool output in a coding-agent session: **52% of tokens removed, every needed output kept**). Four were adapted from open-source projects named pg-jev, jevgrep, jev-ultrafast and fast-jev-compaction.
- **Games**: Tetris 70 → **81** cleared lines when the screen image is added to the text state. Wordle **12/12 solved, 3.8 guesses** average, read from screenshots. Quick, Draw! **5.2/6** over 62 words (chance 0.6).
- **Availability**: Liquid API (`api.liquid.ai/decisions/v1/systemone`), Vercel and OpenRouter (text only for now). Open weights of "upcoming models" on Hugging Face "soon."

### The comparison chart, as data

Quality is in % (Smart Filter is F1). Cost is in USD per 1,000 runs. Time is seconds per run.

| Application | d1 | GPT-6.1 Sol | Claude Opus 5.5 | d1 cost | Sol cost | Opus cost | d1 s | Sol s | Opus s |
|---|---|---|---|---|---|---|---|---|---|
| Visual Inspection | **91** | 82 | **92** | 0.048 | 2.56 | 6.17 | 0.8 | 3.3 | 4.0 |
| Smart Filter | 95 | 95 | **98** | 0.85 | 45 | 142 | 6.0 | 6.6 | 7.8 |
| Code Search | 80 | 87 | **100** | 1.25 | 68 | 251 | 2.2 | 17.8 | 24.3 |
| Web Agent | 100 | 100 | 100 | 0.76 | 30 | 86 | 5.1 | 31.8 | 35.0 |
| Context Compaction | **100** | 86 | **100** | 0.31 | 5.89 | 19 | 0.5 | 6.0 | 7.6 |
| Smart Folders | 96 | 98 | **100** | 0.025 | 1.44 | 4.54 | 7.9 | 19.3 | 15.8 |

Methodology as stated: **each application run once per model**, on 2026-10-05, at default reasoning settings, at list prices with no prompt-cache discount. The chat models get batched questions where the input is shared.

## Reading it critically

> [!warning] The headline picks its comparator
> "Matches or beats GPT-6.1 Sol on 4 of 6" is accurate: VI, Filter (tie), Web (tie), Compaction. Against **Claude Opus 5.5**, d1 ties twice (Web, Compaction) and **loses four times**: VI by 1, Filter by 3, Folders by 4 and **Code Search by 20**. The page's own figure shows this; the prose leaves it out. The fair summary is **near-frontier quality on simple, well-posed decisions at 1/20th to 1/200th the cost**, with a real gap on multi-step search (Code Search 80 vs 100).

- **"Answers significantly faster on every task"** fails in one row: Smart Filter is **6.0 s vs 6.6 s** against Sol. Elsewhere the speed-up is 2–12×.
- **n = 1 per application per model**, with no intervals. Every quality gap under ~5 points is a tie under the wiki's [success-rate audit](../syntheses/platforms/vla-success-rate-audit.md) discipline, which covers most of the table.
- **Partial dev/test separation, disclosed**: *"We wrote six of the 15 code questions and two of the four compaction sessions after d1's pipeline was set."* So **9 of 15 code questions and 2 of 4 compaction sessions were written before the pipeline was fixed** and may have shaped it. Liquid deserves credit for saying so.
- **Visual Inspection is reference-conditioned**: each model sees a good part next to the part under test. That is easier than single-image anomaly detection and should be quoted that way.
- **"First model to rival Jev on text decisions"**: the post never says what *Jev* is. The adapted projects (pg-jev, jevgrep, …) suggest it is a widely used model or service in this space, but no ingested source identifies it.
- **No architecture or size**, so it cannot be placed on the wiki's edge-compute ladders. Until open weights ship it is **API-only**, and 200–300 ms is a network round-trip figure.

## Why it matters here

The question an agent loop asks most often is not "write a plan" but **"yes or no?"**: is the object in the gripper, did the step succeed, is this a person, should I stop. [ASIMOV-Agentic](gemini-robotics-2-safety-report.md) benchmarks exactly that routing decision. A decision model returns those answers **as calibrated-looking probabilities, without parsing generated text**. A probability is something a threshold, a safety monitor or a [guardrail](../syntheses/agents/guardrails-for-robot-agents.md) can act on directly, which a sampled "yes" is not. Whether d1's probabilities are actually **calibrated** is the property that matters for that use, and the post doesn't measure it. See [decision models](../concepts/agents/decision-models.md).

## Entities mentioned
- [Liquid AI](../entities/liquid-ai.md) · [d1](../entities/liquid-d1.md) · [OpenAI](../entities/openai.md) (GPT-6.1 Sol) · [Anthropic](../entities/anthropic.md) (Claude Opus 5.5)

## Concepts touched
- [Decision models](../concepts/agents/decision-models.md) — this source names the category.
- [LLM-agent architecture](../concepts/agents/llm-agent-architecture.md) — d1 as a cheap sub-call inside the loop.

## Open questions
- Are the probabilities **calibrated**? Without a reliability diagram, the main advantage over a chat model ("a probability, not a string") is unverified.
- Architecture and parameter count, and whether it is built on Liquid's LFM line. Can the promised open-weight models run on a Jetson-class device?
- What is "Jev"?
- Results with more than one run, and on a held-out code-question set.
