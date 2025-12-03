def findKthLargest(self, nums: List[int], k: int) -> int:
    # Sorting approach
    # Time Complexity: O(N log N)
    # Space Complexity: O(1 or N) depending on the sorting algorithm used
    nums.sort()
    return nums[len(nums) - k]
    
    # Using a max-heap to find the kth largest element
    # Heap size is maintained at (N - k + 1)
    # Root of the max-heap is the kth largest element
    # Time Complexity: O(N log (N - k + 1))
    # Space Complexity: O(N - k + 1)
    size = len(nums) - k + 1
    maxHeap = []
    for num in nums:
        heappush(maxHeap, -num)
        if len(maxHeap) > size:
            heappop(maxHeap)
    return -maxHeap[0]

    # Using a min-heap to find the kth largest element
    # Heap size is maintained at k
    # Root of the min-heap is the kth largest element
    # Time Complexity: O(N log k)
    # Space Complexity: O(k)
    minHeap = []
    for num in nums:
        heappush(minHeap, num)
        if len(minHeap) > k:
            heappop(minHeap)
    return minHeap[0]