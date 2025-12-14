def minCostClimbingStairs(self, cost: List[int]) -> int:
    # DP Memoization:
    # At each step, climb one or two
    # Add the cost of step to call, return min of both options
    # Base case: When able to reach top, return 0 as cost
    # TC: O(N), SC: O(N)
    dp = {}
    def helper(index):
        if index >= len(cost):
            return 0
        if index in dp:
            return dp[index]
        one = helper(index + 1)
        two = helper(index + 2)
        dp[index] = min(one, two) + cost[index]
        return dp[index]
    return min(helper(0), helper(1))

    # DP Tabulation
    # TC: O(N), SC: O(N)
    dp = [0] * (len(cost) + 2)
    for index in range(len(cost) - 1, -1, -1):
        one = dp[index + 1]
        two = dp[index + 2]
        dp[index] = min(one, two) + cost[index]
    return min(dp[0], dp[1])

    # DP Space Optimized
    # TC: O(N), SC: O(1)
    dp = 0
    dp1 = 0
    dp2 = 0
    for index in range(len(cost) - 1, -1, -1):
        one = dp1
        two = dp2
        dp = min(one, two) + cost[index]
        dp, dp1, dp2 = dp2, dp, dp1
    return min(dp1, dp2)