---
title: AgenticROS GitHub (agenticros/agenticros)
type: source
url: https://github.com/agenticros/agenticros
author: AgenticROS org (maintainers not publicly listed)
published: 2026 (no formal releases; ~125 commits on main)
ingested: 2026-07-05
license: Apache-2.0
format: GitHub repository + docs/
tags: [agenticros, ros2, mcp, openclaw, hermes-agent, nemoclaw, fleet, skills, zenoh, typescript, agent-robot-bridge]
---

# AgenticROS GitHub (agenticros/agenticros)

## Summary

**AgenticROS** is an Apache-2.0 open-source integration layer that turns [ROS 2](../entities/ros2.md) robots into agent-native machines: one shared TypeScript runtime exposes a robot's capabilities to **six AI-agent platforms** — [OpenClaw](../entities/openclaw.md) (flagship, native gateway plugin), [NemoClaw](../entities/nemoclaw.md) (sandboxed), Anthropic Claude (Code/Desktop/Dispatch via MCP), OpenAI Codex CLI (same MCP server), [Hermes Agent](../entities/hermes-agent.md) (MCP client), and Google Gemini CLI (function calling). It is the first **community-maintained, multi-platform ROS 2 ↔ [MCP](../concepts/agents/llm-agent-architecture.md#mcp--model-context-protocol)/agent bridge** the wiki has tracked, and it directly answers the open question posed in [OpenClaw vs Hermes as robot brain](../syntheses/agents/openclaw-vs-hermes-as-robot-brain.md): *"Is there a community ros-mcp-server yet?"* — there is now.

## Key claims

**Architecture** (docs/architecture.md):
- Layered design: agent platforms → platform adapters → shared TypeScript runtime (`@agenticros/transport`, `packages/core`) → transport layer → ROS 2 workspace/hardware.
- **Four deployment modes / transports** behind one `RosTransport` interface: (A) same-machine local DDS via rclnodejs (~ms latency), (B) LAN via `rosbridge_server` WebSocket, (C) cloud via WebRTC data channels with STUN/TURN (10–100 ms), (D) **Zenoh** (`rmw_zenoh_cpp` + `zenoh-ts` router, no rosbridge needed).
- Monorepo: TypeScript 79.6% / Python 8.4%; Node.js ≥ 20 is the only hard requirement; entry point `npx agenticros` (interactive menu + scriptable subcommands). ROS 2 Humble or Jazzy; TurtleBot3 Gazebo sim bringup + Docker Compose included.

**Capability manifests** (docs/skills.md):
- Robots advertise **typed verbs** (e.g. `drive_base`, `take_snapshot`, `find_object`, `follow_person`) that agents plan against instead of raw topics. Each capability declares `id`, `verb`, `description`, `inputs`/`outputs` (typed), **`interruptible`** (can be stopped mid-stream), and **`blocks_base`** (claims exclusive control of base motion). The manifest doubles as an agent card.
- Skills are npm packages exporting `registerSkill(api, config, context)`; scaffolded with `npx agenticros create-skill`; published to a marketplace at skills.agenticros.com.

**Missions and planning**:
- `run_mission` executes **declarative step graphs** with template-based data flow: outputs of any step feed later steps via `{{stepId.outputs.field}}` references — a detection wires straight into the next motion command with no glue code.
- **Natural-language goals compile deterministically** (rule-based, no LLM required): "find a chair and drive toward it" → multi-step mission. Compile errors return the recognized verb list so the agent can self-correct.
- Mission cancellation via in-process tokens.

**Fleet support**:
- `ros2_find_robots_for({capability, kind?, online?})` queries the fleet by capability (e.g. "an AMR that can `follow_person` and is online").
- Each robot publishes a **1 Hz heartbeat on `<ns>/agenticros/robot_info`** for online-status tracking; `cmd_vel` is namespaced per robot; a single mission can route steps to different robots.

**Safety**:
- A **safety validator hook (`before_tool_call`)** enforces velocity limits and workspace bounds before execution.
- **`/estop` bypasses the AI entirely** — same out-of-band-stop conclusion as the [ros2-mcp-server design](../syntheses/projects/ros2-mcp-server-design.md) reached independently.
- Alongside semantic verbs it also exposes a **raw ROS command surface** (`ros2_publish`, `ros2_subscribe_once`, `ros2_service_call`, `ros2_action_goal`) — broader (and riskier) than a semantic-tools-only boundary, mitigated by the validator hooks.

**Memory**:
- Optional cross-adapter persistent memory: `memory_remember` / `memory_recall` / `memory_forget` / `memory_status`, backed by Mem0 (vector store at `~/.mem0/vector_store.db`) or keyword-based local JSON, **namespaced by robot ID**; mission steps write transcripts tagged by capability and status for cross-agent collaboration.

**Maturity** (as of ingest):
- **112 stars, 14 forks, ~125 commits, no formal releases**; active development; comprehensive docs/ (architecture, skills, teleop web app, Zenoh, NemoClaw, Codex/Hermes setup, memory, cameras/RealSense).
- **GitHub org has no public members** — maintainer identity/affiliation unknown. Website: agenticros.com.

> [!note] Credibility caveat
> Anonymous maintainers + no releases + a young star count mean adoption risk is real despite the polished docs. Apache-2.0 mitigates (fork/vendor is always possible).

## Entities mentioned

- [AgenticROS](../entities/agenticros.md) (this project) · [OpenClaw](../entities/openclaw.md) · [NemoClaw](../entities/nemoclaw.md) · [Hermes Agent](../entities/hermes-agent.md) · [ROS 2](../entities/ros2.md) · [Anthropic](../entities/anthropic.md) (Claude) · [ros2-mcp-server](../entities/ros2-mcp-server.md) (first-party counterpart)

## Concepts touched

- [LLM-agent architecture](../concepts/agents/llm-agent-architecture.md) — the converged orchestrator pattern; MCP as tool-access protocol.

## Open questions

- **Who maintains it?** No public org members; no company attribution. Sustainability unknown.
- **Manipulation story is absent** — skills are nav/camera-centric (`drive_base`, `follow_person`, `find_object`, `take_snapshot`); no arm control, no learned-policy integration, no [LeRobot](../entities/lerobot.md)/[Rosetta](../entities/rosetta.md) path, no episode recording. Will one emerge?
- How well does the deterministic NL→mission compiler handle goals beyond simple verb chaining?
- Does the WebRTC cloud mode hold up for anything latency-sensitive?
- Marketplace (skills.agenticros.com) inventory depth — how many third-party skills actually exist?
