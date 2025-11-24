def countBits(self, n: int) -> List[int]:
    # Brute Force, For each number perform number of 1 bits
    # For each number takes, log N times to find the number of bits
    # TC: O(N log N), SC: O(1)
    res = []
    for i in range(n + 1):
        ones = 0
        while i:
            i = i & (i - 1)
            ones += 1
        res.append(ones)
    return res

    # DP: Using Observation
    # 00
    # 01
    # 10    Basically add 1 to left of 0
    # 11    Basically add 1 to left of 1
    # 100   Basically add 1 to left of 0
    # 101   Basically add 1 to left of 1
    # 110   Basically add 1 to left of 2
    # 111   Basically add 1 to left of 3
    # Each time, from the beginning of list to length of list, add 1, Do this until needed length of list
    # TC: O(N), SC: O(N)
    ones = [0]     # Represents ones in zero,
    while len(ones) <= n:           # Build list until needed length
        for i in range(len(ones)):  # From the beginning of ones list, add 1, each time
            ones.append(1 + ones[i])    
            if len(ones) == n + 1:  # If needed length of list reached, return the list of ones
                break
    return ones