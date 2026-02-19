1class Solution:
2    def maxWidthRamp(self, nums: List[int]) -> int:
3        width = 0
4        stack = []
5        for i in range(len(nums)):
6            if not stack or nums[stack[-1]] > nums[i]:
7                stack.append(i)
8        print(stack)
9        for i in range(len(nums) - 1, -1, -1):
10            while stack and nums[stack[-1]] <= nums[i]:
11                idx = stack.pop()
12                width = max(width, i - idx)
13        return width
14