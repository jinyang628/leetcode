class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        row, col = len(s1), len(s2)
        if row + col != len(s3):
            return False
        dp = [[False] * (col + 1) for _ in range(row + 1)]
        dp[0][0] = True
        for i in range(1, row + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]
        for j in range(1, col + 1):
            dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]
        for i in range(1, row + 1):
            for j in range(1, col + 1):
                match_1 = dp[i - 1][j] and s3[i + j - 1] == s1[i - 1]
                match_2 = dp[i][j - 1] and s3[i + j - 1] == s2[j - 1]
                dp[i][j] = match_1 or match_2
        return dp[row][col]