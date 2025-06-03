class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        row = len(triangle)
        dp = [[float('inf')] * row for _ in range(row)]
        dp[0][0] = triangle[0][0]
        for i in range(1, row):
            for j in range(i + 1):
                if j > 0:
                    dp[i][j] = triangle[i][j] + min(dp[i - 1][j-1], dp[i - 1][j])
                else:
                    dp[i][j] = triangle[i][j] + dp[i - 1][j]
        return min(dp[-1])