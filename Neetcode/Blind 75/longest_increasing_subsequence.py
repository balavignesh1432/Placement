def lengthOfLIS(self, nums: List[int]) -> int:
    # Recursion: Top Down DP (Memoization)
    # Each position, decision to take or not, return maximum out of two
    # Each call returns maximum length, so for take add 1 to it
    # Depends on what was chose on previous call
    # Use another parameter for index of previous call (This ensures the size as n*n for dp array)
    # For initial call, use index -1, and while storing, or accessing dp array shift by + 1.
    # If previndex is -1, do not do checks before taking
    # TC: O(N^2), SC: O(N^2)
    dp = [[-1] * (len(nums) + 1) for _ in range(len(nums))]
    def helper(index, prevIndex):
        if index == len(nums):
            return 0
        if dp[index][prevIndex + 1] != -1:
            return dp[index][prevIndex + 1]
        notTake = helper(index + 1, prevIndex)
        take = 0
        if prevIndex == -1 or nums[index] > nums[prevIndex]:
            take = 1 + helper(index + 1, index)
        dp[index][prevIndex + 1] = max(take, notTake)
        return dp[index][prevIndex + 1]
    return helper(0, -1)

    # Iteration Bottom Up DP (Tabulation)
    # Index ranges from end to 0, but previndex ranges from index - 1 to -1
    # While for take case, index has to be shifted by + 1 for 2nd dimension.
    # prevIndex is represented in dp as prevIndex + 1
    # If prevIndex is index, then in dp should be represented as index + 1
    # TC: O(N^2), SC: O(N^2)
    dp = [[0] * (len(nums) + 1) for _ in range(len(nums) + 1)]
    for index in range(len(nums) - 1, -1, -1):
        for prevIndex in range(index - 1, -2, -1):
            notTake = dp[index + 1][prevIndex + 1]
            take = 0
            if prevIndex == -1 or nums[index] > nums[prevIndex]:
                take = 1 + dp[index + 1][index + 1] # Index shift for 2nd dimension which is prevIndex
            dp[index][prevIndex + 1] = max(take, notTake)
    return dp[0][0]

    # Tabulation Space Optimized
    # Only extra row needed, index + 1 row will be additional row
    # And after computing will be updated to current row
    # And current row has to be again initialised with 0s, but better way is to assign it to old row
    # Since only last element is needed for very first iteration, and it will be same for old row also
    # This reduces time for creating new array each time for current row 
    # TC: O(N^2), SC: O(N)
    dp = [0] * (len(nums) + 1)
    dpNext = [0] * (len(nums) + 1)  
    for index in range(len(nums) - 1, -1, -1):
        for prevIndex in range(index - 1, -2, -1):
            notTake = dpNext[prevIndex + 1]
            take = 0
            if prevIndex == -1 or nums[index] > nums[prevIndex]:
                take = 1 + dpNext[index + 1]
            dp[prevIndex + 1] = max(take, notTake)
        dpNext, dp = dp, dpNext
    return dpNext[0]


    # Dp With Binary Search
    # Intuition: For each element think of lis, if element greater than last element add to lis
    # If not then new sequence have to be started with that element
    # Since only length is needed, instead of starting new lis, replace value in existing lis with current element.
    # LIS will not contain the correct lis, but its length will be correctly holding max length of lis
    # Algo: From first take each element, if greater than last picked element 
    # Put the element in LIS array.
    # If not greater than last, then do binary search and place it on appropriate position in lis array, 
    # such that to the left of it all are smaller and to the right of it all are larger
    # Return the length of the lis array
    # TC: O(N log N), SC: O(N)
    def binarySearch(lis, val):
        left = 0
        right = len(lis) - 1
        while left < right:
            mid = (left + right) // 2
            if val > lis[mid]:  # If greater than mid, then position is definitely not mid
                left = mid + 1
            elif val < lis[mid]:    # If less than mid, mid could also be its position, so don't mid - 1
                right = mid         # For ex: If mid - 1 is less than val, then mid is the position
            else:
                return mid
        return left

    lis = [nums[0]]
    for i in range(1, len(nums)):
        if lis[-1] < nums[i]:   # If greater than last element add to lis
            lis.append(nums[i])
        else:
            # Do Binary Search and overwrite nums[i] in approprite position
            index = binarySearch(lis, nums[i])
            lis[index] = nums[i]
    return len(lis)