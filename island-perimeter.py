class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        visited = set()
        def dfs(r: int, c: int) -> int:
            if r < 0 or r >= row or c < 0 or c >= col:
                return 1
            if not grid[r][c]:
                return 1
            if (r,c) in visited:
                return 0
            visited.add((r, c))   
            left = dfs(r - 1, c) 
            right = dfs(r + 1, c) 
            top = dfs(r, c - 1) 
            down = dfs(r, c + 1)
            return left + right + top + down
        for i in range(row):
            for j in range(col):
                if grid[i][j]:
                    return dfs(i, j)