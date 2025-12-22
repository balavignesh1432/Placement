def permuteUnique(self, nums: List[int]) -> List[List[int]]:
    # To avoid Duplicates, first sort
    # We can use backtracking to generate all permutations of the given list
    # We maintain a set to keep track of picked indices to avoid picking the same element again
    # At each step, we iterate through the list from start to end and pick an element if its index is not in the picked set
    # We then add the element to the current permutation and mark its index as picked, adding to set
    # For next iteration we move pointer to next unique position, this avoids duplicates.
    # Base Case: Once the current permutation length matches the input list length, we add a copy of it to the result
    # After exploring that path, we backtrack by removing the last added element and unmarking its index as not picked
    # Time Complexity: O(N * N!) where N is the length of the input list
    # Because there are N! permutations and generating each permutation takes O(N) time
    # Space Complexity: O(N * N!) for storing all permutations in the result list
    # Because there are N! permutations and each permutation takes O(N) space
    res = []
    nums.sort()
    taken = set()
    def helper(perm):
        if len(perm) == len(nums):
            res.append(perm.copy())
            return
        i = 0
        while i < len(nums):
            if i not in taken:
                taken.add(i)
                perm.append(nums[i])
                helper(perm)
                perm.pop()
                taken.remove(i)
                while i < len(nums) - 1 and nums[i] == nums[i + 1]: # Technique to move to unique char position
                    i += 1
            i += 1  # Exceuted even after the previous while, ensures pointing to right position.
    helper([])
    return res