def evalRPN(self, tokens: List[str]) -> int:
    # Stack
    # If operand, convert to number and push to stack
    # If operator, pop last two, compute and push to stack
    # Declare operators set for checking if operator or not
    # Edge Case, if operator is division, floor if positive and ceil if negative to truncate towards zero
    # int() converts negative numbers as well correctly
    # Return top of the stack
    # TC: O(N), SC:O(N) 
    stack = []
    operators = {"+", "-", "/", "*"}        # Set
    for token in tokens:
        if token not in operators:
            stack.append(int(token))        # Also converts negative numbers
        else:
            b = stack.pop()
            a = stack.pop()
            match token:            # Switch Case in Python 3.10+
                case "+": stack.append(a+b)
                case "-": stack.append(a-b)
                case "/": stack.append(math.floor(a/b) if a/b >= 0 else math.ceil(a/b))
                case "*": stack.append(a*b)
    return stack[-1]