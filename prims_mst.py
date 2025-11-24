# Only works on connected graph, not on disconnected components
# Preferred when graph is dense
from heapq import heappush, heappop
class Solution:
    # Idea: Start from 0th vertex, add to heap with weight 0, node 0, parent as -1
    # Until the heap is empty, pop from it
    # Check if visited, if so continue, otherwise
    # Add weight to sum, and mark it visited, and add node and parent to mst set
    # Get all the edges for that node, is not visited neighbor, then
    # add to heap with weights first, neigh as second, node as third (Parent)
    # Finally return sum which is minimum sum, and remove -1, 0 from mst set, this set contains mst edges
    # TC: O(E log E), SC: O(V + E)
    # Heap can run for all edges, so E and for pop log E
    # Other E log E is, iterating through edges totally runs for E, and heappush is log E
    def spanningTree(self, V, edges):
        heap = []
        adj = [[] for _ in range(V)]
        for edge in edges:
            u = edge[0]
            v = edge[1]
            w = edge[2]
            adj[u].append([v, w])
            adj[v].append([u, w])
        visited = [0 for _ in range(V)]
        heappush(heap, [0, 0, -1])  # Intially start with weight 0, node 0, and parent -1
        mst_sum = 0
        mst = set()
        while len(heap) > 0:
            wt, node, parent = heappop(heap) 
            if visited[node]:   # Node has to be outside MST to include the edge
                continue
            mst_sum += wt
            mst.add((parent, node))
            visited[node] = 1   # Node is added to MST
            for neigh, weight in adj[node]:
                if not visited[neigh]:
                    heappush(heap, [weight, neigh, node])
        mst.remove((-1, 0))
        print(mst)
        return mst_sum