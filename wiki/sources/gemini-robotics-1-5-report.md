---
title: "Gemini Robotics 1.5 — Pushing the Frontier of Generalist Robots with Embodied Reasoning, Thinking, and Motion Transfer (tech report)"
type: source
url: https://deepmind.google/discover/blog/gemini-robotics/
fetch_url: https://storage.googleapis.com/deepmind-media/gemini-robotics/Gemini-Robotics-1-5-Tech-Report.pdf
author: Gemini Robotics Team, Google DeepMind
published: 2025 (Google DeepMind technical report; no arXiv id on file)
ingested: 2026-07-04
local_path: raw/Gemini-Robotics-1-5-Tech-Report.pdf
sha256: b41a2f732f4755c7564b973bcc6ff8aebf3bb9a9f163328437e89533d372b2f4
format: pdf (26 pp.)
tags: [gemini-robotics, google-deepmind, vla, embodied-reasoning, thinking, motion-transfer, cross-embodiment, agentic, safety, aloha, franka, apollo]
---

## Summary

The primary technical report for **[Gemini Robotics 1.5](../entities/gemini-robotics.md)** — the first deep source in the wiki for the DeepMind robotics line (previously only the Spot+ER-1.5 blog). A **two-model family**: **GR 1.5** (a multi-embodiment VLA) + **GR-ER 1.5** (a SOTA embodied-reasoning VLM orchestrator), both built on **Gemini 2.5**. Three claimed innovations: **Motion Transfer** (cross-embodiment skill transfer, zero-shot), **Embodied Thinking** ("think before acting" — interleaves actions with natural-language reasoning traces), and **GR-ER 1.5** setting new embodied-reasoning SOTA. Composed as an agentic system (ER orchestrator + VLA action model) for long-horizon tool-using tasks. Successor to Gemini Robotics 1.0 (arXiv 2503.20020).

## Key claims

### Architecture (§2.1)
- Both models inherit Gemini 2.5's multimodal world knowledge (exact sizes undisclosed).
- **GR-ER 1.5** (VLM orchestrator): native tool calling (Search, Code, Function), outputs 2D pointing / trajectories / segmentation / task-progress; produces "ER thinking traces"; plans, does success detection, decides when to advance.
- **GR 1.5** (VLA action model): open-vocab instruction → low-level actions; can reason before emitting an action ("Thinking VLA"); outputs a "next step" + a "motion description" per step; exposed to the orchestrator as a natural-language tool.
- **Embodied Thinking**: converts observations into language "thoughts" appended to context before acting; two-step (high-level instruction → short-horizon thought → actions). Emergent implicit success detection + error-recovery replanning.
- **Motion Transfer (MT)**: architecture + training recipe unifying heterogeneous multi-embodiment data → zero-shot skill transfer across dissimilar robots.

### Embodiments & data (§2.2)
- Multi-embodiment data on **[ALOHA](../entities/aloha.md) 2, bi-arm [Franka](../entities/franka-panda.md) (Research 3), and [Apollo](../entities/apptronik-apollo.md) humanoid**; plus internet text/image/video. **Same GR 1.5 checkpoint controls all three robots out-of-the-box** — no robot-specific post-training.
- Evaluation: A/B/n on real robots; **>90% of dev-eval episodes were in [MuJoCo](../entities/mujoco.md) sim**; primary metric = continuous progress score; 230-task benchmark.

### Results (hard numbers)
- **Generalization (progress scores)**: GR 1.5 beats Gemini Robotics 1.0 and On-Device across ALOHA/Franka/Apollo on in-distribution + instruction/action/visual/task generalization (e.g. ALOHA Task-Gen 0.70 vs 0.44; Franka Visual-Gen 0.77 vs 0.09 vs GRoD).
- **Cross-embodiment zero-shot** (trained only on another robot): success ALOHA 0.43 / Franka 0.58 / Humanoid 0.40 — vs near-0 for single-embodiment/1.0 baselines. MT benefit weakens as embodiment gap grows (humanoid hardest).
- **Thinking helps acting** (multi-step): ALOHA **0.55 vs 0.26** (thinking on/off); Humanoid 0.67 vs 0.51.
- **Embodied reasoning**: GR-ER 1.5 tops a 15-benchmark ER score (BLINK, ERQA, RoboSpatial, Where2Place, …) while retaining generality — expands the Pareto frontier past Gemini 2.5 Pro/Flash, GPT-5. Pointing avg **52.6%** vs GPT-5 30.8%. Improves with thinking-token budget (inference-time scaling).
- **Agentic long-horizon** (GR-ER 1.5 orchestrator + GR 1.5): 8 tasks frequently ~0.80 progress; **total failure 22% vs 44.5%** for a Gemini-2.5-Flash orchestrator — biggest gain in planning. Lesson: an off-the-shelf VLM + strong VLA is insufficient; dedicated embodied reasoning for planning is critical.

### Safety (§6)
- Multi-layer: semantic safety reasoning, "think about safety before acting," ISO 15066 collaborative-robot alignment. Released **ASIMOV-2.0** benchmark + **Auto-Red-Teaming (ART)** (attacker/target/autorater game surfacing ER hallucinations). Thinking-enabled GR-ER 1.5 more robust to obfuscation/hallucination/content-safety attacks.

## Entities mentioned
- [Gemini Robotics](../entities/gemini-robotics.md) — this deepens it. [Google DeepMind](../entities/google-deepmind.md). Backbone Gemini 2.5.
- Robots: [ALOHA](../entities/aloha.md) 2, [Franka](../entities/franka-panda.md), [Apptronik Apollo](../entities/apptronik-apollo.md).
- Compared peers: [GR00T N1](../entities/nvidia-groot.md), [π0.5](../entities/pi-zero-6.md), RT-2, GPT-5/GPT-5-mini, Gemini 2.5 Pro/Flash.

## Concepts touched
- [VLA models](../concepts/learning/vla-models.md) — GR 1.5 is a multi-embodiment VLA; the **Embodied Thinking** = an explicit System-2-before-action, and the **agentic orchestrator + action-model** split maps to [LLM-agent architecture](../concepts/agents/llm-agent-architecture.md).
- [Chain of thought](../concepts/learning/chain-of-thought.md) — embodied thinking traces / inner monologue; inference-time-compute scaling.
- Cross-embodiment / Motion Transfer — the DeepMind analogue of [Open X-Embodiment](../entities/open-x-embodiment.md)-style co-training, with a dedicated transfer recipe.
- [AI safety and alignment](../concepts/safety/ai-safety-alignment.md) — ASIMOV-2.0, ART, ISO 15066.

## Open questions
- **Dexterity ~ previous generation** (stated weakness); RL + new architectures are future work.
- Exact model sizes / action-decoder details undisclosed; appendices not in this PDF.
- Next step: scaling to **non-action data** (human + synthetic video without action labels) — architecture already supports it (the same bet as [GR00T](../entities/nvidia-groot.md)'s neural trajectories + [FLARE](../concepts/world-models/flare.md)'s human-video co-training).
- No arXiv id on the PDF; the DeepMind blog is the citable landing page.
