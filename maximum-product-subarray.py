class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMax = nums[0]
        currMin = nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            tmpMax = currMax
            currMax = max(nums[i], tmpMax * nums[i], currMin * nums[i])
            currMin = min(nums[i], currMin * nums[i], tmpMax * nums[i])
            res = max(res, currMax)
        return res