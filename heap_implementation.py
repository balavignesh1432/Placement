# Heap is complete Binary Tree, except last level full, and last level filled from left side
# Use 1-index parent calculation is easier
# If 1 -indexing, parent is i // 2, or left child at 2 * i, at right child at 2 * i + 1
# Height is ensured as log n, due to complete Binary Tree

class minHeap:
    def __init__(self):
        self.heap = [None]  #  Since first element needs to be at index 1

    # Append to last, and move up by swaps
    # Then compare with parent, if smaller than parent, perform swap
    # Move index to parent, and repeat until condition satisfied or root reached
    # TC: O(log N), Since height is ensured to be log N (Complete Binary Tree)
    def push(self, x: int):
        self.heap.append(x)
        index = len(self.heap) - 1
        # Until root reached or condition fails
        while index > 1 and self.heap[index] < self.heap[index // 2]:
            self.heap[index], self.heap[index//2] = self.heap[index//2], self.heap[index]
            index = index // 2  # Move to Parent
    
    # Swap root with last element and pop last
    # Then move root below by swaps
    # Start from index 1, Compute child indices, Check if children is small, If so
    # See which children is small and swap with it, if only one child (left) swap with it
    # Update index depending on the swap, and update child1 and child2 indices
    # TC: O(log N), Since height is ensured to be log N (Complete Binary Tree)
    def pop(self):
        self.heap[1], self.heap[-1] = self.heap[-1], self.heap[1]
        self.heap.pop()
        index = 1
        child1 = (2 * index)
        child2 = (2 * index) + 1
        while ((child1 < len(self.heap) and self.heap[index] > self.heap[child1]) 
            or (child2 < len(self.heap) and self.heap[index] > self.heap[child2])):
            if child2 >= len(self.heap) or self.heap[child1] < self.heap[child2]:   # If only left child or it is smaller one
                self.heap[index], self.heap[child1] = self.heap[child1], self.heap[index]
                index = child1  # Update index
            else:   # If right child is smaller
                self.heap[index], self.heap[child2] = self.heap[child2], self.heap[index]
                index = child2  # Update index
            child1 = (2 * index)    # Update child indices
            child2 = (2 * index) + 1

    # TC: O(1)
    def peek(self) -> int:
        # Since 0 is None, is length 1 then empty, o/w root at index 1
        return -1 if not len(self.heap) - 1 else self.heap[1]

    def size(self) -> int:
        return len(self.heap) - 1   # Since 0 is None