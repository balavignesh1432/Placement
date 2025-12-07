# Implementing Stack using two Queues
# Push to q1 always
# On pop/top, transfer all elements except last from q1 to q2, perform Pop/top
# Transfer back to q1, so that q1 always has always hass all elements
# Time Complexity: O(1) for push, O(N) for pop and top
# Space Complexity: O(N) for the two queues
class MyStack:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        res =  self.q1.popleft()
        while self.q2:
            self.q1.append(self.q2.popleft())
        return res

    def top(self) -> int:
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        res = self.q1[0]
        self.q2.append(self.q1.popleft())
        while self.q2:
            self.q1.append(self.q2.popleft())
        return res

    def empty(self) -> bool:
        return not self.q1


# Optimized Version:
# Always push to q1. 
# On pop/top, transfer all elements except last from q1 to q2, perform Pop/top
# Swap q1 and q2 references instead of transferring back (Order is identical since queues)
# This way q1 always has all elements after pop/top
# Amortized Time Complexity: O(1) for all operations
# Space Complexity: O(N) for the two queues
class MyStack:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        res =  self.q1.popleft()
        self.q1, self.q2 = self.q2, self.q1
        return res

    def top(self) -> int:
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        res = self.q1[0]
        self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1
        return res

    def empty(self) -> bool:
        return not self.q1