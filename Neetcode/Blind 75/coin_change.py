def coinChange(self, coins: List[int], amount: int) -> int:
    # TC: O(N * amount), SC: O(N * amount)
    # At each step, either to take or not take the denomination
    # If taking, call with same index and sum added
    # If not taking denomination, call with next index, without changing sum so far
    # Since min no. of. coins is the needed answer, add 1 to take's return value
    # Return minimum of take and not take
    # Base Case: If target sum is reached return 0, as 1 is added to parent call for taking that.
    # If running out of denominations or exceeding target sum, return infinity (As minimum is only computed at parent)

    dp = [[-1] * (amount + 1) for _ in range(len(coins))]
    def helper(index, sumCoins):
        if sumCoins == amount:
            return 0
        if sumCoins > amount or index >= len(coins):
            return float('inf') 
        if dp[index][sumCoins] != -1:
            return dp[index][sumCoins]
        take = helper(index, sumCoins + coins[index]) + 1
        notTake = helper(index + 1, sumCoins)
        dp[index][sumCoins] = min(take, notTake)
        return dp[index][sumCoins]
    if amount == 0:
        return 0
    res = helper(0, 0)
    return res if res != float('inf') else -1

    # Can be implemented as 1D array.
    # Instead of take, not take on Coins.
    # At each step going to take a coin, explore possible values for ith coin.
    # Call each denomination with subtracting the value from amount left
    # The coins needed is 1 + the returned value from the call.
    # Only call if coins is smaller or equal to amount left (Or return infinity)
    # Find minimum all possible coin denominations and return
    # TC: (amount * N) All denominations for each depth , SC: O(amount) # Max Depth is amount when denomination is 1
    dp = {}
    def helper(left):
        if left == 0:   # If reached target amount return 0, is added 1 for the parent call
            return 0
        if left in dp:
            return dp[left]
        # Calculate minCoins, for each possible denomination
        minCoins = float('inf')
        for coin in coins:
            if coin <= left: # Only call if coin is less than target left
                minCoins = min(minCoins, helper(left - coin) + 1)   # One to indicate one coin taken
        dp[left] = minCoins
        return dp[left]
    res = helper(amount)
    return res if res != float('inf') else -1