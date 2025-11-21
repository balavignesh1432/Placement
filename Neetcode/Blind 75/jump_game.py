def canJump(self, nums: List[int]) -> bool:
    # Recursion Dp:
    # At each stage check all options to jump
    # Base case, if end or exceeds return True
    # If any jump calls return True, return True else return False
    # Use memoization to avoid repeated calls
    # TC: O(N^2), SC: O(N)
    # Total depth N, For each iteration N - 1, N -2,.., so N^2
    dp = [-1] * len(nums)
    def helper(index):
        if index >= len(nums) - 1:
            return True
        if dp[index] != -1:
            return dp[index]
        for jump in range(1, nums[index] + 1):
            if helper(index + jump):
                dp[index] = True
                return dp[index]
        dp[index] = False
        return dp[index]
    return helper(0)

    # Greedy Intuition: Since goal is to reach end,
    # From end: We can check if from that node we can reach end,
    # If so we mark the index as nearestPossible
    # So goal is to just get to nearestPossible, from each index,
    # At the end, if nearestPossible is not 0th index, then return False
    # TC: O(N), SC: O(1)
    nearestPossible = len(nums) - 1
    for i in range(len(nums) - 1, -1, -1):
        if i + nums[i] >= nearestPossible:
            nearestPossible = i
    return nearestPossible == 0