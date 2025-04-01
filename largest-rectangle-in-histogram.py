class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = [-1]
        for i in range(len(heights)):
            while stack[-1] != -1 and heights[i] < heights[stack[-1]]:
                height = heights[stack.pop()]
                width = i - stack[-1] -1
                res = max(res, width * height)
            stack.append(i)
        while stack[-1] != -1:
            height = heights[stack.pop()]
            width = len(heights) - stack[-1] - 1
            res = max(res, height * width)
        return res