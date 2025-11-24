def missingNumber(self, nums: List[int]) -> int:
    # Store nums in set, Check each number from 0 tot n , is in nums set or not
    # TC: O(N), SC: O(N)
    hashSet = set(nums)
    n = len(nums)
    for i in range(n + 1):
        if i not in hashSet:
            return i

    # Bit Manipulation: 
    # Intuition: Since any number xor with itself is 0,
    # XOR each number with index, Each number will cancel to 0, when its equivalent index is xor somewhere
    # Leaving only the missing number behind
    # Since have to check for [0, n], and nums final index is only n - 1, finally xor with n
    # TC: O(N), SC: O(1) 
    res = nums[0] ^ 0
    n = len(nums)
    for i in range(1, n):
        res = res ^ (nums[i] ^ i)
    return res ^ n