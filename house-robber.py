1class Solution:
2    def rob(self, nums: List[int]) -> int:
3        res = [0] * (len(nums) + 2)
4        for i in range(2, len(res)):
5            res[i] = max(nums[i - 2] + res[i - 2], res[i - 1])
6        return res[-1]
7