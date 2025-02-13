class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        def helper(arr: list[int]) -> int:
            res = [0] * (len(arr) + 2)
            for i in range(2, len(res)):
                res[i] = max(res[i - 1], res[i - 2] + arr[i - 2])
            return res[-1]
        return max(
            helper(nums[:-1]),
            helper(nums[1:])
        )