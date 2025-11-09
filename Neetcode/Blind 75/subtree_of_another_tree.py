def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
          
    # For each node in tree, perform same tree problem
    # TC = O(N*M), SC = O(N + M)
    
    if not subRoot: # If subroot is empty, then always True
        return True
    
    # Same tree sub problem for every node in tree
    def isSame(node1, node2):
        if not node1 and not node2:
            return True
        elif node1 and node2:
            return node1.val == node2.val and isSame(node1.left, node2.left) and isSame(node1.right, node2.right)
        else:
            return False

    # Explore every node in tree
    def helper(node1):
        if node1:
            if isSame(node1, subRoot):  # Check same tree
                return True
            else:   # If not same go for children, call helper not isSame
                return helper(node1.left) or helper(node1.right)    # If any side has match return True
        else:
            return False    # If tree end is reached and still no match (only then children called), then False

    return helper(root) 

    # Serialization and Pattern Matching
    # Perform Traversal, and serialize to list or string
    # TC = O(N*M) can be O(M+N) if used algo like KMP, Rabin Karp, Z
    # SC = O(M+N)
    inorderRoot = []
    inorderSubRoot = []
    def dfs(node, option):
        if not node:
            option.append(None)
        else:
            option.append(node.val) # Preorder Traversal
            dfs(node.left, option)
            dfs(node.right, option)
    rootList = []
    subRootList = []
    dfs(root, rootList) # List is passed by reference
    dfs(subRoot, subRootList)
    # Check if subRootList in rootList
    for i in range(len(rootList)):  # Brute Force Pattern Matching for contains, O(N*M), 
        j = 0
        k = i
        while j < len(subRootList) and k < len(rootList):
            if subRootList[j] == rootList[k]:
                j += 1
                k += 1
            else:
                break
        if j == len(subRootList):
            return True
    return False