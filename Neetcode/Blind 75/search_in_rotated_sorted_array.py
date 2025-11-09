def search(self, nums: List[int], target: int) -> int:
    # Brute - TC = O(N), SC = O(1)
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1

    # Binary Search - Since Sorted
    # If right half is sorted and target is in the range of right half (Inclusive of right end), 
    # update left (Choose right half), else update right (Choose left half)
    # If left half is sorted and target is in the range of left half (Inclusive of left end),
    # Choose right half, else choose left half.
    # At each step if middle is target, return index, So condition while l <= r (Window size 1)
    # TC = O(Log N), SC = O(1)
    l = 0
    r = len(nums) - 1
    while l <= r:   # To include middle when equal to target (Size 1)
        mid = (l + r) // 2
        if target == nums[mid]: # Until window size is 1, and if target return, else window invalid in next step
            return mid
        if nums[mid] < nums[r]: # Right half is sorted
            if nums[mid] < target and target <= nums[r]:
                l = mid + 1
            else:
                r = mid - 1
        else:   # Left half is sorted
            if nums[l] <= target and target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
    return -1