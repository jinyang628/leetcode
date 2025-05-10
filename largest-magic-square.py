class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        prefixSumRows = [[0] * (col + 1) for _ in range(row + 1)]
        prefixSumCols = [[0] * (col + 1) for _ in range(row + 1)]
        for i in range(1, row + 1):
            for j in range(1, col + 1):
                prefixSumCols[i][j] = prefixSumCols[i - 1][j] + grid[i - 1][j - 1]
                prefixSumRows[i][j] = prefixSumRows[i][j - 1] + grid[i - 1][j - 1]
        for size in range(min(row, col), 0, -1):
            for i in range(0, row - size + 1):
                for j in range(0, col - size + 1):
                    right_diagonal = sum(grid[c + i][c + j] for c in range(size))
                    left_diagonal = sum(grid[c + i][size - c + j - 1] for c in range(size))
                    if left_diagonal != right_diagonal:
                        continue
                    for r in range(i, i + size):
                        curr_row_sum = prefixSumRows[r + 1][j + size] - prefixSumRows[r + 1][j]
                        if left_diagonal != curr_row_sum:
                            curr_row_sum = -1
                            break
                    if curr_row_sum == -1:
                        continue 
                    for c in range(j, j + size):
                        curr_col_sum = prefixSumCols[i + size][c + 1] - prefixSumCols[i][c + 1]
                        if left_diagonal != curr_col_sum:
                            curr_col_sum = -1
                            break
                    if curr_col_sum == -1:
                        continue
                    return size
        return -1