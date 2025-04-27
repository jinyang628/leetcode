class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        row, col = len(matrix), len(matrix[0])
        rows = [float('inf') for _ in range(row)]
        cols = [0 for _ in range(col)]
        for i in range(row):
            for j in range(col):
                curr = matrix[i][j]
                rows[i] = min(rows[i], curr)
                cols[j] = max(cols[j], curr)
        res = []
        for i in range(row):
            for j in range(col):
                curr = matrix[i][j]
                if curr == rows[i] and curr == cols[j]:
                    res.append(curr)
        return res