1class Solution:
2    def diagonalSum(self, mat: List[List[int]]) -> int:
3        row = col = len(mat)
4        total = 0
5        if row % 2 == 1:
6            total -= mat[row // 2][col // 2]
7        for i in range(row):
8            total += mat[i][i]
9            total += mat[i][row - i - 1]
10        return total
11