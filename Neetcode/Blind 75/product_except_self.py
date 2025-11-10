def productExceptSelf(self, nums: List[int]) -> List[int]:
    # Computing Prefix and Suffix Products
    # Then multiplying prefix[i-1] and suffix[i+1] to get answer
    # Edge Cases: Only for first 1 * suffix[i+1], and for last 1 * prefix[i-1]
    # TC = O(N), SC = O(N) Extra Space for Storing other than result
    prefix = [1] * len(nums)
    prefix[0] = nums[0]
    for i in range(1, len(nums)):   # Prefix Product
        prefix[i] = prefix[i - 1] * nums[i]

    suffix = [1] * len(nums)
    suffix[-1] = nums[-1]
    for i in range(len(nums) - 2, -1, -1):  # Suffix Product
        suffix[i] = suffix[i+1] * nums[i]

    res = [1] * len(nums)
    res[0], res[-1] = suffix[1], prefix[-2] # Edge Cases
    for i in range(1, len(nums) - 1):   
        res [i] = prefix[i - 1] * suffix[i + 1] # Logic for multiplying prefix and suffix
    return res

    # Modified Computing Prefix Products, and using it as result array
    # Iterate from last and multiply prefix[i-1] and product so far on the right of i
    # Edge Cases: Only for first 1 * product so far on right, and for last 1*prefix[i-1]
    # TC = O(N), SC = O(1) No Extra Space for Storing other than result array
    prefix = [1] * len(nums)
    prefix[0] = nums[0]
    for i in range(1, len(nums)):
        prefix[i] = prefix[i - 1] * nums[i]

    prod = 1
    for i in range(len(nums) - 1, 0, -1):   # Iterate from last and compute prod so far
        prefix[i] = prod * prefix[i-1]  # Compute res for index before calculating prod so far
        prod *= nums[i]     # Update prod so far
    prefix[0] = prod    # For First position, just prod so far * 1
    return prefix