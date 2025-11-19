from collections import deque
def countComponents(self, n: int, edges: List[List[int]]) -> int:
    adjList = [[] for _ in range(n)]
    visited = set()
    # Since undirected graph, both node's adj list needs to be updated
    for edge in edges:
        adjList[edge[0]].append(edge[1])
        adjList[edge[1]].append(edge[0])
    
    # DFS: Mark node visited, Perform Call on all its neighbors
    # Base Case: If node already visited, then return
    # TC: O(V + E), SC: O(V + E) For adjacency List, for only call Stack, Visted set O(V) 
    def dfs(node):
        if node in visited:
            return
        visited.add(node)
        for neigh in adjList[node]:
            dfs(neigh)
    q = deque()

    # BFS: Use queue, Until q is empty pop and mark it visited
    # Add neighbord to Queue only if not already visited 
    # TC: O(V + E), SC: O(V + E) For adjacency List, for only Queue, Visted set O(V) 
    def bfs(node):
        q.append(node)
        while q:
            node = q.popleft()
            visited.add(node)
            for neigh in adjList[node]:
                if neigh not in visited:
                    q.append(neigh)

    components = 0

    # For each node perform dfs or bfs only if not already visited, then increment component counter by 1 
    for node in range(n):
        if node not in visited:
            bfs(node)   # or dfs(node)
            components += 1
    return components

    # Using Disjoint Set, Union Find
    # Perform Union of nodes in each edge
    # Then perform path compression for each node
    # Now, number of unique roots in the list will give the number of components
    # Or the number of nodes, whose parent is itself is also unique root
    # TC: O(V + E) For each edge E Union performed at O(1), For each node N, path compression, O(1) amortized
    # SC: O(V) Only for parent, size lists, No need for adjacency list
    parent = [i for i in range(n)]
    size = [1 for _ in range(n)]
    def findParent(node):
        if parent[node] == node:
            return node
        parent[node] = findParent(parent[node])
        return parent[node]
    
    def unionBySize(u, v):
        pu, pv = findParent(u), findParent(v) 
        if pu == pv:
            return
        if size[pu] <= size[pv]:
            parent[pu] = pv
            size[pv] += size[pu]
        else:
            parent[pv] = pu
            size[pu] += size[pv]
    
    for edge in edges:
        unionBySize(edge[0], edge[1])
    
    
    for node in range(n):
        findParent(node)
    # Count unique roots
    return len(set(parent))

    # Also can use this to count unique roots
    components = 0
    for node in range(n):
        if findParent(node) == node:
            components += 1
    return components