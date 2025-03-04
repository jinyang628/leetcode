class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 1:
            return 0
        left_max = height[0]
        right_max = height[-1]
        water = 0
        left = 0
        right = len(height) - 1
        while left < right:
            if height[left] < height[right]:
                left += 1
                left_max = max(left_max, height[left])
                water += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                water += right_max - height[right]
        return water