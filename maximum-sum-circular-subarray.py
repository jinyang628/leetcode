class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxSum = minSum = nums[0]
        currMax = currMin = total = 0
        prefixSums = []
        for num in nums:
            total += num
            currMax = max(num, currMax + num)
            maxSum = max(currMax, maxSum)
            currMin = min(num, currMin + num)
            minSum = min(currMin, minSum)
        return max(maxSum, total - minSum) if maxSum > 0 else maxSum