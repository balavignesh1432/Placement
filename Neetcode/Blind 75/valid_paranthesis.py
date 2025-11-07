def isValid(self, s: str) -> bool:
    # Stack - Whenever see a close, stack top must be corresponding open
    # TC - O(N), SC - O(N)  
    brackets = {'}': '{', ')':'(', ']':'['} # To find corresponding open bracket
    stack = []
    for b in s:
        if b in brackets:
            if len(stack) and stack[-1] == brackets[b]: # If close bracket
                stack.pop() # Stack pop, penultimate open is at top
            else:
                return False
        else:
            stack.append(b) # Stack push, if open bracket
    return len(stack) == 0


    # Brute Force - Repeatedly remove matching bracket pairs until string is empty
    # TC - O(N*2), SC - O(N)
    prev = None
    while prev != s:    # Keep looping until no change even after removal
        prev = s
        s = s.replace("()", "").replace("{}", "").replace("[]", "") # Each replace O(N)
    return s == ""      # If empty then valid