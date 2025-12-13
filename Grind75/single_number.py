def singleNumber(self, nums: List[int]) -> int:
    # Since XOR of two same number is 0
    # And XOR of 0 with number is itself
    # TC: O(N), SC: O(1)
    res = 0
    for num in nums:
        res = res ^ num
    return res