def minSubArrayLen(self, target: int, nums: List[int]) -> int:
    # Sliding Window: Only because all are positive
    # Window can be increased if sum is less than target, and decreased if greater than target.
    # Keep decreasing left until sum is greater than or equal to target, and keep computing minimum inside it
    # Because minimum of length satisfying that property is needed, so put that inside.
    # TC: O(N), SC: O(1)
    left = 0
    subSum = 0
    res = len(nums) + 1
    for i in range(len(nums)):
        subSum += nums[i]
        while subSum >= target:
            res = min(res, i - left + 1)
            subSum -= nums[left]
            left += 1
    return res if res <= len(nums) else 0