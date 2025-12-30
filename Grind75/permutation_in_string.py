def checkInclusion(self, s1: str, s2: str) -> bool:
    # Sliding Window + HashMap Equality Check
    # Maintain window count map of s2, where window size is equal to size of s1
    # Check equality of s1 count and window map, using have and need counter
    # After adding check equality, if so increase have counter
    # If window shrinks, then check for equality before removing, if so decrease have counter
    # At the end, check if we have all needed, if so return True, else False
    # TC: O(N * 26), SC: (26) Only lowercase letters
    count = {}
    for c in s1:
        count[c] = count.get(c, 0) + 1
    need = len(count)
    left = 0 
    have = 0
    window = {}
    for i in range(len(s2)):
        window[s2[i]] = window.get(s2[i], 0) + 1
        if s2[i] in count and count[s2[i]] == window[s2[i]]:
            have += 1
        if i >= len(s1):
            if s2[left] in count and count[s2[left]] == window[s2[left]]:
                have -= 1
            window[s2[left]] -= 1
            left += 1
        if have == need:
            return True
    return False