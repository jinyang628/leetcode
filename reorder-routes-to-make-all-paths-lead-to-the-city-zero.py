1class Solution:
2    def minReorder(self, n: int, connections: List[List[int]]) -> int:
3        res = [0]
4        neighbors = defaultdict(list)
5        for a, b in connections:
6            neighbors[a].append((b, False))
7            neighbors[b].append((a, True))
8        visited = set()
9        def dfs(node: int) -> None:
10            if node in visited:
11                return
12            visited.add(node)
13            for neighbor, is_inward in neighbors[node]:
14                if neighbor in visited:
15                    continue
16                if not is_inward:
17                    res[0] = res[0] + 1
18                dfs(neighbor)
1920        dfs(0)
21        return res[0]
2223