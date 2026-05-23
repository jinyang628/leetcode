1class Solution:
2    def maximumDetonation(self, bombs: List[List[int]]) -> int:
3        neighbors = defaultdict(list) # key is index of bomb, value is indexes of bombs within its explosion radius
4        for i in range(len(bombs)):
5            xi, yi, ri = bombs[i]
6            for j in range(len(bombs)):
7                if j == i:
8                    continue
9                xj, yj, rj = bombs[j]
10                center_dist = (xj - xi) ** 2 + (yj - yi) ** 2
11                if center_dist <= (ri * ri):
12                    neighbors[i].append(j)
1314        maxSoFar = 0
15        print(neighbors)
16        def dfs(node: int) -> int:
17            if node in visited:
18                return 0
19            visited.add(node)
20            res = 1
21            for neighbor in neighbors[node]:
22                res += dfs(neighbor)
23            return res
24        for i in range(len(bombs)):
25            visited = set()
26            maxSoFar = max(maxSoFar, dfs(i))
27        return maxSoFar
28