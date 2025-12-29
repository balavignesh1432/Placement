def findDuplicate(self, nums: List[int]) -> int:
    # Since numbers are in range [1, n], we can use index marking approach
    # Use 1 indexing (No - 1 shifting of value for index), as the length is n + 1, max value is n
    # So will never be possible to go out of index
    # For each number, mark the index corresponding to that number as negative
    # If we encounter a number whose corresponding index is already negative, 
    # which means some number has pointed to that index before, hence it's a duplicate
    # The number which points to that index is the duplicate number
    # If need to unmodify the array, finally convert all numbers to positive again
    # Time: O(N), Space: O(1)
    for i in range(len(nums)):
        pos = abs(nums[i])
        if nums[pos] < 0:
            return abs(nums[i])
        nums[pos] = -nums[pos]


    # Two Pointer Cycle Start : Fast and Slow (Move and Check)
    # Since 1 index, 0 will never be in array,
    # So first number will not point to itself, even it is 1, then it means index 1 which is 2nd
    # Also there can not be cycle including 0, as no number points to 0
    # Start both slow and fast at 0, move start to nums[start], and fast to nums[fast[fast]]
    # When both fast and slow are equal then they both are meeting,
    # This point could have been that fast passed through slow (was equal to slow on 1 jump), 
    # so they met there, not that it was the duplicate element
    # From the meeting point, move head and meet one at a time, the point where they meet is cycle start
    # which is the duplicate number
    # Important first move and then check, not check and move. 
    # As nums[0] has to compared and not 0
    # TC: O(N), SC: O(1)
    slow = fast = 0
    meet = None
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if fast == slow:
            meet = fast
            break
    slow = 0
    while True:
        meet = nums[meet]
        slow = nums[slow]
        if meet == slow:
            return meet
    