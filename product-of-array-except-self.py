class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]
        runningProduct = 1
        for i in range(len(nums) - 1):
            runningProduct *= nums[i]
            res.append(runningProduct)
        runningProduct = 1
        for i in range(len(nums) - 2, -1, -1):
            runningProduct *= nums[i + 1]
            res[i] *= runningProduct
        return res