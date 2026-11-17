---
title: "embodiedreasoning/ERQA (GitHub)"
type: source
subtype: code-repository
url: https://github.com/embodiedreasoning/ERQA
fetch_url: https://raw.githubusercontent.com/embodiedreasoning/ERQA/main/README.md
local_path: raw/2026-11-17-erqa-github-readme.md
sha256: c4c10f1c66b3a36c3f3d2a052a2a80277ec87aaa4fa504a8a0fc0777bdc0343a
author: Gemini Robotics Team, Google DeepMind
affiliation: Google DeepMind
published: 2025-03-12
ingested: 2026-11-17
license: CC-BY-4.0
format: "GitHub repository at commit 5bba488 (2025-03-12; 8 commits, none since). README captured in raw/. Also read: eval_harness.py, loading_example.py, requirements.txt, the issue list. data/erqa.tfrecord (91 MB, sha256 1974f5e587eac144cc3ba325477477b8ad6a56c22ce4e419c34229520b4c93e2) was parsed directly for the statistics below and is not copied into raw/."
tags: [erqa, benchmark, embodied-reasoning, vqa, dataset, evaluation-harness, google-deepmind, gemini-robotics, primary]
---

# embodiedreasoning/ERQA (GitHub)

## Summary

The public release of **[ERQA](../entities/erqa.md)**, the embodied-reasoning benchmark introduced in the [2025 Gemini Robotics report](gemini-robotics-report-2025.md). The repository is small: one TFRecord file with the 400 questions and their images, a loader, and "an example of a lightweight evaluation harness" for the Gemini and OpenAI APIs. It has had no commits since 2025-03-12, the day the report was announced. There is no leaderboard, no results file, and no implementation of the chain-of-thought prompt behind the report's higher scores. What the repository adds to the wiki is the dataset itself, which can be measured, and the scoring rule, which explains why published ERQA numbers are hard to compare.

## Key claims

### From the README
- "A benchmark of multi-modal embodied reasoning questions" covering "spatial reasoning and world knowledge focused on real-world scenarios, particularly in the context of robotics."
- Questions are "multimodal interleaved images and text, phrased as multiple-choice questions. The answers are provided as a single letter (A, B, C, D)."
- Five features per example: `question`, `image/encoded` (one or more), `answer`, `question_type` and `visual_indices`, which "determines image placement."
- "By default, the full ERQA benchmark consists of 400 examples." The harness's own `--num_examples` default is 1.
- Licence: CC BY 4.0.

### From the harness code (`eval_harness.py`)
- **Scoring is exact string match.** The response, with periods removed and lower-cased, must equal the answer letter. Any response containing reasoning is scored wrong.
- **Settings**: temperature 0; `max_output_tokens=500` for Gemini, 300 for OpenAI. No system prompt, no thinking configuration.
- **Images are interleaved** into the question text at the character offsets in `visual_indices`; when all offsets are zero the images go first.
- It reports overall, single-image, multi-image and per-question-type accuracy.
- An API error on a question is skipped and the question is dropped from the denominator.

### Measured from the dataset (this wiki's analysis of `erqa.tfrecord`)

| Question type | n | Share | Multi-image |
|---|---:|---:|---:|
| Spatial Reasoning | 84 | 21.0% | 27 |
| Action Reasoning | 72 | 18.0% | 6 |
| Trajectory Reasoning | 66 | 16.5% | 2 |
| State Estimation | 55 | 13.8% | 8 |
| Task Reasoning | 38 | 9.5% | 22 |
| Multi-view Reasoning | 37 | 9.2% | 37 |
| Pointing | 34 | 8.5% | 2 |
| Other | 14 | 3.5% | 9 |
| **Total** | **400** | | **113 (28.3%)** |

- **630 images**, all JPEG; 287 questions have one image, and one has 16. The 28.3% multi-image share matches the report's "28%."
- **Options**: 380 questions have four choices, 14 have two, 4 have three, one has six, and one did not parse. Chance accuracy is about **25.9%**.
- **Answer key**: A 123, B 96, C 98, D 83. Always answering "A" scores **30.8%**.
- **Every question ends with the same instruction**: "Please answer directly with only the letter of the correct option and nothing else." The direct-answer prompt is part of the data.
- **Image placement**: 370 questions put all images before the text; 30 interleave them.
- Example, Task Reasoning: "Was the task successful: put carrot in plate. Choices: A. No. B. Yes."

### From the issue tracker
- Eight items, two closed.
- **#3 "Evaluation with CoT"** (July 2025, no reply): a user appending the report's chain-of-thought prompt measured 46.5% where the report gives 50.3% for the same model, and asks how the prompt was applied, "since the implementation of the CoT prompt is not released in this code."
- **#5** (April 2026, no reply) asks for the original Gemini and GPT responses in order to reproduce the report's scores.
- #6 (July 2026) proposes integration into a third-party evaluation framework.
- Issue #3 cites the report as arXiv 2503.20020.

## What this changes

> [!warning] Published ERQA scores are not one measurement
> The released harness cannot produce a chain-of-thought or "thinking" score: the data tells the model to answer with a letter only, and the scorer marks anything else wrong. The report's CoT column (up to 54.8) therefore used a prompt and an answer-extraction step that were never released, and an outside attempt to reproduce one such number fell 3.8 points short. Later vendor figures, including [Gemini 4 Argon's](../entities/gemini-4-argon.md) 87% "using pure reasoning," necessarily used some other harness too. Treat any ERQA number without a stated prompt, thinking budget and extraction rule as vendor-reported.

- **The floor is higher than 25%.** With the answer-key skew, a constant guess scores 30.8%. Claude 3.5 Sonnet's 35.5 and GPT-4o-mini's 37.3 in the original table sit about five to seven points above that.
- **Per-category results are fragile.** Pointing has 34 questions and Multi-view 37. A 95% interval on a category that size is roughly ±16 points, so category breakdowns from a single run say little.
- **Dropped questions inflate scores silently.** The harness removes failed API calls from the denominator and prints the total, so a reader must check that it says 400.
- **The benchmark is frozen and public.** Twenty months of availability with a fixed 400 questions makes contamination of later models' training data a live possibility. The repository offers no held-out split.

## Entities mentioned
- [ERQA](../entities/erqa.md) · [Google DeepMind](../entities/google-deepmind.md) · [Gemini Robotics](../entities/gemini-robotics.md)

## Concepts touched
- [Embodied-reasoning VLMs](../concepts/learning/embodied-reasoning-vlms.md)
- [Chain of thought](../concepts/learning/chain-of-thought.md): the unreleased CoT protocol
- [Robot policy evaluation](../concepts/robotics/robot-policy-evaluation.md): harness details as a confound

## Open questions
- The CoT prompt placement and answer-extraction rule behind the report's Table 2.
- Which harness produced the 2026 scores quoted by Unitree and by Google for Argon.
- Whether any maintained leaderboard exists elsewhere. None is linked from the repository.
- Image provenance per question. The report names the source datasets; the TFRecord carries no per-image attribution.

## Related sources
- [Gemini Robotics: Bringing AI into the Physical World](gemini-robotics-report-2025.md): the report that introduces the benchmark and reports the first scores.
- [Gemini 4 Argon for Robotics](gemini-4-argon-robotics-blog.md) · [UnifoLM-WLA-1 project page](unifolm-wla-1-project-page.md): later scores.
