# Works on Negative weight graphs, and can detect negative weight cycle (Unlike Dijkstra)
# Algo: Like Dijkstra, have distance array initialised and src index as 0.
# For each edge, check if the distance to reach u, and the weight is less than distance to reach v
# This is similar check like dijkstra, if so update the distance array for v
# For the check, first of all u must be reachable, so check if that is not infinity and then do check
# Since this is not dijkstra, where start with node and min weight edge is picked first, so reachable must be checked first
# Perform this for all edges V - 1 times, since at the worst case there could be V - 1 edges to reach a node from src
# And each time, one relaxation can take place
# To detect negative cycle, at Nth iteration if there is relaxation, then there is negative cycle
# TC: O(V * E), SC: O(V)
def bellmanFord(self, V, edges, src):
    dist = [100000000 for _ in range(V)]
    dist[src] = 0
    par = [node for node in range(V)]
    for i in range(V):  # Perform V - 1 times, for cycle check performing V times
        for u, v, d in edges:
            if dist[u] != 100000000 and dist[u] + d < dist[v]:  # Should be Reachable and Relaxation
                if i == (V - 1):        # Negative Cycle Check
                    return [-1]
                dist[v] = dist[u] + d
                par[v] = u  # For tracing path
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