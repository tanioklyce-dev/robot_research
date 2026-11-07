---
title: sparkDash
type: entity
subtype: software
created: 2026-11-07
updated: 2026-11-07
sources: 2
tags: [sparkdash, dgx-spark, gb10, monitoring, dashboard, open-source, apache-2, llm-serving, agent-security]
---

# sparkDash

**sparkDash** is an open-source (Apache-2.0) real-time web dashboard for one or more [NVIDIA DGX Spark](dgx-spark.md) (GB10) units, from Mia's AI Lab (GitHub `MiaAI-Lab`, 840 stars, created 2026-07-19). It streams GPU, CPU, unified-memory, storage, network and **local LLM** metrics. Units can be added or reordered from the UI without restarts.

## Scope (per the upstream [README](../sources/sparkdash-github.md))
- **Monitored hosts.** DGX Sparks, plus dedicated-GPU Linux hosts (RAM and VRAM shown separately), Windows PCs (including AMD-iGPU hosts) and Apple Silicon Macs over SSH, with an optional on-device agent.
- **Integrations.** LLM server presets with backend auto-detection, ComfyUI, **[Hermes Agent](hermes-agent.md) monitoring**, Tailnet and Tailscale Serve, a mobile PWA, a kiosk mode, Glance, Home Assistant/MQTT, Prometheus, alert notifications, wall-power meters, RoCE/RDMA and Intel Arc.
- **Stack.** React 19 and Express 5 in a single **privileged** Docker container (arm64 or amd64). It binds loopback on port 5555 by default, and SSH to remote units runs inside the container as root.
- **Engines and benchmarks.** It auto-detects 14+ inference engines (vLLM, SGLang, llama.cpp, LM Studio, Ollama, NVIDIA Flare and others) and reads KV-cache, queue and latency p95 from their `/metrics`. Benchmarks: decode, prefill, a seeded **Quality** bench (~755 items, McNemar paired comparison) and a **Tool Eval Bench** for tool calling.
- **Agent harnesses.** A read-only occupancy helper lists sessions from [OpenClaw](openclaw.md), OpenCode, oh-my-pi, Hermes and DeepSeek Harness.
- **Security defaults.** A LAN bind with no `SPARKDASH_TOKEN` is **open by default**: anyone who can reach it *"can read telemetry, change settings and power units off."* SSH passwords are AES-256-GCM-encrypted ([sparkDash README](../sources/sparkdash-github.md)).
- **Release lag.** The README documents v2.70.0, while the newest GitHub release is v2.32.0 (2026-10-10) and has no published container image yet.

## Spark Overseer (proposed, PR #284, not merged)
A contributed opt-in page of security **observations** for instrumented local model workloads ([PR #284](../sources/sparkdash-pr284-spark-overseer.md)).
- **How it works.** A command wrapper sits at the tool-execution boundary, an adapter inspects `tool_calls` in OpenAI-compatible responses, and seven deterministic regex signals flag things like uploads and credential paths.
- **What it is not.** The PR is explicit that it is not enforcement. It does not fail closed, and a same-user agent can bypass it.
- **Review status.** The maintainer verified the privacy boundary. The PR is held on lockfile churn and a collector latch bug, and has since stopped merging cleanly.

## Why it matters for this wiki
- **The operational picture.** It shows what a local-agent fleet looks like in practice: engines, KV pressure, harness sessions and energy cost on one page. Its *"preserve unknown or failed measurements instead of presenting them as healthy"* rule (AGENTS.md) is the same discipline the wiki asks of evaluation.
- **A Spark-fleet tool.** It is the practical monitoring layer for the Spark-as-agent-host pattern on the [DGX Spark](dgx-spark.md) page.
- **Overseer illustrates a point the wiki keeps making.** In [AI guardrails](../concepts/safety/ai-guardrails.md), observation and advisory layers are useful only if they are honest about not being controls. This PR is a rare example that states it unprompted.

## Related
- [DGX Spark](dgx-spark.md) · [Hermes Agent](hermes-agent.md) · [NVIDIA OpenShell](nvidia-openshell.md) (enforcement, by contrast)

## Mentioned in
- [sparkDash PR #284 — Spark Overseer](../sources/sparkdash-pr284-spark-overseer.md)
- [sparkDash README](../sources/sparkdash-github.md) — the repository: architecture, engines, benchmarks, harness sessions and security model.
