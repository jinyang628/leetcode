1class Solution:
2    def climbStairs(self, n: int) -> int:
3        res = [0] * (n + 1)
4        res[0] = 1
5        res[1] = 1
6        for i in range(2, n + 1):
7            res[i] = res[i - 1] + res[i - 2]
8        return res[-1]