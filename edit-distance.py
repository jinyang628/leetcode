class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        """
        row, col = len(word1), len(word2)
        dp = [[0] * (col + 1) for _ in range(row + 1)]
        for i in range(row + 1): # delete i characters
            dp[i][0] = i
        for j in range(col + 1): # insert j characters
            dp[0][j] = j
        for i in range(1, row + 1):
            for j in range(1, col + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i][j - 1],
                        dp[i - 1][j],
                        dp[i - 1][j - 1]
                    )
        return dp[row][col]