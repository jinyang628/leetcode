from collections import defaultdict
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        track = Counter(nums)
        length = max(track.keys()) + 3
        dp = [0] * length
        maxSoFar = 0
        for i in range(2, len(dp)):
            dp[i] = max(dp[i - 1], dp[i - 2] + track[i - 2] * (i - 2))
            maxSoFar = max(maxSoFar, dp[i])        
        return maxSoFar