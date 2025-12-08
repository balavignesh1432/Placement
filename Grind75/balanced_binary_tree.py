def isBalanced(self, root: Optional[TreeNode]) -> bool:
    def helper(node):
        if not node:
            return 0
        left = helper(node.left)
        right = helper(node.right)
        if left == - 1 or right == -1 or abs(left - right) > 1:
            return -1
        return 1 + max(left, right)
    return True if helper(root) != -1 else False 