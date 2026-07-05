---
title: ros2-mcp-server GitHub (tanioklyce-dev)
type: source
url: https://github.com/tanioklyce-dev/ros2-mcp-server
author: tanioklyce-dev (first-party)
published: 2026-07-04 (created)
ingested: 2026-07-04 (re-ingested 2026-07-05 after the AgenticROS-pattern layer landed)
format: github-repo
license: MIT
tags: [ros2-mcp-server, mcp, ros2, fleet, agent, tool-schema, skeleton, first-party, so-arm101]
---

## Summary

First-party **[ROS 2 ↔ MCP server](../entities/ros2-mcp-server.md)** — exposes a ROS 2 robot's skills as [Model Context Protocol](../concepts/agents/llm-agent-architecture.md#mcp-model-context-protocol) tools so an LLM agent (on-robot [Gemma-4-E4B](../entities/gemma4.md) or a [DGX Spark](../entities/dgx-spark.md) fleet master) can command it in natural language. Built this session as the load-bearing new code of the [fleet agentic control framework](../syntheses/projects/ros2-mcp-server-design.md); MIT, Python. **The wiki's first ROS 2↔MCP bridge** — it fills the gap the wiki repeatedly flagged: [none of the Claw-ecosystem agents ships a ROS 2 integration **first-party**](../entities/hermes-agent.md#robot-platform-fit) (the community [AgenticROS](../entities/agenticros.md), ingested a day later, covers the nav-level part).

> [!note] Skeleton, and a different layer from the LeRobot↔ROS 2 bridges
> This is an **early skeleton** (`rclpy` action/service calls are stubbed to wire). It is **not** a competitor to [Rosetta](../entities/rosetta.md) / [lerobot-ros](../entities/lerobot-ros.md) / [so101-ros2](../entities/so101-ros2.md) — those bridge *LeRobot policies* to ROS 2 (data/policy plumbing). This server sits a layer **above** them: it bridges an *LLM agent* to ROS 2 *skills* (tool-calling / orchestration), and its manipulation tool calls a [Rosetta](../entities/rosetta.md) policy action underneath. Complementary, not overlapping.

## Key facts
- **MIT**; Python; created 2026-07-04. Deps: the `mcp` SDK + `pyyaml`; **`rclpy` sourced from the ROS 2 env, not pip** (bridge falls back to stub mode without ROS 2, so it imports/tests on a plain laptop).
- **Config-driven tool filtering** — one binary, one YAML per robot (`arms`, `cameras`, `policy_endpoint`); `tools/list` is generated from it, so single-arm robots don't see `handover`/the `arm` arg and dual-arm robots do. Verified: single-arm → 8 robot tools, dual-arm → 9; since `c4ef908` the 3 always-on meta tools (`run_mission`, `compile_mission`, `get_capabilities`) bring `tools/list` to **11 / 12** (+`find_robots_for` on a fleet master).
- **Structured `{status, reason, observation}` result envelope** (closed reason vocabulary) — enables agent closed-loop replanning.
- **Deterministic dispatch** (fixed name→handler table; never `eval`s model output); **out-of-band `stop`** (not a normal tool).
- Transport: **stdio** (local agent) shipped; **SSE** (network / fleet master) is a TODO.
- Tools: `navigate_to`, `pick_object`, `place_object`, `handover` (dual-arm), `list_visible_objects`, `get_robot_state`, `say`, `record_episode`, `report_outcome` — plus the meta tools below.

### AgenticROS-pattern layer (added 2026-07-05, commit `c4ef908`)

Implements the leverage items from the [AgenticROS decision analysis](../syntheses/projects/agenticros-vs-fleet-framework.md#4-what-to-leverage); all pure Python, 23 tests pass without ROS 2:
- **Capability flags** — `blocks_base` (exclusive base-motion claim, **enforced**: a concurrent base-claiming call returns `base_busy`) + `interruptible` (false ⇒ cancel only via out-of-band stop) on every tool; surfaced to the LLM as description annotations.
- **`run_mission`** — declarative step graphs with `{{stepId.outputs.field}}` output templating (full-string refs pass raw values, e.g. a detected pose dict into `navigate_to`); first failure short-circuits with all step envelopes; no nesting.
- **`compile_mission`** — deterministic NL→mission compiler (no LLM): "go to the kitchen, then pick up the sock, then place it in the basket" → a 4-step graph with find-then-pick auto-expansion and "it"-binding to the last detection; unrecognized goals return `recognized_verbs` for agent self-correction.
- **Fleet presence** — `get_capabilities` capability card on every robot + a 1 Hz heartbeat on `<namespace>/mcp/robot_info` (bridge stub); `fleet_role: master` servers ([`configs/spark-master.yaml`](https://github.com/tanioklyce-dev/ros2-mcp-server/blob/main/configs/spark-master.yaml)) keep a `FleetRegistry` and expose `find_robots_for({capability, kind, online})`.
- **Zenoh knob** — `rmw: rmw_zenoh_cpp` in the per-robot YAML sets `RMW_IMPLEMENTATION` before `rclpy` loads (router-based LAN discovery instead of DDS multicast).
- New envelope reasons: `base_busy`, `invalid_mission`, `unrecognized_goal`.
- **Bridge wiring started (commit `5921d35`, same day)** — the node lifecycle (`start`/`stop`: rclpy node under the config namespace + `MultiThreadedExecutor` on a daemon thread) and the fleet pub/sub are **wired**, no longer stubs: `publish_robot_info` publishes the JSON card on `<ns>/mcp/robot_info` (QoS depth 1); `subscribe_robot_info` discovers heartbeat topics by graph scan (once + 2 s rescan — ROS 2 has no topic wildcards) and marshals decoded cards onto the asyncio loop; malformed payloads dropped. 26 tests + a fake-rclpy smoke test. The action/service primitives (Nav2, Rosetta policy, detector, TTS) remain the TODO stubs.

## Entities mentioned
- [ros2-mcp-server](../entities/ros2-mcp-server.md) — this repo's entity. [Rosetta](../entities/rosetta.md) — the LeRobot↔ROS 2 policy bridge its `run_policy` targets. [Nav2](../entities/nav2.md) — the nav action its `navigate_to` targets.
- Fleet hardware: [XLeRobot](../entities/xlerobot.md), [LeKiwi](../entities/lekiwi.md), [ROSOrin Pro](../entities/rosorin-pro.md); [Gemma 4](../entities/gemma4.md) (agent), [DGX Spark](../entities/dgx-spark.md) (master).

## Concepts touched
- [LLM-agent architecture](../concepts/agents/llm-agent-architecture.md) — this is the concrete ROS 2 realization of the LLM-emits-tool-calls pattern (MCP as the wire format).
- [AgenticROS](../entities/agenticros.md) — the community bridge whose capability-flag / mission-graph / heartbeat patterns the 2026-07-05 layer adopts.

## Open questions
- **Skeleton, not proven** — the `ros_bridge.py` action/service calls (Nav2, Rosetta policy, detector, TTS) are TODO stubs; the wired lifecycle + robot_info pub/sub were verified against a **fake rclpy** only, not a real ROS 2 install (check: `ros2 topic echo /lekiwi/mcp/robot_info` should show 1 Hz JSON cards).
- **SSE transport** for the fleet-master deployment is not yet implemented.
- Whether it generalizes beyond the SO-ARM101 fleet (the tool set is generic; only the configs are fleet-specific).
