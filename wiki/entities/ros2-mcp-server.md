---
title: ros2-mcp-server
type: entity
subtype: software-framework
created: 2026-07-04
updated: 2026-07-04
sources: 1
tags: [ros2-mcp-server, mcp, ros2, fleet, agent, tool-schema, first-party, skeleton]
---

**ros2-mcp-server** — first-party MIT server that **exposes a [ROS 2](ros2.md) robot's skills as [MCP](../concepts/agents/llm-agent-architecture.md#mcp-model-context-protocol) tools**, so an LLM agent (on-robot or a [DGX Spark](dgx-spark.md) fleet master) can command it in natural language. The load-bearing new code of the [fleet agentic control framework](../syntheses/projects/fleet-agentic-framework.md); **the wiki's first ROS 2↔MCP bridge**, filling the [standing Claw-ecosystem gap](hermes-agent.md#robot-platform-fit). Repo: [github.com/tanioklyce-dev/ros2-mcp-server](https://github.com/tanioklyce-dev/ros2-mcp-server) ([source page](../sources/ros2-mcp-server-github.md)); design: [ros2-mcp-server design doc](../syntheses/projects/ros2-mcp-server-design.md).

## What it is (and isn't)
- **Is**: an *agent↔ROS 2* tool-calling layer — the LLM emits `navigate_to` / `pick_object` / `say`; a deterministic dispatcher runs each against Nav2 + a LeRobot policy.
- **Isn't**: a [LeRobot↔ROS 2 data bridge](rosetta.md). It sits **above** [Rosetta](rosetta.md) / [lerobot-ros](lerobot-ros.md) / [so101-ros2](so101-ros2.md) and *calls* Rosetta's policy action for the actual manipulation. Complementary layers.

## Design (from the [design doc](../syntheses/projects/ros2-mcp-server-design.md))
- **Semantic tools only** — the tool set is the safety boundary (no raw joint control on the default surface).
- **Config-driven filtering** — one binary; per-robot YAML generates `tools/list` (single-arm robots drop `handover`/the `arm` arg).
- **Structured `{status, reason, observation}` envelope** → agent replanning; **deterministic dispatch** (no `eval`); **out-of-band `stop`**.
- Transport: stdio (local agent) shipped; SSE (fleet master) TODO. `rclpy` bridge stubbed.

## Status
Early **skeleton** (1 commit, MIT, pushed 2026-07-04). Imports + config/tool-filtering tests pass without ROS 2 (bridge stub mode); the `ros_bridge.py` ROS 2 calls are TODO. Will deepen as it's wired against the fleet.

## Related
- [Rosetta](rosetta.md) — the LeRobot↔ROS 2 policy bridge it calls underneath.
- [Nav2](nav2.md) — the navigation stack its `navigate_to` targets.
- [Fleet agentic control framework](../syntheses/projects/fleet-agentic-framework.md) / [design doc](../syntheses/projects/ros2-mcp-server-design.md) — where it fits (Layer 2).
- [LLM-agent architecture](../concepts/agents/llm-agent-architecture.md) — the pattern it implements over MCP.
- [Hermes Agent](hermes-agent.md) / [NemoClaw](nemoclaw.md) — Claw-ecosystem agents that lack exactly this; a candidate MCP client for it.

## Mentioned in
- [ros2-mcp-server GitHub](../sources/ros2-mcp-server-github.md) — primary source.

## Open questions
- Skeleton, unwired against hardware (rclpy stubs); SSE transport not implemented.
- Whether it becomes a reusable/publishable ROS-MCP bridge beyond the SO-ARM101 fleet.
