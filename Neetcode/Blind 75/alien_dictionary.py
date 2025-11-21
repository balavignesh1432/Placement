from collections import deque
# Intuition: Ordering of letters need to be found based on comparison of adjacent word in dictionary
# After finding ordering for each pair of letters, Need to find overall ordering.
# Basically if letter is a node, and order is an edge from one to another,
# Then this effectively becomes topological sort problem
# Invalid Ordering Cases to consider: 1. If cycle found, then invalid ordering and return empty
# When larger (suffix) comes before prefix, EX: aa before a, then invalid ordering, return empty 
# When any ordering possible for all letters, then also considered invalid, atleast one ordering needed
# Edge Cases: There could be duplicate edges during construction of graph for same letter combinations, So use set for edges
# If only one word, then that is the order, just return
# TC: O(L + V + E), SC: O(V + E), where is sum of length of all strings needed for vertex and edges construction
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        if len(words) == 1: # Base case only one word, return the word, it contains the order
            return words[0]
        edges = set()
        # Create list of vertices for all letters from all words
        vertices = set([letter for word in words for letter in word])   
        for i in range(len(words) - 1):
            left = words[i]
            right = words[i + 1]
            i = 0
            while i < len(left) and i < len(right):
                if left[i] == right[i]: # Still ordering not found
                    i += 1
                else:
                    edges.add((left[i], right[i]))  # Ordering Found, should not continue further
                    break
            # Edge case when invalid order prefix only has to come before, aa before a
            if i == len(right) and i != len(left):  # Larger can not exhaust before smaller
                return ""
        # When more than one vertex but no edge, any ordering is possible, considered invalid
        if len(edges) == 0 and len(vertices) > 1:   
            return ""
        return "".join(self.topologicalSort(edges, vertices))

    def topologicalSort(self, edges, vertices):     # Kahn's Algo BFS for Topological Sort
        indeg = defaultdict(int)
        adjList = defaultdict(list)
        for edge in edges:
            indeg[edge[1]] += 1
            adjList[edge[0]].append(edge[1])
        q = deque([vertex for vertex in vertices if indeg[vertex] == 0])
        topo = []
        while q:
            node = q.popleft()
            topo.append(node)
            for neigh in adjList[node]:
                indeg[neigh] -= 1
                if indeg[neigh] == 0:
                    q.append(neigh)
        # Cycle Detection, then invalid ordering
        return topo if len(topo) == len(vertices) else []  

    def topologicalSort(self, edges, vertices):     # DFS for Topological Sort
        adjList = defaultdict(list)
        for edge in edges:
            adjList[edge[0]].append(edge[1])
        stack = []
        path = set()    # For detecting cycle
        visited = set() # To decide whether to run dfs, if already visited then no need
        def dfs(vertex):
            if vertex in path:  # Cycle Detection Logic
                return True
            if vertex in visited:   # Since DFS is run for every vertex, to avoid already performed vertices
                return False
            path.add(vertex) 
            for neigh in adjList[vertex]:
                if dfs(neigh):      # If any return True, cycle exists, return True
                    return True
            path.remove(vertex)
            visited.add(vertex)
            stack.append(vertex)
            return False
        for vertex in vertices:
            if dfs(vertex):         # If any call returns true, cycle exists so invalid ordering
                return []
        return stack[::-1]          # Pop from stack for correct ordering