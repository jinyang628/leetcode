class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = [(1, 1)] * len(nums) # length, number adding up to the length
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[i][0] > dp[j][0] + 1:
                        continue
                    elif dp[i][0] == dp[j][0] + 1:
                        dp[i] = (dp[i][0], dp[i][1] + dp[j][1])
                    else:
                        dp[i] = (dp[j][0] + 1, dp[j][1])
        maxSoFar, res = 0, 0
        for length, number in dp:
            if length > maxSoFar:
                maxSoFar = length
                res = number
            elif length == maxSoFar:
                res += number
        return res