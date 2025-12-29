# Balanced means heights difference should not be more than 1
# At each step height comparison is needed, so return height at each step by taking max of left and right
# Base Case: End of tree then return 0
# If not balanced return -1
# If left or right is -1, then tree is not balaced, return -1
# Finally tree is balanced if return value is not -1.
# TC: O(N), SC: O(H) where H is height, will be N if skewed
def isBalanced(self, root: Optional[TreeNode]) -> bool:
    def helper(node):
        if not node:
            return 0
        left = helper(node.left)
        right = helper(node.right)
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        return 1 + max(left, right)
    return True if helper(root) != -1 else False 