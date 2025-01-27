class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSoFar = maxEndingHere = nums[0]
        for num in nums[1:]:
            maxEndingHere = max(maxEndingHere + num, num)
            maxSoFar = max(maxSoFar, maxEndingHere)
        return maxSoFar