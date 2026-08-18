---
title: Matter
type: entity
subtype: standard
created: 2026-08-17
updated: 2026-08-17
sources: 5
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
- **Fabric Synchronization / Joint Fabric** (1.4) — mechanisms for ecosystems to share devices, with per-ecosystem user consent and an Anchor CA trusted across fabrics. **Joint Fabric Administrator** is a device type as of 1.6.
- **Camera privacy controls** — `HardPrivacyModeOn` (a **physical button or switch** pausing *all* streams across every fabric), plus soft per-usage recording and livestream modes that terminate active WebRTC sessions with reason `PrivacyMode`. **An e-stop for data, on a standard with no e-stop for motion.** No retention or deletion requirements anywhere — privacy here is capture-time control, not lifecycle governance.
- **Semantic tag namespaces** — 28 of them ([Standard Namespaces](../sources/matter-1-6-standard-namespaces.md)), including a standardised vocabulary of home **areas** (Bedroom, Ensuite, GuestBathroom, Attic…), **landmarks** (Bed, Crib, Toilet, LitterBox, PetBowl…), and **Identified Human Activity** — which includes **`0x01 Fall`**.

## The two findings that matter for robotics

### 1. Multi-admin isolates configuration, not state

> "**Most cluster data instances are accessible regardless of the accessing fabric.**" ([Core Spec 1.4](../sources/matter-1-4-core-specification.md) §7.5.3)

Fabric-scoping is explicitly limited to **lists of fabric-scoped structs and fabric-sensitive events**. A device's operational state — a light's `OnOff`, a lock's position — is a **single shared value** visible and writable from every commissioned fabric.

### 2. There is no arbitration, anywhere

**"arbitrat" appears zero times in the 1,173-page core specification.** The eight occurrences of "conflict" all concern DNS-SD name collisions and ephemeral node IDs, never competing commands from different administrators.

> [!warning] Matter did not solve multi-controller arbitration — it externalized the problem
> Two ecosystems writing the same attribute is not an error, not a conflict, and not resolved by any rule in the specification. It works in practice because **the state is trivial**: a bulb toggling between two admins is an annoyance, cheaply re-set, with no physical consequence. **That property is exactly what a mobile actuated robot does not have**, which is why Matter's multi-admin model does not extend to one by analogy. See [the home AI platform synthesis](../syntheses/agents/home-ai-platform-trust-and-authority.md).

> [!note] Confirmed structural, 2026-08-17, across the full 1.6 document set
> `arbitrat` and `interlock` both appear **zero times** in all four 1.6 documents (Core 1,335 pp, Application Cluster 982 pp, Device Library 229 pp, Standard Namespaces 71 pp) — **two major versions after 1.4, and after adding Closures and a Robotic Vacuum Cleaner**, device classes that physically move. The gap is a design decision, not a backlog item.
>
> CSA is not unaware of mutual exclusion. It ships **`BusyWithOtherAdmin`** for two commissioners colliding, and an **Ecosystem Information Cluster** for "conflict resolution between multiple sources of the name and location data." It solved the problem exactly where it chose to and declined to for device commands.

> [!warning] Qualified 2026-08-17 — the keyword search missed a real mechanism
> The zero-hit result above was a search for **`arbitrat`**. **CSA's term is "conflict resolution."** The [Application Cluster spec](../sources/matter-1-6-application-cluster-specification.md) §11.2.1.2.2 is titled **"Multiple Stream Resource Conflict Resolution"**, and it defines exactly what the paragraphs above say does not exist — for **camera streams shared "among clients (potentially in different fabrics)"**: an administrator-configurable **`SetStreamPriorities`** ranking, a **mandatory reuse rule** (matching parameters ⇒ "the camera SHALL reuse the existing one"), and an **incumbent-protected, newcomer-rejected** policy (a new request that would violate an existing stream's minimum configuration "SHALL be rejected with a FAILED notification").
>
> **The claim that survives is narrower and sharper: Matter has join semantics for sensing and none for actuation.** Two fabrics requesting the same stream get *literally the same stream*; two fabrics writing the same attribute get last-write-wins. **Sensing composes; actuation does not.** That is a coherent design — and it is exactly why the model does not extend to a home robot, which is mostly actuation.

## The safety model: device-side refusal, not controller arbitration

Matter never negotiates between competing controllers. **The device refuses**, on its own local sensors and state, and reports why ([Application Cluster spec](../sources/matter-1-6-application-cluster-specification.md)):

- **`SafetyStatusBitmap`** (Window Covering) — `RemoteLockout` (*"Movement commands are ignored… e.g. not granted authorization"*), `StopInput` (*"Local safety sensor… preventing movements (e.g. Safety EU Standard EN60335)"*), `ManualOperation`, `MotorJammed`, `TamperDetection`, `ThermalProtection`.
- **Maintenance mode** — *"all commands… or local inputs that can result in movement, must be ignored"*, answering `BUSY`.
- **`CommandInvalidInState`** — for *"regulatory or manufacturer-imposed safety and security requirements that first necessitate some specific action at the device before a Start command can be honored."*
- **EVSE** — *"a safety mechanism that may lockout remote operation until the initial latching conditions have been met."*

This is the same shape the ARL takes for authority: **the device is the arbiter of last resort, and it refuses rather than negotiates.** [DimOS](dimos.md)'s `CapabilityRegistry` arrived at the same answer independently — *"Cannot start X: capability Y is held by Z."*

> [!note] Refusal is only a safe default when the null action is safe
> A window covering that refuses to move is safe. A robot that refuses to move may be **blocking a doorway**. That is a property of the device class, not of the protocol — and it is the strongest argument that Matter's model does not simply extend to home robots.

## Why the ARL is the interesting part

The **Access Restriction List is a standardized, shipping, vendor-authored bound on what an ecosystem may touch** — discoverable before commissioning (via `CommissioningARL`), negotiable (`ReviewFabricRestrictions`), and enforced *below* the administrator's own grants.

That is the same shape as the **typed capability manifest** the wiki's robot-agent bridges converged on independently — [AgenticROS](agenticros.md)'s `interruptible` / `blocks_base` flags and [ros2-mcp-server](ros2-mcp-server.md)'s config-driven tool filtering. Matter reached it first, at consumer scale, expressed as data rather than as an API convention. It is the strongest existing evidence that the vendor-authored-manifest pattern is where multi-ecosystem device authority lands.

## Limits relevant to this wiki

> [!warning] Corrected 2026-08-17 — "no robot device type" was wrong
> This page previously claimed Matter has no robot device type and that nothing contemplates a mobile actuated node. **False.** The [Device Library](../sources/matter-1-6-device-library.md) defines **§12 Robotic Device Types**, whose first entry is the **Robotic Vacuum Cleaner (`0x0074`)** — mandatory RVC Run Mode and RVC Operational State clusters, optional **Service Area**. The claim was drawn from the *Core Specification*, which is not the document that defines device types. Same error shape as the JetPack correction earlier the same day: **asserting an absence from a document that would not have contained it.**

- **Still nothing on household multi-tenancy** in the human sense — per-person authority, guests, children. Matter's subjects are nodes and certificates, not people.
- **No general home-robot device type.** The RVC is floor-cleaning-specific; nothing in 1.6 contemplates an arm or non-floor locomotion.
- **Device-side refusal is the only safety model.** There is no controller-to-controller negotiation anywhere — see below.

## Related

- [Connectivity Standards Alliance](connectivity-standards-alliance.md) — publisher
- [The home AI platform — trust and authority](../syntheses/agents/home-ai-platform-trust-and-authority.md) — why this standard was ingested
- [Control abstraction levels](../concepts/robotics/control-abstraction-levels.md) — the ARL is an access-level bound expressed as data
- [AgenticROS](agenticros.md) · [ros2-mcp-server](ros2-mcp-server.md) — the robot-side capability-manifest convergence

## Mentioned in

- [Matter 1.6 Core Specification](../sources/matter-1-6-core-specification.md) — current revision
- [Matter 1.6 Device Library](../sources/matter-1-6-device-library.md) — the 89 device types, incl. Robotic Vacuum Cleaner
- [Matter 1.6 Application Cluster Specification](../sources/matter-1-6-application-cluster-specification.md) — the device-refusal safety model
- [Matter 1.6 Standard Namespaces](../sources/matter-1-6-standard-namespaces.md) — the household ontology, incl. `Fall`
- [Matter 1.4 Core Specification](../sources/matter-1-4-core-specification.md) — superseded; retained for the 1.4↔1.6 diff
