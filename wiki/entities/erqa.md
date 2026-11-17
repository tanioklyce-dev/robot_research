---
title: ERQA (Embodied Reasoning Question Answering)
type: entity
subtype: benchmark
created: 2026-11-17
updated: 2026-11-17
sources: 5
tags: [erqa, benchmark, embodied-reasoning, vqa, google-deepmind, spatial-reasoning]
---

**ERQA** — [Google DeepMind](google-deepmind.md)'s open benchmark for embodied reasoning in vision-language models, introduced with the first [Gemini Robotics](gemini-robotics.md) report in March 2025 ([report](../sources/gemini-robotics-report-2025.md)).

## What it is
- **400 multiple-choice VQA questions**, all manually labeled, across spatial reasoning, trajectory reasoning, action reasoning, state estimation, pointing, multi-view reasoning and task reasoning.
- **28% of questions use more than one image**, and those "tend to be more challenging."
- Images are DeepMind's own or drawn from OXE, UMI data, MECCANO, HoloAssist and EGTEA Gaze+.
- Scored as multiple-choice accuracy. Repository: `github.com/embodiedreasoning/ERQA` ([source page](../sources/erqa-github.md)), CC BY 4.0, unchanged since 2025-03-12.
- The authors' motivation: existing benchmarks "highlight more atomic capabilities (e.g., object recognition, counting, localization)" and miss what an agent acting in the world needs.

## Composition and scoring (from the released data and harness)

Measured from the dataset file ([repository source page](../sources/erqa-github.md)):

| Question type | n |
|---|---:|
| Spatial Reasoning | 84 |
| Action Reasoning | 72 |
| Trajectory Reasoning | 66 |
| State Estimation | 55 |
| Task Reasoning | 38 |
| Multi-view Reasoning | 37 |
| Pointing | 34 |
| Other | 14 |

- 630 JPEG images; 113 questions (28.3%) have more than one, and one has 16.
- 380 of 400 questions have four options. Chance is about 25.9%, and always answering "A" scores **30.8%** because the answer key is skewed.
- Every question ends with an instruction to reply with the letter only, and the released harness scores by **exact match** at temperature 0. A response that reasons out loud is marked wrong.
- The chain-of-thought prompt and answer extraction behind the report's higher scores were not released. An outside user reported 46.5% where the report gives 50.3% and received no reply.

## Scores the wiki holds

| When | Model | ERQA | Source |
|---|---|---:|---|
| 2025-02 | Claude 3.5 Sonnet | 35.5 (45.8 with CoT) | [GR report](../sources/gemini-robotics-report-2025.md) |
| 2025-02 | GPT-4o | 47.0 (50.5 with CoT) | same |
| 2025-02 | Gemini 2.0 Pro Experimental | 48.3 (**54.8** with CoT) | same |
| 2026 | UnifoLM-ER-1-4B | 50.0 | [Unitree](../sources/unifolm-wla-1-project-page.md) |
| 2026 | Hy-Embodied-VLM | 60.8 | Unitree's table |
| 2026 | Gemini 3.1 Pro | 65.2 | Unitree's API tests |
| 2026 | [GPT-6 Astra](gpt-6-astra.md) | 77.7 | Unitree's API tests |
| 2026-10 | [Gemini 4 Argon](gemini-4-argon.md) | **87** | [Argon blog](../sources/gemini-4-argon-robotics-blog.md), vendor-stated, no table |

> [!note] Rows are not on one harness
> The 2025 rows are DeepMind's, the middle rows are Unitree's own runs or copied figures, and the Argon figure is a single number in a blog post "using pure reasoning." Chain-of-thought prompting alone moved 2025 scores by 3 to 10 points, so thinking budget is a confound across rows. The public harness cannot score a reasoning response at all, so every row above the direct-answer 2025 column used a protocol that is not published.

> [!note] Four hundred questions is a small test
> At n = 400 a score near 50% has a 95% interval of about ±5 points. The three-way spread among GPT-4o, Gemini 2.0 Flash and Gemini 2.0 Pro in the original table (46.3 to 48.3) is inside it. The jump from the 50s to 87 is not. Per-category results are weaker still: Pointing has 34 questions and Multi-view 37, about ±16 points each.

## Why it matters here
ERQA is the number vendors now quote to claim a model can serve as a robot's planner, the role described in [embodied-reasoning VLMs](../concepts/learning/embodied-reasoning-vlms.md). The original report also gave the reason to care: on real and simulated ALOHA 2 tasks, the model with better embodied reasoning nearly doubled zero-shot control success (27% to 53%). That link has not been re-measured for later, higher-scoring models in any source the wiki holds.

## Related
- [Embodied-reasoning VLMs](../concepts/learning/embodied-reasoning-vlms.md) · [Gemini Robotics](gemini-robotics.md)
- [Molmo2-ER](molmo2-er.md) — ERQA is one of the 13 benchmarks in its reported average.

## Mentioned in
- [Gemini Robotics: Bringing AI into the Physical World](../sources/gemini-robotics-report-2025.md) — introduces the benchmark.
- [embodiedreasoning/ERQA (GitHub)](../sources/erqa-github.md) — the dataset, the exact-match harness, and the unanswered reproduction issues.
- [Gemini Robotics 1.5 tech report](../sources/gemini-robotics-1-5-report.md) — one of 15 benchmarks in its ER score.
- [UnifoLM-WLA-1 project page](../sources/unifolm-wla-1-project-page.md) — third-party scores for open and proprietary models.
- [Gemini 4 Argon for Robotics](../sources/gemini-4-argon-robotics-blog.md) — 87%.

## Open questions
- A like-for-like leaderboard with harness and thinking budget stated. The repository has none.
- Contamination: the 400 questions have been public and fixed since March 2025, with no held-out split.
- Whether ERQA gains above about 55 still predict control success.
