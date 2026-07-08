---
title: ZeroMQ
type: entity
subtype: software
created: 2026-07-07
updated: 2026-07-07
sources: 2
tags: [zeromq, zmq, messaging, middleware, networking, pub-sub, brokerless, infrastructure]
---

**ZeroMQ** (ØMQ / 0MQ / zmq) — brokerless, embeddable messaging library: sockets that carry atomic messages over **inproc, IPC, TCP, UDP, TIPC, multicast, and WebSocket**, with built-in patterns (pub-sub, push-pull/pipeline, request-reply, fan-out) and an asynchronous I/O core ([zeromq.org](../sources/zeromq-org.md)). No broker process, no discovery service — endpoints connect directly, which keeps it small and fast at the cost of the naming/QoS machinery heavier middlewares provide. Polyglot (bindings in most languages; the Guide advertises 750 examples in 28 languages); adopters listed on the site include Microsoft, Spotify, Bitcoin, and **Jupyter** (the kernel protocol runs on ZMQ).

## Where it shows up in this wiki

- **[Isaac-GR00T](../sources/isaac-gr00t-github.md) deployment stack** — GR00T policy inference is served over a **ZMQ server/client** pair: GPU-side policy server, robot-side client sending observations and receiving action chunks. This is the wiki's primary ZMQ consumer. Pattern (from repo code, `gr00t/policy/server_client.py`): **synchronous REQ/REP over TCP, default port 5555**; msgpack-numpy serialization with a hard `allow_pickle=False` boundary; 15 s send/recv timeouts, and the client re-creates its socket on `zmq.error.Again` (a REQ socket is invalid after a failed receive).
- **Implicitly via Jupyter** — every JupyterLab-bundling tutorial (e.g. the [Jetson LeRobot container](../sources/nvidia-jetson-ai-lab-lerobot.md)) ships ZMQ under the kernel protocol.

## The wiki's robot-transport map

Three message layers now documented, each chosen for a different trade:

| Layer | Used by | Shape | What you get / give up |
|---|---|---|---|
| **DDS** | [ROS 2](ros2.md) (pub/sub, services, actions) | discovery + QoS-rich pub/sub | ecosystem-wide interop, QoS profiles; heavyweight, config-sensitive |
| **gRPC** | [LeRobot](lerobot.md) async inference ([Rosetta](../sources/rosetta-github.md) remote-GPU path) | typed RPC over HTTP/2 | schema'd APIs, streaming; needs proto toolchain |
| **ZeroMQ** | [Isaac-GR00T](../sources/isaac-gr00t-github.md) policy server | brokerless sockets + patterns | minimal deps, fast, embeddable; no discovery, no QoS, DIY schema |

The pattern across the stack: **ROS 2/DDS for intra-robot integration, gRPC or ZMQ for the robot↔GPU-policy-server hop** — the policy-serving hop is point-to-point and latency-sensitive, so both GR00T (ZMQ) and LeRobot (gRPC) bypass DDS for it.

## Mentioned in

- [ZeroMQ — official website](../sources/zeromq-org.md) — primary source.
- [Isaac-GR00T GitHub](../sources/isaac-gr00t-github.md) — ZMQ server/client inference service.

## Open questions / TBD

- libzmq version/license not on the homepage (MPL-2.0 as of v4.3.5 per general knowledge — unverified against a wiki source).
- ~~Which ZMQ pattern GR00T's service uses (REQ/REP vs DEALER/ROUTER) — undocumented in the ingested README.~~ **Resolved 2026-07-07 from repo code** (`gr00t/policy/server_client.py`): REQ/REP over `tcp://` port 5555, msgpack-numpy (`allow_pickle=False`), 15 s timeouts + socket re-init on timeout. See the Isaac-GR00T bullet above.
- History thread (iMatix, Pieter Hintjens, the AMQP schism) — only worth capturing if a history source lands.
