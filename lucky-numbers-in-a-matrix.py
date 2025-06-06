from collections import defaultdict
class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        row, col = len(matrix), len(matrix[0])
        mins = []
        track = defaultdict(int)
        for i in range(row):
            for j in range(col):
                track[j] = max(track[j], matrix[i][j])
            minElement = min(matrix[i])
            mins.append([minElement] * col)
        res = []
        for i in range(row):
            for j in range(col):
                if mins[i][j] == track[j]:
                    res.append(mins[i][j])
        return res