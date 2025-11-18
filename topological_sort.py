from collections import deque
# Topological Sorting: Linear Ordering of Vertices in Directed Acyclic Graph
# Used for dependency, scheduling tasks, precedence constraints, Detecting Cycles in directed Graph
# x -> y, then x y is linear order
class Solution:
    def topoSort(self, V, edges):
        # DFS: Intuition all outgoing neighbors have to be in order before current node
        # For each vertex, call with all its outgoing neighbor, 
        # then after all calls, push vertex to stack
        # Finally pop from stack to get linear order
        # Base Case: Use a visited set to keep track of already visited vertices, if already visited then return
        # TC: O(V+E), Every vertex and edge is visited once atmost, SC: O(V) For Visited Set and Call Stack
        adjList = [[] for _ in range(V)]
        for edge in edges:
            adjList[edge[0]].append(edge[1])
        visited = set()
        stack = []
        def dfs(vertex):
            if vertex in visited:
                return
            visited.add(vertex) # vertex visited
            for neigh in adjList[vertex]:
                dfs(neigh)
            stack.append(vertex)    # Push vertex to stack after visiting all the outgoing neighbors
        for vertex in range(V): # Perform DFS for each vertex
            dfs(vertex)
        return stack[::-1]  # Pop from stack for correct order
        
        # BFS: Kahn's Algorithm Using Indegree
        # First compute indegrees of all vertex
        # Initially, Add indeg 0 vertices to q
        # Until q is empty, pop from it, and add to result
        # For each vertex, reduce the neighbor's indegree by 1.
        # If indegree become 0, add the neighbor to queue, finally return result
        # TC: O(V+E), Every vertex and edge is visited once atmost, SC: O(V) For Indegree list and Queue
        adjList = [[] for _ in range(V)]
        indeg = [0] * V
        q = deque()
        topo = []
        for edge in edges:
            adjList[edge[0]].append(edge[1])
            indeg[edge[1]] += 1
        for vertex in range(len(indeg)):
            if indeg[vertex] == 0:
                q.append(vertex)
        while q:
            vertex = q.popleft()
            topo.append(vertex)
            for neigh in adjList[vertex]:
                indeg[neigh] -= 1
                if indeg[neigh] == 0:
                    q.append(neigh)
        return topo

        # In a graph with a cycle, every node in the cycle has at least one incoming edge, 
        # So those nodes will never reach in-degree = 0.
        # Queue eventually becomes empty before processing all nodes, indicating a cycle.