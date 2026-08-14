1class NumMatrix:
23    def __init__(self, matrix: List[List[int]]):
4        row, col = len(matrix), len(matrix[0])
5        prefixSums = [[0] * (col + 1) for _ in range(row + 1)]
6        for i in range(row):
7            currRowSum = 0
8            for j in range(col):
9                currRowSum += matrix[i][j]
10                above = prefixSums[i][j + 1]
11                prefixSums[i + 1][j + 1] = currRowSum + above
1213        self.prefixSums = prefixSums
1415    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
16        corner = self.prefixSums[row1][col1]
17        topRectangle = self.prefixSums[row1][col2 + 1]
18        leftRectangle = self.prefixSums[row2 + 1][col1]
19        bigRectangle = self.prefixSums[row2 + 1][col2 + 1]
20        return bigRectangle - topRectangle - leftRectangle + corner
212223# Your NumMatrix object will be instantiated and called as such:
24# obj = NumMatrix(matrix)
25# param_1 = obj.sumRegion(row1,col1,row2,col2)