---
title: Zenoh — project site, docs, and the NTU performance comparison (zenoh.io)
type: source
url: https://zenoh.io/
author: Eclipse Zenoh project (ZettaScale); performance evaluation contributed by a National Taiwan University team
published: 2020-01-21 (project start; benchmark blog 2023-03-21; site current as of ingest)
ingested: 2026-08-13
license: EPL-2.0 / Apache-2.0 (dual)
tags: [zenoh, middleware, pub-sub, dds-alternative, ros2, rust, eclipse, transport, benchmark, latency, throughput, zenoh-pico, embedded, primary-source]
---

## Summary

**Eclipse Zenoh** (/zeno/) is a **pub/sub + storage + query protocol** that unifies *data in motion, data at rest, and computations* under one addressing scheme. Rust core, multi-language APIs, **EPL-2.0 / Apache-2.0** dual licence, Eclipse **incubating** project. Its two headline engineering claims are **5-byte minimum wire overhead** and a microcontroller implementation (**Zenoh-pico**) that fits in **300 bytes on an 8-bit Atmel**.

Ingested to replace the secondhand [Zenoh entity](../entities/zenoh.md) written from the [DimOS repo](dimos-github.md), and specifically to close the open question recorded there: *"No measured numbers here — latency, throughput and jitter versus Cyclone/Fast DDS and versus LCM are all unestablished."* The site carries an **independent benchmark from National Taiwan University** comparing Zenoh against MQTT, Kafka, and Cyclone DDS, which answers most of it.

## Key claims — the protocol

Three primitives, deliberately more than a message bus:

| Primitive | What it does |
|---|---|
| **Pub/Sub** | Multiple reliability levels, dynamic discovery, fragmentation, wire-level batching |
| **Storages** | Geo-distributed, with **sharding and replication** — historical data uses the same key space as live data |
| **Queries & Queryables** | Applications register *computations* triggered by queries — *"a simple mechanism that allows many patterns to be implemented, such as RPC and map-reduce"* |

Keys are Unix-path-like (`myhome/kitchen/temp`); values carry an encoding (string, JSON, raw bytes). A `zenohd` router adds storage and REST plugins by config.

**Three deployment topologies** — peer-to-peer (mesh / clique), brokered (client through a router), and routed infrastructure. This is the structural difference from its rivals: **MQTT and Kafka are brokered-only, DDS is peer-to-peer-only, Zenoh does both** and can mix them in one topology.

### The constrained-device story

- **5-byte minimum wire overhead**, and it can run **directly on OSI Layer 2** to maximize usable bandwidth.
- Designed for **LPWAN and LowPAN** — genuinely constrained radio links, not just "small."
- **Zenoh-pico**, the microcontroller implementation, is claimed at **300 bytes footprint on an 8-bit Atmel** — and, notably, it *already implements UDP multicast* which the main Rust implementation did not at benchmark time.

## Key claims — the NTU benchmark (2023-03-21)

An independent evaluation by a National Taiwan University team using Zenoh in R2X/V2X projects, published on Zenoh's blog with an arXiv companion. Testbed: AMD Ryzen 7 5800X pinned at 4.0 GHz, 32 GiB DDR4-3200, Ubuntu 20.04, **100 Gb Ethernet** for the multi-machine case. Medians with 1st/99th-percentile outliers removed.

### Latency, 64-byte payload (µs — lower is better)

| Target | Single machine | Multi-machine |
|---|---:|---:|
| `ping` (baseline) | 1 | 7 |
| **Zenoh-pico** | **5** | **13** |
| Cyclone DDS | **8** | 37 |
| **Zenoh P2P** | 10 | **16** |
| Zenoh brokered | 21 | 41 |
| MQTT | 27 | 45 |
| Kafka | 73 | 81 |

### Throughput (small payloads, single machine)

| Target | Peak message rate |
|---|---|
| **Zenoh P2P** | **>4M msg/s** |
| Cyclone DDS | ~2M msg/s |
| Kafka | 56–63K msg/s (≤2 KB payloads) |
| MQTT | 33–38K msg/s (≤32 KB) |

Zenoh reached **up to 67 Gbps** on the single-machine test.

> [!note] Read the DDS row carefully — it is the honest part of the benchmark
> **On a single machine, Cyclone DDS beats Zenoh's Rust implementation on latency (8 µs vs 10 µs)**, and the authors say exactly why: DDS uses **UDP multicast**, which Zenoh's main implementation had not yet implemented. Zenoh-pico, which *does* have it, comes in at **5 µs** — below DDS. The benchmark is published by the Zenoh project and still prints the row where a competitor wins, with the mechanism.
>
> **Across a real network the ordering inverts decisively**: Zenoh P2P 16 µs vs Cyclone DDS 37 µs. That is the number that matters for the deployment this wiki cares about, because multicast is precisely what stops working across subnets, over Wi-Fi, and through NAT.

## Analysis

> [!note] This closes the open question on the entity page, and the answer is "yes, measurably"
> The [Zenoh entity](../entities/zenoh.md) was filed with *"no measured numbers anywhere — and for a robot control loop those are the only numbers that decide anything."* They exist, they are independent, and they support the claim: **Zenoh P2P beats Cyclone DDS by 2.3× on latency over a real network**, and beats brokered MQTT/Kafka by 3–5× everywhere. The remaining unmeasured comparison is the one this wiki most wanted: **Zenoh vs LCM**, which no source has run.

> [!note] Why "5 bytes" and "300 bytes" are the interesting numbers, not the throughput
> 4M msg/s on a Ryzen 7 is a datacentre number and largely irrelevant to a robot. **5-byte wire overhead and a 300-byte 8-bit-micro footprint are robotics numbers** — they mean the same protocol addresses a sensor MCU and a cloud store, which is the thing DDS has historically not done well and the reason ROS 2 fleets fragment into "the DDS part" and "the cloud part." Combined with the Layer-2 option and LPWAN support, Zenoh's actual pitch is **one addressing scheme from the microcontroller to the datacentre**, and the performance table is the supporting evidence rather than the claim.

> [!note] Queryables are the piece with no ROS 2 analogue
> Pub/sub maps cleanly onto ROS 2 topics and DDS. **Queryables — registering a computation that fires on query — do not.** They collapse RPC, map-reduce, and historical-data retrieval into the same key-space operation as a live subscription. For the wiki's robot-fleet work ([fleet agentic framework](../syntheses/projects/fleet-agentic-framework.md), [ros2-mcp-server](../syntheses/projects/ros2-mcp-server-design.md)), that is the interesting primitive: "what is the robot's current pose" and "what was it at 14:02 yesterday" and "compute me a summary" become one addressed call rather than three subsystems.

> [!warning] Incubating, and the benchmark is three years old
> Eclipse **incubation** status is not a maturity endorsement, and the NTU numbers use **Zenoh 0.7.0-rc** against Mosquitto 2.0.15, Kafka 3.2.1, and Cyclone DDS of the period. Zenoh is now at 1.x with an API migration behind it. The *ordering* is likely stable — it follows from architecture, not tuning — but the absolute figures should be treated as 2023 evidence, and the "Zenoh lacks UDP multicast" caveat may already be stale.

## Entities mentioned

- [Zenoh](../entities/zenoh.md) — the subject of this source
- [ROS 2](../entities/ros2.md) — `rmw_zenoh` makes it a ROS 2 middleware; DDS is the incumbent it is measured against
- [DimOS](../entities/dimos.md) — offers Zenoh as its reliable transport alternative to LCM
- [Drake](../entities/drake.md) — the LCM-native, ROS-2-unsupported corner of the same middleware fragmentation

## Concepts touched

- [Robot security](../concepts/robotics/robot-security.md) — routed, non-multicast transport changes the network exposure story
- [Control abstraction levels](../concepts/robotics/control-abstraction-levels.md)

## Open questions

- **Zenoh vs LCM is still unmeasured**, and it is the comparison this wiki actually needs — [DimOS](../entities/dimos.md) ships both and documents the trade qualitatively (LCM fast/best-effort, Zenoh reliable) with no numbers.
- **Jitter is unreported.** Median latency is given; for a control loop the tail is what matters, and no percentile beyond the 99th-outlier trim is published.
- **Has the Rust implementation gained UDP multicast since 0.7?** If so the single-machine DDS advantage disappears and the 2023 table understates current Zenoh.
- **Is `rmw_zenoh` production-default in any ROS 2 distribution yet**, or still opt-in? Unresolved.
- No **security/authn** model was read here, despite routed multi-network deployment being the headline use case.
