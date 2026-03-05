1class Solution:
2    def pivotIndex(self, nums: List[int]) -> int:
3        left_sum = 0
4        right_sum = sum(nums) - nums[0]
5        idx = 0
6        while idx < len(nums):
7            if left_sum == right_sum:
8                return idx
9            idx += 1
10            left_sum += nums[idx - 1]
11            if idx == len(nums):
12                break
13            right_sum -= nums[idx]
14        return -1
15