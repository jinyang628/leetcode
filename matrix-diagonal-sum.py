class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        total = 0
        size = len(mat)
        if size % 2 == 1:
            total -= mat[size // 2][size // 2]
        for i in range(size):
            total += (mat[i][i] + mat[i][size - i - 1])
        return total