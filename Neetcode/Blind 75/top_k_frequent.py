def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    # Storing counts with values in list and sorting
    # TC - O(NlogN), SC - O(N)
    count = defaultdict(int)
    for n in nums:
        count[n] += 1
    items = []
    for item in count:
        items.append([count[item], item])
    items.sort()
    return [items[len(items) - i - 1][1] for i in range(k)]


    # Using only k size min Heap for storing counts and only popping K times
    # If heap gets bigger than k, pop it
    # This ensure k biggest remain in heap.
    # TC - O(N * logK), SC - O(N + K)
    count = defaultdict(int)
    for n in nums:
        count[n] += 1
    heap = []
    for item in count:      # O(N)
        heapq.heappush(heap, [count[item], item])   # O(logk)
        if len(heap) > k:
            heapq.heappop(heap)
    return [heapq.heappop(heap)[1] for _ in range(k)]
    

    # Using bucket where index represent frequencies
    # Iterate from end of bucket to get top frequent
    # Think of it when dealing with frequencies
    # Maximum frequency can only be size of the array. So Frequency Bucket comes in handy.
    # TC - O(N), SC - O(N)
    bucket = [[] for _ in range(len(nums) + 1)]
    count = defaultdict(int)
    for n in nums:
        count[n] += 1
    for item in count:
        bucket[count[item]].append(item)
    res = []
    for i in range(len(bucket) - 1, -1, -1):
        for item in bucket[i]:
            res.append(item)
            if len(res) == k:
                return res