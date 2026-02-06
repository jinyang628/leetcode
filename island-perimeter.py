1class Solution:
2    def islandPerimeter(self, grid: List[List[int]]) -> int:
3        visited = set()
4        row, col = len(grid), len(grid[0])
5        def dfs(r: int, c: int) -> int:
6            if r < 0 or r >= row or c < 0 or c >= col:
7                return 1
8            if grid[r][c] == 0:
9                return 1
10            if (r,c) in visited:
11                return 0
12            visited.add((r, c))
1314            return dfs(r - 1, c) + dfs(r + 1, c) + dfs(r, c - 1) + dfs(r, c + 1)
15        for i in range(row):
16            for j in range(col):
17                if grid[i][j] == 1:
18                    return dfs(i, j)