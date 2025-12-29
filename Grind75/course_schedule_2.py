def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    # Topological Sort using Kahn's Algorithm (BFS)
    # Build adjacency list and indegree array
    # Initialize queue with all nodes having indegree 0 (Only outgoing edges has to come first)
    # Process nodes in queue, relaxing edges and updating indegree of neighbors
    # If indegree of neighbor becomes 0, add it to queue
    # If cycle exists, return empty array
    # Time Complexity: O(V + E), Space Complexity: O(V + E)
    adj = [[] for _ in range(numCourses)]
    indeg = [0] * numCourses
    for edge in prerequisites:
        adj[edge[1]].append(edge[0])
        indeg[edge[0]] += 1
    q = deque()
    for node in range(numCourses):
        if indeg[node] == 0:
            q.append(node)
    order = []
    while q:
        for _ in range(len(q)):
            node = q.popleft()
            order.append(node)
            for neigh in adj[node]:
                indeg[neigh] -= 1
                if indeg[neigh] == 0:
                    q.append(neigh)
    return order if len(order) == numCourses else []


    # Topological Sort using DFS
    # Use Path Set for Cycle Detection
    # If cycle detected, return empty array
    # Use Visited Set to avoid reprocessing nodes
    # Add to path before exploring neighbors, remove after
    # After fully exploring a node, add it to order list
    # Finally, reverse the order list to get correct topological order
    # Time Complexity: O(V + E), Space Complexity: O(V + E)
    path = set()
    visited = set()
    for edge in prerequisites:
        adj[edge[1]].append(edge[0])
    def dfs(node):
        if node in path:
            return True
        if node in visited:
            return False
        path.add(node)
        for neigh in adj[node]:
            if dfs(neigh):
                return True
        path.remove(node)
        visited.add(node)
        order.append(node)
        return False
    for node in range(numCourses):
        if dfs(node):
            return []
    return order[::-1]