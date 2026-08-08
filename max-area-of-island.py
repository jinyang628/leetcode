1class Solution:
2    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
3        row, col = len(grid), len(grid[0])
4        res = 0
5        def dfs(r: int, c: int) -> int:
6            if r < 0 or r >= row or c < 0 or c >= col:
7                return 0
8            if grid[r][c] == 0:
9                return 0
10            grid[r][c] = 0
11            return 1 + dfs(r - 1, c) + dfs(r + 1, c) + dfs(r, c - 1) + dfs(r, c + 1)
12        for i in range(row):
13            for j in range(col):
14                if grid[i][j] == 1:
15                    res = max(res, dfs(i, j))
16        return res
1718