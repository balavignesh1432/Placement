def characterReplacement(self, s: str, k: int) -> int:
    # Brute Force: Check every possible window
    # Use window size and max frequency of character to find replacements needed
    # If that lies within K, calculate length of window, and MaxLen
    # For Calculating MaxFrequency use Map, or Freq array (Only Uppercase)
    # TC: O(N*2), SC: O(26)
    maxLen = 0
    for i in range(len(s)):
        count, maxCount = defaultdict(int), 0   # New Map, and max counter for each window
        for j in range(i, len(s)):
            count[s[j]] += 1            
            maxCount = max(maxCount, count[s[j]])   # MaxCount of the window
            if (j - i + 1) - maxCount <= k: # If Valid Window, calculate len, track max
                maxLen = max(maxLen, j - i + 1)
    return maxLen
    
    
    # Sliding Window Intuition: Keep window size that only satisfies K replacement condition
    # Need to keep track of count of most frequent within the window,
    # Length of the window - maxFreq gives the replacement needed to be done
    # If this exceeds K, keep moving left, and updating count until the condition is satisfied
    # Calculate max Length that is length of the window once valid.
    # For count use Map, or Freq array since only 26 characters
    # TC: O(26 * N), SC: O(26)
    i = 0
    j = 0
    count = [0] * 26
    maxLen = maxCount = 0
    while j < len(s):
        index = ord(s[j]) - ord("A")
        count[index] += 1
        maxCount = max(count)
        while (j - i + 1) - maxCount  > k:
            index = ord(s[i]) - ord("A")
            count[index] -= 1
            maxCount = max(count)
            i += 1
        maxLen = max(maxLen, (j - i) + 1)
        j += 1
    return maxLen


    # Slight Optimisation: 
    # Avoiding repeated computation of maxCount as while moving left, maxCount reduces
    # But we get bigger or better maxLen, when maxCount increases
    # So only keep track of it when it increases, this is enough for MaxLen to be correct
    # TC: O(N), SC: O(26)
    i = 0
    j = 0
    count = [0] * 26
    maxLen = maxCount = 0
    while j < len(s):
        index = ord(s[j]) - ord("A")
        count[index] += 1
        maxCount = max(maxCount, count[index])
        while (j - i + 1) - maxCount  > k:
            index = ord(s[i]) - ord("A")
            count[index] -= 1
            i += 1
        maxLen = max(maxLen, (j - i) + 1)
        j += 1
    return maxLen