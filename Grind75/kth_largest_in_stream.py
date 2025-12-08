class KthLargest:
    # Use Min heap of size k, For maximum k elements
    # Add to heap
    # Pop when size exceeds k
    # TC: O(N log K), SC: O(K)
    # Each add, log K
    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.size = k
        for num in nums:
            heappush(self.heap, num)
            if len(self.heap) > k:
                heappop(self.heap)

    def add(self, val: int) -> int:
        heappush(self.heap, val)
        if len(self.heap) > self.size:
            heappop(self.heap)
        return self.heap[0]