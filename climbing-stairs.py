class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        res = [0] * (n + 1)
        res[0] = 1
        res[1] = 1
        for i in range(2, len(res)):
            res[i] = res[i - 2] + res[i - 1]
        return res[-1]