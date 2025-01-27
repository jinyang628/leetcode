class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        bottom, right = len(matrix) - 1, len(matrix[0]) - 1
        left = top = 0
        while top <= bottom:
            mid = top + (bottom - top) // 2
            if matrix[mid][0] <= target:
                if mid == len(matrix) - 1:
                    break
                if matrix[mid + 1][0] > target:
                    break
                top = mid + 1
            else:
                bottom = mid - 1
        target_row = mid
        while left <= right:
            mid = left + (right - left) // 2
            if matrix[target_row][mid] == target:
                return True
            elif matrix[target_row][mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False