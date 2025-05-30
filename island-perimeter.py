class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        visited = set()
        def dfs(r: int, c: int) -> int:
            if r < 0 or r >= row or c < 0 or c >= col:
                return 1
            if (r, c) in visited:
                return 0
            if grid[r][c] == 0:
                return 1
            visited.add((r, c))
            res = (
                dfs(r - 1, c) + dfs(r + 1, c) + dfs(r, c - 1) + dfs(r, c + 1)
            )
            return res
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    continue
                return dfs(i, j)
        return 0