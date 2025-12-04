def sortColors(self, nums: List[int]) -> None:
    # Simple sort approach
    # Time: O(N log N) where N is the length of the array
    # Space: O(1) since we are sorting in place
    nums.sort()

    # Counting sort approach
    # Count the number of 0s, 1s, and 2s
    # Rewrite the array based on the counts
    # Time: O(N) where N is the length of the array
    # Space: O(1) since we are sorting in place    
    count0 = count1 = 0
    for num in nums:
        if num == 0:
            count0 += 1
        elif num == 1:
            count1 += 1
    # Rewrite the array based on counts
    i = 0
    while i < count0:
        nums[i] = 0
        i += 1
    while i < count0 + count1:
        nums[i] = 1
        i += 1
    while i < len(nums):
        nums[i] = 2
        i += 1

    
    # Use two pointers from end to sort in one pass
    # Pointer 'zero' to track the position to place 0s
    # Pointer 'two' to track the position to place 2s
    # Pointer 'i' to traverse the array
    # When nums[i] is 0, swap with nums[zero], Then move zero until it points to a non-0
    # i is updated to zero since everything before zero is sorted
    # When nums[i] is 2, swap with nums[two], Then move two until it points to a non-2
    # When nums[i] is 1, just move i forward
    # Time: O(N) where N is the length of the array
    # Space: O(1) since we are sorting in place
    zero = i = 0
    two = len(nums) - 1
    while i <= two:                                     # Traverse until i crosses two
        if nums[i] == 0:                                # If current number is 0
            nums[zero], nums[i] = nums[i], nums[zero]   # Swap with the position of zero
            while zero < len(nums) and nums[zero] == 0: # Move zero to the right until it points to a non-0
                zero += 1
            i = zero                                    # Update i to zero since everything before zero is sorted 0s
        elif nums[i] == 2:                              # If current number is 2
            nums[two], nums[i] = nums[i], nums[two]     # Swap with the position of two
            while two >= 0 and nums[two] == 2:          # Move two to the left until it points to a non-2   
                two -= 1
        else:                                           # If current number is 1
            i += 1                                      # Just move i forward      