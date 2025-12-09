def moveZeroes(self, nums: List[int]) -> None:
    # Use left pointer to keep track of next position for non zero element
    # Iterate the array, if non zero put in left pointer place.
    # Then if reached end, iterate left to end filling zeros
    # TC: O(N), SC:O(1)
    left = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[left] = nums[i]
            left += 1
    while left < len(nums):
        nums[left] = 0
        left += 1
    return nums

    # Use left pointer to keep track of next position for non zero element
    # Iterate the array, if non zero swap that left pointer place.
    # This sends non zero to its place, and the zero at left pointer to right
    # TC: O(N), SC: O(1)
    left = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[left] = nums[left], nums[i]
            left += 1
    return nums 