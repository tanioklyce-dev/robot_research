---
title: NVIDIA Brev — Overview & Documentation
type: source
url: https://docs.nvidia.com/brev/getting-started/overview
author: NVIDIA
published: 2025–2026
ingested: 2026-05-14
tags: [nvidia, gpu, cloud, devtools, cost-management]
---

## Summary
NVIDIA Brev is a cross-cloud GPU-instance broker with preconfigured AI/ML environments. The user picks a GPU type, Brev provisions an instance from one of several backing providers (Nebius, AWS, GCP, etc.) with NVIDIA drivers, CUDA, Python 3.10+, Docker, and (optionally) JupyterLab already installed. Workflow surfaces include a web console, a CLI (`brev`), VS Code Remote-SSH integration, and **Launchables** — shareable, one-click GPU environments that bundle hardware + software + code. This ingest covers the public docs at `docs.nvidia.com/brev/*`, with particular focus on the **cost-management surface** that drove the user's question.

## Key claims

### Instance lifecycle and billing
- **Lifecycle**: `Create → Running ⇄ Stopped → Deleted`.
- **Running** — GPU is attached and reserved for you. *Brev bills you per hour for compute time* at the GPU's hourly rate. SSH/shell/VS Code are reachable.
- **Stopped** — GPU is *released back to the provider's pool*. **No compute fees** while stopped, only minimal storage. Workspace data at `/home/ubuntu/workspace` persists. Restart carries **capacity risk**: if regional GPU availability drops, the restart fails and your data stays inaccessible until capacity returns.
- **Deleted** — instance and all data are destroyed permanently; no charges, no recovery.
- **Storage cost while stopped is "minimal"** but non-zero — for long breaks, deleting (after pushing your workspace to git) is cheaper *and* avoids the capacity-loss restart risk.

### CLI commands relevant to spend
Verbatim from the `brev` CLI reference:
- `brev list` (alias `brev ls`) — show all your instances, including running ones.
- `brev start <name>` — start an existing stopped instance.
- `brev start <repo-or-name> --gpu "<gpu-spec>"` — create + start with a specific GPU. Example: `brev create my-instance --gpu "nebius.l40sx1.pcie"`.
- `brev stop <name>` — stop a single instance.
- `brev stop <a> <b> <c>` — stop multiple by name.
- **`brev stop --all`** — stop *every* running instance in your account. The single most important cost-control command.
- `brev delete <name>` — terminate (destroys data).
- `brev shell <name>` — open a shell on a running instance.

### What's NOT in the docs
After fetching the overview, quickstart, GPU-instances concept page, environments, launchables, CLI getting-started, instance-management, GPU-types reference, and the AI-agent guide:
- **No native auto-stop / idle-timeout flag** on `brev start` or `brev create`. There is no documented `--ttl`, `--max-runtime`, `--idle-timeout`, or `--max-cost`.
- **No documented usage/cost CLI subcommand** (no `brev usage`, `brev cost`, `brev billing`, `brev wallet`).
- **No documented free tier or per-account spend cap.**
- **No published rate sheet** in the docs; per-GPU hourly rates appear on the Launchable cards in the Explore view and at instance-creation time, but are not listed in `reference/gpu-types`.

### GPU types (no prices in docs)
- **Datacenter top-end**: B200 (192 GB HBM3e), H200 (141 GB), H100 (96 GB), A100 80 GB.
- **Mid-range**: L40S, L40, L4, RTX 6000 Ada, RTX 4000 Ada, RTX PRO Server 6000, A10G, A16, A6000, A5000, A4000, RTX 5090.
- **Budget / dev**: T4 (16 GB) — flagged as "cost-effective option for development", V100 (32 GB), P4 (8 GB) — cheapest mentioned.

### Launchables
Reproducible, shareable environments bundling GPU spec + software + code. Three sharing levels: organization-only, link-shareable, public/published in Explore. "Cost per hour" is displayed on each Launchable card. Launchables are **not** documented as ephemeral or auto-stopping — once you launch one, it behaves like any other Brev instance and the meter runs until you stop it.

### AI-agent skill (`brev agent-skill install`)
Brev ships an agent-side skill for AI coding assistants with three explicit cost-safety rules:
- "Always show cost/type before creating instances."
- "Always confirm before creating expensive instances (H100, multi-GPU) or clusters."
- "Always confirm before deleting or stopping instances."

These are *agent-side conventions*, not server-side guardrails — there is no spend cap enforced by Brev itself.

## Cost-management guidance (synthesized)
The documented model puts cost discipline entirely on the user. Concrete rules:

1. **Stop when you walk away.** `brev stop <name>` (or `brev stop --all`) is the only thing between you and an open meter. Brev does not auto-stop idle instances.
2. **Prefer `stop` for hours, `delete` for days.** Stopped retains workspace + minor storage cost + capacity-loss risk. Deleting (after `git push`) is the right call for overnight/multi-day breaks.
3. **Right-size aggressively.** A T4 / L4 / A10G is fine for code-loop iteration, profiling, and small fine-tunes. Save H100 / H200 / B200 for runs you've already validated on a smaller GPU.
4. **Audit before you log off.** `brev ls` should show the expected running set; if you see something you forgot, stop it.
5. **Wire your own auto-stop.** Since Brev has no native TTL flag, build it into your run script:
   - `trap "brev stop my-instance" EXIT` around training jobs.
   - A daily cron on your laptop / CI: `brev stop --all` at end of working day.
   - For agent-launched runs, give the agent a max-runtime contract and have it call `brev stop` on completion or timeout.
6. **Treat Launchables like instances.** "One-click launch" doesn't mean "one-click stop" — they meter the same way.
7. **Check the price** on the Launchable card or at create time; it's the only place the per-hour rate is surfaced.

## Entities mentioned
- [NVIDIA](../entities/nvidia.md)
- [NVIDIA Brev](../entities/nvidia-brev.md)

## Concepts touched
- GPU cloud aggregation / brokered compute
- Instance lifecycle (running / stopped / deleted) as the primary cost lever
- Capacity risk on `stop → start`

## Open questions
- Does Brev's web console expose an idle-timeout setting that the CLI/docs don't mention?
- Is there a usage / billing dashboard or API for programmatic spend tracking?
- Per-GPU hourly rates: is there a single rate sheet anywhere outside the per-Launchable display?
- Spot / preemptible / reserved-capacity options — are any exposed through Brev?
