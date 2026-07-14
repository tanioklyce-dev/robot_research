---
title: ros2-mcp-server
type: entity
subtype: software-framework
created: 2026-07-04
updated: 2026-07-13
sources: 2
tags: [ros2-mcp-server, mcp, ros2, fleet, agent, tool-schema, first-party, skeleton, execution-rail, guardrails]
---

**ros2-mcp-server** — first-party MIT server that **exposes a [ROS 2](ros2.md) robot's skills as [MCP](../concepts/agents/llm-agent-architecture.md#mcp-model-context-protocol) tools**, so an LLM agent (on-robot or a [DGX Spark](dgx-spark.md) fleet master) can command it in natural language. The load-bearing new code of the [fleet agentic control framework](../syntheses/projects/fleet-agentic-framework.md); **the wiki's first ROS 2↔MCP bridge**, filling the [standing Claw-ecosystem gap](hermes-agent.md#robot-platform-fit). Repo: [github.com/tanioklyce-dev/ros2-mcp-server](https://github.com/tanioklyce-dev/ros2-mcp-server) ([source page](../sources/ros2-mcp-server-github.md)); design: [ros2-mcp-server design doc](../syntheses/projects/ros2-mcp-server-design.md).

## What it is (and isn't)
- **Is**: an *agent↔ROS 2* tool-calling layer — the LLM emits `navigate_to` / `pick_object` / `say`; a deterministic dispatcher runs each against Nav2 + a LeRobot policy.
- **Isn't**: a [LeRobot↔ROS 2 data bridge](rosetta.md). It sits **above** [Rosetta](rosetta.md) / [lerobot-ros](lerobot-ros.md) / [so101-ros2](so101-ros2.md) and *calls* Rosetta's policy action for the actual manipulation. Complementary layers.

> [!note] No longer the only bridge of its kind (2026-07-05)
> One day after this skeleton was pushed, [AgenticROS](agenticros.md) was ingested — a community Apache-2.0 TypeScript bridge exposing ROS 2 capability manifests to OpenClaw/NemoClaw/Claude/Codex/Hermes/Gemini. It independently converges on four of the five design decisions below (semantic verbs, per-robot capability filtering, deterministic dispatch, out-of-band estop) — but has **no manipulation/LeRobot story**, which remains this repo's reason to exist. Full comparison: [AgenticROS vs the fleet framework](../syntheses/projects/agenticros-vs-fleet-framework.md).

## Design (from the [design doc](../syntheses/projects/ros2-mcp-server-design.md))
- **Semantic tools only** — the tool set is the safety boundary (no raw joint control on the default surface).
- **Config-driven filtering** — one binary; per-robot YAML generates `tools/list` (single-arm robots drop `handover`/the `arm` arg).
- **Structured `{status, reason, observation}` envelope** → agent replanning; **deterministic dispatch** (no `eval`); **out-of-band `stop`**.
- Transport: stdio (local agent) shipped; SSE (fleet master) TODO. `rclpy` bridge stubbed.
- **AgenticROS-pattern layer (2026-07-05)** — `blocks_base`/`interruptible` capability flags (`base_busy` enforcement via a base lock); `run_mission` step graphs with `{{stepId.outputs.field}}` templating; `compile_mission` deterministic NL→mission fast path; `get_capabilities` + `robot_info` heartbeat + `find_robots_for` on `fleet_role: master`; `rmw: rmw_zenoh_cpp` Zenoh knob ([source](../sources/ros2-mcp-server-github.md)).
- **Argument-level execution rail (2026-07-13, `policy.py`)** — the allowlist guards the *verb*; this guards the *noun*. Base **geofence** + named **keep-outs** + **forbidden waypoints** + **forbidden place targets**, per-robot under `safety:`, enforced inside `dispatch()` so mission steps and compiled NL goals hit the same rail as a direct `tools/call`. Deterministic (set lookup + point-in-polygon), **not a guard model**. See [AI guardrails](../concepts/safety/ai-guardrails.md) and [Guardrails for robot agents](../syntheses/agents/guardrails-for-robot-agents.md), which prompted it.

## Status
Early **skeleton**, growing (MIT; created 2026-07-04; AgenticROS-pattern layer `c4ef908` + robot_info wiring `5921d35`, 2026-07-05; execution rail `0b57b68`, 2026-07-13). **43 tests** pass without ROS 2 (bridge stub mode). **Wired**: node lifecycle (executor on a daemon thread), the fleet `robot_info` heartbeat pub/sub (graph-scan discovery, thread-safe marshaling), and the argument-level safety rail — all verified against a fake rclpy, **not yet real hardware**. **Still TODO**: the action/service primitives (Nav2, Rosetta policy, detector, TTS) and SSE transport.

> [!note] The rail is Tier 1 — two gaps are open by design
> It cannot tell a sock from a knife (`object_id` is opaque; the detector's label is dropped → needs an id→label cache, **Tier 2**), and it does not catch `pick(pills)` → `place(trash)` (each call is fine; the *sequence* is the harm → needs held-object provenance, **Tier 3**). `trash` is therefore deliberately **not** in the shipped forbidden targets — a blanket ban would stop the robot tidying without protecting against the case that motivated it. The geofence ships **unset**; it must be measured in the robot's own map frame. A blocklist, not a proof.

## Related
- [Rosetta](rosetta.md) — the LeRobot↔ROS 2 policy bridge it calls underneath.
- [Nav2](nav2.md) — the navigation stack its `navigate_to` targets.
- [Fleet agentic control framework](../syntheses/projects/fleet-agentic-framework.md) / [design doc](../syntheses/projects/ros2-mcp-server-design.md) — where it fits (Layer 2).
- [LLM-agent architecture](../concepts/agents/llm-agent-architecture.md) — the pattern it implements over MCP.
- [AI guardrails](../concepts/safety/ai-guardrails.md) / [Guardrails for robot agents](../syntheses/agents/guardrails-for-robot-agents.md) — the execution-rail concept `policy.py` implements; the synthesis that prompted it.
- [Hermes Agent](hermes-agent.md) / [NemoClaw](nemoclaw.md) — Claw-ecosystem agents that lack exactly this; a candidate MCP client for it.

## Mentioned in
- [ros2-mcp-server GitHub](../sources/ros2-mcp-server-github.md) — primary source.
- [AgenticROS GitHub](../sources/agenticros-github.md) — the community counterpart it is compared against.

## Open questions
- Skeleton, unwired against hardware (rclpy stubs); SSE transport not implemented.
- Whether it becomes a reusable/publishable ROS-MCP bridge beyond the SO-ARM101 fleet — or whether its manipulation tools instead land upstream as an [AgenticROS](agenticros.md) skill (see the [comparison](../syntheses/projects/agenticros-vs-fleet-framework.md#4-what-to-leverage)).
- ~~Adopt AgenticROS's `blocks_base` / `interruptible` capability flags into the tool schema.~~ **Done 2026-07-05** — along with the mission-graph, NL-compiler, fleet-presence, and Zenoh leverage items.
