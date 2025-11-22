# Sliding Window:
# Intuition: Increment window size, until needed letters are all found
# Then store the window, Only have to think how to move left
# There could be cases where inbetween that window, there could be letters that are repeated,
# But since we need minimum window, we decrease window from left, such that still we have letters needed for t
# We use variables have and need to check if we have enough letters for t or not
# We use map for storing count of letters in t and s. Store counts of t, and length of t as need
# need says the unique letters needed for t
# So have must be incremented such that, letter must be in t and count of that must be equal
# Only increment when count is equal in t, otherwise it will increment more than needed
# When have and need are equal then there is a match
# Algo: Start the window, then update count of s in window,
# Now check if that character in t, and check if count of that character matches count in t, then we have that letter
# So increment have, check if equal to need, means we have letters for t
# then update length, keep decrementing left until we have neede, while updating window count,
# If count of left in window becomes less than tcount then we dont have that letter for t, so decrement have
# TC: O(N) length of s, SC: O(52) - Only lower and upper case

def minWindow(self, s: str, t: str) -> str:
    tCount = {}
    sCount = {}
    minLength = len(s) + 1
    minWindow = [0, 0]              # To store minimum window that matches 
    for c in t:
        tCount[c] = tCount.get(c, 0) + 1
    need = len(tCount)              # Letters needed for t
    have = 0                        # Letters in s that match count in t
    left = 0                        # Window start marker
    for right in range(len(s)):
        sCount[s[right]] = sCount.get(s[right], 0) + 1  # Update s counter
        if s[right] in tCount and sCount[s[right]] == tCount[s[right]]: # Check if we have 1 letter for t
            have += 1
        while have == need: # We have enough for t, Store window, and Keep moving left 
            if (right - left) + 1 < minLength:  # Update window
                minLength = (right - left) + 1 
                minWindow = [left, right + 1]
            sCount[s[left]] -= 1    # Keep reducing count of left while moving
            if s[left] in tCount and sCount[s[left]] < tCount[s[left]]: # Update if we don't have while moving
                have -= 1
            left += 1
    return s[minWindow[0]:minWindow[1]]