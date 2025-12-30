# Brute Force: DFS from each node to calculate the height rooted at that node. 
# For each node, initialize height to 1 (leaf), and for each neighbor (excluding the parent to avoid cycles),
# Call the DFS function and add 1 to the returned height to account for the edge to the neighbor.
# Keep track of the maximum height encountered among all neighbors to determine the height of the tree rooted at the current node.
# After calculating heights for all nodes, find the minimum height among them.
# Time Complexity: O(V * (V + E)), where V is the number of vertices (nodes) and E is the number of edges.
# Space Complexity: O(V + E) for the adjacency list.
def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
    adj = [[] for _ in range(n)]
    heights = [1] * n
    res = []
    for edge in edges:
        adj[edge[0]].append(edge[1])
        adj[edge[1]].append(edge[0])
    def dfs(node, parent):
        height = 1
        for neigh in adj[node]:
            if neigh != parent:
                height = max(height, 1 + dfs(neigh, node))
        return height
    for node in range(n):
        heights[node] = dfs(node, node)
    minHeight = min(heights)
    for node in range(len(heights)):
        if heights[node] == minHeight:
            res.append(node)
    return res

    # Optimal: Finding Centroid using Topological Relaxation for undirected graph
    # Basically, the minimum height trees will be rooted at the centermost nodes.
    # The idea is to trim the leaves level by level until we reach the centermost nodes.
    # These centermost nodes will be the roots of the Minimum Height Trees.
    # Base Case: If there are 2 or fewer nodes, all nodes are centermost.
    # Because, if 2 nodes, both are centermost (edge between them).
    # While popping from the queue, reduce the node count in the graph, as they are removed and edges are relaxed.
    # When edges are being relaxed, it can cause degree to become 0, 
    # but will be only reduced to 0 from 1, so will be added to queue before that happens.
    # Time Complexity: O(V + E)
    # Space Complexity: O(V + E), for adjacency list and degree array.
    degree = [0] * n
    for edge in edges:
        adj[edge[0]].append(edge[1])
        adj[edge[1]].append(edge[0])    # Build adjacency list
        degree[edge[0]] += 1            # Calculate degree of each node
        degree[edge[1]] += 1
    leaf = []
    for node in range(n):       # Add all initial leaves to the queue, leaf nodes have degree 1
        if degree[node] == 1:
            leaf.append(node)
    q = deque(leaf)
    while q:
        if n <= 2:              # If 2 or fewer nodes remain, they are centermost
            return list(q)      # Convert to list and return
        for _ in range(len(q)): # Remove all leaves at current level, before moving to next level
            node = q.popleft()
            n -= 1              # Decrease total node count as we remove this leaf
            for neigh in adj[node]:
                degree[neigh] -= 1      # Relax edge
                if degree[neigh] == 1:  # If neighbor becomes a leaf, add to queue
                    q.append(neigh)