class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        row, col = len(triangle), len(triangle[-1])
        dp = [[float('inf')] * (col + 1) for _ in range(row)]
        dp[0][1] = triangle[0][0]
        for i in range(1, row):
            for j in range(1, i + 2):
                dp[i][j] = triangle[i][j - 1] + min(
                    dp[i - 1][j],
                    dp[i - 1][j - 1]
                )
        return min(dp[-1])