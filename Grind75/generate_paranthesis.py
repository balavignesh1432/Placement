def generateParenthesis(self, n: int) -> List[str]:
    # Backtracking approach
    # Use a helper function to build the parentheses combinations
    # Keep track of the number of opened and closed parentheses
    # If the number of opened parentheses is less than n, we can add an opening parent
    # Only close if there are more opened than closed parentheses
    # When the number of closed parentheses equals n, add the combination to the result
    # IMP: Use pop on list after each recursive call to backtrack, since lists are mutable
    # Time: O(4^n / sqrt(n)) which is Catalan number Cn
    # Space: O(n) for the recursion stack
    res = []
    def helper(opened, closed, brackets):
        if closed == n:        # All parentheses are closed
            res.append("".join(brackets))
            return
        if opened < n:          # Can open more parentheses
            brackets.append("(")
            helper(opened + 1, closed, brackets)
            brackets.pop()      # Backtrack, remove last added parenthesis
        if closed < opened:     # Cannot close more than opened
            brackets.append(")")
            helper(opened, closed + 1, brackets)
            brackets.pop()      # Backtrack, remove last added parenthesis
    helper(0, 0, [])
    return res