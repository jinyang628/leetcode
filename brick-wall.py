1class Solution:
2    def leastBricks(self, wall: List[List[int]]) -> int:    
3        rows = len(wall)
4        edges = [[] for _ in range(rows)]
5        counter = Counter()
6        print(edges)
7        minSoFar = float('inf')
8        for idx, row in enumerate(wall):
9            prefixSum = 0
10            minSoFar = min(minSoFar, row[0])
11            for brick in row:
12                prefixSum += brick
13                edges[idx].append(prefixSum)
14        for row in edges:
15            for edge in row[:-1]:
16                counter[edge] += 1
17        if not counter:
18            return rows
19        return rows - max(counter.values())