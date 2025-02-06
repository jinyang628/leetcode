class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        res = nums[0]
        negativeProductSoFar = nums[0]
        positiveProductSoFar = nums[0]
        for num in nums[1:]:
            if num < 0:
                negativeProductSoFar, positiveProductSoFar = positiveProductSoFar, negativeProductSoFar
            negativeProductSoFar = min(num, negativeProductSoFar * num)
            positiveProductSoFar = max(num, positiveProductSoFar * num)
            res = max(res, positiveProductSoFar)
        return res