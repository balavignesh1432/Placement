def evalRPN(self, tokens: List[str]) -> int:
    # Stack
    # If operand, convert to number and push to stack
    # If operator, pop last two, compute and push to stack
    # Edge Case, if operator is division, floor if positive and ceil if negative to truncate towards zero
    # Return top of the stack
    # TC: O(N), SC:O(N) 
    stack = []
    operators = {"+", "-", "/", "*"}
    for token in tokens:
        if token not in operators:
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            match token:
                case "+": stack.append(a+b)
                case "-": stack.append(a-b)
                case "/": stack.append(math.floor(a/b) if a/b >= 0 else math.ceil(a/b))
                case "*": stack.append(a*b)
    return stack[-1]