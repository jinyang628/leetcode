class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        def dfs(r: int, c: int) -> int:
            if r < 0 or r >= row or c < 0 or c >= col:
                return 0
            if not grid[r][c]:
                return 0
            grid[r][c] = 0
            return 1 + dfs(r - 1, c) + dfs(r + 1, c) + dfs(r, c - 1) + dfs(r, c + 1)
        res = 0
        for i in range(row):
            dfs(i, 0)
            dfs(i, col - 1)
        for i in range(col):
            dfs(0, i)
            dfs(row - 1, i) 
        for i in range(1, row - 1):
            for j in range(1, col - 1):
                if grid[i][j]:
                    res += dfs(i, j)
        return res