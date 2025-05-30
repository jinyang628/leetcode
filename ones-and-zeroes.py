class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        counts = [[s.count("0"), s.count("1")] for s in strs]
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for zeros, ones in counts:
            for i in range(m, zeros - 1, -1):
                for j in range(n, ones - 1, - 1):
                    dp[i][j] = max(dp[i][j], 1 + dp[i - zeros][j - ones]) 
        return dp[-1][-1]