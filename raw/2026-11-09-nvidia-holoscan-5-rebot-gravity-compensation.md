# NVIDIA Technical Blog — Make a Robot Arm Feel Weightless with NVIDIA Holoscan 5 (2026-11-09)
Source: https://developer.nvidia.com/blog/make-a-robot-arm-feel-weightless-with-nvidia-holoscan-5/ — text extracted from <article>, fetched 2026-11-16. Share links removed; figures and videos not captured.

## Make a Robot Arm Feel Weightless with NVIDIA Holoscan 5

          Build a responsive gravity-compensation loop with Pinocchio, a Seeed Studio reBot arm, using  a simple Holoscan graph in Python or C++

            Nov 09, 2026

            By Jay Carlson [https://developer.nvidia.com/blog/author/jacarlson/] and Ansley Dunn [https://developer.nvidia.com/blog/author/ansleyd/]

## AI-Generated Summary

- NVIDIA Holoscan 5 [https://nvidia-holoscan.github.io/sdk/] enables low-latency robotic control and high-throughput perception in a single programming model with execution paths for CPU and GPU workloads.
- A gravity-compensation loop built from three custom Holoscan operators reads joint state at 400 Hz, computes inverse dynamics with Pinocchio [https://stack-of-tasks.github.io/pinocchio/], and sends torque commands to the Seeed Studio reBot Arm B601-DM [https://www.seeedstudio.com/reBot-Arm-B601-DM-p-6740.html] using the motorbridge library.
- Holoscan partitions group the operators on one thread to avoid cross-thread handoffs, and drop-oldest queues prevent outdated samples from accumulating.
- Nsight Systems profiling with built-in NVTX annotations shows pinning the control partition to a CPU core reduces p99.99 latency by roughly 5x for C++ and 9.6x for Python implementations.

## Next Steps
- Download the Holoscan 5 SDK [https://nvidia-holoscan.github.io/sdk/] to begin developing robotic control applications.
- Follow the gravity compensation tutorial [https://nvidia-holoscan.github.io/tutorials/rebot-gravity-compensation/] to build and run the complete example on supported hardware.

Powered by NVIDIA Nemotron. AI-generated content may summarize information incompletely. Verify important information. Learn more [https://www.nvidia.com/en-us/agreements/trustworthy-ai/terms/]

Picture guiding a robot arm by hand while its motors supply just enough torque to support its weight and keep the robot upright. This simple interaction, a useful starting point for robots that learn by demonstration, manipulate objects, or work alongside people, depends on a gravity-compensation loop.

Building such a loop is only possible by continuously calculating the inverse dynamics of the system based on precise models of all the links of the robot arm, their dimensions, masses, and moments of inertia. This calculation, which needs to be done rapidly with low jitter, requires knowing the current state of the robot, so gravity-comp demos are an excellent proof of life for both the robot model and the runtime that’s executing these algorithms.

NVIDIA Holoscan 5 [https://nvidia-holoscan.github.io/blog/2026-10-20-holoscan-5-launch/] introduced robotic control alongside streamlined sensor processing. In this tutorial, we’ll build custom Holoscan SDK operators and wire them into a graph. We’ll test the code on a real robot and use the Holoscan SDK’s built-in Nsight Systems annotations to inspect latency and jitter.

This walkthrough has been tested on Jetson Orin Nano, Jetson Thor, and x86 Ubuntu 24.04 systems.

## Why Holoscan? [#why_holoscan]

Video 1. A responsive robot with Holoscan installed for gravity compensation workload vs. a custom script runtime

Holoscan SDK brings low-latency control and high-throughput perception into one programming model, with execution paths designed for CPU- and GPU-based workloads. Its goal is a transparent runtime: minimize avoidable framework overhead while making application execution explicit and inspectable.

Keep the control path focused on the work. Holoscan uses partitions to group chains of operators on a single thread, avoiding cross-thread handoffs and unnecessary syscalls, reducing latency and jitter. Clock and data-arrival triggers express when work should run, while bounded, drop-oldest queues prevent outdated work from accumulating.

Bring existing algorithms and code rather than rewriting them for a framework. Holoscan 5 has a new, lightweight programming model that can be easily integrated into existing code bases, and it’s never been easier to get data into and out of Holoscan graphs.

Add perception without adopting a different programming model. Whether you’re handling 10 kHz CPU-centric motor control loops, heavy-throughput GPU algorithms, or AI inference, Holoscan lets developers and their agents clearly express execution intent using the same operators, ports, and graph APIs, logically splitting their workloads into separate graphs that can coexist, with the ability to pin partitions to dedicated CPU cores, CUDA green contexts, or even execute as a CUDA graph.

Inspect the plan, then measure the result. Operators express their intent with timing contracts, and before the first run, the compiled plan exposes how the application will execute and catches configuration errors before deployment. This means agents and developers can quickly iterate on a design without ever deploying to real hardware. Plus, built-in NVTX annotations make operator execution and message transfers visible in Nsight Systems. Developers can examine host control-path latency and update jitter, then repeat those measurements as the application grows.

## An accessible platform for torque-control development [#an_accessible_platform_for_torque-control_development]

This tutorial is built around the Seeed Studio reBot Arm B601-DM [https://www.seeedstudio.com/reBot-Arm-B601-DM-p-6740.html], which is an accessible, affordable platform for getting started with modern robotics control. Most low-cost robot arm development platforms use highly-geared hobby servos, which are only suitable for positional control. The reBot Arm uses quasi-direct-drive (QDD) actuators that provide high torque bandwidth for both control and sensing — important for haptic, co-bot, or other torque-oriented projects like this one.

## Starting off with gravity-comp [#starting_off_with_gravity-comp]

Before adding perception pipelines, motion planners, and other higher-level controls, building a basic gravity compensation loop helps provide a useful (and entertaining!) sanity-check for whether your simulation model accurately describes the physical robot. While position-control examples can mask problems with joint axes, offsets, link placements, masses, and moments, all of these affect the required torque in instantly-observable ways; any bugs in DH parameters or mass properties can make the arm sag or push upward as its pose changes.

Even if your end application doesn’t need gravity-comp, torque control lets us shape how the robot responds to forces—a key ingredient in safer interaction between humans and co-bots. Our arm combines gravity feedforward with light stiffness and damping, so it supports its weight while yielding to a person’s hand.

That flexibility makes timing critical. Tracking a position through torque commands requires rapid, consistent feedback at hundreds or thousands of Hz, and runtime overhead and thread handoffs can add phase lag and jitter that cause the robot to become unstable.

This tutorial uses Pinocchio [https://stack-of-tasks.github.io/pinocchio/] as the inverse-dynamics solver. It loads the robot’s URDF model and provides a Recursive Newton–Euler Algorithm (RNEA) solver, which calculates joint torques for specified positions, velocities, and accelerations. We also use the motorbridge [https://motorbridge.seeedstudio.com/] library to read joint feedback and send commands to the arm’s motors.

## Set up the Python example [#set_up_the_python_example]

This walkthrough uses Holoscan’s Python API. The tutorial repository also contains a complete C++ implementation [http://apps/gravity_compensation.cpp], with its own build instructions [http://docs/cpp-version.md]. Both implement the same three-operator control loop.

Use Python 3.12 or newer on Linux. From the repository root:

python3.12 -m venv build/python-venv
build/python-venv/bin/python -m pip install --only-binary=:all: -r requirements-python.txt
build/python-venv/bin/python -m pip check

Check the serial device and motor IDs in the arm’s configuration file. The tutorial repository’s technical guide covers configuration, the math, and hardware startup.

## Express the control loop as three operators [#express_the_control_loop_as_three_operators]

Holoscan 5 has two programming concepts: Operators and Graphs. To read the robot’s state, calculate the command using the inverse-dynamics solver, and send it to the arm, we can decompose that problem into three operators wired into a graph:

Figure 1. Closed loop control system diagram

Operators are subclassed from Operator and have three important methods to implement:

MethodPurpose
setup()Declare input and output ports.
contract()Declare when to run and which input data to use.
compute()Read input(s), do work, and publish output(s).

Table 1. Core methods to implement for custom Holoscan operators

Here are outlines of the three operators to build:

## 1. Read joint state on a clock [#1_read_joint_state_on_a_clock]

JointStateSourceOp declares one output in setup(). Its OnClock contract requests a tick every 2.5 ms (we’re running this demo at 400 Hz). Each compute() reads all seven motors and emits their state:

import holoscan as hsdk

class JointStateSourceOp(hsdk.Operator):
    state = hsdk.Output("state", hsdk.pyobject)

    def setup(self, spec):
        spec.output(self.state)

    def contract(self):
        return hsdk.Contract().trigger(hsdk.OnClock(period=hsdk.time.us(2500)))

    def start(self):
        self.sequence = 0

    def compute(self, ctx):
        self.sequence += 1
        self.state.emit(robot.read_state(self.sequence))

## 2. Compute gravity compensation when state arrives [#2_compute_gravity_compensation_when_state_arrives]

PinocchioGravityOp declares a state input and command output. OnEach runs it when state arrives. The hsdk.Param declarations expose gains, torque scaling, and joint direction as operator parameters:

class PinocchioGravityOp(hsdk.Operator):
    state = hsdk.Input("state", hsdk.pyobject)
    command = hsdk.Output("command", hsdk.pyobject)
    kp = hsdk.Param(1.5, range=(0.0, 500.0))
    kd = hsdk.Param(1.0, range=(0.0, 5.0))
    tau_scale = hsdk.Param([1.0] * 6)
    joint_direction = hsdk.Param([1.0] * 6)

    def setup(self, spec):
        spec.input(self.state, queue_depth=1)
        spec.output(self.command)

    def contract(self):
        return hsdk.Contract().trigger(hsdk.OnEach(self.state))

    def compute(self, ctx):
        state = self.state.receive_data()
        command = controller.compute(
            state, kp=self.kp, kd=self.kd,
            tau_scale=self.tau_scale, joint_direction=self.joint_direction)
        self.command.emit(command)

compute() passes the observed state and current parameters to a helper that maps the six arm angles into the URDF model, checks limits, and obtains gravity torques through Pinocchio:

gravity = pin.computeGeneralizedGravity(self.model, self.data, self.q)[self.v_indices]

Its torques become feedforward in the motors’ commands, alongside position, velocity, stiffness, and damping. The arm uses gravity feedforward and the configured compliant gains from the first command.

## 3. Send each command to the motors [#3_send_each_command_to_the_motors]

MotorCommandSinkOp declares one input and runs whenever a command arrives. compute() hands the command to a small robot helper, which rejects expired, out-of-order, or out-of-range commands before sending the batch:

class MotorCommandSinkOp(hsdk.Operator):
    command = hsdk.Input("command", hsdk.pyobject)

    def setup(self, spec):
        spec.input(self.command, queue_depth=1)

    def contract(self):
        return hsdk.Contract().trigger(hsdk.OnEach(self.command))

    def compute(self, ctx):
        robot.send_command(self.command.receive_data())

    def stop(self):
        robot.disable()

After sending all seven motor commands, the helper records the completion time. If no batch completes for 100 ms (the default timeout), the application’s watchdog attempts to disable the motors and stops the graph. The operator’s stop() callback also disables the motors.

## Wire, compile, prepare, and run [#wire_compile_prepare_and_run]

The application connects the operators through their ports and supplies the gravity parameters when creating the operator:

graph = hsdk.Graph("rebot-gravity", default_clock=hsdk.RealtimeClock)
source = graph.op(JointStateSourceOp, "joint_feedback")
gravity = graph.op(PinocchioGravityOp, "gravity", **controller.parameters.operator_kwargs())
sink = graph.op(MotorCommandSinkOp, "motor_commands")
graph.add_flow(source.state, gravity.state, queue_depth=1, queue_policy=hsdk.QueuePolicy.DROP_OLDEST)
graph.add_flow(gravity.command, sink.command, queue_depth=1, queue_policy=hsdk.QueuePolicy.DROP_OLDEST)
graph.partition("control").add(source).add(gravity).add(sink)

A partition groups operators whose callbacks execute serially on one runtime-owned thread. Keeping all three in control avoids thread handoffs between reading state, calculating torque, and sending commands. The source sets the pace; the other operators follow the data. Depth-one, drop-oldest queues keep old samples from piling up.

Holoscan compiles this description into an inspectable execution plan before we enable the motors:

plan = hsdk.compile(build_graph(robot, controller))
if not plan:
    raise RuntimeError(plan.summary())

prepare_gravity_compensation(robot, controller)
hsdk.run_async(plan)

Model and motor initialization live in prepare_gravity_compensation() [http://python/rebot_gravity.py], after graph compilation and immediately before execution. The application’s signal handlers set stop_requested on Ctrl+C; the main loop supervises command progress, and the session context manager stops and joins the graph. The control policies [http://docs/control-policies.md] cover startup, watchdogs, and shutdown.

## See the arm respond [#see_the_arm_respond]

Start with the arm in its power-off-safe home position:

build/python-venv/bin/python python/gravity_compensation.py

When Gravity compensation active appears, guide the arm by hand. Return it home manually before pressing Ctrl+C, which disables the motors.

Video 2. The controller updates while the joint torques as the pose changes

## Measure latency and jitter with Nsight Systems [#measure_latency_and_jitter_with_nsight_systems]

Holoscan has seamless integration with NVIDIA Nsight Systems, giving you powerful tools for analyzing real-world system behavior for both GPU- and CPU-based workloads.  NVIDIA Nsight Systems [https://docs.nvidia.com/nsight-systems/UserGuide/index.html]. No tracing decorators or custom timing code are needed, simply profile the unmodified application:

mkdir -p build/profiles
nsys profile -t nvtx --sample=none --backtrace=none --cpuctxsw=none \
-o build/profiles/gravity-python \
build/python-venv/bin/python python/gravity_compensation.py

Open the timeline:

Figure 2. NVIDIA Nsight Systems (nsys) timeline and NVTX event trace showing task timing and latency across operators

You can also calculate a standard range summary:

nsys stats --report nvtx_sum build/profiles/gravity-python.nsys-rep

## Pinning cores [#pinning_cores]

Holoscan’s deployment API lets us pin the control partition to a CPU. For these runs, we put helper and profiler threads on another CPU, then used a temporary Linux cgroup to reserve both physical cores, including their SMT siblings, from other applications. This is a simple setup that needs no kernel rebuild, boot-parameter changes, or reboot, but interrupts, timers, and some kernel threads can still run on those cores.

We compared all four configurations, retaining more than one million cycles per run. Holoscan latency runs from entry into the first operator to entry into the last, excluding motor-command transmission. Solid curves show pinned runs; dotted curves show unpinned runs.

Implementationp50 (µs)p99.99 (µs)p99.999 (µs)
HSDK C++ pinned7.117.220.7
HSDK C++ unpinned15.386.6133.4
HSDK Python pinned93.0142.61,014.0
HSDK Python unpinned113.81,373.53,134.1

Table 2. Measured latency distributions for C++ and Python Holoscan pipelines in pinned vs. unpinned configurations.

Pinning plus isolation reduced the observed p99.99 latency by roughly 5× for C++ and 9.6× for Python. These sequential, profiled runs exclude the first ten seconds and retain latency outliers.

Both Holoscan versions call Pinocchio’s C++-based solver, but Python adds interpreter execution, object allocation, and GIL coordination around both Pinocchio and the Holoscan runtime. Those costs matter for CPU control loops with microsecond latency budgets. C++ gives us more control over allocations and system calls in the critical path (although this example still allocates memory and is not a zero-syscall pipeline).

For GPU-based perception workloads taking milliseconds or tens of milliseconds—orders of magnitude longer—optimizing small allocations and incidental system calls on the CPU is usually less consequential. Python remains a practical way to compose these pipelines (provided that the pipeline elements are implemented in CUDA).

## From gravity compensation to a full control stack  [#from_gravity_compensation_to_a_full_control_stack_]

You now have a working gravity-compensation loop built from three Holoscan operators: one reads joint state on a clock, one computes gravity torque with Pinocchio, and one sends commands to the motors. Holoscan compiled and checked the graph before the motors were enabled, and Nsight Systems showed how it ran.

Gravity compensation is the foundation rather than the finished controller. The tutorial repository includes a second Python example that adds kinematics and impedance control as reusable Holoscan operators. It lets you inject a goal position and orientation, for example from a learned policy, while the arm stays compliant to the touch.

Video 3. Real-time Cartesian position hold, maintaining target orientation while remaining haptically compliant

From there, you can build toward hand-guided teaching, teleoperation, and manipulation. To add perception, use Holoscan’s vision module, along with components from NVIDIA Isaac ROS, which provides reusable Holoscan operators and reference applications such as GR00T inference.

## Next steps [#next_steps]

Download the Holoscan 5 SDK [https://nvidia-holoscan.github.io/sdk/] and follow the full tutorial here [https://nvidia-holoscan.github.io/tutorials/rebot-gravity-compensation/].

## Tags

             Developer Tools & Techniques [https://developer.nvidia.com/blog/category/development/] | Edge Computing [https://developer.nvidia.com/blog/category/edge-computing/] | Robotics [https://developer.nvidia.com/blog/category/robotics/] | Healthcare & Life Sciences [https://developer.nvidia.com/blog/recent-posts/?industry=Healthcare+%26amp%3B+Life+Sciences] | CUDA [https://developer.nvidia.com/blog/recent-posts/?products=CUDA] | GR00T [https://developer.nvidia.com/blog/recent-posts/?products=GR00T] | Holoscan [https://developer.nvidia.com/blog/recent-posts/?products=Holoscan] | Isaac ROS [https://developer.nvidia.com/blog/recent-posts/?products=Isaac+ROS] | Jetson Orin [https://developer.nvidia.com/blog/recent-posts/?products=Jetson+Orin] | Intermediate Technical [https://developer.nvidia.com/blog/recent-posts/?learning_levels=Intermediate+Technical] | Tutorial [https://developer.nvidia.com/blog/recent-posts/?content_types=Tutorial] | AI Agent [https://developer.nvidia.com/blog/tag/ai-agent/] | Clara [https://developer.nvidia.com/blog/tag/clara/] | Medical Devices [https://developer.nvidia.com/blog/tag/medical-devices/] | MONAI [https://developer.nvidia.com/blog/tag/monai/] | Video Analytics [https://developer.nvidia.com/blog/tag/tracking-video-analytics/]

##
                About the Authors

                  About Jay Carlson

                          Jay Carlson is a senior product manager at NVIDIA, where he works on Holoscan, NVIDIA's platform for real-time sensor processing at the edge. His background is in robotics, embedded systems, and medical devices.

                                            View all posts by Jay Carlson

                                     [https://developer.nvidia.com/blog/author/jacarlson/]

                  About Ansley Dunn

                          Ansley Dunn is product marketing manager for NVIDIA Holoscan, where she oversees go-to-market activations for Holoscan, a real-time edge AI platform. Prior to NVIDIA, Ansley led product marketing for Intel’s flagship edge AI platform, OpenVINO at Intel Corp and has worked on both agency and client side, creating global campaigns and demand-gen efforts for leading tech companies like LG, Intuit, Broadcom, and Sage to name a few. Ansley had a passion for higher education and served as adjunct faculty teaching digital marketing at NYU.

                                            View all posts by Ansley Dunn

                                     [https://developer.nvidia.com/blog/author/ansleyd/]
