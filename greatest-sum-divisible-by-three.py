class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [0, 0, 0]
        for num in nums:
            for sumSoFar in dp[:]:
                sumSoFar += num
                remainder = sumSoFar % 3
                dp[remainder] = max(sumSoFar, dp[remainder])
        return dp[0]