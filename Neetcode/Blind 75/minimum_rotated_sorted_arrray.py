def findMin(self, nums):
        
    # Brute Force - O(N), SC = O(1)
    return min(nums)

    # Binary Search - Because already sorted
    # IMP - At least one half will always be sorted, in rotated sorted array
    # Choosing which half is not in sorted, will always contain minimum
    # But choosing whether to include mid for the half or not depends on which half is sorted]
    # If Only left half is sorted, definitely left and middle wont be minimum
    # Minimum will be in right half, So pick right half by setting left as middle + 1
    # But If right half is sorted or both half sorted
    # Set right at middle. (Because if only right sorted, then middle might be minimum)
    # TC = O(N), SC = O(1)
    l = 0
    r = len(nums) - 1
    while l < r:
        m = (l + r) // 2
        if nums[m] < nums[r]: # Check if right half is sorted
            r = m   # If only right half is sorted, mid might be minimum
        else:   # If only Left half sorted, mid wont be minimum
            l = m + 1
    return nums[l]