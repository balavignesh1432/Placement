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