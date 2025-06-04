class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        def getIslandSize(r: int, c: int) -> int:
            if r < 0 or c < 0 or r >= row or c >= col:
                return 0
            if grid[r][c] == 0 or grid[r][c] == -1:
                return 0
            grid[r][c] = -1
            return 1 + getIslandSize(r - 1, c) + getIslandSize(r + 1, c) + getIslandSize(r, c - 1) + getIslandSize(r, c + 1) 
        res = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == -1:
                    continue
                res = max(res, getIslandSize(i, j))
        return res