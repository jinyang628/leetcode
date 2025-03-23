from collections import defaultdict
class Solution:
    def minCost(self, nums: List[int], k: int) -> int:
        dp = {}
        def helper(start: int) -> int:
            if start >= len(nums):
                return 0
            if start in dp:
                return dp[start]
            track = defaultdict(int)
            importance_value = 0
            min_cost = float('inf')
            for end in range(start, len(nums)):
                track[nums[end]] += 1
                if track[nums[end]] == 2:
                    importance_value += 2
                elif track[nums[end]] > 2:
                    importance_value += 1
                if importance_value > min_cost:
                    break
                min_cost = min(min_cost, importance_value + k + helper(end + 1))
            dp[start] = min_cost
            return dp[start]
        return helper(0)