def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    # BFS
    # Traverse level by level and add the last node's value of each level to the result
    # Use loop for each level to process all nodes at that level
    # TC - O(N), SC - O(N)
    if not root:
        return []
    res = []
    q = deque([root])
    while q:
        res.append(q[-1].val)
        for _ in range(len(q)):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    return res

    # DFS
    # Length of result will be the depth of the tree
    # For each depth, only one will be needed.
    # So use depth to check if we have added a node for that depth
    # Only add the first node we encounter at that depth
    # For that, we visit right child before left child
    # Preorder traversal, visit right child before left child
    # Keep track of depth, if depth equals length of result list, append node value
    # Common technique to write dfs approach for bfs problems is using depth parameter
    #  TC - O(N), SC - O(H) [H - height of tree]
    res = []
    def dfs(node, depth):
        if not node:
            return
        if depth == len(res):   # Ensures only one node per depth is added and it is the rightmost node
            res.append(node.val)
        dfs(node.right, depth + 1)
        dfs(node.left, depth + 1)
    dfs(root, 0)
    return res