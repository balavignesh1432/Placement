def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
    # DFS approach
    # Use DFS to find the target node
    # Once found, use a helper function to find all nodes at distance k in its subtree
    # Return k - 1, which is depth needed for parent, to parent calls to find nodes in other subtrees
    # IMP: If distance returned from child is greater than 0, search in the other subtree, value - 1
    # If distance returned is 0, add current node to result
    # Return -1 if target not found in subtree, or if all nodes at distance k have been found
    # Time: O(N) where N is number of nodes in the tree
    # Space: O(H) for the recursion stack

    res = []
    def findK(node, dist):
        if node:
            if dist == 0:               # If distance is 0, add node to result
                res.append(node.val)    
                return
            if dist > 0:
                findK(node.left, dist - 1)
                findK(node.right, dist - 1)
    def findTarget(node):
        if not node:
            return -1
        if node:
            if node.val == target.val:      # Target found
                findK(node, k)
                return k - 1                # Depth for parent
            left = findTarget(node.left)    # Perform Both Calls, as worst case target is at leaf, TC does not change
            right = findTarget(node.right)
            if left > 0:                    # If found in left subtree, then call right subtree
                findK(node.right, left - 1) # Depth for current - 1
                return left - 1
            if right > 0:                   # If found in right subtree, then call left subtree
                findK(node.left, right - 1) # Depth for current - 1
                return right - 1
            if left == 0 or right == 0:
                findK(node, 0)
            return - 1
    findTarget(root)
    return res



    # Graph BFS : Convert to graph by Using parent as neighbor 
    # Build parent map which holds parent of each node
    # This way each node uses 3 neihbors left right and parent
    # Perform BFS from target node, and add nodes at distance k to result
    # TC: O(N), SC: O(N) for parent map and queue and visited set

    parent = {}

    # Step 1: Build parent map
    def dfs(node, par=None):
        if not node:
            return
        parent[node] = par
        dfs(node.left, node)
        dfs(node.right, node)
    dfs(root)
    # Step 2: BFS from target
    q = deque([(target, 0)])
    visited = {target}
    res = []
    while q:
        node, dist = q.popleft()
        if dist == k:
            res.append(node.val)
            continue
        for nei in (node.left, node.right, parent[node]):
            if nei and nei not in visited:
                visited.add(nei)
                q.append((nei, dist + 1))
    return res