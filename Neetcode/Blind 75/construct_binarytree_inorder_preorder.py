def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    # Intuition: First node of preorder gives root
    # Find the root in inorder, all elements in inorder to the left of it belongs to left of the node
    # And all elements to the right of root in inorder belongs to the right of the node
    # In each step, finding the root in inorder for the range and recursively call with updated root for left and right
    # For left, next of root index in preorder will be new root 
    # For right, root index + (position of root in inorder - left index of inorder) + 1 will be the root
    # Base Case, if range is only one, create node and return
    # If not valid range for inorder, return None
    # TC: O(N*2) For Lookup in inorder N, SC: O(N) For Call Stack
    def helper(rootIndex, left, right):
        if left == right:
            return TreeNode(inorder[left])
        if left > right:
            return None
        root = preorder[rootIndex]
        node = TreeNode(root)
        for i in range(left, right + 1):
            if inorder[i] == root:
                node.left = helper(rootIndex + 1, left, i - 1)
                node.right = helper(rootIndex + (i - left) + 1, i + 1, right)
                return node
    return helper(0, 0, len(preorder) - 1)

    # Optimised Recursion: Using Map for O(1) lookup in inorder for root, instead of loop
    # TC: O(N), SC: O(N) For Call Stack and Map
    indexMap = {inorder[index]: index for index in range(len(inorder)) }
    def helper(rootIndex, left, right):
        if left == right:
            return TreeNode(inorder[left])
        if left > right:
            return None
        root = preorder[rootIndex]
        node = TreeNode(root)
        i = indexMap[root]
        node.left = helper(rootIndex + 1, left, i - 1)
        node.right = helper(rootIndex + (i - left) + 1, i + 1, right)
        return node
    return helper(0, 0, len(preorder) - 1)