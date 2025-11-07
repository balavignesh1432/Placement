def isAnagram(self, s: str, t: str) -> bool:
    # Equal when Sorted
    # TC O(nlogn + mlogm), SC O(m+n) or O(1)
    return sorted(s) == sorted(t)
    
    # Using hashing to store frequency
    # TC O(m + n), SC - O(1) as only 26
    sCount  = [0] * 26
    tCount  = [0] * 26
    for letter in s:
        sCount[ord(letter) - ord('a')] += 1
    for letter in t:
        tCount[ord(letter) - ord('a')] += 1
    return sCount == tCount

    # Using hashing to store frequency
    # TC O(m + n), SC - O(1) as only 26
    sCount = {}
    tCount = {}
    for letter in s:
        if letter not in sCount:
            sCount[letter] = 1
        else:
            sCount[letter] += 1
    
    for letter in t:
        if letter not in tCount:
            tCount[letter] = 1
        else:
            tCount[letter] += 1
    return tCount == sCount