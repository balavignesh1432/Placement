class MinStack(object):
    # Using stack
    # Since minimum so far is needed
    # Add that to the element itself
    # So when popping, if minimum element is popped
    # The top will be having previous min so far
    # When pushing, find min of top and val, and push
    # TC: O(1), SC: O(N)
    
    def __init__(self):
        self.stack = [[None, float('inf')]]

    def push(self, val):
        self.stack.append([val, min(val, self.stack[-1][1])])
    
    def pop(self):
        self.stack.pop()

    def top(self):
        return self.stack[-1][0]

    def getMin(self):
        return self.stack[-1][1]