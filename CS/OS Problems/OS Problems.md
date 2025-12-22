# Producer-Consumer Problem

## Problem Description

- **Producers** → produces items and puts them into a buffer
- **Consumers** → consumes items from the buffer
- **Buffer** has limited capacity

## The Challenge

The challenge is to ensure:

1. Producer does not produce when buffer is full
2. Consumer does not consume when buffer is empty
3. No race condition (Only one thread allowed to access the buffer)

---

## Naive Solution (Using Global Variables)

### Code Implementation

```c
int empty = N;
int full = 0;

// Producer:
while (empty == 0);   // busy wait ❌
empty--;
insert_item();
full++;

// Consumer:
while (full == 0);    // busy wait ❌
full--;
remove_item();
empty++;
```

### Problems with This Approach

#### 1. Race Condition

- `empty--` is not atomic. Internally: read empty, decrement, write empty
- Multiple threads can interfere with each other's operations

#### 2. Busy Waiting (CPU Wastage)

- `while (empty == 0);` - Thread spins continuously. CPU time wasted
- Thread consumes CPU cycles without doing useful work

---

## Solution: Semaphores

### Producer Code

```c
wait(empty);
wait(mutex);
produce();
signal(mutex);
signal(full);
```

### Consumer Code

```c
wait(full);
wait(mutex);
consume();
signal(mutex);
signal(empty);
```

### Why This Works

- **No busy waiting**: Semaphores block threads (Moved to Blocked State), and wake it later.
- **No race condition**: `wait` and `signal` are atomic operations.
- **Empty and Full semaphores** ensure no overflow/underflow
- **Mutex** ensures only one thread enters critical section. Otherwise, if multiple threads, then they may overwrite same index in Buffer.

### Important: Order of Semaphore Operations

**⚠️ Do not put `wait(mutex)` before `wait(empty)`, results in deadlock**

**Example of Deadlock Scenario**:
- If buffer full, then producer acquires lock, then waits on empty
- Consumer waits for lock
- Results in deadlock.

Acquiring mutex before checking resource availability can cause deadlock because the thread may block while holding the lock, preventing others from making progress.

### Potential Issue: Starvation

- But still can cause starvation, when same thread is waked up, others waiting
- Can be avoided if implemented FIFO wake up for semaphores (But not done natively).

---

# Reader-Writer Problem

## Problem Description

- There is a **shared resource**.
- There are multiple **reader processes** and **writer processes**.
- **Readers**: Only read the data, do not modify.
- **Writers**: Modify the data.

### Requirements

- Multiple readers can read simultaneously.
- Writers need exclusive access.

---

## Solution 1: Reader Priority (Using Semaphores)

Writer waits for all readers to complete reading.

### Approach

- First reader acquires, last reader releases
- So track this, need counter variable, but has to perform updation atomically
- So use another semaphore around the updation section

### Code Implementation

```c
int read_count = 0;     // number of readers currently reading 
semaphore mutex = 1;    // protects read_count semaphore 
rw_mutex = 1;           // controls access to the shared resource

// READER - ENTRY SECTION 
wait(mutex);                // lock mutex to safely change read_count 
read_count++; 
if (read_count == 1) {      // first reader arrives 
    wait(rw_mutex);         // lock the resource for readers (block writers) 
} 
signal(mutex);              // done updating read_count           

// CRITICAL SECTION (READING) 
read_data();                // actual reading of shared resource 

// EXIT SECTION 
wait(mutex);                // lock mutex to safely change read_count 
read_count--; 
if (read_count == 0) {      // last reader leaving 
    signal(rw_mutex);       // release the resource so writers can proceed 
} 
signal(mutex);              // done updating read_count

// WRITER 
wait(rw_mutex); 
write_data(); 
signal(rw_mutex);
```

---

## Solution 2: Fair Solution (Using Turnstile)

Readers read until writers arrive, Write only after existing reads complete.
Using Turnstile, an extrasemaphore, which both reader and writer wait for, ensures fairness. This way, if writer arrives and acquires turnstile, blocks upcoming readers. Before they were waiting on different semaphores, but now on common turnstile semaphore.
### Reader Code

```c
// READER 
wait(turn);        // wait your turn
wait(mutex_read);   // protect read_count 
read_count++; 
if (read_count == 1) { 
    wait(rw_mutex); // first reader locks resource 
} 
signal(mutex_read); 
signal(turn);      // allow next processese to acquire turn 

// CRITICAL SECTION 
read_data(); 

// EXIT 
wait(mutex_read); 
read_count--; 
if (read_count == 0) { 
    signal(rw_mutex); // last reader releases resource 
} 
signal(mutex_read);
```

### Writer Code

```c
// WRITER 
wait(turn);    // wait your turn 
wait(rw_mutex); // exclusive access to resource 
signal(turn);  // allow next processese to acquire turn 

// CRITICAL SECTION 
write_data(); 
signal(rw_mutex);
```

### How Fairness is Achieved

1. **When writer acquires tunrstile**: All new readers wait for it (Also new writers)
2. **Writer acquires lock**: (Existing reads complete), then releases tunrstile
3. **Next process proceeds**: So that whoever acquires turnstile next can proceed (Fairness to read and write)
4. **If reader next**: It will acquire turnstile, and be first (As count decreased to 0 when all are complete), waits for lock
5. **If writer next**: It will acquire turnstile, and waits for lock
6. **Writer completes**: Releases lock

This ensures that:
- Readers and writers are served fairly and not after one is completelty exhausted.
- No process is starved
- Existing reads complete before new writes
- New readers can join if a reader is already in the queue
