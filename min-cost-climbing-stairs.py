class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        res = [0] * (len(cost) + 1)
        for i in range(2, len(res)):
            res[i] = min(res[i - 2] + cost[i - 2], res[i - 1] + cost[i - 1])
        return res[-1]