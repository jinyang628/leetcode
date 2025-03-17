class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, col = len(grid), len(grid[0])
        def dfs(r: int, c: int) -> bool:
            if r < 0 or r >= row or c < 0 or c >= col:
                return False
            if grid[r][c] == "0":
                return False
            grid[r][c] = "0"
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)
            return True
        count = 0
        for i in range(row):
            for j in range(col):
                if dfs(i, j):
                    count += 1
        return count