---
title: "AI Coding on Jetson with Claude Code and NVIDIA Skills (JetsonHacks)"
type: source
url: https://www.youtube.com/watch?v=swH7ogB2mz8
author: JetsonHacks (YouTube channel)
published: 2026-07-07
ingested: 2026-07-16
format: youtube-video
tags: [jetson, claude-code, agent-skills, vs-code, remote-ssh, edge-ai, jetpack, tutorial, jetson-device-skills, workflow]
---

## Summary

A ~12.7-minute **practitioner walkthrough** from the JetsonHacks channel showing how to turn VS Code into "an AI coding workstation for Jetson": **[Claude Code](../concepts/agents/agent-skills.md) in VS Code + [Jetson Device Skills](jetson-device-skills-github.md) + remote SSH development**, using a **Jetson AGX Orin 64 GB as the host** to program a **headless Jetson Orin Nano** over SSH. The video is the hands-on companion to the [Jetson Device Skills repo](jetson-device-skills-github.md) and confirms two ecosystem facts: **JetPack 7.2 introduces the Jetson-specific skills**, and (per an official JetsonHacks poll) **Claude Code is the most popular coding agent among the channel's audience by a 2:1 margin**.

## Key claims (from auto-caption transcript)

- **Workflow**: install Microsoft VS Code (ARM64 `.deb`) on the Jetson host; add Anthropic's official **Claude Code VS Code extension**; edit on the host, run on the Jetson; scale to a **headless Orin Nano over remote SSH**.
- **Agent choice**: JetsonHacks poll → **Claude Code most popular by 2:1**. Presenter notes OpenAI Codex feels more token-efficient / "generous," and that he runs the **lowest paid tier of both** so they can "argue with each other." Both have **5-hour + weekly spend limits**.
- **Installing Device Skills the agentic way**: rather than manually cloning, have a chatbot **research the tool, then draft a prompt** telling the agent to install it — hand that prompt to **Claude Code**, which clones and runs the [Jetson Device Skills](jetson-device-skills-github.md) installer. ("Having chatbots and agents draft prompts is the first aha moment.")
- **JetPack 7.2** introduces skills for the Jetson itself **plus** skills to help build **board-support packages**.
- **Caution (the thesis of the video)**: *"The agent works for you. You do not work for it… If you fail to [direct it], the agent will go down a path from which you cannot recover. It can build slop an order of magnitude faster than you can throw it out. Time spent upfront specifying and planning has a huge payback."*
- **On LLM web research**: good at searching + summarizing, but *"the LLM is built to provide answers, not the correct answer"* — use it as a starting point, follow the provided references, verify. (Example used: Ollama trouble on JetPack 7.2, searched against the Jetson forums.)

## Entities mentioned

- [Jetson Device Skills](../entities/jetson-device-skills.md)
- [Jetson Orin Nano](../entities/jetson-orin-nano.md), [Jetson Thor](../entities/jetson-thor.md) (context), [JetPack](../entities/jetpack.md)

## Concepts touched

- [Agent skills (portable SKILL.md)](../concepts/agents/agent-skills.md)
- [LLM-agent architecture](../concepts/agents/llm-agent-architecture.md)

## Open questions

- The video demos install/diagnostics but not a full robot-control loop on the Jetson — how far do the skills carry into an actual [LeRobot](../entities/lerobot.md)/policy deployment session?
