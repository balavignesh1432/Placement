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
    def dijkstra(self, V, edges, src):
        adj = [[] for _ in range(V)]
        dist = [float('inf') for _ in range(V)]
        dist[src] = 0
        for edge in edges:
            adj[edge[0]].append([edge[1], edge[2]])
            adj[edge[1]].append([edge[0], edge[2]])
        
        heap = []
        heappush(heap, [0, src])
        while len(heap):
            weight, node = heappop(heap)
            if weight > dist[node]:
                continue
            for neigh, d in adj[node]:
                if weight + d < dist[neigh]:
                    dist[neigh] = weight + d
                    heappush(heap, [dist[neigh], neigh])
        return dist
