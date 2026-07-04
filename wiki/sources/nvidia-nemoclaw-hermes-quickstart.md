---
title: NemoClaw Quickstart with Hermes (NVIDIA docs)
type: source
url: https://docs.nvidia.com/nemoclaw/user-guide/hermes/get-started/quickstart
author: NVIDIA
published: 2026 (docs, continuously updated)
ingested: 2026-07-04
format: web (docs)
tags: [nemoclaw, hermes-agent, openshell, nemotron, sandbox, local-agent, mcp, nvidia, claw-ecosystem]
---

## Summary

The concrete deployment recipe for running **[Hermes Agent](../entities/hermes-agent.md) inside [NVIDIA NemoClaw](../entities/nemoclaw.md)** — i.e., Hermes as a selectable agent variant in NemoClaw's OpenShell sandbox instead of the default OpenClaw agent. Resolves several NemoClaw/Hermes open questions in the wiki with primary-source detail: the `nemohermes` CLI (an alias for `nemoclaw` with Hermes pre-selected), the OpenShell containerized sandbox, dashboard (18789) + OpenAI-compatible API (8642) ports, network-policy tiers, and the default model **`nvidia/nemotron-3-super-120b-a12b`** served via NVIDIA inference endpoints. The deployment recipe underpinning the wiki's [on-device / on-robot / local-server agents synthesis](../syntheses/agents/on-device-and-on-robot-agents.md).

## Key claims

### What it deploys
- **Hermes = an agent variant in NemoClaw**, not a separate install: *"Use NemoHermes to create an OpenShell sandbox that runs Hermes instead of the default OpenClaw agent."* Selected via `export NEMOCLAW_AGENT=hermes`; `nemohermes` is an alias for `nemoclaw` with Hermes pre-selected. Hermes and OpenClaw sandboxes can run side by side (distinct sandbox names, e.g. `my-hermes`).
- **Install**: `export NEMOCLAW_AGENT=hermes && curl -fsSL https://www.nvidia.com/nemoclaw.sh | bash`. Requires **Docker** (installer can add the user to the `docker` group on Linux; macOS needs Docker Desktop/Colima). First build takes several minutes (sandbox base image).

### Architecture / runtime
- Runs in an **OpenShell sandbox** (Linux container + Python runtime), **not purely on-device**. Exposes a **browser dashboard on port 18789** and an **OpenAI-compatible REST API on port 8642** (`/v1`, `/health`).
- Model traffic routed via `inference.local`; reaches Nous Research service endpoints, PyPI, NVIDIA inference endpoints. Default example model **`nvidia/nemotron-3-super-120b-a12b`** (NVIDIA Endpoints — cloud, not local-hardware-pinned). `nemohermes inference set --model <model> --provider <provider>` reconfigures (patches `/sandbox/.hermes/config.yaml`).
- Tools/skills: web search (Tavily or Nous-managed), plus image gen / audio / browser automation / managed code execution via Nous gateways. **MCP server** at `docs.nvidia.com/nemoclaw/_mcp/server`.

### Security (OpenShell policy)
- **Agent-specific baseline policy** allows only the Hermes binary + Python runtime to reach required endpoints (Nous services, PyPI, NVIDIA inference, selected messaging APIs). **Network-policy tiers + presets** chosen during onboarding; credentials (`TAVILY_API_KEY`, `NVIDIA_INFERENCE_API_KEY`) validated and **stored in sandbox scope**. Dashboard is a local management UI — *"avoid exposing it on shared or public networks unless you put it behind your own access controls."*
- Hermes dashboard auth uses **bearer tokens** (vs OpenClaw's URL-fragment tokens).

### Lifecycle commands
`nemohermes onboard [--resume|--recreate-sandbox --fresh]`; `nemohermes my-hermes connect|status|logs --follow|rebuild|destroy`; `snapshot create --name …`; `dashboard-url`; `policy-add`; `credentials reset <KEY>`; API health `curl -sf http://127.0.0.1:8642/health`.

## Entities mentioned
- [Hermes Agent](../entities/hermes-agent.md) (Nous Research), [NVIDIA NemoClaw](../entities/nemoclaw.md), [OpenClaw](../entities/openclaw.md) — the Claw ecosystem. [Nous Research](../entities/nous-research.md).
- NVIDIA OpenShell (sandbox + policy layer), `nvidia/nemotron-3-super-120b-a12b` (default model), Tavily Search, Nous Portal OAuth, MCP.

## Concepts touched
- [LLM-agent architecture](../concepts/agents/llm-agent-architecture.md) — MCP tool-calling agent in a sandbox; the local/endpoint-inference deployment shape.
- The **local-AI-server** node in the [on-device / on-robot / local-server agents synthesis](../syntheses/agents/on-device-and-on-robot-agents.md).

## Open questions
- **This quickstart is hardware-agnostic** — it routes to NVIDIA *endpoints*, so the "local Nemotron on DGX Spark" story from the [NemoClaw product page](nvidia-nemoclaw-page.md) is the *other* deployment mode; the quickstart's default is endpoint-hosted Nemotron, not on-device.
- Supported messaging platforms referenced but not enumerated here.
- No robot integration — same MCP-server-over-ROS-2 gap as the rest of the Claw ecosystem.
