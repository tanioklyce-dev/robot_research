---
title: ros2-mcp-server GitHub (tanioklyce-dev)
type: source
url: https://github.com/tanioklyce-dev/ros2-mcp-server
author: tanioklyce-dev (first-party)
published: 2026-07-04 (created)
ingested: 2026-07-04
format: github-repo
license: MIT
tags: [ros2-mcp-server, mcp, ros2, fleet, agent, tool-schema, skeleton, first-party, so-arm101]
---

## Summary

First-party **[ROS 2 ↔ MCP server](../entities/ros2-mcp-server.md)** — exposes a ROS 2 robot's skills as [Model Context Protocol](../concepts/agents/llm-agent-architecture.md#mcp-model-context-protocol) tools so an LLM agent (on-robot [Gemma-4-E4B](../entities/gemma4.md) or a [DGX Spark](../entities/dgx-spark.md) fleet master) can command it in natural language. Built this session as the load-bearing new code of the [fleet agentic control framework](../syntheses/projects/ros2-mcp-server-design.md); MIT, Python. **The wiki's first ROS 2↔MCP bridge** — it fills the gap the wiki repeatedly flagged: [none of the Claw-ecosystem agents ships a ROS 2 integration](../entities/hermes-agent.md#robot-platform-fit).

> [!note] Skeleton, and a different layer from the LeRobot↔ROS 2 bridges
> This is an **early skeleton** (1 commit; `rclpy` action/service calls are stubbed to wire). It is **not** a competitor to [Rosetta](../entities/rosetta.md) / [lerobot-ros](../entities/lerobot-ros.md) / [so101-ros2](../entities/so101-ros2.md) — those bridge *LeRobot policies* to ROS 2 (data/policy plumbing). This server sits a layer **above** them: it bridges an *LLM agent* to ROS 2 *skills* (tool-calling / orchestration), and its manipulation tool calls a [Rosetta](../entities/rosetta.md) policy action underneath. Complementary, not overlapping.

## Key facts
- **MIT**; Python; created 2026-07-04. Deps: the `mcp` SDK + `pyyaml`; **`rclpy` sourced from the ROS 2 env, not pip** (bridge falls back to stub mode without ROS 2, so it imports/tests on a plain laptop).
- **Config-driven tool filtering** — one binary, one YAML per robot (`arms`, `cameras`, `policy_endpoint`); `tools/list` is generated from it, so single-arm robots don't see `handover`/the `arm` arg and dual-arm robots do. Verified: single-arm → 8 tools, dual-arm → 9.
- **Structured `{status, reason, observation}` result envelope** (closed reason vocabulary) — enables agent closed-loop replanning.
- **Deterministic dispatch** (fixed name→handler table; never `eval`s model output); **out-of-band `stop`** (not a normal tool).
- Transport: **stdio** (local agent) shipped; **SSE** (network / fleet master) is a TODO.
- Tools: `navigate_to`, `pick_object`, `place_object`, `handover` (dual-arm), `list_visible_objects`, `get_robot_state`, `say`, `record_episode`, `report_outcome`.

## Entities mentioned
- [ros2-mcp-server](../entities/ros2-mcp-server.md) — this repo's entity. [Rosetta](../entities/rosetta.md) — the LeRobot↔ROS 2 policy bridge its `run_policy` targets. [Nav2](../entities/nav2.md) — the nav action its `navigate_to` targets.
- Fleet hardware: [XLeRobot](../entities/xlerobot.md), [LeKiwi](../entities/lekiwi.md), [ROSOrin Pro](../entities/rosorin-pro.md); [Gemma 4](../entities/gemma4.md) (agent), [DGX Spark](../entities/dgx-spark.md) (master).

## Concepts touched
- [LLM-agent architecture](../concepts/agents/llm-agent-architecture.md) — this is the concrete ROS 2 realization of the LLM-emits-tool-calls pattern (MCP as the wire format).

## Open questions
- **Skeleton, not proven** — the `ros_bridge.py` ROS 2 calls (Nav2, Rosetta policy, detector, TTS) are TODO stubs; unwired against real hardware.
- **SSE transport** for the fleet-master deployment is not yet implemented.
- Whether it generalizes beyond the SO-ARM101 fleet (the tool set is generic; only the configs are fleet-specific).
