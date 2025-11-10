def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    # Brute Force = Recursion, TC: O(N), SC: O(H)
    # For Generic Binary Tree, LCA
    # At each step, Call for both left and right,
    # If not None is returned from left and right, then node is the LCA
    # If any one side is not None, then return that side to parent
    # If encounter any of p and q, then return that to parent
    def helper(node, p, q):
        if node:
            if node.val == p.val or node.val == q.val:
                return node
            left = helper(node.left, p, q)
            right = helper(node.right, p, q)
            if left and right:
                return node
            else:
                return left or right
    return helper(root, p, q)


    # TC = O(H), SC = O(H) Call Stack
    # Node Elements are unique.
    # Property of BST, value less than node's val, present on left side, greater than it on right side
    # Recurse from root, Check if bigger and smaller number on other side, then that is the LCA
    # If bigger is less than node, then both must be on the left side, so call only for left side
    # Otherwise call for right side only.
    # Also case when node is equal to one of them, then also return the node itself, as it is the LCA of p and q.
    def helper(node, p, q):
        if node:
                # If min and max on other side then return node
            if p.val < node.val < q.val or node.val == p.val or node.val == q.val: # If node is either of p and q, then also return node
                return node
            elif q.val < node.val:  # Maximum is less than node, then both on left
                return helper(node.left, p, q)
            else:                   # Otherwise both on right
                return helper(node.right, p, q)
    if p.val < q.val:   # Call such that 1st parameter is low, and second is high
        return helper(root, p, q)
    else:
        return helper(root, q, p)

    
    # Iteration : Binary Search with tree
    # Same logic as Recursion, but doing it using iteration, only constant extra space
    # TC: O(H), SC: O(1) 
    node = root
    while node: # Reached end of the tree
        if min(p.val, q.val) > node.val:
            node = node.right
        elif max(p.val, q.val) < node.val:
            node = node.left
        else:   # When both on other side, or when one is equal to node value itself
            return node
    return node 