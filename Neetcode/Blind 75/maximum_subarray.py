def maxSubArray(self, nums: List[int]) -> int:
    # Brute Force: O(N*2), SC: O(1)
    # Calculate Sum of every subarray, and keep track of maximum
    maxSum = float('-inf')
    for i in range(len(nums)):
        subSum = 0
        for j in range(i, len(nums)):
            subSum += nums[j]
            maxSum = max(subSum, maxSum)
    return maxSum

    # Kadane's Sliding Window, TC: O(N), SC: O(1)
    # Intuition: Keep Calculating Subarray sum,  if a number when added with Subsum so far and results less than it itself,
    # Then reset the window from that number.
    # Otherwise keep increasing window, and keep calculating subSum, keep track of maximum Subsum.
    # Note: the window does not necessarily hold the maxSub array, but maxSum always results correct maximum value.
    j = 0
    maxSum = subSum = float('-inf')
    while j < len(nums):
        if nums[j] > nums[j] + subSum: # This equation can be simplified, canceling both sides, 0 > subSum (Kadane's)
            subSum = nums[j]
        else:
            subSum += nums[j]
        j += 1
        maxSum = max(subSum, maxSum)
    return maxSum