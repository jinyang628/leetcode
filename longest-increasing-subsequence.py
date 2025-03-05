class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        res = [1] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            curr = nums[i]
            for j in range(i + 1, len(nums)):
                if curr >= nums[j]:
                    continue
                res[i] = max(res[i], 1 + res[j])
        return max(res)