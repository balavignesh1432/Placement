def majorityElement(self, nums: List[int]) -> int:
    # Use Hashmap, and count frequency
    # Return the element with more than half times frequency
    # TC: O(N), SC: O(N)
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1
        if count[num] > len(nums)//2:
            return num

    # Using counting technique: Moore's Voting
    # Intuition: Majority element count will be atleast 1, if other elements deduct its count
    # Assume first element is majority, then iterate if same as majority increment count
    # If not decrement count
    # If count becomes 0, assign the current as majority with count 1
    # TC: O(N), SC: O(1) 
    majority = nums[0] 
    count = 0
    for num in nums:
        if num == majority:
            count += 1
        else:
            count -= 1
        if count == 0:
            majority = num
            count = 1
    return majority