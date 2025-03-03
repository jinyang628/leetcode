class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum = sum(nums)
        if target > total_sum or target < -total_sum:
            return 0
        col = 2 * total_sum + 1
        row = len(nums)
        dp = [[0] * col for _ in range(row)]
        mid = col // 2
        dp[0][mid + nums[0]] += 1
        dp[0][mid - nums[0]] += 1
        for i in range(row - 1):
            for j in range(col):
                if not dp[i][j]:
                    continue
                curr = nums[i + 1]
                dp[i + 1][j + curr] += dp[i][j]
                dp[i + 1][j - curr] += dp[i][j]
        res = dp[-1][mid + target]
        print(dp)
        return res