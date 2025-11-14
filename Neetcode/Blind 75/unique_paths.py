def uniquePaths(self, m: int, n: int) -> int:
    # Recursion DP: Top Down
    # TC: O(M * N), SC: O(M * N)
    dp = [[-1] * n for _ in range(m)]
    def dfs(row, col):
        if row == m or col == n:
            return 0
        if row == m - 1 and col == n - 1:
            return 1
        if dp[row][col] != -1:
            return dp[row][col]
        dp[row][col] = dfs(row + 1, col) + dfs(row, col + 1)
        return dp[row][col]
    return dfs(0, 0)

    # DP Iteration: Bottom Up
    # TC: O(M * N), SC: O(M * N)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    dp[m - 1][n - 1] = 1
    for row in range(m - 1, -1, -1):
        for col in range(n - 1, -1, -1):
            if row == m - 1 and col == n - 1:
                continue
            dp[row][col] = dp[row + 1][col] + dp[row][col + 1]
    return dp[0][0]

    # DP Iteration Space Optimized, TC: O(m * n), SC: O(n)
    # Since last row is 1, and Last Col is 1,
    # If iterating from penultimate row, bottom row and right value is only needed.
    # So only use extra memory for 1 row
    dp = [1] * n
    for row in range(m - 2, -1, -1):    # Since last row is already computed
        for col in range(n - 2, -1, -1):    # Since last col is always 1, only compute from penultimate
            dp[col] = dp[col] + dp[col + 1] # dp[col] is bottom cell value, dp[col + 1] is right cell value
            # Update to dp[col] for computing above row cell, in future iteration
    return dp[0] # Return value of start cell.