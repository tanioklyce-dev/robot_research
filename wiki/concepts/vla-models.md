---
title: VLA models
type: concept
created: 2026-05-06
updated: 2026-05-08
sources: 8
tags: [vla, vision-language-action, foundation-model, robotics]
---

**Vision-Language-Action (VLA) models** are robot foundation models that take visual input plus a language instruction and emit low-level actions for a robot to execute. The dominant model class powering "agentic" robotics in 2026.

## Definition
A VLA combines a vision encoder, a language encoder/decoder (often an LLM backbone), and an action head. Trained on large mixed datasets — robot teleoperation, human videos, simulation rollouts. Inference loop: image + text instruction → action token sequence → robot motors.

## Notable VLAs (2026)
- **[NVIDIA GR00T](../entities/nvidia-groot.md)** N1.6 GA / N1.7 EA — 3B-parameter open VLA built on a Cosmos-Reason2-2B backbone; pretrained on ~20,854 hours of egocentric human video ([Top 10 Physical AI Models 2026](../sources/top-10-physical-ai-models-2026.md), [NVIDIA Newton Contact-Rich Manipulation Blog](../sources/nvidia-newton-contact-rich-manipulation-blog.md)).
- **Pi series** — Physical Intelligence's VLAs, benchmarked by [AGIBOT Genie Sim 3.0](../entities/agibot-genie-sim.md).
- **GO-2 series** — also benchmarked by Genie Sim.
- **SmolVLA** — runs on consumer hardware (single RTX, even MacBooks).
- **LingBot-VLA** — Ant Group's foundation model for real-world manipulation.

## Adjacent: utility models / non-language-conditioned policies
- **[Robot Utility Models](../entities/robot-utility-models.md)** (NYU / Meta) — visuomotor behavior cloning achieving zero-shot ~90% success on novel environments **without language conditioning**. The "utility model" framing is a deliberate distinction from VLAs but solves an overlapping problem ([Robot Utility Models Project Page](../sources/robot-utility-models-website.md)).
- **[stretch_ai](../entities/stretch-ai.md)'s LLM agent** — uses an LLM to emit tool calls, *not* low-level actions. A VLA-substitute architecture for high-level planning, paired with classical perception/manipulation primitives ([Stretch AI LLM Agent Documentation](../sources/stretch-ai-llm-agent-docs.md), [LLM-agent architecture](llm-agent-architecture.md)).

## Why simulators matter for VLAs
- **Pretraining data** — synthetic rollouts at massive scale (e.g. Genie Sim's 10k hours).
- **Evaluation** — standardized scenarios for comparable benchmarks (Genie Sim's 100k+ scenarios; ManiSkill-HAB; RoboCasa365).
- **Closed-loop training** — RL fine-tuning of action heads in fast GPU-parallel environments (Isaac Lab, MuJoCo Playground, Genesis).

## Related
- [Sim-to-real transfer](sim-to-real-transfer.md) — the bridge from simulator-trained policies to real robots.
- [World-model simulators](world-model-simulators.md) — alternate paradigm for VLA training environments.

## Mentioned in
- [AGIBOT Genie Sim 3.0 Announcement](../sources/agibot-genie-sim-3-announcement.md)
- [Top 10 Physical AI Models 2026](../sources/top-10-physical-ai-models-2026.md)
- [Genesis Project Page](../sources/genesis-project-page.md)
- [NVIDIA Newton Contact-Rich Manipulation Blog](../sources/nvidia-newton-contact-rich-manipulation-blog.md)
- [Robot Utility Models Project Page](../sources/robot-utility-models-website.md)
- [Stretch AI LLM Agent Documentation](../sources/stretch-ai-llm-agent-docs.md)
