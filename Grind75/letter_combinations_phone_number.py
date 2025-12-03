# Backtracking approach
# Intuition: For each digit, we have multiple letter choices. We explore each choice recursively until we form a complete combination.
# Base Case: When the current index reaches the length of the digits string, we have formed a complete combination.
# Time Complexity: O(3^N) where N is the number of digits.
# Space Complexity: O(N) for the recursion stack.
def letterCombinations(self, digits: str) -> List[str]:
    res = []
    digit = {2: ['a', 'b', 'c'], 3: ['d','e','f'], 4: ['g','h','i'], 5: ['j','k','l'], 6: ['m','n','o'], 7:
    ['p','q','r','s'], 8:['t','u','v'], 9: ['w','x','y','z']}
    def helper(index, comb):
        if index == len(digits):
            res.append("".join(comb))
            return
        number = int(digits[index])
        for letter in digit[number]:
            comb.append(letter)
            helper(index + 1, comb)
            comb.pop()
    helper(0, [])
    return res