---
title: "Jetson Device Skills (NVIDIA-AI-IOT/jetson-device-skills)"
type: source
url: https://github.com/NVIDIA-AI-IOT/jetson-device-skills
author: NVIDIA (NVIDIA-AI-IOT)
published: 2026 (JetPack 7.2 era)
ingested: 2026-07-16
secondary_url: https://www.jetson-ai-lab.com/tutorials/getting-started-with-jetson/#ai-assisted-workflows-with-jetson-device-skills
license: CC-BY-4.0 (docs) + Apache-2.0 (code)
tags: [nvidia, jetson, agent-skills, claude-code, edge-ai, jetpack, tooling, cursor, codex, llm-serving]
---

## Summary

**Jetson Device Skills** is NVIDIA's catalog of **[Agent Skills](../concepts/agents/agent-skills.md)** for operating a Jetson device *after boot* — portable `SKILL.md` instruction sets paired with helper scripts that let an AI coding agent (Claude Code, Cursor, Codex) inspect and manage **live Jetson hardware**. The core rationale: without device-specific knowledge, agents give "**generic Linux or discrete-GPU advice that does not apply to Jetson**" ([Jetson AI Lab getting-started](https://www.jetson-ai-lab.com/tutorials/getting-started-with-jetson/)). Introduced with **JetPack 7.2**. This is the productized form of the "**Jetson Agent Skills**" feature the wiki already noted from the [Thor T3000/T2000 blog](nvidia-jetson-thor-t3000-t2000-blog.md) (memory-optimization automation, up to 15 GB reclaimed).

## Key claims

- **What a skill is**: a `SKILL.md` file with frontmatter metadata (so the agent can discover it) + helper scripts the agent invokes to fetch live device data, then reasons over the returned output.
- **Install target dirs**: skills are linked into agent-specific directories — `~/.claude/skills`, `~/.cursor/skills`, `~/.codex/skills`, `~/.agents/skills`. Install via `git clone` + `./install.sh` (flags: `--copy`, `--targets`, `--force`); restart the agent session afterward.
- **Eight bundled skills**:
  - `jetson-diagnostic` — device health snapshot (memory, GPU, thermal, power, storage)
  - `jetson-memory-audit` — DRAM/NvMap usage + reclamation verification
  - `jetson-headless-mode` — disable desktop/background services for edge nodes
  - `jetson-inference-mem-tune` — runtime recommendations for vLLM / SGLang / llama.cpp / TensorRT
  - `jetson-llm-serve` — serving recipes for vLLM and SGLang
  - `jetson-llm-benchmark` — structured metrics across inference frameworks
  - `jetson-package` — Jetson-specific packaging guidance
  - `jetson-speculative-decoding` — EAGLE-3 / draft-model guidance for vLLM
- **License**: dual CC-BY-4.0 (docs) + Apache-2.0 (code).
- **Sibling repo**: `jetson-bsp-skills` — board-support-package customization *before* flashing (vs. this repo's *post-boot* focus).
- **Verification prompt** (from the tutorial): *"Use the Jetson diagnostic skill to inspect this device and summarize the model, JetPack/L4T version, memory, GPU usage, thermals, and power mode."*

## Entities mentioned

- [Jetson Device Skills](../entities/jetson-device-skills.md) — this project
- [Jetson Thor](../entities/jetson-thor.md) / [Jetson Orin Nano](../entities/jetson-orin-nano.md) — the target hardware
- [JetPack](../entities/jetpack.md) — 7.2 introduces the skills

## Concepts touched

- [Agent skills (portable SKILL.md)](../concepts/agents/agent-skills.md) — the pattern this instantiates
- [LLM-agent architecture](../concepts/agents/llm-agent-architecture.md) — the agent side

## Open questions

- Are the skills hardware-gated (Thor vs Orin), or do the diagnostic scripts adapt at runtime? The repo documents no hardware restriction.
- How do these interact with [jetson-containers](../entities/jetson-containers.md) — complementary (device-side) or overlapping?
