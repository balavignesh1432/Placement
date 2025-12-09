def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    diameter = 0
    def helper(node):
        if not node:
            return 0
        left = helper(node.left)
        right = helper(node.right)
        nonlocal diameter
        diameter = max(diameter, left + right)
        return max(left, right) + 1
    helper(root)
    return diameter