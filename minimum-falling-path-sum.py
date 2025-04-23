class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        row = len(matrix) + 1
        col = len(matrix[0]) + 2
        dp = [[0] * col for _ in range(row)]
        for i in range(row):
            dp[i][0] = float('inf')
        for i in range(row):
            dp[i][col - 1] = float('inf')
        for i in range(1, row):
            for j in range(1, col - 1):
                dp[i][j] = min(
                    dp[i - 1][j - 1], 
                    dp[i - 1][j], 
                    dp[i - 1][j + 1]
                ) + matrix[i - 1][j - 1]
        print(dp)
        return min(dp[row - 1])