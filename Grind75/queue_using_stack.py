# Implementing Queue using two Stacks
# Add to stack1 on push
# On pop/peek, transfer all elements to stack2, perform operation, transfer back to stack1
# Time Complexity: O(1) for push, O(N) for pop and peek
# Space Complexity: O(N) for the two stacks

class MyQueue:  
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        front = self.stack2.pop()
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        return front
    
    def peek(self) -> int:
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        front = self.stack2[-1]
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        return front

    def empty(self) -> bool:
        return len(self.stack1) == 0


# Optimized Version: 
# Always push to stack1, Always pop/peek from stack2
# If stack2 is empty during pop/peek, transfer all elements from stack1 to stack2
# Stack2 will have elements in reverse order, so popping from stack2 gives correct queue order
# Keep adding to stack1 with stack2 containing elements in reverse order
# During pop/peek, only transfer all elements from stack1 to stack2 if stack2 is empty
# This way any element is moved only at most once between the stacks
# Amortized Time Complexity: O(1) for all operations
# Space Complexity: O(N) for the two stacks
# Each element is pushed into stack1 once.
# Each element is transferred to stack2 at most once.
# Each element is popped from stack2 once.
# 3 operations per element → constant.
class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        if not self.stack2:       
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()
    
    def peek(self) -> int:
        if not self.stack2:       
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

    def empty(self) -> bool:
        return not self.stack1 and not self.stack2