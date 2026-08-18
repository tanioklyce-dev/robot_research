---
title: DimOS GitHub repository (dimensionalOS/dimos)
type: source
url: https://github.com/dimensionalOS/dimos
author: Dimensional Inc. — 12+ contributors, led by `spomichter` (284 commits), `paul-nechifor` (211), `leshy` (139)
published: 2024-10-19 (repo created; last push 2026-08-13, active daily)
ingested: 2026-08-13
license: Apache-2.0 (Copyright 2025 Dimensional Inc.)
tags: [dimos, dimensional, agentic-robotics, llm-agent, mcp, middleware, ros2-alternative, lcm, zenoh, unitree, teleoperation, lerobot, spatial-memory, open-source]
---

## Summary

**DimOS** — *"the agentive operating system for physical space"* — is an Apache-2.0 Python robotics middleware plus agent layer from **Dimensional Inc.**, pitched explicitly as a **ROS 2 alternative**: *"With a simple install and no ROS required, build physical applications entirely in python that run on any humanoid, quadruped, or drone."*

Two things make it worth a wiki page. First, scale: **3,874 stars / 788 forks / 12+ contributors / active daily commits** as of ingest — the largest agentic-robotics codebase this wiki has ingested, an order of magnitude past [Rosetta](../entities/rosetta.md) (76 stars) and with actual code where [Waddle](waddle-labs-introducing-waddle.md) had only a blog post.

Second, architecture: DimOS is the **fourth implementation of the converged LLM-agent pattern** documented in [LLM-agent architecture across stacks](../syntheses/agents/llm-agent-architecture-across-stacks.md) — and it **breaks two of that synthesis's four convergences**, while partly closing the bifurcation the synthesis called its most important structural finding.

It also resolves an open question from the previous ingest: `dimos-vulcan` in the [Vulcan Robotics](../entities/vulcan-robotics.md) org is a fork of this repository.

## Key claims — the middleware

The core abstraction is **Modules communicating over typed streams**, composed by **Blueprints**:

```python
class RobotConnection(Module):
    cmd_vel: In[Twist]
    color_image: Out[Image]

    @rpc
    def start(self): ...
```

- **`In[T]` / `Out[T]` class annotations** declare a module's stream interface with typed messages (`dimos.msgs.geometry_msgs`, `dimos.msgs.sensor_msgs` — deliberately ROS-shaped names).
- **`autoconnect(...)`** wires modules by matching `(name, type)` pairs and returns a `Blueprint`; blueprints compose, remap, and can have transports overridden when autoconnect hits a name/type conflict.
- **`@rpc`** exposes module methods for remote call; `dimos shell` drops an IPython session attached to every module's RPCs.
- **Transports are swappable under an unchanged module API** — LCM (current default, UDP multicast, best-effort), Zenoh (reliable), shared memory (`pSHMTransport`, for large local streams), DDS/CycloneDDS, and **ROS 2**. Selectable globally at the CLI: `dimos --transport=zenoh run unitree-go2`.
- The transport docs are unusually candid about semantics: *"Some are best-effort (e.g., UDP multicast / LCM): loss can happen. Some can be reliable... but may add latency/backpressure. So: treat the API as uniform, but pick a backend whose semantics match the task."*
- **Multi-language via LCM interop** — C++, Lua, TypeScript examples ship in `examples/language-interop/`. Repo languages: Python 10.3 MB, Rust 434 KB, TypeScript 418 KB, C++ 173 KB.

> [!note] "No ROS required" — but ROS 2 is a transport
> DimOS is not anti-ROS; it is *ROS-optional*. ROS 2 sits alongside LCM and Zenoh as one interchangeable backend under the same module API, and the navigation docs advertise SLAM and planning *"via both DimOS native and ROS."* The claim being made is about the **dependency**, not the ecosystem: you can install with `pip` and never touch a colcon workspace. Compare [Rosetta](../entities/rosetta.md), which solves the adjacent problem in the opposite direction (bring ROS 2 robots *into* [LeRobot](../entities/lerobot.md) via a YAML contract).

## Key claims — the agent layer

This is the part that bears on the wiki's [LLM-agent architecture](../concepts/agents/llm-agent-architecture.md) coverage.

- **Agents are ordinary Modules.** `McpClient` has `human_input: In[str]`, `agent: Out[BaseMessage]`, `agent_idle: Out[bool]`. It subscribes to the same camera / LiDAR / odometry / spatial-memory streams every other module sees.
- **Skills are discovered, not declared.** Any method on any Module decorated with `@skill` becomes an agent tool. *"On startup, it discovers all `@skill`-annotated methods across deployed modules via RPC and exposes them as LangChain tools."* Docstrings become the tool description the LLM reads.
- **MCP is the tool surface.** `McpServer` publishes `@skill` methods as MCP tools; `McpClient` runs a **LangGraph** agent against them. Any external MCP client can attach. CLI: `dimos mcp list-tools`, `dimos mcp call relative_move --arg forward=0.5`.
- **Default LLM is `gpt-5.6-luna`** (cloud, requires `OPENAI_API_KEY`). A local path exists — `dimos --simulation run unitree-go2-agentic-ollama` via [Ollama](../entities/ollama.md).
- **The README points agents at the repo**: *"Direct your favorite Agent ([OpenClaw](../entities/openclaw.md), Claude Code, etc.) to AGENTS.md and our CLI and MCP interfaces to start building powerful Dimensional applications."* The CLI is designed to be driven by a coding agent, not just a human.

### Shipped built-in skills

| Skill | Module |
|---|---|
| `relative_move(forward, left, degrees)`, `execute_sport_command(name)`, `wait(seconds)` | `UnitreeSkillContainer` |
| `observe()` — capture and return current camera frame | `GO2Connection` |
| `navigate_with_text(query)`, `tag_location(name)`, `stop_navigation()` | `NavigationSkillContainer` |
| `follow_person(query)`, `stop_following()` | `PersonFollowSkillContainer` |
| `speak(text)` | `SpeakSkill` |
| `where_am_i()`, `get_gps_position_for_queries(...)` | `GoogleMapsSkillContainer` |
| `set_gps_travel_points(points)` | `GpsNavSkillContainer` |
| `map_query(query_sentence)` — OpenStreetMap search with a VLM | `OsmSkill` |

Skill parameters must be JSON-serializable primitives; returns are `str` or objects implementing `agent_encode()` (e.g. an `Image`).

## Key claims — capabilities

- **Navigation** — "column-carving voxel map": each new LiDAR frame *replaces* the corresponding region of the global map, so the map always reflects latest observations. Live mapping (fast, reactive, drifts) vs **premap + relocalization** (record once, run pose-graph optimization offline with GTSAM, relocalize at runtime against the exported premap). Also frontier exploration, A* replanning, visual servoing, patrolling, CMU-nav, 3D nav.
- **Spatial memory (`dimos/memory2`)** — a spatio-temporal stream store on SQLite with embeddings and a queryable/transformable stream API. A published example session holds `color_image` 4,164 items, `color_image_embedded` 267, `lidar` 2,251, `odom` 5,465 over 292.5 s. Streams support `.transform(speed())`, `.transform(smooth(50))`, downsampling, throttling, and SVG rendering against a global map. Marketed as *"spatio-temporal RAG, dynamic memory, object localization and permanence."*
- **Perception** — detectors, 3D projections, VLMs, audio. VLM backends in `dimos/models/vl/`: **[Florence-2](../entities/florence-2.md)**, Moondream (local + hosted), Qwen, OpenAI. Object detection via Ultralytics.
- **Manipulation** — arm planning via **Drake**; xArm and [AgileX Piper](../entities/agilex-piper.md) SDKs.
- **dimTELE** — hosted teleoperation over WebRTC from a browser or Quest headset. **The robot dials out to a hosted broker**, so no inbound ports need opening: works behind a home router, on Wi-Fi, wired LAN, or cellular. Blueprints: `teleop-hosted-go2-transport`, `teleop-hosted-go2-multicam`.
- **Simulation** — MuJoCo (`dimos[sim]`); `dimos --simulation run unitree-g1-sim`.
- **Replay** — `dimos --replay run unitree-go2` runs the full SLAM / costmap / A* stack against a recorded session with no hardware. Recorded sessions ship via Git LFS (~75 MB).

## Key claims — imitation-learning pipeline

`dimos/imitation` is the piece most relevant to the rest of this wiki:

```
teleop (Quest) ─▶ CollectionRecorder ─▶ session_<robot>_<ts>.db ─▶ dimos dataprep ─▶ dataset
```

- Quest controller teleop with hold-to-engage (A/X), toggle-record (B), discard (Y).
- Sessions land in `~/.local/state/dimos/recordings/session_<robot>_<timestamp>.db`, recording `color_image`, `coordinator_joint_state`, and `status` (episode markers). New timestamped file per run; nothing overwritten.
- **`dimos dataprep` exports to [LeRobot](../entities/lerobot.md) v3.0 or HDF5** — `dimos/imitation/dataprep/formats/{lerobot,hdf5}`, with `pyarrow` for *"LeRobot v3.0 data/episodes parquet"* and `pandas` for *"LeRobot v3.0 tasks.parquet (task-indexed)."*
- Collection blueprints: `learning-collect-quest-xarm7` (sim or real), `learning-collect-quest-piper`.

## Hardware support (with the project's own maturity labels)

| Platform | Class | Status |
|---|---|---|
| [Unitree Go2](../entities/unitree-go2.md) pro/air | Quadruped | 🟩 stable |
| [Unitree G1](../entities/unitree-g1.md) | Humanoid | 🟨 beta |
| xArm ([xArm 7](../entities/xarm-7.md)) | Arm | 🟨 beta |
| [AgileX Piper](../entities/agilex-piper.md) | Arm | 🟨 beta |
| MAVLink / DJI Mavic | Drone | 🟧 alpha |
| Unitree B1 | Quadruped | 🟥 experimental |
| openFT force-torque sensor | Misc | 🟥 experimental |

> [!note] Credit where due — the maturity labels are honest
> Most robotics projects present a support matrix as a list of checkmarks. DimOS ships a four-level scale and puts **exactly one platform at "stable."** The humanoid everyone would want to demo is beta; drones are alpha. Combined with the README's *"⚠️ Pre-Release Beta ⚠️"* banner and a **version string of `0.0.14b1`**, this is a project that is not overselling itself — which makes the rest of its claims easier to take at face value.

## Requirements

| | Minimum | Recommended |
|---|---|---|
| GPU | NVIDIA RTX 3000+ (8 GB) | RTX 4070+ (12 GB+) |
| CPU | 8-core | 12+ cores |
| RAM | 16 GB | 32 GB+ |
| OS | Ubuntu 22.04 / macOS 12.6+ | Ubuntu 24.04 |

GPU is optional for basic control, **required for perception, VLMs, and AI features**. Tested configs include **Jetson AGX Orin ✅** and **Jetson Orin Nano 🟧 experimental** — placing DimOS in the same on-robot compute band as the wiki's [Jetson ladder](../syntheses/platforms/jetson-module-ladder-power-performance.md) analysis.

Dependency tiers are granular: bare `pip install dimos` is core-only (transport, streams, CLI, blueprints, occupancy maps); `agents`, `perception`, `sim`, `unitree`, `drone`, `manipulation`, `mapping`, `cuda`, `visualization`, `web` layer on top. Only `perception` and `cuda` require a GPU.

## Analysis

> [!note] Skill discovery by RPC introspection is a genuine advance on the converged pattern
> The three stacks in [LLM-agent architecture across stacks](../syntheses/agents/llm-agent-architecture-across-stacks.md) each hand-write a prompt template enumerating the skill vocabulary, then hand-roll a dispatcher (`PickupExecutor` FSM, `eval(f'self.{a}')`, ROS 2 services). DimOS **derives the tool surface from the running system**: decorate a method with `@skill`, deploy the module, and the agent finds it over RPC at startup with the docstring as its description. Adding a capability is adding a decorated method — no prompt edit, no dispatcher edit. It is the difference between a hand-maintained tool manifest and one that cannot drift from the code.

> [!warning] It breaks two of that synthesis's four convergences
> **Convergence 2 said** every stack hand-rolls a JSON tool schema rather than depending on a provider's function-calling API, buying provider portability. DimOS instead standardizes on **MCP + LangGraph** — a portability bet on an *open protocol* rather than on avoiding protocols. Arguably the same goal reached the modern way; either way the stated pattern no longer holds universally.
> **Convergence 1 said** small open-weights Qwen is the effective default planner for on-device agency. DimOS defaults to a **cloud model** (`gpt-5.6-luna`) and treats [Ollama](../entities/ollama.md) as an alternate blueprint. Its stated GPU requirements explain why: this stack expects an RTX-class workstation or an AGX Orin, not an Orin Nano.

> [!warning] The VLA / agentic bifurcation narrows but does not close
> That synthesis's sharpest claim was that **no ingested stack combined LLM-agent control with imitation learning, LeRobot, or VLAs** — a clean split between research VLA work and deployed agentic robotics. DimOS is the **first counterexample in one direction**: `dimos dataprep` exports Quest-teleop episodes as LeRobot v3.0 datasets, so a single stack now spans agentic control *and* demonstration collection for policy learning. But the split survives where it matters most: **nothing in the repository runs a VLA policy in the control loop**. There is no π0, GR00T, OpenVLA, ACT, or SmolVLA integration. DimOS **feeds** the VLA pipeline and is **controlled by** an LLM calling classical skills. The two paths now share a data format, not a control path.

> [!note] Repository health — read the ratios
> 626 open issues against 3,874 stars is a **16% issue-to-star ratio**, high for a project of this size, and 277 MB of repository against a `0.0.14b1` version string. Both are consistent with fast growth and a large surface area (transports, five hardware classes, perception, mapping, memory, teleop, manipulation, sim, web UI) maintained by a dozen contributors. Treat capability breadth as real and per-capability depth as unverified — the maturity labels are the project's own guidance on which is which.

> [!note] dimTELE's dial-out topology is the practical bit
> Robot-initiated WebRTC to a hosted broker removes the single most common reason home and field robot teleop fails: NAT traversal and inbound port forwarding. It also means teleoperation depends on Dimensional's hosted service — the one clearly non-self-hostable piece in an otherwise Apache-2.0 stack, and the visible commercial surface.

## Entities mentioned

- [GTSAM](../entities/gtsam.md) — pose-graph optimization behind premap relocalization
- [LangGraph](../entities/langgraph.md) — the agent runtime inside `McpClient`
- [Drake](../entities/drake.md)
- [Zenoh](../entities/zenoh.md)
- [DimOS](../entities/dimos.md), [Dimensional Inc.](../entities/dimensional-inc.md)
- [Moondream](../entities/moondream.md) — one of its local VLM backends
- [ROS 2](../entities/ros2.md) · [LeRobot](../entities/lerobot.md) · [Rosetta](../entities/rosetta.md) · [MuJoCo](../entities/mujoco.md) · [Ollama](../entities/ollama.md) · [OpenClaw](../entities/openclaw.md) · [Florence-2](../entities/florence-2.md)
- [Unitree Go2](../entities/unitree-go2.md) · [Unitree G1](../entities/unitree-g1.md) · [xArm 7](../entities/xarm-7.md) · [AgileX Piper](../entities/agilex-piper.md)
- [Waddle Labs](../entities/waddle-labs.md) — nearest positional competitor
- [Vulcan Robotics](../entities/vulcan-robotics.md) — maintains a `dimos-vulcan` fork

## Concepts touched

- [LLM-agent architecture](../concepts/agents/llm-agent-architecture.md) · [Agent skills](../concepts/agents/agent-skills.md) · [Code as policy](../concepts/agents/code-as-policy.md)
- [Imitation learning](../concepts/learning/imitation-learning.md) · [Motion planning](../concepts/robotics/motion-planning.md) · [End-user robot programming](../concepts/robotics/end-user-robot-programming.md)

## Addendum — direct tree read, 2026-08-17

The 2026-08-13 ingest worked from the README and docs. Re-checked against the repository itself (GitHub tree API, 2,775 paths, plus raw file reads) to settle questions the summary had left open:

- **`dimos/agents/capabilities.py` — `CapabilityRegistry`**, *"capability registry for skill-level mutual exclusion."* Skills declare occupancy via **`@skill(uses=[...])`**; the MCP server acquires before every `tools/call`. Per-invocation token holds, same-tool takeover, different-tool conflict, atomic all-or-nothing acquire, try-lock default with an optional timeout that waits only on `instant` (not `background`) holders. Conflict returns *"Cannot start X: capability Y is held by Z"* to the agent. **`CAP_MOVEMENT` is the only capability declared.**
- **No authentication on the MCP server.** Only middleware is CORS with `allow_origins=["*"]`, `allow_methods=["POST","GET"]`, `allow_headers=["*"]`; no `Depends` / `HTTPBearer` / `APIKey` / `Security` on `POST /mcp` or `GET /mcp`.
- **No e-stop.** No `estop`, `emergency`, `interlock` or `deadman` path in the tree; nearest is `dimos/core/coordination/watchdog_main.py`.
- **`SkillResult`** (`dimos/agents/skill_result.py`) — typed `error_code` return replacing free-form strings, so callers branch on codes rather than parsing prose. Domain-specific `Literal` aliases enforce which codes a skill may emit.
- **"security" in this tree is the surveillance demo**, not access control: `dimos/experimental/security_demo/`, `unitree_go2_security.py`.

## Open questions

- **No success rates, latencies, or benchmark numbers anywhere.** Same evidentiary problem as [Waddle](waddle-labs-introducing-waddle.md), on a far larger codebase: capability breadth is verifiable from the source tree, capability *quality* is not. What is `navigate_with_text` success rate in an unseen building? What is agent-loop latency at the `gpt-5.6-luna` tier? Unmeasured here and unmeasurable from a repo.
- **Why is the Orin Nano experimental?** The wiki's [onboard-compute analysis](../syntheses/platforms/jetson-onboard-compute-xlerobot.md) cares about exactly this boundary. Is it VRAM for the perception stack, ARM wheel availability, or thermals?
- **What does `dimos dataprep` do about action-space conventions?** Exporting to LeRobot v3.0 requires committing to an `observation.state` / `action` layout. Whether that layout is compatible with policies trained on SO-101 or DROID conventions is undocumented — and it is the whole question for anyone hoping to train a policy on DimOS-collected data.
- **Company facts are thin.** Apache-2.0 header reads "Copyright 2025 Dimensional Inc."; homepage is dimensional.org; hosted services at dimensionalos.com. Founder, funding, and headcount are not established by any source ingested here — see [Dimensional Inc.](../entities/dimensional-inc.md) for what is and isn't known.
- The **openFT force-torque sensor** is a separate `dimensionalOS` repo and un-ingested. Open FT sensing is scarce; worth a look given the wiki's repeated finding that low-cost platforms record position only.
- What is `gpt-5.6-luna`? Named as the default in both the agent docs and AGENTS.md, and otherwise uncovered here.
