def containsDuplicate(self, nums: List[int]) -> bool:
    # Brute Force - TC O(N^2), SC O(1) 
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[j] == nums[i]:
                return True
    return False

    # Sorting - TC O(NlogN), SC O(1)
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i-1] == nums[i]:
            return True
    return False

    # Using Hash Set- TC O(N), SC O(N)
    return len(nums) != len(set(nums))
