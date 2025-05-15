class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        """
        top, down = 0, len(matrix) - 1
        while top < down:
            matrix[top], matrix[down] = matrix[down], matrix[top]
            top += 1
            down -= 1
        row, col = len(matrix), len(matrix[0])
        for i in range(row):
            for j in range(i + 1, col):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]