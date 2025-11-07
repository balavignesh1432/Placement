# Check if Palindrome
def isPalindrome(self, s: str) -> bool:
    # Reversing String
    # TC - O(N), SC - O(N)
    string = ""
    for c in s:
        if c.isalnum():
            string += c.lower()
    return string == string[::-1]

    # Two pointers at end, move towards each if match 
    i = 0
    j = len(s) - 1
    while i < j:
        # Skipping non alphanumeric characters
        while i < j and not s[i].isalnum(): 
            i += 1
        while i < j and not s[j].isalnum():
            j -= 1
        if i < j and s[i].lower() != s[j].lower(): # If no match, stop then
            return False
        i += 1
        j -= 1
    return True
    # TC - O(N), SC - O(1)
    
    # Recursive 
    def helper(i, j):
        # Skipping non alpha numeric characters
        while i < j and not s[i].isalnum():
            i += 1
        while i < j and not s[j].isalnum():
            j -= 1
        if i >= j:  # Base case, if pointers crossed then palindrome
            return True
        # And operation because each subproblem must be palindrome
        return s[i].lower() == s[j].lower() and helper(i+1, j-1)   
    return helper(0, len(s) - 1)
    # TC - O(N), SC - O(1) [Stack space - N]