class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        res = count = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                count += 1
                res = max(res, count)
            else:
                count = 1
        count = 1
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                count += 1
                res = max(res, count)
            else:
                count = 1
        return res