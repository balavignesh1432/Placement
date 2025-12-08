def leastInterval(self, tasks: List[str], n: int) -> int:
    # Brute Force:
    # Use a max-heap to always get the most frequent task
    # Keep track of the last position each task was placed
    # If the most frequent task cannot be placed due to cooldown
    # Store it in seperate memory and pick the next most frequent task
    # Reinsert the stored tasks back into the heap, after each placement
    # If a task is placeable, update its last placed position
    # Decrease the count and reinsert into the heap if still available
    # If no task can be placed, we have to idle
    # Increment the time index after each placement or idle
    # Time Complexity: O(N log K) where N is number of tasks and K is number of unique tasks
    # Space Complexity: O(K) for the count dictionary, position dictionary and max-heap
    # K <= 26 for uppercase English letters, so O(1) space effectively
    count = {}
    pos = {}
    for task in tasks:
        count[task] = count.get(task, 0) + 1
    maxHeap = []
    for c in count:
        maxHeap.append([-count[c], c])
        pos[c] = -1

    heapify(maxHeap)
    store = []
    index = 0
    while maxHeap:
        count, task = heappop(maxHeap)
        while pos[task] != -1 and maxHeap and index - pos[task] <= n: 
            store.append([count, task])
            count, task = heappop(maxHeap)
        if pos[task] == -1 or index - pos[task] > n:   # Placeable
            pos[task] = index
            count += 1
            if count < 0:
                heappush(maxHeap, [count, task])
        else:                                           # Idle
            store.append([count, task])
        while store:
            heappush(maxHeap, store.pop())
        index += 1
    return index

    # Optimized Approach:
    # Intution: Use a queue to still maintain the order of tasks in their cooldown period
    # Move back tasks from the cooldown queue to the max-heap as soon as they are available
    # This way we don't have to push to heap from separate memory after every placement
    # Front of Queue will always have the task which is going to be max Freq and available the earliest
    # Use a max-heap to always get the most frequent task
    # Use a queue to keep track of tasks in their cooldown period
    # After each placement, add the task to the cooldown queue with the time it will be available again
    # At each time index, check if any task in the cooldown queue is now available
    # If available, reinsert it back into the max-heap
    # Pop the most frequent task from the max-heap and place it
    # If placed, decrease its count and add it to the cooldown queue if still available (count < 0)
    # Increment the time index after each placement or idle
    # Time Complexity: O(N log K) where N is number of tasks and K is number of unique tasks
    # Space Complexity: O(K) for the count dictionary, cooldown queue and max-heap
    # K <= 26 for uppercase English letters, so O(1) space effectively
    count = {}
    for task in tasks:
        count[task] = count.get(task, 0) + 1                                            
    maxHeap = []
    for c in count:
        maxHeap.append([-count[c], c])
    heapify(maxHeap)
    index = 0
    cooldown = deque()
    while maxHeap or cooldown:
        if cooldown and cooldown[0][0] == index:
            cool, task, count = cooldown.popleft()
            heappush(maxHeap, [count, task])
        if maxHeap:
            count, task = heappop(maxHeap)
            count += 1
            if count < 0:
                cooldown.append([index + n + 1, task, count])
        index += 1
    return index



    # Mathematical Approach:
    # Intuition: The most frequent tasks will determine the structure of the schedule.
    # We create "blocks" of size (n + 1) to accommodate the cooldown period. 
    # Where first place in each block is occupied by the most frequent tasks.
    # The number of such full blocks will be (maxFreq - 1)
    # The last block may not need to be full, hence we add maxCount. (Will be atleast 1)
    # As these will be occupied by the similar most frequent tasks.
    # We take the maximum with len(tasks) to ensure we account for cases
    # where there are more tasks to fill all idle slots.
    # Logic: Count the frequency of each task
    # Find the maximum frequency among all tasks
    # Count how many tasks have this maximum frequency
    # Calculate the minimum time required using the formula:
    # Time = (maxFreq - 1) * (n + 1) + maxCount
    # Finally, return the maximum of the calculated time and the length of tasks
    # 
    # Time Complexity: O(N) where N is number of tasks
    # Space Complexity: O(1) since we are using a fixed size array
    count = [0] * 26
    for task in tasks:
        count[ord(task) - ord('A')] += 1

    maxf = max(count)
    maxCount = 0
    for i in count:
        if i == maxf:
            maxCount += 1

    time = (maxf - 1) * (n + 1) + maxCount
    return max(len(tasks), time)