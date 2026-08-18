---
title: Matter 1.6 Application Cluster Specification
type: source
url: https://csa-iot.org/developer-resource/specifications-download-request/
local: ../../raw/23-27350-010_Matter-1.6-Application-Cluster-Specification.pdf
author: Connectivity Standards Alliance
published: 2026-06-16 (Document 23-27350, revision 10)
ingested: 2026-08-17
venue: Connectivity Standards Alliance
format: PDF, 982 pages
tags: [matter, csa, clusters, safety, device-refusal, window-covering, rvc, evse, smart-home]
---

## Summary

The cluster definitions — what Matter devices can *do*. Ingested with the [1.6 core spec](matter-1-6-core-specification.md), and it supplies the finding that reframes this wiki's whole reading of Matter:

> [!note] **Matter's answer to physical safety is device-side refusal, not controller-side arbitration**
> Matter never negotiates between competing controllers. Instead **the device unilaterally refuses**, using its own local sensors and state, and reports *why* through a structured status attribute. Arbitration between admins is absent; **veto by the device is everywhere.** That is a coherent architecture, not an omission — and it is the same shape [DimOS](../entities/dimos.md)'s `CapabilityRegistry` arrived at independently ("Cannot start X: capability Y is held by Z").

## Key claims

### `SafetyStatusBitmap` — the device says no, and says why (Window Covering, §5.3.5.4)

| Bit | Name | Summary |
|---|---|---|
| 0 | **RemoteLockout** | *"Movement commands are ignored (locked out). e.g. **not granted authorization**, outside some time/date range."* |
| 1 | TamperDetection | *"a device has been forcedly moved without its actuator(s)"* |
| 2 | FailedCommunication | to sensors or other safety equipment |
| 3 | PositionFailure | failed to reach the desired position |
| 4 | ThermalProtection | motor/circuit thermal limit |
| 6 | Power | running on backup battery / limited power |
| 7 | **StopInput** | *"Local safety sensor (not a direct obstacle) is preventing movements (e.g. **Safety EU Standard EN60335**)"* |
| 8 | MotorJammed | mechanical problem |
| 9 | HardwareFailure | PCB, fuse, electrics |
| 10 | **ManualOperation** | *"Actuator is manually operated and is preventing…"* |

**Bit 0 is an authority statement expressed as a safety flag** — "not granted authorization" sits in the same bitmap as a jammed motor. And **bit 7 cites a real safety standard, EN 60335**, which is the only place in the four documents where an external safety standard is named as a behavioural cause.

### Maintenance mode — a total command veto

> "While in maintenance mode, **all commands (e.g: UpOrOpen, DownOrClose, GoTos) or local inputs that can result in movement, must be ignored** and respond with a **BUSY** status."

### `CommandInvalidInState` — the device's regulatory refusal (Operational State)

> "There may be either **regulatory or manufacturer-imposed safety and security requirements that first necessitate some specific action at the device** before a Start command can be honored. In such instances, a device SHALL respond with a status code of `CommandInvalidInState`."

A standardised way for a device to say *the law or my manufacturer says a human must do something here first*. This is the closest thing in Matter to an interlock, and the word "interlock" appears **zero** times.

### EVSE lockout

> "This cluster supports a **safety mechanism that may lockout remote operation until the initial latching conditions have been met.**" Fault conditions reference **SAE J1772** (GFCI, charging-circuit faults).

### RVC error semantics

The Robotic Vacuum Cleaner's operational errors are physical-world, not protocol: **`CannotReachTargetArea`** — *"The device is unable to move to an area where it was asked to operate, such as by setting the ServiceArea cluster's SelectedAreas attribute, due to an obstruction. For example, the obstruction might be a closed door or objects blocking the mapped path."* Also `DirtyWaterTankFull`, low battery.

Note what that error implies: **the robot navigates a named area model of a home and reports semantic failures against it** — see [Standard Namespaces](matter-1-6-standard-namespaces.md).

### Fan speed — safety overriding the setpoint

Even a fan may decline to obey: the current setting "MAY stay above" a newly-requested lower value "for a period necessary to dissipate internal heat, **maintain product operational safety**, etc."

## Entities mentioned

- [Matter](../entities/matter.md) · [Connectivity Standards Alliance](../entities/connectivity-standards-alliance.md)

## Concepts touched

- Device-side veto as an alternative to controller arbitration; [control abstraction levels](../concepts/robotics/control-abstraction-levels.md) — the device holds the bottom of the stack and bounds everything above it.

## Open questions

- **Does any device implement `RemoteLockout` for authorization rather than for time-of-day?** The bit's own summary names both; only one of them is an access-control mechanism.
- **Is device-side refusal sufficient for a mobile robot?** A window covering that refuses to move is safe. A robot that refuses to move may be **blocking a doorway**. Refusal is a safe default only when the null action is safe, which is a property of the device class, not of the protocol.
