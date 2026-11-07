---
title: "MiaAI-Lab/sparkDash — multi-unit DGX Spark monitoring dashboard (GitHub README)"
type: source
url: https://github.com/MiaAI-Lab/sparkDash
fetch_url: https://raw.githubusercontent.com/MiaAI-Lab/sparkDash/main/README.md
local_path: raw/2026-11-07-sparkdash-readme.md
sha256: c883105c3f5b37141a7c969f581d122ecff0b1d4eefe169ec9e5330479013b5f
author: "Mia's AI Lab (MiaAI-Lab); macOS collectors by C. Michael Gibbs and Nyx Voss (Onyx AI Labs); ~40 contributors"
published: 2026-07-19
venue: "GitHub repository (Apache-2.0; some files MIT per LICENSE-MIT); homepage mia-ai.net"
format: "README (1,475 lines), AGENTS.md excerpt, top-level file list, GitHub API metadata (stars, forks, releases, contributors)"
license: Apache-2.0
github_stats: "840 stars, 201 forks, 15 open issues, 31 open PRs; created 2026-07-19; main head e89f8d1 (2026-11-06); latest GitHub release v2.32.0 (2026-10-10) while the README changelog is at 2.70.0; top committers MiaAI-Lab 283, oscarlius 62, MikeGibbsOnyx 53"
tags: [sparkdash, dgx-spark, gb10, monitoring, dashboard, llm-serving, vllm, sglang, llama-cpp, ollama, benchmarks, tool-calling-eval, hermes-agent, openclaw, agent-harness, tailscale, prometheus, home-assistant, security, apache-2]
ingested: 2026-11-07
---

# MiaAI-Lab/sparkDash

## Summary

**[sparkDash](../entities/sparkdash.md)** is a real-time web dashboard for a fleet of [DGX Sparks](../entities/dgx-spark.md). It has grown, in under four months, into the de facto operations console for people running local LLMs and agents on GB10 boxes. The design rule is *"one Spark model, N instances"*: every unit is a record in `config/sparks.json`, and the same collector, monitor and LLM-probe code runs for each one. Remote units, and the dashboard's own host if you like, are read over SSH, so the dashboard need not run on a Spark.

Coverage goes well beyond Sparks:
- Linux GPU hosts, multi-GPU hosts, Windows PCs (NVIDIA, or AMD Strix Halo iGPU via Windows counters), Apple Silicon Macs and Intel Arc.
- Unified-memory accounting, RoCE/RDMA counters and GPU clock caps.
- Auto-detection of **14+ inference engines**, with live tok/s from each engine's own counters.

It also has a benchmark suite: decode, prefill, a seeded **Quality** bench with McNemar paired comparison, and a **Tool Eval Bench** for tool calling. And it monitors agents: **Hermes Agent** update management, plus a read-only **harness-session** helper for OpenClaw, OpenCode, oh-my-pi, Hermes and DeepSeek Harness.

The security model is stated plainly, and it is permissive by default for a LAN bind. Read it before deploying.

## Key claims

### Architecture
- **Components.** An Express 5 server (plain JS ESM, no build step) with a React 19 / Vite / Tailwind 4 frontend. A WebSocket `/ws` streams snapshots and a REST API sits under `/api/*`.
- **Polling.** Poll loops run with no browser attached, so rate metrics such as tok/s stay correct.
- **Docker-first.** A *"single privileged container for host metrics"* with host mounts. The image is native arm64 or amd64.
- **Network defaults.** The server binds loopback on port 5555 by default. Remote access is via an SSH tunnel, Tailscale Serve, an authenticated TLS proxy, or `BIND_HOST=0.0.0.0` with `SPARKDASH_TOKEN`.
- **SSH runs inside the container** as root, from the dashboard host's point of view. Keys are bind-mounted into `/root/.ssh`.
- **Contributor rules** (AGENTS.md): *"Preserve unknown or failed measurements instead of presenting them as healthy measured values"*; catch collector failures so polling continues; use a separate worktree when the user's checkout is dirty.

### LLM and inference monitoring
- **Engine auto-detection.** llama.cpp, vLLM, SGLang, LM Studio, Ollama, ds4-server, EXL3, TensorFold, FreeToken, Strata, q27, **NVIDIA Flare**, Locals and Splash. Engines in containers and engines reachable only over SSH (via a forward) are supported, with several LLM ports per unit.
- **Inference health from Prometheus `/metrics`.** KV-cache free and pool size, the run/wait queue, TTFT/E2E/ITL p95, preemptions, prefix-cache hits and MTP acceptance (vLLM, q27).
- **Unified memory.** The GB10 128 GB LPDDR5X pool (*"~273 GB/s"*), with the GPU/CPU split and `nvidia-smi dmon` bandwidth.
- **Health findings.** Small explainable rules: GPU at 85/90 °C, unified memory under 3 GB (warn) or 1.5 GB (critical), NVIDIA Xid errors, kernel OOM kills, a link below 1 Gb/s, RoCE loss. Each finding is held 90 s so it doesn't flap.
- **Fleet pages.** Token totals per model, fleet energy (24 h and 31 d, plus a monthly archive and optional cost), activity, temperatures, and a **Cost compare** page that prices fleet usage as if it ran on a hosted model.
- **Optional inference activity.** A card of in-flight and recent requests grouped by approved display labels. It reads a sanitized JSON source restricted to RFC 1918 or loopback IP literals. It does *not* intercept inference or handle client keys.

### Benchmarks
- **Decode.** Multi-concurrency streaming tok/s by content type, with selectable temperature and thinking. A **start context** (16k–256k) prefills each stream first and flags waves whose prefix cache was recomputed.
- **Prefill.** A 1k–300k context sweep of prefill tok/s and TTFT.
- **Quality.** About 755 seeded requests at temperature 0 across eight categories:
  - QA, reasoning, arithmetic chains and state tracking;
  - GSM8K (200) and MMLU (285, 5 per subject);
  - optional instruction-following and long-context recall up to 256k, with stale-code detection.
  - Runs are paired item by item, and a **McNemar p-value** reports *"difference within noise"* when p ≥ 0.05. It is a sensible way to compare quantizations and KV-cache formats on one box.
- **Tool Eval Bench.** Powered by the MIT-licensed [tool-eval-bench](https://github.com/SeraphimSerapis/tool-eval-bench), adapting ToolCall-15's scenario method. It reports score, rating, outcomes, **safety warnings** and categories, and compares runs across Sparks.
- **Prompt Showcase.** Up to 32 streaming terminals.

### Agents and harnesses
- **[Hermes Agent](../entities/hermes-agent.md).** Opt-in per unit: a background update check every 10 min, status badges, and one-click or batch `hermes update`.
- **Harness sessions.** One read-only *occupancy helper* on the agent machine caches session lists from [OpenClaw](../entities/openclaw.md), OpenCode, oh-my-pi, Hermes and DeepSeek Harness.
  - **What it does not do.** No ACP connection per session, no session titles, and it never starts an agent.
  - **Network limits.** The helper refuses `0.0.0.0`, needs a token for any non-loopback bind, and rejects plain HTTP outside loopback when a token is set.
  - **Status labels.** "Generating" and "Stalled" are used only when Hermes or DeepSeek Harness reports a running session itself.
- **Spark Overseer** (agent tool-call and command observation) is a separate, **unmerged** PR; see [PR #284](sparkdash-pr284-spark-overseer.md).

### Security (README §Security)
- **SSH passwords** are AES-256-GCM-encrypted in `config/sparks-secrets.json` and never returned by the API. Deleting the key file makes them unreadable.
- **Target validation** rejects link-local `169.254.0.0/16`, `0.0.0.0/8` and multicast/reserved addresses. Timeouts are short: 5 s for SSH, 3 s for HTTP.
- **Open by default on a LAN bind.** A non-loopback bind **without a token is open by default**: *"anyone who can reach the port can read telemetry, change settings and power units off."* The header shows an "Open access" warning that can be dismissed per browser. `SPARKDASH_ALLOW_OPEN_REMOTE=0` makes a tokenless remote bind refuse to start. `/api/health` reports `authMode`.
- **Tested scale.** *"Tested operator capacity for this remediation: 12 units."*

### Release state
- **No published image yet.** The README describes **v2.70.0**, but the newest GitHub release is **v2.32.0** (2026-10-10). The GHCR image workflow only builds tags pushed after it was added, so *"releases up to v2.32.0 have no image"* and `docker pull` returns `denied` until the next tag. Build from source.
- **x86 Docker builds are untested.** A bare `npm install && npm run build && npm start` (Node 22) works off-Spark.

## Entities mentioned
- [sparkDash](../entities/sparkdash.md) · [DGX Spark](../entities/dgx-spark.md)
- [Hermes Agent](../entities/hermes-agent.md) · [OpenClaw](../entities/openclaw.md)
- Engines: vLLM, SGLang, llama.cpp, LM Studio, [Ollama](../entities/ollama.md) and others (mostly no pages)

## Concepts touched
- [LLM agent architecture](../concepts/agents/llm-agent-architecture.md): agent harness occupancy as an operational signal.
- [AI guardrails](../concepts/safety/ai-guardrails.md): open-by-default remote binds versus explicit token modes.

## Open questions
- **The open-by-default LAN bind.** It can power units off. A one-line `SPARKDASH_ALLOW_OPEN_REMOTE=0` closes it, but that is not the default. For a Spark running a robot or agent stack, treat the dashboard host as part of the control surface.
- **Privileged container with root SSH keys.** The dashboard host holds credentials to every unit. Its blast radius equals the fleet's.
- **Release lag.** README 2.70.0 vs release v2.32.0 means "what the README says" and "what a tagged install does" differ. Pin by commit.
- **Is Tool Eval Bench's safety scoring meaningful?** It isn't described in the README. Ingest tool-eval-bench or ToolCall-15 if tool-calling evaluation of local models becomes decision-relevant.
