class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left = top = 0
        right = len(matrix[0]) - 1
        bottom = len(matrix) - 1
        res = []
        while left <= right and top <= bottom:
            original_left = left
            while left <= right:
                res.append(matrix[top][left])
                left += 1
            left = original_left
            top += 1
            original_top = top
            while top <= bottom:
                res.append(matrix[top][right])
                top += 1
            top = original_top
            right -= 1
            original_right = right
            if not left <= right or not top <= bottom:
                break
            while right >= left:
                res.append(matrix[bottom][right])
                right -= 1
            right = original_right
            bottom -= 1
            original_bottom = bottom
            while bottom >= top:
                res.append(matrix[bottom][left])
                bottom -= 1
            bottom = original_bottom
            left += 1
        return res