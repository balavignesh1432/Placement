def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    # DFS Intuition: This can be represented by a directed graph
    # Edge from A to B, represent A prerequisite for B
    # Then this effectively turns into cycle detection problem
    # Use set to keep track of nodes in path, if encounter again then loop exists.
    # But remove from path after exploring, Because: Think of X structure of 5 nodes,
    # Center node visited again from other axis path does not mean there is loop.
    # Also use another set, and add node to it after exploring and no loop exists
    # This ensures that node is not explored again
    # TC: O(V + E), SC: O(V + E) storing adjList
    adjList = [[] for _ in range(numCourses)]
    for pre in prerequisites:   # Construct adjacency List for the graph
        adjList[pre[1]].append(pre[0])
    visited = set()  # Set to keep track of nodes already completely explored
    path = set()     # Set to keep track of nodes in the current path, for cycle detection
    def dfs(course): # Returns True if Loop Exists
        if course in path:
            return True
        if course in visited:   # Will be already visited if explored and loop did not exist
            return False
        path.add(course)    # Add node to path
        for adj in adjList[course]:
            if dfs(adj):        # If loop exists, return True
                return True
        path.remove(course)     # Remove node from path, 
        visited.add(course)     # Add node to visited, as it need not be further explored again
        return False
    for course in range(numCourses):
        if dfs(course):         # If cycle exists, then not possible
            return False
    return True     # No Cycle exists, so possible
    
    # Using Topological Sort: In a graph with a cycle, every node in the cycle has at least one incoming edge, 
    # So those nodes will never reach in-degree = 0.
    # If no. of processed nodes in Kahn's algo is equal to total nodes, then no cycle.
    # TC: O(V + E), SC: O(V + E) storing adjList
    adjList = [[] for _ in range(numCourses)]
    indeg = [0] * numCourses
    for edge in prerequisites:   # Construct adjacency List for the graph
        adjList[edge[1]].append(edge[0])
        indeg[edge[0]] += 1
    q = deque()
    for vertex in range(numCourses):
        if indeg[vertex] == 0:
            q.append(vertex)
    visited = 0
    while q:
        vertex = q.popleft()
        visited += 1
        for neigh in adjList[vertex]:
            indeg[neigh] -= 1
            if indeg[neigh] == 0:
                q.append(neigh) 
    return numCourses == visited
        