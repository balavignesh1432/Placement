def findClosestElements(self, arr, k, x):
    # Use MinHeap, of size n
    # Then pop k elements, which are smallest
    # Then sort the results
    # TC: O(N log N), SC: O(N)
    minHeap = []
    for num in arr:
        heappush(minHeap, [abs(num - x), num])
    res = [heappop(minHeap)[1] for _ in range(k)]
    res.sort()
    return res
    
    # Use MaxHeap, of size K
    # Push negated value, Then if size exceeds K, Pop
    # IMP: Use negative value for 2nd parameter also, as when there is match,
    # the bigger number should be naturally popped.
    # Finally sort the results and return
    # Edge Case, when dealing with maxHeap in Python, handle 0 as infinity
    # TC: O(N log K), SC: O(K)
    maxHeap = []
    for num in arr:
        dist = -abs(num - x)
        if dist == 0:
            dist = float('inf')
        heappush(maxHeap, [dist, -num])
        if len(maxHeap) > k:
            heappop(maxHeap)
    res = [-heappop(maxHeap)[1] for _ in range(k)]
    res.sort()
    return res

    # Two Pointer on Sorted - Intuition: Using the fact that aleady sorted, and need k elements
    # Use two pointers from the end, and shrink until window length becomes k
    # Move the pointer that is farther from the x
    # If match always move right side pointer
    # TC: O(N), SC: O(1)
    i = 0
    j = len(arr) - 1
    while i <= j and (j - i) + 1 > k:
        if abs(arr[i] - x) <= abs(arr[j] - x):
            j -= 1
        else:
            i += 1 
    return arr[i: j + 1]