class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxSoFar = 0
        row, col = len(grid), len(grid[0])
        def dfs(r: int, c: int) -> int:
            if r < 0 or r >= row or c < 0 or c >= col:
                return 0
            if grid[r][c] ==  0:
                return 0
            res = 1
            grid[r][c] = 0
            res += dfs(r - 1, c) + dfs(r + 1, c) + dfs(r, c - 1) + dfs(r, c + 1)
            return res
        for i in range(row):
            for j in range(col):
                maxSoFar = max(maxSoFar, dfs(i, j))
        return maxSoFar