class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        mat = [[0] * n for _ in range(n)]
        left = top = 0
        right = bottom = n - 1
        count = 1
        while left <= right and top <= bottom:
            original_left = left
            while left <= right:
                mat[top][left] = count
                count += 1
                left += 1
            left = original_left
            top += 1
            original_top = top
            while top <= bottom:
                mat[top][right] = count
                count += 1
                top += 1
            top = original_top
            right -= 1
            original_right = right
            while right >= left:
                mat[bottom][right] = count 
                count += 1
                right -= 1
            right = original_right
            bottom -= 1
            original_bottom = bottom
            while bottom >= top:
                mat[bottom][left] = count
                count += 1
                bottom -= 1
            bottom = original_bottom
            left += 1
        return mat
        return mat