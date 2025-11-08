def invertTree(self, root):
    # Recursion - DFS
    # TC = O(N), SC = O(N) Call Stack
    def helper(node):
        if node:
            left = helper(node.left)
            right = helper(node.right)
            node.right = left
            node.left = right
            return node
    return helper(root)

    # BFS Using Queue
    # Add root to queue
    # Keep pop left queue, invert then push children to queue
    # Keep repeating until queue is empty
    # Return root, finally
    # TC = O(N), SC = O(N) for Queue
    q = deque([root])
    while q:
        node = q.popleft()
        if node:
            node.left, node.right = node.right, node.left
            if node.left:   # Only push if valid Node
                q.append(node.left)
            if node.right:  # Only push if valid Node
                q.append(node.right)
    return root

    # Iterative DFS Using Stack
    # Keep popping node, and invert
    # Push children to stack
    # Repeat until stack is empty
    # TC = O(N), SC = O(N) for Stack 
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            node.left, node.right = node.right, node.left
            if node.left:   # Only push if valid Node
                stack.append(node.left)
            if node.right:  # Only push if valid Node
                stack.append(node.right)
    return root
