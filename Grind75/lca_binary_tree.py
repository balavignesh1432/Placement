def lowestCommonAncestor(self, root, p, q):
    # DFS Approach
    # If we find either p or q, return that node
    # If both left and right return non-null, current node is LCA.
    # If only one side returns non-null, propagate that non-null value up
    # TC - O(N), SC - O(H) [Call stack space, Max Height of tree]
    def helper(node, p, q):
        if not node or node == p or node == q:
            return node
        left = helper(node.left, p, q)
        right = helper(node.right, p, q)
        return node if left and right else left or right  
    return helper(root, p, q)