class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left = 0
        right = len(matrix[0]) - 1
        top = 0
        down = len(matrix) - 1
        res = []
        while left <= right and top <= down:
            copy_top = top
            copy_down = down
            copy_left = left
            copy_right = right
            while left <= right:
                res.append(matrix[top][left])
                left += 1
            left = copy_left
            copy_top += 1
            top = copy_top
            if top > down:
                break
            while top <= down:
                res.append(matrix[top][right])
                top += 1
            top = copy_top
            copy_right -= 1
            right = copy_right
            if right < left:
                break
            while right >= left:
                res.append(matrix[down][right])
                right -= 1
            right = copy_right
            copy_down -= 1
            down = copy_down
            if down < top:
                break
            while down >= top:
                res.append(matrix[down][left])
                down -= 1
            down = copy_down
            copy_left += 1
            left = copy_left
        return res