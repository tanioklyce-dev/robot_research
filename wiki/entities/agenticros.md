---
title: AgenticROS
type: entity
subtype: software-framework
created: 2026-07-05
updated: 2026-07-05
sources: 1
tags: [agenticros, ros2, mcp, openclaw, hermes-agent, nemoclaw, fleet, skills-marketplace, zenoh, typescript, agent-robot-bridge]
---

**AgenticROS** — Apache-2.0, TypeScript-monorepo integration layer that exposes a [ROS 2](ros2.md) robot (or fleet) to **six agent platforms at once**: [OpenClaw](openclaw.md) (native plugin, flagship), [NemoClaw](nemoclaw.md), Claude Code/Desktop/Dispatch + OpenAI Codex + [Hermes Agent](hermes-agent.md) (one shared [MCP](../concepts/agents/llm-agent-architecture.md#mcp-model-context-protocol) server), and Gemini CLI. The first **community** ROS 2↔agent bridge in the wiki — the thing multiple wiki pages had flagged as the [standing Claw-ecosystem gap](hermes-agent.md#robot-platform-fit). Repo: [github.com/agenticros/agenticros](https://github.com/agenticros/agenticros) ([source page](../sources/agenticros-github.md)).

## Capabilities

- **Capability manifests** — robots advertise typed verbs (`drive_base`, `find_object`, `follow_person`, …) with typed `inputs`/`outputs` plus `interruptible` and `blocks_base` (exclusive base-motion claim) flags; agents plan against verbs, not raw topics ([AgenticROS GitHub](../sources/agenticros-github.md)).
- **Missions** — `run_mission` runs declarative step graphs with `{{stepId.outputs.field}}` output templating; a **deterministic rule-based NL→mission compiler** (no LLM needed for known verb patterns); in-process cancel tokens.
- **Fleet primitives** — `ros2_find_robots_for({capability, kind?, online?})` capability queries; 1 Hz heartbeat on `<ns>/agenticros/robot_info`; namespaced `cmd_vel`; one mission can route steps across robots ([AgenticROS GitHub](../sources/agenticros-github.md)).
- **Transports** — one `RosTransport` interface over local DDS (rclnodejs), rosbridge WebSocket, WebRTC (cloud/NAT), and **Zenoh** (`rmw_zenoh_cpp`).
- **Safety** — `before_tool_call` validator hook (velocity limits, workspace bounds); `/estop` bypasses the AI entirely (out-of-band stop). Also exposes a raw command surface (`ros2_publish`, `ros2_service_call`, `ros2_action_goal`) — wider than a semantic-only boundary.
- **Memory** — cross-adapter `memory_*` tools (Mem0 vector store or local JSON), namespaced per robot; mission transcripts tagged by capability/status.
- **Skills marketplace** — skills are npm packages (`registerSkill(api, config, context)`); `npx agenticros create-skill` / `publish`; marketplace at skills.agenticros.com.

## What it is not (as of ingest)

**No manipulation or learning story.** Skills are navigation/camera-centric; there is no arm control, no [LeRobot](lerobot.md)/[Rosetta](rosetta.md) integration, no learned-policy dispatch, no episode recording — i.e. none of the data-flywheel layer the [fleet framework](../syntheses/projects/fleet-agentic-framework.md) needs. See the [decision analysis](../syntheses/projects/agenticros-vs-fleet-framework.md).

## Status

Early but real: 112 stars / 14 forks / ~125 commits, **no formal releases**, comprehensive docs, TurtleBot3 Gazebo sim + teleop web app + Docker Compose. **Anonymous maintainers** (org has no public members) — sustainability unknown ([AgenticROS GitHub](../sources/agenticros-github.md)).

## Related

- [ros2-mcp-server](ros2-mcp-server.md) — first-party counterpart; manipulation-first where AgenticROS is nav-first. Comparison: [AgenticROS vs the fleet framework](../syntheses/projects/agenticros-vs-fleet-framework.md).
- [OpenClaw](openclaw.md) / [NemoClaw](nemoclaw.md) / [Hermes Agent](hermes-agent.md) — the agent platforms it adapts.
- [openclaw_controller](openclaw-controller.md) — Hiwonder's vendor-specific OpenClaw↔ROS 2 bridge; AgenticROS is the generic community equivalent.
- [LLM-agent architecture](../concepts/agents/llm-agent-architecture.md) — the pattern it implements.

## Mentioned in

- [AgenticROS GitHub](../sources/agenticros-github.md) — primary source.
