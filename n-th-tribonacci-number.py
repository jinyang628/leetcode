1class Solution:
2    def tribonacci(self, n: int) -> int:
3        dp = [0, 1, 1]
4        for i in range(3, n + 1):
5            dp.append(
6                dp[-1] + dp[-2] + dp[-3]
7            )
8        return dp[n]