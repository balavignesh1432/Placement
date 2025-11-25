# For Dynamic Graphs, building from scratch, find can be used at any time
# Can be used for cycle detection in undirected graph, number of components in undirected graph
# Without this, you have to use DFS to check if two nodes belong to same set, which will take O(V + E)
# But with this DS, it can be performed with O(1) amortized TC
# Initially each node is considered independent set
# Then from the edges, union is performed for two nodes
# If two nodes already part of same set, no union will be performed
# Path Compression is performed while finding ultimate parent, to make it amortized O(1) operation
# For each union, find, findParent takes O(1) amortized TC, 
# SC: O(V) for storing ranks, sizes, and parent of each node
class DisjointSet:
    def __init__(self, n: int):
        self.parent = [node for node in range(n)]
        self.rank = [0 for _ in range(n)]       # For Union By Rank
        self.size = [1 for _ in range(n)]       # For Union By Size

    # Finding the ultimate parent recursively
    # Also using memoization like dp such that,
    # also updates all intermediary nodes parent to ultimate parent while backtracking
    # This reduces TC to O(1) from O(log N) height for eventual calls
    def findParent(self, node):
        if self.parent[node] == node:
            return node
        self.parent[node] = self.findParent(self.parent[node])  # Path Compression by modifying also instead of just returning
        return self.parent[node]

    def find(self, u: int, v: int) -> bool:    # To find if both u and v are part of same set
        pu, pv = self.findParent(u), self.findParent(v)
        return pu == pv # If ultimate parents are equal, then belong to same set, otherwise not

    def unionByRank(self, u: int, v: int) -> None:
        pu, pv = self.findParent(u), self.findParent(v)
        if pu == pv:    # If ultimate parents are equal, then no Union needed, belong to same set
            return
        # Connect smaller rank to larger rank (Updating parents), larger rank is unmodified
        if self.rank[pu] < self.rank[pv]:
            self.parent[pu] = pv
        elif self.rank[pv] < self.rank[pu]:
            self.parent[pv] = pu
        else:   # If same rank, connect any to any, increase rank by 1 accordingly
            self.parent[pu] = pv
            self.rank[pv] += 1
    
    def unionBySize(self, u: int, v: int) -> None:
        pu, pv = self.findParent(u), self.findParent(v)
        if pu == pv:    # If ultimate parents are equal, then no Union needed, belong to same set
            return
        # Connect smaller size to larger size (Updating parents), add smaller's size to larger's size
        if self.size[pu] < self.size[pv]:
            self.parent[pu] = pv
            self.size[pv] += self.size[pu]
        else:
            self.parent[pv] = pu
            self.size[pu] += self.size[pv]