def printNos(x: int) -> List[int]: 
    def helper(n):
        if n == x:
            return [x]
        return [n] + helper(n + 1)
    return helper(1)
    # TC - O(N), Space - O(N) Stack Space

def sumFirstN(n: int) -> int:
    def helper(x):
        if x == 1:
            return 1
        return x + helper(x - 1)
    return helper(n)
    # TC - O(N), Space - O(N) Stack Space

    return n * (n + 1) // 2
    # TC - O (1)

def factorial(n):
    # Write your code here
    # Print the factorial value.
    def helper(x):
        if x == 1:
            return 1
        return x * helper(x - 1)
    
    # TC - O(N), Space - O(N) Stack Space
    print(helper(n))


def reverseArray(n: int, nums: List[int]) -> List[int]:
    # Two pointers at ends to reverse using swaps
    i = 0
    j = len(nums) - 1
    while i < j:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1
    return nums
    # TC - O(N), Space O(1)

    # Recursion Implementation of iteration
    def helper(i, j):
        if i >= j:
            return
        nums[i], nums[j] = nums[j], nums[i]
        helper(i+1, j - 1)
    helper(0, len(nums) - 1)
    return nums
    # TC - O(N) Space - O(N) Call Stack, O(1) ignoring Call stack

# Check if Palindrome
def isPalindrome(self, s: str) -> bool:
    i = 0
    j = len(s) - 1
    while i < j:
        while i < j and not s[i].isalnum():
            i += 1
        while i < j and not s[j].isalnum():
            j -= 1
        if i < j and s[i].lower() != s[j].lower():
            return False
        i += 1
        j -= 1
    return True
    # TC - O(N), SC - O(1)
    
    # Recursive 
    def helper(i, j):
        while i < j and not s[i].isalnum():
            i += 1
        while i < j and not s[j].isalnum():
            j -= 1
        if i >= j:
            return True
        return s[i].lower() == s[j].lower() and helper(i+1, j-1)
    return helper(0, len(s) - 1)
    # TC - O(N), SC - O(1) [Stack space - N]


# Fibonacci Number
def fib(self, n: int) -> int:
    if n <= 1:
        return n
    
    # Space optimisation - As only two variables needed for calculation
    prev1 = 0
    prev2 = 1
    res = 0
    for _ in range(n-1):
        res = prev1 + prev2
        # Update variable, smaller one (0) with bigger one, and bigger one(1) with prev answer
        prev1 = prev2
        prev2 = res
    return res
    # TC - O(N), SC - O(1)

    def helper(n):
        if n <= 1:
            return n
        return helper(n-1) + helper(n-2)
    return helper(n)
    # TC - O(N), SC - O(1) [Call Stack - N]