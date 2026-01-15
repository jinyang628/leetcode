1class Solution:
2    def maxArea(self, height: List[int]) -> int:
3        left, right = 0, len(height) - 1
4        maxSoFar = 0
5        while left < right:
6            curr = (right - left) * min(height[left], height[right])
7            maxSoFar = max(
8                maxSoFar, 
910            )
11            if height[left] <= height[right]:
12                left += 1
13            else:
14                right -= 1
15        return maxSoFar