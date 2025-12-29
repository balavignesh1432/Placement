def maxProfit(self, prices: List[int]) -> int:
    # Instead of having second parameter as last purchased index
    # Just use a flag, to handle profit calculation use the returns of the recurrence relation
    # DP : Memoization
    # At each step, either buy or sell, and skip
    # Use a flag as 2nd parameter to check if can buy or sell
    # Recurrence relation, for each day profit calculation is
    # If buy, subtract price to call next
    # If sell, add price to call next
    # If skip, just go to next 
    # Base case: If exceeds boundary return 0
    # At Last place, will call next that is definitely returning 0
    # So this will always return itself (Selling) as it is the maximum for last step
    # When this is returned, its depending on parents call whether skip or buy it will be forwared
    # If parent was buy, then profit is basically subtract of that from returned
    # If parent was skip, then just sent back until the one that called buy, and calculate profit
    # IMP: Return value will never be negative as skip will be 0, max will choose 0
    # TC: O(N), SC:(N) 
    dp = [[-1, -1] for _ in range(len(prices))]
    def helper(index, canBuy):
        if index >= len(prices):
            return 0
        if dp[index][canBuy] != -1:
            return dp[index][canBuy]
        skip = helper(index + 1, canBuy)
        buy = sell = 0
        if canBuy:
            buy = -prices[index] + helper(index + 1, 0)
        else:
            sell = prices[index] + helper(index + 1, 1)
        dp[index][canBuy] = max(skip, buy, sell)
        return dp[index][canBuy]
    return helper(0, 1)

    # Dp Tabulation
    dp = [[0, 0] for _ in range(len(prices) + 1)]
    for index in range(len(prices) - 1, -1, -1):
        for canBuy in range(2):
            skip = dp[index + 1][canBuy]
            buy = sell = 0
            if canBuy:
                buy = -prices[index] + dp[index + 1][0]
            else:
                sell = prices[index] + dp[index + 1][1]
            dp[index][canBuy] = max(skip, buy, sell)
    return dp[0][1]

    # Dp Space Optimized
    curr = [0, 0]
    dp = [0, 0]
    for index in range(len(prices) - 1, -1, -1):
        for canBuy in range(2):
            skip = dp[canBuy]
            buy = sell = 0
            if canBuy:
                buy = -prices[index] + dp[0]
            else:
                sell = prices[index] + dp[1]
            curr[canBuy] = max(skip, buy, sell)
        dp, curr = curr, dp
    return dp[1]