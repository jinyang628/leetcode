class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        row, col = len(matrix), len(matrix[0])
        total = num_negative = 0
        min_abs = float('inf')
        for i in range(row):
            for j in range(col):
                mid = matrix[i][j]
                total += abs(mid)
                if mid < 0:
                    num_negative += 1
                min_abs = min(min_abs, abs(mid))
        if num_negative % 2:
            total -= min_abs * 2
        return total