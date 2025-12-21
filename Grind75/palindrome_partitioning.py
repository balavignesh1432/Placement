def partition(self, s: str) -> List[List[str]]:
    # Backtracking
    # Each step, either continue or start a partition
    # Check palindrome, only then call for next index
    # Since 2^N options, and each step N for slicing and palindrome check
    # TC: O(N * 2^N), SC: O(2^N * N)
    palindromePartitions =  []
    def backtrack(index, part):
        if index == len(s):
            palindromePartitions.append(part.copy())
            return
        for i in range(index, len(s)):
            substring = s[index: i + 1]
            if substring == substring[::-1]:
                backtrack(i + 1, part + [substring])
    backtrack(0, [])
    return palindromePartitions