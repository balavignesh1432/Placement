def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
    # For Every node, create copy of the node
    # Call neighbors, creation, then append those to node's neighbords
    # Return cloned node.
    # But since graph is undirected, there can be infinite call, 1 <-> 2, 2 can call 1 again
    # So maintain a hashMap, where key is the node value, and value is the cloned node.
    # So if node val already in hashMap, return the value (cloned node)
    # Else, clone the node, then add that to hasMap BEFORE calling neighbord to prevent infinite recursion
    # The value is node, that will be updated after the assignment before returning (Mutable)
    # TC: O(V + E), SC: O(V), For Call Stack and HashMap
    clonedNodes = {}
    def dfs(node):
        if node.val in clonedNodes:
            return clonedNodes[node.val]
        cloned = Node(node.val, [])
        clonedNodes[node.val] = cloned # Important to add to map, before calling neighbor creation
        for neighbor in node.neighbors:
            cloned.neighbors.append(dfs(neighbor))
        return cloned
    return dfs(node) if node else None

    # BFS - Using Queue
    # TC: O(V + E), SC: O(V), For Call Queue and HashMap
    def bfs(node):
        q = deque()
        q.append(node)  
        clonedNodes[node.val]= Node(node.val)   # Create clone initially, as inside creation is for neighbors only
        while q:
            # Current node who is already cloned, neighbors have to be cloned and updated for it [Access from map finally]
            cur = q.popleft()
            for neighbor in cur.neighbors: # Iterate its neighbors
                if neighbor.val not in clonedNodes: # Check if already cloned
                    q.append(neighbor)  # Only add to queue if not already cloned
                    clonedNodes[neighbor.val] = Node(neighbor.val) # Clone the neighbor, and update map so we know it is already cloned
                # Update the neighbors of the current nodes clone using map
                clonedNodes[cur.val].neighbors.append(clonedNodes[neighbor.val])    # If clone already available for that neighbor just uses it
        return clonedNodes[node.val]
    return bfs(node) if node else None