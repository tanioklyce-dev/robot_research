---
title: Jetson Device Skills
type: entity
subtype: software
created: 2026-07-16
updated: 2026-07-16
sources: 2
tags: [nvidia, jetson, agent-skills, claude-code, edge-ai, jetpack, tooling, cursor, codex]
---

# Jetson Device Skills

**Jetson Device Skills** (`NVIDIA-AI-IOT/jetson-device-skills`) — NVIDIA's catalog of **[Agent Skills](../concepts/agents/agent-skills.md)** that teach an AI coding agent (Claude Code / Cursor / Codex) how to inspect and operate a **live [Jetson](jetson-thor.md) device** after boot. Introduced with **[JetPack](jetpack.md) 7.2**; the productized form of the "Jetson Agent Skills" feature ([Thor T3000/T2000 blog](../sources/nvidia-jetson-thor-t3000-t2000-blog.md)).

## What it is

Portable `SKILL.md` files (frontmatter for agent discovery) + helper scripts the agent runs to fetch real device data, then reasons over. Without them, agents give **generic Linux / discrete-GPU advice that doesn't apply to Jetson**. Installed via `./install.sh` into `~/.claude/skills`, `~/.cursor/skills`, `~/.codex/skills`, `~/.agents/skills`.

## The eight skills

| Skill | Purpose |
|---|---|
| `jetson-diagnostic` | Device health snapshot (memory / GPU / thermal / power / storage) |
| `jetson-memory-audit` | DRAM/NvMap usage + reclamation verification |
| `jetson-headless-mode` | Disable desktop/services for edge nodes |
| `jetson-inference-mem-tune` | Runtime tuning for vLLM / SGLang / llama.cpp / TensorRT |
| `jetson-llm-serve` | Serving recipes (vLLM, SGLang) |
| `jetson-llm-benchmark` | Structured cross-framework metrics |
| `jetson-package` | Jetson-specific packaging guidance |
| `jetson-speculative-decoding` | EAGLE-3 / draft-model guidance for vLLM |

Sibling repo **`jetson-bsp-skills`** covers board-support-package customization *before* flashing.

## License

Dual **CC-BY-4.0** (docs) + **Apache-2.0** (code).

## Why it matters in this wiki

The wiki's first concrete instance of **on-device [agent skills](../concepts/agents/agent-skills.md) for robotics hardware** — the same portable-`SKILL.md` pattern that [NVIDIA Halos](nvidia-halos.md) ships for deployment (`warehouse-deploy` / `halos-deploy`) and that FRC teams ([HighTide](team-4414-hightide.md)) ship for their codebases. It closes the loop between the wiki's Claude-Code-agentic thread and its Jetson-onboard-compute thread: the box you deploy a [LeRobot](lerobot.md)/[VLA](../concepts/learning/vla-models.md) policy onto is now agent-manageable.

## Mentioned in

- [Jetson Device Skills GitHub](../sources/jetson-device-skills-github.md) — the repo + Jetson AI Lab tutorial
- [AI Coding on Jetson with Claude Code (JetsonHacks)](../sources/jetsonhacks-ai-coding-jetson-claude-code.md) — practitioner demo

## Related

- [Agent skills (portable SKILL.md)](../concepts/agents/agent-skills.md), [LLM-agent architecture](../concepts/agents/llm-agent-architecture.md)
- [Jetson Thor](jetson-thor.md), [Jetson Orin Nano](jetson-orin-nano.md), [JetPack](jetpack.md), [jetson-containers](jetson-containers.md)
