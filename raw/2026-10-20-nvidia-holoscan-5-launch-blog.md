# NVIDIA Holoscan blog — Introducing Holoscan 5: The Transparent Runtime for Physical AI (2026-10-20)
Source: https://nvidia-holoscan.github.io/blog/2026-10-20-holoscan-5-launch/ — text extracted from <article>/<main>, fetched 2026-11-16.

Blog / Stories [../]

## Introducing Holoscan 5: The Transparent Runtime for Physical AI# [#introducing-holoscan-5-the-transparent-runtime-for-physical-ai]

Written October 20, 2026 by Jay Carlson

A robot, a satellite, and an MRI scanner look very different. Look at the computing, however, and the same pattern emerges: sense, think, act. Ultrasound systems, endoscopes, and scientific instruments also combine incoming data, computation, and control—each with its own timing requirements.

Holoscan 5 is NVIDIA’s platform for real-time sensor processing and control. It includes:

- Holoscan SDK (HSDK) provides the runtime and APIs for CPU and GPU sensor processing and control.

- Holoscan Sensor Bridge (HSB) connects sensors and acquisition electronics to accelerated computing through Ethernet using an NVIDIA-provided FPGA IP, with direct GPU data delivery and control paths back to devices.

- DAQIRI (Data Acquisition for Integrated Real-time Instruments) is a data-acquisition library for getting high-bandwidth network traffic into and out of CPU or GPU memory, focused on scientific and industrial instruments.

- Holoscan Modules provide reusable Camera, Vision, Inference, Visualization, and Multimedia operators.

- Holoscan Reference Designs provide hardware-and-software starting points for complete systems.

Developers and their agents can design the machine around its intelligence: explore sensing, algorithms, and control in simulation, then build the physical data and execution paths.

HSDK 5.0 is the biggest upgrade in Holoscan 5. Its rebuilt runtime brings the same API to ultra-low-latency, microsecond-scale control pipelines and high-bandwidth GPU sensor perception workloads. Partitions organize parallel processing chains and manage their thread and CUDA-stream coordination.

HSDK 5.0 is also the most agent-friendly release of HSDK yet. Strongly typed interfaces and graph compilation let developers and their agents validate pipeline designs before hardware testing.

The goal is a runtime transparent to the algorithm and inspectable to the engineer: low avoidable overhead, an inspectable execution plan, and observable behavior on hardware.

## One API for control and perception# [#one-api-for-control-and-perception]

Perception needs to move large volumes of data through GPU processing and inference. A control loop may compute for only a few microseconds, making scheduling, allocation, and thread handoffs significant parts of its response time. Some frameworks expose perception through message-driven callbacks and control through a separate controller API with its own update-loop semantics.

HSDK 5.0 uses the same operator lifecycle, typed ports, and graph-composition APIs for both. The workloads differ in timing and resources, not in how developers write them. Control and perception can run at different cadences within the same graph. Simple temporal contracts specify when an operator runs and which inputs it uses.

## Partitions make parallel pipelines natural# [#partitions-make-parallel-pipelines-natural]

The natural unit of concurrency is a processing chain—not every individual operator. A simple acquire → preprocess → infer pipeline can live in one partition. Add an independent read feedback → estimate state → update commands chain, and it naturally belongs in another, running at its own cadence.

There is no scheduler to choose. The compiler groups compatible linear chains, separates branches and joins, and records the layout in an execution plan. Inspect it with plan.partitions() or declare named partitions for explicit control.

- One stable CPU thread. Callbacks within a processing partition stay on that thread. Applications can request CPU affinity and scheduling policy.

- A runtime-owned CUDA stream per active GPU, by default. Operators submit work through ExecutionContext::cuda_stream(); HSDK handles Tensor readiness ordering. CPU-only partitions need no CUDA stream.

Cross-thread handoffs occur between partitions, not between successive stages within one. Eligible chains continue directly to the next ready operator; compiler-proven linear GPU chains sharing a stream omit redundant readiness events, waits, and release fences.

CUDA Graph fusion launches a GPU processing chain in one operation, reducing CPU dispatch and launch overhead. Eligible fixed-shape, linear regions are captured once and replayed.

Independent partitions can run concurrently where workload and hardware permit. Low overhead follows naturally: keep sequential work together and let HSDK coordinate parallel chains.

## What changes from HSDK 4.x# [#what-changes-from-hsdk-4x]

HSDK 5.0 retains the operator-based approach of HSDK 4.x [https://docs.nvidia.com/holoscan/archive/4.0.0/overview.html], but replaces its execution and configuration APIs.

HSDK 5.0 replaces GXF with a rebuilt runtime powered by HoloMQ that combines iceoryx2 shared-memory publish–subscribe with CUDA Virtual Memory Management (VMM) IPC. For supported GPU buffers on the same system, processes share the allocation instead of copying Tensor payloads through CPU memory. Developers get those benefits through HSDK’s graph and operator APIs.

Area | 
HSDK 4.x | 
HSDK 5.0 | 

Application structure | 
Application and Fragment composition | 
Simple graphs that can be used stand-alone or embedded into existing code and reused across applications. | 

Execution | 
Select and configure a scheduler | 
Compiler-planned partitions coordinate threads and streams, so parallel pipelines do not need a custom scheduler. | 

Timing | 
Conditions attached to operators, combined with queue and scheduler configuration | 
Timing declarations sit beside operator logic, making different-rate pipelines easier to read and reason about. | 

Connections | 
Ports declared in operator setup and connected through string names | 
Typed ports reject incompatible connections during code compilation, helping developers and agents wire pipelines correctly. | 

Configuration | 
Named Parameter<T> values, commonly supplied through YAML | 
Typed parameter schemas validate settings during code compilation, catching configuration mistakes early. | 

Memory | 
Operator-configured allocators and memory pools | 
Preallocated Tensor pools and bounded queues expose buffering requirements in the plan, so you can budget before running. | 

CUDA coordination | 
Operator-facing stream APIs and synchronization support | 
Partition-owned streams and automatic Tensor ordering remove manual stream plumbing while preserving data dependencies. | 

Components | 
Built-in operators and reusable libraries | 
Install only the modules you need for capture, processing, inference, display, or decoding—without pulling in every capability. | 

## Make execution transparent before and during the run# [#make-execution-transparent-before-and-during-the-run]

HSDK 5.0 separates graph construction, execution planning, and running:

- Compose. Connect operators through typed ports and reuse processing stages as embedded graphs.

- Compile. Call holoscan::compile(graph) to produce an immutable execution plan, with structured diagnostics for rejected configurations. This is graph planning, separate from compiling C++ source.

- Run. Execute the accepted plan with run(plan), or use run_async(plan) to control an asynchronous session.

The plan exposes partitioning and Tensor-pool decisions before devices start. During execution, NVTX annotations let Nsight Systems show operator compute ranges and correlated message activity.

## Typed interfaces and preallocated buffers# [#typed-interfaces-and-preallocated-buffers]

- Typed ports catch incompatible connections. C++ operators declare Input<T> and Output<T> members, so a Tensor output cannot silently become an integer input.

- Parameter schemas make configuration checkable. Typed aggregates carry defaults and versioned schemas define allowed values. Each activation reads one consistent parameter snapshot.

- Errors are values on the C++ hot path. Fallible operations return holoscan::expected<T, Error>, giving the operator an explicit outcome to handle rather than relying on exceptions for ordinary runtime failures.

allocate_tensor() borrows a slot from a pool prepared before execution; exhaustion returns ErrorCode::kResourceExhausted instead of expanding the pool. Queue depths can be explicit or compiler-derived where sufficient rate information is available.

QueuePolicy::kDropOldest with depth one keeps the freshest unread sample; larger depths retain a bounded backlog.

## Holoscan 5 connects the whole physical system# [#holoscan-5-connects-the-whole-physical-system]

The Holoscan 5 platform extends beyond HSDK 5.0 to acquisition, networking, and reference designs. Extreme co-design means engineering these components together across the sensor-to-action path.

## Ultrasound and endoscopy reference designs# [#ultrasound-and-endoscopy-reference-designs]

- Ultrasound: The Holoscan Ultrasound Reference Design [https://github.com/nvidia-holoscan/holoscan-ultrasound-imaging] connects TI acquisition electronics and HSB to GPU beamforming and reconstruction. Raw echoes flow in; CPU- or GPU-computed transmit settings shape the next shot, with the host scheduling transmission. It is an evaluation reference, not a clinically validated device.

- Endoscopy: The Holoscan Endoscopy Reference Design connects MIPI camera input through an FPGA capture card to GPU imaging and AI, then returns processed frames for camera-clocked display. Software controls exposure, frame geometry, and output timing. An FPGA image-processing path can provide a live-image fallback without host processing. The design is in NDA early access.

## DAQIRI for scientific instrumentation# [#daqiri-for-scientific-instrumentation]

DAQIRI [https://nvidia.github.io/daqiri/] provides the data-acquisition library for high-bandwidth instrument workflows. It moves network sensor data into and out of CPU or GPU memory, including GPUDirect paths, so researchers can analyze raw measurements as they arrive and build feedback into acquisition or experiment control.

## Start with reusable modules rather than infrastructure code# [#start-with-reusable-modules-rather-than-infrastructure-code]

Five independently installable Holoscan Modules provide 16 native operators for acquisition, image processing, model preparation, inference, compositing, and compressed-video input.

## Holoscan.Camera# [#holoscancamera]

- V4l2CaptureOp — capture packed YUYV frames from Linux V4L2 cameras into host, pinned-host, or CUDA device memory.

- SIPLCaptureOp — capture RAW10 or ISP-processed NV12 images from NvSIPL-managed cameras on supported Jetson and IGX configurations.

- ArgusCaptureOp — capture ISP-processed images through Jetson Argus on supported Orin configurations, with sensor and capture metadata.

## Holoscan.Vision# [#holoscanvision]

- BayerDemosaicOp — reconstruct RGB or RGBA from a Bayer mosaic.

- ResizeOp — resize images with selectable interpolation.

- CustomCropOp — extract a rectangular region.

- CopyMakeBorderOp — add borders or padding.

- RemapOp — transform an image using a coordinate map.

- NormalizeOp — normalize image values.

- ConvertToOp — convert element types with scaling and offset.

- ReformatOp — convert between interleaved and planar layouts.

- NonMaximumSuppressionOp — select detection candidates using score and overlap thresholds.

## Holoscan.Inference# [#holoscaninference]

- TensorPreprocessorOp — prepare fixed-shape, fixed-type inference inputs on the GPU: supported YUV-to-RGB conversion, resizing, normalization, and tensor-layout conversion.

- InferenceOp — execute one or multiple TensorRT models, with dispatch selected from the model configuration.

## Holoscan.Visualization# [#holoscanvisualization]

- HolovizOp — composite images, geometry, and text, then render to a window, a supported exclusive-display path, or CUDA-backed output for further processing.

## Holoscan.Multimedia# [#holoscanmultimedia]

- VideoDecoderOp — use NVDEC to decode H.264 or HEVC packets into GPU-resident images, retaining native NV12 or P010 surfaces.

## Give developers and their agents a faster iteration loop# [#give-developers-and-their-agents-a-faster-iteration-loop]

Typed ports and parameter schemas help agents construct correctly wired pipelines on the first attempt. The graph compiler checks the result without starting live acquisition.

The loop is compose → build → compile the graph → inspect diagnostics → revise. Structured diagnostics with stable identifiers give agents specific problems to fix, moving more iteration to a workstation or CI rather than a physical prototype.

Agents can generate C++ or Python operator tests that stage inputs and check outputs against the real runtime. HSDK 5.0 documentation, examples, and installation skills ground that work in current APIs. Hardware testing still establishes device integration, application behavior, latency, and jitter.

## Get started with Holoscan 5# [#get-started-with-holoscan-5]

Start with the HSDK documentation [https://docs.nvidia.com/holoscan/sdk-user-guide/], source and release notes [https://github.com/nvidia-holoscan/holoscan-sdk], and installation options [https://developer.nvidia.com/holoscan-downloads] today.

 All stories → [../]
