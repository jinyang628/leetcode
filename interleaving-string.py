1class Solution:
2    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
3        if len(s3) != (len(s1) + len(s2)):
4            return False
5        row, col = len(s1) + 1, len(s2) + 1
6        res = [[False] * col for _ in range(row)]
7        res[0][0] = True
8        for i in range(1, row):
9            res[i][0] = (s1[i - 1] == s3[i - 1]) and res[i - 1][0]
10        for i in range(1, col):
11            res[0][i] = (s2[i - 1] == s3[i - 1]) and res[0][i - 1]
1213        for i in range(1, row):
14            for j in range(1, col):
15                s3_idx = i + j - 1
16                res[i][j] = (res[i - 1][j] and s3[s3_idx] == s1[i - 1]) or (s3[s3_idx] == s2[j - 1] and res[i][j - 1])
17        return res[-1][-1]
1819