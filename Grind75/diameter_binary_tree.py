# DFS
# At each step, think what to return to parent
# Here max depth of left and right is needed for parent to calculate diameter
# Diameter is left + right depth, Keep track of maximum diameter at each level
# Base Case: If reached end, return 0 as it is the depth
# TC: O(N), SC: O(H)
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