---
title: NVIDIA BlueField (DPU) and DOCA
type: entity
subtype: hardware-platform
created: 2026-09-29
updated: 2026-09-29
sources: 4
tags: [nvidia, bluefield, dpu, supernic, doca, connectx, data-center, networking, zero-trust, sentry]
---

**NVIDIA BlueField** is NVIDIA's line of **data processing units (DPUs) and SuperNICs**. Each is a network card with its own Arm cores and OS, and it runs infrastructure services (networking, storage, security) in a domain isolated from the host's workloads. **DOCA** is BlueField's SDK and runtime; DOCA-Host is the host-side driver package for BlueField and ConnectX ([DOCA page](../sources/nvidia-doca-developer-page.md)).

## Platform (from the DOCA page)

- Isolates *"the infrastructure service domain from the workload domain."* This is the property the agent-safety use case relies on.
- The BlueField bundle ships bootloader, kernel, NIC firmware, drivers and **Ubuntu 22.04**. The DOCA runtime orchestrates containerized services across *"hundreds or thousands"* of DPUs.
- SDK areas: RDMA/GPUDirect, SDN acceleration (ASAP²), **security acceleration (inline crypto, App Shield runtime security)**, storage, DPA, management. Connectivity up to 800 Gb/s.

## Role in agent safety (2026-09)

**BlueField-4** hosts **[NVIDIA Sentry](nvidia-sentry.md)**, the out-of-band watchdog layer of the Open Agent Safety Platform ([newsroom](../sources/nvidia-newsroom-open-agent-safety-platform.md)). In a Vera Rubin POD, each compute tray's BlueField-4 sits *"on the node's only path to the model,"* where it provides line-rate observability and enforcement *"even when host resources cannot be trusted"* ([Sentry blog](../sources/nvidia-open-agent-safety-platform-sentry-blog.md)). [OpenShell](nvidia-openshell.md) does **not** require BlueField ([solutions page](../sources/nvidia-open-agent-safety-platform-page.md)).

## Relevance to robots

This is data-centre silicon. No [Jetson](jetson-thor.md) module carries a DPU. The closest on-robot counterpart is the **Functional Safety Island** on IGX Thor under [Halos](nvidia-halos.md): an isolated domain, but one that enforces functional safety rather than agent policy. The page exists so the Sentry claims can be read in context.

## Related

- [NVIDIA Sentry](nvidia-sentry.md) · [NVIDIA OpenShell](nvidia-openshell.md) · [NVIDIA](nvidia.md)

## Mentioned in

- [NVIDIA DOCA Software Platform — Developer Page](../sources/nvidia-doca-developer-page.md)
- [NVIDIA Open Agent Safety Platform: A Reference for Continuous In-Silicon Agent Monitoring](../sources/nvidia-open-agent-safety-platform-sentry-blog.md)
- [NVIDIA Launches Open Agent Safety Platform (Newsroom)](../sources/nvidia-newsroom-open-agent-safety-platform.md)
- [NVIDIA Open Agent Safety Platform — Solutions Page](../sources/nvidia-open-agent-safety-platform-page.md)
