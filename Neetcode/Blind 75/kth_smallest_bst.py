def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    # Recursive DFS: Since inorder Traversal of BST result in ascending Order
    # Go left until not possible, then reduce k by 1
    # Then go right.
    # When K becomes 0, store the value in result variable and return
    # TC: O(N), SC:O(N) Call Stack
    ans = root.val
    def helper(node):
        if node:
            helper(node.left)
            nonlocal k, ans # To modify immutable objects outside the scope
            k -= 1  # Only perform after all node left complete
            if k == 0:  
                ans = node.val  # Store in Variable and Return, No further Calls
                return
            helper(node.right)
    helper(root)
    return ans

    # Iterative 'DFS':
    # Initially keep stack empty, Keep adding node left to stack until None
    # Then pop, and reduce K
    # Then make node as node's right, so that the same is performed again for the node,
    # Do this until stack empty or node is not None (initially stack empty, but node is root), 
    # as when there is no left stack will be empty but still have to look in right
    # TC: O(N), SC:O(N) Stack
    stack = []
    node = root
    while stack or node:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        k -= 1
        if k == 0:
            return node.val
        node = node.right