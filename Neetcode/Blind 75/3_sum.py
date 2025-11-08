def threeSum(self, nums):
    # For every element, problems becomes two sum. 
    # Using Hash like in two sum, for each element
    # To remove duplicates, sort and use tuple as key
    # TC = O(N*2), SC = O(N) for hashSet
    nums.sort()     # For ensuring key consistency while storing result
    triplets = set()
    for i in range(len(nums)):
        target = -1 * nums[i]
        hashSet = set()
        for j in range(i + 1, len(nums)):
            if target - nums[j] in hashSet:
                triplets.add((nums[i], nums[j], target -nums[j]))
            else:
                hashSet.add(nums[j])
    return [list(item) for item in triplets]


    # Sorting and Two Pointers
    # For two sum, it was not best TC.
    # But for 3sum, it is because N logN is better than N*2
    # For every element, problems becomes two sum. 
    # TC - O(N*2), SC - O(M) for storing triplets
    res = []
    i = 0
    nums.sort()
    while i < len(nums):
        # Two pointers from ends
        j = i + 1
        k = len(nums) - 1
        target = -1 * nums[i] # For each target
        while j < k:    # Until valid window
            if nums[j] + nums[k] == target:
                res.append([nums[i], nums[j], nums[k]])
                # There could be multiple match inside, so move both pointers inward
                while j < k and nums[j] == nums[j+1]: # To remove duplicates
                    j += 1
                j += 1
                while j < k and nums[k] == nums[k-1]: # To remove duplicates
                    k -= 1
                k -= 1
            elif nums[j] + nums[k] < target:       # If less, move left pointer
                while j < k and nums[j] == nums[j+1]:   # To remove duplicates
                    j += 1
                j += 1
            else:   # If more than target move right pointer
                while j < k and nums[k] == nums[k-1]:   # To remove duplicates
                    k -= 1
                k -= 1
        while i < len(nums) - 1 and nums[i] == nums[i+1]:   # For next unique element
            i += 1
        i += 1
    return res