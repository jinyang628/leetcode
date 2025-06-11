class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        col = total * 2 + 1
        row = len(nums)
        dp = [[0] * (col + 2) for _ in range(row + 1)]
        dp[0][total + 1] =  1
        for i in range(1, row + 1):
            for j in range(1, col + 1):
                if j - nums[i - 1] >= 0:
                    dp[i][j] += dp[i - 1][j - nums[i - 1]]
                if j + nums[i - 1] < col + 2:
                    dp[i][j] += dp[i - 1][j + nums[i - 1]]
        target_idx = (total + target + 1)
        return dp[row][target_idx] if target_idx < (col + 2) else 0