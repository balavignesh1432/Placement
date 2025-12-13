def minDistance(self, word1: str, word2: str) -> int:
    # DP - Memoization (Two pointers)
    # Each step, 3 options if char mismatch
    # Depending on action move both pointers
    # Add 1 to each, and return min
    # IF match, then just move both and return (No need to call for other ops if match, will be handled in future)
    # Base case, if word1 reached end, suppose word2 did not, then remaining length is the number of deletes
    # Similarly if word2 reached end, suppose word1 did not, then remaining length is the number of deletes
    # TC: O(M * N), SC: O(M * N)
    dp = {}
    def helper(index1, index2):
        if index2 == len(word2):
            return len(word1) - index1
        if index1 == len(word1):
            return len(word2) - index2
        if (index1, index2) in dp:
            return dp[(index1, index2)]
        if word1[index1] == word2[index2]:
            return helper(index1 + 1, index2 + 1)
        insert = 1 + helper(index1, index2 + 1)
        delete = 1 + helper(index1 + 1, index2)
        replace = 1 + helper(index1 + 1, index2 + 1)
        dp[(index1, index2)] = min(insert, delete, replace)
        return dp[(index1, index2)]
    return helper(0, 0)

    # DP: Tabulation
    # TC: O(M * N), SC: O(M * N)
    dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]
    for index2 in range(len(word2) - 1, -1, -1):
        dp[-1][index2] = len(word2) - index2
    for index1 in range(len(word1) - 1, -1, -1):
        dp[index1][-1] = len(word1) - index1
    for index1 in range(len(word1) - 1, -1, -1):
        for index2 in range(len(word2) -1, -1, -1):
            if word1[index1] == word2[index2]:
                dp[index1][index2] = dp[index1 + 1][index2 + 1]
                continue
            insert = 1 + dp[index1][index2 + 1]
            delete = 1 + dp[index1 + 1][index2]
            replace = 1 + dp[index1 + 1][index2 + 1]
            dp[index1][index2] = min(insert, delete, replace)
    return dp[0][0]

    # Space Optimised DP
    # Min length has to be word 2
    # replace dp[index1 + 1] with dp1
    # Initialise dp1 to base case, 
    # For Base of dp only last value has to be set, so inside the for loop just set for last pos of dp
    # TC: O(M * N), SC: O(min(M, N))
    if len(word1) < len(word2):
        word1, word2 = word2, word1

    dp = [0] * (len(word2) + 1)
    dp1 = [0] * (len(word2) + 1)

    for index2 in range(len(word2) - 1, -1, -1):
        dp1[index2] = len(word2) - index2

    for index1 in range(len(word1) - 1, -1, -1):
        dp[-1] = len(word1) - index1
        for index2 in range(len(word2) -1, -1, -1):
            if word1[index1] == word2[index2]:
                dp[index2] = dp1[index2 + 1]
                continue
            insert = 1 + dp[index2 + 1]
            delete = 1 + dp1[index2]
            replace = 1 + dp1[index2 + 1]
            dp[index2] = min(insert, delete, replace)
        dp, dp1 = dp1, dp
    return dp1[0]