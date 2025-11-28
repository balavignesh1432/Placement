def isValidBST(self, root: Optional[TreeNode]) -> bool:
    # TC : O(N), SC: O(N)
    # Inorder Traversal of BST, results in sorted order
    # Add values to list, check is list is sorted using pointer
    dfs = []
    def helper(node):
        if node:
            helper(node.left)
            dfs.append(node.val)
            helper(node.right)
    helper(root)        
    for i in range(1, len(dfs)):
        if dfs[i] <= dfs[i-1]:
            return False
    return True

    # We can perform dfs, providing valid range for each node
    # Initially for root node, valid range is -inf to inf
    # If node not in the valid range, return False
    # Only perform dfs for children, if node lies in the valid range
    # Then for node's left, update higher bound, as all elements must be less than it on left
    # Then for node's right, update lower bound, as all elements must be greter than it on the right
    # Base Case when node is null, return True
    # TC: O(N), SC: O(N) - Call Stack
    def helper(node, low, high):
        if not node:
            return True
        if low < node.val < high:
            left = helper(node.left, low, node.val)
            right = helper(node.right, node.val, high)
            return left and right
        return False
    return helper(root, float('-inf'), float('inf'))