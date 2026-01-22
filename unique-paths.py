1class Solution:
2    def uniquePaths(self, m: int, n: int) -> int:
3        res = [[0] * n for _ in range(m)]
4        for i in range(n):
5            res[0][i] = 1
6        for i in range(m):
7            res[i][0] = 1
8        for i in range(1, m):
9            for j in range(1, n):
10                res[i][j] = res[i - 1][j] + res[i][j - 1]
11        return res[-1][-1]