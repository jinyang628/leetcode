from collections import defaultdict
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        dp = [1] + nums + [1]
        track = defaultdict(int)
        def dfs(l: int, r: int):
            if l > r:
                return 0
            if (l, r) in track:
                return track[(l, r)]
            for i in range(l, r + 1):
                counts = dp[l - 1] * dp[r + 1] * dp[i]
                track[(l, r)] = max(
                    counts + dfs(l, i - 1) + dfs(i + 1, r),
                    track[(l, r)]
                )
            return track[(l, r)]
        return dfs(1, len(nums))