def findMaxAverage(self, nums: List[int], k: int) -> float:
    # Effectively maximum sum subarray of length k
    # First compute k length subarray sum
    # Set this as maxSum, as from k add the right element and decrement left element from sum
    # Take the maximum of maxSum, subSum
    # Return subSum divided by K for Average
    # TC: O(N), SC: O(1)
    subSum = 0
    left = 0
    for i in range(k):
        subSum += nums[i]
    maxSum = subSum
    for i in range(k, len(nums)):
        subSum += nums[i]
        subSum -= nums[left]
        left += 1
        maxSum = max(maxSum, subSum)
    return maxSum/k