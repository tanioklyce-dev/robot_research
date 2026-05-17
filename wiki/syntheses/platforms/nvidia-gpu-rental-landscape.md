---
title: NVIDIA GPU rental landscape — providers, pricing, and what to pick
type: synthesis
created: 2026-05-17
updated: 2026-05-17
tags: [gpu, rental, cloud, nvidia, brev, dgx-cloud, h100, b200, dgx-spark, hosting, cost-management]
---

A grouped catalog of **where to rent NVIDIA GPUs by the hour** in 2026, with pricing context and recommendations by use case. Spun off from the [Wiki-query agent on DGX Spark deployment plan](../projects/wiki-query-agent-on-dgx-spark.md) to centralize the buyer's view across providers.

## TL;DR

| Use case | Pick |
| --- | --- |
| **Just need a GPU for one notebook, low budget** | [Vast.ai](https://vast.ai) or [RunPod](https://runpod.io) community cloud — peer / community pricing, ~$1.25–$2/hr for H100 spot |
| **Need NVIDIA-native devtools** ([Isaac Lab](../../entities/nvidia-isaac-lab.md), [GR00T](../../entities/nvidia-groot.md), preconfigured Launchables) | **[NVIDIA Brev](../../entities/nvidia-brev.md)** ([brev.nvidia.com](https://brev.nvidia.com)) |
| **Production AI workloads with SLAs** | [CoreWeave](https://coreweave.com), [Lambda Labs](https://lambda.ai), or hyperscaler (AWS p5 / GCP A3 / Azure NDv5) |
| **DGX Spark specifically** | **[Enverge](https://spark.enverge.ai/)** ($0.48/hr); also Server Room, Primcast |
| **Multi-node training (DGX-class)** | [NVIDIA DGX Cloud](https://www.nvidia.com/en-us/data-center/dgx-cloud/) |
| **Cheapest, willing to handle reliability variance** | [Vast.ai](https://vast.ai) (peer marketplace) |

## NVIDIA-native options

### NVIDIA Brev — [brev.nvidia.com](https://brev.nvidia.com)

The wiki's [primary GPU-rental entry point](../../entities/nvidia-brev.md). Cross-cloud broker: launches preconfigured GPU instances on a backing cloud (AWS / GCP / Azure / etc.) with NVIDIA drivers + CUDA + Python + Docker + optional JupyterLab. Single `brev` CLI / web console / VS Code Remote-SSH path. **GPU catalog: B200 / H200 / H100 / A100 / L4 / A10G / T4 / V100 / P4.** Acquired by NVIDIA in 2024 (origin: brev.dev). **No DGX Spark in the Brev catalog as of last ingest** — Brev's focus is data-center SKUs.

Best for: NVIDIA-native workflows (the [Isaac Launchable](../../sources/isaac-launchable-repo.md) is the canonical example), VS Code Remote-SSH dev loops, and "I want one click to a preconfigured GPU box."

**Caveat**: no native auto-stop / TTL / spend-cap — cost discipline is on the user. See [Brev entity](../../entities/nvidia-brev.md) for the full guidance.

### NVIDIA DGX Cloud

NVIDIA's hosted DGX-class compute (8× H100 / H200 / B200 nodes), running on AWS / GCP / Azure / Oracle backends. **DGX Cloud Lepton** is the more developer-facing variant (lower-friction onboarding than enterprise DGX Cloud). Pricing is opaque without contact-sales for the enterprise tier; cloud-side rentals start around **$3.72/hr average for H100**, with B200 in the **$4–6/hr** range and B300 at **$2.45–$6.80/hr**.

Best for: serious multi-node training, fine-tuning at scale, anything that needs NVLink-fabric coherence across a full DGX node.

### NVIDIA Launchables

Shareable one-click GPU environments built on Brev. Each card shows a `$/hr` rate. The [Isaac Launchable](../../sources/isaac-launchable-repo.md) is the wiki-tracked example: VS Code + Isaac Sim 5.1 + Isaac Lab 2.3 + Kit App Streaming on an RT-core GPU. **Launchables meter like regular Brev instances — one-click launch is not one-click stop.**

## AI-focused cloud providers

The category of clouds built specifically for AI workloads — typically cheaper than hyperscalers, less ops-heavy than peer-marketplace.

| Provider | H100 on-demand (per GPU-hr) | Notes |
| --- | --- | --- |
| **[RunPod](https://runpod.io)** | $1.99 (community) / $2.39–$2.69 (secure cloud) | Lowest-friction signup; serverless tier; community cloud is cheaper but variable reliability. Strong for hobbyists + ML researchers. |
| **[Lambda Labs](https://lambda.ai)** | $2.99–$3.78 (SXM) | Long-standing AI-first cloud; reserved instances + on-demand; first-class for PyTorch / NVIDIA stack. |
| **[CoreWeave](https://coreweave.com)** | $4.25 (PCIe) – $6.16 (HGX) | Enterprise SLA + multi-GPU cluster networking; IPO'd 2025; the choice if you need real production guarantees. |
| **[Vast.ai](https://vast.ai)** | $1.25 (spot, sometimes lower) | Peer-to-peer marketplace; cheapest H100 you'll find; reliability + bandwidth varies host-to-host. |
| **[Paperspace](https://paperspace.com)** (DigitalOcean) | varies | Gradient platform; tighter integration with notebook workflows. |
| **[Modal](https://modal.com)** | per-second billing | Serverless GPU; great for sporadic inference or batch jobs; less great for long interactive dev sessions. |
| **[Together AI](https://together.ai)** | per-token (inference-as-a-service) | Different category — not GPU rental, but hosts open-source models you'd otherwise self-serve. |
| **FluidStack, Crusoe, Spheron** | various | Smaller aggregators; sometimes very competitive on spot. |

H100 prices across 15+ providers span **$1.49–$6.98/hr** as of mid-2026; B200 spans **~$2.12–$8/hr**. Spot / preemptible tiers are typically 30–60% cheaper than on-demand.

## Hyperscaler GPU instances

Generally the **most expensive** path for raw GPU compute, but the right answer if you're already on the hyperscaler for everything else, need their broader services, or have committed-use discounts.

| Hyperscaler | Headline GPU instances |
| --- | --- |
| **AWS** | p5 (H100), p4 (A100), g5 (A10G), g6 (L4) |
| **Google Cloud** | A3 (H100), A2 (A100), G2 (L4) |
| **Azure** | ND H100 v5, NDv4 (A100) |
| **Oracle Cloud** | Bare-metal H100 — often the cheapest hyperscaler price for committed compute |

## DGX Spark-specific rentals

Surfaced 2026-05-17 while planning [the wiki-query agent deployment](../projects/wiki-query-agent-on-dgx-spark.md). [DGX Spark](../../entities/dgx-spark.md) (GB10 Grace Blackwell, 128 GB unified, 273 GB/s) is not in the Brev catalog as of last ingest, but third-party providers rent it:

| Provider | Price | Notes |
| --- | --- | --- |
| **[Enverge](https://spark.enverge.ai/)** | **$0.48 / hr** | 128 GB Spark instance, SSH + Docker. Aggressive entry price. |
| **[Server Room](https://www.serverroom.net/spark)** | quoted (not public-listed) | Dedicated, pre-configured environments, enterprise networking. |
| **[Primcast](https://www.primcast.com/spark)** | quoted | Dedicated, pre-optimized NVIDIA AI stack. |
| **Peer-to-peer** | varies | Active discussion on the [NVIDIA DGX Spark / GB10 forum](https://forums.developer.nvidia.com/t/anyone-renting-out-their-dgx-spark-when-not-using-it/362924) — owners renting unused cycles. |

**Buy-vs-rent at $0.48/hr**: $345/month always-on; Spark dev kit (~$3,500) pays back at ~10–12 months 24/7. For a pilot phase or evaluation work, **rent first**.

## Peer-to-peer / spot tier

The cheapest tier of all, with the most variance.

- **[Vast.ai](https://vast.ai)** — peer marketplace; anyone can host their GPU and rent it out. H100 spot has hit $1.25/hr; A100 commonly under $1/hr. Network bandwidth, disk performance, and host reliability vary widely. Excellent for batch jobs that tolerate interruption.
- **NVIDIA forum DGX Spark peer rental** — informal, but real ([forum thread](https://forums.developer.nvidia.com/t/anyone-renting-out-their-dgx-spark-when-not-using-it/362924)). Same shape as Vast but Spark-only and currently uncommercialized.
- **RunPod community cloud** — RunPod's own peer-tier; cheaper than their secure cloud, with more variance.

## Pricing context (as of mid-2026)

Headline rates per GPU per hour, on-demand single GPU:

| GPU | Spot floor | Typical on-demand | Premium / SLA |
| --- | --- | --- | --- |
| **H100 (80 GB)** | $1.25 | $2–$4 | $5–$7 |
| **H200 (141 GB)** | ~$2 | $3–$5 | $6–$8 |
| **B200 (192 GB)** | $2.12 | $4–$6 | $6–$8 |
| **B300** | $2.45 | $4–$5 | $6.80 |
| **A100 (80 GB)** | $0.80 | $1.30–$2.50 | $3+ |
| **DGX Spark (128 GB unified)** | $0.48 | $0.48–quoted | quoted |
| **L4 / A10G** | $0.20–$0.40 | $0.50–$1.00 | $1.50 |

The general lesson: **GPU rental pricing has compressed sharply in 2026 compared to the 2023–2024 H100 supply crunch.** H100 spot floors near $1.25 is a meaningful change vs $4–$8/hr during peak demand. B200/B300 supply has caught up enough that they're now in similar price bands as H200.

## Cost-management lessons (general)

Lifted from the [Brev cost-management guidance](../../entities/nvidia-brev.md#cost-management):

1. **Stop instances when you walk away.** Almost no provider has aggressive auto-stop. The meter runs until you stop or delete.
2. **Right-size first.** L4 / A10G / T4 for dev-loop work; only escalate to H100 / H200 / B200 once a run is validated.
3. **Spot / preemptible for batch.** 30–60% savings if the workload tolerates interruption.
4. **Reserve / commit when usage is predictable.** Most providers offer 30–70% reserved-instance discounts for committed use.
5. **Wire your own auto-stop** — `trap "provider-cli stop $NAME" EXIT` around scripts, or a daily `stop --all` cron.
6. **Watch storage drag.** Stopped instances often retain workspace storage at low-but-nonzero cost; **delete** if you're away for days, not just stopped.

## How to choose

The decision factors that actually matter for picking a provider:

1. **Do you need NVIDIA-native devtools?** ([Isaac Lab](../../entities/nvidia-isaac-lab.md), Launchables, NVAIE) → Brev or DGX Cloud.
2. **Is this DGX Spark specifically?** → Enverge / Server Room / Primcast (not Brev — Spark isn't catalogued).
3. **Multi-GPU NVLink-fabric workload?** → CoreWeave or DGX Cloud — most providers don't expose true HGX-fabric nodes.
4. **Need production SLAs?** → CoreWeave / Lambda Labs / hyperscaler.
5. **Hobbyist / research with tight budget?** → RunPod community or Vast.ai.
6. **Already on AWS / GCP / Azure for everything else?** → Stay there, even though it's more expensive — integration savings beat the GPU-hour delta.
7. **Sporadic inference workload?** → Modal (serverless, per-second billing).
8. **Just want to evaluate an open model for an evening?** → RunPod or Vast spot.

## Related

- [NVIDIA Brev](../../entities/nvidia-brev.md) — the wiki's main rental entry point.
- [NVIDIA Brev Docs](../../sources/nvidia-brev-docs.md) — full lifecycle + CLI reference.
- [Jetson Thor vs DGX Spark](jetson-thor-vs-dgx-spark.md) — the buy-side decision tree for owned hardware.
- [Wiki-query agent on DGX Spark deployment plan](../projects/wiki-query-agent-on-dgx-spark.md) — concrete project where this rental landscape was load-bearing.
- [Isaac Launchable](../../sources/isaac-launchable-repo.md) — canonical example of an NVIDIA Brev preconfigured environment.

## Open questions / TBD

- **NVIDIA DGX Cloud Lepton vs the older DGX Cloud enterprise offering** — what's the actual feature delta and pricing transparency story?
- **Brev catalog evolution** — when (if) DGX Spark and the GB200 NVL line surface in Brev.
- **Peer-to-peer Spark market commercialization** — currently informal via NVIDIA forums; will it consolidate into a Vast.ai-shaped marketplace?
- **Together AI / Anyscale / Replicate** as substitutes — for some workloads, paying per-token to a hosted open-model inference service is cheaper than renting the GPU yourself. The wiki doesn't track these systematically yet.

## Provenance

Filed 2026-05-17. Trigger: while planning the [wiki-query agent deployment on DGX Spark](../projects/wiki-query-agent-on-dgx-spark.md), found that Spark is rentable from third-party providers (not in NVIDIA Brev's catalog). That gap motivated a broader survey of NVIDIA GPU rental options to centralize the buyer's view.
