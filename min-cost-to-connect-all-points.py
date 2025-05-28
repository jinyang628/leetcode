import math
class UnionFind: 
    def __init__(self, n: int):
        self.parents = [i for i in range(n)]
        self.rank = [1] * n
    def find(self, a: int) -> int:
        while self.parents[a] != a:
            tmp = self.parents[a]
            self.parents[a] = self.parents[tmp]
            a = tmp
        return a
    def union(self, a: int, b: int):
        if self.rank[a] <= self.rank[b]:
            self.rank[b] += self.rank[a]
            self.parents[self.find(a)] = self.find(b)
        else:
            self.rank[a] += self.rank[b]
            self.parents[self.find(b)] = self.find(a)
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def getDist(a: list[int], b: list[int]) -> int:
            return abs(a[0] - b[0]) + abs(a[1] - b[1])
        uf = UnionFind(len(points))
        edges = []
        for i in range(len(points) - 1):
            for j in range(i + 1, len(points)):
                edges.append((
                    getDist(points[i], points[j]),
                    i,
                ))
        edges.sort()
        total = 0
        for dist, a, b in edges:
            if uf.rank[0] == len(points):
                break
            if uf.find(a) == uf.find(b):
                continue 
            uf.union(a, b)
            total += dist
        return total