1class Solution:
2    def canJump(self, nums: List[int]) -> bool:
3        last_idx = len(nums) - 1
4        for i in range(len(nums) - 2, -1, -1):
5            jump_dist = nums[i]
6            max_target = i + jump_dist
7            if max_target >= last_idx:
8                last_idx = i
910        return last_idx == 0
11