class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        suffixLength = [[None] * col for _ in range(row)]
        def dfs(r: int, c: int, prev: int) -> int:
            if r < 0 or r >= row or c >= col:
                return 0 
            curr = grid[r][c]
            if curr <= prev:
                return 0
            if suffixLength[r][c] is not None:
                return suffixLength[r][c]
            best = 0
            for dr in (-1, 0, 1):
                nr, nc = dr + r, c + 1
                if 0 <= nr < row and nc < col and grid[nr][nc] > curr:
                    best = max(best, 1 + dfs(nr, nc, curr))
            suffixLength[r][c] = best
            return suffixLength[r][c]
        for r in range(row):
            dfs(r, 0, - 1)
        return max(dfs(r, 0, -1) for r in range(row))