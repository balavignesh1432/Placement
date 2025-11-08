def maxDepth(self, root):
    # DFS Recursion: TC - O(N), SC = O(N)
    # Each call find max of right and left
    # Return it by adding with 1, for its height to its parent
    def helper(node):
        if not node:
            return 0
        return max(helper(node.left), helper(node.right)) + 1
    return helper(root)

    # Iterative DFS
    # TC - O(N), SC = O(N) For Stack
    stack = [[root, 1]]
    maxi = 0
    while stack:
        node, height = stack.pop()
        if node:
            maxi = max(maxi, height)
            if node.left:
                stack.append([node.left, height + 1])
            if node.right:
                stack.append([node.right, height + 1])
    return maxi
            
    # BFS - Using Queue
    # Pop queue, level by level, After each level increase height
    # TC - O(N), SC = O(N)
    q = deque()
    if root:    # Only if root is not None add to Queue
        q.append(root)
    level = 0
    while q:
        for _ in range(len(q)): # For Level by level computation, len(q) will only be executed once
            node = q.popleft()
            if node:
                if node.left:   # Only add non None nodes
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        level += 1  # After one level is completed. Increment counter
    return level