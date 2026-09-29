---
title: NVIDIA OpenShell
type: entity
subtype: software-framework
created: 2026-08-23
updated: 2026-09-29
sources: 7
tags: [nvidia, openshell, open-agent-safety-platform, formal-verification, opa-rego, mcp, secure-runtime, sandbox, policy-enforcement, guardrails, agentic-ai, nemoclaw, hermes-agent, least-privilege, audit]
---

**NVIDIA OpenShell** — the **secure runtime** layer of NVIDIA's agent stack: a containerized sandbox that owns isolation, identity, policy, credentials and audit for an AI agent, and inside which the agent's harness runs. Its design claim is positional — *"[a] control that the agent can decline to invoke is not an effective security control"* ([Where Security Fits in an AI Agent Stack](../sources/nvidia-where-security-fits-agent-stack.md)) — so the runtime is created **before** the harness starts, by an orchestrator, and the harness plus its plugins, MCP processes and tools all start inside that boundary.

> [!note] Resolves a wiki open question: OpenShell is *not* NeMo Guardrails renamed
> [The NemoClaw product page](../sources/nvidia-nemoclaw-page.md) left this unconfirmed — was OpenShell's "policy-based guardrails" the same thing as [NeMo Guardrails](nemo-guardrails.md) under another name? The 2026-08 architecture post answers it by placement: **NeMo Guardrails is a rail engine that runs in the harness layer** (Colang, input/dialog/retrieval/execution/output rails, shaping text); **OpenShell is the runtime layer beneath it** (isolation, identity, credentials, audit, network policy). Different jobs on opposite sides of the security boundary — and by the post's own argument, only OpenShell's side is authoritative.

## What it does

| Responsibility | Evidence |
|---|---|
| **Container isolation** | Linux container + Python runtime per sandbox; named sandboxes can run side by side ([Hermes quickstart](../sources/nvidia-nemoclaw-hermes-quickstart.md)) |
| **Network policy** | Agent-specific baseline policy allowing only the agent binary + runtime to reach named endpoints; **network-policy tiers + presets** chosen at onboarding |
| **Credential scoping** | API keys validated and **stored in sandbox scope**, not handed to the agent — *"keeping the raw credential out of the agent's reach creates a stronger boundary"* |
| **Delegation ceilings** | Subagents receive **child runtimes with ceilings they cannot exceed** |
| **Recovery** | `snapshot create`, `rebuild`, `destroy`, `credentials reset <KEY>`, `policy-add` ([Hermes quickstart](../sources/nvidia-nemoclaw-hermes-quickstart.md)) |
| **Audit** | *"independent evidence… immutable records below the security boundary"* |

The four escalating **security profiles** (Isolated / Connected / Production / Adversarial) are defined against this runtime — same stack and interfaces at every level, differing in authority granted, freshness of policy evaluation, oversight, and recovery speed. See the [source page](../sources/nvidia-where-security-fits-agent-stack.md) for the table.

## Where it shows up in this wiki

- **[NemoClaw](nemoclaw.md)** bundles it as the privacy/security half of NVIDIA's [OpenClaw](openclaw.md) distribution — the article now classifies NemoClaw as the *distribution/product* layer sitting above OpenShell.
- **[Hermes Agent](hermes-agent.md)** is the concrete, documented case: `nemohermes onboard` **creates an OpenShell sandbox and runs Hermes inside it** ([quickstart](../sources/nvidia-nemoclaw-hermes-quickstart.md)). That deployment recipe predates the architecture post and independently demonstrates its central move — the harness starts inside the runtime, not the other way round.

## Status — shipped (updated 2026-09-29)

> [!note] Supersedes the August "no GA artifact" hedge
> **OpenShell 0.1.0 shipped on 2026-09-25**, launched on 2026-09-28 as the runtime layer of the **NVIDIA Open Agent Safety Platform**, and described as *"now broadly available"* ([newsroom](../sources/nvidia-newsroom-open-agent-safety-platform.md)). The repo is `NVIDIA/OpenShell`, **Apache-2.0**, written in **Rust**, and ships **aarch64 Linux builds** (GitHub, checked 2026-09-29; see the [walkthrough page](../sources/nvidia-openshell-runtime-controls-blog.md)). The August hedge was partly a gap in the wiki: `0.0.x` releases were already on GitHub (v0.0.116 on 2026-08-28), but no ingested source said so.

It **does not require BlueField-4**. It runs on local, on-prem, cloud and Kubernetes infrastructure ([solutions page](../sources/nvidia-open-agent-safety-platform-page.md)). The optional hardware layer beneath it is **[NVIDIA Sentry](nvidia-sentry.md)** on [BlueField-4](nvidia-bluefield.md).

## Architecture (0.1.0)

From the [technical walkthrough](../sources/nvidia-openshell-runtime-controls-blog.md):

- **Gateway** manages sandbox lifecycles and policies across fleets and workspaces. **Supervisor** runs one per sandbox, *outside* the workload, and checks every outbound request. **Sandbox** applies kernel-level filesystem and process controls and has **no network path except through the supervisor**.
- **L7 policy.** YAML is compiled to **OPA/Rego** and evaluated per request. It can inspect **HTTP, GraphQL and MCP**, so it can allow a read and block a write through the same API. Rules bind a **binary path** as well as a host. Audit is recorded in **OCSF**.
- **Credential substitution.** The agent holds a placeholder, and the real secret is swapped in only for approved endpoints.
- **Policy advisor.** The agent may *propose* a scoped rule change. The default is human review, and *"the agent cannot approve its own request."* Network rules hot-load; filesystem and process limits need a new sandbox. Enterprise deployments can enable auto-approval within pre-approved limits ([solutions page](../sources/nvidia-open-agent-safety-platform-page.md)). Slack integration surfaces approvals to humans ([newsroom](../sources/nvidia-newsroom-open-agent-safety-platform.md)).
- **Policy prover.** Formal analysis of what a policy *permits*: it proves the policy stays inside a boundary or produces a counter-example action. It proves the policy model, not the agent's behavior (see the [scope-loss note](../sources/nvidia-open-agent-safety-platform-page.md)). Multi-agent composition is in progress.
- **Compute drivers**: Docker, Podman, MicroVM, Kubernetes. **Supported agents**: Claude Code, Codex, OpenCode, Copilot CLI, Pi, [Hermes](hermes-agent.md), [OpenClaw](openclaw.md).

**Adopters with a robotics angle:** Gecko Robotics (*"govern agents making decisions on physical robots"*), [Figure](figure.md) and [Skild AI](skild-ai.md) (*"building with OpenShell,"* one sentence, no detail) ([newsroom](../sources/nvidia-newsroom-open-agent-safety-platform.md)).

## For robots

OpenShell is the closest thing in this wiki to the **enforcement layer** that [guardrails for robot agents](../syntheses/agents/guardrails-for-robot-agents.md) says ships empty and [the home-AI platform analysis](../syntheses/agents/home-ai-platform-trust-and-authority.md) calls "mostly aspirational." Its boundary is drawn around **processes, files, networks and credentials** — the right shape for a robot's *planning* layer, and the wrong shape for its *control* layer, where the effects are continuous joint commands at [rates](../syntheses/platforms/control-rate-ladder.md) no policy engine is going to evaluate per item. Nothing published says where the line falls for an embodied agent. The 2026-09 launch names robot companies as adopters and still doesn't say.

**MCP inspection is the new handle.** The fleet's [ROS 2 ↔ MCP server](ros2-mcp-server.md) enforces its `policy.py` inside a process the agent calls, which makes it behavioral by the August test. OpenShell's supervisor can inspect MCP traffic from outside the sandbox. If its rules can match tool *arguments* and not only method names (not stated), the fleet's predicates could move below the boundary unchanged. Whether the sandbox's kernel controls work on a JetPack L4T kernel is untested; aarch64 builds exist. See [the walkthrough's analysis](../sources/nvidia-openshell-runtime-controls-blog.md).

## Related

- [NVIDIA Sentry](nvidia-sentry.md) — the out-of-band hardware layer · [NVIDIA BlueField](nvidia-bluefield.md)
- [NemoClaw](nemoclaw.md) · [OpenClaw](openclaw.md) · [Hermes Agent](hermes-agent.md) · [NVIDIA](nvidia.md)
- [NeMo Guardrails](nemo-guardrails.md) — the layer above · [garak](garak.md) — the red-team tool
- [AI guardrails](../concepts/safety/ai-guardrails.md) · [Robot security](../concepts/robotics/robot-security.md)
- [NVIDIA's two safety stacks](../syntheses/agents/nvidia-two-safety-stacks-halos-vs-agent-safety.md): how OpenShell relates to Halos on a robot

## Mentioned in

- [Where Security Fits in an AI Agent Stack](../sources/nvidia-where-security-fits-agent-stack.md)
- [NemoClaw Quickstart with Hermes](../sources/nvidia-nemoclaw-hermes-quickstart.md)
- [NVIDIA NemoClaw — Product Page](../sources/nvidia-nemoclaw-page.md)
- [Add Runtime Controls to AI Agents with NVIDIA OpenShell](../sources/nvidia-openshell-runtime-controls-blog.md)
- [NVIDIA Open Agent Safety Platform: A Reference for Continuous In-Silicon Agent Monitoring](../sources/nvidia-open-agent-safety-platform-sentry-blog.md)
- [NVIDIA Launches Open Agent Safety Platform (Newsroom)](../sources/nvidia-newsroom-open-agent-safety-platform.md)
- [NVIDIA Open Agent Safety Platform — Solutions Page](../sources/nvidia-open-agent-safety-platform-page.md)
