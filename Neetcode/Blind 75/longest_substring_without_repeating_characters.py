def lengthOfLongestSubstring(self, s: str) -> int:
    # Brute Force: TC: O(N*2), SC: O(K - Characer Set)
    # For Every Subarray left, create new set, 
    # Iterate right from left if element in set, then break inner loop
    # Whenever moving right in inner loop, keep adding in set, and compute length(len set) and maxLen
    maxLen = 0
    for i in range(len(s)):
        charSet = set()
        for j in range(i, len(s)):
            if s[j] in charSet:
                break
            charSet.add(s[j])
        maxLen = max(maxLen, len(charSet))
    return maxLen


    # Using HashMap, and two pointers: TC O(N), SC: O(K)
    # Init both pointers at start
    # If element not in hashmap, add element and index to hashmap
    # Compute length as right - left + 1, and MaxLen
    # If element in hashMap, Move left until after the index of the element( val of Map)
    # While moving left, keep deleting from left from hashMap
    # This ensures that only elements in the window are in hashMap
    # Do this until right reaches end
    left = right = 0
    maxLen = 0
    hashMap = {}
    while right < len(s):
        if s[right] not in hashMap:
            length = (right - left)  + 1
            maxLen = max(length, maxLen)
        else:
            index = hashMap[s[right]]
            while left <= index:
                del hashMap[s[left]]
                left += 1
        hashMap[s[right]] = right
        right += 1
    return maxLen

    # Using HashSet, and two pointers: TC O(N), SC: O(K)
    # Can Also use Set to implement above logic,
    # We only needed map for deleting point left
    # Rather delete left from set until the repeated character is removed from set
    # This ensures only elements within window are in the set
    hashSet = set()
    left = 0
    maxLen = 0
    while right < len(s):
        while s[right] in hashSet:
            hashSet.remove(s[left])
            left += 1   # Update window and Set
        hashSet.add(s[right])
        maxLen = max(maxLen, (right - left) + 1)
    return maxLen
