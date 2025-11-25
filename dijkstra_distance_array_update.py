# Only works for graphs with non negative weights and no negative cycles
from heapq import heappop, heappush
class Solution:
    # Returns shortest distances from src to all other vertices
    # Initialize distance array with all distances to infinity
    # Initialize distance of soure as in array, and add distance and src node to heap
    # Until heap is empty, pop from it, check if the distance to reach the node, is greater than dist[node]
    # This means that shorter distance is already found, and no point in go to neighbors from this node,
    # As those distance will add to distance needed to reach this node
    # Otherwise, Go to neighbors, and check if edge weight + distance needed is less than dist[neigh],
    # This means shorter distance is found to reach neighbor, so update distance array, and add to heap
    # TC: O(E log V), SC: O(V + E),
    # Since E = V2, for complete graph, log E = log V^2 = 2 log V
    def dijkstra(vertices, edges, source):
        dist = [0x7FFFFFFF for _ in range(vertices)]
        dist[source] = 0
        heap = []
        heappush(heap, [0, source])
        adj = [[] for _ in range(vertices)]
        par = [node for node in range(vertices)]
        for edge in edges:
            adj[edge[0]].append([edge[1], edge[2]])
            adj[edge[1]].append([edge[0], edge[2]])
        while len(heap):
            du, u = heappop(heap)
            if du < dist[u]:
                continue
            for v, dv in adj[u]:
                if du + dv < dist[v]:
                    dist[v] = du + dv
                    par[v] = u          # Can be used to find the path from source to any target
                    heappush(heap, [dist[v], v])
        return dist

    def findPath(src, target, par): # Src is can not be different than one used for algo
        cur = target
        path = []
        while cur != src:       # Until node reaching src
            path.append(cur)    # Add node to path
            cur = par[cur]      # Go to node's parent
        path.append(src)        # Append src to path
        path.reverse()          # Reverse it
        return path
