---
title: "ZeroMQ — official website (zeromq.org)"
type: source
url: https://zeromq.org/
author: ZeroMQ community (originally iMatix / Pieter Hintjens)
published: rolling (site snapshot 2026-07-07)
ingested: 2026-07-07
format: project website
tags: [zeromq, zmq, messaging, middleware, networking, pub-sub, infrastructure, transport]
---

## Summary

Official homepage of **[ZeroMQ](../entities/zeromq.md)** (ØMQ / 0MQ / zmq) — "an embeddable networking library" that "acts like a concurrency framework." It provides **sockets that carry atomic messages** across multiple transports, supporting N-to-N connection topologies and standard messaging patterns without a broker. Ingested as infrastructure context: ZeroMQ is the transport under the [Isaac-GR00T](isaac-gr00t-github.md) inference server/client stack, making it one of the three message-transport layers the wiki's robot stacks actually run on (alongside DDS under [ROS 2](../entities/ros2.md) and gRPC under [LeRobot](../entities/lerobot.md) async inference).

## Key claims

- **Four headline properties**: *Universal* (connects code across languages and platforms), *Smart* (built-in patterns: pub-sub, push-pull, client-server), *High-speed* (asynchronous I/O engines, small library footprint), *Multi-transport* — "carries messages across **inproc, IPC, TCP, UDP, TIPC, multicast and WebSocket**."
- **Brokerless, pattern-based**: supported patterns include **fan-out, pub-sub, task distribution (pipeline), and request-reply**; sockets deliver whole messages atomically.
- **Concurrency model**: asynchronous message-processing tasks over an async I/O model — pitched as the path to "scalable multicore applications" without shared-state locking.
- **Polyglot**: language APIs for most mainstream languages; runs on most operating systems. The ZeroMQ Guide is advertised as having **"60+ diagrams and 750 examples in 28 languages."**
- **Notable adopters listed**: Microsoft, Samsung, AT&T, Spotify, Facebook, DigitalOcean, Auth0, Bitcoin, **Jupyter**, Mongrel2, Jina. (Jupyter is the wiki-relevant one — the Jupyter kernel messaging protocol runs on ZeroMQ, so every JupyterLab bundle in the wiki's tutorials, e.g. the [Jetson LeRobot container](nvidia-jetson-ai-lab-lerobot.md), already ships it.)

> [!note] Not stated on the homepage
> The homepage does not carry version or license information. (libzmq's license is MPL-2.0 as of v4.3.5, previously LGPL-3.0 with a static-link exception — from general knowledge, not this source; verify against the libzmq repo if it matters.)

## Why it matters in this wiki

- **The GR00T deployment transport.** The [Isaac-GR00T](isaac-gr00t-github.md) stack serves policy inference over a **ZMQ server/client** pair — a robot-side client sends observations to a GPU-side policy server. ZeroMQ's brokerless request-reply pattern is exactly this shape.
- **Completes the transport map.** The wiki now has all three live message layers documented: **DDS** (pub/sub with discovery + QoS, under [ROS 2](../entities/ros2.md)), **gRPC** (typed RPC, under [LeRobot](../entities/lerobot.md)'s async inference / [Rosetta](rosetta-github.md)), and **ZeroMQ** (brokerless sockets, under GR00T). See the [ZeroMQ entity](../entities/zeromq.md) for the comparison.

## Entities mentioned

- [ZeroMQ](../entities/zeromq.md) — the library itself (new entity).
- [ROS 2](../entities/ros2.md), [LeRobot](../entities/lerobot.md) — the adjacent transport ecosystems.

## Concepts touched

- None directly — infrastructure source; nearest neighbors are the deployment sections of [VLA models](../concepts/learning/vla-models.md) (policy-server patterns).

## Open questions / TBD

- Current libzmq version and license text — homepage carries neither; the GitHub repo would settle both.
- ~~Which ZMQ pattern and transport Isaac-GR00T's service actually uses (REQ/REP vs DEALER/ROUTER; TCP presumably) — not documented in the [repo README ingest](isaac-gr00t-github.md).~~ **Resolved 2026-07-07 from repo code**: REQ/REP over TCP port 5555, msgpack-numpy — details on the [Isaac-GR00T source page](isaac-gr00t-github.md) and [ZeroMQ entity](../entities/zeromq.md).
