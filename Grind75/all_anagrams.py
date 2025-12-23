def findAnagrams(self, s: str, p: str) -> List[int]:
    # Sliding Window + Map
    # Technique of Map equality in sliding window, using have and need counter 
    # Find the count of p counter map, distinct letters, it will be need value
    # Intuition: Whenever character in s has same count as p, increment have counter.
    # If have and need are equal, means map is equal. So add to result
    # Use left pointer for start of window, initially 0
    # Until p length, just add right to map, increment map counter
    # If window size exceeds, then left has to be incremented.
    # But before increment if it had count equal to p, then have has to be reduced
    # And then its count will be reduced
    # Add left to the result index finally, if there is match(anagram)
    # TC: O(N), SC: O(K), K - Distinct characters in p. (26 in case of only lowercase)
    pCount = {}
    for c in p:
        pCount[c] = pCount.get(c, 0) + 1

    need = len(pCount)
    have = 0
    sCount = {}
    res = []
    left = 0
    for i in range(len(s)):
        sCount[s[i]] = sCount.get(s[i], 0) + 1
        if s[i] in pCount and sCount[s[i]] == pCount[s[i]]:
            have += 1
        if i >= len(p):
            if s[left] in pCount and sCount[s[left]] == pCount[s[left]]:
                have -= 1 
            sCount[s[left]] -= 1
            left += 1
        if have == need:
            res.append(left)
    return res