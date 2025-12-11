def canPartition(self, nums: List[int]) -> bool:
    # Since two partition with all elements without missing any
    # This effectively becomes finding subset sum as total sum / 2.
    # So check if total sum is odd, then it is not possible to split, as all are integers
    # If even, then divide by 2 and do subset sum equals k.
    # At each step, 2 options to take or not take
    # If take add to subsum
    # Base case: If subsum is target, then return True
    # If out of bounds return False
    # TC: O(N ^ 2), SC: O(N ^ 2)

    target = sum(nums)
    if target & 1:      # Check odd
        return False
    else:               # If even, target is sum / 2
        target = target >> 1
    
    dp = [[-1] * (target + 1) for _ in range(len(nums) + 1)]
    def helper(index, subSum):
        if subSum == target:    # IF target found, Comes before out of bounds check
            return True
        if index >= len(nums):
            return False
        if dp[index][subSum] != -1:
            return dp[index][subSum]
        notTake = helper(index + 1, subSum)
        take = False
        if subSum + nums[index] <= target:
            take = helper(index + 1, subSum + nums[index]) 
        dp[index][subSum] = take or notTake
        return dp[index][subSum]
    return helper(0, 0)
    
    # DP Tabulation
    # TC: O(N ^ 2), SC: O(N ^ 2)
    dp = [[False] * (target + 1) for _ in range(len(nums) + 1)]
    for index in range(len(nums) + 1):
        dp[index][target] = True
    for index in range(len(nums) - 1, -1, -1):
        for subSum in range(target, -1, -1):
            notTake = dp[index + 1][subSum]
            take = False
            if subSum + nums[index] <= target:
                take = dp[index + 1][subSum + nums[index]]
            dp[index][subSum] = take or notTake
            return dp[index][subSum]
    return dp[0][0]

    # DP Space Optimized
    # TC: O(N ^ 2), SC: O(N)
    curr = [False] * (target + 1)
    dp = [False] * (target + 1)
    dp[target] = True
    for index in range(len(nums) - 1, -1, -1):
        for subSum in range(target, -1, -1):
            notTake = dp[subSum]
            take = False
            if subSum + nums[index] <= target:
                take = dp[subSum + nums[index]]
            curr[subSum] = take or notTake
        curr, dp = dp, curr
    return dp[0]