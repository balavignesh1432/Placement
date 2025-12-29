def maxProfit(self, prices: List[int]) -> int:
    # Using 2nd parameter as lastbought
    # If not bought, then it is -1,
    # Calculate profit when selling, add to the call next  + 1 (Cooldown)
    # If buying just mark the index, and call next
    # If skipping, just call next with the lastbought
    # REturn max of all 3 operations
    # Base case when exceeded range return 0
    # TC: O(N^2), SC:(N^2) 
    dp = [[-1] * (len(prices) + 1) for _ in range(len(prices))]
    def helper(index, lastBought):
        if index >= len(prices):
            return 0
        if dp[index][lastBought + 1] != -1:
            return dp[index][lastBought + 1]
        buy = skip = sell = 0
        skip = helper(index + 1, lastBought)
        if lastBought == -1:
            buy = helper(index + 1, index)
        if lastBought != -1 and prices[index] > prices[lastBought]:
            sell = helper(index + 2, -1) + (prices[index] - prices[lastBought])        
        dp[index][lastBought + 1] =  max(buy, sell, skip)
        return dp[index][lastBought + 1]
    return helper(0, -1)


    # Instead of having second parameter as last purchased index
    # Just use a flag, to handle profit calculation use the returns of the recurrence relation
    # DP : Memoization
    # At each step, either buy or sell, and skip
    # Use a flag as 2nd parameter to check if can buy or sell
    # Recurrence relation, for each day profit calculation is
    # If buy, subtract price to call next
    # If sell, add price to call next + 1 (As cooldown is 1)
    # If skip, just go to next 
    # Base case: If exceeds boundary return 0
    # At Last place, will call next that is definitely returning 0
    # So this will always return itself (Selling) as it is the maximum for last step
    # When this is returned, its depending on parents call whether skip or buy it will be forwared
    # If parent was buy, then profit is basically subtract of that from returned
    # If parent was skip, then just sent back until the one that called buy, and calculate profit
    # Profit formula becomes -prices[buy] + 0 (Skip) + prices[sell] 
    # IMP: Return value will never be negative as skip will be 0, max will choose 0.
    # TC: O(N), SC:(N) 
    dp = [[-1, -1] for _ in range(len(prices) +  1)]
    def helper(index, canBuy):
        if index >= len(prices):
            return 0
        if dp[index][canBuy] != -1:
            return dp[index][canBuy]
        buy = skip = sell = 0
        skip = helper(index + 1, canBuy)
        if canBuy:
            buy = helper(index + 1, 0) - prices[index]
        else:
            sell = helper(index + 2, 1) + prices[index]
        dp[index][canBuy] =  max(buy, sell, skip)
        return dp[index][canBuy]
    return helper(0, 1)

    # DP Tabulation
    # TC: O(N), SC: O(N)
    dp = [[0, 0] for _ in range(len(prices) + 2)]
    for index in range(len(prices) - 1, -1, -1):
        for canBuy in range(2):
            buy = skip = sell = 0
            skip = dp[index + 1][canBuy]
            if canBuy:
                buy = dp[index + 1][0] - prices[index]
            else:
                sell = dp[index + 2][1] + prices[index]
            dp[index][canBuy] =  max(buy, sell, skip)
    return dp[0][1]


    # DP Space Optimized
    # TC: O(N), SC: O(1)
    curr = [0, 0]
    dp1 = [0, 0]
    dp2 = [0, 0]
    for index in range(len(prices) - 1, -1, -1):
        for canBuy in range(2):
            buy = skip = sell = 0
            skip = dp1[canBuy]
            if canBuy:
                buy = dp1[0] - prices[index]
            else:
                sell = dp2[1] + prices[index]
            curr[canBuy] =  max(buy, sell, skip)
        curr, dp1, dp2 = dp2, curr, dp1
    return dp1[1]