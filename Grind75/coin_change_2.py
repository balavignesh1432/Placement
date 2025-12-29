def change(self, amount: int, coins: List[int]) -> int:
    # DP: Iterating through coins for every amount value
    # But index is needed to avoid permuations and counting only combinations'
    # Using this index, At each step, explore coin denomination from index to end
    # When taking the coin, call with same index as it can be taken multiple times
    # Base case: If amount left is 0, return 1 as one combination is found
    # If left < 0, combination is not possible, so return 0
    # Add all combinations at each step and return the count
    # TC: O(N^2 * amount) SC: O(N * amount)
    # Because N * amount states, and for each state exploring all coins from index to end (N).
    dp = {}
    def helper(index, left):
        if left == 0:
            return 1
        if left < 0:
            return 0
        if (index, left) in dp:
            return dp[(index, left)]
        count = 0
        for i in range(index, len(coins)):
            count += helper(i, left - coins[i])
        dp[(index, left)] = count
        return count

    return helper(0, amount)
    
    # Optimised DP: Using take and not Take
    # At each step, either take if so add the coin to amount and call with same index (Multiple times)
    # If not take, call with next index without changing amount.
    # Base case: If target is reached, return 1 as one combination is found
    # If out of coins or exceeding target return 0, as combination is not possible.
    # Add all combinations at each step and return the count
    # TC: O(N * amount), SC: O(N * Amount)
    dp = {}
    def helper(index, target):
        if target == amount:
            return 1
        if index >= len(coins) or target > amount:
            return 0
        if (index, target) in dp:
            return dp[(index, target)]
        take = helper(index, target + coins[index])
        notTake = helper(index + 1, target)
        dp[(index, target)] = take + notTake
        return take + notTake
    return helper(0, 0)