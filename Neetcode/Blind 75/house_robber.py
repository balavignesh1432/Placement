def rob(self, nums: List[int]) -> int:

    # dp = [-1] * len(nums)
    # DP Top Down Recursion: TC = O(N), SC = O(N) Call Stack
    # At each step, can rob or not, Return maximum of two scenarios
    # If rob, then move to index + 2, else move to index + 1
    # If robbing, money looted is returned value + nums[index]
    # If not robbing, money looted is returned value
    # Check is already computed for index in dp array, before calling cases
    # Base case: when index reached end, maximum value is taking that element (Since money non negative)
    # Base Case: When index exceeds, no money can be looted so return 0
    def helper(index):
        if index > len(nums) - 1:
            return 0
        if index == len(nums) - 1:
            return nums[index]
        if dp[index] != -1:
            return dp[index]
        rob = nums[index] + helper(index + 2)
        notRob = helper(index + 1)
        dp[index] = max(rob, notRob)
        return dp[index]
    return helper(0)

    # DP Bottom Up Iteration: TC = O(N), SC = O(N)
    dp = [0] * (len(nums) + 1) # For Out of bound case
    dp[len(nums) - 1] = nums[-1]
    for i in range(len(nums) - 2, -1, -1): # Iterate for dp values that have to be computed
        rob = nums[i] + dp[i + 2]
        notRob = dp[i + 1]
        dp[i] = max(rob, notRob)
    return dp[0]

    # DP - Space Optimised
    # TC = O(N), SC = O(1)
    # Since only dp variables used in iteration at a time, use two variables instead of array
    # Update two variables, after computing result
    next1 = nums[-1] # Index at end
    next2 = 0   # Out of bound
    for i in range(len(nums) - 2, -1, -1):
        rob = nums[i] + next2
        notRob = next1
        store = max(rob, notRob)
        next2 = next1
        next1 = store
    return next1

    # Can also be implemented in recursion like this, but cannot use DP
    maxMoney = 0
    def helper(index, money):
        if index > len(nums) - 1:
            nonlocal maxMoney
            maxMoney = max(money, maxMoney)
        if index <= len(nums) - 1:
            helper(index + 2, money + nums[index])
            helper(index + 1, money)
    helper(0, 0)
    return maxMoney
