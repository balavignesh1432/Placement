def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    # Recursion DP:
    # Check if both characters are equal, if so move both pointers forward, return value will be 1 + return
    # If both characters are not equal, we have to move only one at a time
    # But we have two options for that, so return max of the two call
    # Base Case: When any go out of bounds return 0
    # Use Memoization for avoiding recomputation for same indices
    # TC: O(M * N), SC: O(M * N)
    dp = [[-1] * len(text2) for _ in range(len(text1))]
    def helper(index1, index2):
        if index1 > len(text1) - 1 or index2 > len(text2) - 1:
            return 0
        if dp[index1][index2] != -1:
            return dp[index1][index2]
        if text1[index1] == text2[index2]:  # If equal, move both pointers
            # 1 is added because match, and should be included in length of common subsequence
            dp[index1][index2] = 1 + helper(index1 + 1, index2 + 1) 
        else:                               # If not equal only move 1 pointer at a time, return max
            dp[index1][index2] = max(helper(index1 + 1, index2), helper(index1, index2 + 1))
        return dp[index1][index2]
    return helper(0, 0)
        
    # Iteration DP:
    # TC: O(M * N), SC: O(M * N)
    dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
    for index1 in range(len(text1) - 1, -1, -1):
        for index2 in range(len(text2) - 1, -1, -1):
            if text1[index1] == text2[index2]:
                dp[index1][index2] = 1 + dp[index1 + 1][index2 + 1]
            else:
                dp[index1][index2] = max(dp[index1 + 1][index2], dp[index1][index2 + 1])
    return dp[0][0]