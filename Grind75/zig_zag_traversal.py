def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    # BFS approach
    # Traverse level by level using a queue
    # Keep track of depth to determine whether to reverse the level or not
    # If depth is odd, reverse the level before adding to result
    # Base Case: If root is None, return empty list
    # Time: O(N) where N is number of nodes in the tree
    # Space: O(N) for the queue
    if not root:                         
        return []
    q = deque([root])
    depth = 0
    res = []
    while q:
        level = []                      # Store nodes at current level   
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        if depth & 1:                   # If depth is odd, reverse the level
            level.reverse()
        res.append(level)
        depth += 1
    return res