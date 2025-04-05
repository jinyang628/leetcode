class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # res[i][j] = min(res[i-1][j], res[i][j-1]) + grid[i][j]
        # 1 3 1
        # 1 5 1
        # 4 2 1
        row, col = len(grid), len(grid[0])
        res = [[0] * col for _ in range(row)]
        res[0][0] = grid[0][0]
        for i in range(1, row):
            res[i][0] = grid[i][0] + res[i - 1][0]
        for i in range(1, col):
            res[0][i] = grid[0][i] + res[0][i - 1]
        for i in range(1, row):
            for j in range(1, col):
                res[i][j] = min(res[i-1][j], res[i][j-1]) + grid[i][j]
        print(res)
        return res[-1][-1]