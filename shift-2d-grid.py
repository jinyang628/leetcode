class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        row, col = len(grid), len(grid[0])
        res = [[0] * col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                new_col = (k + j) % col
                new_row = (((k + j) // col) + i) % row
                res[new_row][new_col] = grid[i][j]
        return res