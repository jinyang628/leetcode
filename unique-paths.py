1class Solution:
2    def uniquePaths(self, m: int, n: int) -> int:
3        dp = [[0] * (n + 1) for _ in range(m + 1)]
4        dp[0][1] = 1
5        for i in range(1, m + 1):
6            for j in range(1, n + 1):
7                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
8        return dp[-1][-1]