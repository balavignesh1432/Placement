def climbStairs(self, n: int) -> int:
    # Top Down Recursion DP: Call with n, if end reached then one way is found, so return 1
    # If landing beyond base return 0, as it is not a plausible way
    # Each level, call with one jump and two jump, add the number of ways for each type and return
    # Just store this values in 1D dp array, check if already exist for that index
    # where dp[index] has number of ways to reach end for index stairs
    # So use negative numbers to check for already computed, if not computed, then compute and update dp.
    dp = [-1] * (n + 1)
    def helper(level):
        if level == 0:
            return 1
        if level < 0:
            return 0
        if dp[level] == -1:
            dp[level] = helper(level - 1) + helper(level - 2)
        return dp[level]
    return helper(n)

    # Bottom Up DP Iteration: TC = O(N), SC: O(1)
    # Since two values are needed in Top Down. Start from bottom with those two values
    # Fill all values of dp array from 3rd index by adding previous 2. As 1 and 2 are already filled
    # return nth index of dp array
    dp = [0] * (n + 1)
    if n <= 2:
        return n
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

    # Space optimisation: TC = O(N), SC: O(1)
    # Since only 2 values, no need entire array. Use two variables
    if n <= 2:  # If only base cases, then return then itself
        return n
    one = 1 # Ways for 1 step
    two = 2 # Ways for 2 step
    ans = 0
    for _ in range(3, n + 1):   # Only start from 3, as already have 2, until n (inclusive - nth step)
        ans = one + two
        one = two
        two = ans
    return ans