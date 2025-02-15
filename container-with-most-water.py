class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        res = 0
        while left < right:
            minHeight = min(height[left], height[right])
            res = max(res, (right - left) * minHeight)
            if minHeight == height[left]:
                left += 1
            else:
                right -= 1
        return res