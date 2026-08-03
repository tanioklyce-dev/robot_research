---
title: LLM-agent architecture
type: concept
created: 2026-05-07
updated: 2026-08-03
sources: 40
tags: [llm-agent, tool-use, agentic-robotics, planning, mcp, a2a, code-as-policy]
---

**LLM-agent architecture for robots** — a control pattern in which a large language model converts natural-language goals into sequences of tool calls that a deterministic executor runs against perception/manipulation primitives. Distinct from end-to-end [VLA models](../learning/vla-models.md) (which output low-level actions directly) and from [world-model simulators](../world-models/world-model-simulators.md) (which generate the training environment).

## Pattern
1. User states a goal in natural language ("pick up the toy chicken and put it in the basket").
2. LLM is prompted with the goal plus a tool-call schema.
3. LLM emits a sequence of structured calls: `find(toy_chicken)`, `pickup(toy_chicken)`, `place(basket)`, etc.
4. Executor (often a finite-state machine) dispatches each call to a deterministic skill module: navigation, grasping, perception.
5. Skills run on real hardware or in simulation; failures bubble back as observations the LLM can re-plan over.

## Concrete examples
- **[stretch_ai](../../entities/stretch-ai.md)'s LLM agent** ([Hello Robot](../../entities/hello-robot.md), research tier) — `PickupExecutor` + `PickupTask` FSM, with [Qwen2.5-3B-Instruct](../../entities/qwen.md) / Gemma / GPT-4o-mini as the planner ([Stretch AI LLM Agent Documentation](../../sources/stretch-ai-llm-agent-docs.md)). Tool primitives: `pickup`, `explore`, `place`, `say`, `find`, `go_home`, etc.
- **[Hiwonder ROSOrin](../../entities/rosorin.md)'s embodied-AI demos** ([Hiwonder](../../entities/hiwonder.md), educational tier, mobile-only) — same JSON tool-call pattern: LLM emits `{action: [...], response: ...}`, executor dispatches each call via `eval(f'self.{a}')`. Both cloud (GPT-4o, [Qwen-plus](../../entities/qwen.md), StepFun VLM) and offline ([Ollama](../../entities/ollama.md) + [qwen3:1.7b](../../entities/qwen.md) + sherpa-onnx) variants ([Hiwonder ROSOrin Documentation](../../sources/hiwonder-rosorin-docs.md)).
- **[OpenClaw](../../entities/openclaw.md) on [ROSOrin Pro](../../entities/rosorin-pro.md)** (educational tier, mobile + 6-DOF arm; upstream OpenClaw plus [Hiwonder](../../entities/hiwonder.md)'s [`openclaw_controller`](../../entities/openclaw-controller.md) ROS 2 bridge module) — same architecture, manipulation-capable. Skill library expands to include `pick`, `place`, `voice_pick`, `voice_give`, plus AprilTag pickup and depth-based interactive grasping. ROS 2 services like `/start_pick`, `/place`, `/claw_track_and_grab/start` ([Hiwonder OpenClaw Practical Tutorial](../../sources/hiwonder-openclaw-tutorial.md)).
- **[Gemini Robotics-ER 1.5](../../entities/gemini-robotics.md) on [Spot](../../entities/spot.md)** ([Boston Dynamics](../../entities/boston-dynamics.md), commercial quadruped tier) — same architecture using a *frontier-grade* multimodal model from [Google DeepMind](../../entities/google-deepmind.md). A thin layer over the Spot SDK exposes `GoTo`, `TakePicture`, object identification, `Pickup`, `PutDown`. Demonstrated cleaning a residential living room from handwritten task lists ("make sure all the shoes at the front door are on the shoe rack") ([Spot + Gemini Robotics blog](../../sources/bostondynamics-spot-gemini-robotics.md)). Productized as Boston Dynamics' AIVI-Learning with ER 1.6.

- **[Waddle](../../entities/waddle-labs.md)'s agent** ([Waddle Labs](../../entities/waddle-labs.md), commercial API tier) — the same planner-over-a-skill-library pattern, with two distinctive moves: the action vocabulary is **executable code, not a fixed JSON tool schema** (see [code as policy](code-as-policy.md)), and the skill library is **agent-authored and shared across all agents**, growing from experience. The agent decomposes goals, writes control code, and *calls [VLAs](../learning/vla-models.md) as tools* — so VLAs sit *below* the planner rather than competing with it. Reported as a deployed system (robots via API); no success rates given ([Introducing Waddle](../../sources/waddle-labs-introducing-waddle.md)).

The pattern is **converging across tiers, capabilities, and price points** — research-grade (stretch_ai), educational (ROSOrin / OpenClaw), and commercial-quadruped-grade (Spot + Gemini Robotics) stacks adopt the same architecture; mobile-only and arm-equipped variants adopt the same architecture; open-weights small LLMs ([Qwen](../../entities/qwen.md) 1.7B / 3B local) and frontier closed-weights VLMs (Gemini Robotics-ER, GPT-4o) plug into the same slot. The only differences are the size and contents of the skill library and the planner model.

> [!note] On naming: Google calls this "embodied reasoning" (Gemini Robotics-**ER**). Functionally it is the LLM-agent / planner-emits-tool-calls pattern documented above. The framing is a vendor branding choice, not a new architecture.

## Non-robotics example: agent-driven ML research

The same control pattern works outside robotics. **[Karpathy's autoresearch (March 2026)](../../sources/karpathy-autoresearch.md)** is the most distilled example in the wiki: an AI coding agent ([Claude Code](../../entities/anthropic.md) or Codex) is pointed at a `program.md` instruction file and given a small but real LLM training pipeline (a simplified [nanochat](../../sources/karpathy-nanochat.md)). The "tool calls" the agent makes are `edit train.py`, `run 5-minute experiment`, `compare val_bpb`, `keep or revert`. Over ~100 overnight iterations, this loop produced **two leaderboard improvements on the nanochat GPT-2 speedrun** (rows 5–6: 2.02 → 1.80 → 1.65 hours wall-clock), the first public evidence that a coding-agent loop can produce measurable improvements on a frontier ML training pipeline.

The robotics variant of the pattern uses `find / pickup / place` tool primitives over a perception+manipulation skill library; autoresearch uses `edit / train / measure / commit` tool primitives over a training pipeline. **Same control flow, different action vocabulary.** The pattern's robustness across these very different domains is one of the strongest signals that "LLM-emits-actions-against-a-skill-library" is a load-bearing architectural primitive of 2026 AI systems, not a robotics-specific trick.

The [Onchain AI Garage LeWM reproduction](../../sources/onchain-ai-garage-lewm-reproduction.md) is an independent occurrence of the same pattern applied to a different ML target (reproducing a JEPA world model), supporting the same generality claim.

## Inter-agent communication protocols

As LLM agents proliferate, two complementary protocols have emerged to connect them to external resources and to each other:

### MCP — Model Context Protocol
- Developed by **Anthropic**.
- Standard interface for LLMs to access external tools, data sources, cloud storage, financial systems, IoT, and enterprise services.
- **>1,000 community-built connectors** available (as of 2025).
- In a robotics context, MCP is the natural connector layer for an LLM-agent robot to call external APIs (maps, object databases, smart-home systems) without custom integration per tool.
- The direction also runs inward: **ROS 2↔MCP bridges expose the robot itself as MCP tools** — first-party [ros2-mcp-server](../../entities/ros2-mcp-server.md) (manipulation-first) and community [AgenticROS](../../entities/agenticros.md) (nav-first, six agent platforms; [source](../../sources/agenticros-github.md)).

### A2A — Agent-to-Agent Protocol
- Backed by **Google**; **50+ corporate supporters** including Microsoft, Salesforce, and SAP.
- Enables AI agents to discover each other and coordinate — one agent can delegate subtasks to another agent via a standardized handoff.
- Relevant to multi-robot or heterogeneous-fleet architectures where a high-level planner (cloud LLM) delegates to a low-level executor (on-device LLM agent on the robot).

These protocols represent the infrastructure layer that makes "networked AI" — multiple cooperating agents — practical at scale. Primary source: [Are We Building Skynet? (Medium, 2025)](../../sources/medium-are-we-building-skynet.md) (secondary journalism; MCP and A2A facts corroborated by Anthropic and Google public documentation).

## The missing layer: guardrails on the planner

Every implementation above shares an omission. The pattern is *LLM → tool call → actuator*, and in none of the ingested sources is there anything **between** the LLM and the skill library: no input sanitization, no policy check on the emitted tool call, no jailbreak detector. The planner's context is filled from user speech and from perception (OCR'd labels, VLM scene descriptions), and whatever comes out is dispatched — in ROSOrin's case literally via `eval(f'self.{a}')` ([Hiwonder ROSOrin Documentation](../../sources/hiwonder-rosorin-docs.md)).

The [NVIDIA safety recipe](../../sources/nvidia-safety-recipe-agentic-ai.md) and the [NeMo Guardrails library docs](../../sources/nemo-guardrails-library-overview.md) are the wiki's primary sources on what the missing layer looks like in industry: a build→deploy→run lifecycle ending in [runtime guardrails](../safety/ai-guardrails.md) — content safety, topic control, jailbreak detection, PII — plus an **execution rail** that validates tool calls before they run. **Full treatment: [Guardrails for robot agents](../../syntheses/agents/guardrails-for-robot-agents.md).**

Two things follow for robots specifically:

- **[Prompt injection](../safety/ai-red-teaming.md) becomes physical.** A chat agent's untrusted input arrives in the user's message. A robot's planner ingests text from *the environment* — signage, labels, screens, whiteboards — so the attack is available to anyone who can **leave a note where the robot will look**.
- **The guard models don't cover the dangerous channel.** Every shipped guardrail *model* classifies text; the robot's harmful output is a *tool call* (`pickup(knife)`, `drive(toward_stairs)`). The execution rail is the right hook and it does exist — but it ships **empty**, as a place to put your own Python function, because "is this tool call safe" is irreducibly domain-specific. In practice this job falls to hand-written preconditions in the skill library, or to the deterministic [machinery-safety layer (ISO 13482)](../robotics/robot-safety-standards.md), a separate stack that knows nothing about LLMs. A robot that satisfies ISO 13482 will not crush you; nothing in it stops the planner from calmly deciding to put your medication in the trash.
- **An MCP allowlist *is* an execution rail** — a static, name-level one. The [fleet's ros2-mcp-server](../../syntheses/projects/ros2-mcp-server-design.md) ("the tool set *is* the safety boundary", deterministic `name→handler` dispatch, out-of-band `stop`) independently derived most of the properties NVIDIA's execution rail asks for. What it still lacks is **argument-level and world-state-level** policy: `pick(knife)` and `place(cup, on=laptop)` pass any name-level allowlist.

> [!note] Unmeasured, not merely unmitigated
> No ingested source red-teams an embodied LLM agent. The wiki cannot say how exploitable these stacks are — only that none of them appear to have looked.

## Trade-offs vs. VLA
- **Pro**: composes with battle-tested classical perception/manipulation; LLM only needs symbolic-level reasoning.
- **Pro**: easy to swap LLMs (just change the API); easier to debug than end-to-end policies.
- **Con**: action vocabulary is hand-engineered; new skills require new primitives.
- **Con**: closed-loop replanning depends on how cleanly skill failures surface to the LLM.

## Related
- [Code as policy](code-as-policy.md) — the sub-pattern where the action vocabulary is *arbitrary code* rather than a fixed tool schema (Code as Policies → Voyager → CaP-X/ASPIRE → [Waddle](../../entities/waddle-labs.md)).
- [VLA models](../learning/vla-models.md) — competing paradigm (end-to-end action prediction).
- [On-device / on-robot / local-server agents](../../syntheses/agents/on-device-and-on-robot-agents.md) — *where* the agent brain runs (edge vs LAN server vs cloud); the deployment-topology companion.
- [Fleet agentic control framework](../../syntheses/projects/fleet-agentic-framework.md) — a full multi-robot build of this pattern (per-robot MCP servers + a DGX Spark master).
- [stretch_ai](../../entities/stretch-ai.md) — concrete implementation.
- [World-model simulators](../world-models/world-model-simulators.md) — orthogonal (training-environment paradigm, not control paradigm).
- [AI safety and alignment](../safety/ai-safety-alignment.md) — safety properties of the LLM brain matter when it has real-world tool access via MCP.
- [Guardrails for robot agents](../../syntheses/agents/guardrails-for-robot-agents.md) — **the synthesis**: the five-layer safety cake, why the MCP allowlist is already an execution rail, and the unguarded perception channel.
- [AI guardrails](../safety/ai-guardrails.md) — the enforcement layer that *should* sit between the planner and the skill library, and currently doesn't.
- [AI red-teaming](../safety/ai-red-teaming.md) — prompt injection through the perception channel is this pattern's distinctive attack surface.
- [Strange loops and self-reference](strange-loops-and-self-reference.md) — the *structural* reading of this control pattern: the model's own output re-enters as its input, which is what people are naming when they call an agent "agentic." Includes the deflationary counter (a loop in the transcript is not necessarily a loop in the system).
- [Control abstraction levels](../robotics/control-abstraction-levels.md) — where this pattern sits on the ladder (level 3, "policy control"), and the measured cost of overriding the layer below.
- [AI uplift studies](../safety/ai-uplift.md) — the **other** way an LLM touches a robot: writing the code offline rather than sitting in the control loop. [Project Fetch](../../sources/anthropic-project-fetch-robot-dog.md) measures that mode, and argues it is the leading indicator for this one — *uplift precedes autonomy*. Notably, the biggest measured gap was in **connecting to unfamiliar hardware and reading its sensors**, i.e. exactly the integration layer this pattern assumes already exists.

## Mentioned in
- [AI is a Strange Loop (Carroll, 2026)](../../sources/arcnem-strange-loops-ai-agents.md) — names this loop Observe→Reason→Act→Evaluate and argues the self-reference *is* the agency.
- [How Claude Performs on Robotics Tasks](../../sources/anthropic-how-claude-performs-on-robotics-tasks.md) — this pattern **measured**: an LLM supervising a pretrained [MolmoAct](../../entities/molmoact.md) policy scores *worse* than the policy alone in-distribution, better on novel tasks. Knowing when **not** to override is the skill.
- [Stretch AI LLM Agent Documentation](../../sources/stretch-ai-llm-agent-docs.md)
- [Hiwonder ROSOrin Documentation](../../sources/hiwonder-rosorin-docs.md)
- [Hiwonder OpenClaw Practical Tutorial](../../sources/hiwonder-openclaw-tutorial.md)
- [Are We Building Skynet? (Medium, 2025)](../../sources/medium-are-we-building-skynet.md)
- [Tools for Your To Do List with Spot and Gemini Robotics (Boston Dynamics blog)](../../sources/bostondynamics-spot-gemini-robotics.md)
- [AgenticROS GitHub](../../sources/agenticros-github.md)
- [Awesome-Embodied-Robotics-and-Agent](../../sources/awesome-embodied-robotics-agent.md) — community-curated external index of the same LLM/VLM-embodied-agent landscape; useful coverage cross-check.
- [Safeguard Agentic AI Systems with the NVIDIA Safety Recipe](../../sources/nvidia-safety-recipe-agentic-ai.md) — the guardrail layer this pattern lacks.
- [NeMo Guardrails — Library Overview](../../sources/nemo-guardrails-library-overview.md) — execution rails, tool-call validation, LangGraph multi-agent safety.
- [Project Fetch: Can Claude train a robot dog?](../../sources/anthropic-project-fetch-robot-dog.md) — the contrast case: Claude writes the robot code, but never runs in the loop.
- [Introducing Waddle — Agents that Control Robots](../../sources/waddle-labs-introducing-waddle.md) — a deployed commercial instance: code-as-actions planner + a shared, agent-authored skill library, calling VLAs as tools.
