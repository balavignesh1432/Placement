def countSubstrings(self, s: str) -> int:
    # For every substring, check palindrome
    # Use Two pointer method for checking palindrome from ends
    # If Palindrome, update counter
    # TC: O(N^3), SC: O(1)
    # N^2 for substrings, and N for palindrome check
    res = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            left = i
            right = j
            while left < right and s[left] == s[right]:
                right -= 1
                left += 1
            if left >= right:
                res += 1
    return res
    
    # Optimal Two Pointers:
    # Instead of moving pointers from ends, start moving from center to outwards for every index
    # Edge Case: There could be even length, so perform from index, as well as index and index + 1
    # If equality checks, then add to list of palindromes
    # TC: O(N^2), SC: O(1)
    # N for indices, N for Palindrome Check
    res = 0
    def isPalindrome(left, right, s):
        while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
                nonlocal res
                res += 1
                right += 1
                left -= 1
    for i in range(len(s)):
        isPalindrome(i, i, s)
        isPalindrome(i, i + 1, s)
    return res