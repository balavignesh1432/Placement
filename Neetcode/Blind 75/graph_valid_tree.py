from collections import deque
def validTree(self, n: int, edges: List[List[int]]) -> bool:
    # For Tree, There should be only one connected component
    # There should not be a cycle present
    # So perform dfs for cycle detection with initial node only once, 
    # Since undirected graph, parent node should not be called as it will say cycle
    # So only call for neighbors that is not parent of the current node, use extra parameter
    # If at the end, there is still some node not visited, then it is not tree.
    # For cycle detection use path set, add to path set before calling neighbors
    # If any neighbor calls return True, return True
    # There is no need for removing from set after calling neighbors and using another set for presence
    # Since there will not be case of X structure in directed graph, where center will be visited twice.
    # Base Case: If node in path, return True (Cycle Exists)
    # TC: O(V + E), SC: O(V + E) For Adj List, for Call Stack and Set O(V)
    adjList = [[] for _ in range(n)]
    for edge in edges:
        adjList[edge[0]].append(edge[1])
        adjList[edge[1]].append(edge[0])
    path = set()
    def dfs(node, parent):  # Check Cycle Exists
        if node in path:
            return True
        path.add(node)      # Only addition to the set is enough, no need to remove after dfs
        for neigh in adjList[node]:
            if neigh != parent and dfs(neigh, node): # Only call for not parent neighbors
                return True
        return False

    # BFS Implementation
    # TC: O(V + E), SC: O(V + E) For Adj List, for Queue and Path Set O(V)
    q = deque()
    def bfs(node, parent):
        q.append([node, parent])
        while q:
            [node, parent] = q.popleft()    # Pop from queue, until empty
            if node in path:    # If node already in path, cycle exists
                return True
            path.add(node)      # Add node to path and explore neighbors
            for neigh in adjList[node]: 
                if neigh != parent:     # Only add neigh that are not parent of the node
                    q.append([neigh, node]) # Parent for next iterations, is current node
        return False

    if dfs(0, None):    # Only call with starting node, check cycle
        return False
    if len(path) != n:   # If all nodes not visited, then disconnected graph
        return False
    return True    # Valid Tree


    # Disjoint Set Union Find
    # If during union operation, if ultimate parent is already same for both nodes,
    # Then that means there already exists a path between them via the parent, and thus a cycle is detected
    # Perform union for all edges, then perform path compression for all nodes
    # Then check if there is only one unique root for all nodes.
    # If so, there is only one connected component, return True, else False
    # TC: O(V + E), SC: O(V) for parent, size lists
    parent = [i for i in range(n)]
    size = [1 for _ in range(n)]
    components = n
    def findParent(node):
        if parent[node] == node:
            return node
        parent[node] = findParent(parent[node])
        return parent[node]
    
    def unionBySize(u, v):
        pu, pv = findParent(u), findParent(v)
        # If same ultimate parent exists for both nodes, 
        # Then already there is a path between u and v, which is via the common ultimate parent
        # So loop will be present if new edge is coming between two already connected nodes, so cycle 
        if pu == pv:    
            return True
        nonlocal components
        components -= 1
        if size[pu] <= size[pv]:
            parent[pu] = pv
            size[pv] += size[pu]
        else:
            parent[pv] = pu
            size[pu] += size[pv]    
        return False

    for edge in edges:
        if unionBySize(edge[0], edge[1]): # IF cycle detected, return False
            return False
    
    return components == 1 # Only one component, then tree
    
    # Or Perform path compression for all nodes
    for vertex in range(n):         
        findParent(vertex)
    
    # Check only one unique root, meaning only one component
    root = parent[0]
    for item in parent:
        if item != root:
            return False
    return True
    # Or Use Set and Length
    return len(set(parent)) == 1