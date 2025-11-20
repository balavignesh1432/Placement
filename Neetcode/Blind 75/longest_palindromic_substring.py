def longestPalindrome(self, s: str) -> str:
    # For every substring, check palindrome
    # Use Two pointer method for checking palindrome from ends
    # Keep track of length, if maximum found, update the result
    # TC: O(N^3), SC: O(1)
    # N^2 for substrings, and N for palindrome check
    maxLen = 0
    res = ""
    for i in range(len(s)):
        for j in range(i, len(s)):
            left = i
            right = j
            while left < right and s[left] == s[right]:
                right -= 1
                left += 1
            if left >= right and j - i + 1 >= maxLen:   # If Palindrome, then check if length is bigger
                maxLen = j - i + 1
                res = s[i : j + 1]
    return res

    # Optimal Two Pointers:
    # Instead of moving pointers from ends, start moving from center to outwards for every index
    # Edge Case: There could be even length, so perform from index, as well as index and index + 1
    # Keep track of length, and update result if max length found during equality check inside palindrome
    # TC: O(N^2), SC: O(1)
    # N for indices, N for Palindrome Check
    maxLen = 0
    res = ""
    def isPalindrome(left, right, s):
        while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
            nonlocal res, maxLen
            if right - left + 1 >= maxLen:
                maxLen = right - left + 1
                res = s[left:right+1]
            right += 1
            left -= 1
    for i in range(len(s)):
        isPalindrome(i, i, s)
        isPalindrome(i, i + 1, s)
    return res