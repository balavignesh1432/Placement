def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
    # DFS approach
    # End to End path sum
    # Base Case: If leaf node and path sum equals target, add path to result
    # Explore left and right subtrees, keeping track of the current path and path sum
    # IMP: Append to path before exploring, Pop the last node from path after exploring both subtrees
    # Time: O(N) where N is number of nodes in the tree
    # Space: O(H) where H is height of the tree for the recursion stack
    res = []
    def dfs(node, path, pathSum):
        if node:
            if not node.left and not node.right and pathSum + node.val == targetSum:
                res.append(path + [node.val])
                return
            path.append(node.val)
            dfs(node.left, path, pathSum + node.val)
            dfs(node.right, path, pathSum + node.val)
            path.pop()
    dfs(root, [], 0)
    return res