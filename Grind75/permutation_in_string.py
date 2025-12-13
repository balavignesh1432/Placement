def checkInclusion(self, s1: str, s2: str) -> bool:
    # Maintain window count map of s2, where window size is equal to size of s1
    # Check equality of s1 count and window map
    # TC: O(N * 26), SC: (26)
    if len(s1) > len(s2):
        return False
    count = [0] * 26
    def ind(c):
        return ord(c) - ord('a')        
    for c in s1:
        count[ind(c)] += 1
    window = [0] * 26   
    j = 0
    while j < len(s1) - 1:
        window[ind(s2[j])] += 1
        j += 1
    i = 0
    while j < len(s2):
        window[ind(s2[j])] += 1
        j += 1
        if window == count:
            return True
        window[ind(s2[i])] -= 1
        i += 1
    return False