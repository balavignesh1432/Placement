# Operating System Study Guide

---

## 1. Introduction to Operating Systems

### 1.1 Definition

**Operating System** provides an interface between the user and the computer hardware.

**Key Functions:**
- Provides Access Control to users
- Security to data and files

---

## 2. Types of Operating Systems

### 2.1 Time-Sharing Operating System
- Share resources among multiple processes
- Small slice of CPU time (Quantum)

### 2.2 Distributed Operating System
- Collection of independent computers
- Appear to the user as a single coherent system

### 2.3 Real-Time Operating System
- Processing needed to be executed within a short time

### 2.4 Batch Operating System
- Executes a batch of jobs automatically without user interaction

---

## 3. Kernel Architecture

### 3.1 What is a Kernel?

A **kernel** is the central component of an operating system that manages the operations of computers and hardware. The kernel provides an interface between the application and hardware.

**Main Purpose:**
- Memory management
- Disk management
- Process management
- Task management

### 3.2 Types of Kernels

#### Monolithic Kernel
- It is larger in size
- Entire OS runs in kernel space
- It uses signals and sockets to achieve inter-process communication
- **Example:** Linux

#### Microkernel
- Minimal kernel, smaller in size
- Most services run in user space
- It uses message queues to achieve inter-process communication

#### Hybrid Kernel
- **Example:** Windows, MacOS

### 3.3 Kernel Space vs User Space

#### Kernel Space
The OS kernel runs with full privileges:
- Direct access to hardware
- Can access all memory

**Examples:** System Calls, Device Drivers, Memory Manager, Process Schedulers

#### User Space
User applications run with limited privileges:
- Cannot directly access hardware, kernel memory
- Indirect via system call (Switches to Kernel Mode)

**Examples:** Browsers

#### Purpose of Separation
- **Security:** User code cannot damage the OS
- **Stability:** Faulty program does not crash system

---

## 4. System Startup (Bootstrapping)

**Bootstrapping** is the process of starting up and loading the operating system into memory.

**Process:**
1. BIOS/firmware runs first: Power-On Self Test (POST)
2. Bootloader/Bootstrap is loaded into memory
3. It loads the Kernel and initializes OS
4. OS takes control

---

## 5. Process Management

### 5.1 Program vs Process

- **Program** is a passive entity as it resides in the secondary memory.
- A **process** is an instance of a program in execution.

### 5.2 Process Control Block (PCB)

**Process Table** contains: Process id, State, Program Counter, Registers

**Program Counter:** A register that holds the address of the next instruction to be executed.

**Process Control Block** is one entry in Process Table.

### 5.3 Process States

- **New:** Process is being created
- **Ready:** Process is waiting to be assigned to a processor
- **Running:** Instructions are being executed
- **Blocked:** Process is waiting for some event to occur
- **Terminated:** Process has finished execution

### 5.4 Context Switching

**Context Switch:** Switching of CPU to another process

- **Scheduler** decides which process should run
- **Dispatcher** actually runs it

**Dispatcher:** Gives control of the CPU to the process selected by the scheduler.
- Runs in kernel mode

**Dispatcher performs context switch:**
1. Saves current process state
2. Loads next process state
3. Switches CPU to user mode
4. Jumps to the correct instruction using program counter of new process

**Invoked:**
- After an interrupt
- After system call
- When time slice expires

**Dispatch latency** = time taken to stop one process and start another

**Includes:** Context switch time and Mode switch

**Note:** Context switch does not require hardware support (for user-level threads)


## System Calls

A **system call** is a controlled entry point through which a user-level program requests a service from the operating system kernel.

#### `fork()`
- Creates a **new process** by duplicating the calling process
- Child gets a **new PID**
- Both parent and child continue execution from the next instruction

#### `exec()`
- Replaces the **current process image** with a new program
- **does not create a new process**, it replaces the program.
- PID remains the same
- Code, data, heap, stack are replaced

#### `wait()`
- Parent process waits for child to terminate
- Collects exit status

### 5.5 Special Process Types

#### Zombie Process (Defunct Process)
A process that has finished execution but still has an entry in the process table.

**Process Flow:** Parent Process → fork() → Child Process

- The OS keeps a PCB entry for the child so the parent can read its exit status via wait()
- Until the parent calls wait(), the child remains a zombie
- It occupies no resources, Still occupies a PCB entry

**Problem:** If parent never calls wait() then PCB entries accumulate, Process table fills up.

#### Orphan Process
A process whose parent has terminated before it, leaving it without a parent.

- These are adopted by init process (PID = 1)
- Every process has a parent process

#### Cascading Termination
When a parent process terminates, all of its child processes are also terminated automatically. Some OS (not Linux) allow cascading termination to prevent orphan processes.

### 5.6 Process Communication

- **Process communicates** through Inter-Process Communication (IPC) — slower
- **Threads communicate** through shared memory — faster

---

## 6. Thread Management

### 6.1 What is a Thread?

A **thread** is a single sequence stream within a process. Because threads have some of the properties of processes, they are sometimes called lightweight processes.

**Example:** In a browser, multiple tabs can be different threads.

### 6.2 Thread Components

Each thread has its own:
- Program counter
- Registers
- Stack
- Thread ID (Thread Control Block)

But shares with other threads of the same process:
- Text (Code)
- Data (Global and Static Variables)
- Heap (Dynamically allocated Memory)
- Files

**Memory Layout:**
- **Stack:** Function Calls, Return Addresses, Local Variables
- **Heap:** Dynamically allocated Memory
- **Text:** Code
- **Data:** Global and Static Variables

### 6.3 Types of Threads

#### Kernel-Level Threads
- Implemented by OS
- Independent threads: If one kernel thread performs a blocking operation then others can continue execution
- Context switch requires hardware support

#### User-Level Threads
- Implemented by User
- Dependent threads: If one user-level thread performs a blocking operation then entire process will be blocked
- Context switch does not require hardware support

---

## 7. CPU Scheduling

### 7.1 Multiprogramming Concepts

#### Multitasking
- It is a system that allows more efficient use of computer hardware
- This system works on more than one task at one time by rapidly switching between various tasks
- These systems are also known as time-sharing systems
- **(Single CPU)**

#### Multiprocessing
- It is a system that allows multiple or various processors in a computer to process two or more different portions of the same program simultaneously
- It is used to complete more work in a shorter period of time
- **(Multiple CPU)**

#### Multiprogramming
- One processor multiple programs
- Time-sharing is a logical extension of multiprogramming
- The CPU performs many tasks by switches that are so frequent that the user can interact with each program while it is running
- Allows multiple users to share computers simultaneously

### 7.2 Types of Multiprocessing

#### Symmetric Multiprocessing (SMP)
- Multiple identical processors treated equally by OS
- Processors share the same main memory and I/O system
- If one processor fails, others can continue

#### Asymmetric Multiprocessing (Master-Slave)
- **Master processor:** Handles OS tasks, scheduling, and I/O operations
- **Slave processors:** Execute only the tasks assigned by the master
- **Problem:** Single point of Failure

### 7.3 Scheduling Algorithms

1. **First-Come, First-Served (FCFS) Scheduling** (Non-Preemptive)
2. **Shortest-Job-Next (SJN) Scheduling**
3. **Shortest Remaining Time First (SRTF)** (Preemptive)
4. **Priority Scheduling**
5. **Round Robin (RR) Scheduling** (Time Slicing - Quantum)

## Scheduling Metrics

- Turnaround Time = Completion Time − Arrival Time
- Waiting Time = Turnaround Time − CPU Burst Time
- Response Time = First CPU Allocation − Arrival Time

### 7.4 Scheduling Issues

#### Starvation
Process does not get the resources it needs for a long time because the resources are being allocated to other processes. It's also called indefinite blocking.

- Occurs in Priority Based Scheduling   

#### Aging
Technique to avoid starvation. Increase the priority of the request as time passes.

- Round Robin prevents starvation

---

## 8. Memory Management

### 8.1 Address Spaces

#### Logical Address
- Generated by the CPU
- Visible to users

#### Physical Address
- A location in a memory unit
- Computed by MMU (Memory Management Unit)
- Invisible to users
- Physical addresses mapped to the corresponding logical addresses

### 8.2 Memory Loading Techniques

#### Dynamic Loading
- A program loads code into memory only when it is needed, not at program start
- Saves Memory
- Improves Startup Times
- **(OS-managed)**

#### Overlays
- A program is larger than the available main memory, so only the required part of the program is kept in memory at a time
- **(Programmer-managed)**
- **(No Page Faults)**

**Process:**
- Program is divided into modules (overlays)
- Only ONE overlay (or a few) is loaded into a fixed memory region
- When another part is needed, the current overlay is replaced

### 8.3 Virtual Memory

The idea of virtual memory is to use disk space to extend the RAM.

**Demand Paging:** The process of loading the page into memory on demand (whenever a page fault occurs) is known as demand paging.

**Page Table:** Keeps track of which pages are in memory and which are on disk.

#### Thrashing
Thrashing occurs when a system spends more time processing page faults than executing transactions. While processing page faults is necessary in order to appreciate the benefits of virtual memory, thrashing has a negative effect on the system.

### 8.4 Paging (Fixed Partitioning)

Paging is a memory management technique where secondary memory is divided into pages and main memory into frames. Pages are loaded into available frames in main memory. Logical address is split into page number and page offset.

- OS maintains a list of free frames

#### Page Replacement
When a page fault occurs and no free frame is available

**Types:** FIFO, LRU, LFU, Round Robin

#### Belady's Anomaly
Occurs when increasing the number of page frames causes an increase in the number of page faults. **(FIFO)**

#### Inverted Page Table
- One entry per physical frame
- One table for the entire system
- (VPN, PID) is key which is hashed into buckets of frame count
- Value is the physical frame number

### 8.5 Segmentation (Variable Size Partitioning)

Program is divided into variable-size sections, by the user. Logical address is split into section number and section offset. Matches programmer's view of memory.

**Examples:** Text, Data, Stack, Heap

### 8.6 Non-Contiguous Memory Allocation

Random Access in Memory (No sequential order). Both Frames and Segments.

### 8.7 Fragmentation

**Fragmentation:** Available memory exists, but it is not usable, leading to wasted space.

#### Internal Fragmentation
- Unused space inside an allocated block
- Occurs in **Paging** - When Page size is smaller (last page)

**Reduction:** Use smaller block sizes

#### External Fragmentation
- Free memory (Holes) exists but is scattered
- No single contiguous block is large enough
- Occurs in **Segmentation**
- OS keeps a list of free memory blocks (holes)

**When a new segment is created:**
- **First fit:** place in first hole big enough
- **Best fit:** smallest hole that fits
- **Worst fit:** largest hole

**Reduction:** Compaction (shift processes to combine free space)

### 8.8 Locality of Reference

**Locality of reference** is the tendency of a program to access a relatively small set of memory locations repeatedly over a short period of time. Explains why caches, paging, and virtual memory work efficiently.

#### Temporal Locality
Recently accessed memory locations are likely to be accessed again soon

#### Spatial Locality
Memory locations near recently accessed locations are likely to be accessed soon

### 8.9 Swapping

**(RAM is limited)**

- **Swap Out:** Move process from RAM → Disk
- **Swap In:** Move process from Disk → RAM

---

## 9. Storage Management (RAID)

### 9.1 Introduction to RAID

**RAID** combines multiple physical disks into one logical unit to improve performance, reliability, or both. Instead of trusting one disk, RAID: splits data, duplicates data, or adds parity data across multiple disks.

**Benefits:**
- **Redundancy** → protects against disk failure
- **Performance** → faster reads/writes
- **Capacity** → combine multiple disks

### 9.2 RAID Levels (0 - 6)

#### RAID 0 — Striping (Only Data split across disks)
- **Fastest** But **No fault tolerance**

**Example:**
- Disk1: A1 A2
- Disk2: A3 A4

#### RAID 1 - Mirroring
- **High reliability** But **50% storage efficiency**

**Example:**
- Disk1: A1 A2
- Disk2: A1 A2

#### RAID 2 - Bit Level Striping + Parity (Hamming Code)
- **Bit-level striping:** Data is split at the bit level across multiple disks
- **Hamming code parity:** Uses Hamming codes for error detection and correction (correct single-bit errors)

#### RAID 3 - Byte Level Striping + Parity (XOR)
- **Byte-level striping:** Data is split at the byte level across disks. **Sequential Access**
- **Dedicated parity disk:** One disk stores parity (Can survive 1 disk failure)
- If any disk fails, parity + remaining disks → reconstruct missing data

**Write usually requires: (Write penalty)**
1. Compute new parity
2. Write new data
3. Write new parity

#### RAID 4: Block Level Striping + Parity (XOR)
- Data is split into blocks (Block Size: 4 Bytes) across multiple disks. **Random Access**
- **Dedicated parity disk:** One disk stores parity for all data blocks. (Can survive 1 disk failure)
- **Parity disk is a bottleneck for writes** (all writes must update parity disk: Hotspot/Bottleneck)

**Example:**
- Disk 1: D1   D4   D7
- Disk 2: D2   D5   D8
- Disk 3: P1   P2   P3

#### RAID 5 — Block Level Striping + Distributed Parity (XOR)
- Parity blocks spread across all disks
- **Better Write Performance** (Survives 1 disk failure)

#### RAID 6 — Block Level Striping + Double Distributed Parity (XOR)
- Two independent parity blocks per stripe
- Parity is distributed across disks
- **Survives 2 disk failures** But **Slower writes** (Extra Parity)

---

## 10. I/O Management

### 10.1 Direct Memory Access (DMA)

**Direct memory access (DMA)** is a method that allows an input/output (I/O) device to send or receive data directly to or from the main memory, bypassing the CPU to speed up memory operations. The process is managed by a chip known as a DMA controller.

- DMA controller requests bus access and CPU temporarily releases the bus
- High-speed I/O operations

### 10.2 Cycle Stealing

An I/O device temporarily takes control of the CPU (or memory bus) cycles to directly transfer data to/from main memory, suspending the CPU for those cycles. CPU and I/O device share the system bus.

### 10.3 CPU Clock Cycle

**CPU (Clock) Cycle:** The smallest unit of time in which a CPU performs one basic operation.

**Duration** = 1 / clock frequency (GHz)

### 10.4 Spooling

**Spooling:** Simultaneous Peripheral Operations On-Line

- I/O data/jobs is temporarily stored on disk and processed later by a peripheral device
- CPU does not wait for I/O. As these devices are slower

### 10.5 Buffering

**Buffering:** Suitable for fast I/O, Uses main memory, small data chunks

### 10.6 Interrupts

An **interrupt** is a signal sent to CPU: Temporarily stops the current CPU execution so the OS can handle an important event. One of the bus control lines is dedicated to this purpose and is called the Interrupt Service Routine (ISR).

**Purpose:**
- Handle errors
- Handle I/O completion

**Working:**
1. Saves current context (PC, registers)
2. Switches to kernel mode
3. OS runs Interrupt Service Routine (ISR)
4. CPU restores context

#### Types of Interrupts

**Hardware Interrupts:** Hardware devices generated (EX: I/O)

**Software Interrupts:** Generated by programs (Exceptions (Divide by 0), System Calls)

**Trap:** A trap is a software interrupt, usually the result of an error condition, and is also a non-maskable interrupt and has the highest priority.

**Trapdoor:** A trapdoor is a secret undocumented entry point into a program used to grant access without authentication.

### 10.7 Disk Access Time

**Seek Time:** This is the time it takes for the disk's read/write head to move to the correct track (cylinder) where the data is stored. You first need the head positioned on the correct track.

**Rotational Latency:** Once the head is over the right track, wait for the disk to rotate so that the desired sector is under the head. This is the rotational delay.

---

## 11. Inter-Process Communication (IPC)

**Inter Process Communication:** mechanism that allows processes to communicate with each other.

### 11.1 Pipes

**(buffer in kernel memory):** Unidirectional data stream.

- One process writes data into the pipe
- Another process reads data from the pipe
- Data flows sequentially

**Types:**
- **Unnamed Pipes** (Parent - Child)
- **Named Pipes** (Different Processes)

### 11.2 Message Queuing

Messages through a queue managed by the OS.

- Messages are stored in a queue, Queue exists in kernel space
- Sender and receiver are decoupled
- Sender puts a message into the queue
- Receiver reads messages in order (FIFO, usually)
- Messages are coordinated using an API

### 11.3 Sockets

A **socket** is an endpoint for communication between processes (IPC).

- Endpoint is referred to as a combination of an IP address and port number
- Sockets provide a bidirectional communication channel
- Can be used for IPC: On same machine and Across Machines
- Data is sent as streams (TCP) or datagrams (UDP)

### 11.4 Shared Memory

Interchange of data through a defined area of memory. Semaphore values have to be obtained before data can get access to shared memory.

---

## 12. Synchronization Mechanisms

### 12.1 Critical Section

**Critical Section:** Section of a program that accesses shared resources and must be executed by only one process or thread at a time to avoid race conditions.

**Shared Resources:** Variables, Files, Memory.

### 12.2 Solutions to Critical Section Problem

Three solutions to the critical section problem:

1. Software solutions (Peterson's Solution)
2. Hardware solutions
3. Semaphores

### 12.3 Semaphores

**Semaphore:** Synchronization mechanism

- Controls access to shared resources in concurrent systems
- Prevents race conditions
- An integer variable
- Accessed only via atomic operations

#### Atomic Operations

**Two Atomic Operations:**
- **wait():** Decrements semaphore value
- **signal():** Increments semaphore value

**No Ownership:** OS does not check who acquired it (Can be misused)
- Thread T1 does wait()
- Thread T2 can legally do signal()

#### Types of Semaphores

**Binary Semaphore:** Value = 0 or 1, Similar to a mutex, Used for mutual exclusion

**Counting Semaphore:** Value ≥ 0, Controls access to multiple identical resources

**Common Problems with Semaphores:** Deadlock, Starvation, Priority inversion

### 12.4 Priority Inversion

**Priority inversion** is a scheduling problem where a high-priority process/thread is forced to wait because a lower-priority process holds a resource, and a medium-priority process preempts the low-priority one, indirectly blocking the high-priority task.

**Why Happens:**
- Mutex held by a low-priority thread
- Preemptive priority scheduling

**Scenario:**
1. L acquires a mutex and enters critical section
2. H becomes ready and tries to lock the same mutex → blocked
3. M becomes ready and preempts L (Preemptive Scheduling)
4. L cannot run → cannot release mutex (M is running)
5. H keeps waiting (Inverted Priority)

### 12.5 Mutex

A **mutex** is a synchronization primitive used to ensure that only one process or thread can access a critical section at a time. Ownership-based (only the thread that locks it should unlock it).

**Usage:**
- Lock before entering the critical section
- Unlock after leaving it
- If a thread tries to lock an already locked mutex, it waits

```
lock(mutex);
/* critical section */
unlock(mutex);
```

#### Priority Inheritance

Mutex supports priority inheritance:
- When a low-priority thread holds a resource needed by a high-priority thread, the low-priority thread temporarily inherits the higher priority until it releases the resource
- L Cannot be preempted by M
- After unlock, restored priority and H acquires mutex

#### Recursive Mutex

If a thread that had already locked a non-recursive mutex, tries to lock the mutex again (Recursion), results in a deadlock. It is because no other thread can unlock the mutex.

### 12.6 Peterson's Solution

**Peterson's solution** is a software-based algorithm that solves the critical section problem for two processes using a bool array flag of size 2 and an int variable turn to accomplish it.

**Assumptions:**
- Only two processes: P0 and P1
- Atomic read/write of variables

**Working:**
1. A process signals its intention using flag[i]
2. It politely gives priority to the other process using turn
3. If both want to enter, turn can only be one of the following, other has to wait, no order
4. When a process exits, it resets its flag

### 12.7 Bounded Waiting

A system is said to follow **bounded waiting conditions** if a process wants to enter into a critical section will enter in some finite time.


## 13. Deadlock

### 13.1 Definition

A **deadlock** is a situation in an operating system where two or more processes are stuck forever, each waiting for a resource that is held by another process in the group.

### 13.2 Necessary Conditions for Deadlock

A deadlock can occur only if all four conditions hold simultaneously:

1. **Mutual Exclusion:** Only one process can use the resource at a time
2. **Hold and Wait:** A process is holding at least one resource and waiting to acquire additional resources
3. **No Preemption:** Resources must be released voluntarily by the process holding them, not preempted by OS
4. **Circular Wait:** A set of processes waiting for each other in circular form

### 13.3 Deadlock Prevention

**(Simpler But Leads to Poor Utilization)**

**Break Mutual Exclusion:** Make resources sharable

**Break Hold and Wait:** A process must release held resources before requesting new ones

**Break No Preemption:** Allow resources to be forcibly taken away

**Break Circular Wait:** Processes request resources only in increasing order

### 13.4 Deadlock Avoidance

The set of dispatchable processes is in a **safe state** if there exists at least one temporal order in which all processes can be run to completion without resulting in a deadlock.

#### Resource Allocation Graph (RAG)

A **Resource Allocation Graph (RAG)** is a directed graph used by an operating system to model resource usage and analyze deadlocks.

**Nodes:**
- **Process nodes:** circles
- **Resource nodes:** rectangles

**Edges:**
- **Request edge:** P → R [Process P is requesting resource R]
- **Assignment edge:** R → P [Resource R is allocated to process P]

**Single Instance per Resource:**
- Cycle exists ⟹ Deadlock
- No cycle ⟹ No deadlock

**Multiple Instances per Resource:** Cycle may exist, but deadlock is not guaranteed

#### Wait-For Graph (WFG)

A **Wait-For Graph** is a directed graph used to detect deadlocks, derived from a Resource Allocation Graph

**Nodes:** Only processes (P1, P2, …)

**Edges:** Pi → Pj (Replace Pi → Rk → Pj)
- Process Pi is waiting for a resource currently held by Pj

**Single-Instance Resources:**
- Cycle exists ⟹ Deadlock
- No cycle ⟹ No deadlock

**Multiple-Instance Resources:** WFG cannot be directly used

#### Banker's Algorithm

**Banker's Algorithm** is a deadlock avoidance algorithm used by an operating system to ensure that resource allocation keeps the system in a safe state. It decides whether to grant a resource request by simulating the allocation and checking if the system can still avoid deadlock.

**Like a banker:**
- Gives loans only if it can still satisfy all customers
- Avoids situations where the bank runs out of money

### 13.5 Deadlock Handling or Recovery

#### Process Termination

**Abort All Deadlocked Processes:**
- Simple and fast
- But causes loss of all work

**Abort One Process at a Time:**
- Repeatedly kill processes until deadlock is resolved
- (Based on Priority or Resources Held)

#### Resource Preemption

Take resources from processes. Choose the process for preemption that causes the least overall system cost.

#### Challenges in Recovery

- Rollback may not be possible
- Preempting non-preemptable resources (printers) is impossible

---

## 14. File Systems

### 14.1 Definition

A **file** is a collection of related information that is recorded on secondary storage. Or file is a collection of logically related entities.

### 14.2 File Allocation Table (FAT)

Disk is divided into fixed-size blocks (clusters)

**File Allocation Table (FAT)** tells the OS which file belongs to which block and what the next block is. FAT is an array where each entry corresponds to one block.

---

**End of Document**
