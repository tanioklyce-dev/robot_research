---
title: VLA models
type: concept
created: 2026-05-06
updated: 2026-05-07
sources: 6
tags: [vla, vision-language-action, foundation-model, robotics]
---

**Vision-Language-Action (VLA) models** are robot foundation models that take visual input plus a language instruction and emit low-level actions for a robot to execute. The dominant model class powering "agentic" robotics in 2026.

## Definition
A VLA combines a vision encoder, a language encoder/decoder (often an LLM backbone), and an action head. Trained on large mixed datasets — robot teleoperation, human videos, simulation rollouts. Inference loop: image + text instruction → action token sequence → robot motors.

## Notable VLAs (2026)
- **[[nvidia-groot|NVIDIA GR00T]]** N1.6 GA / N1.7 EA — 3B-parameter open VLA built on a Cosmos-Reason2-2B backbone; pretrained on ~20,854 hours of egocentric human video ([[top-10-physical-ai-models-2026|Top 10 Physical AI Models 2026]], [[nvidia-newton-contact-rich-manipulation-blog|NVIDIA Newton Contact-Rich Manipulation Blog]]).
- **Pi series** — Physical Intelligence's VLAs, benchmarked by [[agibot-genie-sim|AGIBOT Genie Sim 3.0]].
- **GO-2 series** — also benchmarked by Genie Sim.
- **SmolVLA** — runs on consumer hardware (single RTX, even MacBooks).
- **LingBot-VLA** — Ant Group's foundation model for real-world manipulation.

## Adjacent: utility models / non-language-conditioned policies
- **[[robot-utility-models|Robot Utility Models]]** (NYU / Meta) — visuomotor behavior cloning achieving zero-shot ~90% success on novel environments **without language conditioning**. The "utility model" framing is a deliberate distinction from VLAs but solves an overlapping problem ([[robot-utility-models-website|Robot Utility Models Project Page]]).
- **[[stretch-ai|stretch_ai]]'s LLM agent** — uses an LLM to emit tool calls, *not* low-level actions. A VLA-substitute architecture for high-level planning, paired with classical perception/manipulation primitives ([[stretch-ai-llm-agent-docs|Stretch AI LLM Agent Documentation]], [[llm-agent-architecture|LLM-agent architecture]]).

## Why simulators matter for VLAs
- **Pretraining data** — synthetic rollouts at massive scale (e.g. Genie Sim's 10k hours).
- **Evaluation** — standardized scenarios for comparable benchmarks (Genie Sim's 100k+ scenarios; ManiSkill-HAB; RoboCasa365).
- **Closed-loop training** — RL fine-tuning of action heads in fast GPU-parallel environments (Isaac Lab, MuJoCo Playground, Genesis).

## Related
- [[sim-to-real-transfer|Sim-to-real transfer]] — the bridge from simulator-trained policies to real robots.
- [[world-model-simulators|World-model simulators]] — alternate paradigm for VLA training environments.

## Mentioned in
- [[agibot-genie-sim-3-announcement|AGIBOT Genie Sim 3.0 Announcement]]
- [[top-10-physical-ai-models-2026|Top 10 Physical AI Models 2026]]
- [[genesis-project-page|Genesis Project Page]]
- [[nvidia-newton-contact-rich-manipulation-blog|NVIDIA Newton Contact-Rich Manipulation Blog]]
- [[robot-utility-models-website|Robot Utility Models Project Page]]
- [[stretch-ai-llm-agent-docs|Stretch AI LLM Agent Documentation]]
