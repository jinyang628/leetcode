class Solution:
    def rob(self, nums: List[int]) -> int:
        # res[i] = max(res[i - 1], nums[i] + res[i - 2])
        res = [0] * (len(nums) + 2)
        for i in range(2, len(nums) + 2):
            res[i] = max(res[i - 1], nums[i - 2] + res[i - 2])
        return res[-1]