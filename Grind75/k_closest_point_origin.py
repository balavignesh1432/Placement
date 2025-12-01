# Brute Force: 
# Sort the points based on their squared distance from the origin
# Return the first k points from the sorted list
# Time Complexity: O(N log N) where N is the number of points
# Space Complexity: O(1) if we ignore the space required for the output
def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    points.sort(key=lambda p: p[0]**2 + p[1]**2)
    return points[:k]

# Use a max-heap of size k to keep track of the k closest points to the origin
# For each point, we calculate its squared distance from the origin
# We push the negative of the distance along with the point into the max-heap
# If the size of the max-heap exceeds k, we pop the farthest point (the root of the max-heap)
# This is to ensure that we only keep the k closest points in the heap, and remove k+1 th biggest point
# IMP: Do not perform comparison with root, maxheap pop will take care of it when size exceeds k
# Finally, we extract the points from the max-heap to return as the result
# Time Complexity: O(N log k) where N is the number of points   
# Space Complexity: O(k) for the max-heap
# We use squared distance to avoid computing square roots which are unnecessary for comparison
# Since we only need ordering of distances and not exact distances, squared distances suffice
from heapq import heappush, heappop
import math
def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxheap = []
        for x, y in points:
            distance = math.pow(x, 2) + math.pow(y, 2)
            heappush(maxheap, [-distance, [x, y]])
            if len(maxheap) > k:
                heappop(maxheap)
        return [point[1] for point in maxheap]