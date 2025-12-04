def widthOfBinaryTree(self, root):
    # BFS approach
    # Assign a position to each node as if it were in a complete binary tree
    # The left child gets position 2 * pos and the right child gets position 2 * pos + 1
    # This way, the width of each level can be calculated using the positions of the first and last nodes
    # Calculate the width at each level and update the maximum width found
    # Base Case: If root is None, return 0
    # Time: O(N) where N is number of nodes in the tree
    # Space: O(N) for the queue
    if not root:
        return 0

    q = deque([[root, 0]])
    maxWidth = 0
    while q:
        width = (q[-1][1] - q[0][1]) + 1
        maxWidth = max(width, maxWidth)
        for _ in range(len(q)):
            node, pos = q.popleft()
            pos = pos << 1      # Multiply position by 2
            if node.left:
                q.append([node.left, pos])
            if node.right:
                q.append([node.right, pos + 1])
    return maxWidth