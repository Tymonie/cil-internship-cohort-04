#Solution to Task 1
Layered Operating system 

The operating system is divided into a number of levels. Each layer has a separate set of features in the layered operating system. As an advance over the initial monolithic systems, this kind of operating system was developed.
In an operating system, layering offers a clear benefit. Each layer may be designed independently and may interact with the others as necessary. Additionally, structuring the system into layers makes it simpler to develop, maintain, and upgrade. Changes to one layer's specification have no impact on the other layers.Each of the layers in the operating system can only interact with the layers that are above and below it. The lowest layer handles the hardware and the uppermost layer deals with the user applications

Layer 6: USER PROGRAMS
In the layered operating system, this layer is the topmost. Word processors, games, browsers, and other user programs and applications that are active within an operating system are handled by this layer. Given that it is focused on application programs, you may alternatively refer to this as an application layer.

Layer 5: INPUT/OUTPUT BUFFER
I/O hardware plays a crucial role in computer systems. They provide consumers ways to communicate with the system. The I/O device buffers are managed by this layer, which also ensures their proper operation.
Let's say you are using a keyboard to type. The keyboard has a connected keyboard buffer, which temporarily stores data. In a similar vein, every input/output device has a buffer connected to it. This is due to the processing and storage speeds of the input/output devices. Buffers are used by the computer to maintain the input/output devices' and the processor's excellent timing speed.

Layer 4: PROCESS MANAGEMENT
This layer is in charge of controlling the processes, which includes choosing how many processes will remain in the waiting schedule and allocating the processor to each process. In this layer, the processes' priorities are also handled. First-come, first-served (FCFS), SJF (shortest job first), priority scheduling, round-robin scheduling, and others are some of the numerous methods used for process scheduling.

Layer 3: MEMORY MANAGEMENT
Memory management is concerned with managing memory and transferring programs from disk to main memory for execution and back. The operating system's third layer is in charge of handling this. This layer encompasses all memory management. The computer has several different types of memory, such as RAM and ROM.
When RAM is taken into account, swapping in and out of memory is a worry. Some operations that our computer does go to the main memory (RAM) for execution, and when applications, like the calculator, quit, they are also removed from the main memory.

Layer 2: CPU SCHEDULING
The CPU task scheduling is handled by this layer. To manage operations, many scheduling queues are employed. The processes are added to the work queue as soon as they enter the system.
The ready queue is used to store processes that are prepared to run in main memory. This layer is in charge of controlling how many processes will be assigned to the CPU and which ones will not.

Layer 1: HARDWARE
This layer coordinates with all peripheral devices utilized, including a printer, mouse, keyboard, scanner, etc., and interfaces with the system hardware. The hardware layer controls these kinds of physical devices.
In the layered operating system architecture, the hardware layer is the lowest and most powerful layer. It is directly connected to the system's brain.
