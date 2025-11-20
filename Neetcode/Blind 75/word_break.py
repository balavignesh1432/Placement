def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    # TC: O(N*2^N), SC: O(N + W*L)
    # At each step, choice to whether extend or not
    # For each choice, checking the slice N, in set 1.
    wordSet = set(wordDict)
    def helper(index):
        if index >= len(s):
            return True 
        for i in range(index, len(s)):
            if s[index: i + 1] in wordSet:
                if helper(i + 1):
                    return True
        return False
    return helper(0)


    # TC: O(W^N * L), SC: O(N)
    # Branching factor W, Depth is N
    # For each choice, checking the slice N, in set 1.
    def helper(index):
        if index >= len(s):
            return True 
        for word in wordDict:
            if ((index + len(word)) <= len(s) and s[index : index + len(word)] == word):
                if helper(index + len(word)):
                    return True
        return False
    return helper(0)
    
    # Recursion DP: Using Set for check word, letter by letter from index
    # If word available, call with i + 1, where i is the pointer for iterating from index
    # If any of the calls return True, return True, o/w False
    # TC: O(N*3), SC: O(N + W*L)
    # Since, For each index, moving index to len results in N*2, and for slicing is N, In set is 1.
    # Space: W*L for set, where w is number of words, and L is avg. length of word
    dp = [-1] * (len(s) + 1)
    wordSet = set(wordDict)
    def helper(index):
        if index >= len(s):
            return True 
        if dp[index] != -1:
            return dp[index]
        for i in range(index, len(s)):
            if s[index: i + 1] in wordSet:
                if helper(i + 1):
                    dp[index] = True
                    return dp[index]
        dp[index] = False
        return dp[index]
    return helper(0)

    # Recursion DP, instead of checking letter by letter in word set,
    # Use word from word list, and check if word length of s from index is equal
    # IF equal, call with index + length.
    # TC: O(N*W*L), SC: O(N)
    # For each index, wordlist is iterated which is W, And For equality Check is L.
    dp = [-1] * (len(s) + 1)
    def helper(index):
        if index >= len(s):
            return True 
        if dp[index] != -1:
            return dp[index]
        for word in wordDict:
            if ((index + len(word)) <= len(s) and s[index : index + len(word)] == word):
                if helper(index + len(word)):
                    dp[index] = True
                    return dp[index]
        dp[index] = False
        return dp[index]
    return helper(0)


    # DP Bottom Up: Tabulation
    # Initialise with False
    # TC: O(N*W*L), SC: O(N)
    # Can not be space optimised, as depends on not next 1 or 2, but entire length
    dp = [False] * (len(s) + 1)
    dp[len(s)] = True
    for index in range(len(s) - 1, -1, -1):
        for word in wordDict:
            if ((index + len(word)) <= len(s) and s[index : index + len(word)] == word):
                if dp[index + len(word)]:
                    dp[index] = True
                    break
        # Since already initialised with False, no write needed for False
    return dp[0]