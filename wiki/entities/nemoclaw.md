---
title: NVIDIA NemoClaw
type: entity
subtype: software-framework
created: 2026-05-28
updated: 2026-07-04
sources: 2
status: early preview
tags: [nemoclaw, nvidia, openclaw, nemotron, nvidia-agent-toolkit, nvidia-openshell, guardrails, privacy, dgx-spark, rtx-pro, claw-ecosystem]
---

**NVIDIA NemoClaw** — NVIDIA's **open-source stack that wraps [OpenClaw](openclaw.md) with privacy and security controls + NVIDIA-native local-LLM inference**. *"Adds privacy and security controls to OpenClaw."* Early-preview status; no GA pricing / release date stated on the [product page](../sources/nvidia-nemoclaw-page.md).

> [!note] NemoClaw is a distribution of OpenClaw; the ROSOrin Pro stack uses a different mechanism
> NemoClaw is a desktop/workstation distribution of OpenClaw — it adds NVIDIA security + Nemotron local LLM. The ROSOrin Pro, by contrast, isn't a separate OpenClaw distribution at all — it runs stock upstream OpenClaw plus Hiwonder's [`openclaw_controller`](openclaw-controller.md) ROS 2 bridge module. So NemoClaw and `openclaw_controller` aren't peers: NemoClaw replaces the OpenClaw distribution; `openclaw_controller` is an extension that sits below any OpenClaw distribution.

## What it bundles

- **OpenClaw** — the underlying agent framework.
- **NVIDIA Agent Toolkit** — security infrastructure.
- **NVIDIA OpenShell** — open-source runtime for **policy-based guardrails**.
- **NVIDIA Nemotron** — NVIDIA's open-LLM family for privacy-preserving on-device inference.

## Target hardware

- **NVIDIA GeForce RTX** PCs / laptops.
- **NVIDIA RTX PRO** workstations.
- **NVIDIA DGX Station** and **[DGX Spark](dgx-spark.md)** systems.

Same compute matrix as the broader NVIDIA "agent on local hardware" pitch — runs on a single consumer GPU at the low end up to a DGX Spark at the high end.

## Value-add over plain OpenClaw

1. **Privacy / security controls** — policy-based guardrails via NVIDIA OpenShell.
2. **Always-on, self-evolving agents** — same continuous-improvement framing as [Hermes Agent](hermes-agent.md).
3. **Compute-aware deployment** — NemoClaw *"evaluates available compute resources to run high-performance open models like NVIDIA Nemotron locally."*
4. **NVIDIA Nemotron** as the default inference target rather than a cloud API.

## Agent variants (from the [Hermes quickstart](../sources/nvidia-nemoclaw-hermes-quickstart.md))

NemoClaw is not tied to one agent: `NEMOCLAW_AGENT` selects which agent runs in the OpenShell sandbox — **default OpenClaw**, or **[Hermes](hermes-agent.md)** via the `nemohermes` alias. Both can run side by side (distinct sandbox names). Each sandbox exposes a browser **dashboard (port 18789)** + an **OpenAI-compatible API (port 8642)**; the default model in the Hermes quickstart is **`nvidia/nemotron-3-super-120b-a12b`** served via **NVIDIA inference endpoints** (i.e., the quickstart's default is endpoint-hosted, distinct from the [product page](../sources/nvidia-nemoclaw-page.md)'s local-Nemotron-on-DGX-Spark pitch). **OpenShell** applies **network-policy tiers** gating each sandbox's egress and stores credentials in sandbox scope — the concrete form of the "policy-based guardrails" claim.

## Position in the Claw ecosystem

NemoClaw is the **NVIDIA-secured production wrapper** in the 3-project landscape:

| Project | Layer | License |
|---|---|---|
| [OpenClaw](openclaw.md) | Foundation | MIT |
| **NemoClaw** | NVIDIA security wrapper + Nemotron + hardware-aware deployment | (early preview) |
| [Hermes Agent](hermes-agent.md) | Competing sibling stack | MIT |

The interesting question (worth a future synthesis): is NemoClaw + OpenClaw NVIDIA's answer to Nous Research's bet on Hermes Agent, or is it cooperative (both are valid first-party paths to "agent on RTX hardware")?

## Robot-platform fit

**No robot integration documented.** Inherits OpenClaw's MCP / extension story — a robot integration would require writing an MCP server exposing ROS 2 actions / topics / services.

For the ROSOrin Pro use case specifically: NemoClaw is **not** a drop-in swap for the upstream [OpenClaw](openclaw.md) running there today — Hiwonder's [`openclaw_controller`](openclaw-controller.md) bridge talks to upstream OpenClaw, and a NemoClaw-side equivalent of the same ROS 2 wiring would need to be written. NemoClaw could theoretically be the planner brain in a future *robot-extended* version of itself, but not today.

## Related

- [OpenClaw](openclaw.md) — the framework NemoClaw wraps.
- [Hermes Agent](hermes-agent.md) — competing sibling stack.
- [openclaw_controller](openclaw-controller.md) — Hiwonder's ROS 2 bridge module (the robot-side mechanism that puts OpenClaw on a ROSOrin Pro).
- [NVIDIA](nvidia.md) — vendor.
- [DGX Spark](dgx-spark.md) — featured hardware target.
- [LLM-agent architecture](../concepts/agents/llm-agent-architecture.md) — concept.

## Mentioned in

- [NVIDIA NemoClaw product page](../sources/nvidia-nemoclaw-page.md) — primary source.
- [NemoClaw Quickstart with Hermes](../sources/nvidia-nemoclaw-hermes-quickstart.md) — concrete recipe (`nemohermes`, OpenShell sandbox, ports, Nemotron endpoint).

## Open questions

- **What's in the NVIDIA Agent Toolkit?** Not enumerated.
- **NVIDIA OpenShell policy language** — the quickstart confirms **network-policy tiers + presets** (allowlist-style egress control) but not the underlying policy language.
- **Nemotron model family** — the Hermes default is `nemotron-3-super-120b-a12b` (a 120B-total / 12B-active MoE); full family sizes/fp4-fp8 tiers still not enumerated.
- **GA timeline / pricing**.
- **Relationship to [Hermes Agent](hermes-agent.md)** — both NVIDIA blog-promoted; one cooperative, one competitive?
- **Robot extension** — none today; would close a real gap.
