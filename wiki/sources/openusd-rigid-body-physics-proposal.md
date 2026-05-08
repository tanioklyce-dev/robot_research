---
title: OpenUSD Rigid Body Physics Proposal (UsdPhysics)
type: source
url: https://openusd.org/release/wp_rigid_body_physics.html
author: Apple, NVIDIA, Pixar Animation Studios
published: 2020 (v1.0; documentation in OpenUSD 26.05 release tree)
ingested: 2026-05-07
tags: [openusd, usdphysics, rigid-body, articulation, robotics-schema, joint, drive]
---

## Summary
The authoritative whitepaper specifying the **UsdPhysics** schema family — OpenUSD's baseline extension for representing rigid-body physics, articulations, joints, and collision data inside a USD scene graph. Co-authored by Apple, NVIDIA, and Pixar; explicitly targets robotics applications alongside engineering and AI use cases. Establishes that OpenUSD is **not just a scene-description format** but a robotics-physics representation in its own right.

## Key claims

### Robotics-specific schemas
- **`PhysicsRigidBodyAPI`** — applied to `UsdGeomXformable` prims to mark them as physics-driven bodies (pose updates during simulation).
- **`PhysicsArticulationRootAPI`** — marks the root of an articulated robot. Hints to the simulator that the subtree's joints should be simulated using a **reduced-coordinate approach** (Featherstone-style) rather than maximal-coordinate constraints.
- **`PhysicsCollisionAPI`** — defines collision geometry on `UsdGeomGprim` objects.
- **`PhysicsMassAPI`** — specifies mass, density, inertia tensors, center of mass.

### Joint subtypes
Base `PhysicsJoint` with concrete subtypes:
- `PhysicsRevoluteJoint` — rotational with axis definition.
- `PhysicsPrismaticJoint` — translational.
- `PhysicsFixedJoint` — locks all DOF.
- `PhysicsSphericalJoint`.
- `PhysicsDistanceJoint`.

### Floating vs fixed articulations (robotics jargon in the standard)
> "For floating articulations (robotics jargon for something not bolted down, e.g. a wheeled robot or a quadcopter), this API should be used on the root body... For fixed articulations (robotics jargon for e.g. a robot arm for welding that is bolted to the floor), this API can be on a direct or indirect parent of the root joint."

This is the most concrete sign that UsdPhysics was authored with robotics use cases as a first-class concern, not retrofitted later.

### Joint drives (motor models)
Joint drives apply spring-damper torques: `stiffness * (targetPosition - p) + damping * (targetVelocity - v)`. Multi-apply schemas allow per-DOF instances (transX/Y/Z, rotX/Y/Z, distance).

### Units and conventions
- Distance and time follow USD conventions (`metersPerUnit`, `timeCodesPerSecond`).
- **`kilogramsPerUnit`** metadata for SI mass consistency.
- Angular values in **degrees** (not radians).
- Velocities in local space (consistent with `UsdGeomPointInstancer`).

### Collision filtering
- Group-based via `CollisionGroup`.
- Pairwise via `FilteringPairsAPI` for explicit interaction control.

## Limitations
- **No nested rigid bodies**: `PhysicsRigidBodyAPI` in subtrees of existing bodies is silently ignored.
- **No scaling during simulation**: dynamic scaling unsupported; affects joint frame specifications.
- Multiple colliders on a single geometry require a parent `Xform` wrapper.
- Sleep/deactivation state is implementation-specific; not exposed to USD.

## Entities mentioned
- [[openusd|OpenUSD]] — the parent format.
- [[nvidia|NVIDIA]] — co-author and primary downstream consumer (Isaac Sim / Isaac Lab / Newton).

## Concepts touched
- Robotics schemas in scene-description formats (the structural fact this document establishes).

## Open questions
- Why degrees for angular values rather than radians? (USD-wide convention vs. robotics norm.)
- How does `PhysicsArticulationRootAPI` interact with closed kinematic chains, which URDF cannot represent?
- Is the schema sufficient to round-trip a MJCF or URDF model through USD without information loss? The proposal does not address conversion fidelity.
