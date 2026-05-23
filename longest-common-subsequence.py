1class Solution:
2    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
3        row, col = len(text1) + 1, len(text2) + 1
4        dp = [[0] * col for _ in range(row)]
5        for i in range(1, row):
6            increment = False
7            for j in range(1, col):
8                if text1[i - 1] == text2[j - 1]:
9                    dp[i][j] = dp[i - 1][j - 1] + 1
10                else:
11                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
12        return dp[-1][-1]
13