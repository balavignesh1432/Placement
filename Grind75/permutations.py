# We can use backtracking to generate all permutations of the given list
# We maintain a set to keep track of picked indices to avoid picking the same element again
# At each step, we iterate through the list from start to end and pick an element if its index is not in the picked set
# We then add the element to the current permutation and mark its index as picked, adding to set
# Base Case: Once the current permutation length matches the input list length, we add a copy of it to the result
# After exploring that path, we backtrack by removing the last added element and unmarking its index as not picked
# Time Complexity: O(N * N!) where N is the length of the input list
# Because there are N! permutations and generating each permutation takes O(N) time
# Space Complexity: O(N * N!) for storing all permutations in the result list
# Because there are N! permutations and each permutation takes O(N) space

def permute(self, nums: List[int]) -> List[List[int]]:
    res = []
    picked = set()
    def helper(perm):
        if len(perm) == len(nums):
            res.append(perm.copy())
            return
        for index in range(len(nums)):
            if index not in picked:
                picked.add(index)
                perm.append(nums[index])
                helper(perm)
                picked.remove(index)
                perm.pop()
    helper([])
    return res

    # Slight Optimization: Alternative approach using swapping to avoid using extra space for picked set
    # We swap the current index with the iterating index to mark it as picked
    # After adding the element to the current permutation, we call the helper for the next index of current call
    # After exploring that path, we swap back to unmark it
    # Time Complexity: O(N * N!) where N is the length of the input list
    # Space Complexity: O(N * N!) for storing all permutations in the result list
    def helper(index, perm):
        if len(perm) == len(nums):
            res.append(perm.copy())
            return
        for i in range(index, len(nums)):
            perm.append(nums[i])
            nums[index], nums[i] = nums[i], nums[index]
            helper(index + 1, perm)
            nums[index], nums[i] = nums[i], nums[index]
            perm.pop()

    helper(0, [])

    # Further Space Optimization: We can avoid using extra space for current permutation as well
    # We can directly use the nums list to build permutations by swapping elements
    # Base case: When index reached end, we add a copy of the current nums list to the result
    # Time Complexity: O(N * N!) where N is the length of the input list
    # Space Complexity: O(N * N!) for storing all permutations in the result list
    def helper(index, nums):
            if index == len(nums):
                res.append(nums.copy())
                return
            for i in range(index, len(nums)):
                nums[index], nums[i] = nums[i], nums[index]
                helper(index + 1, nums)
                nums[index], nums[i] = nums[i], nums[index]
    helper(0, nums)