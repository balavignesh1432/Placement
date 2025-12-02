def subsets(self, nums: List[int]) -> List[List[int]]:
    # Backtracking approach
    # Each element has two choices: either to be included in the current subset or not.
    # Base case: when we reach the end of the list, we add the current subset to the list of subsets.
    # Only unique elements are considered, so no duplicates handling is necessary.
    # Time Complexity: O(N * 2^N), Because there are 2^N subsets and generating each subset takes O(N) time.
    #  Space Complexity: O(N * 2^N)
    subsets = []
    subset = []
    def helper(index):
        if index == len(nums):
            subsets.append(subset.copy())
            return
        subset.append(nums[index])
        take = helper(index + 1)
        subset.pop()
        notTake = helper(index + 1)
    helper(0)
    return subsets


    # Iterative approach
    # Start with an empty subset. Empty set is always a subset.
    # For each number in the input list, we take all existing subsets and add the current number to them to form new subsets.
    # Do not iterate all numbers from beginning for each subset, only add the current number to existing subsets.
    # Time Complexity: O(N * 2^N)
    # Space Complexity: O(N * 2^N)
    subsets = [[]]
    for num in nums:
        for index in range(len(subsets)):
            subsets.append([num] + subsets[index])
    return subsets