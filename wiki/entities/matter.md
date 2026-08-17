---
title: Matter
type: entity
subtype: standard
created: 2026-08-17
updated: 2026-08-17
sources: 1
tags: [matter, smart-home, home-automation, interoperability, multi-admin, fabric, access-control, csa, standard]
---

**Matter** — the IP-based application-layer interoperability standard for smart-home devices, published by the [Connectivity Standards Alliance](connectivity-standards-alliance.md). It is the layer beneath Apple Home, Google Home, Amazon Alexa and SmartThings, and the reason a single bulb or lock can be controlled by more than one of them.

The wiki's first home-automation source. It exists here because a **[home AI platform](../syntheses/agents/home-ai-platform-trust-and-authority.md)** is agentic robot AI fused with home automation, and Matter is the only part of that fusion with a published, mature trust model.

## Structure

- **Fabric** — a set of devices sharing a trusted root; one fabric ≈ one ecosystem. The root of trust is a **Root CA** issuing **NOCs** (Node Operational Certificates). Fabrics are "unrelated by any common roots of trust" ([Core Spec 1.4](../sources/matter-1-4-core-specification.md) §2.4).
- **Multi-admin** — a device may be commissioned into several fabrics at once, each with independent credentials. `SupportedFabrics` is fixed per device; `CommissionedFabrics` counts current ones.
- **Access Control List (ACL)** — deny-by-default, matched **per fabric**, with five nested privileges: `View` → `ProxyView` / `Operate` → `Manage` → `Administer`.
- **Access Restriction List (ARL)** — per-fabric, **set by the device**, naming attributes/commands/events an ecosystem may *not* reach. It **overrides** privileges the ecosystem's own administrator grants, returning `ACCESS_RESTRICTED`.
- **Fabric-scoped data** — per-fabric configuration lists (ACLs, bindings, group keys), isolated so fabrics don't clobber each other's settings.
- **Fabric Synchronization / Joint Fabric** (1.4) — mechanisms for ecosystems to share devices, with per-ecosystem user consent and an Anchor CA trusted across fabrics.

## The two findings that matter for robotics

### 1. Multi-admin isolates configuration, not state

> "**Most cluster data instances are accessible regardless of the accessing fabric.**" ([Core Spec 1.4](../sources/matter-1-4-core-specification.md) §7.5.3)

Fabric-scoping is explicitly limited to **lists of fabric-scoped structs and fabric-sensitive events**. A device's operational state — a light's `OnOff`, a lock's position — is a **single shared value** visible and writable from every commissioned fabric.

### 2. There is no arbitration, anywhere

**"arbitrat" appears zero times in the 1,173-page core specification.** The eight occurrences of "conflict" all concern DNS-SD name collisions and ephemeral node IDs, never competing commands from different administrators.

> [!warning] Matter did not solve multi-controller arbitration — it externalized the problem
> Two ecosystems writing the same attribute is not an error, not a conflict, and not resolved by any rule in the specification. It works in practice because **the state is trivial**: a bulb toggling between two admins is an annoyance, cheaply re-set, with no physical consequence. **That property is exactly what a mobile actuated robot does not have**, which is why Matter's multi-admin model does not extend to one by analogy. See [the home AI platform synthesis](../syntheses/agents/home-ai-platform-trust-and-authority.md).

## Why the ARL is the interesting part

The **Access Restriction List is a standardized, shipping, vendor-authored bound on what an ecosystem may touch** — discoverable before commissioning (via `CommissioningARL`), negotiable (`ReviewFabricRestrictions`), and enforced *below* the administrator's own grants.

That is the same shape as the **typed capability manifest** the wiki's robot-agent bridges converged on independently — [AgenticROS](agenticros.md)'s `interruptible` / `blocks_base` flags and [ros2-mcp-server](ros2-mcp-server.md)'s config-driven tool filtering. Matter reached it first, at consumer scale, expressed as data rather than as an API convention. It is the strongest existing evidence that the vendor-authored-manifest pattern is where multi-ecosystem device authority lands.

## Limits relevant to this wiki

- **No robot device type**, and nothing in 1.4 contemplates a mobile actuated node.
- Nothing in the standard addresses **household multi-tenancy** in the human sense — per-person authority, guests, children. Its subjects are nodes and certificates, not people.
- **Version caveat**: 1.4 (2024-11-04) is what is ingested; CSA has since published 1.4.1, 1.4.2, 1.5 and 1.5.1. **1.5 adds cameras** — the first Matter device class whose data sensitivity approaches a home robot's.

## Related

- [Connectivity Standards Alliance](connectivity-standards-alliance.md) — publisher
- [The home AI platform — trust and authority](../syntheses/agents/home-ai-platform-trust-and-authority.md) — why this standard was ingested
- [Control abstraction levels](../concepts/robotics/control-abstraction-levels.md) — the ARL is an access-level bound expressed as data
- [AgenticROS](agenticros.md) · [ros2-mcp-server](ros2-mcp-server.md) — the robot-side capability-manifest convergence

## Mentioned in

- [Matter 1.4 Core Specification](../sources/matter-1-4-core-specification.md)
