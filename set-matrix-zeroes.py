class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        """
        top_left_row_is_zero = False
        row, col = len(matrix), len(matrix[0])
        for i in range(col):
            if matrix[0][i] == 0:
                top_left_row_is_zero = True
                break
        for i in range(row):
            if matrix[i][0] == 0:
                matrix[0][0] = 0
                break
        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if matrix[0][0] == 0:
            for i in range(row):
                matrix[i][0] = 0
        if top_left_row_is_zero:
            for i in range(col):
                matrix[0][i] = 0