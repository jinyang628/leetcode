class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # i = j -> 1 + lcs(i - 1, j - 1)
        # i != j -> max(lcs(i - 1, j), lcs(i, j - 1))
        row = len(text1)
        col = len(text2)
        res = [[0] * col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                if text1[i] == text2[j]:
                    if i == 0 or j == 0:
                        res[i][j] = 1
                    else:
                        res[i][j] = res[i - 1][j - 1] + 1
                else:
                    res[i][j] = max(res[i - 1][j], res[i][j - 1])
        return res[row - 1][col - 1]