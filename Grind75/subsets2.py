def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
    # Sort to avoid duplicates, when adding to set Ex: [1,2,2], and [2,1,2] are same
    # Using Set to avoid duplicates
    # Base Case: When we reach end of array, add current subset to result set
    # TC: O(N * 2^N), SC O(N * 2^N)
    nums.sort()
    res = set()
    def helper(index, sub):
        if index == len(nums):
            res.add(tuple(sub))
            return
        sub.append(nums[index])
        take = helper(index + 1, sub)
        sub.pop()
        notTake = helper(index + 1, sub)
    helper(0, [])
    return [list(sub) for sub in res]


    # Optimized Backtracking - TC O(N * 2^N), SC O(N * 2^N)
    # Sort to handle duplicates
    # IMP: Take the current element, and only while not taking, skip duplicates
    # This ensures that we do not generate same subset again
    # Base Case: When we reach end of array, add current subset to result
    nums.sort()
    res = []
    def helper(index, sub):
        if index == len(nums):
            res.append(sub.copy())
            return
        sub.append(nums[index])
        take = helper(index + 1, sub)
        while index + 1 < len(nums) and nums[index] == nums[index + 1]:
            index += 1
        index += 1
        sub.pop()
        notTake = helper(index, sub)
    helper(0, [])
    return res

    