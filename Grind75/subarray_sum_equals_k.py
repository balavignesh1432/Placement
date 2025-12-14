def subarraySum(self, nums: List[int], k: int) -> int:
    # Brute Force: Compute Every sub array sum, count when equals K
    # TC: O(N^2), SC: O(1)
    
    # Prefix Sum: Effectively turns into two sum
    # Since sum[a:b] = sum[:b] - sum[:a]
    # So all we need to do is find how many subarrays with sum[:b] - target is previously available
    # That many complement subSum will be available for ending at b, so increment counter by that value
    # store prefixSum into map with count incremented by 1, if already exists, o/w 1
    # Edge Case: Initially, add 0 with count 1, think when first element is the target
    # TC: O(N), SC: O(N)
    count = 0
    subCount = {0: 1}
    prefixSum = 0
    for num in nums:
        prefixSum += num
        if prefixSum - k in subCount:
            count += subCount[prefixSum - k]
        subCount[prefixSum] = subCount.get(prefixSum, 0) + 1
    return count   