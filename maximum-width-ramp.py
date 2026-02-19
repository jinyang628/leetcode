1class Solution:
2    def maxWidthRamp(self, nums: List[int]) -> int:
3        stack = []
4        for i in range(len(nums)):
5            if not stack or nums[stack[-1]] > nums[i]:
6                stack.append(i)
7        maxSoFar = 0
8        for i in range(len(nums) - 1, -1, -1):
9            while stack and nums[stack[-1]] <= nums[i]:
10                maxSoFar = max(maxSoFar, i - stack[-1])
11                stack.pop()
12        return maxSoFar