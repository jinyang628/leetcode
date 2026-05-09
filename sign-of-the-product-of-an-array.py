class Solution:
    def arraySign(self, nums: List[int]) -> int:
        if 0 in nums:
            return 0
        prod = list(accumulate(nums, lambda x, y: x * y))
        return 1 if prod[-1] > 0 else -1