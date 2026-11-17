# Holoscan SDK v5.0.0 — GitHub release notes (published 2026-10-21T03:30:20Z)
Source: https://github.com/nvidia-holoscan/holoscan-sdk/releases/tag/v5.0.0 — release body via GitHub API, fetched 2026-11-16.

## <a id="release-artifacts"></a>Release Artifacts

The links below identify the Holoscan SDK 5.0 installation channels. Check individual channels for published artifacts.

- 🐋 [Docker container](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/clara-holoscan/containers/holoscan): tag `v5.0.0-cuda13`
- 🐍 Python wheels: `pip install holoscan==5.0.0`

  <details>
  <summary>Python wheel packages</summary>

  All packages below are version **5.0.0**. Native component wheels target CPython 3.12+ (`abi3`) on Linux (`manylinux_2_39`) with CUDA 13. Universal wheels are metapackages that select the corresponding native components.

  | Package | Contents |
  | --- | --- |
  | [holoscan](https://pypi.org/project/holoscan/5.0.0/) | Full SDK metapackage |
  | [holoscan-cu13](https://pypi.org/project/holoscan-cu13/5.0.0/) | CUDA 13 SDK metapackage |
  | [holoscan-core](https://pypi.org/project/holoscan-core/5.0.0/) | Core metapackage |
  | [holoscan-core-cu13](https://pypi.org/project/holoscan-core-cu13/5.0.0/) | Core native component (CUDA 13) |
  | [holoscan-vision](https://pypi.org/project/holoscan-vision/5.0.0/) | Vision metapackage |
  | [holoscan-vision-cu13](https://pypi.org/project/holoscan-vision-cu13/5.0.0/) | Vision native component (CUDA 13) |
  | [holoscan-visualization](https://pypi.org/project/holoscan-visualization/5.0.0/) | Visualization metapackage |
  | [holoscan-visualization-cu13](https://pypi.org/project/holoscan-visualization-cu13/5.0.0/) | Visualization native component (CUDA 13) |
  | [holoscan-inference](https://pypi.org/project/holoscan-inference/5.0.0/) | Inference metapackage |
  | [holoscan-inference-cu13](https://pypi.org/project/holoscan-inference-cu13/5.0.0/) | Inference native component (CUDA 13) |

  For more details, see [Python Bindings](#release-python-bindings).

  </details>

- 📦️ [Debian packages](https://developer.nvidia.com/holoscan-downloads)
- 📕 [Documentation](https://docs.nvidia.com/holoscan/sdk-user-guide/)

See [SDK Installation prerequisites](https://docs.nvidia.com/holoscan/sdk-user-guide/setup/sdk-installation#prerequisites) for supported platforms and system requirements.

## <a id="release-notes"></a>Release Notes

### New Features and Improvements

> [!IMPORTANT]
> Holoscan SDK 5.0 is a ground-up rewrite of the Holoscan SDK runtime and API.

Learn more about the Holoscan platform at [holoscan.org](https://holoscan.org/).

#### API stability

The Stable source API core covers basic in-process graph/operator authoring, ordinary built-in scalar ports, existing explicitly named and unambiguous Python port declarations/lookup, and structured error handling in C++ and Python. These documented source contracts remain compatible across 5.x updates; deprecation and removal follow the major-release policy described in [API stability](https://docs.nvidia.com/holoscan/sdk-user-guide/introduction/api-stability). The Stable entry-point call contracts do not freeze omitted-contract trigger resolution, clock selection/admission, or automatic queue/resource derivation; these policies remain Beta. Tensor declarations, ownership, output specifications, and pools remain Beta. Plan inspection, resolved-defaults reports, typed records, and report formats remain Prototype. Existing schema version counters and compatibility epochs are retained across GA and follow their own evolution rules. Source API stability does not promise binary compatibility between SDK packages or cross-version interoperability for channels, schemas, or serialized artifacts. Follow the release-specific rebuild and deployment requirements when upgrading.

#### Programming model

- **Callback-scoped scalar borrowing (C++ and Python)** - `Input<T>::selected_sample()` exposes immutable selected data and metadata without a payload copy, heap allocation, or owning read claim. `sensor_io::ImageDescriptorScratch` prepares bounded metadata storage during startup for Image transforms; output pixels still use a separate Tensor loan. Hosted Python Operators expose the same frozen scalar selection as `OperatorPort.selected_sample()`: metadata remains independently inspectable, while `.data` lazily materializes an owning Python projection. C++ views, references, and the Python selection facade must not escape the compute callback. Owning receive APIs remain available.
- **Prepared generated-schema transforms (C++)** - Generated ordinary and descriptor-Tensor schemas can opt into bounded reusable native metadata with `NATIVE_BOUNDS_FILE`. `schema::SchemaScratch<T>` and `schema::DescriptorMetadataScratch<T>` retain cold-prepared capacity, while `Output<T>::emit_ref()` synchronously publishes an ordinary generated schema without a by-value native-object copy. Values outside authored native bounds fail with `ErrorCode::kResourceExhausted`; altering prepared owners or retaining a nested owner across reuse fails closed with `ErrorCode::kPreparedStorageInvalid`. The bounds policy is a build and deployment contract rather than wire identity, so every producer and prepared consumer for a schema must use the same bounds file. Owning APIs remain available alongside prepared storage.
- **`holoscan::Graph` API** - Graph definition without an `Application` wrapper. `compile()` produces an immutable `ExecutionPlan`; `run_async()` returns a `RunSession` for deterministic asynchronous execution and clean shutdown.
- **Typed Operators and ports** - Operators declare strongly typed input and output ports; payloads flow as `Sample<T>` with causal metadata.
- **Reusable Graph embedding** - A compiled subgraph can be embedded into a parent graph and reused across multiple compositions.
- **CUDA Graph regions** - Applications can explicitly fuse an eligible fixed-shape, linear GPU region with `RegionConstraint::cuda_graph()`. Runtime captures member CUDA work once after lifecycle startup and replays it on the source's planned stream while retaining ordinary Tensor readiness and publication behavior. The ordinary execution path remains available for comparison.
- **Automatic graph partitioning and inspection** - Graphs without partition declarations use the `holoscan.partition.source_chain/1` planner, which forms linear execution chains across the complete DAG, including fan-out, fan-in, diamond, and parallel edge topologies. Different partitions may execute callbacks concurrently. Applications can author exact manual anchors and request an automatic remainder, use `partition(name).include_all()` for one complete composed partition, and inspect the accepted cover through `ExecutionPlan::partitions()`. Green Context bindings require exact named anchors; dedicated contexts are not assigned automatically.
- **CUDA streams follow execution partitions** - By default, each active execution-partition/device pair receives one Runtime-owned CUDA compute stream, allowing independent branches to submit GPU work independently while Tensor readiness and release ordering remain automatic. Applications can select `CudaComputeStreamPolicy::kSharedProcessDevice` in `CompileOptions` when measurements favor one ordinary stream per process group and device. Separate streams permit but do not guarantee concurrent CUDA execution.
- **Support-thread placement (C++)** - Applications can request CPU affinity for the run-session controller and, when present, the process-local Channel pump. The compiled plan records the admitted placement. A pump binding does not create a pump when the selected transport does not need one.
- **CUDA Green Context manual placement (developer preview)** - Applications can query a qualified CUDA 13 target, bind an exact manually authored execution partition to a driver-structured set of streaming multiprocessors, and inspect the accepted placement and diagnostics in the compiled plan. The compiler and Runtime validate the target, materialize the Green Context streams before operator execution, and preserve Tensor ordering across ordinary and Green Context streams. Automatic graph partitioning does not automatically size or assign dedicated contexts. See the [CUDA Green Contexts guide](https://docs.nvidia.com/holoscan/sdk-user-guide/advanced/cuda-green-contexts).
- **Lifecycle stage graph** - Bounded operator lifecycle with deterministic startup, running, and shutdown stages.
- **Managed shutdown signals** - On Linux, blocking `run(plan)` synchronously accepts SIGINT and SIGTERM through an HSDK signal domain by default; the first accepted occurrence requests cooperative stop. `RunSignalPolicy::kCallerManaged` provides a blocking opt-out, while early `ManagedShutdownSignals` plus `run_async(plan, signals)` provides managed asynchronous execution. Plain `run_async(plan)` remains caller-managed. A second accepted occurrence delegates the actual signal under the unchanged prior policy; first-signal shutdown remains cooperative, with no forced cancellation or whole-run completion bound. A clean first accepted SIGINT returns control after cleanup with a nonzero blocking result (currently `1`). Managed blocking runs require an adoptable signal domain or a single live task during setup; otherwise they fail before session creation. Establish `ManagedShutdownSignals` before creating participant threads when managed asynchronous execution is needed. An adopted domain has one binding attempt; close it after retirement and create a fresh domain for another managed run. A child created while the domain is active inherits blocked SIGINT/SIGTERM, and `exec()` preserves that mask. Reset the child mask with `sigprocmask()` before `exec()`, or use `POSIX_SPAWN_SETSIGMASK`; `system()` and `popen()` do not reset it automatically.

#### Temporal scheduling

- **Temporal contracts** - `OnEach`, `LatestWithin`, and `Skip` combinators control per-input selection policy; each operator declares a `Contract` that is verified at compile time.
- **Maximum start delay** - C++ `Contract::max_start_delay(...)` and Python `Contract.max_start_delay(...)`, paired with `on_violation(...)`, bound how late `compute()` may start relative to the trigger's frozen source coordinate. Entry exactly at the bound is permitted. This contract does not bound compute completion or preempt a callback. See the [Temporal Contracts guide](https://docs.nvidia.com/holoscan/sdk-user-guide/building-operators/temporal-contracts#maximum-start-delay).
- **Deterministic time and clock identities** - Monotonic clock registry and execution identities for reproducible trace correlation.

#### Parameters

- **Typed parameter system** - Operators declare typed parameters with optional defaults; parameter values are snapshot-consistent across an activation.
- **Unified startup parameter authoring** - Decode startup configuration with `try_decode<T>()` or the throwing `decode<T>()`, move the resulting `PreparedParams<T>` into `OperatorHandle::set_params()`, and compile the graph. Use graph-owned `params::set_params()` or `load_and_set_params()` for atomic multi-operator configuration or snapshot restore before compilation. Semantic edits with `Document::patched()` may clear the exact current-source digest; guarded saves should use `document.digest().base_source` as `SaveOptions::expected_source_digest`.
- **Runtime parameter generations** - Parameter values can be updated at runtime between activations; a generation counter ensures consumers observe a consistent snapshot.
- **Parameter configuration and persistence** - Parameter sets are serializable to and from configuration files; an experimental tuner supports iterative parameter search.
- **Derived Tensor pool capacity** - Tensor output byte-span capacity can be derived during compilation from Parameter bounds, input bounds, and lifecycle-selected limits. Nominal-rate evidence can independently derive the edge queue depth needed for that output. The compiled plan retains both derivations and reports invalid or incomplete formulas; explicit capacity and queue depth remain available when needed. See the [Tensor sizing guide](https://docs.nvidia.com/holoscan/sdk-user-guide/data-and-payloads/tensors-in-depth).
- **Parameter-derived Tensor storage (C++)** - Tensor outputs can select host or device memory from compile-time parameter values. A named projector can derive a bounded output byte span when the built-in size expressions are insufficient; the compiler checks and freezes both choices before execution.
- **Bounded Vision outputs (C++)** - Vision operators can derive fixed output-pool bounds from their typed parameters or an input Tensor's maximum size. Invalid or overflowing bounds fail during setup or compilation.

#### Channels and transport

- **In-process channel binding** - Zero-copy operator-to-operator communication within a process via a shared temporal cache; no serialization is required.
- **Bounded Tensor allocation with CUDA stream integration** - Host-pinned and device `Tensor` producers with explicit device placement, CUDA stream association, and loan/commit lifetime semantics. *Requires a CUDA device.*
- **Typed Tensor port contracts** - `TensorRepresentation`, `TensorBounds`, `TensorInputSpec`, `TensorOutputSpec`, and `TensorBoundaryContract` describe Tensor representation, bounded output storage, and boundary requirements. The same input and output specs apply to descriptor-schema Tensor fields. Transfer policy belongs in `TensorOutputSpec::transfer`; input memory conversion belongs in `TensorInputSpec::memory_conversion`. See the [Tensors 101 guide](https://docs.nvidia.com/holoscan/sdk-user-guide/getting-started/tensors-101) and [Custom FlatBuffer Schemas guide](https://docs.nvidia.com/holoscan/sdk-user-guide/data-and-payloads/custom-flatbuffer-schemas).
- **Bounded drop-oldest queues** - `QueuePolicy::kDropOldest` with depth one retains the freshest sample. Larger depths retain the newest bounded N-sample backlog in FIFO order. See the [Composing a Graph guide](https://docs.nvidia.com/holoscan/sdk-user-guide/getting-started/composing-a-graph).
- **Sensor payload schemas** - Image and IMU schemas and Image metadata helpers are provided by `holoscan::sensor_io`. Include `<holoscan/sensor_io/image_metadata.hpp>` and link `holoscan::sensor_io`; schema types retain their `holoscan::schema` names.
- **Interprocess channel runtime** - HoloMQ/iceoryx2-backed bounded IPC transport with zero-copy GPU memory across process boundaries.
- **External channel clients** - Standalone non-Operator processes connect to a running graph using only `endpoint-catalog.json` and the stable endpoint name; client code does not require HoloMQ headers.
- **Explicit external subscriber close** - Scalar, POD, generated-schema, raw-Tensor, and descriptor-Tensor Channel subscribers now provide a checked `close()` operation for deterministic local endpoint retirement. Subscriber close discards unread local work and makes later checked operations report `kClosed`; it does not publish producer EOS, close a graph port, or contribute natural-completion evidence. Publisher `close()` remains the ordered EOS operation.
- **External producer EOS propagation** - Ordered publisher EOS now has explicit end-to-end coverage through finite input-driven graph paths. Earlier accepted data and retained work drain before eligible Operator outputs close; live external subscribers observe final data before `kClosed`, and a fully finite graph reaches natural `kCompleted` without `request_stop()`. Inputs on independent triggers remain side inputs, and admitted external-restart capacity keeps outputs open for the replacement generation. A required export subscriber must remain attached through remote EOS; disappearance after data acceptance fails terminal drain rather than satisfying EOS or retrying indefinitely.
- **Descriptor-Tensor schema external topics** - Graph imports and exports now carry application-owned singular or multi-Tensor descriptor schemas through the endpoint catalog. Standalone non-Operator peers attach with the catalog-aware tensor-schema publisher and subscriber facades, preserving typed per-field contracts, metadata, capture coordinates, bounded backing, cross-process operation, and ordered health, data, and end-of-stream control. Tensor bytes remain in retained or imported backing rather than being serialized inline. See the [External Topic Boundaries guide](https://docs.nvidia.com/holoscan/sdk-user-guide/composing-applications/external-topics).
- **Larger catalog inline services** - Ordinary catalog-attached scalar, POD, and generated-schema endpoints now support complete fixed-inline frames through 32 KiB. After framing, the maximum application capacities are 32,744 bytes for scalar/POD and 32,704 bytes for ordinary generated schemas. Raw Tensor and descriptor-Tensor backing remains out of band and does not count toward this inline limit. See the capacity details in [External Topic Boundaries](https://docs.nvidia.com/holoscan/sdk-user-guide/composing-applications/external-topics) and [Standalone Channel Clients](https://docs.nvidia.com/holoscan/sdk-user-guide/advanced/standalone-channel-clients).
- **Event-driven channel waits** - Typed subscribers block on their transport event lane with `wait_and_receive_sample` instead of polling `receive_sample`; a wait takes an absolute deadline, cancels through a `std::stop_token`, and reports timeout, cancellation, and end of stream as distinct outcomes.
- **External subscriber event-loop integration (C++)** - Supported scalar, Tensor, and generated-schema subscribers expose a move-only readiness handle for Linux `poll`, `select`, or `epoll`. Applications acknowledge a wake and drain nonblocking receives without a separate polling helper thread.

#### Graph artifacts

- **Cold artifact generation** - A graph-definition executable can emit its deployment bundle (`endpoint-catalog.json`, FlatBuffers schema packages, and compiled plan) without starting operator lifecycle, CUDA, or transport. The `--emit-artifacts` CLI flag and `_graph_artifacts` CMake build target support this workflow. Rebuilding the target is a no-op when nothing has changed. Partition-inspection, Tensor-placement, and Parameter record keys share the segment-encoded `OperatorPath` grammar without a leading slash, such as `pipeline/source`.
- **HoloMQ library (`holoscan::holomq`)** - Zero-copy GPU IPC publish/subscribe transport built on iceoryx2 v0.9.3 and shipped with the Holoscan SDK. The `holomq::holomq` target remains a compatibility alias. Features include publish/subscribe queue controls, drop-oldest queues, and reusable host-memory imports that can be rebound across connection refresh.

#### Visualization

- **Typed image and Tensor layers** - Image layers of `holoscan::visualization::HolovizOp` bind `Input<holoscan::schema::ImageT>` through `image_layer_input(i)`; geometry, text, and LUT layers bind `Input<holoscan::Tensor>` through `tensor_layer_input(i)`. Both accessors use the declared layer index, with up to eight layers in any mix. Image metadata is checked against the declared `ImageLayerDesc`: `width` and `height` give the visible size, while `plane_layouts` describe backing storage, including the two planes of NV12 frames. Color-space declarations must match the layer's color-space and YUV-model settings; an `UNSPECIFIED` wire color space is accepted into any layer. Holoviz consumers depend on `holoscan::sensor_io`, which `find_package(holoscan COMPONENTS visualization)` loads. See the [Visualization guide](https://docs.nvidia.com/holoscan/sdk-user-guide/modules/visualization).
- **HolovizOp CUDA output** - `HolovizOp` can render to a CUDA-backed `schema::ImageT` output for another visualization, encoder, or inference operator without an intermediate display. The application binds the output to the intended CUDA device; see the source-tree CUDA sink example.

#### <a id="release-python-bindings"></a>Python Bindings

The [`holoscan-core-cu13`](https://pypi.org/project/holoscan-core-cu13/5.0.0/) distribution provides the `holoscan` Python package for graph authoring, compilation, execution sessions, typed ports and parameters, Tensor interchange, and external-channel clients. Tensor values support DLPack and NumPy/CUDA array interfaces. Python coverage is broad but not identical to the C++ API; module-specific and newly introduced facilities can have narrower coverage.

Python bindings for Vision, Visualization, and Inference are built as separate CUDA 13 component distributions, respectively [`holoscan-vision-cu13`](https://pypi.org/project/holoscan-vision-cu13/5.0.0/), [`holoscan-visualization-cu13`](https://pypi.org/project/holoscan-visualization-cu13/5.0.0/), and [`holoscan-inference-cu13`](https://pypi.org/project/holoscan-inference-cu13/5.0.0/), each depending on the matching Core distribution. Their canonical packages are `holoscan_vision`, `holoscan_visualization`, and `holoscan_inference`; installed providers can also be discovered under the corresponding `holoscan.<module>` alias. Vision exposes registered image-processing operators, including Bayer demosaicing, through generated typed facades; Visualization and Inference expose `HolovizOp` and `InferenceOp` graph authoring through their module facades.

The [`holoscan`](https://pypi.org/project/holoscan/5.0.0/) metapackage selects the CUDA 13 Core, Vision, Visualization, and Inference distributions through [`holoscan-cu13`](https://pypi.org/project/holoscan-cu13/5.0.0/). Install individual component distributions when only part of the SDK is needed, using the same SDK version for each component. Wheels contain Python bindings and native runtime libraries; C++ headers, CMake package files, examples, and sample datasets are provided through the other installation options.

#### Example catalog

- **Install-tree smoke tests** - `hello_world`, `hello_core`, `hello_logger`, `hello_tensor`, `hello_schema`, `hello_matx`, and `hello_cccl` check SDK headers, CMake targets, and selected third-party dependencies in an SDK installation.
- **SDK example applications** - `slow_fast_fusion` shows a two-rate graph with temporal scheduling in C++ and Python; `camera_imu_control` shows a camera/IMU fusion graph with external import and control export in both languages; and `external_clients` supplies `external_client_relay`, `sensor_daemon`, and `result_recorder` companion programs with Python client variants. See the [Slow/Fast Fusion](https://docs.nvidia.com/holoscan/sdk-user-guide/examples/slow-fast-fusion), [Camera + IMU Control](https://docs.nvidia.com/holoscan/sdk-user-guide/examples/camera-imu-control), and [External Clients](https://docs.nvidia.com/holoscan/sdk-user-guide/examples/external-clients) guides.

#### Performance

- Runtime dispatch suppresses redundant HoloMQ wake notifications and avoids polling cycles when no event-backed readiness source can make progress, reducing activation and fanout overhead. The expanded benchmark suites attribute Runtime and transport costs separately; their dated measurements are reference evidence rather than guarantees for other systems. See the [Core Runtime Benchmarks](https://docs.nvidia.com/holoscan/sdk-user-guide/performance/core-runtime-benchmarks) and [Channel Benchmarks](https://docs.nvidia.com/holoscan/sdk-user-guide/performance/channel-benchmarks).
- Tensor pool and catalog tensor-backing sharing reduce allocation pressure.
- Channel and HoloMQ benchmark suite (`comm_benchmark`).

### <a id="breaking-changes"></a>Breaking Changes

> [!WARNING]
> Holoscan SDK 5.0 is not source- or binary-compatible with Holoscan SDK 4.x. Port applications to the graph, typed-port, temporal contract, and parameter APIs described above. See [Migrating from Holoscan SDK 4.x](https://docs.nvidia.com/holoscan/sdk-user-guide/introduction/migrating-from-4x) and [Migrating Python from Holoscan SDK 4.x](https://docs.nvidia.com/holoscan/sdk-user-guide/introduction/migrating-python-from-4x).

#### API and ABI changes

- **Unified startup parameter authoring** - The detached `ParamOverrideSet` path was removed, including `decode_overrides()`, `to_overrides()`, `load_overrides()`, `make_param_rebind_target()`, `ParamAdmissionContext`, and `CompileOptions::parameter_overrides`. Decode ordinary startup configuration with `try_decode<T>()`, move the resulting `PreparedParams<T>` into `OperatorHandle::set_params()`, and call the normal `compile(graph, options)`. For an atomic multi-operator configuration or snapshot restore, call the graph-owned `params::set_params()` or `load_and_set_params()` form before compiling. No compatibility shim is provided for the removed APIs. Applying semantic edits with `Document::patched()` may clear its exact current-source digest; guarded saves of an edited document should use `document.digest().base_source` as `SaveOptions::expected_source_digest`. The `decode_params<T>()` and `decode_params_or_throw<T>()` names are now `try_decode<T>()` and `decode<T>()`, respectively.

- **Temporal maximum start delay** — C++ `Contract::deadline(...)` and Python `Contract.deadline(...)` are now `max_start_delay(...)`, with no compatibility aliases. Related inspection types, record fields, activation reasons, derived-term identifiers, and compiler/runtime diagnostic tokens also change. Update callers and diagnostic filters using the [complete migration map](https://docs.nvidia.com/holoscan/sdk-user-guide/building-operators/temporal-contracts#migrating-early-access-contracts). Rebuild C++ applications and regenerate artifacts: temporal records advance from version 1 to 2 and private execution plans from v8 to v9, with renamed keys and witness identities. Old artifacts have no compatibility reader. The inclusive compute-start bound and violation policies remain unchanged.

- **Tensor port-spec revision**: Tensor port authoring now uses `TensorRepresentation`, `TensorBounds`, `TensorInputSpec`, `TensorOutputSpec`, and `TensorBoundaryContract`. Replace `TensorPortLayout` with `TensorRepresentation`; replace separate `TensorAllocationBounds` and `tensor_allocation()` calls with `TensorOutputSpec{.bounds = tensor_bounds(...), .storage = TensorOutputStorage::kRuntimePool}`; replace `LogicalTensorRequirements` and `LogicalTensorBounds` with `TensorBoundaryContract`; and use the same input and output specs for descriptor-schema Tensor fields. Transfer policy belongs in `TensorOutputSpec::transfer`, while input memory conversion belongs in `TensorInputSpec::memory_conversion`. This is an intentional source and ABI break: perform a clean rebuild, and do not mix libraries, plugins, generated artifacts, or endpoint catalogs from before and after this change. See the [Tensors 101 guide](https://docs.nvidia.com/holoscan/sdk-user-guide/getting-started/tensors-101), and [Custom FlatBuffer Schemas guide](https://docs.nvidia.com/holoscan/sdk-user-guide/data-and-payloads/custom-flatbuffer-schemas).

- **HolovizOp image layers carry `schema::ImageT`**: Image-kind layers of `holoscan::visualization::HolovizOp` now bind `Input<holoscan::schema::ImageT>` ports and check each frame's `encoding`, `color_space`, and `plane_layouts` against the declared `ImageLayerDesc`; geometry, text, and LUT layers keep `Input<holoscan::Tensor>`. The uniform `layer_input(i)` accessor is replaced by `image_layer_input(i)` and `tensor_layer_input(i)`, both indexed by declared layer. Migrate `graph.add_flow(camera->frame, viz->layer_input(0))` to `graph.add_flow(camera->frame, viz->image_layer_input(0))`, where `camera->frame` is an `Output<schema::ImageT>` published with `emit_tensor(loan, descriptor, options)`, and overlay edges to `viz->tensor_layer_input(i)`. `ImageT::width`/`height` are the visible size; NV12 frames carry the schema's two `plane_layouts` records (Y, UV), so the backing Tensor may be a flat byte buffer. A wire `color_space` of `UNSPECIFIED` is accepted into any layer; `SRGB` requires `ColorSpace::kSRGBNonlinear` and `REC601`/`REC709`/`REC2020` on a YUV format require the matching `yuv_model`. `holoscan::sensor_io` is now a public link and runtime dependency of every HolovizOp consumer; `find_package(holoscan COMPONENTS visualization)` loads it. The layer budget stays `kMaxLayerPorts` (8) in any kind mix. This is a source and ABI break: rebuild consumers.

- **Sensor payload schemas moved to `holoscan::sensor_io`**: `image.fbs`, `imu.fbs`, and the Image metadata helpers moved out of the Core schema library. Sources include `<holoscan/sensor_io/image_metadata.hpp>` instead of `<holoscan/schema/image_metadata.hpp>` and link `holoscan::sensor_io`. The affected symbols keep their `holoscan::schema` names, but `libholoscan_sensor_io.so` defines them instead of `libholoscan_schema.so`, so objects and libraries built against the earlier Core schema library must not be mixed with this release; perform a clean source rebuild.

- **Queue-policy simplification** - `QueuePolicy::kLatest` is removed, and `kDropOldest` has numeric value 1 in Core, Channel, and HoloMQ. Rebuild all consumers; objects and libraries compiled against the previous enum must not be mixed with this release. Migrate `kLatest` to `kDropOldest` with depth one to preserve freshest-only mailbox behavior. Retaining an authored depth greater than one is an intentional semantic change: the queue preserves the newest bounded N-sample backlog in FIFO order. See the [Composing a Graph guide](https://docs.nvidia.com/holoscan/sdk-user-guide/getting-started/composing-a-graph).

#### Graph execution and artifacts

- **Default automatic partitioning and artifact contract** - Graphs with no partition declarations now use the production source-chain planner. Multiple resulting partition owners may execute callbacks concurrently and change observable ordering across partitions. Applications that depend on the previous one-owner topology should use `partition(name).include_all()` as the compatibility form or author exact anchors. The public partitioning-plan record layout requires downstream rebuilds. Embedded partition-inspection and Tensor-placement keys now use the same segment-encoded, no-leading-slash `OperatorPath` grammar as Parameter records; replace leading-slash spellings such as `/pipeline/source` with `pipeline/source`.

- **Private execution-plan schema** - The current private artifact schema is `holoscan.execution_plan.private.v9`. No forwards or backwards compatibility is provided: there is no older-schema reader or translation path. Regenerate artifacts with the current SDK because any schema-identifier mismatch fails before admission. The private schema is not an ABI promise.

- **Linux blocking-run signal policy**: `run(plan)` now requires either an adoptable compatible managed domain or exactly one live task at both process-task census reads; otherwise it fails before session creation. With no adoptable domain, successful census reads that change or are not exactly one report `RUNTIME_MANAGED_SIGNAL_DOMAIN_REQUIRED`, while a census read error reports `RUNTIME_MANAGED_SIGNAL_INSTALL_FAILED`; an unavailable domain or binding, or a poisoned process registry, reports `RUNTIME_MANAGED_SIGNAL_OWNER_BUSY`. Adopting an explicit domain consumes its sole binding attempt, so close it after retirement and create a fresh domain before another managed run. Hosts that already own process signals should use `run(plan, RunSignalPolicy::kCallerManaged)` or plain `run_async(plan)`; hosts needing managed async behavior should establish `ManagedShutdownSignals` before creating participant threads. A child created while that domain is active inherits the blocked SIGINT/SIGTERM mask, and `exec()` preserves it: reset the child mask with `sigprocmask()` before `exec()`, or use `POSIX_SPAWN_SETSIGMASK` with an application-chosen mask. `system()` and `popen()` do not perform that reset automatically.

#### Platform and toolchain requirements

- **Platform requirements** - Holoscan SDK 5.0 requires CUDA 13 and does not support IGX Orin or JetPack 6 and earlier. Building C++ applications against an installed SDK requires CMake 4.0 or newer. See [SDK Installation prerequisites](https://docs.nvidia.com/holoscan/sdk-user-guide/setup/sdk-installation#prerequisites).

### Advance notice: OnSpin compatibility in a future release

A future Holoscan SDK release is planned to introduce a new API for native Boolean readiness. The current proposal uses `OnCondition` with rising-edge and level-triggered firing. The release schedule, API name, and signatures are still subject to change. This API is not available in 5.0.

Existing supported 5.0 applications using `OnSpin` will remain supported when the new API is introduced. The C++ Spin API and its supported behavior will be retained, so upgrading to that release will not require a migration. You can keep your existing code as it is. Migration guidance will be provided when the new API is released.

This notice does not deprecate `OnSpin` in 5.0 or add compiler deprecation warnings. No removal release has been announced. The compatibility commitment covers the supported public API, not private runtime bindings. HSDK 5.0 has no public API for attaching a Spin predicate and no Python Spin authoring API. See the [Spin compatibility guide](https://docs.nvidia.com/holoscan/sdk-user-guide/building-operators/temporal-contracts#onspin-compatibility-and-future-readiness-apis) for the existing C++ API, firing behavior, and binding limits.

### <a id="bug-fixes"></a>Bug Fixes

Camera and Holoscan CLI entries refer to the separately distributed companion components.

| Issue | Component | Description |
| ----- | --------- | ----------- |
| — | core | Fixed Runtime startup for process-local 1:1 and fanout graphs whose application-defined FlatBuffers schema contains one descriptor-backed CUDA-device Tensor field. The single-field schema now uses the same admitted binding path without requiring a dummy host Tensor field. See the [Custom FlatBuffer Schemas guide](https://docs.nvidia.com/holoscan/sdk-user-guide/data-and-payloads/custom-flatbuffer-schemas). |
| — | core | Fixed typed inline receive so temporary typed-slot contention cannot drop an already accepted sample while receive staging is blocked. |
| — | core | Fixed subscriber-owner wake routing for single-process graphs with multiple execution partitions. |
| — | core | Fixed bracketed temporal windows so their anchors stop after end of stream instead of repeatedly scheduling empty windows. See the [Temporal Contracts guide](https://docs.nvidia.com/holoscan/sdk-user-guide/building-operators/temporal-contracts). |
| — | core | Fixed stale retained `LatestWithin` evidence retirement, including retained Tensor readiness and end-of-stream paths, so a stale sample cannot remain falsely reusable. See the [Temporal Contracts guide](https://docs.nvidia.com/holoscan/sdk-user-guide/building-operators/temporal-contracts). |
| — | core | Fixed pinned-host Tensor deallocation ordering so ordinary and CUDA Graph pipelines retain the consumer stream until asynchronous access is safe to release. |
| 6525925 | core | Clarified the external-client example procedure: artifact emission writes a deployment bundle, while the no-argument example starts the graph used for its end-to-end smoke test. |
| 6526032 | core | Updated Python Tensor test and benchmark device selection to handle deferred CUDA initialization on mixed-GPU Tegra systems. The affected runtime completion test now waits for its readiness boundary before replaying an event. |
| 6571835 | core | Corrected physical-core detection for benchmark CPU selection on platforms such as IGX Thor, allowing the documented Core Runtime benchmark preset to launch with the recommended CPU selection. |
| 6572980 | core | Stabilized the Core Runtime benchmark suite's Tensor and transport cases across the affected platforms. |
| 6717629 | core | Corrected runtime Channel readiness and contention-retry behavior that could stall GH200 transport benchmarks during publication. |
| 6568005 | visualization | Corrected Holoviz Vulkan initialization to select matching surface-maintenance and swapchain-maintenance extensions, and to reject an unsupported pairing early. |
| 6835093 | inference | Corrected Inference Python stub-generation dependencies so the Image schema module is built before it is imported during a parallel source build. |
| 6835133 | core | Corrected managed-signal setup in the running-and-stopping example. Green Context example tests now skip configurations with insufficient capacity and include shared-context coverage. |
| 6837623 | core | Corrected CUDA queue ordering in the borrowed-descriptor tests and added private IPC isolation for shared-host test runs. |
| 6800245 | camera | Corrected V4L2 setup on IGX R38.5 to skip downloading unsupported Argus headers. |
| 6840016, 6843559 | camera | Corrected standalone V4L2 build selection so unrelated SIPL and Argus components are not built by default. |
| 6927709 | cli | Corrected `env-check` discovery of SDK libraries installed by Debian packages under `/usr/lib/<triplet>`. This correction requires the updated CLI. |
| 6932398 | core | Updated `hello_matx` to fetch MatX when it is not found in the SDK distribution, and clarified that MatX is an example dependency rather than a Core SDK build dependency. |
| 6933604 | vision | Corrected `vision_pipeline` so its `cpp` directory can be configured directly as a standalone CMake project against an installed SDK. |

### <a id="known-limitations"></a>Known Limitations

- Python bindings do not yet cover every C++ capability. The separately built module bindings require their native dependencies; Inference also requires a compatible TensorRT 10 runtime in the deployment environment.
- Interprocess Channel transport and external subscriber readiness integration use Linux facilities. CUDA-backed examples and module operators require a supported CUDA 13 environment and suitable hardware.
- **Camera capture quality (6744108)** - On some USB camera and host configurations, V4L2 capture can intermittently report degraded frames or lose frames. Similar drops have been observed with direct V4L2 capture; the underlying capture-quality limitation remains unresolved.

### <a id="known-issues"></a>Known Issues

Camera entries apply to the separately distributed Holoscan Camera module.

| Issue | Component | Description |
| ----- | --------- | ----------- |
| — | packaging | Debian packages, Core-only installations, and builds with `HOLOSCAN_BUILD_PYTHON=OFF` omit `holoscan/python/constructor_handle_capsule.hpp`. Downstream C++/Python extensions using `__holoscan_constructor_handle__` can fail to compile because this header is missing. As a workaround, vendor `include/holoscan/python/` from the SDK source matching the installed release, preserve its directory structure, and add the parent `include/` directory to the extension's include path. Full Python-enabled source installations already include this header. |
| 6957369 | core | In Holoscan SDK 5.0, CUDA graph pipelines whose egress consumer runs in another execution partition can intermittently terminate with `RUNTIME_OPERATOR_REPLAY_MISMATCH` (`partition_causal_frontier_ingress`). This was observed on Jetson AGX Orin when pinned-host ingress is inside the CUDA graph region and device egress is outside it. The fix is planned for 5.1. |
| — | visualization | On AGX Thor, display output at refresh rates above 144 Hz can crash the SoC display engine, including when a high-refresh-rate mode is selected through X11. Use a display refresh rate of 144 Hz or lower. If the crash occurs, physically disconnect and reconnect power to recover; a software reboot is insufficient. |
| 6801049 | camera | SIPL capture from a single mapped VB1940 camera can fail on Jetson AGX Thor. The reported single-camera failure remains under investigation separately from stereo startup timing. |
| 6843297 | core, visualization | GH200 full-suite testing has reported visualization startup and surface failures, as well as prepared CUDA-descriptor test failures. The remaining failures are under investigation. |
| 6843550 | visualization | Visualization applications on IGX Thor with an RTX PRO 5000 Blackwell dGPU can fail to find a matching CUDA/Vulkan display adapter. Build for the intended display GPU (`CMAKE_CUDA_ARCHITECTURES=120` for this dGPU) and select that same GPU with `CUDA_VISIBLE_DEVICES`, preferably by UUID. These settings address architecture/device mismatches; some application-launch failures remain under investigation. |
| 6857163 | visualization | Visualization applications fail to launch with `--display` on DGX Spark. |
| 6934123 | camera | VB1940 stereo-synchronized capture on Jetson AGX Thor can exceed the default 15-second startup timeout. Set `--startup-timeout-s 40` for `sipl_stereo_monitor`; this timeout allowed the reported capture test to pass. |
| 6938874 | vision | Holoscan 5 CUDA 13 Debian Vision packages contain dangling public CV-CUDA SONAME and linker symlinks. The tested Holoscan Vision CMake consumer and runtime workflow pass, but direct CV-CUDA linking through default library paths fails. Linking through the bundled `holoscan/cvcuda` directory works. |
| 6940713 | core, inference, visualization | Full-suite testing on IGX Thor iGPU has reported display-surface and cross-process CUDA Tensor retirement/stress-test failures. Related Jetson reports also include Inference example failures that have not reproduced in targeted developer runs. The remaining failure scope and configuration dependencies are under investigation. |
| 6940969 | core | Interprocess pinned-host Tensor throughput can be substantially lower than reference measurements on some x86_64 RTX A6000 configurations, with high run-to-run variability. The reported throughput reduction remains under investigation. |
| 6962655 | core | Immediately rerunning an execution plan with newly created Channel clients may fail during startup with `RUNTIME_PORT_BINDING_UNAVAILABLE` and an underlying wake-service `kNotReady` error. Fully shut down the failed session and clients before retrying; no guaranteed workaround has been validated. |
| 6962658 | core | A failed active lifecycle restart that rolls back while downstream Channel input is pending may lose a sample, even though the run later completes with a lifecycle warning. Applications requiring lossless delivery should avoid active restart during data processing and should not assume rollback preserves all in-flight data. |
| 6962940 | core | External topic inputs created with `import_topic` currently use a 1 ms polling fallback in sleeping wait mode, which can add receive latency. As a workaround, configure the consumer's execution partition with `WakeMode::kBusyPoll` to poll continuously, at the cost of increased CPU usage. Event-driven wakeups for this input path are planned for a future release. |



---

# Holoscan SDK 5.0 — Installation prerequisites and tested platforms
Source: https://docs.nvidia.com/holoscan/sdk-user-guide/setup/sdk-installation — text extracted, fetched 2026-11-16 (prerequisites + tested-platforms sections only).

Prerequisites
Before you choose an installation method, check that your system meets the
Holoscan SDK 5.0 requirements:
Operating system: The packaged options use Ubuntu 24.04. You can run the
development container on another Linux host supported by the
NVIDIA Container Toolkit.
“Bare metal” host support is limited to the listed Ubuntu version.
Host Architectures: The SDK supports x86_64 and arm64. On arm64, the Debian
packages (architecture sbsa) and the container cover both arm64 servers
with discrete GPUs and NVIDIA Jetson and IGX systems running JetPack 7 or
IGX OS 2 and later.
GPU Architectures: Ampere or newer. See a complete list of tested platforms below.
GPU mode: Holoscan SDK 5.0 uses a single CUDA 13 software stack for
discrete and integrated GPUs. JetPack 6 and earlier are not supported; there is no separate iGPU container or
package.
CUDA: Holoscan SDK 5.0 requires CUDA 13. Use an NVIDIA driver compatible with CUDA 13
(R580 or newer) on the host machine. Container users also need Docker and the NVIDIA Container Toolkit.
Python: Use Python 3.12 or newer. Holoscan SDK wheels use the CPython 3.12
stable ABI and are intended for Python 3.12, 3.13, and 3.14.
CMake: Building C++ applications against an installed SDK requires
CMake 4.0 or newer. Ubuntu 24.04 ships CMake 3.28, so install a newer
version with sudo snap install cmake --classic, pipx install cmake,
or the Kitware APT repository
. The development
container already includes it.
Bare-metal package and wheel users must additionally provide the runtime dependencies
identified by their selected components.
Tested platforms
Holoscan SDK 5.0 is tested on the following platforms:
Platform | OS | GPU | 
x86_64 workstation (RTX 6000 Ada or RTX PRO 6000 Blackwell) | Ubuntu 24.04, R610 driver | dGPU | 
NVIDIA Jetson AGX Thor | JetPack 7.2.1 | iGPU | 
NVIDIA Jetson AGX Orin, Jetson Orin Nano | JetPack 7.2.1 | iGPU | 
NVIDIA IGX Thor 5000 | IGX OS 2.0 | iGPU | 
NVIDIA IGX Thor 7000 | IGX OS 2.0 | iGPU, or iGPU + dGPU | 
NVIDIA DGX Spark | DGX OS 7.6.0 | iGPU | 
NVIDIA Grace Hopper (GH200) | Ubuntu 24.04, R610 driver | dGPU | 
NVIDIA Grace Blackwell (GB200) | Ubuntu 24.04, R610 driver | dGPU | 
IGX Orin (IGX OS 1.x) and JetPack 6 are not supported.
For hardware-specific configuration, see
Additional Setup and
Third-Party Hardware Setup.
For RDMA, see
Enabling RDMA.
