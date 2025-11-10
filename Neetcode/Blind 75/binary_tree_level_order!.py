from collections import deque
def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    # BFS = Queue
    # TC = O(N), SC = O(N)
    # Each level create a list, append the nodes to it by deque until length of queue
    # Also append children to q for next level
    q = deque()
    traversal = []
    if not root:    # Check root is None, then empty return
        return traversal
    q.append(root)
    while q:
        level = []  # Each new level
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            # Add children to queue for next iteration, only if valid node
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        traversal.append(level) # Add level to result
    return traversal


    # Recursion = DFS TC = O(N), SC = O(N)
    # Keep parameter depth for indicating level
    # Add the node to level index of result array
    # Call children with next depth
    # But here array size has to be dynamic, use depth parameter for when creating new level
    res = []
    def helper(node, depth):
        if node:
            if len(res) == depth:   # No. of levels is length of res, create new level, when depth increases
                res.append([])
            res[depth].append(node.val) # Now length res will equal for depth for next call
            helper(node.left, depth + 1)    # Call children with increased depth
            helper(node.right, depth + 1)
    helper(root, 0) # Call with depth 0
    return res