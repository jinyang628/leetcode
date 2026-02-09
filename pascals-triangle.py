1class Solution:
2    def generate(self, numRows: int) -> List[List[int]]:
3        if numRows == 1:
4            return [[1]]
5        if numRows == 2:
6            return [[1], [1,1]]
7        res = [[1], [1, 1]]
8        for i in range(2, numRows):
9            new_row = [1]
10            for j in range(i - 1):
11                new_row.append(res[i-1][j] + res[i-1][j+ 1])
12            new_row.append(1)
13            res.append(new_row)
14        return res