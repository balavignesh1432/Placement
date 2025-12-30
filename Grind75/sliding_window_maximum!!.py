# When dealing with sliding window problems, and using heaps or queue, store index along with value
# This helps when popping out of window elements
def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    # MaxHeap: Intuition
    # For each index, maximum within the window is needed,
    # So use maxheap, and pop until the maximum in the heap is within the window, or becomes empty
    # Then push current element to heap along with index, now root is maximum
    # Store it in result, Finally return it slicing from kth position
    # Note: Heap may not need to contain only the window elements, lazily popped
    # TC: O(N log N), SC: O(N)
    res = []
    heap = []
    for i in range(len(nums)):
        while heap and i - heap[0][1] >= k:
            heappop(heap)
        heappush(heap, [-nums[i], i])
        res.append(-heap[0][0])
    return res[k-1:]

    # Monotonically Decreasing Queue, Deque
    # Intuition, When a big element is seen inside a window, all elements to the left of it is not needed,
    # So add to queue, then until empty, check if bigger than last element
    # If so keep popping, until condition fails
    # That is only place element current element is smaller than previous
    # This ensures, when popping front when window moves, the next bigger element is next to it
    # Every time check window and then popleft, then maintaing the mono queue
    # Note: Biggest element is always at the front
    # Add that to result, then return sliced result from k-1
    # TC: O(N), SC: O(N) 
    monotonic = deque()
    result = []
    for i in range(len(nums)):
        if monotonic and i - monotonic[0][1] >= k:
            monotonic.popleft()
        while monotonic and nums[i] >= monotonic[-1][0]:
            monotonic.pop()
        monotonic.append([nums[i], i])
        result.append(monotonic[0][0])
    return result[k-1:]