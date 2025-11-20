def rob(self, nums: List[int]) -> int:
    # Recursion: Normal House Robber but with flag to check include last or not
    # Edge Case: If only one element then can take it, so index is 0, then go for take
    def helper(index, start):
        if index >= len(nums):
            return 0
        res = helper(index + 1, start) # Not Take
        if index == 0 or index != len(nums) - 1 or (index == len(nums) - 1 and start): 
            res = max(res, helper(index + 2, start) + nums[index]) # Take
        return res
    return max(helper(0, 0), helper(1, 1))

    # Top Down DP: Recursion
    # Just a flag if taken 1st element or not, to evaluate whether to include last element or not
    # So 1D dp array with 2 elements for the flag value
    # TC: O(N), SC: O(N)
    dp = [[-1, -1] for _ in range(len(nums) + 1)]
    def helper(index, start):
        if index >= len(nums):
            return 0
        if dp[index][start] != -1:
            return dp[index][start]
        res = helper(index + 1, start) # Not Take
        if index == 0 or index != len(nums) - 1 or (index == len(nums) - 1 and start):
            res = max(res, helper(index + 2, start) + nums[index]) # Take
        dp[index][start] = res
        return dp[index][start]
    return max(helper(0, 0), helper(1, 1))

    # Bottom Up Dp: Tabulation
    # TC: O(N), SC: O(N)
    dp = [[0, 0] for _ in range(len(nums) + 2)]
    for index in range(len(nums) - 1, -1, -1):
        for start in range(2):
            res = dp[index + 1][start] # Not Take
            if index == 0 or index != len(nums) - 1 or (index == len(nums) - 1 and start):
                res = max(res, dp[index + 2][start] + nums[index]) # Take
            dp[index][start] = res
    return max(dp[0][0], dp[1][1])  

    # Space Optimized Dp
    # TC: O(N), SC: O(1)
    dp, dpNext1, dpNext2 = [0, 0]
    for index in range(len(nums) - 1, -1, -1):
        for start in range(2):
            res = dpNext1[start] # Not Take
            if index == 0 or index != len(nums) - 1 or (index == len(nums) - 1 and start):
                res = max(res, dpNext2[start] + nums[index]) # Take
            dp[start] = res
        dp, dpNext1, dpNext2 = dpNext2, dp, dpNext1
    return max(dpNext1[0], dpNext2[1])  # Here 00 becomes Next1 0, and 11 becomes Next2 1