1class Solution:
2    def isMonotonic(self, nums: List[int]) -> bool:
3        is_increasing = is_decreasing = True
4        for i in range(len(nums) - 1):
5            if nums[i] < nums[i + 1]:
6                is_decreasing = False
7            if nums[i] > nums[i + 1]:
8                is_increasing = False
9        return is_increasing or is_decreasing
101112