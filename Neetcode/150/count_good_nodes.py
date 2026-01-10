# Good node, from path to itself there is no node greater than itself.
def goodNodes(self, root: TreeNode) -> int:
    # DFS: Keep global counter
    # At each step, check if pathMaximum is less than node value, if so update good
    # Explore left and right path with updating path maximum
    # Initial call, root and path maximum as negative infinity
    # TC: O(N), SC: O(H)
    good = 0
    def helper(node, pathMax):
        if node:
            if node.val >= pathMax:
                nonlocal good
                good += 1
            helper(node.left, max(pathMax, node.val))
            helper(node.right, max(pathMax, node.val))
    helper(root, float('-inf'))
    return good

    # BFS: Start with root and negative infinity in queue
    # Keeping dequeueing, and check if good node, then update global counter
    # Only add if children exists, and update path maximum as node value
    # TC: O(N), SC: O(H)  
    good = 0
    queue = deque()
    queue.append([root, float('-inf')])
    while queue:
        node, pathMax = queue.popleft()
        if node.val >= pathMax:
            good += 1
        if node.left:
            queue.append([node.left, max(pathMax, node.val)])
        if node.right:
            queue.append([node.right, max(pathMax, node.val)])
    return good
        