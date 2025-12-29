# Use Max Heap to get largest two stones
# Push all stones into max heap
# Until the heap size is atleast 2 pop largest two stones and smash
# Smash and push into heap if different size
# TC: O(N log N), SC: O(N)
def lastStoneWeight(self, stones: List[int]) -> int:
    maxHeap = []
    for stone in stones:
        heappush(maxHeap, -stone)
    while len(maxHeap) > 1:
        y = -heappop(maxHeap)
        x = -heappop(maxHeap)
        if y > x:
            heappush(maxHeap, -(y - x))
    return 0 if not len(maxHeap) else -maxHeap[0]