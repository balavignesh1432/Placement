def longestConsecutive(self, nums: List[int]) -> int:
    # Brute Force: For every number, consider start of the series, keep checking if there is next number
    # Use set to check if there is next number, Keep track of length and return maximum
    # TC: O(N*2), SC: O(N)
    maxLen = 0
    numSet = set(nums)
    for num in nums:
        length, start = 0, num
        while start in numSet:   # Check as long as the num in set
            length += 1 # Increment length as long as it is present in set
            start += 1   # Check next number
        maxLen = max(maxLen, length)
    return maxLen
    
    # Instead of checking next number for every number, only check for numbers that is start of the series
    # This way in worst case, if last iterated element is the start of the series whose length is entire list,
    # Then total visits is N + N, TC: O(N), SC: O(1)
    maxLen = 0
    numSet = set(nums)
    for num in numSet:
        if num - 1 not in numSet:
            start = num
            length = 0
            while start in numSet:
                start += 1
                length += 1
                maxLen = max(maxLen, length)
    return maxLen

    # Using sort, this way consecutive numbers are present nearby, just skip duplicates
    # Using two pointers from start, where one marks the start and other keep tracks of the end of sequence
    # Use the value of start, and end value to calculate length, return the maxLen
    # TC: O(N log N) for Sorting, SC: O(1)
    nums.sort()
    i = 0
    j = i + 1
    maxLen = 0
    while j < len(nums):
        if nums[j] == nums[j - 1] + 1:
            length = (nums[j] - nums[i]) + 1
            maxLen = max(length, maxLength)
            j += 1
        elif nums[j] == nums[j - 1]:
            j += 1
        else:
            i = j
            j = i + 1
    return maxLen