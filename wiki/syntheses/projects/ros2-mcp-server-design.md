---
title: ROS 2 ↔ MCP server — design doc
type: synthesis
created: 2026-07-04
updated: 2026-07-05
tags: [project-scope, mcp, ros2, fleet, agent, tool-schema, design, rosetta, nav2, so-arm101]
---

# ROS 2 ↔ MCP server — design doc

The load-bearing piece of new code in the [fleet agentic control framework](fleet-agentic-framework.md): a server that **exposes a ROS 2 robot's skills as [MCP](../../concepts/agents/llm-agent-architecture.md#mcp-model-context-protocol) tools**, so an LLM agent — on-robot ([Gemma-4-E4B](../../entities/gemma4.md)) or on the fleet master (Gemma-4-31B / [Hermes](../../entities/hermes-agent.md) on the [DGX Spark](../../entities/dgx-spark.md)) — can command it in natural language. This is the integration the wiki had flagged as [missing across the whole Claw ecosystem](../../entities/hermes-agent.md#robot-platform-fit): none of Hermes / OpenClaw / NemoClaw ships one **first-party** (the community [AgenticROS](../../entities/agenticros.md) now covers the nav-level part — see the prior-art note below).

> [!note] The code lives outside the wiki
> The wiki is a markdown knowledge base; the server is deployable software. It lives in a **separate git repo** — [`ros2-mcp-server`](../../entities/ros2-mcp-server.md) ([github.com/tanioklyce-dev/ros2-mcp-server](https://github.com/tanioklyce-dev/ros2-mcp-server), MIT). This page is the design; the repo is the implementation. It round-trips back into the wiki as a normal [source page](../../sources/ros2-mcp-server-github.md) + [entity](../../entities/ros2-mcp-server.md), exactly like [Rosetta](../../entities/rosetta.md) / [lerobot-ros](../../entities/lerobot-ros.md) — the wiki *documents* code repos, it doesn't contain them.

## Where it sits

```
LLM agent  ──tools/list, tools/call (MCP)──▶  ros2-mcp-server  ──rclpy──▶  ROS 2
(edge or master)                              (deterministic dispatch)    Nav2 + Rosetta policy
                                                                          + detector + TTS
```

Layer-2 of the framework's [three-layer architecture](fleet-agentic-framework.md): the agent emits tool calls; this server runs them against Layer-1 skills ([Nav2](../../entities/nav2.md) for nav, a [LeRobot](../../entities/lerobot.md) policy via [Rosetta](../../entities/rosetta.md) for manipulation).

> [!note] Prior art discovered 2026-07-05 — AgenticROS
> [AgenticROS](../../entities/agenticros.md) ([source](../../sources/agenticros-github.md)) is a community Apache-2.0 bridge that independently converges on decisions 1, 2, 4, and 5 below (typed capability manifests, per-robot capability filtering, deterministic mission compilation, `/estop` bypassing the AI). It diverges on 3 (typed outputs but no closed failure-reason vocabulary) and additionally exposes a raw `ros2_publish`/`ros2_service_call` surface behind validator hooks. It has no manipulation/[LeRobot](../../entities/lerobot.md) path — which is this server's remit. See [AgenticROS vs the fleet framework](agenticros-vs-fleet-framework.md).
>
> **Adopted same day** ([repo commit `c4ef908`](../../sources/ros2-mcp-server-github.md#agenticros-pattern-layer-added-2026-07-05-commit-c4ef908)): `blocks_base`/`interruptible` capability flags (with `base_busy` enforcement), `run_mission` step graphs with `{{stepId.outputs.field}}` templating, a `compile_mission` deterministic NL→mission fast path, the `robot_info` heartbeat + `find_robots_for` fleet layer (`fleet_role: master`), and a Zenoh RMW config knob.

## Six design decisions

1. **Semantic tools only — the tool set *is* the safety boundary.** `navigate_to`, `pick_object`, `place_object`, `list_visible_objects`, `say`, `record_episode`, `report_outcome`. No raw joint control on the default surface (that's an admin-gated escape hatch). Same property as [Gemini-ER on Spot](../../entities/gemini-robotics.md): the agent "can't invent capabilities beyond the API." The full JSON tool schema is in the [implementation notes](fleet-framework-implementation-notes.md#part-1-mcp-tool-schema-for-the-so-arm101-robots).
2. **Config-driven tool filtering.** One server binary; one YAML per robot (`arms`, `cameras`, `policy_endpoint`). `tools/list` is *generated* from it, so the LLM only ever sees tools the robot can do: single-arm robots ([LeKiwi](../../entities/lekiwi.md), post-swap [ROSOrin](../../entities/rosorin-pro.md)) don't get `handover` or the `arm` argument; dual-arm [XLeRobot](../../entities/xlerobot.md) gets the `arm` enum + `handover`. The two single-arm configs are byte-identical → they point at the same [shared checkpoint](fleet-framework-implementation-notes.md#cross-embodiment-shortcut-two-checkpoints-from-one-data-pool).
3. **Structured result envelope, not prose.** Every action returns `{status, reason, observation}` from a closed reason vocabulary (`no_grasp_found`, `gripper_slipped`, `path_blocked`, …). This is what makes the agent's [closed-loop replanning](../agents/llm-agent-architecture-across-stacks.md#implementation-hazards-visible-in-the-sources) work — a `{failed, gripper_slipped}` becomes "retry with the other arm."
4. **Deterministic dispatch — never `eval` model output.** A fixed `name → handler` table; unknown tools return `{rejected, unknown_tool}`. This closes the [RCE hazard](../agents/llm-agent-architecture-across-stacks.md#implementation-hazards-visible-in-the-sources) both Hiwonder kits have (`eval(f'self.{a}')`).
5. **`stop` is out-of-band.** A blocking `pick`/`navigate` call can't also receive a cancel through the same channel, so `stop` is **not** a normal MCP tool — it's a separate transport (a dedicated ROS 2 topic / second MCP session / hardware e-stop). Routing emergency-stop through the blocked channel would be the classic mistake.
6. **The allowlist guards the *verb*; an argument-level rail guards the *noun*.** Added 2026-07-13 (repo commit [`b925ddc`](../../sources/ros2-mcp-server-github.md#execution-rail-added-2026-07-13-commit-b925ddc)) after [Guardrails for robot agents](../agents/guardrails-for-robot-agents.md) established that decision 1 is a **static, name-level [execution rail](../../concepts/safety/ai-guardrails.md)** in NVIDIA's enterprise-guardrail vocabulary — and that a name-level rail lets `navigate_to(pose=<top of the stairs>)` straight through, because it is a well-formed call to an allowed tool. [`policy.py`](../../entities/ros2-mcp-server.md) adds a base **geofence**, named **keep-out zones**, **forbidden waypoints**, and **forbidden place targets**, configured per robot under `safety:`.

   The hook is in **`dispatch()`** — after the `unknown_tool` allowlist, before the base lock. That placement is load-bearing: `missions.py` routes through the same function, so a **compiled NL goal — exactly where an injected instruction would arrive — hits the same rail as a direct `tools/call`**. And unlike a system-prompt instruction ("never go near the stairs"), a [prompt injection](../../concepts/safety/ai-red-teaming.md) cannot argue it away: the server, not the model, is the trust boundary. It is a set lookup and a point-in-polygon test — **not a guard model**, so none of the guardrail latency budget applies.

   Denials return through the decision-3 envelope (`{status: rejected, reason: outside_geofence, observation: {x, y}}`) with four new entries in the closed reason vocabulary, so the agent re-plans rather than crashing.

### The execution rail: what it catches, and what it does not

| Call | Verdict | Tier |
|---|---|---|
| `navigate_to(pose=…)` outside the geofence | `outside_geofence` | 1 |
| `navigate_to(pose=…)` inside a named keep-out | `inside_keepout` | 1 |
| `navigate_to(location="top_of_stairs")` | `forbidden_waypoint` | 1 |
| `place_object(target="toilet")` | `unsafe_place_target` | 1 |
| `pick_object` whose detected label is on the never-pick list | `unsafe_object` | **2** |
| `pick_object` on an id never detected, or below the confidence floor | `unknown_object` | **2** |
| `pick_object` on a detection too old to trust | `stale_object` | **2** |

**Tier 2 — object-aware picking** (`e2853d1`). `object_id` was opaque, so the rail could refuse to *drive* at the stairs but not to *grasp* a blade. **`world.ObjectCache`** is the missing memory: `list_visible_objects` upserts every detection, the rail looks the id up before a grasp.

> [!warning] Tier 2's design finding: a stale label is worse than no label
> The naive cache is a **downgrade**. The tool schema warns ids *"expire when the scene changes"* — and a cache that ignores that doesn't leave the rail *blind*, it makes the rail **confidently wrong** (green-lighting `pick(obj_3)` because obj_3 *was* a sock 30 s ago, in a scene that has moved). Blind fails safe; confidently-wrong fails **toward the actuator**. So the cache's key behavior is **refusing to answer**: past `object_ttl_s` a lookup reports `stale_object`, not a label — and `stale` is distinct from `unknown` because the agent's recovery differs (*go look again* vs. *you never looked*).
>
> **Fails closed:** configuring `unsafe_pick_labels` derives `require_known_object` — a denylist you can consult only *sometimes* is not a denylist, and a *lazy planner* that never calls `list_visible_objects` would otherwise bypass it by default.
>
> **Limit, pinned by a test:** it is a blocklist over the **detector's vocabulary**. A model that says `"cleaver"` or `"utensil"` walks past a list that says `"knife"`. And `detect_objects` is **still a stub** — none of Tier 2 has met a real detector.

> [!warning] Tier 3 remains open — and shapes two shipped defaults
> **`pick(pills)` → `place(trash)` is not caught.** Each call is individually fine; the **sequence** is the harm. Needs held-object provenance from `run_policy`.
>
> Two consequences, both pinned by tests rather than left as folklore:
> - **`trash` is absent** from `forbidden_place_targets` — disposal safety depends on what is held, so a blanket ban stops the robot tidying while protecting no one.
> - **Medication is absent** from `unsafe_pick_labels` — banning the grasp would destroy the [fetcher-only medication scope](../assistive/underserved-par-domains.md#realistic-researcher-target-2), *the one deployable medication target in this wiki*, while leaving the real failure mode (disposal) wide open.
>
> **Blocking the wrong step and calling it safety is theater.**
>
> The **geofence ships unset** (a commented worked example) — a fabricated polygon either rejects every legitimate goal or silently permits everything, and both are worse than leaving it off. **Measure it in the robot's own map frame.** The name-based rails (waypoints, place targets) are live by default, since they need no map knowledge. Malformed polygons and typo'd `safety:` keys (`keepout` vs `keepouts`, which would silently disable a zone) raise at config load rather than degrading to "no constraint".
>
> It is a blocklist, not a proof — a seatbelt, not an airbag.

## Transport

- **stdio** (default) — a local on-robot agent spawns the server as a subprocess. Simplest; matches the edge-agent deployment.
- **SSE / streamable-HTTP** (config `transport: sse`) — for the **fleet master** on the Spark to reach each robot's server over the LAN as an MCP client. This is how central-MCP coordination works before any [A2A](../../concepts/agents/llm-agent-architecture.md#a2a-agent-to-agent-protocol). (Skeleton ships stdio; SSE is a wiring TODO.)

## Package shape (`ros2-mcp-server` repo)

```
ros2_mcp_server/
  server.py     MCP entrypoint: build tools from config, dispatch tools/call
  config.py     per-robot YAML -> RobotConfig (arms, cameras, policy_endpoint) + SafetyPolicy
  tools.py      tool registry (JSON schemas) + build_tools(config) filtering + dispatch
  policy.py     the argument-level execution rail (decision 6), enforced inside dispatch()
  envelope.py   the {status, reason, observation} Result type + reason vocabulary
  ros_bridge.py the ONLY rclpy module — lifecycle + robot_info pub/sub wired; Nav2 /
                policy / detector / TTS action-service calls still stubs
  skills/       one module per family (navigation, manipulation, perception, speech, data, control)
configs/        lekiwi.yaml, xlerobot.yaml, rosorin.yaml  (each now carries a `safety:` block)
tests/          config filtering + envelope + skill + policy tests (pass without ROS 2)
```

`rclpy` is sourced from the ROS 2 environment, **not** pip — and the bridge falls back to a **stub mode** (`{rejected, ros_unavailable}`) when ROS 2 is absent, so the package imports, launches, and tests on a plain laptop / CI. Verified: single-arm config yields 8 robot tools (no `handover`, no `arm`), dual-arm 9 (with both); with the meta tools (`run_mission`, `compile_mission`, `get_capabilities`) the served `tools/list` is **11 / 12** (+`find_robots_for` on a `fleet_role: master` server).

## Wiring checklist (skeleton → real)

> [!note] Validated on real hardware, 2026-07-05 — and the order below changed because of it
> The server now runs on the [XLeRobot](../../entities/xlerobot.md)'s Jetson Orin NX under **ROS 2 Humble**: node up, 1 Hz JSON capability cards on `<ns>/mcp/robot_info`, clean start/stop ([source](../../sources/ros2-mcp-server-github.md#first-real-hardware-validation-2026-07-05-on-the-xlerobot-commits-c89869f--bf2653c)). Everything prior had only met a *fake* rclpy.
>
> **The generic order below is wrong for that machine.** The XLeRobot has neither Nav2 nor Rosetta yet, and — the real finding — it is **LeRobot-native**, so its FeeTech-USB arms publish **no `/joint_states`** for `joint_states()` to subscribe to (see [gap 4b](fleet-agentic-framework.md#gaps-risks-and-hazards-be-clear-eyed)). Revised order **on the XLeRobot**: a FeeTech→`JointState` publisher, then `joint_states()` → `speak()` → `detect_objects()` (fixture stub, then a real open-vocab model — the Orin NX 16 GB can run OWL-ViT / YOLO-World class detectors) → `run_policy`; **defer Nav2** until a nav stack exists on this base.

The `ros_bridge.py` methods are the only TODOs:
1. ~~`start()` — `rclpy.init()`, node, spin an executor~~ **wired** (`5921d35`) **and hardware-validated** (2026-07-05, ROS 2 Humble); the **action clients** it should create are still TODO.
2. `navigate_to_pose` → Nav2 `NavigateToPose`. *(Deferred on the XLeRobot — no nav stack yet.)*
3. `run_policy` → the [Rosetta](../../entities/rosetta.md)/LeRobot async policy action at `policy_endpoint` (skills: pick/place/handover).
4. `detect_objects` → an open-vocab detector/VLM service. **Also the unlock for the [execution rail's Tier 2](#the-execution-rail-what-it-catches-and-what-it-does-not)** — an `id → label` cache over this service's replies is what would let `policy.py` refuse `pick_object` on a knife.
5. `joint_states` — on LeRobot-native robots this needed a publisher first; **written 2026-07-13** ([`feetech-joint-states`](../../sources/ros2-mcp-server-github.md#feetech--joint_states-publisher-added-2026-07-13-commit-8087288), commit `8087288`, **not yet run on hardware** — start with `--probe`). With it running, `joint_states()` is just a `sensor_msgs/JointState` subscription. Then `speak`, `start_recording` (Rosetta episode_recorder), `estop`.
6. Named-waypoint resolution; SSE transport for the fleet-master deployment (**add auth** — the tool set is a real actuator surface).

**Environment gotcha:** running `pytest` with ROS 2 sourced needs `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1` (Humble's `launch_testing` plugins are incompatible with pytest 9).

## Related
- [Fleet agentic control framework](fleet-agentic-framework.md) — this server is Layer 2's bridge.
- [Fleet framework — implementation notes](fleet-framework-implementation-notes.md) — the full MCP tool schema + return envelope this implements.
- [LLM-agent architecture](../../concepts/agents/llm-agent-architecture.md) — MCP + the tool-call pattern.
- [Guardrails for robot agents](../agents/guardrails-for-robot-agents.md) — **decision 1 ("the tool set *is* the safety boundary") is an [execution rail](../../concepts/safety/ai-guardrails.md)** in NVIDIA's enterprise-guardrail vocabulary, independently derived. The synthesis grades this server **A–** against that standard and names what's still missing: argument-level predicates (`pick(knife)` passes a name-level allowlist), a reversibility partition with confirmation prompts, and an input rail on perception-derived text. The first two are hours of work in `tools.py`.
- [Rosetta](../../entities/rosetta.md) — the LeRobot↔ROS 2 bridge the `run_policy` action targets.
