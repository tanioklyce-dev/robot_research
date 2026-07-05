---
title: ROS 2 ↔ MCP server — design doc
type: synthesis
created: 2026-07-04
updated: 2026-07-04
tags: [project-scope, mcp, ros2, fleet, agent, tool-schema, design, rosetta, nav2, so-arm101]
---

# ROS 2 ↔ MCP server — design doc

The load-bearing piece of new code in the [fleet agentic control framework](fleet-agentic-framework.md): a server that **exposes a ROS 2 robot's skills as [MCP](../../concepts/agents/llm-agent-architecture.md#mcp-model-context-protocol) tools**, so an LLM agent — on-robot ([Gemma-4-E4B](../../entities/gemma4.md)) or on the fleet master (Gemma-4-31B / [Hermes](../../entities/hermes-agent.md) on the [DGX Spark](../../entities/dgx-spark.md)) — can command it in natural language. This is the integration the wiki keeps flagging as [missing across the whole Claw ecosystem](../../entities/hermes-agent.md#robot-platform-fit): none of Hermes / OpenClaw / NemoClaw ships one.

> [!note] The code lives outside the wiki
> The wiki is a markdown knowledge base; the server is deployable software. It lives in a **separate git repo** — [`ros2-mcp-server`](../../entities/ros2-mcp-server.md) ([github.com/tanioklyce-dev/ros2-mcp-server](https://github.com/tanioklyce-dev/ros2-mcp-server), MIT). This page is the design; the repo is the implementation. It round-trips back into the wiki as a normal [source page](../../sources/ros2-mcp-server-github.md) + [entity](../../entities/ros2-mcp-server.md), exactly like [Rosetta](../../entities/rosetta.md) / [lerobot-ros](../../entities/lerobot-ros.md) — the wiki *documents* code repos, it doesn't contain them.

## Where it sits

```
LLM agent  ──tools/list, tools/call (MCP)──▶  ros2-mcp-server  ──rclpy──▶  ROS 2
(edge or master)                              (deterministic dispatch)    Nav2 + Rosetta policy
                                                                          + detector + TTS
```

Layer-2 of the framework's [three-layer architecture](fleet-agentic-framework.md): the agent emits tool calls; this server runs them against Layer-1 skills ([Nav2](../../entities/nav2.md) for nav, a [LeRobot](../../entities/lerobot.md) policy via [Rosetta](../../entities/rosetta.md) for manipulation).

## Five design decisions

1. **Semantic tools only — the tool set *is* the safety boundary.** `navigate_to`, `pick_object`, `place_object`, `list_visible_objects`, `say`, `record_episode`, `report_outcome`. No raw joint control on the default surface (that's an admin-gated escape hatch). Same property as [Gemini-ER on Spot](../../entities/gemini-robotics.md): the agent "can't invent capabilities beyond the API." The full JSON tool schema is in the [implementation notes](fleet-framework-implementation-notes.md#part-1-mcp-tool-schema-for-the-so-arm101-robots).
2. **Config-driven tool filtering.** One server binary; one YAML per robot (`arms`, `cameras`, `policy_endpoint`). `tools/list` is *generated* from it, so the LLM only ever sees tools the robot can do: single-arm robots ([LeKiwi](../../entities/lekiwi.md), post-swap [ROSOrin](../../entities/rosorin-pro.md)) don't get `handover` or the `arm` argument; dual-arm [XLeRobot](../../entities/xlerobot.md) gets the `arm` enum + `handover`. The two single-arm configs are byte-identical → they point at the same [shared checkpoint](fleet-framework-implementation-notes.md#cross-embodiment-shortcut-two-checkpoints-from-one-data-pool).
3. **Structured result envelope, not prose.** Every action returns `{status, reason, observation}` from a closed reason vocabulary (`no_grasp_found`, `gripper_slipped`, `path_blocked`, …). This is what makes the agent's [closed-loop replanning](llm-agent-architecture-across-stacks.md#implementation-hazards-visible-in-the-sources) work — a `{failed, gripper_slipped}` becomes "retry with the other arm."
4. **Deterministic dispatch — never `eval` model output.** A fixed `name → handler` table; unknown tools return `{rejected, unknown_tool}`. This closes the [RCE hazard](llm-agent-architecture-across-stacks.md#implementation-hazards-visible-in-the-sources) both Hiwonder kits have (`eval(f'self.{a}')`).
5. **`stop` is out-of-band.** A blocking `pick`/`navigate` call can't also receive a cancel through the same channel, so `stop` is **not** a normal MCP tool — it's a separate transport (a dedicated ROS 2 topic / second MCP session / hardware e-stop). Routing emergency-stop through the blocked channel would be the classic mistake.

## Transport

- **stdio** (default) — a local on-robot agent spawns the server as a subprocess. Simplest; matches the edge-agent deployment.
- **SSE / streamable-HTTP** (config `transport: sse`) — for the **fleet master** on the Spark to reach each robot's server over the LAN as an MCP client. This is how central-MCP coordination works before any [A2A](../../concepts/agents/llm-agent-architecture.md#a2a-agent-to-agent-protocol). (Skeleton ships stdio; SSE is a wiring TODO.)

## Package shape (`ros2-mcp-server` repo)

```
ros2_mcp_server/
  server.py     MCP entrypoint: build tools from config, dispatch tools/call
  config.py     per-robot YAML -> RobotConfig (arms, cameras, policy_endpoint)
  tools.py      tool registry (JSON schemas) + build_tools(config) filtering
  envelope.py   the {status, reason, observation} Result type + reason vocabulary
  ros_bridge.py the ONLY rclpy module (Nav2 / policy / detector / TTS) — stubs to wire
  skills/       one module per family (navigation, manipulation, perception, speech, data, control)
configs/        lekiwi.yaml, xlerobot.yaml, rosorin.yaml
tests/          config filtering + envelope + skill tests (pass without ROS 2)
```

`rclpy` is sourced from the ROS 2 environment, **not** pip — and the bridge falls back to a **stub mode** (`{rejected, ros_unavailable}`) when ROS 2 is absent, so the package imports, launches, and tests on a plain laptop / CI. Verified: single-arm config yields 8 tools (no `handover`, no `arm`), dual-arm yields 9 (with both).

## Wiring checklist (skeleton → real)

The `ros_bridge.py` methods are the only TODOs:
1. `start()` — `rclpy.init()`, node + action clients, spin an executor.
2. `navigate_to_pose` → Nav2 `NavigateToPose`.
3. `run_policy` → the [Rosetta](../../entities/rosetta.md)/LeRobot async policy action at `policy_endpoint` (skills: pick/place/handover).
4. `detect_objects` → an open-vocab detector/VLM service.
5. `joint_states`, `speak`, `start_recording` (Rosetta episode_recorder), `estop`.
6. Named-waypoint resolution; SSE transport for the fleet-master deployment.

## Related
- [Fleet agentic control framework](fleet-agentic-framework.md) — this server is Layer 2's bridge.
- [Fleet framework — implementation notes](fleet-framework-implementation-notes.md) — the full MCP tool schema + return envelope this implements.
- [LLM-agent architecture](../../concepts/agents/llm-agent-architecture.md) — MCP + the tool-call pattern.
- [Rosetta](../../entities/rosetta.md) — the LeRobot↔ROS 2 bridge the `run_policy` action targets.
