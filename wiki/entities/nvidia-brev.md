---
title: NVIDIA Brev
type: entity
subtype: product
created: 2026-05-14
updated: 2026-07-13
sources: 4
tags: [nvidia, gpu, cloud, devtools, cost-management]
---

NVIDIA's cross-cloud GPU-instance broker for AI/ML development. Lets you launch a preconfigured GPU box (NVIDIA drivers + CUDA + Python + Docker + optional JupyterLab) on a backing cloud provider via a single CLI / web console / VS Code Remote-SSH path. Supports B200 / H200 / H100 / A100 down to T4 / V100 / P4. Acquired by NVIDIA in 2024 (origin: brev.dev).

## Surface
- **CLI**: `brev` — `list`, `start`, `stop`, `stop --all`, `delete`, `shell`, `refresh`, `login`, `agent-skill install`.
- **Web console**: `brev.nvidia.com`.
- **VS Code Remote-SSH** integration.
- **Launchables**: shareable one-click GPU environments (org / link / public scopes); each card shows a `$/hr`.
- **AI-agent skill**: ships rules like "always show cost before creating", "confirm before H100 / multi-GPU".

## Lifecycle and billing model
- `Create → Running ⇄ Stopped → Deleted`.
- **Running**: hourly GPU billing.
- **Stopped**: workspace data persists at `/home/ubuntu/workspace`, no compute fees, minor storage cost, **GPU released to the provider pool** — restart can fail if capacity dries up.
- **Deleted**: data destroyed, no charges.

See [NVIDIA Brev Docs](../sources/nvidia-brev-docs.md) for the full lifecycle / CLI / GPU catalog.

## Cost management
Brev does **not** have native auto-stop, idle-timeout, TTL, max-runtime, or spend-cap features (as documented at ingest). Cost discipline is on the user:

1. `brev stop <name>` (or `brev stop --all`) when you walk away — *the only thing pausing the meter*.
2. **Stop** for hours; **delete** (after `git push`) for days, to avoid storage drag and capacity-loss restart risk.
3. Right-size: T4 / L4 / A10G for dev-loop work; only escalate to H100 / H200 / B200 once a run is validated.
4. `brev ls` audit before logging off.
5. Wire your own auto-stop — `trap "brev stop $NAME" EXIT` around runs, or a daily `brev stop --all` cron on your laptop.
6. Launchables meter like regular instances; one-click launch is *not* one-click stop.

Full guidance with examples in [NVIDIA Brev Docs — Cost-management guidance](../sources/nvidia-brev-docs.md#cost-management-guidance-synthesized).

## Notable Launchables
- **[Isaac Launchable](../sources/isaac-launchable-repo.md)** (`env-35JP2ywERLgqtD0b0MIeK1HnF46`) — official NVIDIA Brev Launchable for [Isaac Sim](nvidia-isaac-sim.md) 5.1 + [Isaac Lab](nvidia-isaac-lab.md) 2.3 + VS Code + Kit App Streaming. RT-core GPU required (no T4-tier escape); AWS-default; "learning only". The canonical example of a multi-container, browser-delivered Brev Launchable.

## Related
- [NVIDIA](nvidia.md) — owner.
- [NVIDIA Isaac Sim](nvidia-isaac-sim.md), [NVIDIA Isaac Lab](nvidia-isaac-lab.md) — distributed via the Isaac Launchable.
- [NVIDIA GPU rental landscape](../syntheses/platforms/nvidia-gpu-rental-landscape.md) — comparative survey across Brev + other NVIDIA-GPU rental providers (RunPod / Lambda Labs / CoreWeave / Vast.ai / Modal / DGX Cloud / hyperscalers / DGX Spark-specific).

## Mentioned in
- [NVIDIA Brev Docs](../sources/nvidia-brev-docs.md)
- [Isaac Launchable Repo](../sources/isaac-launchable-repo.md)
- [Safeguard Agentic AI Systems with the NVIDIA Safety Recipe](../sources/nvidia-safety-recipe-agentic-ai.md) — the safety recipe shipped as a one-click Brev Launchable from `build.nvidia.com`; a second example of NVIDIA using Launchables as the default delivery vehicle for a reference workflow.
