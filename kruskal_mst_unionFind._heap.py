# FOR MST this is enough to remember
# Works on disconnected Components as well as connected graph
# Faster when graph is sparse (E ≈ V)
from heapq import heappush, heappop, heapify
# Construct MST using Union Find, taking minimum weight edge everytime
# Put edges into heap, then until heap is empty, pop edges from it
# Get two nodes, if both have same parent do not proceed
# Otherwise, add the weight to sum, and the nodes of edge into mst list
# TC: O(E log E), SC: O(E + V)
# E for constructing Disjoint Set, E log E for getting edges in sorted order, log E for heap operations
# Since, E can be at worst V^2 for complete graph, log E = log V^2 = 2 log V
# So Total TC: O(E log V), SC: O(V + E)
class UnionFind:
    def __init__(self, n):
        self.parent = [node for node in range(n)]
        self.size = [1 for _ in range(n)]
    def findParent(self, node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.findParent(self.parent[node])
        return self.parent[node]
        
    def find(self, u, v):
        pu = self.findParent(u)
        pv = self.findParent(v)
        return pu == pv
    
    def union(self, u, v):
        pu = self.findParent(u)
        pv = self.findParent(v)
        if self.size[pu] < self.size[pv]:
            self.size[pv] += self.size[pu]
            self.parent[pu] = pv
        else:
            self.size[pu] += self.size[pv]
            self.parent[pv] = pu
        
class Solution:
    def spanningTree(self, V, edges):
        heap = []
        disjointSet = UnionFind(V)
        mstSum = 0
        mst = []
        for u,v,w in edges:
            heap.append([w, u, v])
        
        heapify(heap) 
        while len(heap):
            weight, u, v = heappop(heap)
            if not disjointSet.find(u, v):
                mstSum += weight
                disjointSet.union(u, v)
                mst.append([u,v])
        print(mst)
        return mstSum
        