class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        row, col = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * (col + 1) for _ in range(row + 1)]
        dp[1][1] = 1
        for i in range(1, row + 1):
            for j in range(1, col + 1):
                if obstacleGrid[i - 1][j - 1] == 1:
                    continue
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1] + dp[i][j]
        return dp[-1][-1]