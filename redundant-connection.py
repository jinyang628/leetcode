class UnionFind:
    def __init__(self, n: int):
        self.rank = [1] * n
        self.par = [i for i in range(n)]
    def find(self, a: int) -> int:
        while self.par[a] != a:
            a = self.par[a]
            self.par[a] = self.par[self.par[a]]
        return a
    def union(self, a: int, b: int):
        parent_a = self.find(a)
        parent_b = self.find(b)
        if self.rank[parent_a] >= self.rank[parent_b]:
            self.par[parent_b] = parent_a
            self.rank[parent_a] += self.rank[parent_b]
        else:
            self.par[parent_a] = parent_b
            self.rank[parent_b] += self.rank[parent_a]
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(len(edges))
        for a, b in edges:
            if uf.find(a - 1) == uf.find(b - 1):
                return [a, b]
            uf.union(a - 1, b - 1)