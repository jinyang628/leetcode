class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        row, col = len(matrix), len(matrix[0])
        dp = [[None] * col for _ in range(row)]
        def dfs(r: int, c: int, prev: int) -> int:
            if r < 0 or r >= row or c < 0 or c >= col:
                return 0
            if matrix[r][c] <= prev:
                return 0
            if dp[r][c] is not None:
                return dp[r][c]
            curr = matrix[r][c]
            left = dfs(r - 1, c, curr)
            right = dfs(r + 1, c, curr)
            top = dfs(r, c - 1, curr)
            down = dfs(r, c + 1, curr)
            result = 1 + max(left, right, top, down)
            dp[r][c] = result
            return result
        for i in range(row):
            for j in range(col):
                dfs(i, j, -1)
        res = -1
        for i in range(row):
            for j in range(col):
                res = max(res, dp[i][j])
        return res