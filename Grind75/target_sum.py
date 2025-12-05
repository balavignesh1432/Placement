def findTargetSumWays(self, nums: List[int], target: int) -> int:
    # DFS with memoization approach
    # Use a helper function to explore adding and subtracting each number
    # Store results in a map to avoid recomputation
    # Use tuple (index, sums) as key for memoization
    # Base Case: If index reaches length of nums, check if sums equals target
    # If yes, return 1 as a valid path is found, else return 0 not a valid path
    # At each step, explore both adding and subtracting the current number
    # Add result of ways from both paths and store in dp map
    # Time: O(N * S) where N is the length of nums and S is the range of possible sums
    # Space: O(N * S) for the memoization map
    dp = {}
    def helper(index, sums):
        if index == len(nums):
            if sums == target:
                return 1
            else:
                return 0
        if (index, sums) in dp:
            return dp[(index, sums)]
        add = helper(index + 1, sums + nums[index])
        sub = helper(index + 1, sums - nums[index]) 
        dp[(index, sums)] = add + sub
        return dp[(index, sums)]
    return helper(0, 0)


    # Bottom-up DP approach
    # Use a DP table where dp[i][sums] represents number of ways to reach 'sums' using elements from index i to end
    # Initialize the DP table with array of defaultdict with length of nums + 1
    # base case: dp[len(nums)][target] = 1
    # IMP: Iterate the 2nd loop from totalSum to -totalSum to cover all possible sums
    # Fill the DP table in reverse order from the end of nums to the start
    # At each index, for each possible sum, calculate ways by adding and subtracting current number
    # Time: O(N * (2 * S)) where N is the length of nums and S is the range of possible sums
    # Space: O(N * (2 * S)) for the DP table

    totalSum = sum(nums)
    dp = [defaultdict(int) for _ in range(len(nums) + 1)]
    dp[len(nums)][target] = 1
    for index in range(len(nums) - 1, -1, -1):
        for sums in range(totalSum, -(totalSum + 1), -1):
            add = dp[index + 1][sums + nums[index]]
            sub = dp[index + 1][sums - nums[index]]
            dp[index][sums] = add + sub
    return dp[index][0]

    # Space optimized Bottom-up DP approach
    # Use two dictionaries to store current and previous row results
    # IMP: Iterate the 2nd loop from totalSum to -totalSum to cover all possible sums
    # Initialize dp1 with base case dp1[target] = 1
    # At the end of each index iteration, swap dp and dp1
    # Time: O(N * (2 * S)) where N is the length of nums and S is the range of possible sums
    # Space: O(2 * S) for the two dictionaries
    dp = defaultdict(int)
    dp1 = defaultdict(int)
    dp1[target] = 1
    for index in range(len(nums) - 1, -1, -1):
        for sums in range(totalSum, -(totalSum + 1), -1):
            add = dp1[sums + nums[index]]
            sub = dp1[sums - nums[index]]
            dp[sums] = add + sub
        dp1, dp = dp, dp1
    return dp1[0]