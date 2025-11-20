def numDecodings(self, s: str) -> int:
    # Recursion Brute Force:
    # At each step, two options, either only take one digit and call rest
    # Or take 2 digits and call rest, satsifying <= 26
    # In case 0, can not be taken for single digit so return 0 (Not a way)
    # Cases with 0, will be called with double digit calls, anyways, 
    # So no need to worry about return 0 if 0 encountered
    # TC: O(2^n), SC: O(N)
    def helper(index):   
        if index == len(s): # If end of word reached, one way is found (End marked by last + 1)
            return 1
        if s[index] == "0": # If 0 encountered return 0, as split can not be possible, 
            return 0        # Not an issue if 10 because, that will be called as 10 also, apart from 1 and 0.
        ways = helper(index + 1)    # For digits other 0, call with next, split there possible 
        if index < len(s) - 1:  # If two digit call can be possible (Can not be possible from last index)
            if s[index] == "1" or (s[index] == "2" and s[index + 1] <= "6"):
                ways += helper(index + 2)   # Call only if valid two digit less than 27
        return ways
    return helper(0)

    # Use Memoization DP: Avoid Repeated Computations
    # TC: O(N), SC: O(N)
    dp = [-1] * len(s)
    def helper(index):   
        if index == len(s): # If end of word reached, one way is found (End marked by last + 1)
            return 1
        if s[index] == "0": # If 0 encountered return 0, as split can not be possible, 
            return 0        # Not an issue if 10 because, that will be called as 10 also, apart from 1 and 0.
        if dp[index] != -1:
            return dp[index]
        ways = helper(index + 1)    # For digits other 0, call with next, split there possible 
        if index < len(s) - 1:  # If two digit call can be possible (Can not be possible from last index)
            if s[index] == "1" or (s[index] == "2" and s[index + 1] <= "6"):
                ways += helper(index + 2)   # Call only if valid two digit less than 27
        dp[index] = ways
        return dp[index]
    return helper(0)

    # DP Bottom Up: Tabulation
    # TC: O(N), SC: O(N)
    dp = [0] * (len(s) + 1)
    dp[len(s)] = 1  # Base Case 
    for index in range(len(s) - 1, -1, -1):
        if s[index] == "0":  # Already dp[index] value is 0, so no computation, skip for next iteration
            continue
        ways = dp[index + 1]
        if index < len(s) - 1:
            if s[index] == "1" or (s[index] == "2" and s[index + 1] <= "6"):
                ways += dp[index + 2]   # Compute only if valid two digit less than 27
        dp[index] = ways
    return dp[0]

    # Space Optimisation: Tabulation
    # TC: O(N), SC: O(1)
    res = 0
    dp1 = 1
    dp2 = None 
    for index in range(len(s) - 1, -1, -1):
        if s[index] == "0":
            res = 0
        else:
            ways = dp1
            if index < len(s) - 1:
                if s[index] == "1" or (s[index] == "2" and s[index + 1] <= "6"):
                    ways += dp2
            res = ways
        res, dp1, dp2 = 0, res, dp1
    return dp1
