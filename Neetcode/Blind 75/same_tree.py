def isSameTree(self, p, q):
    # Recursion DFS
    # TC = O(N), SC = O(N)
    # At each call, compare equality of value, left, right
    # Perform and of all 3
    # Base case: If both None, return True to parent, 
    # But if one is not, then return False 
    def helper(node1, node2):
        if not node1 and not node2:
            return True
        if not node1 or not node2:
            return False
        return node1.val == node2.val and helper(node1.left, node2.left) and helper(node1.right, node2.right)
    return helper(p, q)

    # Iterative DFS
    # TC = O(N), SC = O(N)
    # In each iteration only look cases to return False. 
    # Other wise proceed with iteration by pushing children to stack.
    # Finally return True
    stack = []
    stack.append([p,q]) # Push both roots to stack
    while stack:
        node1, node2 = stack.pop()
        if node1 and node2: # Only proceed if both are valid nodes
            if node1.val == node2.val:  
                stack.append([node1.right, node2.right])    # Preorder Traversal so right first append (VLR)
                stack.append([node1.left, node2.left])
            else:   # If value not equal, can return False
                return False
        elif not node1 and not node2:   # If both nodes are none, continue with other nodes in stack
            continue    # Don't return True. Need to run for all nodes
        else:   # If one is none and other not, then False
            return False
    return True # If after running for all nodes, then return True