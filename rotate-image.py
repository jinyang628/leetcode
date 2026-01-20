1class Solution:
2    def rotate(self, matrix: List[List[int]]) -> None:
3        """
45        """
6        row, col = len(matrix), len(matrix[0])
7        top, bottom = 0, row - 1
8        while top < bottom:
9            matrix[top], matrix[bottom] = matrix[bottom], matrix[top]
10            top += 1
11            bottom -= 1
12        for i in range(row):
13            for j in range(i + 1, col):
14                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
15