1class Solution:
2    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
3        row, col = len(grid), len(grid[0])
4        res = 0
5        visited = set()
67        def bfs(r: int, c: int) -> int:
8            if r < 0 or r >= row or c < 0 or c >= col:
9                return 0
10            if (r, c) in visited:
11                return 0
12            if grid[r][c] == 0:
13                return 0
14            visited.add((r, c))
15            return 1 + bfs(r - 1, c) + bfs(r + 1, c) + bfs(r, c - 1) + bfs(r, c + 1)
1617        for i in range(row):
18            for j in range(col):
19                if grid[i][j] == 1 and (i, j) not in visited:
20                    res = max(res, bfs(i, j))
2122        return res