class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        row, col = len(word1) + 1, len(word2) + 1
        dp = [[0] * (col) for _ in range(row)]
        for i in range(1, row):
            dp[i][0] = i
        for j in range(1, col):
            dp[0][j] = j
        for i in range(1, row):
            for j in range(1, col):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i - 1][j - 1],
                        dp[i - 1][j],
                        dp[i][j - 1]
                    )
        return dp[-1][-1]