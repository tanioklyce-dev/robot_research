---
title: DimOS
type: entity
subtype: software-framework
created: 2026-08-13
updated: 2026-08-17
sources: 11
tags: [dimos, dimensional, agentic-robotics, llm-agent, mcp, langgraph, middleware, ros2-alternative, lcm, zenoh, unitree, teleoperation, lerobot, spatial-memory, apache-2-0, open-source]
---

**DimOS** — *"the agentive operating system for physical space"*: an Apache-2.0 Python robotics middleware **plus** agent layer from [Dimensional Inc.](dimensional-inc.md), positioned as a ROS-optional SDK for generalist robotics. Repo: [github.com/dimensionalOS/dimos](https://github.com/dimensionalOS/dimos) — **3,874 stars / 788 forks / 12+ contributors**, created Oct 2024, committed daily as of ingest. Docs: [docs.dimensionalos.com](https://docs.dimensionalos.com). Version `0.0.14b1`, self-labelled **"Pre-Release Beta."**

Primary source: [DimOS GitHub repository](../sources/dimos-github.md).

## Why it matters in this wiki

**The largest agentic-robotics codebase ingested here**, by an order of magnitude — and the fourth implementation of the pattern in [LLM-agent architecture across stacks](../syntheses/agents/llm-agent-architecture-across-stacks.md). It matters less as a new idea than as the first *industrial-scale* instance of that idea, which lets the synthesis's claims be tested rather than restated. Two of its four convergences do not survive contact with DimOS.

It is also the closest thing the wiki has to a working [Waddle](waddle-labs.md): the same "put an LLM agent above the robot and let it call skills" thesis, with a public repository instead of a blog post.

## Architecture

### Modules and streams

```python
class RobotConnection(Module):
    cmd_vel: In[Twist]
    color_image: Out[Image]

    @rpc
    def start(self): ...
```

Typed `In[T]` / `Out[T]` stream declarations on a `Module` subclass, with deliberately ROS-shaped message names (`dimos.msgs.geometry_msgs.Twist`, `dimos.msgs.sensor_msgs.Image`). `@rpc` exposes methods for remote call — `dimos shell` gives an IPython session attached to every deployed module's RPCs.

### Blueprints

`autoconnect(...)` wires modules by matching `(name, type)` pairs and returns a composable `Blueprint`; conflicts are resolved by remapping or overriding transports. A blueprint is the runnable unit — `dimos list` enumerates them, `dimos run <name>` starts one.

### Transports

Swappable **under an unchanged module API**: LCM (default, UDP multicast, best-effort), **Zenoh** (reliable), shared memory (large local streams), DDS/CycloneDDS, and **ROS 2**. Selected globally at the CLI (`dimos --transport=zenoh run ...`). Multi-language interop over LCM (C++, Lua, TypeScript examples ship in-repo).

> [!note] "No ROS required" means ROS-optional, not anti-ROS
> ROS 2 is one interchangeable backend among five, and navigation is advertised *"via both DimOS native and ROS."* The claim is about the install dependency — `pip install dimos`, no colcon workspace — not about rejecting the ecosystem. Contrast [Rosetta](rosetta.md), which solves the mirror-image problem: bringing ROS 2 robots *into* [LeRobot](lerobot.md) via a declarative YAML contract.

### Agents

Agents are ordinary Modules. `McpClient` carries `human_input: In[str]`, `agent: Out[BaseMessage]`, `agent_idle: Out[bool]`, and subscribes to the same camera / LiDAR / odometry / spatial-memory streams as everything else.

**Skills are discovered, not declared.** Decorate any Module method with `@skill`; at startup the agent enumerates them across all deployed modules over RPC and exposes them as LangChain tools, using the docstring as the tool description. `McpServer` republishes them as **MCP** tools for any external client; `McpClient` runs a **[LangGraph](langgraph.md)** agent against them.

```bash
dimos mcp list-tools
dimos mcp call relative_move --arg forward=0.5
dimos agent-send "explore the room"
```

Default LLM: **`gpt-5.6-luna`** (cloud, `OPENAI_API_KEY`). Local path via [Ollama](ollama.md) (`unitree-go2-agentic-ollama`).

## Capabilities

| Area | What ships |
|---|---|
| **Navigation** | "Column-carving" voxel map (each LiDAR frame replaces its region of the global map); live mapping vs **premap + **[GTSAM](gtsam.md)** pose-graph optimization + relocalization**; frontier exploration, A* replanning, visual servoing, patrolling |
| **Spatial memory** | `dimos/memory2` — SQLite spatio-temporal stream store with embeddings; streams are queryable and composable (`.transform(speed())`, `smooth(50)`, downsample, throttle) and renderable to SVG over a global map. Marketed as "spatio-temporal RAG" |
| **Perception** | Detectors (Ultralytics), 3D projections, audio; VLM backends **[Florence-2](florence-2.md)**, **[Moondream](moondream.md)** (local + hosted), Qwen, OpenAI |
| **Manipulation** | **[Drake](drake.md)** planning; xArm and [AgileX Piper](agilex-piper.md) SDKs; Quest VR teleop; dual-arm coordinator |
| **Teleoperation** | **dimTELE** — hosted WebRTC teleop from browser or Quest; **robot dials out to a broker**, so no inbound ports (works behind home NAT, Wi-Fi, LAN, cellular) |
| **Simulation** | [MuJoCo](mujoco.md) (`dimos[sim]`) for Go2 and G1 |
| **Replay** | `dimos --replay run unitree-go2` runs the full SLAM/costmap/A* stack on recorded sessions with no hardware |
| **Imitation** | Quest teleop → episode recorder → **`dimos dataprep` → [LeRobot](lerobot.md) v3.0 or HDF5 dataset** |

## Hardware support (project's own maturity labels)

🟩 stable · 🟨 beta · 🟧 alpha · 🟥 experimental

| Platform | Class | Status |
|---|---|---|
| [Unitree Go2](unitree-go2.md) pro/air | Quadruped | 🟩 |
| [Unitree G1](unitree-g1.md) | Humanoid | 🟨 |
| xArm ([xArm 7](xarm-7.md)) | Arm | 🟨 |
| [AgileX Piper](agilex-piper.md) | Arm | 🟨 |
| MAVLink / DJI Mavic | Drone | 🟧 |
| Unitree B1 | Quadruped | 🟥 |
| **[openFT force-torque sensor](openft-sensor.md)** | Misc | 🟥 |

Exactly one platform at "stable," and the humanoid everyone would demo is beta. Unusually honest for a support matrix — see the [source page](../sources/dimos-github.md) for why that improves the credibility of the rest.

## Compute

RTX 3000+ / 8 GB VRAM minimum, RTX 4070+ recommended; GPU optional for control, **required for perception and VLMs**. **Jetson AGX Orin tested ✅; Jetson Orin Nano 🟧 experimental** — placing DimOS above the [Orin Nano tier](../syntheses/platforms/jetson-onboard-compute-xlerobot.md) that the wiki's low-cost platforms live in.

## What DimOS changes about this wiki's agentic-robotics picture

> [!warning] It breaks two of four convergences
> The [across-stacks synthesis](../syntheses/agents/llm-agent-architecture-across-stacks.md) found that every stack (a) defaults to a small open-weights Qwen for on-device agency and (b) hand-rolls a JSON tool schema rather than depending on a provider's function-calling API. DimOS does **neither** — cloud `gpt-5.6-luna` by default, and **MCP + LangGraph** as the tool surface. The portability bet moved from *avoid protocols* to *standardize on an open one*.

> [!note] Capability registry — skill-level mutual exclusion (verified in-tree 2026-08-17)
> `dimos/agents/capabilities.py` implements a **`CapabilityRegistry`**: a skill declares what it occupies via **`@skill(uses=[...])`**, and the MCP server consults a process-wide registry before dispatching every `tools/call`. Holds are keyed by **per-invocation token** rather than tool name, so a stale invocation cannot release a live hold and a same-tool re-acquire is a **takeover**; different tools sharing a capability **conflict**. Acquire is **atomic all-or-nothing**, try-lock by default, with an optional timeout that waits only on `instant` holders — `background` holders "run until explicitly stopped, so refuse instead." On conflict the server refuses with *"Cannot start X: capability Y is held by Z"* and lets the agent decide (typically: call the stop tool, retry).
>
> This is a **more developed preemption primitive than [AgenticROS](agenticros.md)'s `blocks_base` boolean** — but *"today the only declared capability is `CAP_MOVEMENT`."* The base is arbitrated; arms, cameras and the speaker are not.

> [!warning] No authentication on the MCP surface (verified in-tree 2026-08-17)
> `mcp_server.py`'s only middleware is CORS — **`allow_origins=["*"]`, `allow_methods=["POST","GET"]`, `allow_headers=["*"]`** — with no `Depends`, `HTTPBearer`, `APIKey` or `Security` on either `POST /mcp` or `GET /mcp`. There is **no per-client scoping of the skill surface**: any attaching MCP client gets every `@skill`. The tree also contains **no estop / emergency / interlock / deadman path** (nearest: `dimos/core/coordination/watchdog_main.py`). Analysis: [DimOS as a home-AI substrate](../syntheses/agents/dimos-as-home-ai-substrate.md).
>
> Note for anyone grepping: **"security" in this repo means the surveillance application** — `dimos/experimental/security_demo/`, `unitree_go2_security.py` — not access control.

> [!note] Skill discovery is a real improvement on the pattern
> The other three stacks maintain a prompt template listing the skill vocabulary plus a hand-written dispatcher. DimOS derives the tool surface from the running system by RPC introspection of `@skill` methods. Adding a capability is adding a decorated method — the manifest cannot drift from the code.

> [!warning] The VLA / agentic bifurcation narrows but does not close
> DimOS is the first ingested stack to combine LLM-agent control with an imitation-learning pipeline, exporting Quest-teleop episodes as **LeRobot v3.0 datasets**. But **no VLA runs in its control loop** — no π0, GR00T, OpenVLA, ACT, or SmolVLA anywhere in the repo. It *feeds* the VLA path while being *controlled by* an LLM calling classical skills. The two paths now share a data format, not a control path.

> [!note] Health signals to read together
> 626 open issues / 3,874 stars (a 16% ratio), 277 MB repo, version `0.0.14b1`, "Pre-Release Beta" banner, and a large surface area — five hardware classes, five transports, nav, perception, memory, manipulation, teleop, sim, web UI — held up by ~12 contributors. Breadth is verifiable from the tree; per-capability depth is not, and **the repo publishes no success rates, latencies, or benchmarks of any kind**.

## Related

- [Dimensional Inc.](dimensional-inc.md) — the company
- [Waddle Labs](waddle-labs.md) — same thesis, blog post instead of a repo
- [ROS 2](ros2.md) — the incumbent it is positioned against and also speaks
- [Rosetta](rosetta.md) — the mirror-image bridge (ROS 2 robots → LeRobot)
- [LeRobot](lerobot.md) — dataset target of `dimos dataprep`
- [stretch_ai](stretch-ai.md), [ROSOrin](rosorin.md), [OpenClaw](openclaw.md) — the three stacks it joins in the [across-stacks synthesis](../syntheses/agents/llm-agent-architecture-across-stacks.md)
- [Vulcan Robotics](vulcan-robotics.md) — maintains a `dimos-vulcan` fork

## Mentioned in

- [DimOS GitHub repository](../sources/dimos-github.md)
- [LLM-agent architecture across stacks](../syntheses/agents/llm-agent-architecture-across-stacks.md)
- [DimOS as a home-AI substrate](../syntheses/agents/dimos-as-home-ai-substrate.md) — read against the [home AI platform](../syntheses/agents/home-ai-platform-trust-and-authority.md) framework: **owns the household world model, lacks the authority model.** `memory2` is the asset, locally owned; replay + inspectable state make it the wiki's most auditable stack; but `@skill` is **allow-by-decoration** where [Matter](matter.md)'s ARL is deny-by-default per ecosystem.
