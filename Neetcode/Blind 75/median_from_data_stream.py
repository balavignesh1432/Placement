# Brute Force: Using Array
# Each add operation takes O(1)
# For median, sort and return media. Each median operation takes O(N log N)
# SC: O(N)
class MedianFinder:
    def __init__(self):
        self.list = []

    def addNum(self, num: int) -> None:
        self.list.append(num)

    def findMedian(self) -> float:
        self.list.sort()
        mid = len(self.list)//2
        if len(self.list) % 2 == 0:
            return (self.list[mid] + self.list[mid - 1]) / 2
        else:
            return self.list[mid]

# Using Heaps: Goal to reduce findMedian to O(1), by trading with addNum
# Since median can require two value, if even length, we need two heaps, 
# such that lookup of root element only takes O(1)
# So we need two heaps one max heap containing lower half element
# Another min heap containing higher half elements
# For adding, initially when both empty add to upperhalf
# When adding, check if <= upperhalf minheap peak, then belongs to lower half
# Otherwise if > belongs to upperhalf.
# But since two heaps have to only contain half of the elements,
# After pushing to the appropriate heap, do balancing. if size difference exceeds 1
# For Balancing pop from bigger size heap and push to lower size heap
# This ensures equal half of elements present in both heaps
# For Median, if both heaps are equal size then find average of their roots
# Otherwise, return root of the bigger size heap
# TC: O(Log N) for Add, Since each Pop, Push takes O(Log N), O(1) for FindMedian as peek only
# SC: O(N)
import heapq
class MedianFinderHeaps:
    def __init__(self):
        self.minheap = []
        self.maxheap = []

    def addNum(self, num: int) -> None:
        if len(self.minheap) == 0:
            heapq.heappush(self.minheap, num)
        else:
            if num <= self.minheap[0]:
                heapq.heappush(self.maxheap, -1 * num)
                if len(self.maxheap) - len(self.minheap) > 1:
                    mid = heapq.heappop(self.maxheap)
                    heapq.heappush(self.minheap, -1 * mid)
            else:
                heapq.heappush(self.minheap, num)
                if len(self.minheap) - len(self.maxheap) > 1:
                    mid = heapq.heappop(self.minheap)
                    heapq.heappush(self.maxheap, -1 * mid)
    
    def findMedian(self) -> float:
        if len(self.minheap) == len(self.maxheap):
            return ((-1 * self.maxheap[0]) + self.minheap[0]) / 2
        elif len(self.minheap) > len(self.maxheap):
            return self.minheap[0]
        else:
            return -1 * self.maxheap[0]