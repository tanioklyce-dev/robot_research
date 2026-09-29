---
title: "Add Runtime Controls to AI Agents with NVIDIA OpenShell"
type: source
url: https://developer.nvidia.com/blog/add-runtime-controls-to-ai-agents-with-nvidia-openshell/
author: Alex Watson, Ali Golshan (NVIDIA)
published: 2026-09-28
ingested: 2026-09-29
venue: NVIDIA Technical Blog
format: blog post (technical walkthrough)
local_path: raw/2026-09-28-nvidia-blog-openshell-runtime-controls.md
sha256: 0667d50321470ed1b50bcd82a8f41e14ad4b23615d2e231fee8b8b50f9053510
tags: [nvidia, openshell, secure-runtime, sandbox, policy-enforcement, formal-verification, opa-rego, ocsf, mcp, credentials, agentic-ai, open-agent-safety-platform, robot-security]
---

# Add Runtime Controls to AI Agents with NVIDIA OpenShell

## Summary

The technical launch post for **[OpenShell](../entities/nvidia-openshell.md) 0.1.0**, the first versioned release after a long `0.0.x` preview. Published the same morning as the [Open Agent Safety Platform launch](nvidia-newsroom-open-agent-safety-platform.md), of which OpenShell is the runtime layer. It turns the [August architecture post](nvidia-where-security-fits-agent-stack.md)'s argument into software you can install. The claim is that you can put **enforceable permissions around an existing agent without rewriting it**: a sandbox with kernel-level filesystem and process controls, **no network path except through an out-of-process supervisor** that inspects HTTP / GraphQL / **MCP** traffic at the request level, credentials substituted outside the workload, and a **formal policy prover** that checks what a policy actually permits. This is the post that settles the wiki's open question of whether OpenShell ships ([backlog](../backlog.md)). It does: **Apache-2.0, written in Rust, on GitHub, with aarch64 Linux builds**. The GitHub facts come from the repo (checked 2026-09-29), not from the post.

## Key claims

**Architecture: three components** (§"Enforce permissions outside the agent")
- **Gateway**: manages the lifecycles and policies of many sandboxes (fleets, multi-tenant workspaces).
- **Supervisor**: one per sandbox, runs **outside the agent workload**, and checks every outbound request against policy.
- **Sandbox**: *"kernel-level controls over its filesystem and processes, and **no network path except through the supervisor**."* The controls persist when the agent opens a shell, runs generated code, spawns children, or delegates to sub-agents.

**Request-level (L7) network policy**
- Policies are written in YAML and **compiled to OPA/Rego**, then evaluated per outbound request. The worked example allows `/usr/bin/curl` to `GET api.github.com:443` and blocks `POST` through the same API with `protocol: rest`, `access: read-only`.
- Rules bind to a **binary path** as well as a host. The network rule says which program may talk, not only where.
- Denied requests can return a descriptive error, *"that helps the agent decide what to do next."*
- Audit goes to an **OCSF** (Open Cybersecurity Schema Framework) trail.

**Credentials never enter the workload** (§"Access services without exposing credentials")
- The agent holds a placeholder. The supervisor swaps in the real credential **only for an approved endpoint**, and a placeholder sent anywhere else is rejected.
- This control is separate from the credential's own scope: *"an inspected read-only API policy can block write requests even when the credential itself has write access."*
- A **provider profile** bundles credentials, endpoints and permitted programs, e.g. `openshell sandbox create --provider github -- codex`.

**Live policy change, human-gated** (§"Adjust network access while the agent runs")
- **Policy advisor**: when a request is denied, the agent may *propose* a narrowly scoped network or file policy change. The proposal waits for human review by default, and **"the agent cannot approve its own request."** Approved network rules hot-load without a restart.
- **Filesystem and process restrictions are fixed at sandbox start**; changing them requires a new sandbox.

> [!warning] Minor internal inconsistency
> The advisor can propose a "network **or file** policy change", which then loads into the running sandbox. Yet the next paragraph says filesystem controls are fixed at start. Two readings: file policy means something narrower than the kernel filesystem restrictions, or file proposals take effect only in a new sandbox. The post doesn't say which.

**Formal policy prover** (§"Verify the permissions a policy grants")
- The prover checks the permissions a policy grants, including access that providers contribute. It either proves they stay within an operator-defined boundary or produces **a concrete action that crosses it**. *"Because the result comes from the policy model, an agent's explanation cannot change that result."*
- The motivating failure: blocking a write through one tool is worthless if another permitted tool or generated code can make the same write with the same credential.
- **Adversarial result:** *"frontier agents with reduced safeguards spent **up to two hours** trying to persuade an AI reviewer to grant permissions"* to write a protected repo, and *"no protected repository writes occurred."* No run count, models, or methodology are given.
- **Ongoing work:** extending the analysis **across multiple agents** whose separate grants combine into a joint capability.

**Deployment surface**
- Compute drivers for **Docker, Podman, MicroVM, Kubernetes**. Workloads can run on CPUs or GPUs.
- *"Trusted middleware"* outside the sandbox connects identity services and adds application-specific checks to the request path.
- Supported agents: **Codex, Claude Code, Pi, [Hermes](../entities/hermes-agent.md)** (the [solutions page](nvidia-open-agent-safety-platform-page.md) adds OpenCode, GitHub Copilot CLI, [OpenClaw](../entities/openclaw.md)).
- Named adopters: **Cadence** (ChipStack RTL agent), **Slack** (on-demand agent platform), and **Gecko Robotics**, which *"uses OpenShell to govern agents making decisions on physical robots."* The scope line claims *"physical AI… robotics and edge systems."*
- Community: CNCF Slack `#openshell-dev`, which suggests a CNCF-adjacent governance path. The post doesn't state it.

**Repository facts (from GitHub, not the post; checked 2026-09-29)**
- `NVIDIA/OpenShell`: **Apache-2.0**, **Rust**, ~10k stars, repo created 2026-02-24.
- **v0.1.0 tagged 2026-09-25**, followed by v0.1.1 (09-26) and v0.1.2 (09-28). Before that, `v0.0.116` (2026-08-28).
- Release assets include **`aarch64-unknown-linux-musl`/`-gnu`** builds of the CLI, gateway and prover, plus a separate `openshell-prover` package.
- v0.1.0 changelog items: `feat(ci): add Codex Security release qualification`, sandbox templates, split gateway/workspace Helm charts, and `defaults-without-telemetry`.

## Entities mentioned

- [NVIDIA OpenShell](../entities/nvidia-openshell.md) · [NVIDIA](../entities/nvidia.md)
- [Hermes Agent](../entities/hermes-agent.md) · [OpenClaw](../entities/openclaw.md) (via the solutions page)
- Cadence, Slack, Gecko Robotics (no wiki pages)

## Concepts touched

- [AI guardrails](../concepts/safety/ai-guardrails.md): the behavioral/infrastructure split, now with code.
- [Robot security](../concepts/robotics/robot-security.md)
- [Agent–hardware abstraction](../concepts/agents/agent-hardware-abstraction.md): MCP traffic is inspectable at the supervisor.

## Analysis

**MCP inspection at the supervisor changes the robot story.** The wiki's [ROS 2 ↔ MCP server](../entities/ros2-mcp-server.md) enforces `policy.py` inside the server the agent calls. That is a behavioral control by the [August post](nvidia-where-security-fits-agent-stack.md)'s own test, because it lives in a process the agent reaches. With OpenShell, the same predicates could sit on the **supervisor's side of the wire** as an L7 MCP rule, and the agent would have no route around them. That is the cleanest reading yet of "put the control below the boundary" for this wiki's fleet. Whether OpenShell's MCP inspection can express *argument-level* predicates (for example `pick(obj)` where `obj ∉ knives`) rather than method-level allow/deny is **not stated**. That is the question to answer before relying on it.

**The prover proves the policy, not the agent.** The phrase "policies are formally verified" on the [solutions page](nvidia-open-agent-safety-platform-page.md) compresses this. The blog is careful: the prover reasons over the *policy model*, so it bounds what the sandbox will allow, not what the agent will attempt. Any path the model doesn't include is outside the proof. On a robot, that includes a motion command whose harm depends on world state.

**Still no latency number.** L7 inspection with per-request OPA evaluation is cheap at API rates. The post gives no per-request overhead figure, and the [solutions page](nvidia-open-agent-safety-platform-page.md) offers only "minimal overhead" and a Vera sandbox-speed claim. The [latency gap](../syntheses/agents/guardrails-for-robot-agents.md) flagged in August stays open.

## Open questions

- Can MCP rules match **tool arguments**, or only tool names and methods?
- Which kernel mechanisms does the sandbox use (Landlock, seccomp, namespaces), and **do they work on a JetPack L4T kernel**? The aarch64 builds exist; Jetson support is not claimed.
- What is the per-request supervisor overhead, and what is it on a ROS 2 control-adjacent path?
- Two-hour persuasion experiment: how many runs, which models, what reviewer?
- Can multi-agent policy analysis express *shared physical resources*? ([backlog item](../backlog.md) on child runtimes and one body)
