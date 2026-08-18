---
title: DimOS as a home-AI substrate — it owns the asset and lacks the authority model
type: synthesis
created: 2026-08-17
updated: 2026-08-17
tags: [dimos, dimensional, home-ai, agents, mcp, capability-manifest, authority, world-model, auditability, trust-boundary, matter, synthesis]
---

# DimOS as a home-AI substrate — it owns the asset and lacks the authority model

Applying the [home AI platform](home-ai-platform-trust-and-authority.md) framework to a specific stack: **[DimOS](../../entities/dimos.md)** (DimensionalOS), the largest agentic-robotics codebase in this wiki. The lens produces a clean split — DimOS already implements the asset the platform fight is over, and has essentially none of the authority model that would let an ecosystem be trusted with it.

> [!warning] Evidence base: one source, no measurements
> Everything here derives from the [DimOS repository](../../sources/dimos-github.md) as ingested 2026-08-13. **The repo publishes no success rates, latencies, or benchmarks of any kind.** This is an architecture read, not a performance one. Also, the source page is a summary of a **277 MB repository** — where this page says "no ingested evidence of X," that is a statement about the wiki, not a proof about the code. **Updated 2026-08-17**: the two claims flagged for verification were checked directly against the repository tree and raw files. One held, one did not — both marked inline in §3.

## 1. It already implements the household world model

The [home AI platform](home-ai-platform-trust-and-authority.md) page argues the platform's real asset is a **persistent world model of a household** — floorplan, objects, routines, people, state over time — and that the robot is a sensor endpoint feeding it.

**DimOS has built that.** `dimos/memory2` is a **spatio-temporal stream store on SQLite with embeddings**, marketed as *"spatio-temporal RAG, dynamic memory, object localization and permanence."* Streams are queryable and composable (`.transform(speed())`, `smooth(50)`, downsample, throttle) and renderable to SVG against a global map. A published example session holds 4,164 colour images, 267 embeddings, 2,251 LiDAR frames and 5,465 odometry samples over 292.5 s.

Around it sits the rest of a household model: a **column-carving voxel map** (each LiDAR frame replaces its region of the global map), **premap + [GTSAM](../../entities/gtsam.md) pose-graph optimization + relocalization**, and a `tag_location(name)` skill binding names to places.

> [!note] The strategically loaded fact: the asset is Apache-2.0 and lives in a local file
> The thing Google, Amazon and Apple would hold as a cloud service, DimOS puts in a **SQLite file on your disk**. If the moat in this category is world-model lock-in — historical, un-exportable, un-re-buyable — then DimOS is architecturally the **anti-lock-in position**, and nothing in its own documentation markets it that way.

## 2. It is accidentally the most auditable architecture in the wiki

The [home AI platform](home-ai-platform-trust-and-authority.md) page identifies liability as the category's central unsolved problem: [world-model governance](../../concepts/safety/world-model-governance.md) asks for a record of *"what the system perceived, the state it inferred, and the action it took,"* but the wiki's own callout warns that for an end-to-end learned policy the inferred state is **"a latent vector with no committed semantics — logging it is easy; reading it after an incident is the unsolved part."**

**That objection does not apply to DimOS.** Its inferred state is a voxel map, a pose graph, an A* path — inspectable objects with committed semantics. And it ships replay: `dimos --replay run unitree-go2` re-runs the full SLAM / costmap / A* stack against a recorded session **with no hardware**, with sessions shipped in-repo via Git LFS.

The reason is the same one that makes DimOS look weak on capability: **no VLA runs in its control loop** — no π0, GR00T, OpenVLA, ACT or SmolVLA anywhere in the repo. LLM-plus-classical-skills is less capable than a learned policy and vastly more explainable.

**For a platform facing a liability regime, that trade may be the right one**, and it is the strongest argument for DimOS that its own documentation never makes. It is also fragile: the property comes from the absence of a learned policy, so it erodes the moment one is added.

## 3. The authority model is inverted — and this is the real gap

Compare the two manifest philosophies directly.

| | **[Matter](../../entities/matter.md) ARL** | **DimOS `@skill`** |
|---|---|---|
| Authored by | **the device vendor** | whoever wrote the method |
| Default posture | *"no implicit access permitted by default"* | **exposed on decoration** |
| Granularity | **per-fabric** (per ecosystem) | global — one surface for all clients |
| Expresses | what a given ecosystem may **not** touch | what exists, plus what it **occupies** (`uses=`) |
| Discoverable in advance | yes (`CommissioningARL`) | at runtime, by attaching |
| Negotiable | yes (`ReviewFabricRestrictions`) | n/a |
| Overrides the caller's own admin | **yes** (`ACCESS_RESTRICTED`) | n/a |

DimOS's mechanism: *"on startup it discovers all `@skill`-annotated methods across deployed modules via RPC and exposes them as LangChain tools,"* with docstrings as tool descriptions. `McpServer` republishes them and **any external MCP client can attach**.

The [DimOS entity page](../../entities/dimos.md) praises this, correctly, because **"the manifest cannot drift from the code."** Through this lens the same property is a liability: **exposure is a property of the code, not of the relationship.** There is no way to say *this client may not do that*, because there is no per-client anything. Decorating a method grants it to every attached agent.

> [!note] Qualified 2026-08-17 — part of the manifest *is* declared
> `@skill` is not purely discovery. Its **`uses=[...]`** argument is a declared field naming the capabilities the skill occupies (see the tree check below). So DimOS declares **occupancy** and discovers **existence**. That is a meaningful distinction: it means the decorator already has a place to carry per-skill metadata, and an authority field could live beside `uses=` without redesigning the mechanism. The gap is not that DimOS lacks a manifest format — it is that the manifest has no notion of *who is asking*.

**Matter is deny-by-default; DimOS is allow-by-decoration.** That is the single largest architectural difference between the wiki's best agentic stack and the standard that already governs hundreds of millions of home devices.

### And the exposed surface reaches low in the stack

The shipped skills include **`relative_move(forward, left, degrees)`** — direct base motion, not a goal handed to a pretrained policy.

The [home AI platform](home-ai-platform-trust-and-authority.md) page predicted the commercially plausible split as *ecosystem gets Level 3, vendor keeps Levels 1–2*. **That split does not hold here.** Per [control abstraction levels](../../concepts/robotics/control-abstraction-levels.md), the de-facto safety boundary is the pretrained-policy layer — "models cannot reliably drive joints, but can competently supervise controllers." DimOS has no policy in the loop, so that boundary is absent; whatever bounds exist live inside individual skill implementations and are undocumented here.

> [!warning] Checked against the tree 2026-08-17 — **one half of this was wrong**
> This page originally listed arbitration as absent and flagged it as the highest-value thing to verify. Verified via the GitHub tree API and raw file reads. **The arbitration claim was wrong; the authority claim was right.**
>
> **Arbitration exists, and is better than AgenticROS's flag.** `dimos/agents/capabilities.py` implements a **`CapabilityRegistry`** — *"capability registry for skill-level mutual exclusion."* A skill **declares** what it occupies via **`@skill(uses=[...])`**; the MCP server consults a process-wide registry before dispatching every `tools/call`. Holds are **per-invocation tokens**, not tool names, so a stale invocation's teardown cannot release a live hold; same-tool re-acquire is a **takeover**, different-tool is a **conflict**. Acquire is **atomic all-or-nothing** across the requested capabilities, with a try-lock default and an optional timeout that blocks only on `instant` holders (`background` holders "run until explicitly stopped, so refuse instead"). On conflict the server **refuses** — *"Cannot start X: capability Y is held by Z"* — and hands the decision back to the LLM, with advice to call the holder's stop tool and retry.
>
> **But the vocabulary is one word long.** *"Today the only declared capability is `CAP_MOVEMENT`."* So the base is arbitrated and **nothing else is** — not arms, not cameras, not the speaker. The mechanism is sound and essentially unpopulated.
>
> **Authentication and authorization are genuinely absent.** `mcp_server.py`'s only middleware is CORS, configured **`allow_origins=["*"]`, `allow_methods=["POST","GET"]`, `allow_headers=["*"]`**. No `Depends`, no `HTTPBearer`, no `APIKey`, no `Security` — `POST /mcp` and `GET /mcp` are unauthenticated.
>
> **No e-stop.** The tree contains no `estop`, `emergency`, `interlock`, or `deadman` path; the nearest thing is one `dimos/core/coordination/watchdog_main.py`. [AgenticROS](../../entities/agenticros.md)'s `/estop` that bypasses the AI still has no counterpart here.
>
> *(Incidental but worth knowing: **"security" in the DimOS tree means the surveillance application**, not access control — `dimos/experimental/security_demo/`, `unitree_go2_security.py`. Searching for the word finds the opposite of what a reader expects.)*

## 4. Multi-homing: architecturally yes, which is exactly the problem

`McpServer` → any external MCP client → **DimOS is trivially multi-homed at the agent layer.** That confirms the framework's prediction that agent-layer multi-homing is the easy part.

It then lands straight in the gap [Matter](../../entities/matter.md) also has, with worse consequences. Two MCP clients concurrently invoking `relative_move` is the shared-unarbitrated-state problem **with a physical object attached** — and where Matter externalized arbitration to the triviality of a bulb's state, DimOS has no such excuse. Nothing in the ingested evidence arbitrates it.

By the framework's layer table, DimOS is unusual: it is multi-homeable at the command surface **and** hands over the world model, because `memory2` is just a file. That is either the most user-respecting posture in the category or the least governed one, depending entirely on whether an authority layer is added.

## 5. Trust: right capabilities, wrong defaults — twice

The framework's falsifiable predictor of trust is **local-first vs cloud**, because it is architectural and visible in a teardown.

- **Default LLM is `gpt-5.6-luna`** — cloud, `OPENAI_API_KEY`. A local path exists via [Ollama](../../entities/ollama.md) (`unitree-go2-agentic-ollama`) but is not the default.
- **dimTELE**: *"the robot dials out to a hosted broker, so no inbound ports need opening — works behind a home router, on Wi-Fi, wired LAN, or cellular."* Excellent NAT engineering. Read as trust architecture it is **a persistent outbound tunnel from inside the home to a vendor's server**, brokered with per-account API keys — and it is [Dimensional](../../entities/dimensional-inc.md)'s clearest business model.

**DimOS lands on the wrong side of both defaults while possessing the local capability for both.** Defaults are what ship.

Also absent: **any multi-tenancy.** The agent module carries `human_input: In[str]` — a single undifferentiated string channel. No identity, no per-person authority, nothing addressing the framework's third boundary (consent is household-level, not user-level).

## 6. Where it sits in the value chain

**Not the consumer product.** RTX 3000+ / 8 GB VRAM minimum, RTX 4070+ recommended, **[Jetson](../../entities/jetson-orin-nano.md) AGX Orin tested, Orin Nano experimental** — above the tier the wiki's low-cost platforms occupy ([onboard compute](../platforms/jetson-onboard-compute-xlerobot.md)). A $2,499 [Zeroth M1](../../entities/zeroth-m1.md) cannot run it.

DimOS is the **developer/integrator layer beneath** a home AI platform, not the platform. Its business model maps precisely onto the [value chain](../society/consumer-robotics-value-chain.md) page's Tier 2 — *give away the middleware, sell the hosted connectivity* — the same shape as [Vulcan Robotics](../../entities/vulcan-robotics.md)'s rented inference for [Sourccey](../../entities/sourccey.md). Two 2026 startups open-sourcing the hard engineering and monetizing what the robot cannot do for itself.

## Verdict

| Dimension | DimOS |
|---|---|
| Household world model | **Built** — `memory2`, premap, relocalization, locally owned |
| Auditability / incident reconstruction | **Best in the wiki** — inspectable state + full replay |
| Multi-homing surface | **Yes** — MCP, any client |
| Authority model | **Absent** — allow-by-decoration; CORS `*`, no auth middleware, no per-client scoping |
| Arbitration (concurrency) | **Present, and good** — `CapabilityRegistry`, `@skill(uses=[...])`, token-scoped holds, atomic acquire — but **`CAP_MOVEMENT` is the only capability declared** |
| E-stop | **Absent** — no estop/emergency/interlock path in the tree |
| Trust defaults | **Cloud on both** model and transport |
| Multi-tenancy | **Absent** |
| Consumer-tier compute | **No** — AGX Orin class |

**The single change that would make DimOS a credible home-AI substrate is an ARL-equivalent**: a per-client, deny-by-default restriction on which `@skill`s are reachable, declared separately from the code that implements them. [Matter](../../entities/matter.md) demonstrates the shape and demonstrates it ships at consumer scale. DimOS's discovery mechanism — its most elegant property — is the piece that would have to give.

## Open questions

- ~~**Does an auth/permission layer exist in the repo?**~~ **Answered 2026-08-17: no.** CORS `allow_origins=["*"]`, no auth middleware on either `/mcp` endpoint.
- ~~**Is there any preemption primitive?**~~ **Answered 2026-08-17: yes** — `CapabilityRegistry` with `@skill(uses=[...])`. The live question is now **why the capability vocabulary has exactly one entry**, and what breaks when two agents contend for an arm or a camera, neither of which is arbitrated.
- **What happens when two MCP clients issue conflicting skill calls?** Unmeasured and unspecified.
- **Would adding a VLA to the control loop destroy the auditability advantage?** Almost certainly yes, and DimOS's roadmap already feeds [LeRobot](../../entities/lerobot.md) v3.0 datasets. **The auditability property is an accident of not having done the thing the project is building toward.**
- **What is `gpt-5.6-luna`?** Named as the default in the agent docs; uncovered anywhere in this wiki.

## Related

- [The home AI platform — trust and authority](home-ai-platform-trust-and-authority.md) — the framework applied here
- [DimOS](../../entities/dimos.md) · [Dimensional Inc.](../../entities/dimensional-inc.md) · [DimOS repository](../../sources/dimos-github.md)
- [Matter](../../entities/matter.md) — the deny-by-default counterexample
- [LLM-agent architecture across stacks](llm-agent-architecture-across-stacks.md) · [Guardrails for robot agents](guardrails-for-robot-agents.md)
- [Consumer robotics value chain](../society/consumer-robotics-value-chain.md) — where Dimensional's business model sits
