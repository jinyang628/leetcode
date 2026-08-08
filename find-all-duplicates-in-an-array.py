1class Solution:
2    def findDuplicates(self, nums: List[int]) -> List[int]:
3        res = []
4        for i in range(len(nums)):
5            idx = abs(nums[i]) - 1
6            if nums[idx] < 0:
7                res.append(abs(nums[i]))
8            nums[idx] = -nums[idx]
9        return res